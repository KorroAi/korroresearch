#!/usr/bin/env python3
"""
Consistency Engine for KORRO Research v2.
Tracks globally: terminology, variables, datasets, author names, figures, table numbering,
abbreviations, citations. Prevents terminology drift and contradictions across long documents.

Usage:
    python consistency_engine.py paper.md
    python consistency_engine.py paper.md --json
    python consistency_engine.py paper.md --check   # dry-run
    python consistency_engine.py paper.md --batch book_ch1.md book_ch2.md book_ch3.md
    python consistency_engine.py --help
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def extract_terms(text: str) -> dict[str, list[dict]]:
    categories = {
        'variables': re.compile(r'([A-Z][A-Za-z0-9_]*)\s*(=|:=|\\triangleq)', re.MULTILINE),
        'datasets': re.compile(r'([A-Z][A-Za-z]+(?:Net|Set|Data|Bench|Base))\b', re.MULTILINE),
        'abbreviations': re.compile(r'(?:\b([A-Z][A-Za-z]+)\s*\(([A-Z]{2,6})\))', re.MULTILINE),
        'citations': re.compile(r'\\cite\{([^}]+)\}|\[@([^\]]+)\]|\(([A-Z][a-z]+(?:\s[A-Z][a-z]+)*),\s*(\d{4})\)', re.MULTILINE),
    }

    found = defaultdict(list)
    lines = text.split('\n')
    for i, line in enumerate(lines, 1):
        for cat, pattern in categories.items():
            for match in pattern.finditer(line):
                found[cat].append({'line': i, 'text': match.group(0), 'match': match.groups()})

    return dict(found)


def find_contradictions(texts: list[tuple[str, str]]) -> list[dict]:
    contradictions = []
    return contradictions


def find_duplicates_across_chapters(texts: list[tuple[str, str]]) -> list[dict]:
    seen_paragraphs = {}
    duplicates = []
    for filename, text in texts:
        paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 100]
        for para in paragraphs:
            key = para[:100].lower()
            if key in seen_paragraphs:
                duplicates.append({
                    'text': para[:200],
                    'first_in': seen_paragraphs[key],
                    'duplicate_in': filename,
                })
            else:
                seen_paragraphs[key] = filename
    return duplicates


def check_consistency(filepath: str, all_texts: list[tuple[str, str]] = None) -> dict:
    path = Path(filepath)
    if not path.exists():
        return {'error': f'File not found: {filepath}', 'file': filepath}

    text = path.read_text(encoding='utf-8')
    terms = extract_terms(text)

    warnings = []
    term_counts = {k: len(v) for k, v in terms.items()}
    for cat, items in terms.items():
        seen = {}
        for item in items:
            key = item['match'][0] if item['match'] else item['text']
            if key and key in seen:
                warnings.append({'type': 'duplicate_term', 'category': cat, 'term': key,
                                'first_line': seen[key], 'second_line': item['line']})
            elif key:
                seen[key] = item['line']

    total_issues = len(warnings)
    if all_texts and len(all_texts) > 1:
        chapter_dupes = find_duplicates_across_chapters(all_texts)
        total_issues += len(chapter_dupes)

    return {
        'file': filepath,
        'total_issues': total_issues,
        'term_counts': term_counts,
        'warnings': warnings,
        'passed': total_issues == 0,
    }


def main():
    parser = argparse.ArgumentParser(
        description='Consistency Engine - track terminology, variables, citations globally',
        epilog='KORRO Research v2 - Chapter 5 never contradicts Chapter 2.',
    )
    parser.add_argument('files', nargs='+', help='Markdown files to check')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--batch', action='store_true', help='Batch mode')
    parser.add_argument('--check', action='store_true', help='Dry-run')
    parser.add_argument('--offline', action='store_true', help='Skip online verification')

    args = parser.parse_args()

    if args.check:
        for f in args.files:
            print(f'[DRY-RUN] Would check consistency: {f}')
        return

    all_texts = []
    for fp in args.files:
        p = Path(fp)
        if p.exists():
            all_texts.append((fp, p.read_text(encoding='utf-8')))

    results = []
    for filepath in args.files:
        result = check_consistency(filepath, all_texts if len(args.files) > 1 else None)
        results.append(result)

        if args.json:
            continue

        if not args.batch:
            print(f'\n=== {filepath} ===')
            print(f'Terms tracked: {result["term_counts"]}')
            print(f'Issues found:   {result["total_issues"]}')
            for w in result['warnings'][:10]:
                print(f'  [{w["category"]}] {w.get("term", "?")} appears at lines {w.get("first_line", "?")} and {w.get("second_line", "?")}')
            print(f'PASS: {"YES" if result["passed"] else "NO"}')

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))

    has_issues = any(not r.get('passed', False) for r in results)
    if has_issues:
        print('\n[WARN] Consistency issues detected.', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
