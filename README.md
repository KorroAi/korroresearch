# KORRO Research

![MUE-X: Cross-modal agents with shared memory and zero-shot task transfer](assets/mue-x-illustration.png)

**One command. Nine formats. Complete document production system.**

```bash
python scripts/wizard.py
```

KORRO Research transforms blank-page paralysis into a finished document skeleton in 60 seconds. It is not a writing tips collection, it is a production pipeline: wizard → skeleton → write → verify → format → submit. Nine output formats, six hardened scripts, thirty-eight reference guides, zero excuses.

---

## About

**KORRO Research** is built and maintained by **Kevin** under the [KorroAi](https://github.com/KorroAi) organization. It transforms the academic and professional writing process from weeks of procrastination into a 60-second pipeline.

**What it does**: An interactive wizard asks five questions about your idea, then generates a complete document skeleton with section prompts, writing tips, and a verification checklist. Six scripts handle everything else: claim-evidence checking, dash elimination, PDF generation, figure production, and citation formatting.

**By the numbers**:
- 9 output formats (research paper, pitch deck, grant, white paper, magazine, book, blog, talk, thesis)
- 6 hardened Python scripts (all with `--help`, zero known crashes)
- 38 reference guides covering every section, process, and format
- 4 citation styles (APA, IEEE, BibTeX, MLA)
- 1 rule: zero dashes, commas and colons only

**What makes it different**: KORRO Research does not give writing advice. It enforces quality automatically. `claim_checker.py` verifies that every claim maps to experimental evidence. `clean_dashes.py` eliminates every em dash, en dash, and double hyphen from your prose. `generate_pdf.py` produces submission-ready output with no manual formatting. The system treats writing as an engineering discipline, not an art.

**License**: MIT — use it, fork it, ship it. See [LICENSE](LICENSE).

---

## What This Is

You have an idea. You need a research paper, a pitch deck, a grant proposal, or a white paper. You open a blank document. Two hours later, you have written and deleted the same three sentences seventeen times.

KORRO Research eliminates this. The wizard asks five questions about your idea, then generates a complete document skeleton with section prompts, writing tips, and a checklist. Each section tells you exactly what to write. Each prompt includes examples of what good looks like. You replace placeholders with your content, run the verification scripts, and you are done.

---

## Formats

| # | Format | Use Case | Sections | Output |
|---|---|---|---|---|
| 1 | Research Paper (Conference) | NeurIPS, ICML, ACL, CVPR, IEEE, ACM | Abstract, Introduction, Related Work, Method, Experiments, Conclusion | LaTeX or PDF |
| 2 | Pitch Deck | Seed to Series A fundraising | 12 slides: One-Liner through The Vision | PDF slide deck |
| 3 | Grant Proposal | NSF, ERC, NIH, Horizon Europe | Specific Aims, Research Strategy, Preliminary Results, Budget, Timeline, Broader Impact | PDF or DOCX |
| 4 | White Paper | Architecture vision, thought leadership | Executive Summary, Problem, Architecture, Migration Path, ROI, Call to Action | PDF |
| 5 | Magazine Article | Nature, Wired, MIT Tech Review, Quanta, The Atlantic | Hook, Context, Deep Dive, Human Element, Takeaway | PDF or web |
| 6 | Academic Book | 200-600 page comprehensive work | Preface, Journey chapters, Synthesis, Appendices | PDF or LaTeX |
| 7 | Technical Blog Post | Engineering blog, FAANG-style essay | Headline, Opening, Problem, Solution, Results, Code, Closing | Markdown or web |
| 8 | Conference Talk | 15-min presentation, keynote, seminar | Hook, Problem, Method, Results, Limitations, Thank You | Beamer or Reveal.js |
| 9 | Thesis / Dissertation | PhD, Masters | Full academic structure | LaTeX or PDF |

---

## Quick Start

```bash
# Clone
git clone https://github.com/loopiak/korroresearch.git
cd korroresearch

# Install
pip install -r requirements.txt

# Generate your first document skeleton
python scripts/wizard.py

# Open QUICKSTART.md for your exact path
```

### First time, never written anything?

```bash
python scripts/wizard.py              # Choose [1] Research Paper
# Answer 5 questions. Get a complete skeleton.
# Open QUICKSTART.md → PATH 0: Beginner Researcher
```

---

## Scripts

Six production-hardened scripts. Each has `--help`, robust error handling, and graceful fallbacks. Zero known crashes.

### wizard.py — Interactive Onboarding

```bash
python scripts/wizard.py                                    # Interactive: choose format, answer questions
python scripts/wizard.py --format pitch                     # Skip format selection
python scripts/wizard.py --format paper --batch \           # Non-interactive mode
    "My insight" "Why now" "Audience" "Worldview" "Name"
python scripts/wizard.py --help                             # Show all options
```

The wizard asks five questions (Shannon Filter), then generates a markdown skeleton with section prompts, writing tips, and a next-steps checklist. Output lands in `output/`.

### generate_pdf.py — Markdown to Publication PDF

```bash
python scripts/generate_pdf.py paper.md paper.pdf
python scripts/generate_pdf.py paper.md paper.pdf --template single-column
python scripts/generate_pdf.py paper.md paper.pdf --preview     # Auto-open after generation
```

Two engines, zero configuration:
1. **weasyprint** (primary): HTML+CSS rendering, two-column academic layout, best typography. Requires GTK3 on Windows.
2. **fpdf2** (fallback): Pure Python, zero system dependencies, works everywhere. Automatic selection.

Output is always PDF. Always.

### claim_checker.py — Claim-Evidence Verification

```bash
python scripts/claim_checker.py paper.md                  # Human-readable report
python scripts/claim_checker.py paper.md --strict         # Fail if ANY claim lacks evidence
python scripts/claim_checker.py paper.md --json           # Machine-readable output
```

Detects claims in Abstract and Introduction, checks them against data points and references in the Experiments section. Flags orphan claims. Supports section aliases (Abstract/Summary, Experiments/Results/Evaluation).

### clean_dashes.py — Dash Elimination

```bash
python scripts/clean_dashes.py                            # Process all .md files in skill tree
python scripts/clean_dashes.py paper.md                   # Process single file
python scripts/clean_dashes.py --check                    # Dry-run: report only, no changes
```

Zero dashes policy enforced automatically. Replaces em dashes, en dashes, and double hyphens with commas or colons based on context. Number ranges become "X to Y". Skips code blocks and inline code.

### generate_figures.py — Publication Charts

```bash
python scripts/generate_figures.py bar --data results.json --output figure1.pdf
python scripts/generate_figures.py line --data metrics.json --output plot.pdf
python scripts/generate_figures.py heatmap --data matrix.json --output heatmap.pdf
python scripts/generate_figures.py ablation --data ablation.json --output ablation.pdf
```

All charts use a colorblind-friendly ColorBrewer palette at 300 DPI. Vector-ready PDF output. Data format documented in `--help` for each chart type.

**JSON data formats:**
- `bar`: `{"labels": [...], "values": [...], "highlight_idx": 3}`
- `line`: `{"x": [...], "series": [{"label": "Our Method", "values": [...]}]}`
- `heatmap`: `{"labels_x": [...], "labels_y": [...], "matrix": [[...]]}`
- `ablation`: `{"labels": ["Full Model", ...], "values": [25.7, 24.1, ...], "metric": "PSNR"}`

### semantic_scholar.py — Paper Search & Citation

```bash
python scripts/semantic_scholar.py search "gradient compression" --limit 5
python scripts/semantic_scholar.py search "transformers" --json --limit 10
python scripts/semantic_scholar.py cite abc123def456 --format bibtex
python scripts/semantic_scholar.py search "test" --offline        # Show API URL without calling
```

Four citation formats: APA 7th, IEEE, BibTeX, MLA. Exponential backoff with 5 retries for rate limiting. `--offline` flag for dry-run without network. Free API, no key required.

---

## Architecture

```
korroresearch/
├── SKILL.md                       # Claude Code skill entry point
├── README.md                      # This file
├── QUICKSTART.md                  # 4 paths: Researcher, Founder, Author, Speaker
├── LICENSE                        # MIT
├── requirements.txt               # Python dependencies
├── output/                        # Generated documents (gitignored except .gitkeep)
│   └── .gitkeep
├── assets/
│   └── mue-x-illustration.png    # Example illustration
├── scripts/
│   ├── wizard.py                  # Interactive onboarding wizard (0 → skeleton in 60s)
│   ├── generate_pdf.py            # Markdown → publication PDF (weasyprint or fpdf2)
│   ├── generate_figures.py        # Publication charts (bar, line, heatmap, ablation)
│   ├── claim_checker.py           # Claim-evidence verification
│   ├── semantic_scholar.py        # Paper search + citation formatting (4 styles)
│   └── clean_dashes.py            # Zero-dash enforcement (commas/colons only)
└── references/
    ├── sections/                  # Section writing guides
    │   ├── abstract.md            #   3 abstract templates
    │   ├── introduction.md        #   4 task intro + 3 challenge + 4 pipeline versions
    │   ├── relatedwork.md         #   Thematic vs chronological, gap identification
    │   ├── method.md              #   Technical clarity, reproducibility, notation
    │   ├── experiments.md         #   3 core questions, experiment planning
    │   ├── conclusion.md          #   Summary, limitations, future work
    │   └── title.md               #   Strategic title design (read 5x more than abstract)
    ├── processes/                 # Meta-workflow guides
    │   ├── ideation.md            #   7 protocols: Shannon filter, anti-paper, elegance razor
    │   ├── impact.md              #   8 principles of unforgettable writing
    │   ├── audience.md            #   Reader psychology: who reads, what they believe
    │   ├── mastery.md             #   7 unteachable dimensions (taste, danger, obsession...)
    │   ├── end-to-end.md          #   Blank page to submit: timeline, revision cycles
    │   ├── rebuttal.md            #   Reviewer response: tone, structure, point-by-point
    │   ├── venues.md              #   Conference/journal selection: impact, audience
    │   ├── supplementary.md       #   Appendices, extra results, cross-referencing
    │   ├── coauthoring.md         #   Multi-author workflows, CRediT taxonomy
    │   ├── grantsections.md       #   Budget, timeline, broader impact, preliminary results
    │   ├── recognition.md         #   12-month flywheel: paper → talk → magazine → investor
    │   └── dossier.md             #   Complete package: paper + pitch + press kit + social proof
    ├── formats/                   # Output format guides
    │   ├── latexieee.md           #   IEEE/ACM conference-ready LaTeX
    │   ├── latexmlm.md            #   NeurIPS/ICML/ACL conference-ready LaTeX
    │   ├── htmlpdf.md             #   HTML + weasyprint professional PDF
    │   ├── docx.md                #   python-docx editable documents
    │   ├── presentation.md        #   Beamer/Reveal.js talks
    │   ├── pitchdeck.md           #   Investor pitch structure and design
    │   ├── blogpost.md            #   Technical blog posts, FAANG-style
    │   └── magazine.md            #   Nature, Wired, MIT Tech Review, The Atlantic
    ├── examples/                  # Annotated examples
    │   ├── muex_paper.md           #   Complete MUE-X research paper (full example)
    │   ├── abstracttemplateaannotated.md
    │   └── introductionannotated.md
    ├── paperreview.md             # 5-dimension adversarial self-review
    ├── figuresandtables.md        # Visual standards + anti-patterns gallery
    └── doesmywritingflowsource.md # Paragraph flow diagnostics
```

---

## The Pipeline

```
🎠 WIZARD          →  Generate skeleton with section prompts
🔮 IDEATION        →  Shannon Filter, impact analysis, audience profiling
⚡ WRITE           →  One paragraph at a time, one message per paragraph
⚡+🔮 VERIFY       →  claim_checker.py, reverse outlining
🔮 REVIEW         →  5-dimension adversarial self-review
📄 FORMAT         →  generate_pdf.py, generate_figures.py
✅ SUBMIT         →  Ready for reviewers, investors, or editors
```

---

## Key Principles

1. **Idea quality before writing.** The Shannon Filter determines if your idea deserves to exist as a document. If the idea fails, do not write.
2. **Impact over information.** Being correct is not enough. You must be unignorable. Every sentence must earn its place.
3. **Claim-evidence alignment.** Every claim maps to specific experimental evidence. No orphan claims. No "could potentially" or "may allow."
4. **Audience-first thinking.** Write for a skeptical reader who wants to reject, fund, or ignore your document. Remove every excuse they could use.
5. **Visual-first impression.** Figures and tables are consumed before text. They must tell the complete story without reading a single word of prose.
6. **Zero dashes.** No em dashes, en dashes, or double hyphens. Commas and colons only. Enforced by `clean_dashes.py`.
7. **Active voice.** "We propose" not "It is proposed." State what changed before explaining how.

---

## Quality Rules

### Writing Mechanics
- One paragraph = one message. First sentence states the message.
- Define all terms before using them. No forward references.
- Maintain terminology stability across the entire document.
- Sentence-to-sentence flow: cause, contrast, consequence, or refinement.
- Quantify every claim: "3.2x faster" not "significantly faster."

### Tables
- Caption ABOVE the table.
- Booktabs style: no vertical lines, no double rules.
- Highlight best and second-best values.
- Label metric direction: PSNR ↑, LPIPS ↓, Runtime (ms) ↓.
- Consistent decimal places within each metric column.

### Figures
- Every figure must have a clear message visible without reading the caption.
- Vector graphics (PDF/SVG) for diagrams, high-resolution PNG for photos.
- Colorblind-friendly palette (viridis, cividis, or ColorBrewer).
- Figure captions are content, not decoration. State what to observe and the conclusion.

### Citations
- Prefer recent papers (last 3 years) for SOTA comparisons.
- Cite the original source, not a survey that mentions it.
- Format consistently: author-year or numeric depending on venue.
- Use `semantic_scholar.py` for search and formatting.

---

## Requirements

- **Python 3.10+** ([python.org](https://python.org))
- **pip packages**: `pip install -r requirements.txt`
  - `markdown` (HTML conversion)
  - `fpdf2` (PDF generation, pure Python)
  - `weasyprint` (best PDF typography, optional, needs GTK3 on Windows)
  - `matplotlib` (figures and charts)

Semantic Scholar API is free, no key required. Rate limiting is handled with exponential backoff.

---

## Installation

### Claude Code (Recommended)

```bash
git clone https://github.com/loopiak/korroresearch.git ~/.claude/skills/korroresearch
cd ~/.claude/skills/korroresearch
pip install -r requirements.txt
```

The skill activates automatically. Just mention "research paper," "pitch deck," "grant proposal," or invoke it directly with `/korroresearch`.

### Standalone

```bash
git clone https://github.com/loopiak/korroresearch.git
cd korroresearch
pip install -r requirements.txt
python scripts/wizard.py
```

### Windows Users

PDF generation uses fpdf2 by default (zero system dependencies). For weasyprint's superior typography with two-column academic layout, install GTK3:

```bash
# Option 1: MSYS2 (recommended)
pacman -S mingw-w64-x86_64-gtk3

# Option 2: gvsbuild
pip install weasyprint
gvsbuild build gtk3
```

Either way, `generate_pdf.py` always produces a PDF. The best available engine is selected automatically.

---

## Development

```bash
# Run all checks
python scripts/clean_dashes.py --check
python scripts/claim_checker.py output/paper_draft.md --strict

# Run a single script with full help
python scripts/wizard.py --help
```

All scripts use `argparse`. All have `--help`. All handle `KeyboardInterrupt` cleanly. Exit codes: 0 = success, 1 = error, 130 = interrupted.

---

## Complete Example

The repository includes a fully written research paper generated with KORRO Research:

**[MUE-X: Multi-User Environment for Cross-Modal Agents with Shared Memory and Zero-Shot Task Transfer](references/examples/muex_paper.md)**

This paper demonstrates every principle and script in action:
- Generated with `wizard.py --format paper --batch`
- Claims verified with `claim_checker.py --strict` (33 claims, 0 needs_evidence)
- Formatted as publication-ready PDF with `generate_pdf.py`
- Zero dashes, verified with `clean_dashes.py --check`

---

## License

MIT — see [LICENSE](LICENSE)

---

Built with the conviction that writing cannot save a bad idea, but bad writing can kill a great one.
