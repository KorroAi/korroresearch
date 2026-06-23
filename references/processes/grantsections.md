# Grant Proposal Sections, Beyond the Research Paper

## Goal

Write the sections unique to grant proposals that have no equivalent in research papers. Research papers need abstract, intro, method, experiments, conclusion. Grant proposals need all of that PLUS budget, timeline, preliminary results, broader impact, and a cover letter.

---

## Section 1: Specific Aims (1 page)

The most important page of the grant. Most reviewers decide based on this page alone.

### Structure
```
Paragraph 1: The PROBLEM — what is the gap, and why is it urgent?
Paragraph 2: The APPROACH — what will you do, and why will it work?
Paragraph 3: The IMPACT — what changes if you succeed?
```

### Rules
- One page only. No exceptions for NIH R01, NSF CAREER, or ERC.
- Bold your hypothesis or central claim so it jumps off the page.
- No citations (save them for the research strategy).
- No jargon that a panel member outside your subfield would not understand.
- End with a sentence that makes NOT funding feel irresponsible.

### Example (bad → good)
```
Bad:  "This proposal aims to investigate novel approaches to
       gradient compression for distributed deep learning."

Good: "Training large neural networks requires hundreds of GPUs
       communicating gradients at every step — a bottleneck that
       wastes 60% of compute cycles. We will develop the first
       lossless compression framework that eliminates this waste
       with zero accuracy degradation, reducing training costs
       by 3x across vision, language, and scientific ML workloads."
```

---

## Section 2: Preliminary Results

The second most important section. Without preliminary results, your proposal is a wish, not a plan.

### What Counts as Preliminary
- Experimental data showing feasibility on a small scale
- A prototype that works on a subset of the problem
- Published papers by your group on related methods
- Negative results that motivated your approach (these are UNDERUSED and powerful: "We tried X, it failed because Y, which led us to Z")

### Structure
```
For each preliminary result:
  1. What we did (1 sentence)
  2. What we found (1 sentence + figure/table)
  3. What it implies for the proposed work (1 sentence)
```

### Rules
- Every preliminary result must directly connect to a specific aim.
- Show error bars. Preliminary results without statistics are not results.
- If you have zero preliminary results, you are not ready to submit. Go back to the lab.

---

## Section 3: Budget Justification

Reviewers skim the budget. The justification must make every line item feel non-negotiable.

### Structure
| Category | Amount | Justification |
|---|---|---|
| Personnel | $X | Postdoc for 24 months: will execute Aim 2 experiments. PhD student for 36 months: will develop Aim 1 methods. |
| Equipment | $X | 4× A100 GPUs: required for large-scale experiments. Existing cluster is oversubscribed 3:1. |
| Travel | $X | 2 conference presentations per year + 1 collaborator visit. |
| Materials | $X | Cloud compute credits for baseline reproduction. |

### Rules
- Round to reasonable numbers. "$143,276.42" looks like you made it up. "$143,000" looks professional.
- Every line item must be traceable to a specific aim or activity.
- Personnel costs must match your institution's published rates. Check before writing.
- If your budget is above the program limit, cut before submitting. It will be rejected unread.

---

## Section 4: Timeline and Milestones

Show that you have thought about execution, not just ideas.

### Format
```
Year 1, Q1-Q2: Hire postdoc. Set up infrastructure. Reproduce baselines.
  Milestone: Baseline reproduction complete. Initial prototype running.

Year 1, Q3-Q4: Execute Aim 1. First-pass implementation of core method.
  Milestone: Prototype achieves 2x compression on benchmark datasets.
  Risk: Encoding overhead may exceed projections. Mitigation: Fallback to simpler scheme.

Year 2, Q1-Q2: Execute Aim 2. Scale to production workloads.
  Milestone: End-to-end training with full pipeline on 64+ GPUs.
  Risk: Scaling may expose communication bottlenecks. Mitigation: Profiling + optimization phase.

Year 2, Q3-Q4: Execute Aim 3. Generalization studies. Write papers.
  Milestone: Results on 3+ modalities. 2 papers submitted.

Year 3, Q1-Q2: Refinement. Open-source release. Documentation.
  Milestone: Public release with tutorials and pre-trained models.
```

### Rules
- One milestone per quarter minimum.
- Every risk must have a mitigation. No mitigation = you have not thought about it.
- Include "write papers" and "release code" as milestones. They are real work.
- The timeline must match the budget period exactly.

---

## Section 5: Broader Impact

Not boilerplate. The weakest section in most proposals. Make it your strongest.

### Components
1. **Scientific impact**: Who else benefits from this work? Name specific communities, not "the field."
2. **Societal impact**: What changes in the world if you succeed? Be specific. "Reducing training costs by 3x makes large-scale ML accessible to academic labs without industry compute budgets, democratizing AI research."
3. **Education and outreach**: Workshops, tutorials, curriculum integration, undergraduate research.
4. **Open science**: Code, data, models released under what license? When?

### Rules
- No "this research could potentially benefit society." Name the benefit or cut the sentence.
- If your broader impact involves "workshops for underrepresented groups," name the specific groups and the specific workshops. Vague promises read as insincere.
- Open-source commitment must include a license, a timeline, and a maintenance plan.

---

## Section 6: Cover Letter (if allowed)

Most grants do not require one. If they do, treat it like an abstract.

### Template
```
Dear [Program Officer / Review Panel],

[Problem and urgency — 2 sentences]

[Our approach and why it will work — 2 sentences]

[Why we are the right team — 1 sentence citing relevant expertise]

[Funding requested and timeline — 1 sentence]

Respectfully,
[PI Name]
```

---

## Quality Checklist
- [ ] Specific Aims: one page, bolded hypothesis, ends with urgency
- [ ] Preliminary results: every result connected to an aim, error bars present
- [ ] Budget: every line item traceable to activity, personnel rates verified
- [ ] Timeline: one milestone per quarter, every risk has mitigation
- [ ] Broader impact: specific beneficiaries named, open-source plan concrete
- [ ] Cover letter: fits on one page, names the program officer if known
