# HTML to PDF - Professional Paper Output

Generate publication-ready PDFs using HTML + weasyprint. This is the recommended format for preprints, white papers, and any paper where you need full design control.

## When to Use

- Preprints (arxiv-ready appearance)
- White papers with custom branding
- Papers where LaTeX is unavailable
- Documents needing web distribution alongside PDF

## Prerequisites

```bash
pip install weasyprint markdown
```

## Quick Start

Use the bundled script. It handles markdown conversion, CSS styling, and PDF generation in one step.

```bash
python scripts/generate_pdf.py paper.md paper.pdf
python scripts/generate_pdf.py paper.md paper.pdf --template single-column
```

The script applies the full CSS stylesheet (two-column IEEE-style by default, single-column for white papers). Source: `scripts/generate_pdf.py`.

## Typography Standards

| Element | Font | Size | Style |
|---------|------|------|-------|
| Title | Times New Roman | 16pt | Bold, centered |
| Authors | Times New Roman | 10pt | Centered |
| Section headers | Times New Roman | 12pt | Bold |
| Body text | Times New Roman | 10pt | Justified |
| Abstract | Times New Roman | 9pt | Justified |
| Captions | Times New Roman | 9pt | Left-aligned |
| References | Times New Roman | 9pt | Left-aligned |
| Code | Consolas / Monaco | 8pt | Monospace |
| Footnotes | Times New Roman | 8pt | - |

## Markdown to PDF (Manual)

If you need custom styling beyond what the script provides, convert manually:

```python
import markdown
from weasyprint import HTML

with open('paper.md', 'r') as f:
    md = f.read()

html_body = markdown.markdown(md, extensions=['tables', 'fenced_code', 'footnotes', 'codehilite'])

html = f"""<!DOCTYPE html><html lang="en">
<head><meta charset="UTF-8"><style>{custom_css}</style></head>
<body>{html_body}</body></html>"""

HTML(string=html).write_pdf('paper.pdf')
```

## Quality Checklist
- [ ] PDF renders correctly (no overlapping elements)
- [ ] All figures are vector or high-resolution
- [ ] Tables follow booktabs style (no vertical lines)
- [ ] References are properly numbered/ordered
- [ ] Page numbers present
- [ ] Two-column layout if conference paper style
- [ ] Color output for figures, grayscale for text
- [ ] Hyperlinks work in the PDF
