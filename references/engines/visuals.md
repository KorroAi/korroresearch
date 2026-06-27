# Visual Generation Engine

## Figure Types

No more "Insert screenshot here." All figures auto-generated.

| Figure Type | Command |
|---|---|
| Bar chart | --chart bar |
| Line plot | --chart line |
| Heatmap | --chart heatmap |
| Architecture diagram | --diagram architecture |
| Pipeline diagram | --diagram pipeline |
| Confusion matrix | --chart confusion |
| Ablation table | --table ablation |
| Comparison table | --table comparison |

## Quality Standards

- Vector graphics (PDF/SVG) for diagrams
- Colorblind-friendly palette (viridis, cividis, ColorBrewer)
- Every figure has a clear message visible without reading the caption

## Usage

```bash
python scripts/generate_figures.py bar --data results.json --output figure.pdf
python scripts/generate_figures.py --diagram architecture --output arch.pdf
```
