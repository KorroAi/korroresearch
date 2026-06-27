# Fact Checking Engine

## What Gets Checked

1. **Statistics** - Percentages must be plausible (no >100% claims)
2. **Names** - Author names, researcher names
3. **Institutions** - Universities, labs, companies
4. **Conference Names** - Must match known venue names
5. **Dates** - Years, submission dates
6. **Datasets** - Must match known dataset names or be explicitly introduced
7. **Benchmarks** - Named benchmarks must exist

## Known Databases

The engine maintains databases of:
- Known institutions (MIT, Stanford, CMU, Berkeley, Oxford, etc.)
- Known conferences (NeurIPS, ICML, CVPR, ACL, etc.)
- Known datasets (ImageNet, COCO, SQuAD, GLUE, etc.)

## Verification Levels

| Level | Meaning |
|---|---|
| verified | Matched known database or verified source |
| unverifiable | Needs manual verification |
| flagged | Suspicious (e.g., percentage > 100%, impossible date) |

## Usage

```bash
python scripts/fact_checker.py paper.md
python scripts/fact_checker.py paper.md --stats --names --institutions
python scripts/fact_checker.py paper.md --json
```
