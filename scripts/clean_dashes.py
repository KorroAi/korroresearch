#!/usr/bin/env python3
"""Replace typographic dashes in markdown prose with plain text equivalents.

Skips fenced code blocks and inline code. Preserves compound words.
Matches SKILL.md rule: em-dash -> ' -- ' (space, two hyphens, space).

Usage:
    python clean_dashes.py                         process all .md files in skill tree
    python clean_dashes.py path/to/file.md         process a single file
    python clean_dashes.py --check                 dry-run: report what would change, don't modify
    python clean_dashes.py --check path/to/file.md dry-run on a single file
    python clean_dashes.py --help                  show this help
"""

import re
import sys
import os
import argparse
from pathlib import Path

EM_DASH = "—"
EN_DASH = "–"
REPLACEMENT = " -- "


def clean_dashes(text):
    lines = text.split("\n")
    result = []
    in_fence = False
    fence_marker = ""

    for line in lines:
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

        parts = re.split(r"(`[^`]+`)", line)
        cleaned_parts = []
        for i, part in enumerate(parts):
            if i % 2 == 0:
                part = part.replace(EM_DASH, REPLACEMENT)
                part = part.replace(EN_DASH, REPLACEMENT)
            cleaned_parts.append(part)
        result.append("".join(cleaned_parts))

    return "\n".join(result)


def _count_changes(text):
    """Count how many dashes would be replaced."""
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

    changes = _count_changes(original)
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
        description="Replace typographic dashes in markdown files",
        add_help=False,
    )
    parser.add_argument("--help", action="store_true", help="Show this help")
    parser.add_argument("path", nargs="?", help="File to process (default: all .md files in skill tree)")
    parser.add_argument("--check", action="store_true", help="Dry-run: report what would change without modifying")

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    if args.help:
        parser.print_help()
        print("\nExamples:")
        print("  python clean_dashes.py")
        print("  python clean_dashes.py paper.md")
        print("  python clean_dashes.py --check")
        return 0

    dry_run = args.check
    stats = {"ok": 0, "fixed": 0, "would_fix": 0, "skip": 0, "fail": 0}

    if args.path:
        result = process_file(args.path, dry_run=dry_run)
        stats[result] = 1
    else:
        skill_dir = Path(__file__).resolve().parent.parent
        for root, dirs, files in os.walk(skill_dir):
            # Skip hidden and cache directories
            dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
            for f in sorted(files):
                if f.endswith(".md"):
                    path = os.path.join(root, f)
                    result = process_file(path, dry_run=dry_run)
                    stats[result] += 1

    # Summary
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
