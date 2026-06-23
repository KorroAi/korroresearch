# KORRO Research

**One command. Answer questions. Get a complete document skeleton.**

```bash
python scripts/wizard.py
```

KORRO Research is not a writing guide. It is a complete document production system that takes you from blank page to submission-ready output across 9 formats: research papers, grant proposals, pitch decks, white papers, magazine articles, blog posts, academic books, theses, and conference talks.

---

## Quick Start

```bash
# 1. Run the wizard, generates your document skeleton in 60 seconds
python scripts/wizard.py

# 2. Pick your path
#    Researcher   → publish papers, get cited
#    Founder      → pitch investors, raise money
#    Author       → write a book, build authority
#    Speaker      → give talks, build reputation

# 3. Open QUICKSTART.md for your exact sequence of steps
```

[QUICKSTART.md →](QUICKSTART.md)

---

## Installation

### Claude Code (Recommended)
```bash
# Clone into your Claude Code skills directory
git clone https://github.com/your-username/researchpaperpro.git ~/.claude/skills/researchpaperpro

# Install Python dependencies
cd ~/.claude/skills/researchpaperpro
pip install -r requirements.txt

# The skill activates automatically when you mention any trigger word:
# "write a paper", "pitch deck", "grant proposal", etc.
```

### Standalone (Without Claude Code)
```bash
git clone https://github.com/your-username/researchpaperpro.git
cd researchpaperpro
pip install -r requirements.txt
python scripts/wizard.py
```

### First Time? Never Written Anything?
```bash
python scripts/wizard.py    # Choose option [1] Research Paper
# Then open QUICKSTART.md → PATH 0
```

---

## Formats

| Format | Best For | Guide |
|---|---|---|
| Research Paper (Conference) | Original contribution, peer validation | `references/formats/latexieee.md` |
| Research Paper (ML/NLP) | NeurIPS, ICML, ACL, CVPR | `references/formats/latexmlm.md` |
| Grant Proposal | NSF, ERC, NIH funding | `references/processes/grantsections.md` |
| Pitch Deck | Seed/Series A fundraising | `references/formats/pitchdeck.md` |
| White Paper | Architecture vision, decision-maker audience | `references/formats/htmlpdf.md` |
| Magazine Article | Nature, Wired, MIT Tech Review | `references/formats/magazine.md` |
| Blog Post | Technical essays, FAANG-style posts | `references/formats/blogpost.md` |
| Academic Book | 200-600 page comprehensive work | `references/processes/end-to-end.md` |
| Conference Talk | 15-min presentation, keynote | `references/formats/presentation.md` |

---

## Architecture

```
korroresearch/
├── SKILL.md                  ← Entry point (loaded automatically by Claude Code)
├── QUICKSTART.md             ← 4 paths: Researcher, Founder, Author, Speaker
├── README.md                 ← This file
├── LICENSE                   ← MIT
├── scripts/
│   ├── wizard.py             ← Interactive onboarding wizard
│   ├── generate_pdf.py       ← Markdown → PDF (weasyprint)
│   ├── generate_figures.py   ← Publication-ready charts
│   ├── claim_checker.py      ← Claim-evidence verification
│   ├── semantic_scholar.py   ← Paper search + citation formatting
│   └── clean_dashes.py       ← Typographic dash cleanup
└── references/
    ├── sections/             ← Section writing guides (abstract, intro, method, etc.)
    ├── processes/            ← Meta-workflow guides (ideation, impact, mastery, etc.)
    ├── formats/              ← Output format guides (LaTeX, PDF, pitch deck, etc.)
    ├── examples/             ← Annotated examples
    ├── paperreview.md        ← Adversarial self-review checklist
    ├── figuresandtables.md   ← Visual standards + anti-patterns gallery
    └── doesmywritingflowsource.md ← Paragraph flow diagnostics
```

---

## Key Principles

1. **Idea quality before writing** — The Shannon Filter determines if your idea deserves a paper.
2. **Impact over information** — Being correct is not enough. Be unignorable.
3. **Claim-evidence alignment** — Every claim maps to evidence. No orphan claims.
4. **Audience-first thinking** — Write for the skeptical reviewer, investor, or editor.
5. **Visual-first impression** — Figures and tables must tell the story without reading the text.
6. **Mastery beyond rules** — Taste, danger, obsession, network, timing, voice. The unteachable dimensions.

---

## Scripts

| Script | Usage |
|---|---|
| `wizard.py` | `python scripts/wizard.py [--format paper\|pitch-deck\|grant\|...]` |
| `generate_pdf.py` | `python scripts/generate_pdf.py paper.md paper.pdf [--template two-column\|single-column]` |
| `generate_figures.py` | `python scripts/generate_figures.py bar --data results.json --output figure.pdf` |
| `claim_checker.py` | `python scripts/claim_checker.py paper.md [--strict] [--json]` |
| `semantic_scholar.py` | `python scripts/semantic_scholar.py search "query" --limit 5 --format apa` |
| `clean_dashes.py` | `python scripts/clean_dashes.py paper.md` |

---

## Requirements

- Python 3.10+ ([download](https://python.org))
- `pip install -r requirements.txt`
- Semantic Scholar API is free, no key required

### PDF Generation

Output is **always PDF**. Research papers, grant proposals, pitch decks — all submitted as PDF.

The script tries two engines:
1. **weasyprint** (best typography, two-column layout) — requires GTK3 on Windows.
2. **fpdf2** (pure Python, works everywhere) — automatic fallback, zero dependencies.

```bash
# Always produces a PDF, auto-selects best available engine
python scripts/generate_pdf.py paper.md paper.pdf
python scripts/generate_pdf.py paper.md paper.pdf --template single-column
```

**Windows users**: if weasyprint GTK is not installed, fpdf2 is used automatically. PDF is generated either way. For best results, install GTK3 via [MSYS2](https://www.msys2.org/).

---

## License

MIT — see [LICENSE](LICENSE)
