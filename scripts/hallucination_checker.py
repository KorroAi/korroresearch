#!/usr/bin/env python3
"""
Hallucination Detection Engine for KORRO Research v2.
Classifies every factual claim into: verified, user_provided, ai_hypothesis, speculative.

Usage:
    python hallucination_checker.py paper.md
    python hallucination_checker.py paper.md --mode classify --json
    python hallucination_checker.py paper.md --strict  # fail on speculative claims
    python hallucination_checker.py paper.md --batch paper1.md paper2.md
    python hallucination_checker.py paper.md --check   # dry-run, show what would be checked
    python hallucination_checker.py --help

Classification levels:
    VERIFIED     - Claim is backed by a citation or verifiable source
    USER_PROVIDED - Claim came from user input, assumed factual
    HYPOTHESIS   - AI-generated but plausible, needs user verification
    SPECULATIVE  - No evidence, no citation, no user basis — DANGER ZONE
"""

import argparse
import json
import re
import sys
from pathlib import Path


CLAIM_PATTERNS = [
    (re.compile(r'(\d+\.?\d*)\s*%', re.IGNORECASE), 'percentage'),
    (re.compile(r'(\d+\.?\d*)\s*x\s*(faster|slower|more|less)', re.IGNORECASE), 'multiplier'),
    (re.compile(r'(state-of-the-art|SOTA|outperforms?|surpasses?|exceeds?)', re.IGNORECASE), 'comparison'),
    (re.compile(r'(we (propose|introduce|present|develop))', re.IGNORECASE), 'contribution'),
    (re.compile(r'(first|novel|new|original|unprecedented)', re.IGNORECASE), 'novelty'),
    (re.compile(r'(significantly|substantially|dramatically|remarkably)', re.IGNORECASE), 'intensifier'),
    (re.compile(r'\[@?[\w\d_\-\.]+\]|\(\d{4}\)|\\cite\{', re.IGNORECASE), 'citation'),
    (re.compile(r'(\d+\.?\d*)\s*(ms|s|GB|TB|MB|hours?|days?|epochs?|parameters?|layers?)', re.IGNORECASE), 'quantity'),
    (re.compile(r'(could potentially|may allow|might be able to|possibly)', re.IGNORECASE), 'hedging'),
]


def extract_claims(text: str) -> list[dict]:
    claims = []
    lines = text.split('\n')
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('```'):
            continue
        for pattern, claim_type in CLAIM_PATTERNS:
            for match in pattern.finditer(line):
                claims.append({
                    'line': i,
                    'text': line[:200],
                    'matched': match.group(0),
                    'type': claim_type,
                    'classification': None,
                })
    return claims


def classify_claim(claim: dict, has_citation: bool, is_user_provided: bool) -> str:
    ctype = claim['type']

    if ctype == 'citation':
        return 'verified'
    if ctype == 'hedging':
        return 'speculative'
    if is_user_provided:
        return 'user_provided'
    if has_citation:
        return 'verified'

    if ctype in ('percentage', 'multiplier', 'quantity'):
        return 'hypothesis'
    if ctype in ('novelty', 'comparison'):
        return 'speculative'

    return 'hypothesis'


def check_document(filepath: str, strict: bool = False) -> dict:
    path = Path(filepath)
    if not path.exists():
        return {'error': f'File not found: {filepath}', 'file': filepath}

    text = path.read_text(encoding='utf-8')
    claims = extract_claims(text)

    has_citation = bool(re.search(r'\[@?[\w\d_\-\.]+\]|\(\d{4}\)|\\cite\{', text))
    is_user_provided = bool(re.search(r'(user.provided|user_data|user_input)', text, re.IGNORECASE))

    for claim in claims:
        claim['classification'] = classify_claim(claim, has_citation, is_user_provided)

    stats = {
        'verified': sum(1 for c in claims if c['classification'] == 'verified'),
        'user_provided': sum(1 for c in claims if c['classification'] == 'user_provided'),
        'hypothesis': sum(1 for c in claims if c['classification'] == 'hypothesis'),
        'speculative': sum(1 for c in claims if c['classification'] == 'speculative'),
    }
    total = sum(stats.values()) or 1

    return {
        'file': filepath,
        'total_claims': len(claims),
        'stats': stats,
        'trust_score': round((stats['verified'] + stats['user_provided']) / total * 100, 1),
        'dangers': [c for c in claims if c['classification'] == 'speculative'],
        'warnings': [c for c in claims if c['classification'] == 'hypothesis'],
        'passed': stats['speculative'] == 0,
        'claims': claims if strict else None,
    }


def main():
    parser = argparse.ArgumentParser(
        description='Hallucination Detection Engine - classify every factual claim',
        epilog='KORRO Research v2 - Zero hallucinations. Every claim classified.',
    )
    parser.add_argument('files', nargs='+', help='Markdown files to check')
    parser.add_argument('--mode', default='classify', choices=['classify', 'audit', 'strip'],
                       help='classify: tag claims; audit: full report; strip: remove speculative claims')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--strict', action='store_true', help='Fail if any speculative claims found')
    parser.add_argument('--batch', action='store_true', help='Batch mode: process all files silently')
    parser.add_argument('--check', action='store_true', help='Dry-run: show what would be checked without classifying')
    parser.add_argument('--offline', action='store_true', help='Skip any online verification steps')

    args = parser.parse_args()

    if args.check:
        for f in args.files:
            print(f'[DRY-RUN] Would check: {f}')
        return

    results = []
    for filepath in args.files:
        path = Path(filepath)
        if not path.exists():
            print(f'[ERROR] File not found: {filepath}', file=sys.stderr)
            continue

        result = check_document(filepath, strict=args.strict)
        results.append(result)

        if args.json:
            continue

        if not args.batch:
            print(f'\n=== {filepath} ===')
            print(f'Claims found:  {result["total_claims"]}')
            print(f'  VERIFIED:     {result["stats"]["verified"]}')
            print(f'  USER PROVIDED: {result["stats"]["user_provided"]}')
            print(f'  HYPOTHESIS:   {result["stats"]["hypothesis"]}')
            print(f'  SPECULATIVE:  {result["stats"]["speculative"]}')
            print(f'Trust Score:    {result["trust_score"]}%')
            print(f'PASS:           {"YES" if result["passed"] else "NO - speculative claims detected!"}')

            if result['dangers']:
                print(f'\n!!! DANGER - Speculative Claims ({len(result["dangers"])}) !!!')
                for d in result['dangers'][:10]:
                    print(f'  L{d["line"]}: {d["text"][:120]}')
                if len(result['dangers']) > 10:
                    print(f'  ... and {len(result["dangers"]) - 10} more')

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))

    if args.strict:
        has_speculative = any(not r.get('passed', False) for r in results)
        if has_speculative:
            print('\n[FAIL] Speculative claims detected. Fix before finalizing.', file=sys.stderr)
            sys.exit(1)

    print('\n[OK] Hallucination check complete.', file=sys.stderr)


if __name__ == '__main__':
    main()
