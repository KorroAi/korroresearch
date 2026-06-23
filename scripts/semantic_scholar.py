#!/usr/bin/env python3
"""Search Semantic Scholar API for academic papers and format citations.

Supports APA 7th, IEEE, BibTeX, and MLA formats.
Rate-limited with exponential backoff for reliability.

Usage:
    python semantic_scholar.py search "multi model code verification" --limit 5
    python semantic_scholar.py search "ensemble methods code generation" --limit 10 --json
    python semantic_scholar.py cite "paper_id_here" --format bibtex
    python semantic_scholar.py search "transformers" --offline   (dry-run: shows URL only)
"""

import sys
import json
import urllib.request
import urllib.parse
import urllib.error
import time
import argparse
from pathlib import Path

API_BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,authors,year,venue,citationCount,externalIds,abstract,url,journal"
MAX_RETRIES = 5
BASE_DELAY = 2  # seconds


# ── Author formatting ──────────────────────────────────────────

def _name_initials(name: str) -> str:
    """Convert 'John Smith' to 'Smith, J.'"""
    parts = name.strip().split()
    if len(parts) < 2:
        return name or "Anonymous"
    last = parts[-1]
    initials = "".join(f"{p[0]}." for p in parts[:-1] if p)
    return f"{last}, {initials}"


def _format_apa_authors(authors: list) -> str:
    if not authors:
        return "Anonymous"
    names = [_name_initials(a.get("name", "Unknown")) for a in authors]
    n = len(names)
    if n == 1: return names[0]
    if n == 2: return f"{names[0]}, & {names[1]}"
    if n <= 20: return ", ".join(names[:-1]) + f", & {names[-1]}"
    return ", ".join(names[:19]) + f", ... {names[-1]}"


def _format_ieee_authors(authors: list) -> str:
    if not authors:
        return "Anonymous"
    names = [a.get("name", "Unknown") for a in authors[:6]]
    if len(authors) > 6:
        return ", ".join(names) + " et al."
    return ", ".join(names)


# ── API ────────────────────────────────────────────────────────

def _fetch(url: str, max_retries: int = MAX_RETRIES) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": "KORROResearch/1.2"})
    last_error = None

    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read()
                if not raw:
                    last_error = "Empty response body"
                    continue
                data = json.loads(raw)
                if "error" in data:
                    print(f"API error: {data['error']}", file=sys.stderr)
                    return None
                return data
        except urllib.error.HTTPError as e:
            if e.code == 429:
                delay = BASE_DELAY * (2 ** attempt)
                print(f"Rate limited (attempt {attempt + 1}/{max_retries}). Waiting {delay}s...", file=sys.stderr)
                time.sleep(delay)
                continue
            if e.code == 404:
                print(f"Not found (HTTP 404)", file=sys.stderr)
                return None
            if e.code >= 500:
                delay = BASE_DELAY * (2 ** attempt)
                print(f"Server error HTTP {e.code} (attempt {attempt + 1}/{max_retries}). Waiting {delay}s...", file=sys.stderr)
                time.sleep(delay)
                continue
            last_error = f"HTTP {e.code}: {e.reason}"
            print(last_error, file=sys.stderr)
            return None
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            last_error = str(e)[:100]
            if attempt < max_retries - 1:
                delay = BASE_DELAY * (2 ** attempt)
                print(f"Network error (attempt {attempt + 1}/{max_retries}): {last_error}", file=sys.stderr)
                print(f"  Waiting {delay}s...", file=sys.stderr)
                time.sleep(delay)
            else:
                print(f"API unreachable after {max_retries} retries: {last_error}", file=sys.stderr)
                return None
        except json.JSONDecodeError as e:
            print(f"Invalid API response: {e}", file=sys.stderr)
            return None

    print(f"All {max_retries} retries exhausted: {last_error}", file=sys.stderr)
    return None


def search_papers(query: str, limit: int = 10, offline: bool = False) -> dict | None:
    url = f"{API_BASE}/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields={FIELDS}"
    if offline:
        print(f"[OFFLINE MODE] Would search: {url}")
        return None
    return _fetch(url)


def get_paper(paper_id: str, offline: bool = False) -> dict | None:
    url = f"{API_BASE}/paper/{paper_id}?fields={FIELDS}"
    if offline:
        print(f"[OFFLINE MODE] Would fetch: {url}")
        return None
    return _fetch(url)


# ── Citation formatting ────────────────────────────────────────

