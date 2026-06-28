# KORRO Research

![KORRO Research](assets/illustration.png)

**From blank page to venue-compliant PDF. Zero hallucinations. Every claim verified.**

**[See a complete example → MUE-X: Cross-Modal Agents with Shared Memory](references/examples/muex_paper.pdf)**

```bash
python scripts/wizard.py
```

KORRO Research is a complete document production system. It does not give writing advice — it enforces quality automatically through eight cross-cutting engines that check every claim, verify every fact, track every term, and match every format before a single page leaves the pipeline. Nine output formats. Fourteen scripts. Fifty-plus reference guides. One command.

---

## Why KORRO Research

Most writing tools help you write faster. KORRO Research helps you write correctly.

| Problem | KORRO Research Solution |
|---|---|
| AI-generated papers contain fabricated statistics | `hallucination_checker.py` classifies every claim as verified, user-provided, hypothesis, or speculative |
| Citations don't match references | `source_manager.py` generates BibTeX, APA, IEEE, ACM, DOI — all verified against CrossRef and arXiv |
| Terminology drifts across chapters | `consistency_engine.py` tracks every term, variable, citation, and abbreviation globally |
| Section titles land alone at page bottom | `generate_pdf.py` enforces orphan heading prevention with automatic page breaks |
| Documents look like Word defaults | `typography-layout.md` enforces 13 typography rules including font hierarchy, spacing, widows/orphans |
| Venue requirements missed | `review_engine.py` checks NeurIPS/ICML/CVPR/ACL compliance before export |
| No reproducibility information | `reproducibility_checklist.py` verifies dataset, code, hardware, seeds, license, ethics |
| Claims without evidence survive editing | `claim_checker.py` maps every claim to experimental evidence |

---

## Formats

| # | Format | Target Venue | Key Output |
|---|---|---|---|
| 1 | Research Paper (Conference) | NeurIPS, ICML, CVPR, ACL, IEEE, ACM | Two-column PDF + DOCX |
| 2 | Pitch Deck | YC, Sequoia, a16z, Accel | PDF slides + DOCX |
| 3 | Grant Proposal | NSF, NIH, ERC, Horizon, DARPA | PDF + DOCX |
| 4 | White Paper | Gartner, Microsoft, AWS, Google Cloud | PDF + DOCX |
| 5 | Magazine Article | Nature, Quanta, MIT Tech Review, Wired | PDF + DOCX |
| 6 | Academic Book | 200—600 pages | PDF + DOCX |
| 7 | Technical Blog Post | Medium, Dev.to, Hashnode, Substack | Markdown + PDF + DOCX |
| 8 | Conference Talk | PowerPoint, Keynote, Beamer, Reveal.js | Slide deck + speaker notes |
| 9 | Thesis / Dissertation | PhD, Masters, APA/IEEE/Chicago | PDF + DOCX |

Every format produces three files: `.md` (source), `.pdf` (publication-ready), `.docx` (editable). No manual export step.

---

## Quick Start

```bash
git clone https://github.com/KorroAi/korroresearch.git
cd korroresearch
pip install -r requirements.txt
python scripts/wizard.py
```

The wizard asks five questions. You get a complete document skeleton with PDF and DOCX generated automatically. Open `QUICKSTART.md` for your exact path: Researcher, Founder, Author, or Speaker.

---

## The Pipeline

```
PHASE A: BEFORE WRITING
  wizard.py  →  ideation.md  →  impact.md  →  audience.md  →  style_engine.py

PHASE B: WRITING
  math_generator.py  →  section guides  →  generate_figures.py  →  consistency_engine.py

PHASE C: BEFORE FINALIZING
  hallucination_checker.py  →  fact_checker.py  →  source_manager.py
  →  paperreview.md  →  review_engine.py  →  claim_checker.py
  →  reproducibility_checklist.py  →  clean_dashes.py  →  style_engine.py
  →  generate_pdf.py + generate_docx.py

PHASE D: MASTERY
  mastery.md — 7 dimensions: Taste. Danger. Obsession. Network. Anti-fragility. Timing. Voice.

PHASE E: HUMAN-IN-THE-LOOP
  Outline approval  →  Section-by-section  →  Inline comments  →  Version history
```

---

## Scripts

### Production

| Script | Purpose |
|---|---|
| `wizard.py` | Interactive onboarding: 5 questions → document skeleton + PDF + DOCX |
| `generate_pdf.py` | Markdown → publication PDF (two-column or single-column) |
| `generate_docx.py` | Markdown → editable DOCX (Times New Roman, proper hierarchy) |
| `generate_figures.py` | Publication charts: bar, line, heatmap, ablation, architecture, pipeline |
| `semantic_scholar.py` | Paper search + citation formatting: APA, IEEE, BibTeX, ACM |
| `clean_dashes.py` | Zero-dash enforcement: commas and colons only |

### Verification Engines

