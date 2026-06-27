# Style Engine

## Available Presets

| Preset | Use Case | Key Rules |
|---|---|---|
| Nature | Nature journal | Concise, accessible, 150-word abstract |
| NeurIPS | ML conferences | Anonymous, 9 pages, ethics statement |
| MIT | Academic CS | Direct, rigorous, no fluff |
| Google | Industry research | Data-first, ablation mandatory |
| McKinsey | Consulting | MECE, executive summary, action items |
| YC | Startup pitches | Traction-first, bold, numbers-forward |
| NSF | Grant proposals | Intellectual merit + broader impacts |

## What It Does

1. **Terminology substitution** - "utilize" -> "use", "leverage" -> "use"
2. **Anonymity check** - For NeurIPS/ICML: flags author-identifying text
3. **Format compliance** - Checks page limits, required sections
4. **Tone adjustment** - Ensures voice matches venue expectations

## Apply vs Check

- `--check`: Verify compliance without modifying (recommended for review)
- `--apply`: Automatically fix terminology (use cautiously)

## Usage

```bash
python scripts/style_engine.py paper.md --preset nature --check
python scripts/style_engine.py paper.md --preset neurips --apply
python scripts/style_engine.py --list
```
