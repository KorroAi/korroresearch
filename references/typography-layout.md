# Typography and Layout — Professional Document Standards

## Goal

A document that looks amateur is treated as amateur. Typography and layout are not decorative. They are the first signal of quality the reader receives, before reading a single word. This guide enforces the rules that make documents look professionally typeset, not word-processor default.

## The Golden Rule

**If it looks like a Word document with default settings, it is wrong.** Professional documents are distinguished by consistent font hierarchy, generous but not wasteful margins, proper line spacing, and attention to invisible details: the space between paragraphs, the alignment of captions, the suppression of widows and orphans. These details are invisible when correct and glaring when wrong.

---

## Typography Rules

### Rule 1: Font Hierarchy (NON-NEGOTIABLE)

Every document must use exactly three font sizes, no more, no less. The hierarchy must be instantly scannable.

| Level | Size | Weight | Style | Usage |
|-------|------|--------|-------|-------|
| H1 (title) | 16-18pt | Bold | Normal | Document title only |
| H2 (section) | 12-14pt | Bold | Normal | Major sections |
| H3 (subsection) | 10-11pt | Bold Italic | Normal | Subsections |
| Body | 10-11pt | Regular | Normal | All paragraph text |
| Caption/note | 8-9pt | Regular | Italic | Figure/table captions, footnotes |

