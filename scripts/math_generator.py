
#!/usr/bin/env python3
"""
Mathematics Generator for KORRO Research v2.
Generates: notation table, equation stubs, algorithm boxes, pseudo-code.

Usage:
    python math_generator.py paper.md
    python math_generator.py paper.md --notation
    python math_generator.py paper.md --equations
    python math_generator.py paper.md --algorithm
    python math_generator.py paper.md --json
    python math_generator.py paper.md --check
    python math_generator.py --help
"""

import argparse
import json
import re
import sys
from pathlib import Path


def extract_variables(text: str) -> list[dict]:
    variables = []
    patterns = [
        (re.compile(r'([A-Za-z])\s*(=|:=|\\triangleq)\s*'), 'definition'),
        (re.compile(r'\\mathbf\{([^}]+)\}'), 'bold_vector'),
        (re.compile(r'\\mathcal\{([^}]+)\}'), 'calligraphic'),
        (re.compile(r'\\mathbb\{([^}]+)\}'), 'blackboard'),
        (re.compile(r'\$([A-Za-z])\s*\\in\s*\\mathbb\{R\}'), 'real_scalar'),
    ]
    lines = text.split('\n')
    for i, line in enumerate(lines, 1):
        for pattern, var_type in patterns:
            for match in pattern.finditer(line):
                variables.append({
                    'line': i,
                    'symbol': match.group(0),
                    'type': var_type,
                    'context': line.strip()[:120],
                })
    return variables


def generate_notation_table(variables: list[dict]) -> str:
    if not variables:
        return 'No mathematical notation found in document.'
    rows = []
    seen = set()
    for v in variables:
        symbol = v['symbol'].strip()
        if symbol not in seen:
            seen.add(symbol)
            rows.append(f'| `{symbol}` | [DEFINE] | [DESCRIPTION] |')
    header = '| Symbol | Definition | Description |\n|---|---|---|\n'
    return header + '\n'.join(rows)


def generate_algorithm_box(name: str = 'Algorithm', steps: list[str] = None) -> str:
    if steps is None:
        steps = ['Input: ...', 'Output: ...', '1: [Step 1]', '2: [Step 2]', '3: return result']
    lines = [f'**{name}**', '', '```', r'\begin{algorithmic}', r'\REQUIRE Input specification', r'\ENSURE Output specification']
    for step in steps:
        lines.append(r'\STATE ' + str(step))
    lines.extend([r'\end{algorithmic}', '```', ''])
    return '\n'.join(lines)


def generate_math(filepath: str, mode: str = 'all') -> dict:
    path = Path(filepath)
    if not path.exists():
        return {'error': f'File not found: {filepath}', 'file': filepath}

    text = path.read_text(encoding='utf-8')
    variables = extract_variables(text)
    notation = generate_notation_table(variables) if mode in ('notation', 'all') else None
    algorithm = generate_algorithm_box() if mode in ('algorithm', 'all') else None

    return {
        'file': filepath,
        'variables_found': len(variables),
        'variables': variables[:20],
        'notation_table': notation,
        'algorithm_box': algorithm,
    }


def main():
    parser = argparse.ArgumentParser(
        description='Math Generator - notation tables, equation stubs, algorithm boxes',
        epilog='KORRO Research v2 - No ML paper ships without proper notation.',
    )
    parser.add_argument('file', nargs='?', help='Markdown file to analyze')
    parser.add_argument('--notation', action='store_true', help='Generate notation table')
    parser.add_argument('--equations', action='store_true', help='Generate equation stubs')
    parser.add_argument('--algorithm', action='store_true', help='Generate algorithm box')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--check', action='store_true', help='Dry-run')
    parser.add_argument('--offline', action='store_true', help='Skip online generation')

    args = parser.parse_args()

    if args.check:
        print(f'[DRY-RUN] Would generate math for: {args.file or "stdin"}')
        return

    if not args.file:
        print('[ERROR] No file specified.', file=sys.stderr)
        sys.exit(1)

    mode = 'all'
    if args.notation: mode = 'notation'
    if args.equations: mode = 'equations'
    if args.algorithm: mode = 'algorithm'

    result = generate_math(args.file, mode=mode)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f'\n=== Math Generation: {args.file} ===')
        print(f'Variables found: {result["variables_found"]}')
        if result.get('notation_table'):
            print(f'\n--- Notation Table ---\n{result["notation_table"]}')
        if result.get('algorithm_box'):
            print(f'\n--- Algorithm Box ---\n{result["algorithm_box"]}')


if __name__ == '__main__':
    main()
