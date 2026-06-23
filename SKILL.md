---
name: korroresearch
description: Universal academic and professional writing skill. Use whenever the user needs to write, draft, revise, or format any of: research paper, academic article, conference paper, journal submission, grant proposal, white paper, literature review, academic book, thesis, dissertation, technical blog post, pitch deck, investor deck, conference talk, keynote, or poster. Triggers on: "research paper", "academic paper", "write a paper", "paper draft", "conference paper", "journal article", "scientific writing", "grant proposal", "literature review", "white paper", "academic book", "thesis", "dissertation", "publishable", "IEEE format", "ACM format", "NeurIPS format", "Nature style", "peer review", "camera ready", "arxiv", "rebuttal", "reviewer response", "pitch deck", "investor deck", "keynote", "technical blog", "blog post", "dissertation defense", "impact", "unignorable". Even if the user only mentions one section, use this skill: it contains section-specific templates and review checklists for every format.
---

# KORRO Research

**One command. Answer questions. Get a complete document skeleton.**

```bash
python scripts/wizard.py
```

9 formats. 38 reference guides. One wizard that takes you from blank page to complete skeleton in 60 seconds. Pick your path: Researcher. Founder. Author. Speaker.

**[QUICKSTART.md →](QUICKSTART.md)** — 4 paths, exact sequence of files to load + commands to run.

---

## Core Philosophy

A document is not a data dump. It is a persuasive argument that changes what the reader believes is possible. Every sentence must earn its place. This applies to research papers, grant proposals, white papers, books, theses, pitch decks, and talks equally.

Five pillars — format-agnostic, always apply:
1. **Idea quality before writing** — Writing cannot save a bad idea. Run `references/processes/ideation.md` first. If the idea fails the Shannon Filter, do not write.
2. **Impact over information** — Being correct is not enough. You must be unignorable. Run `references/processes/impact.md` before any section writing.
3. **Claim-evidence alignment** — Every claim must map to evidence. No orphan claims. No "could potentially."
4. **Audience-first thinking** — Write for a skeptical reader who wants to reject/fund/ignore your document. Remove every excuse they could use.
5. **Visual-first impression** — Figures, slides, and tables are consumed first. They must tell the story without reading the text.
6. **Readability and fluidity** — Every sentence must be a pleasure to read. Run `references/doesmywritingflowsource.md` before finalizing. Good writing is not about complexity. It is about clarity, rhythm, and forward momentum.

---

## Format Decision Tree

Before writing, determine the right format. If unsure, answer these questions:

```
Q1: "Do I have a single clear technical insight?"
    YES → Conference paper or workshop paper
    NO  → Go to Q2

Q2: "Do I need funding to execute this work?"
    YES → Grant proposal
    NO  → Go to Q3

Q3: "Am I synthesizing existing knowledge, not presenting new results?"
    YES → Literature review, academic book, or white paper
    NO  → Go to Q4

Q4: "Is my audience investors / executives / non-specialists?"
    YES → Pitch deck, white paper, or technical blog post
    NO  → Journal paper, thesis, or technical report
```

---

## Quick Workflow

### Phase A — Before Writing (MANDATORY)

0. **Run the wizard** — `python scripts/wizard.py` — generates a complete document skeleton with section prompts. Choose your format. Answer the questions. Get writing in 60 seconds.
1. **Ideation diagnostic** — `references/processes/ideation.md`
   - Passes the Shannon Filter? Proceed. Fails? Return to research.
2. **Impact meta-guide** — `references/processes/impact.md`
   - What worldview are you destroying? What's the ONE thing? Who's the hero?
3. **Audience analysis** — `references/processes/audience.md`
   - Who is reading? What do they believe? What makes them say yes?
4. **Choose format** — Use the decision tree above. Load the corresponding format guide.

### Phase B — Writing (iterative)

5. **Define the story** — One paragraph. Problem, why unsolved, your answer, evidence.
6. **Load the section guide** from `references/sections/` for the section you're writing.
7. **Write paragraph by paragraph** — One message per paragraph, first sentence states it.
8. **Reverse outline** after each section — Topic sentences must form a coherent mini-story.