**Anti-patterns**: 
- More than four heading levels (H4+ is noise)
- Body text below 9pt (illegible) or above 11pt (looks like a children's book)
- Bold used for emphasis in body text (use italics for emphasis, bold only for structural hierarchy)

### Rule 2: Font Families

**Serif for body text.** Serif fonts guide the eye along the line and are proven to improve reading speed and comprehension for continuous text. Sans-serif is acceptable for headings, figure labels, and code, but never for body paragraphs in a professional document.

| Context | Font | Fallback |
|---------|------|----------|
| Body text | Times New Roman, STIX Two Text, or DejaVu Serif | Georgia, serif |
| Headings | Same as body, bold | — |
| Code blocks | Courier New, DejaVu Sans Mono | monospace |
| Figure labels | Same as body or Helvetica | sans-serif |

**Anti-patterns**: 
- Sans-serif body text (reads as informal, blog-post, or slide-deck style)
- Mixed serif and sans-serif in the same paragraph
- Decorative, script, or display fonts in any academic document

### Rule 3: Line Spacing (Leading)

Line spacing must be 1.3 to 1.5 times the font size. Tighter spacing reduces readability. Looser spacing wastes space and looks padded.

| Font Size | Line Spacing |
|-----------|-------------|
| 10pt body | 14-15pt (1.4-1.5x) |
| 11pt body | 15-16pt (1.4-1.45x) |
| 12pt headings | 16-18pt (1.3-1.5x) |
| 8pt captions | 11-12pt (1.4-1.5x) |

### Rule 4: Measure (Line Width)

Lines of body text must be 60 to 75 characters wide. Narrower lines cause excessive hyphenation and ragged right edges. Wider lines cause the eye to lose its place when scanning back to the start of the next line.

**Check**: Count characters in a full line. If fewer than 55, widen the text block or reduce font size. If more than 80, narrow the text block or increase font size.

---

## Layout Rules

### Rule 5: Page Geometry

| Parameter | Value |
|-----------|-------|
| Page size | A4 (210 x 297mm) |
| Top margin | 22-25mm |
| Bottom margin | 22-25mm |
| Inner/left margin | 20-25mm |
| Outer/right margin | 20-25mm |
| Header/footer space | 12-15mm from edge |

Margins must be generous enough that the text block feels framed, not cramped, and large enough to hold the document without thumbs covering content. Equal left and right margins are acceptable for single-sided documents. Bound documents need a larger inner margin (25-30mm).

### Rule 6: Paragraph Spacing

Two valid approaches, never mixed in the same document:

**Approach A (Preferred for academic)**: First-line indent of 4-6mm (0.4-0.6cm), no space between paragraphs. This is the traditional typesetting standard. It signals continuity of thought while providing visual paragraph separation.

**Approach B (Preferred for business)**: No indent, 4-6pt space between paragraphs. Cleaner, more modern. Acceptable for white papers, reports, and pitch decks.

**Anti-pattern**: Both indent AND space between paragraphs. This is redundant and marks amateur formatting.

### Rule 7: Widows and Orphans (NON-NEGOTIABLE)

- **Widow**: A single line of a paragraph at the TOP of a page. FORBIDDEN.
- **Orphan**: A single line of a paragraph at the BOTTOM of a page. FORBIDDEN.
- **Solution**: Adjust page breaks, slightly adjust spacing, or reword the paragraph so at least 2 lines appear together at page top or bottom.

### Rule 8: Page Numbering

Every page after the first must be numbered. Page numbers appear centered at the bottom or aligned to the outer edge. Font: same as body, 8-9pt.

First page (title page): no page number.
Front matter (table of contents, preface): Roman numerals (i, ii, iii).
Main content: Arabic numerals (1, 2, 3).

### Rule 9: Headers and Footers

Headers/footers are optional but must be consistent if used. 
- Header: Document title (left) or section title (left) + page number (right). 8pt, same font as body.
- Footer: Page number only (center) or author name (left) + page number (right).
- No decorative lines, no colored backgrounds, no logos in headers/footers of academic documents.

---

## Figure and Table Rules

### Rule 10: Figure Placement

- Figures must appear AFTER their first citation in the text, never before.
- Figures must be centered horizontally.
- Figure width must be either full text width or exactly half text width. No arbitrary widths.
- Vector graphics (PDF, SVG) for diagrams. High-resolution PNG (300dpi+) for photos and screenshots.
- Every figure must have a numbered caption BELOW the figure. Caption format: "Figure 1: Description." in 8-9pt italic.

### Rule 11: Table Formatting

- Tables use booktabs style: horizontal rules only (top, header separator, bottom). NO vertical rules. NO double rules.
- Table caption ABOVE the table. Format: "Table 1: Description." in 8-9pt italic.
- Column alignment: text columns left-aligned, number columns right-aligned or decimal-aligned.
- Best and second-best values may be highlighted with subtle bold or gray background. Never use color alone to convey information.
- Tables must fit within the text block width. If a table is too wide, reduce font size to 8pt minimum or rotate the page to landscape.

### Rule 12: Cross-References

- All figures and tables must be referenced in the text before they appear.
- Reference format: "Figure 1 shows..." or "As shown in Table 2..."
- Never use "the figure below" or "the table above" — figures may move during final layout.
- All cross-references must be verifiable. A reader must be able to find every referenced figure, table, and section.

---

## Pre-PDF Checklist

Before running `python scripts/generate_pdf.py`, verify:

- [ ] Exactly three font sizes used (H1, H2-H3, body)
- [ ] Serif font for all body text
- [ ] Line spacing between 1.3x and 1.5x font size
- [ ] Line width between 60 and 75 characters
- [ ] Margins at least 20mm on all sides
- [ ] No widows (single line at top of page)
- [ ] No orphans (single line at bottom of page)
- [ ] All pages after first are numbered
- [ ] All figures have captions BELOW
- [ ] All tables have captions ABOVE
- [ ] No vertical rules in tables
- [ ] Every figure and table is cited in text before it appears
- [ ] First-line indent OR paragraph spacing, never both
- [ ] Dashes removed (`python scripts/clean_dashes.py`)

Any unchecked box = document is not ready for output.

---

## Integration With the Skill

- Run this diagnostic as Phase C, Step 13, after readability check and before clean dashes.
- The `generate_pdf.py` script applies font hierarchy, margins, page numbering, and line spacing automatically.
- Widow/orphan control requires manual review after PDF generation.
- Figure and table rules are enforced during writing, not during PDF generation.
