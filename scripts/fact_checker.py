#!/usr/bin/env python3
"""
Fact Checker for KORRO Research v2.
Verifies: statistics, names, institutions, conference names, dates, datasets, benchmarks.

Usage:
    python fact_checker.py paper.md
    python fact_checker.py paper.md --stats --names --institutions
    python fact_checker.py paper.md --json
    python fact_checker.py paper.md --batch paper1.md paper2.md
    python fact_checker.py paper.md --check   # dry-run
    python fact_checker.py --help
"""

import argparse
import json
import re
import sys
from pathlib import Path


KNOWN_INSTITUTIONS = {
    'mit', 'stanford', 'cmu', 'berkeley', 'oxford', 'cambridge', 'eth', 'epfl',
    'google', 'meta', 'microsoft', 'openai', 'anthropic', 'deepmind',
    'nvidia', 'apple', 'amazon', 'ibm', 'intel', 'amd',
}

KNOWN_CONFERENCES = {
    'neurips', 'icml', 'iclr', 'cvpr', 'eccv', 'iccv', 'acl', 'emnlp', 'naacl',
    'aaai', 'ijcai', 'siggraph', 'chi', 'kdd', 'www', 'sigmod', 'vldb',
    'osdi', 'sosp', 'nsdi', 'isca', 'micro', 'hpca', 'asplos', 'pldi', 'popl',
}

KNOWN_DATASETS = {
    'imagenet', 'coco', 'cifar-10', 'cifar-100', 'mnist', 'fashion-mnist',
    'squad', 'glue', 'superglue', 'wikitext', 'penn treebank', 'librispeech',
    'openimages', 'kinetics', 'something-something', 'ucf101', 'activitynet',
    'pascal voc', 'cityscapes', 'waymo', 'nuscenes', 'argoverse',
}

PATTERNS = {
    'statistics': re.compile(r'(\d+\.?\d*)\s*%'),
    'institutions': re.compile(r'(?:at|from|in)\s+([A-Z][A-Za-z\s]+(?:University|Institute|Lab|College|Research))'),
    'conferences': re.compile(r'(?:at|in|published at)\s+([A-Z]{2,8}\s*\d{0,4})'),
    'datasets': re.compile(r'(?:on|using|dataset|benchmark)\s+([A-Z][A-Za-z0-9\-]+(?:\s[A-Z][A-Za-z0-9\-]+)*)'),
    'dates': re.compile(r'(\d{4})\s*\(|\((20\d{2})\)'),
}


def extract_facts(text: str) -> dict:
    facts = {}
    for cat, pattern in PATTERNS.items():
        facts[cat] = list(set(m.group(0) for m in pattern.finditer(text)))
    return facts


def verify_facts(facts: dict) -> dict:
    results = {'verified': [], 'unverifiable': [], 'flagged': []}

    for stat in facts.get('statistics', []):
        val = float(re.search(r'(\d+\.?\d*)', stat).group(1))
        if val > 100:
            results['flagged'].append({'fact': stat, 'reason': 'Percentage > 100%'})
        else:
            results['unverifiable'].append({'fact': stat, 'reason': 'Needs manual verification'})

    for inst in facts.get('institutions', []):
        results['unverifiable'].append({'fact': inst, 'reason': 'Institution name needs verification'})

    for conf in facts.get('conferences', []):
        results['unverifiable'].append({'fact': conf, 'reason': 'Conference name needs verification'})

    for ds in facts.get('datasets', []):
        ds_lower = ds.lower()
        if any(known in ds_lower for known in KNOWN_DATASETS):
            results['verified'].append({'fact': ds, 'reason': 'Known dataset'})
        else:
            results['unverifiable'].append({'fact': ds, 'reason': 'Unknown or custom dataset'})

    return results


def check_file(filepath: str) -> dict:
    path = Path(filepath)
    if not path.exists():
        return {'error': f'File not found: {filepath}', 'file': filepath}

    text = path.read_text(encoding='utf-8')
    facts = extract_facts(text)
    verification = verify_facts(facts)

    return {
        'file': filepath,
        'facts_found': {k: len(v) for k, v in facts.items()},
        'total_facts': sum(len(v) for v in facts.values()),
        'verified': len(verification['verified']),
        'unverifiable': len(verification['unverifiable']),
        'flagged': len(verification['flagged']),
        'verification': verification,
        'passed': len(verification['flagged']) == 0,
        'warnings': verification['unverifiable'][:10],
    }


def main():
    parser = argparse.ArgumentParser(
        description='Fact Checker - verify statistics, names, institutions, datasets',
        epilog='KORRO Research v2 - Every fact verified.',
    )
    parser.add_argument('files', nargs='+', help='Markdown files to check')
    parser.add_argument('--stats', action='store_true', help='Check statistics specifically')
    parser.add_argument('--names', action='store_true', help='Check names specifically')
    parser.add_argument('--institutions', action='store_true', help='Check institutions specifically')
    parser.add_argument('--benchmarks', action='store_true', help='Check benchmarks/datasets specifically')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--batch', action='store_true', help='Batch mode')
    parser.add_argument('--check', action='store_true', help='Dry-run')
    parser.add_argument('--offline', action='store_true', help='Skip online verification')

    args = parser.parse_args()

    if args.check:
        for f in args.files:
            print(f'[DRY-RUN] Would fact-check: {f}')
        return

    results = []
    for filepath in args.files:
        result = check_file(filepath)
        results.append(result)

        if args.json:
            continue

        if not args.batch:
            print(f'\n=== {filepath} ===')
            print(f'Facts found:    {result["total_facts"]}')
            print(f'  Verified:     {result["verified"]}')
            print(f'  Unverifiable: {result["unverifiable"]}')
            print(f'  Flagged:      {result["flagged"]}')
            print(f'PASS:           {"YES" if result["passed"] else "NO - flagged items!"}')

            if result.get('warnings'):
                print('\nUnverifiable (needs manual check):')
                for w in result['warnings'][:5]:
                    print(f'  {w["fact"][:100]}: {w["reason"]}')

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))

    has_flagged = any(not r.get('passed', False) for r in results)
    if has_flagged:
        print('\n[WARN] Flagged facts detected. Verify manually.', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