### Phase C — Before Finalizing (MANDATORY)

9. **Adversarial review** — `references/paperreview.md` — 5-dimension self-review.
10. **Anti-paper test** — `references/processes/ideation.md` Protocol 6.
11. **Claim-evidence check** — `python scripts/claim_checker.py paper.md --strict`
12. **Readability and fluidity check** — `references/doesmywritingflowsource.md` — Full readability diagnostic. Sentence rhythm. Active voice. Transition flow. Paragraph variety. Filler elimination. Read-aloud test.
13. **Clean dashes** — `python scripts/clean_dashes.py paper.md`
14. **Generate output** — Format guide + corresponding script in `scripts/`.

### Phase D — Mastery (the level above)

14. **Mastery diagnostic** — `references/processes/mastery.md` — 7 dimensions that separate good from unforgettable. Taste. Danger. Obsession. Network. Anti-fragility. Timing. Voice. Run this AFTER all writing is done. This is what transforms "accepted" into "cited for 30 years."

---

## Section Guides (load only the one you need)

| Section | Reference File | When to Load |
|---|---|---|
| Abstract | `references/sections/abstract.md` | Writing or revising the abstract |
| Introduction | `references/sections/introduction.md` | Writing or revising the introduction |
| Related Work | `references/sections/relatedwork.md` | Writing or revising related work |
| Method | `references/sections/method.md` | Writing or revising the method section |
| Experiments | `references/sections/experiments.md` | Writing or revising experiments |
| Conclusion | `references/sections/conclusion.md` | Writing or revising the conclusion |
| Title | `references/sections/title.md` | **BEFORE writing — the title is strategic, not decorative** |
| Paper Review | `references/paperreview.md` | Before finalizing ANY draft |
| Figures & Tables | `references/figuresandtables.md` | Creating or improving figures/tables |

---

## Meta-Workflow Guides (load for process tasks)

| Process | Reference File | When to Load |
|---|---|---|
| **Ideation (IDEA QUALITY)** | `references/processes/ideation.md` | **Before any writing — does this idea deserve to exist?** |
| **Impact (UNIGNORABLE)** | `references/processes/impact.md` | **ALL FORMATS — 8 universal principles of unforgettable writing** |
| **Audience Analysis** | `references/processes/audience.md` | **Who reads this? What makes them say yes?** |
| End-to-End Process | `references/processes/end-to-end.md` | First-time authors: blank page to submit |
| Rebuttal / Reviewer Response | `references/processes/rebuttal.md` | Responding to peer reviews |
| Venue Selection | `references/processes/venues.md` | Choosing where to submit |
| Supplementary Material | `references/processes/supplementary.md` | Preparing appendices, extra results |
| Co-Author Workflow | `references/processes/coauthoring.md` | Multi-author collaboration, CRediT taxonomy |
| **Recognition (12-MONTH PLAN)** | `references/processes/recognition.md` | **Paper → talk → magazine → investor. The flywheel.** |
| **Dossier (COMPLETE PACKAGE)** | `references/processes/dossier.md` | **Paper + pitch + press kit + social proof. Ready to send in 5 minutes.** |
| **Mastery (THE LEVEL ABOVE)** | `references/processes/mastery.md` | **Taste. Danger. Obsession. Network. Anti-fragility. Timing. Voice. 7 unteachable dimensions.** |

---

## Output Format Guides

| Format | Reference File | Best For |
|---|---|---|
| LaTeX (IEEE/ACM) | `references/formats/latexieee.md` | Conference/journal submission (CS, engineering) |
| LaTeX (NeurIPS/ICML) | `references/formats/latexmlm.md` | ML conference submission |
| HTML -> PDF | `references/formats/htmlpdf.md` | Preprints, white papers, web |
| DOCX | `references/formats/docx.md` | Grant proposals, internal docs |
| Beamer/Reveal.js | `references/formats/presentation.md` | Conference talks, seminars |
| Pitch Deck | `references/formats/pitchdeck.md` | Investor decks, startup pitches |
| Blog Post | `references/formats/blogpost.md` | Technical essays, FAANG-style blog posts |
| Magazine Article | `references/formats/magazine.md` | Nature, Wired, MIT Tech Review, Quanta, The Atlantic |
| Grant Proposal Sections | `references/processes/grantsections.md` | Budget, timeline, broader impact, preliminary results |

