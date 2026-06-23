# End-to-End Process  --  From Blank Page to Submit

## Goal

A complete timeline and checklist for authors writing their first paper, grant, book, or thesis. No guide covers the full process. This one does.

## The Universal Timeline

### T-8 weeks: Story and Outline
- [ ] Run `ideation.md` Shannon Filter. Idea passes?
- [ ] Run `impact.md`. What's the ONE thing? Who's the hero?
- [ ] Run `audience.md`. Who decides? What changes their mind?
- [ ] Choose format and venue. Load `venues.md` if unsure.
- [ ] Write the one-paragraph story: problem, why unsolved, our answer, evidence.
- [ ] Write section-level outline. One sentence per planned section.
- [ ] Share outline with co-authors. Align before writing.

### T-6 weeks: First Draft
- [ ] Write Abstract first (`abstract.md`)  --  it forces clarity on the story.
- [ ] Write Introduction (`introduction.md`). This will be rewritten later; write it now anyway.
- [ ] Write Method (`method.md`). Most factual section, easiest to write early.
- [ ] Write Experiments plan (`experiments.md`). What claims need evidence? Run remaining experiments.
- [ ] Write Related Work (`relatedwork.md`) only AFTER you know your contribution.
- [ ] Write Conclusion draft.
- [ ] **Anti-perfectionism rule**: The first draft is supposed to be bad. Write fast. Revise later.

### T-5 weeks: Internal Review Round 1
- [ ] Lead author reads full draft end-to-end. Fixes terminology, flow, contradictions.
- [ ] Each co-author reads and comments.
- [ ] Run `paperreview.md` five-dimension self-review.
- [ ] Run Protocol 6 (anti-paper) from `ideation.md`.
- [ ] Run `claim_checker.py --strict`. Every claim has evidence?
- [ ] Run `doesmywritingflowsource.md` reverse outlining on each section.

### T-4 weeks: Major Revision
- [ ] Address every issue from internal review.
- [ ] Rewrite Introduction completely (it always needs it).
- [ ] Ensure every figure passes the "message without caption" test.
- [ ] Run `clean_dashes.py`.
- [ ] Check all citations. Recent and relevant?
- [ ] Check all equations. Consistent notation? All symbols defined?

### T-3 weeks: Internal Review Round 2
- [ ] Senior author reads for technical correctness.
- [ ] External reader (someone NOT on the project) reads for clarity.
- [ ] Run the "read-only-first-sentences" test: do the topic sentences alone tell the story?
- [ ] Run the "read-only-figures" test: do figures and captions alone tell the story?

### T-2 weeks: Polish
- [ ] Final formatting: template, margins, page limits.
- [ ] Final figure quality: vector, readable fonts, colorblind-safe.
- [ ] Final table formatting: booktabs, best values bold, arrow indicators.
- [ ] Final citation check: all references cited, no missing entries.
- [ ] Proofread: read aloud every sentence. If you stumble, rewrite.
- [ ] Abstract word count within venue limit.
- [ ] Title passes the `title.md` protocol.

### T-1 week: Pre-Submission
- [ ] Format check: compile LaTeX/PDF, verify page count, verify no overfull boxes.
- [ ] Anonymization check (if double-blind): remove author names, acknowledgments, identifying citations.
- [ ] Supplementary material ready and cross-referenced.
- [ ] Code and data release ready (anonymized if needed).
- [ ] Cover letter written (if journal).
- [ ] All co-authors give final approval.

### T-0: Submit
- [ ] Submit. Do not re-read the paper. You will find a typo. It does not matter.
- [ ] Schedule the "what did we learn" post-mortem for after reviews come back.
- [ ] Start the next project.

---

## Timeline by Format

| Format | Total Time | Key Difference |
|---|---|---|
| Conference paper | 8 weeks | Hard deadline. No extensions. |
| Journal paper | 12-16 weeks | Rolling deadline. Can iterate more. |
| Grant proposal | 12 weeks | Preliminary results must exist before writing. |
| Thesis | 6-12 months | Write as you go, not at the end. |
| White paper | 4-6 weeks | Faster cycle. Less formal review. |
| Pitch deck | 2-4 weeks | Iterate with live feedback from friendly investors. |
| Blog post | 1-2 weeks | Ship fast. You can edit after publishing. |

---

## The Three-Reader Rule

Before submitting, ensure three people have read the full document:

1. **Domain expert**  --  Catches technical errors, missing baselines, related work gaps.
2. **Intelligent non-expert**  --  Catches unclear writing, undefined terms, missing motivation.
3. **The skeptic**  --  Actively tries to reject. Every weakness they find is a weakness reviewers will find.

If you cannot find three readers, you are not ready to submit.

---

## When to Stop

Signs the paper is ready:
- Each revision cycle produces fewer than 5 changes.
- You are moving commas around, not rewriting paragraphs.
- You can state the contribution in one sentence without hesitation.
- The anti-paper feels weak. You struggle to find genuine criticisms.
- You would rather submit than revise one more time. This is a real signal. Trust it.

Signs the paper is NOT ready:
- You know there is a weakness you are hoping reviewers will not notice.
- A section still feels "placeholder."
- You cannot explain Figure 3 to a colleague in 10 seconds.
- The abstract uses "could potentially" or "may allow."

---

## The Post-Submission Protocol

After submitting, do not:
- Re-read the paper immediately (you will find a typo and panic).
- Check the submission portal obsessively.
- Start rewriting before reviews come back.

Instead, do:
- Archive the source code and data.
- Write a one-page "what we would do differently" reflection.
- Start the next project.
