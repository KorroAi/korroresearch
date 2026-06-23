#!/usr/bin/env python3
"""Verify that claims in Abstract and Introduction map to experimental evidence.

Matches claims against explicit references (tables, figures, sections) and
numerical values in the Experiments section. Flags orphan claims.

Usage:
    python claim_checker.py paper.md
    python claim_checker.py paper.md --json
    python claim_checker.py paper.md --strict
    python claim_checker.py --help
"""

import sys
import re
import json
import argparse
from pathlib import Path

# Patterns that signal a CLAIM (quantified or absolute)
CLAIM_SIGNALS = [
    r"(?:achieves?|reduces?|improves?|outperforms?|surpasses?|delivers?|boosts?|cuts?|lowers?|raises?)\s+[^.]{0,80}\d+(?:\.\d+)?\s*[%×x]",
    r"\d+(?:\.\d+)?\s*[%]\s+(?:of|improvement|reduction|faster|better|higher|lower|more|less)",
    r"(?:higher|better|faster|lower|more|less)\s+(?:quality|performance|accuracy|efficiency|speed|memory|throughput)",
    r"(?:state.of.the.art|SOTA|best|first|only|novel|outperforms?\s+all)",
    r"(?:we|our method|our approach|our model|our pipeline)\s+[^.]{0,100}(?:better|faster|more|higher|lower|outperforms?)",
    r"\d+(?:\.\d+)?\s*(?:×|x|times)\s*(?:faster|speedup|improvement|reduction)",
    r"(?:we propose|we introduce|we present|our contribution|we develop)",
]

REF_PATTERNS = [
    r"(?:Table|Figure|Fig\.)\s*\d+",
    r"(?:Section|§)\s*\d+(?:\.\d+)*",
    r"(?:see|shown in|reported in|presented in|summarized in)\s+(?:Table|Figure|Fig\.|Section)",
]

DATA_PATTERN = re.compile(
    r"(?:(?:PSNR|LPIPS|FID|BLEU|ROUGE|METEOR|accuracy|precision|recall|F1|AUC|mAP|IoU|WER|CER|perplexity"
    r"|runtime|latency|throughput|memory|parameters)\s*(?:\([^)]*\))?\s*(?:↑|↓|improvement|reduction)?)"
    r"|(?:\d+(?:\.\d+)?\s*[%×x])",
    re.IGNORECASE,
)

# Common section name aliases
SECTION_ALIASES = {
    "abstract": ["abstract", "summary", "tl;dr"],
    "introduction": ["introduction", "intro"],
    "experiments": ["experiments", "results", "evaluation", "experimental results", "experimental evaluation"],
    "conclusion": ["conclusion", "discussion", "conclusions", "discussion and conclusion"],
}