---

## Global Quality Rules

### Writing Mechanics (ALL formats)
- Zero dashes of any kind. No em dashes, en dashes, or double hyphens. Use commas or colons instead. Run `scripts/clean_dashes.py` before finalizing.
- Prefer active voice. "We propose" not "It is proposed." Active voice creates forward momentum.
- Impact first: state what changed before explaining how.
- One paragraph = one message. First sentence states the message.
- Define all terms before using them. No forward references to unexplained concepts.
- Maintain terminology stability across the entire document.
- Sentence-to-sentence flow: cause, contrast, consequence, or refinement.

### Readability and Fluidity (ALL formats — NON-NEGOTIABLE)
The reader's attention is a depleting resource. Every sentence that is unpleasant to read steals attention from the next sentence. Run `references/doesmywritingflowsource.md` before finalizing any document.

- **Sentence rhythm**: Vary sentence length. A short sentence (4-8 words) creates impact. A medium sentence (12-22 words) develops an idea. A long sentence (25-40 words) synthesizes and connects. Monotony kills reading. Three long sentences in a row = the reader's eyes glaze over. Two short sentences in a row = punch. Alternate deliberately.
- **Active voice dominance**: At least 80% of sentences must use active voice. "We analyzed the data" not "The data was analyzed." Passive voice has its place (when the actor is unknown or irrelevant), but it should be the exception, not the default.
- **Filler elimination**: Remove "It is worth noting that," "Interestingly," "In order to," "It should be noted that," "It is important to mention," "The fact that." These phrases add syllables and remove nothing.
- **Concrete over abstract**: "The four-year-old stacking blocks" not "a young child engaging in constructive play." "Dopamine neurons fire in bursts" not "neurotransmitter release patterns exhibit phasic characteristics." Specific words create images. Abstract words create fog.
- **Paragraph rhythm**: Open with a short, clear topic sentence. Develop the idea in 2-4 supporting sentences. Close with impact or a transition. A paragraph of 8+ sentences needs to earn every one of them.
- **Read-aloud test**: Read every paragraph aloud. If you stumble, the reader will stumble. If you run out of breath, the sentence is too long. If it sounds like a robot wrote it, rewrite it.
- **Transition craft**: Each sentence must connect to the previous one with a clear logical relationship. Cause. Contrast. Consequence. Refinement. Example. If the relationship is unclear, add an explicit transition word or restructure.

### Claims and Evidence (research papers, grants, white papers)
- Every major claim must map to evidence (experiment, citation, or preliminary result).
- If a claim cannot be supported, weaken or remove it.
- Never use "could potentially", "may allow", "might be able to". Either it works or it does not.
- Quantify every claim possible: "3.2x faster" not "significantly faster".

### Tables (ALL formats)
- Caption ABOVE the table.
- Use booktabs style (no vertical lines, no double rules).
- Highlight best/second best values with subtle color.
- Label metric direction: PSNR ↑, LPIPS ↓, Runtime (ms) ↓.
- One table = one message. Consistent decimal places within each metric column.

### Figures (ALL formats)
- Every figure must have a clear message visible without reading the caption.
- Vector graphics (PDF/SVG) for diagrams, high resolution PNG for photos.
- Colorblind-friendly palette (viridis, cividis, or ColorBrewer).
- Figure captions are content, not decoration. State what to observe and the conclusion.
- See `references/figuresandtables.md` for anti-patterns gallery.

### Citations
- Use Semantic Scholar API: `python scripts/semantic_scholar.py search "query" --limit 5`
- Prefer recent papers (last 3 years) for SOTA comparisons.
- Cite the original source, not a survey that mentions it.
- Format consistently (author-year or numeric depending on venue).

