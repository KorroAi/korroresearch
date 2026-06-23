# Introduction Writing Guide

## Goal

Write an introduction that makes reviewers feel the problem is important, previous solutions are insufficient, and your solution is the natural next step.

## Three Steps
1. Think through the introduction logic (backward, then forward)
2. Apply the appropriate templates
3. Revise repeatedly

## Backward Reasoning (answer first)

1. What technical problem do we solve, and why is there no well established solution?
2. What are the contributions of our pipeline?
3. What are the benefits of our contributions, and what new insight do they bring?
4. How do we use prior methods to lead readers to our solved challenge?

## Forward Story (write in this order)

1. Introduce the paper's task
2. Use prior methods to lead to the technical challenge we solve
3. Present contributions that solve this challenge
4. Explain technical advantages and explicitly express new insight
5. State experiments and contributions at the end

## Introduction Logic Map

```
What task? -> Which metrics? -> SOTA fails at metrics -> Root technical issue -> Our solution -> Why it works -> Additional contributions
     |              |                    |                       |                  |            |                |
  Part 1: Task + applications    Part 2: SOTA failure + root issue    Part 3: Solution + why    Part 4: Extra + impact    Part 5: Experiments
```

## Part A: Introduce Task and Application

### Version A1: Task first, then applications
For niche tasks.
```
[Task] targets at recovering [output] from [input].
[Task] has a variety of applications such as [app1], [app2], and [app3].
```

### Version A2: Application first
For well known tasks. Open with application importance.
```
[Task] has a variety of applications such as [app1], [app2], and [app3].
```

### Version A3: General to specific
For new settings. Start from the general task, narrow to your specific setting.
```
[General task] has applications such as [app1], [app2].
This paper focuses on [specific setting] of [output] from [input].
```

### Version A4: Open with challenge
For familiar tasks - expose the target challenge in the first paragraph.
```
[Task importance sentence].
Given [input], previous methods usually [approach].
Although they work in many cases, they fail at [failure] because [technical reason].
```

## Part B: Technical Challenge for Previous Methods (CRITICAL)

This section builds reader curiosity. It must show exactly why existing methods fail at the problem YOU solve.

### Version B1: Existing task, existing methods
Chain: general challenge -> traditional methods -> recent methods -> remaining gap.
```
This problem is particularly challenging due to [reason].
To overcome these challenges, traditional methods [approach]. However, they [limitation].
Recently, [method class 1] methods [approach]. However, they [limitation] because [technical reason].
To overcome this, [method class 2] methods [approach]. However, they [limitation] because [technical reason].
```

### Version B2: Existing task, insight has historical roots
When your insight appears in traditional methods but modern methods lost it.
```
Traditional methods used [insight-based approach], which [advantage].
However, these methods still [limitation] because [reason].
Modern methods [approach], but they [different limitation].
```

### Version B3: Novel task, no direct methods
Define the challenge and decompose it.
```
In this work, our goal is to [goal]. This problem is challenging for three reasons.
First, [challenge 1].
Second, [challenge 2].
Finally, [challenge 3].
```

## Part C: Introduce Our Pipeline

### Version C1: One contribution, multiple advantages
```
In this paper, we propose [framework name] for [task].
The basic idea is illustrated in Figure 1.
Our innovation is in [key novelty].
Specifically, [implementation steps].
In contrast to previous methods, [advantage 1].
Another advantage is that [advantage 2].
```

### Version C2: Two contributions
```
In this paper, we propose [framework].
Our innovation is in [novelty statement].
Specifically, [contribution 1 details].
In contrast to previous methods, [advantage].
However, [remaining challenge].
To address this, we introduce [contribution 2] which [how it solves it].
```

### Version C3: Build on existing pipeline, add one module
```
Inspired by [prior work], we [base setup].
Our innovation is introducing [new module].
We observe that [motivating observation].
Considering that, we introduce [module mechanism].
In contrast to [generic alternative], our module [why better].
```

### Version C4: Observation driven
```
Our innovation is [key idea].
We observe that [intuitive observation].
Considering that, we [implementation].
This leads to [advantage] and achieves [result].
```

## Red Flag: Do NOT Write Incremental Patch Style

Never present a naive solution, then describe your improvement. This makes the work look low score.
Even if the work IS incremental, frame it from the challenge perspective, not the patching perspective.

## Introduction Quality Checklist

1. Does the first sentence of each paragraph state its message?
2. Does each paragraph carry ONE message only?
3. Are technical challenge, technical reason, and solved mechanism all explicit?
4. Are claims in Introduction aligned with experiment evidence?
5. Is terminology stable across all sections?
6. Would a reviewer understand the problem and contribution in 2 minutes?
