
#!/usr/bin/env python3
"""
Reproducibility Checklist for KORRO Research v2.
Generates conference-required reproducibility checklist including:
dataset, code, hardware, training hours, random seed, license, ethics.

Usage:
    python reproducibility_checklist.py paper.md
    python reproducibility_checklist.py paper.md --json
    python reproducibility_checklist.py paper.md --check   # dry-run
    python reproducibility_checklist.py --help
"""

import argparse
import json
import re
import sys
from pathlib import Path


CHECKLIST_ITEMS = [
    {
        'id': 'dataset',
        'question': 'Dataset source, splits, and preprocessing described?',
        'required': True,
        'regex': re.compile(r'(dataset|data|split|preprocess)', re.IGNORECASE),
    },
    {
        'id': 'code',
        'question': 'Code repository and license provided?',
        'required': True,
        'regex': re.compile(r'(github|gitlab|code|repository|open.source|license)', re.IGNORECASE),
    },
    {
        'id': 'hardware',
        'question': 'Hardware specified (GPU model, CPU, RAM)?',
        'required': True,
        'regex': re.compile(r'(GPU|CPU|RAM|hardware|A100|V100|H100|RTX|TPU)', re.IGNORECASE),
    },
    {
        'id': 'training_time',
        'question': 'Training time and number of runs reported?',
        'required': True,
        'regex': re.compile(r'(training.time|hours?|days?|epochs?|runs?|seeds?)', re.IGNORECASE),
    },
    {
        'id': 'random_seed',
        'question': 'Random seed(s) specified?',
        'required': True,
        'regex': re.compile(r'(random.seed|seed\s*=\s*\d+|seeds\s*\d+)', re.IGNORECASE),
    },
    {
        'id': 'license',
        'question': 'License for code and dataset?',
        'required': True,
        'regex': re.compile(r'(license|MIT|Apache|BSD|GPL)', re.IGNORECASE),
    },
    {
        'id': 'ethics',
        'question': 'Ethics statement and limitations discussed?',
        'required': True,
        'regex': re.compile(r'(ethic|bias|limitation|fairness|privacy|societal)', re.IGNORECASE),
    },
    {
        'id': 'hyperparameters',
        'question': 'Hyperparameters specified?',
        'required': True,
        'regex': re.compile(r'(learning.rate|batch.size|optimizer|hyperparameter|learning_rate)', re.IGNORECASE),
    },
    {
        'id': 'baseline',
        'question': 'Baseline methods and their implementations described?',
        'required': True,
        'regex': re.compile(r'(baseline|comparison|prior.work|existing)', re.IGNORECASE),
    },
    {
        'id': 'evaluation',
        'question': 'Evaluation metrics clearly defined?',
        'required': True,
        'regex': re.compile(r'(metric|accuracy|F1|BLEU|ROUGE|precision|recall)', re.IGNORECASE),
    },
]


def check_reproducibility(filepath: str) -> dict:
    path = Path(filepath)
    if not path.exists():
        return {'error': f'File not found: {filepath}', 'file': filepath}

    text = path.read_text(encoding='utf-8')
    items = []

    for item in CHECKLIST_ITEMS:
        found = bool(item['regex'].search(text))
        items.append({
            'id': item['id'],
            'question': item['question'],
            'found': found,
            'status': 'PASS' if found else 'MISSING',
            'required': item['required'],
        })

    passed = sum(1 for i in items if i['found'])
    total = len(items)
    missing = [i for i in items if not i['found']]

    return {
        'file': filepath,
        'items': items,
        'passed_count': passed,
        'total_count': total,
        'score': round(passed / total * 100, 1),
        'missing': missing,
        'all_passed': passed == total,
    }


def main():
    parser = argparse.ArgumentParser(
        description='Reproducibility Checklist - generate conference-required checklist',
        epilog='KORRO Research v2 - Every paper reproducible by default.',
    )
    parser.add_argument('file', nargs='?', help='Markdown file to check')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--check', action='store_true', help='Dry-run')
    parser.add_argument('--offline', action='store_true', help='Skip online checks')

    args = parser.parse_args()

    if args.check:
        print(f'[DRY-RUN] Would check reproducibility: {args.file or "stdin"}')
        return

    if not args.file:
        print('[ERROR] No file specified.', file=sys.stderr)
        sys.exit(1)

    result = check_reproducibility(args.file)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f'\n=== Reproducibility Checklist: {args.file} ===')
        for item in result['items']:
            status = '[PASS]' if item['found'] else '[MISS]'
            print(f'  {status} {item["question"]}')
        print(f'\nScore: {result["score"]}% ({result["passed_count"]}/{result["total_count"]})')
        print(f'All passed: {"YES" if result["all_passed"] else "NO - fill missing items!"}')

    if not result['all_passed']:
        sys.exit(1)


if __name__ == '__main__':
    main()
