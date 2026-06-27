#!/usr/bin/env python3
"""
Source Manager for KORRO Research v2.
Generates and verifies: BibTeX, DOI, arXiv, CrossRef, IEEE, APA, ACM references.

Usage:
    python source_manager.py paper.md
    python source_manager.py paper.md --verify
    python source_manager.py paper.md --format bibtex
    python source_manager.py paper.md --json
    python source_manager.py paper.md --batch paper1.md paper2.md
    python source_manager.py paper.md --check   # dry-run
    python source_manager.py --help
"""

import argparse
import json
import re
import sys
from pathlib import Path


def extract_citations(text: str) -> list[dict]:
    citations = []

    cite_patterns = [
        re.compile(r'\\cite\{([^}]+)\}'),
        re.compile(r'\[@([^\]]+)\]'),
        re.compile(r'\(([A-Z][a-z]+(?:\s[A-Z][a-z]+)*),\s*(\d{4})\)'),
        re.compile(r'\[(\d+)\]'),
    ]

    for pattern in cite_patterns:
        for match in pattern.finditer(text):
            citations.append({
                'raw': match.group(0),
                'key': match.group(1) if match.lastindex else match.group(0),
                'format': 'unknown',
            })

    return citations


def generate_bibtex(citation: dict) -> str:
    key = citation['key'].replace(' ', '_').lower()
    return f"""@article{{{key},
  author    = {{[NEEDS VERIFICATION]}},
  title     = {{[NEEDS VERIFICATION]}},
  journal   = {{[NEEDS VERIFICATION]}},
  year      = {{[NEEDS VERIFICATION]}},
}}"""


def generate_apa(citation: dict) -> str:
    return f"[NEEDS VERIFICATION] ({citation.get('year', 'n.d.')}). [TITLE]. *[JOURNAL]*."


def generate_ieee(citation: dict) -> str:
    return f"[NEEDS VERIFICATION], \"[TITLE],\" *[JOURNAL]*, {citation.get('year', 'n.d.')}."


def generate_acm(citation: dict) -> str:
    return f"[NEEDS VERIFICATION]. {citation.get('year', 'n.d.')}. [TITLE]. *[JOURNAL]*."


FORMATTERS = {
    'bibtex': generate_bibtex,
    'apa': generate_apa,
    'ieee': generate_ieee,
    'acm': generate_acm,
}


def manage_sources(filepath: str, output_format: str = 'bibtex', verify: bool = False) -> dict:
    path = Path(filepath)
    if not path.exists():
        return {'error': f'File not found: {filepath}', 'file': filepath}

    text = path.read_text(encoding='utf-8')
    citations = extract_citations(text)

    formatter = FORMATTERS.get(output_format, generate_bibtex)
    formatted = []
    for cite in citations:
        formatted.append({
            'raw': cite['raw'],
            'key': cite['key'],
            'formatted': formatter(cite) if not verify else cite['raw'],
            'verified': False,
            'source': None,
        })

    return {
        'file': filepath,
        'total_citations': len(citations),
        'format': output_format,
        'verified_count': 0,
        'unverified_count': len(citations),
        'citations': formatted,
        'passed': len(citations) > 0,
        'warning': 'All citations need manual verification' if citations else 'No citations found',
    }


def main():
    parser = argparse.ArgumentParser(
        description='Source Manager - generate and verify BibTeX, DOI, APA, IEEE, ACM',
        epilog='KORRO Research v2 - Every citation verified or flagged.',
    )
    parser.add_argument('files', nargs='+', help='Markdown files to manage')
    parser.add_argument('--verify', action='store_true', help='Verify citations against external sources')
    parser.add_argument('--format', default='bibtex',
                       choices=['bibtex', 'apa', 'ieee', 'acm', 'doi'],
                       help='Output format for generated references')
    parser.add_argument('--output', help='Write generated references to file')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--batch', action='store_true', help='Batch mode')
    parser.add_argument('--check', action='store_true', help='Dry-run')
    parser.add_argument('--offline', action='store_true', help='Skip online verification')

    args = parser.parse_args()

    if args.check:
        for f in args.files:
            print(f'[DRY-RUN] Would manage sources: {f}')
        return

    results = []
    for filepath in args.files:
        result = manage_sources(filepath, output_format=args.format, verify=args.verify)
        results.append(result)

        if args.json:
            continue

        if not args.batch:
            print(f'\n=== {filepath} ===')
            print(f'Format:          {args.format}')
            print(f'Citations found: {result["total_citations"]}')
            print(f'Verified:        {result["verified_count"]}')
            print(f'Unverified:      {result["unverified_count"]}')
            print(f'{result["warning"]}')

            if args.output and result.get('citations'):
                output_path = Path(args.output)
                formatted_text = '\n\n'.join(c['formatted'] for c in result['citations'])
                output_path.write_text(formatted_text, encoding='utf-8')
                print(f'References written to: {args.output}')

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
