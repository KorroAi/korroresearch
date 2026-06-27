# Hallucination Detection Engine

## Classification Levels

Every factual claim in your document is classified into one of four categories:

| Level | Label | Meaning | Action Required |
|---|---|---|---|
| 1 | VERIFIED | Backed by citation or verifiable source | None |
| 2 | USER PROVIDED | From user input, assumed factual | Confirm with user |
| 3 | AI HYPOTHESIS | Plausible but unverified | User must verify or remove |
| 4 | SPECULATIVE | No evidence, no citation | REMOVE before publication |

## How It Works

The engine scans every sentence for claim patterns:

1. **Statistics** - Percentages, multipliers ("3.2x faster"), quantities
2. **Comparisons** - SOTA claims, outperforms, surpasses
3. **Novelty claims** - "First", "novel", "unprecedented"
4. **Intensifiers** - "Significantly", "substantially", "dramatically"
5. **Hedging** - "Could potentially", "may allow", "might be able to"

Each claim is matched against:
- Does it have a citation?
- Is it backed by user-provided data?
- Is it a known verifiable fact?

## Trust Score

The engine outputs a Trust Score (0-100%) based on:
`(verified + user_provided) / total_claims * 100`

- 90-100%: Publication-ready
- 70-89%: Needs verification
- 50-69%: Significant gaps
- <50%: DO NOT PUBLISH

## Strict Mode

In strict mode (`--strict`), any SPECULATIVE claim causes failure.
Use this for final camera-ready checks.

## Usage

```bash
python scripts/hallucination_checker.py paper.md
python scripts/hallucination_checker.py paper.md --strict
python scripts/hallucination_checker.py paper.md --json
```
