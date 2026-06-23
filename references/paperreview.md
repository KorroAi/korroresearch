# Paper Review - Adversarial Self Review Checklist

## Core Principle

Assume reviewers will probe every weak point. Fix them before they do.

## Critical Rule

Every major claim, especially in Abstract and Introduction, must be:
1. Technically correct
2. Explicitly supported by experimental evidence

If unsupported: add evidence, or weaken/remove the claim.

## What Gets Papers Accepted

1. Sufficient contribution (novel task, pipeline, module, design choice, finding, or insight)
2. Better empirical performance than prior methods under FAIR comparisons
3. Sufficient comparison experiments and ablation studies

## Five Rejection Dimensions

### 1. Insufficient Contribution
- Targeted failure cases are too common/trivial
- Proposed technique already well explored; gains are predictable
- No clear novelty type identifiable

### 2. Unclear Writing
- Missing technical details; work not reproducible
- Method module lacks clear motivation
- Terminology inconsistent across sections
- Readers cannot follow the chain of reasoning

### 3. Weak Empirical Effect
- Improvement over prior methods is only marginal
- Absolute performance still not competitive
- Gains are within noise/variance

### 4. Incomplete Evaluation
- Missing ablation studies
- Missing important baselines or metrics
- Datasets too simple to prove the method works
- No failure case analysis

### 5. Problematic Method Design
- Experimental setting is unrealistic
- Method has technical flaws or unreasonable assumptions
- Method not robust; needs per scenario hyperparameter tuning
- New design introduces stronger limitations than benefits (negative net value)

## End of Paper Self Review Questions

### Contribution
1. What new knowledge does this paper give to readers?
2. Are we solving a truly meaningful failure case?
3. Is the technical idea genuinely non obvious?
4. Is our gain surprising or just a predictable improvement?
5. Is there at least one clear novelty type?

### Writing Clarity
1. Can a knowledgeable reader reproduce the method from the paper?
2. Did we provide enough technical detail for each key module?
3. Is the motivation of every module explicit and logically connected?
4. Are terms and notation consistent across sections?
5. Does each paragraph carry one clear message with smooth transitions?

### Experimental Strength
1. Are improvements over strong baselines meaningful?
2. Is absolute performance competitive for the target venue?
3. Are gains consistent across multiple datasets/settings/metrics?
4. Do we report both strengths and failure cases honestly?

### Evaluation Completeness
1. Do we include ablations for all key design choices?
2. Are all strong/recent baselines included under fair settings?
3. Are evaluation metrics standard and sufficient?
4. Are datasets/scenarios challenging enough?
5. Are comparison and ablation protocols clearly documented?

### Method Design Soundness
1. Is the experimental setting realistic for practical use?
2. Does the method have hidden technical defects?
3. Is the method robust without heavy per case tuning?
4. Do benefits outweigh added complexity and new limitations?
5. Could reviewers argue the net benefit is negative?

## Adversarial Workflow

1. Read the paper as a skeptical reviewer
2. Answer every question above with explicit evidence from the paper
3. Mark each: `pass`, `needs revision`, or `needs new experiment`
4. Revise claims, writing, experiments, or method scope accordingly
5. Repeat until NO major rejection risk remains

## Pre Submission Final Check

- [ ] Abstract claims all map to experiment tables/figures
- [ ] Introduction chain: task -> challenge -> prior work failure -> our solution -> why it works
- [ ] Every figure and table has a purpose and clear message
- [ ] All acronyms defined at first use
- [ ] All citations complete and formatted consistently
- [ ] Method section is reproducible from text alone
- [ ] Ablation studies isolate every claimed contribution
- [ ] Limitations and failure cases are honestly discussed
- [ ] No em dashes anywhere
- [ ] No "could potentially", "may allow", "might be able to"
