# Co-Author Workflow Guide

## Goal

Collaborate with multiple authors on the same paper without version conflicts, inconsistent terminology, or fragmented prose.

## Authorship Criteria (ICMJE / standard)

Each author must have contributed to ALL of:
1. Substantial contributions to conception, design, data acquisition, analysis, or interpretation
2. Drafting or critically revising the paper for important intellectual content
3. Final approval of the version to be published
4. Agreement to be accountable for all aspects of the work

Contributors who do not meet all four criteria should be acknowledged, not listed as authors.

### Author Order, Conventions by Field

Author order is the #1 source of conflict in multi-author papers. Agree BEFORE writing.

| Field | Convention | Notes |
|---|---|---|
| Computer Science / ML | Contribution order | First author did the most work. Last author is senior/advisor. Middle authors in decreasing contribution. |
| Mathematics | Alphabetical | All authors equal. No significance to order. Do NOT change this without explicit agreement. |
| Physics / High-Energy | Alphabetical (large collaborations) | Often 100+ authors. Order is meaningless. |
| Biology / Medicine | First = did the work. Last = PI/senior. | Very strict. Changing order requires justification. |
| Economics | Alphabetical or contribution | Varies by subfield. Clarify early. |
| Humanities | Solo authorship is the norm | Multi-author is rare and signals equal contribution. |

**Conflict resolution**: If two co-authors cannot agree on order, use the CRediT taxonomy (below) as an objective reference. If still unresolved, the senior author (PI) decides.

### CRediT Taxonomy (Recommended)

Document each author's role explicitly using the CRediT standard:

| Role | Definition |
|---|---|
| Conceptualization | Ideas; formulation of research goals and aims |
| Data Curation | Management, cleaning, annotation of data |
| Formal Analysis | Mathematical, statistical, or computational analysis |
| Funding Acquisition | Obtaining financial support |
| Investigation | Conducting experiments or data collection |
| Methodology | Development or design of methodology |
| Project Administration | Management and coordination responsibility |
| Resources | Providing materials, reagents, computing, instrumentation |
| Software | Programming, software development, algorithm implementation |
| Supervision | Oversight and mentorship |
| Validation | Verification of results and reproducibility |
| Visualization | Preparation of figures, tables, and visual presentations |
| Writing, Original Draft | Preparation of the initial draft |
| Writing, Review & Editing | Critical review, commentary, and revision |

**Include in the paper** (many venues now require this):
```
Author Contributions:
Alice: Conceptualization, Methodology, Software, Writing — Original Draft.
Bob: Investigation, Data Curation, Validation.
Charlie: Supervision, Funding Acquisition, Writing — Review & Editing.
```

The CRediT table removes ambiguity. If two authors claim the same role, the one listed first contributed more to that role. Use this to resolve order disputes objectively.

## Workflow

### Git-Based (Recommended)

```
main (camera-ready target)
├── abstract
├── intro
├── related-work
├── method
├── experiments
└── conclusion
```

- One branch per section during drafting
- Merge to main only after all authors review
- Use Pull Requests for major section merges
- Keep the compiled PDF committed alongside source

### Overleaf / Collaborative LaTeX

- Use `\input{}` or `\include{}` for each section
- One author edits one file at a time
- Track changes with Overleaf history or git integration
- Comment mode for line-level feedback

### Markdown + Pandoc

Best for papers with eventual LaTeX output:
- Write sections as separate `.md` files
- Use pandoc to convert to LaTeX for final formatting
- Git-friendly, easy to diff
- Agree on a shared terminology glossary before writing

## Terminology Stability (CRITICAL)

Before writing begins, create a shared glossary:

```yaml
terms:
  method_name: "GradZip"  # never "Grad-Zip", "GradZip framework", "our compression method"
  main_metric: "gradient communication reduction"
  key_component_1: "runtime profiler"  # never "profiling module", "warmup analyzer"
  key_component_2: "variable-width encoding"  # never "adaptive encoding", "per-tensor encoding"
```

## Writing Division by Strengths

| Author Role | Best For |
|---|---|
| Lead author | Abstract, Introduction, Experiments |
| Senior author | Method (technical depth), Conclusion |
| Collaborator A | Related Work (literature knowledge) |
| Collaborator B | Experiments (running baselines, producing tables) |

## Review Protocol

### Internal Review (before submitting to external reviewers)

1. Lead author reads the full paper end-to-end. Fixes:
   - Terminology inconsistencies
   - Flow breaks between sections
   - Contradictory claims

2. Senior author reads for:
   - Technical correctness
   - Contribution framing
   - Missing related work

3. Each co-author reads the whole paper and flags:
   - Errors in their domain
   - Unclear passages (noting page/paragraph)

4. Lead author resolves all comments.

5. Final read-through by all authors.

## Timeline

| Milestone | T-? | Duration |
|---|---|---|
| Outline and story agreed | T-8 weeks | 3-5 days |
| First draft complete | T-6 weeks | 2 weeks |
| Internal review round 1 | T-5 weeks | 5 days |
| Revision | T-4 weeks | 1 week |
| Internal review round 2 | T-2 weeks | 3 days |
| Final polish | T-1 week | 1 week |
| Submit | Deadline | - |

## Conflict Resolution

When two authors disagree on a technical claim:
1. Find the data. If there is no data, run the experiment.
2. If running the experiment is impossible, weaken the claim to what both can agree on.
3. The senior author breaks ties on framing decisions after all evidence is reviewed.

## Quality Checklist
- [ ] Terminology glossary created and shared before writing
- [ ] Each section has a single primary author
- [ ] All authors have read and approved the full paper
- [ ] Authorship criteria met for every listed author
- [ ] Acknowledgments section lists non-author contributors
- [ ] Author order discussed and agreed upon early
