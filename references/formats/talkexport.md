# Conference Talk Export Options

## Export Formats

| Format | Tool | Best For |
|---|---|---|
| PDF (Beamer) | LaTeX | Academic conferences |
| PPTX | PowerPoint/Keynote | Industry talks |
| HTML | Reveal.js | Web-based talks |
| Google Slides | Google Slides | Collaborative talks |

## Speaker Kit (Generated per Talk)

1. **Slide deck** - Formatted per venue template
2. **Presenter notes** - What to say on each slide
3. **Timing guide** - Minutes per slide
4. **Demo script** - Steps for live demos
5. **Q&A prep** - Anticipated questions + answers
6. **Backup slides** - Extra material if Q&A is short
7. **Social media kit** - Tweet-sized summaries for each slide

## Animation and Visual Standards

- No bullet-point reveals (cognitive load)
- One figure per slide maximum
- Dark background for projection readability
- Font size never below 24pt
- 3 minutes per slide average
- Last slide: call to action + contact

## Usage

```bash
python scripts/wizard.py --format talk --export beamer
python scripts/wizard.py --format talk --export pptx
python scripts/wizard.py --format talk --export revealjs
```
