# Supplementary Material Guide

## Goal

Provide additional evidence, details, and resources that support the main paper without cluttering it.

## What Goes in Supplementary

### Required (venue-dependent)
- **Reproducibility checklist** (NeurIPS, ICML, ICLR)
- **Ethics statement** (ACL, NeurIPS, CHI)
- **Broader impact statement** (NeurIPS)
- **Data availability statement** (Nature, Science)
- **Code availability / artifact appendix** (systems conferences)

### Recommended
- Full hyperparameter tables
- Additional ablation studies not fitting in main paper
- Per-dataset breakdowns when main paper shows aggregates
- Extra qualitative examples
- Detailed proofs or derivations
- Extended related work discussion
- Implementation details that aid reproducibility (hardware, library versions)

### Optional
- User study materials (questionnaires, instructions)
- Full prompt templates (for LLM papers)
- Additional baseline comparisons
- Failure case galleries

## Organization

### Structure
```
A. Reproducibility Information
   - Hardware, software, library versions
   - Hyperparameters for ALL experiments
   - Random seeds
   - Data preprocessing details

B. Additional Experiments
   B.1 Extended Ablation Studies
   B.2 Per-Category Results
   B.3 Additional Datasets
   B.4 Runtime / Memory Profiling

C. Theoretical Derivations
   - Full proofs for claims in the main paper

D. Qualitative Examples
   - Best-case, median, and failure examples

E. Code and Data
   - Repository link (anonymized if needed)
   - Dataset details, splits, preprocessing
```

### Cross-Referencing
Every supplementary section must be referenced from the main paper:

| Main Paper Reference | Supplementary Location |
|---|---|
| "See Appendix B.1 for full results" | Section B.1 |
| "Implementation details in Appendix A" | Section A |
| "Proof provided in Appendix C" | Section C |

## Format Rules

- Same template as the main paper (same document class, font, margins)
- Numbered sections (A, B, C) not separate papers
- Figures continue numbering from the main paper or restart as "Figure S1"
- Tables follow the same style rules as the main paper (booktabs, no vertical lines)
- Page limit: typically 4-10 pages for conference supplementary

## Quality Checklist
- [ ] All supplementary content is referenced from the main paper
- [ ] Reproducibility information is complete (hyperparameters, seeds, hardware, software versions)
- [ ] Cross-references use exact section/table/figure labels
- [ ] File size within venue limits (if any)
- [ ] Anonymized if the main paper is under double-blind review
- [ ] Code repository link included (anonymized if under review  --  use anonymous GitHub or zip upload)