---

## Document Types and Their Requirements

### Research Paper
| Subtype | Pages | Key Requirement | Section Guides |
|---|---|---|---|
| Conference Paper | 6-10 | One clear contribution. Ablation mandatory. Teaser figure mandatory. | `abstract.md`, `introduction.md`, `method.md`, `experiments.md` |
| Journal Paper | 12-20 | Deeper analysis. Failure cases. Supplementary material. | Same + `conclusion.md`, `supplementary.md` |
| Workshop Paper | 4-6 | Work in progress OK. Smaller scope. Higher acceptance. | Same, relax ablation requirement |
| Literature Review | 10-30 | Systematic search. Thematic synthesis. Gap identification. | `relatedwork.md` + `experiments.md` (for methodology) |

### Professional
| Subtype | Length | Key Requirement | Process Guides |
|---|---|---|---|
| White Paper | 5-20 pages | Executive summary first. Business impact + technical depth. | `impact.md`, `grantsections.md` |
| Technical Blog Post | 800-3000 words | One insight per post. Accessible opening. Code examples. | `blogpost.md` |
| Grant Proposal | 5-15 pages | Problem significance. Preliminary results. Budget + timeline. | `grantsections.md`, `impact.md` |
| Pitch Deck | 10-15 slides | Story arc. Traction. The ask. | `pitchdeck.md`, `impact.md` |

### Long-Form
| Subtype | Length | Key Requirement | Process Guides |
|---|---|---|---|
| Academic Book | 200-600 pages | Chapter organization. Pedagogical progression. Exercises. | `coauthoring.md` (if multi-author) |
| Thesis / Dissertation | 100-300 pages | Establish expertise. Deep methodology. Comprehensive lit review. | All section guides + `end-to-end.md` |

---

## Claim-Evidence Map (Required Before Finalizing)

| Claim | Evidence Source | Status |
|---|---|---|
| "Our method achieves X% improvement" | Table 2, Row 3 | supported |
| "Module Y is essential for Z" | Ablation Table 4 | supported |
| ... | ... | needs evidence |

Claims with "needs evidence" status must be resolved before the document is final.

---

## Execution Rules

1. **Before writing any prose**: Build a mini-outline with thesis, topic sentences, and evidence. This applies to ALL formats.
2. **For each subsection** (papers, grants, books): Explicitly include motivation, design, and contribution.
3. **For papers**: Never write incremental patch style. Frame from the challenge perspective, not the patching perspective.
4. **For grants**: Lead with the problem's significance and your unique capability to solve it. Preliminary results are non-negotiable.
5. **For white papers and pitch decks**: Open with the crisis or opportunity. The reader must feel urgency within 30 seconds.
6. **For books**: Each chapter must tell a complete story. The book as a whole must have an arc (see impact.md Principle 4).
7. **Keep terminology stable**: Do not rename the same concept across sections. Applies to ALL formats.
8. **Before finalizing**: Run `references/paperreview.md` five-dimension self-review. For papers, also run Protocol 6 (anti-paper) from `ideation.md`.
9. **After writing each section**: Run reverse outlining on that section before moving on.

---

## Output Contract

Adapt to request complexity:

| Request Scope | Deliverables |
|---|---|
| Full section or paper | 1. Compact outline (3-7 bullets) 2. Revised text with explicit paragraph roles 3. Self-review checklist 4. Claim-evidence map |
| Paragraph revision | 1. Revised paragraph 2. One-line rationale |
| Minor edit (phrasing, grammar) | 1. Revised text only |
| Review/feedback only | 1. Findings organized by severity 2. Specific fix for each finding |
| Format selection / decision | 1. Recommended format 2. Rationale 3. What changes if you chose differently |

---

## Reference Files Index

