#!/usr/bin/env python3
"""
Review Engine for KORRO Research v2.
Automatic flagging before export: unsupported claims, missing sections, repeated paragraphs,
weak transitions, vague novelty, missing ethics, missing limitations, formatting violations.

Usage:
    python review_engine.py paper.md
    python review_engine.py paper.md --venue neurips
    python review_engine.py paper.md --json
    python review_engine.py paper.md --batch paper1.md paper2.md
    python review_engine.py paper.md --check   # dry-run
    python review_engine.py --help
"""

import argparse
import json
import re
import sys
from pathlib import Path


VENUE_RULES = {
    'neurips': {
        'required_sections': ['abstract', 'introduction', 'related work', 'method', 'experiments', 'conclusion'],
        'required_elements': ['ethics statement', 'limitations', 'reproducibility', 'broader impact'],
        'max_pages': 9,
        'anonymous': True,
    },
    'icml': {
        'required_sections': ['abstract', 'introduction', 'related work', 'method', 'experiments', 'conclusion'],
        'required_elements': ['ethics statement', 'reproducibility'],
        'max_pages': 8,
        'anonymous': True,
    },
    'cvpr': {
        'required_sections': ['abstract', 'introduction', 'related work', 'method', 'experiments', 'conclusion'],
        'required_elements': ['supplementary material', 'acknowledgements'],
        'max_pages': 8,
        'anonymous': False,
    },
    'acl': {
        'required_sections': ['abstract', 'introduction', 'related work', 'method', 'experiments', 'conclusion'],
        'required_elements': ['limitations', 'ethics statement', 'acknowledgements'],
        'max_pages': 8,
        'anonymous': True,
    },
    'generic': {
        'required_sections': ['abstract', 'introduction', 'related work', 'method', 'experiments', 'conclusion'],
        'required_elements': ['limitations', 'ethics statement'],
    },
}

WEAK_PATTERNS = [
    (re.compile(r'could potentially', re.IGNORECASE), 'hedging'),
    (re.compile(r'may allow', re.IGNORECASE), 'hedging'),
    (re.compile(r'might be able to', re.IGNORECASE), 'hedging'),
    (re.compile(r'it is (worth noting|important to mention|interesting to note)', re.IGNORECASE), 'filler'),
    (re.compile(r'(significantly|substantially|dramatically)\s+(improves?|outperforms?)', re.IGNORECASE), 'unquantified_claim'),
    (re.compile(r'(novel|first|new|original|unprecedented)', re.IGNORECASE), 'novelty_claim'),
]


def check_sections(text: str, required: list[str]) -> list[str]:
    missing = []
    for section in required:
        pattern = re.compile(rf'#{{1,3}}\s*{re.escape(section)}', re.IGNORECASE)
        if not pattern.search(text):
            missing.append(section)
    return missing


def check_elements(text: str, required: list[str]) -> list[str]:
    missing = []
    for element in required:
        if element.lower() not in text.lower():
            missing.append(element)
    return missing


def find_weak_claims(text: str) -> list[dict]:
    issues = []
    lines = text.split('\n')
    for i, line in enumerate(lines, 1):
        for pattern, issue_type in WEAK_PATTERNS:
            for match in pattern.finditer(line):
                issues.append({
                    'line': i,
                    'text': line.strip()[:200],
                    'matched': match.group(0),
                    'issue': issue_type,
                    'severity': 'high' if issue_type == 'unquantified_claim' else 'medium',
                })
    return issues


def find_repeated_paragraphs(text: str) -> list[dict]:
    paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 50]
    seen = {}
    duplicates = []
    for i, para in enumerate(paragraphs):
        key = para[:80].lower()
        if key in seen:
            duplicates.append({'text': para[:200], 'first_seen': i, 'repeat': seen[key][1]})
        else:
            seen[key] = (para, i)
    return duplicates


def check_anonymity(text: str, required: bool) -> list[dict]:
    if not required:
        return []
    issues = []
    author_pattern = re.compile(r'author|affiliation|university of|institute of', re.IGNORECASE)
    for match in author_pattern.finditer(text):
        issues.append({'text': match.group(0), 'issue': 'potential_author_info', 'severity': 'critical'})
    return issues


def review_document(filepath: str, venue: str = 'generic') -> dict:
    path = Path(filepath)
    if not path.exists():
        return {'error': f'File not found: {filepath}', 'file': filepath}

    text = path.read_text(encoding='utf-8')
    rules = VENUE_RULES.get(venue, VENUE_RULES['generic'])

    missing_sections = check_sections(text, rules['required_sections'])
    missing_elements = check_elements(text, rules.get('required_elements', []))
    weak_claims = find_weak_claims(text)
    duplicates = find_repeated_paragraphs(text)
    anon_issues = check_anonymity(text, rules.get('anonymous', False))

    total_issues = len(missing_sections) + len(missing_elements) + len(weak_claims) + len(duplicates) + len(anon_issues)

    return {
        'file': filepath,
        'venue': venue,
        'total_issues': total_issues,
        'missing_sections': missing_sections,
        'missing_elements': missing_elements,
        'weak_claims': weak_claims,
        'duplicate_paragraphs': len(duplicates),
        'anonymity_issues': len(anon_issues),
        'passed': total_issues == 0,
        'suggestions': [],
        'summary': f'{total_issues} issues found. {"All checks passed." if total_issues == 0 else "Fix required before submission."}',
    }


def main():
    parser = argparse.ArgumentParser(
        description='Review Engine - automatic pre-export flagging',
        epilog='KORRO Research v2 - No paper leaves unreviewed.',
    )
    parser.add_argument('files', nargs='+', help='Markdown files to review')
    parser.add_argument('--venue', default='generic',
                       choices=['neurips', 'icml', 'cvpr', 'acl', 'emccv', 'iccv', 'generic'],
                       help='Target venue for format-specific checks')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--batch', action='store_true', help='Batch mode')
    parser.add_argument('--check', action='store_true', help='Dry-run')
    parser.add_argument('--offline', action='store_true', help='Skip online checks')

    args = parser.parse_args()

    if args.check:
        for f in args.files:
            print(f'[DRY-RUN] Would review: {f} for venue: {args.venue}')
        return

    results = []
    for filepath in args.files:
        result = review_document(filepath, venue=args.venue)
        results.append(result)

        if args.json:
            continue

        if not args.batch:
            print(f'\n=== {filepath} === [Venue: {args.venue}]')
            print(f'Total issues: {result["total_issues"]}')
            if result['missing_sections']:
                print(f'  Missing sections: {", ".join(result["missing_sections"])}')
            if result['missing_elements']:
                print(f'  Missing elements: {", ".join(result["missing_elements"])}')
            if result['weak_claims']:
                print(f'  Weak/vague claims: {len(result["weak_claims"])}')
            if result['duplicate_paragraphs']:
                print(f'  Duplicate paragraphs: {result["duplicate_paragraphs"]}')
            if result.get('anonymity_issues'):
                print(f'  Anonymity issues: {result["anonymity_issues"]}')
            print(f'PASS: {"YES" if result["passed"] else "NO - Issues found!"}')

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))

    has_issues = any(not r.get('passed', False) for r in results)
    if has_issues:
        sys.exit(1)


if __name__ == '__main__':
    main()
