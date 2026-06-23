# Research Paper Pro, QuickStart

**38 reference files. You need the right ones for YOUR mission. Pick your path.**

---

## PATH 0, I've never written anything. Where do I start?

This is the most common question. You have an idea, a project, or a goal, but you've never published, never pitched, never spoken at a conference. Here is your exact path, no experience required.

```
┃  Step 1: python scripts/wizard.py
│          Choose format [1] Research Paper. It's the foundation.
│
┃  Step 2: Just answer the questions. If you don't know an answer,
│          type "I don't know yet" — the wizard still generates your skeleton.
│
┃  Step 3: Open the generated file. Each section has a prompt in comments.
│          Don't try to write perfectly. Just fill in what you know.
│
┃  Step 4: When you're stuck (and you will be):
│          → Load references/sections/abstract.md — it shows you HOW to write each section
│          → Ask Claude: "I'm stuck on my abstract. Here's what I have so far: [...]
│            Help me improve it using the researchpaperpro skill."
│
┃  Step 5: After you have a rough draft:
│          → references/processes/ideation.md — check if your idea is strong
│          → references/processes/impact.md — make it unignorable
│
┃  Step 6: Polish and submit:
│          → python scripts/clean_dashes.py paper.md
│          → python scripts/generate_pdf.py paper.md paper.pdf
│          → Submit to arXiv (free, instant, no peer review — great first step!)
│          → Then submit to a conference (see references/processes/venues.md)
```

**Estimated time**: 4 weeks for a beginner's first draft. That's normal. Don't rush.

**What happens after?** → PATH 4 (be recognized). Your paper → talk → magazine → investor. The flywheel.

---

## PATH 1, I want to publish a research paper

```
┃  python scripts/wizard.py --format paper
┃
┃  Then, in order:
┃  1. references/processes/ideation.md     ← Is your idea worth it?
┃  2. references/processes/impact.md       ← Make it unignorable
┃  3. references/sections/title.md         ← The title is strategy
┃  4. references/sections/abstract.md      ← Write this first
┃  5. references/sections/introduction.md  ← Then this
┃  6. references/sections/method.md        ← Most factual, easiest
┃  7. references/sections/experiments.md   ← Evidence for every claim
┃  8. references/paperreview.md            ← Before submitting
┃  9. python scripts/claim_checker.py paper.md --strict
┃  10. python scripts/generate_pdf.py paper.md paper.pdf
```

**Estimated time to first draft**: 2 weeks.

---

## PATH 2, I want to raise money (pitch deck + investor dossier)

```
┃  python scripts/wizard.py --format pitch-deck
┃
┃  Then, in order:
┃  1. references/processes/impact.md       ← Investors see 500 decks/year
┃  2. references/processes/audience.md     ← What makes a VC say yes?
┃  3. references/formats/pitchdeck.md      ← The 12-slide template
┃  4. references/processes/dossier.md      ← Deck + exec summary + financials
┃  5. references/processes/recognition.md  ← Build reputation BEFORE fundraising
```

**Estimated time to first draft**: 1 week.

---

## PATH 3, I want to write a book

```
┃  python scripts/wizard.py --format book
┃
┃  Then, in order:
┃  1. references/processes/ideation.md     ← The ONE mental model
┃  2. references/processes/impact.md       ← Principle 4: book arc
┃  3. references/processes/coauthoring.md  ← If multi-author
┃  4. references/processes/end-to-end.md   ← Book timeline (6-12 months)
```

**Estimated time to first chapter**: 1 month.

---

## PATH 4, I want to be recognized (conferences, magazines, investors)

```
┃  python scripts/wizard.py --format talk
┃
┃  Then, in order:
┃  1. references/processes/recognition.md  ← The 12-month plan
┃  2. references/processes/dossier.md      ← Your complete package
┃  3. references/processes/audience.md     ← Know every audience
┃  4. references/formats/magazine.md       ← Magazine articles
┃  5. references/formats/pitchdeck.md      ← Investor pitches
┃  6. references/formats/presentation.md   ← Conference talks
```

**Estimated time to first talk**: 1 week.

---

## Universal Rule

**Always run these three first, no matter what:**

1. `python scripts/wizard.py`, generates your skeleton
2. `references/processes/ideation.md`: the Shannon Filter
3. `references/processes/impact.md`: the 8 unignorable principles

**Complete beginner?** PATH 0 above walks you through everything step by step.

Everything else is optional until you need it.

---

## Quick Commands

```bash
# Start any project
python scripts/wizard.py
python scripts/wizard.py --format pitch-deck
python scripts/wizard.py --format grant

# Find papers to cite
python scripts/semantic_scholar.py search "your topic" --limit 5 --format apa

# Generate publication figures
python scripts/generate_figures.py bar --data results.json --output figure.pdf

# Check your claims against evidence
python scripts/claim_checker.py paper.md --strict

# Generate final PDF
python scripts/generate_pdf.py paper.md paper.pdf

# Clean typographic dashes
python scripts/clean_dashes.py paper.md
```