### Section Writing Guides
- `references/sections/abstract.md` — 3 abstract templates
- `references/sections/introduction.md` — 4 task intro versions, 3 challenge versions, 4 pipeline versions
- `references/sections/relatedwork.md` — Thematic vs chronological, gap identification
- `references/sections/method.md` — Technical clarity, reproducibility, notation consistency
- `references/sections/experiments.md` — 3 core questions, experiment planning, figure/table rules
- `references/sections/conclusion.md` — Summary without copy-paste, limitations, future work
- `references/sections/title.md` — **STRATEGIC.** The title is read 5x more than the abstract.

### Meta-Workflow Guides
- `references/processes/ideation.md` — **START HERE.** 7 protocols: Shannon filter, paper-first, territory map, cross-domain pollination, elegance razor, anti-paper, new language
- `references/processes/impact.md` — **ALL FORMATS.** 8 universal principles: worldview, one insight, audience as hero, inevitability, memorability, density, opening, call to action
- `references/processes/audience.md` — **BEFORE WRITING.** Who reads? What do they believe? How do they decide?
- `references/processes/recognition.md` — **12-MONTH FLYWHEEL.** Paper → talk → magazine → investor → repeat.
- `references/processes/dossier.md` — **COMPLETE PACKAGE.** Paper + pitch + press kit + social proof + website.
- `references/processes/mastery.md` — **THE LEVEL ABOVE.** Taste. Danger. Obsession. Network. Anti-fragility. Timing. Voice. 20-document curriculum.
- `references/processes/end-to-end.md` — Blank page to submit: timeline, revision cycles, when to stop.
- `references/processes/rebuttal.md` — Reviewer response: tone, structure, point-by-point
- `references/processes/venues.md` — Conference/journal selection: impact, audience, acceptance rate
- `references/processes/supplementary.md` — Supplementary material: content, organization, cross-referencing
- `references/processes/coauthoring.md` — Multi-author workflows, CRediT taxonomy, conflict resolution
- `references/processes/grantsections.md` — Grant-specific sections: budget, timeline, broader impact, preliminary results

### Quality Assurance
- `references/paperreview.md` — 5-dimension adversarial self-review
- `references/figuresandtables.md` — Publication-ready visuals + anti-patterns gallery
- `references/doesmywritingflowsource.md` — Paragraph clarity and flow diagnostics

### Output Formats
- `references/formats/latexieee.md` — IEEE/ACM conference-ready LaTeX
- `references/formats/latexmlm.md` — NeurIPS/ICML/ACL conference-ready LaTeX
- `references/formats/htmlpdf.md` — HTML + weasyprint for professional PDFs
- `references/formats/docx.md` — python-docx for editable documents
- `references/formats/presentation.md` — Beamer/Reveal.js for talks
- `references/formats/pitchdeck.md` — Investor pitch deck structure and design
- `references/formats/blogpost.md` — Technical blog posts, FAANG-style essays
- `references/formats/magazine.md` — Magazine articles: Nature, Wired, MIT Tech Review, Quanta, The Atlantic

### Executable Scripts
- `scripts/wizard.py` — **START HERE.** Interactive wizard: choose format, answer questions, get document skeleton: `python scripts/wizard.py` or `python scripts/wizard.py --format pitch-deck`
- `scripts/generate_pdf.py` — Markdown to publication PDF: `python scripts/generate_pdf.py paper.md paper.pdf [--template two-column|single-column]`
- `scripts/semantic_scholar.py` — Find and cite papers: `python scripts/semantic_scholar.py search "query" --limit 5 --format apa`
- `scripts/generate_figures.py` — Publication figures (bar, line, heatmap, ablation): `python scripts/generate_figures.py bar --data data.json --output figure.pdf`
- `scripts/claim_checker.py` — Verify claims map to evidence: `python scripts/claim_checker.py paper.md [--strict] [--json]`
- `scripts/clean_dashes.py` — Remove ALL dashes from prose (replaced with commas or colons): `python scripts/clean_dashes.py paper.md`

### Annotated Examples
- `references/examples/abstracttemplateaannotated.md` — Abstract with line-by-line annotation
- `references/examples/introductionannotated.md` — Introduction with section-by-section annotation
