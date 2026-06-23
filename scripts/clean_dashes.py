#!/usr/bin/env python3
"""Remove ALL dashes from markdown prose. Zero tolerance.

Replaces:
    Em dash (—) and " -- " → ", " or ": " depending on context
    En dash (–) between numbers → " to "
    En dash (–) elsewhere → ", "

Skips fenced code blocks and inline code. Preserves compound words (state-of-the-art).
ZERO dashes in output. Commas and colons only.

Usage:
    python clean_dashes.py                         process all .md files in skill tree
    python clean_dashes.py path/to/file.md         process a single file
    python clean_dashes.py --check                 dry-run: report what would change
    python clean_dashes.py --help
"""

import re
import sys
import os
import argparse
from pathlib import Path

EM_DASH = "—"
EN_DASH = "–"
DOUBLE_HYPHEN = " -- "


def _choose_replacement(text, match_start, match_end, match_text):
    """Determine whether to use ', ' or ': ' based on context."""
    # After the dash: look at what follows
    after = text[match_end:].lstrip()
    before = text[:match_start].rstrip()

    # If between digits, use " to "
    if re.search(r'\d\s*$', before) and re.match(r'\s*\d', after):
        return " to "

    # If the text after starts a list, example, or definition → colon
    if re.match(r'^(for example|e\.g\.|i\.e\.|specifically|namely|that is|in other words)', after, re.IGNORECASE):
        return ": "
    if re.match(r'^(see|defined as|a |an |the )', after):
        return ": "

    # If before is a complete clause and after is an explanation → colon
    if re.search(r'[.!?]\s*$', before):
        return ": "

    # Default: comma (most parenthetical breaks)
    return ", "


def clean_dashes(text):
    """Replace all dashes with commas or colons based on context."""
    lines = text.split("\n")
    result = []
    in_fence = False
    fence_marker = ""

    for line in lines:
        # Track fenced code blocks
        if not in_fence:
            m = re.match(r"^(```+|~~~)\s*$", line)
            if m:
                in_fence = True
                fence_marker = m.group(1)
                result.append(line)
                continue
        else:
            if line.strip().startswith(fence_marker):
                in_fence = False
                fence_marker = ""
            result.append(line)
            continue

        # Split on inline code spans, only process prose parts
        parts = re.split(r"(`[^`]+`)", line)
        cleaned_parts = []

        for i, part in enumerate(parts):
            if i % 2 == 0:  # prose
                # Replace em dashes
                while EM_DASH in part:
                    idx = part.index(EM_DASH)
                    repl = _choose_replacement(part, idx, idx + 1, EM_DASH)
                    part = part[:idx] + repl + part[idx + 1:]

                # Replace en dashes
                while EN_DASH in part:
                    idx = part.index(EN_DASH)
                    repl = _choose_replacement(part, idx, idx + 1, EN_DASH)
                    part = part[:idx] + repl + part[idx + 1:]

                # Replace " -- " (double hyphen used as dash)
                # Only replace when surrounded by spaces (actual dash usage, not in paths/URLs)
                part = re.sub(r'\s+--\s+', lambda m: _choose_replacement(part, m.start(), m.end(), m.group()), part)
            cleaned_parts.append(part)

        result.append("".join(cleaned_parts))

    return "\n".join(result)


def _count_dashes(text):
    """Count dash occurrences in prose (excluding code)."""
    count = 0
    lines = text.split("\n")
    in_fence = False
    fence_marker = ""

    for line in lines:
        if not in_fence:
            m = re.match(r"^(```+|~~~)\s*$", line)
            if m:
                in_fence = True
                fence_marker = m.group(1)
                continue
        else:
            if line.strip().startswith(fence_marker):
                in_fence = False
                fence_marker = ""
            continue

        parts = re.split(r"(`[^`]+`)", line)
        for i, part in enumerate(parts):
            if i % 2 == 0:
                count += part.count(EM_DASH) + part.count(EN_DASH)
                count += len(re.findall(r'\s+--\s+', part))

    return count


def process_file(filepath, dry_run=False):
    p = Path(filepath)
    try:
        original = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"SKIP  {filepath}  (not UTF-8)", file=sys.stderr)
        return "skip"
    except OSError as e:
        print(f"SKIP  {filepath}  ({e})", file=sys.stderr)
        return "skip"

    changes = _count_dashes(original)
    if changes == 0:
        return "ok"

    if dry_run:
        print(f"WOULD FIX  {filepath}  ({changes} dash(es))")
        return "would_fix"

    cleaned = clean_dashes(original)
    try:
        p.write_text(cleaned, encoding="utf-8")
        print(f"FIXED  {filepath}  ({changes} dash(es))")
        return "fixed"
    except OSError as e:
        print(f"FAIL  {filepath}  ({e})", file=sys.stderr)
        return "fail"


def main():
    parser = argparse.ArgumentParser(
        description="Remove ALL dashes from markdown prose (replaced with commas or colons)",
        add_help=False,
    )
    parser.add_argument("--help", action="store_true")
    parser.add_argument("path", nargs="?", help="File to process (default: all .md files in skill tree)")
    parser.add_argument("--check", action="store_true", help="Dry-run: report what would change")

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    if args.help:
        parser.print_help()
        print("\nReplaces: —  –  and ' -- '  with ', ' or ': ' (comma or colon)")
        print("Number ranges like 10–20 become 10 to 20")
        print("ZERO dashes remain in output.")
        return 0

    dry_run = args.check
    stats = {"ok": 0, "fixed": 0, "would_fix": 0, "skip": 0, "fail": 0}

    if args.path:
        result = process_file(args.path, dry_run=dry_run)
        stats[result] = 1
    else:
        skill_dir = Path(__file__).resolve().parent.parent
        for root, dirs, files in os.walk(skill_dir):
            dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
            for f in sorted(files):
                if f.endswith(".md"):
                    path = os.path.join(root, f)
                    result = process_file(path, dry_run=dry_run)
                    stats[result] += 1

    if not args.path:
        total = sum(stats.values())
        parts = []
        if stats["ok"]: parts.append(f"{stats['ok']} OK")
        if stats["fixed"]: parts.append(f"{stats['fixed']} fixed")
        if stats["would_fix"]: parts.append(f"{stats['would_fix']} would fix")
        if stats["skip"]: parts.append(f"{stats['skip']} skipped")
        if stats["fail"]: parts.append(f"{stats['fail']} failed")
        print(f"\nTotal: {total} files ({', '.join(parts)})")

    return 1 if stats["fail"] > 0 else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
