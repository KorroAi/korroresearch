#!/usr/bin/env python3
"""
Style Engine for KORRO Research v2.
Switch between Nature, NeurIPS, MIT, Google, McKinsey, YC, NSF styles
without regenerating everything. Handles terminology, tone, formatting presets.

Usage:
    python style_engine.py paper.md --preset neurips
    python style_engine.py paper.md --preset nature --apply
    python style_engine.py paper.md --list                         # List available presets
    python style_engine.py paper.md --check                        # Verify compliance
    python style_engine.py paper.md --preset mckinsey --json
    python style_engine.py --help
"""

import argparse
import json
import re
import sys
from pathlib import Path


PRESETS = {
    'nature': {
        'description': 'Nature journal style — concise, authoritative, accessible',
        'tone': 'authoritative but accessible to interdisciplinary readers',
        'voice': 'active preferred, first-person plural',
        'terminology': {
            'utilize': 'use',
            'demonstrate': 'show',
            'leverage': 'use',
            'facilitate': 'help',
            'regarding': 'about',
            'in order to': 'to',
        },
        'rules': {
            'abstract_max_words': 150,
            'no_footnotes_in_abstract': True,
            'methods_last': True,
            'data_availability_statement': True,
        },
    },
    'neurips': {
        'description': 'NeurIPS/ML conference — technical, rigorous, anonymous',
        'tone': 'technical, precise, evidence-driven',
        'voice': 'third-person for anonymity, active for clarity',
        'terminology': {
            'our': 'the',
            'we': 'the authors',
            'SOTA': 'state-of-the-art',
        },
        'rules': {
            'anonymous': True,
            'max_pages': 9,
            'ethics_statement': True,
            'broader_impact': True,
            'checklist': True,
        },
    },
    'mit': {
        'description': 'MIT style — direct, rigorous, no fluff',
        'tone': 'direct, precise, intellectually honest',
        'voice': 'active, first-person',
        'terminology': {},
        'rules': {},
    },
    'google': {
        'description': 'Google research — data-driven, scalable, clear',
        'tone': 'data-first, practical, engineer-friendly',
        'voice': 'active, we, metrics-heavy',
        'terminology': {},
        'rules': {'metrics_upfront': True, 'ablation_mandatory': True},
    },
    'mckinsey': {
        'description': 'McKinsey — MECE, executive-friendly, action-oriented',
        'tone': 'structured, decisive, business-impact',
        'voice': 'declarative, bottom-line up front',
        'terminology': {
            'maybe': '',
            'perhaps': '',
            'could potentially': '',
        },
        'rules': {'executive_summary_first': True, 'action_items': True},
    },
    'yc': {
        'description': 'Y Combinator — punchy, traction-focused, memorable',
        'tone': 'bold, concise, momentum-driven',
        'voice': 'first-person, present tense, numbers-forward',
        'terminology': {},
        'rules': {'traction_first': True, 'team_slide': True, 'ask_slide': True},
    },
    'nsf': {
        'description': 'NSF grant — intellectual merit + broader impacts',
        'tone': 'scholarly, impact-focused, rigorous',
        'voice': 'active, we, forward-looking',
        'terminology': {},
        'rules': {'intellectual_merit': True, 'broader_impacts': True, 'data_management_plan': True},
    },
}


def list_presets():
    print('Available style presets:\n')
    for name, preset in PRESETS.items():
        print(f'  {name:12s} — {preset["description"]}')
    print()


def check_compliance(text: str, preset_name: str) -> dict:
    preset = PRESETS.get(preset_name, {})
    violations = []

    for old, new in preset.get('terminology', {}).items():
        if old.lower() in text.lower():
            violations.append({
                'type': 'terminology',
                'term': old,
                'suggestion': new or '[REMOVE]',
            })

    rules = preset.get('rules', {})
    if rules.get('anonymous'):
        author_patterns = [r'university of', r'institute of', r'department of', r'@\w+\.\w+']
        for pat in author_patterns:
            if re.search(pat, text, re.IGNORECASE):
                violations.append({'type': 'anonymity', 'detail': f'Potential author info: matched "{pat}"'})

    return {
        'preset': preset_name,
        'preset_description': preset.get('description', ''),
        'tone': preset.get('tone', ''),
        'voice': preset.get('voice', ''),
        'violations': violations,
        'violation_count': len(violations),
        'compliant': len(violations) == 0,
    }


def apply_style(text: str, preset_name: str) -> str:
    """Apply terminology substitutions."""
    preset = PRESETS.get(preset_name, {})
    for old, new in preset.get('terminology', {}).items():
        pattern = re.compile(r'\b' + re.escape(old) + r'\b', re.IGNORECASE)
        replacement = new if new else ''
        text = pattern.sub(replacement, text)
    return text


def main():
    parser = argparse.ArgumentParser(
        description='Style Engine - switch between Nature, NeurIPS, MIT, McKinsey, YC, NSF',
        epilog='KORRO Research v2 - One document, any venue. No rewriting.',
    )
    parser.add_argument('file', nargs='?', help='Markdown file to process')
    parser.add_argument('--preset', help='Style preset to apply or check')
    parser.add_argument('--list', action='store_true', help='List available presets')
    parser.add_argument('--apply', action='store_true', help='Apply style substitutions (writes to file)')
    parser.add_argument('--check', action='store_true', help='Check compliance without modifying')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--offline', action='store_true', help='Skip online style references')

    args = parser.parse_args()

    if args.list:
        list_presets()
        return

    if args.preset and args.preset not in PRESETS:
        print(f'[ERROR] Unknown preset: {args.preset}', file=sys.stderr)
        print(f'Available: {", ".join(PRESETS.keys())}', file=sys.stderr)
        sys.exit(1)

    if not args.file:
        print('[ERROR] No file specified.', file=sys.stderr)
        sys.exit(1)

    path = Path(args.file)
    if not path.exists():
        print(f'[ERROR] File not found: {args.file}', file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding='utf-8')
    preset = args.preset or 'neurips'

    if args.apply:
        new_text = apply_style(text, preset)
        path.write_text(new_text, encoding='utf-8')
        print(f'[OK] Applied {preset} style to {args.file}')
        return

    result = check_compliance(text, preset)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f'\n=== Style Check: {args.file} ===')
        print(f'Preset:   {preset} — {result["preset_description"]}')
        print(f'Tone:     {result["tone"]}')
        print(f'Voice:    {result["voice"]}')
        print(f'Issues:   {result["violation_count"]}')
        for v in result['violations'][:15]:
            print(f'  [{v["type"]}] {v.get("term", v.get("detail", "?"))}')
        print(f'PASS:     {"YES" if result["compliant"] else "NO"}')

    if not result['compliant']:
        sys.exit(1)


if __name__ == '__main__':
    main()
