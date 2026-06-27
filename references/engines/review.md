# Review Engine

## Pre-Export Checklist

### Critical Issues
- Missing required sections (abstract, experiments, conclusion)
- Missing ethics statement (required by NeurIPS, ACL, etc.)
- Missing limitations section
- Missing reproducibility information
- Author information in anonymous submissions

### High Issues
- Unsupported claims without numbers
- Uncited statistics
- Vague novelty claims
- Missing baselines

### Medium Issues
- Repeated paragraphs (common in AI-generated text)
- Weak transitions between sections
- Formatting violations (page limits, font sizes)
- Inconsistent terminology

## Venue-Specific Rules

| Venue | Anonymous | Page Limit | Special Requirements |
|---|---|---|---|
| NeurIPS | Yes | 9 | Ethics, broader impact, checklist |
| ICML | Yes | 8 | Ethics, reproducibility |
| CVPR | No | 8 | Supplementary, acknowledgements |
| ACL | Yes | 8 | Limitations, ethics, acknowledgements |

## Usage

```bash
python scripts/review_engine.py paper.md --venue neurips
python scripts/review_engine.py paper.md --venue icml --json
```
