# Experiments Writing Guide

## Goal

Convince reviewers with complete evidence on effectiveness, causality, and practical value.

## Three Core Questions

1. **Is the method better than strong baselines?**
   - Compare against strong and recent baselines
   - Report standard metrics on main benchmarks
   - Include SOTA or strongest public methods
   - Keep protocol fair (same data split, preprocessing, evaluation)

2. **Which modules/design choices make the gain?**
   - Ablation studies for each key module/design choice
   - Use remove/replace/disable variants, report delta to full model
   - Include component interaction ablations when modules are coupled

3. **How far can the method generalize?**
   - Demos/evaluations on harder or out of distribution settings
   - Stress test scenarios (more complex, rarer cases, noisier inputs)
   - Report both gains and failure modes

## Experiment Planning

Start from claims and work backward:
```
Paper Claims -> Contributions -> Validation Experiments
Pipeline Figure -> Modules/Parameters -> Ablation Studies
```

Every contribution claimed in the introduction MUST have a validation experiment.
Every module shown in the pipeline figure MUST appear in an ablation study.

## Section Decomposition

1. **Experimental Setup** - Datasets, metrics, baselines, implementation details
2. **Validation Experiment 1** - Main comparison against SOTA
3. **Validation Experiment 2** - Additional scenario or metric
4. **Ablation Studies** - Component analysis, parameter sensitivity
5. **Qualitative Results** - Visual comparisons, case studies
6. **Limitations and Failure Cases** - Honest assessment

## Figure and Table Rules

### Tables (HARD RULES)
1. Caption ABOVE the table
2. No vertical lines in tabular columns
3. No double rules or dense \hline stacks
4. Use booktabs: \toprule, \midrule, \bottomrule
5. Minimal horizontal rules - only separate groups, not every row
6. Highlight best/second best with subtle color
7. Label metric direction: PSNR ↑, LPIPS ↓, Runtime (ms) ↓
8. Add units so values are interpretable
9. Align text columns left, numeric columns consistently
10. Consistent decimal places within a metric column
11. Group multi dataset results with \multicolumn + \cmidrule
12. One table = one message
13. Keep caption focused on setting/protocol

### Figures (HARD RULES)
1. Every figure must have a clear message visible WITHOUT reading the caption
2. Use vector formats (PDF/SVG) for diagrams
3. Colorblind friendly palette: viridis, cividis, or ColorBrewer
4. Label axes with units
5. Caption states what to observe AND the conclusion
6. Consistent styling across all figures

### Minimal LaTeX Setup
```latex
\usepackage{booktabs}
\usepackage{colortbl,xcolor}
% Optional for decimal alignment:
\usepackage{siunitx}
```

## Recommended Ablation Package
1. One core ablation table for all major contributions
2. Several focused mini-ablations for module-level design choices
3. Matching qualitative visual results for each important ablation

## Experimental Rigor Checklist
- [ ] Baselines are recent and relevant
- [ ] Metrics are sufficient and standard
- [ ] Ablation tied to every key design claim
- [ ] Claims in Abstract/Introduction supported by reported numbers
- [ ] Limitations of evaluation scope explicitly stated
- [ ] Statistical significance reported (std dev, confidence intervals)
- [ ] Hardware/software environment documented