def format_citation(paper: dict, fmt: str = "apa") -> str:
    authors = paper.get("authors") or []
    year = paper.get("year") or "n.d."
    title = paper.get("title") or "Untitled"
    venue = paper.get("venue") or ""
    journal = paper.get("journal") or {}
    journal_name = journal.get("name", "") if isinstance(journal, dict) else ""
    venue_str = journal_name or venue

    if fmt == "apa":
        author_str = _format_apa_authors(authors)
        base = f"{author_str} ({year}). {title}"
        return f"{base}. {venue_str}." if venue_str else f"{base}."

    if fmt == "ieee":
        author_str = _format_ieee_authors(authors)
        venue_suffix = f", {year}." if not venue_str else f", in *{venue_str}*, {year}."
        return f'{author_str}, "{title}"{venue_suffix}'

    if fmt == "bibtex":
        author_str = " and ".join(a.get("name", "Unknown") for a in authors[:8])
        paper_id = paper.get("paperId", "ref")
        key = paper_id[:12] if paper_id else "ref"
        doi = (paper.get("externalIds") or {}).get("DOI", "")
        lines = [f"@article{{{key},"]
        lines.append(f"  author = {{{author_str}}},")
        lines.append(f"  title = {{{title}}},")
        lines.append(f"  year = {{{year}}},")
        if venue_str:
            lines.append(f"  journal = {{{venue_str}}},")
        if doi:
            lines.append(f"  doi = {{{doi}}},")
        lines.append("}")
        return "\n".join(lines)

    if fmt == "mla":
        author_str = ", ".join(a.get("name", "Unknown") for a in authors[:3])
        if len(authors) > 3:
            author_str += " et al."
        base = f'{author_str}. "{title}."'
        if venue_str:
            base += f" {venue_str},"
        return f"{base} {year}."

    return format_citation(paper, "apa")


# ── Commands ────────────────────────────────────────────────────

def search_cmd(args) -> int:
    if not args.query:
        print("Error: query is required for search", file=sys.stderr)
        return 1

    data = search_papers(args.query, args.limit, args.offline)
    if data is None:
        if args.offline:
            return 0
        print("No results found. The API may be rate-limited or unreachable.", file=sys.stderr)
        print("Try again in a few minutes, or use a VPN.", file=sys.stderr)
        return 1

    papers = data.get("data")
    if not papers:
        print("No results found for that query.")
        return 0

    if args.json:
        print(json.dumps(papers, indent=2, ensure_ascii=False))
        return 0

    fmt = args.cite_format or "apa"
    print(f"\nResults for: {args.query}\n{'=' * 60}")
    for i, paper in enumerate(papers, 1):
        title = paper.get("title", "Untitled")
        year = paper.get("year", "?")
        citations = paper.get("citationCount", 0)
        paper_id = paper.get("paperId", "")
        print(f"\n[{i}] {title}")
        print(f"    {format_citation(paper, fmt)}")
        print(f"    Citations: {citations} | ID: {paper_id}")

    if data.get("next"):
        print("\n  (More results available -- increase --limit to see more)")
    return 0


def cite_cmd(args) -> int:
    if not args.paper_id:
        print("Error: paper_id is required for cite", file=sys.stderr)
        return 1

    paper = get_paper(args.paper_id, args.offline)
    if paper is None:
        if args.offline:
            return 0
        print("Paper not found or API unreachable.", file=sys.stderr)
        return 1

    fmt = args.cite_format or "apa"
    print(format_citation(paper, fmt))
    return 0


# ── Main ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Search Semantic Scholar and format citations",
        add_help=False,
    )
    parser.add_argument("--help", action="store_true", help="Show this help")
    sub = parser.add_subparsers(dest="command")

    # search
    p_search = sub.add_parser("search", add_help=False)
    p_search.add_argument("query", nargs="?", help="Search query")
    p_search.add_argument("--limit", type=int, default=10, help="Max results (default 10)")
    p_search.add_argument("--json", action="store_true", help="JSON output")
    p_search.add_argument("--format", dest="cite_format", choices=["apa", "ieee", "bibtex", "mla"],
                           default="apa", help="Citation format")
    p_search.add_argument("--offline", action="store_true", help="Dry-run: show API URL without calling it")

    # cite
    p_cite = sub.add_parser("cite", add_help=False)
    p_cite.add_argument("paper_id", nargs="?", help="Semantic Scholar paper ID")
    p_cite.add_argument("--format", dest="cite_format", choices=["apa", "ieee", "bibtex", "mla"],
                         default="apa", help="Citation format")
    p_cite.add_argument("--offline", action="store_true", help="Dry-run: show API URL without calling it")

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    if args.help or not args.command:
        parser.print_help()
        print("\nExamples:")
        print('  python semantic_scholar.py search "gradient compression" --limit 5')
        print('  python semantic_scholar.py search "transformers" --json --limit 3')
        print('  python semantic_scholar.py cite abc123def456 --format bibtex')
        print('  python semantic_scholar.py search "test" --offline')
        return 0

    try:
        if args.command == "search":
            return search_cmd(args)
        elif args.command == "cite":
            return cite_cmd(args)
        else:
            print(f"Unknown command: {args.command}", file=sys.stderr)
            return 1
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