| Script | Purpose |
|---|---|
| `hallucination_checker.py` | Classify every claim: verified / user-provided / hypothesis / speculative |
| `fact_checker.py` | Verify statistics, names, institutions, conferences, datasets |
| `source_manager.py` | Generate BibTeX, DOI, arXiv, APA, IEEE, ACM references |
| `consistency_engine.py` | Track terminology, variables, citations, numbering across chapters |
| `style_engine.py` | Switch between Nature, NeurIPS, MIT, McKinsey, YC, NSF presets |
| `review_engine.py` | Flag missing sections, weak claims, duplicates, venue violations |
| `math_generator.py` | Generate notation tables, equation stubs, algorithm boxes |
| `reproducibility_checklist.py` | Dataset, code, hardware, seeds, license, ethics |
| `claim_checker.py` | Map every claim to experimental evidence |

All scripts have `--help`, `--json`, `--check` (dry-run), `--batch`, and `--offline` flags. Exit codes: 0 = pass, 1 = issues found.

---

## Architecture

```
korroresearch/
├── SKILL.md                           # Skill entry point (loaded by Claude Code)
├── README.md                          # This file
├── QUICKSTART.md                      # 4 paths: Researcher, Founder, Author, Speaker
├── LICENSE                            # MIT
├── requirements.txt                   # Python dependencies
├── output/                            # Generated .md, .pdf, .docx files
├── assets/                            # Illustrations
├── scripts/
│   ├── wizard.py                      # Interactive onboarding (→ .md + .pdf + .docx)
│   ├── generate_pdf.py                # Markdown → publication PDF
│   ├── generate_docx.py               # Markdown → editable DOCX
│   ├── generate_figures.py            # Publication charts and diagrams
│   ├── semantic_scholar.py            # Paper search + citation formatting
│   ├── clean_dashes.py                # Zero-dash enforcement
│   ├── hallucination_checker.py       # Claim classification engine
│   ├── fact_checker.py                # Statistic and fact verification
│   ├── source_manager.py              # Reference generation and verification
│   ├── consistency_engine.py          # Global terminology and variable tracking
│   ├── style_engine.py                # Venue-specific style presets
│   ├── review_engine.py               # Pre-export issue detection
│   ├── math_generator.py              # Notation tables and algorithm boxes
│   ├── reproducibility_checklist.py   # Conference-required checklist
│   └── claim_checker.py               # Claim-evidence mapping
└── references/
    ├── sections/                      # Section writing guides (8 files)
    ├── processes/                     # Meta-workflow guides (14 files)
    ├── formats/                       # Output format guides (18 files)
    ├── engines/                       # Engine documentation (7 files)
    ├── examples/                      # Complete example papers (4 files)
    ├── paperreview.md                 # 5-dimension adversarial self-review
    ├── figuresandtables.md            # Visual standards + anti-patterns
    ├── doesmywritingflowsource.md     # Paragraph flow diagnostics
    └── typography-layout.md           # 13 typography rules + pre-PDF checklist
```

---

## Global Quality Rules

### Non-Negotiable
- **No dashes.** Em dashes, en dashes, double hyphens → replaced with commas or colons.
- **Active voice.** At least 80% of sentences. "We analyzed" not "It was analyzed."
- **Orphan headings.** No section title alone at the bottom of a page. Enforced by `generate_pdf.py`.
- **Claim-evidence map.** Every claim must trace to a specific experiment, citation, or preliminary result.
- **Terminology stability.** Same concept, same name, across the entire document.

### Tables
- Caption above. Booktabs style (no vertical lines). Metric direction labeled: PSNR ↑, LPIPS ↓.
- Best and second-best values highlighted. Consistent decimal places per column.

### Figures
- Vector graphics for diagrams. Colorblind-friendly palette (viridis, cividis, ColorBrewer).
- Captions state what to observe AND the conclusion. Every figure tells its story without the text.

### Citations
- Use `semantic_scholar.py` for search. Prefer recent (last 3 years) for SOTA comparisons.
- Cite the original source, not a survey. Format consistently per venue.

---

## Requirements

- Python 3.10+
- `pip install -r requirements.txt`
- Semantic Scholar API: free, no key required
- WeasyPrint: optional, requires GTK3 on Windows for best typography (fpdf2 fallback works everywhere)

---

## Installation

```bash
# Claude Code (recommended)
git clone https://github.com/KorroAi/korroresearch.git ~/.claude/skills/korroresearch
cd ~/.claude/skills/korroresearch
pip install -r requirements.txt

# Standalone
git clone https://github.com/KorroAi/korroresearch.git
cd korroresearch
pip install -r requirements.txt
python scripts/wizard.py
```

The skill activates automatically in Claude Code. Mention "research paper", "pitch deck", "grant proposal", or any supported format.

---

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, ship it.

---

Built on the conviction that writing cannot save a bad idea, but bad writing can kill a great one — and that no document should ship with a claim it cannot prove.
