# Method Writing Guide

## Goal

Write a method section that is reproducible, technically clear, and logically motivated.

## Core Principles

1. **Reproducibility first** - A knowledgeable reader must be able to reimplement from the text alone
2. **Motivation before mechanism** - State WHY each component exists before WHAT it does
3. **Notation stability** - Same symbol means same thing everywhere
4. **Top down structure** - Overview first, then component details

## Section Structure

### 1. Overview (1 2 paragraphs)
- Restate the problem formulation in precise notation
- Present the pipeline figure and walk through it top down
- Define key terms that will be used throughout

### 2. Component Sections
For each major component:
```
Motivation: What problem does this component solve?
Design: How does it work? (text + equations + algorithm)
Rationale: Why this design choice over alternatives?
Connection: How does it connect to the previous/next component?
```

### 3. Training/Implementation Details (if applicable)
- Loss functions with exact formulations
- Optimization procedure (optimizer, learning rate, schedule, batch size)
- Hardware, runtime, memory footprint
- Hyperparameter values and how they were chosen

## Writing Rules

### Clarity
- Define every symbol at first use
- Use consistent mathematical notation throughout
- Prefer words over equations when the idea is simple
- Number all equations that are referenced elsewhere
- Use algorithm environments for multi step procedures

### Reproducibility
- Specify ALL hyperparameters with exact values
- Document data preprocessing steps completely
- State random seeds if results are stochastic
- Note any implementation tricks that matter

### Common Mistakes to Avoid
- Describing WHAT without explaining WHY
- Skipping the architectural motivation
- Using different notation for the same concept across sections
- Hiding important details in "implementation details" that should be in the main text
- Overcomplicating simple ideas with unnecessary formalism

## Quality Checklist
- [ ] Can a reader reproduce the method from the text?
- [ ] Is the motivation for each component explicit?
- [ ] Is notation consistent across ALL sections?
- [ ] Are all hyperparameters specified?
- [ ] Does the pipeline figure match the text description?
- [ ] Are equations properly numbered and referenced?