def _find_section(text, aliases):
    """Extract section text matching any of the alias names."""
    for alias in aliases:
        for prefix in ("## ", "# "):
            pattern = rf"(?m)^{re.escape(prefix)}{re.escape(alias)}.*?\n(.*?)(?=^{re.escape(prefix)}\s|\Z)"
            match = re.search(pattern, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
    return ""


def extract_section(text, name):
    return _find_section(text, SECTION_ALIASES.get(name.lower(), [name]))


def extract_claims(text):
    claims = []
    seen = set()
    if not text:
        return claims
    for i, line in enumerate(text.split("\n"), 1):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("```") or line.startswith("|") or line.startswith("<!--"):
            continue
        if len(line) < 30:
            continue
        for pattern in CLAIM_SIGNALS:
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                key = line[:120]
                if key not in seen:
                    seen.add(key)
                    claims.append({
                        "line": i,
                        "text": line[:300],
                        "matched_pattern": m.group()[:80],
                    })
                break
    return claims


def extract_evidence(text):
    if not text:
        return {"references": [], "data_points": [], "has_tables": False}

    refs = []
    for m in re.finditer("|".join(REF_PATTERNS), text, re.IGNORECASE):
        refs.append(m.group())

    data_points = []
    for m in DATA_PATTERN.finditer(text):
        data_points.append(m.group())

    return {
        "references": list(set(refs)),
        "data_points": data_points,
        "has_tables": bool(re.search(r"^##\s+|^###\s+", text, re.MULTILINE)),
    }


def check_claim(claim, evidence):
    claim_text = claim["text"].lower()
    refs_in_evidence = [r.lower() for r in evidence["references"]]
    data_in_evidence = " ".join(evidence["data_points"]).lower()

    claim_refs = []
    for pattern in REF_PATTERNS:
        for m in re.finditer(pattern, claim_text, re.IGNORECASE):
            claim_refs.append(m.group())

    referenced_evidence = any(
        any(r.lower() in ev_ref for ev_ref in refs_in_evidence)
        for r in claim_refs
    )

    claim_numbers = set(re.findall(r"\d+(?:\.\d+)?", claim_text))
    evidence_numbers = set(re.findall(r"\d+(?:\.\d+)?", data_in_evidence))
    metric_numbers = {n for n in claim_numbers if len(n) >= 2 and float(n) > 1.0}
    matching_numbers = metric_numbers & evidence_numbers

    if referenced_evidence and matching_numbers:
        status, confidence = "well_supported", 0.9
    elif referenced_evidence or matching_numbers:
        status, confidence = "supported", 0.6
    elif evidence["has_tables"]:
        status, confidence = "needs_explicit_ref", 0.3
    else:
        status, confidence = "needs_evidence", 0.0

    return {
        "status": status,
        "confidence": confidence,
        "claim_refs": claim_refs,
        "matching_numbers": sorted(matching_numbers, key=lambda x: -len(x))[:5],
        "evidence_refs_count": len(evidence["references"]),
        "evidence_datapoints_count": len(evidence["data_points"]),
    }


def check_paper(filepath, strict=False):
    try:
        text = Path(filepath).read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        return {"error": f"Cannot read {filepath}: not a valid UTF-8 file ({e})"}
    except OSError as e:
        return {"error": f"Cannot read {filepath}: {e}"}

    if not text.strip():
        return {"error": f"{filepath} is empty"}

    abstract = extract_section(text, "abstract")
    intro = extract_section(text, "introduction")
    experiments = extract_section(text, "experiments")

    if not abstract and not intro:
        return {
            "paper": filepath,
            "total_claims": 0,
            "supported": 0,
            "needs_explicit_ref": 0,
            "needs_evidence": 0,
            "has_experiments_section": bool(experiments),
            "experiments_has_tables": False,
            "experiments_has_datapoints": 0,
            "claims": [],
            "pass": True,
            "warning": "No Abstract or Introduction section found. Check heading format (## Abstract, ## Introduction).",
        }

    abstract_claims = extract_claims(abstract)
    intro_claims = extract_claims(intro)
    evidence = extract_evidence(experiments)

    results = []
    for claim in abstract_claims:
        result = check_claim(claim, evidence)
        result["source"] = "abstract"
        claim["evidence"] = result
        results.append(claim)

    for claim in intro_claims:
        if claim not in abstract_claims:
            result = check_claim(claim, evidence)
            result["source"] = "introduction"
            claim["evidence"] = result
            results.append(claim)

    supported = sum(1 for r in results if r["evidence"]["status"] in ("well_supported", "supported"))
    needs_explicit = sum(1 for r in results if r["evidence"]["status"] == "needs_explicit_ref")
    needs_evidence = sum(1 for r in results if r["evidence"]["status"] == "needs_evidence")

    return {
        "paper": filepath,
        "total_claims": len(results),
        "supported": supported,
        "needs_explicit_ref": needs_explicit,
        "needs_evidence": needs_evidence,
        "has_experiments_section": bool(experiments),
        "experiments_has_tables": evidence["has_tables"],
        "experiments_has_datapoints": len(evidence["data_points"]),
        "claims": results,
        "pass": needs_evidence == 0 if strict else needs_evidence <= max(1, len(results) * 0.15) if results else True,
    }


def format_output(report, json_out=False):
    if "error" in report:
        print(f"Error: {report['error']}", file=sys.stderr)
        return 1

    if json_out:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    warning = report.pop("warning", None)

    print(f"\nClaim-Evidence Check: {report['paper']}")
    print(f"{'=' * 60}")
    print(f"Claims found:              {report['total_claims']}")
    print(f"  Well supported:           {report['supported']}")
    print(f"  Needs explicit reference: {report['needs_explicit_ref']}")
    print(f"  Needs evidence:           {report['needs_evidence']}")
    print(f"  PASS: {report['pass']}")
    print(f"Experiments section:       {'FOUND' if report['has_experiments_section'] else 'NOT FOUND'}")
    print(f"  Data points extracted:   {report['experiments_has_datapoints']}")

    if warning:
        print(f"\n  Note: {warning}")

    if report["needs_explicit_ref"] or report["needs_evidence"]:
        print(f"\nClaims needing attention:")
        for claim in report["claims"]:
            ev = claim["evidence"]
            if ev["status"] in ("needs_evidence", "needs_explicit_ref"):
                print(f"  [{ev['status'].upper()}] [{claim['evidence']['source']} L{claim['line']}]")
                print(f"    {claim['text'][:150]}")
                if ev["claim_refs"]:
                    print(f"    Claim references: {', '.join(ev['claim_refs'])}")
                print()
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Verify claims in academic papers map to evidence",
        add_help=False,
    )
    parser.add_argument("--help", action="store_true", help="Show this help")
    parser.add_argument("file", nargs="?", help="Markdown file to check")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--strict", action="store_true", help="Fail if ANY claim lacks evidence")

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    if args.help or not args.file:
        parser.print_help()
        print("\nExamples:")
        print("  python claim_checker.py paper.md")
        print("  python claim_checker.py paper.md --strict")
        print("  python claim_checker.py paper.md --json")
        return 0

    filepath = args.file
    if not Path(filepath).exists():
        print(f"Error: {filepath} not found", file=sys.stderr)
        return 1

    report = check_paper(filepath, strict=args.strict)
    return format_output(report, json_out=args.json)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
