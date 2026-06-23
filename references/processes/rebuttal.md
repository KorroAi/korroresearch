# Rebuttal / Reviewer Response Guide

## Goal

Convert a rejection or major revision into acceptance by addressing every reviewer concern completely, respectfully, and convincingly.

## Core Principles

1. **Never argue.** Even if the reviewer is wrong, they are still the gatekeeper. Thank them first, then address.
2. **Every comment gets a response.** No exceptions. Unanswered comments signal disrespect.
3. **Make the reviewer's job easy.** Format your response so they can verify each point in seconds.
4. **Show, don't tell.** For every "we fixed this," include the exact new text or figure.

## Response Structure

### Opening Letter

```
Dear [Area Chair / Editor / Reviewers],

We thank the reviewers for their careful reading and constructive feedback.
We have addressed every comment in detail below. Major changes include:

1. [Change 1 — one sentence]
2. [Change 2 — one sentence]
3. [Change 3 — one sentence]

We believe these revisions fully address all concerns raised.
```

### Per-Reviewer Response Format

For each reviewer:

```
## Response to Reviewer [N]

We thank Reviewer [N] for their [insightful / detailed / constructive] feedback.

### Comment 1: [Short quote or summary]
[Our response — 3-5 sentences max]
[Action taken — exact new text, table, figure reference]
[Location: Section X, Page Y]

### Comment 2: ...
```

## Tone Rules

| Wrong | Right |
|---|---|
| "The reviewer misunderstood..." | "We apologize for the unclear presentation. We have clarified..." |
| "This is beyond the scope of our work." | "We acknowledge this limitation. We have added a discussion in Section X noting that..." |
| "We cannot run this experiment." | "We agree this would strengthen the paper. We have added [alternative] and discussed this as future work in Section Y." |
| "The reviewer is incorrect." | "We respectfully note that [evidence]. However, we have rephrased the text to avoid this confusion." |

## Common Reviewer Comments and Responses

### "Missing baseline X"
- If feasible: add the baseline and report results.
- If infeasible: explain why (closed-source, unavailable), add a discussion, and if possible add a proxy comparison.

### "Ablation is insufficient"
- Add the requested ablations.
- If they are redundant with existing ones, explain the existing evidence and add a clarifying sentence.

### "Writing needs improvement"
- Do not just say "we improved the writing."
- List every section you rewrote, with examples of before/after.

### "The contribution is marginal"
- Clarify the specific gap your work fills.
- Add a stronger contrast with closest prior work.
- Re-frame from the challenge perspective (see introduction guide).

### "Method seems simple / obvious"
- Acknowledge that the best solutions often appear simple in hindsight.
- Emphasize that nobody did it before you.
- Show the non-obvious insight that led to the approach.

## Quality Checklist
- [ ] Every reviewer comment addressed individually
- [ ] No argumentative or defensive language
- [ ] Every change includes the actual new text (not just "we changed this")
- [ ] Section and page numbers for every change
- [ ] Color-coded diff if the venue allows (red = old, blue = new)
- [ ] Opening letter summarizes major changes
- [ ] Response is self-contained (reviewer does not need to read the revised paper to judge changes)
