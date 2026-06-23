# Ideation  --  Is Your Idea Paper-Worthy?

## Goal

Determine whether an idea deserves to become a document BEFORE writing begins. The greatest documents in history share properties that no writing guide teaches. This diagnostic enforces all of them.

## Cross-Domain Note

The examples in this guide are primarily from CS/ML  --  the domain with the most publicly-documented breakthrough patterns. The protocols are universal. A biology paper applying the Shannon filter: "CRISPR is a bacterial immune system that can be reprogrammed to edit any genome." A chemistry paper: "Molecules can be assembled like Lego blocks using click chemistry." A social science paper: "People do not make decisions rationally  --  they use heuristics that are predictable and systematically biased." The domain does not matter. The principles are the same.

## Core Principle

**Writing cannot save a bad idea. A great idea survives mediocre writing.** The skill's writing machinery is useless if the idea underneath is incremental. This guide is the gatekeeper. Run it first, every time.

---

## Protocol 1: The Shannon Filter  --  Three Tests

If the idea fails any of these, do not write the paper. Go back to research.

### Test A: The One-Sentence Theorem
State your core insight in one sentence without jargon, without "by leveraging", without "through the integration of".

| Pass | Fail |
|---|---|
| "Attention replaces recurrence." | "We propose a novel architecture that leverages attention mechanisms to enhance sequential processing." |
| "Two networks fighting each other produce realistic data." | "An adversarial training framework where a generator and discriminator compete in a minimax game." |
| "Information is entropy." | "Communication can be quantified through probabilistic measures of uncertainty reduction." |
| "Forgetting randomly during training makes networks generalize." | "A stochastic regularization technique that randomly drops units during forward propagation." |

**Rule**: If a smart colleague outside your subfield cannot understand your one-sentence statement, you do not understand it yourself. Simplify until they can.

### Test B: Why Now?
Why has nobody done this before?

| Answer | Verdict |
|---|---|
| "Everyone assumed it was impossible." | Paper-worthy. You broke an assumption. |
| "Nobody thought to connect X and Y." | Paper-worthy. Cross-domain pollination. |
| "The enabling technology didn't exist until recently." | Paper-worthy. Timing is contribution. |
| "We tried a slightly different architecture." | NOT paper-worthy. Go deeper. |
| "We added more data / more parameters." | NOT paper-worthy. Engineering report, not research. |

### Test C: The Hindsight Inevitability
In ten years, will people look back and say "of course  --  that had to be true"?

- Shannon: "Of course information has a mathematical measure."
- Vaswani: "Of course attention is sufficient without recurrence."
- Goodfellow: "Of course competition can drive generation."

If the answer is no  --  if people in ten years would say "that was a strange detour"  --  you have a novelty paper, not a classic. Novelties get published. Classics get cited for 30 years.

---

## Protocol 2: Paper-First  --  Write Before Experiments

**Counter-intuitive and used by Hinton, Schmidhuber, LeCun, and others.**

The trap: running experiments then writing the paper around whatever you found. This produces incremental papers because you never asked "what would be worth finding?"

Instead:

```
Step 1: Write the abstract, introduction, and method section as if it already works.
        Every declarative sentence in these sections is now a claim.

Step 2: Extract every claim into a checklist:
        "Our method achieves X% on benchmark Y" → Run benchmark Y.
        "Module Z is essential for performance" → Design ablation for Z.
        "This generalizes across modalities A, B, C" → Test on A, B, C.

Step 3: Run experiments. For each claim that fails:
        Option A: Debug the method. The claim was right, the implementation was wrong.
        Option B: Weaken the claim. "Always works" becomes "works when condition W holds."
        Option C: Remove the claim. Better a shorter paper than a wrong claim.

Step 4: The remaining claims + verified results = your paper.
```

**Why this works**: It forces you to think about the STORY before the data. Papers that start from data read like "we ran experiments and here's what we found." Papers that start from claims read like "here's what we predicted and here's the evidence."

---

## Protocol 3: The Territory Map  --  End With What You Don't Know

Great papers open more questions than they close. A paper that answers everything is a dead end. A paper that opens 10 questions is cited for 30 years.

### Structure the Final Section as "Open Problems"

Not:
> "In this paper, we presented GradZip and demonstrated 3.2x compression. Future work includes applying it to other tasks."

But:
> "GradZip raises several questions we cannot yet answer. (1) Why do batch normalization layers exhibit 98% sparsity while convolutional layers show only 40%? Understanding this asymmetry could lead to architecture designs that are inherently more compressible. (2) Our variable-width encoding assumes per-tensor granularity; finer-grained per-neuron encoding might achieve even higher ratios but requires different hardware primitives. (3) The 100-step warmup profiling window works empirically, but a theoretical bound on the minimum profiling duration would make the approach provably correct. (4) Lossless compression may be unnecessary: preliminary evidence suggests 0.1% reconstruction error is tolerable for all layers except the first and last. Determining the exact tolerance per layer could yield another 2x compression."

### Territory Quality Checklist
- [ ] At least 3 open questions, each technically specific
- [ ] Each question could become a paper on its own
- [ ] Questions are not vague ("more research is needed") but pointed ("why does X exhibit property Y?")
- [ ] At least one question challenges your own method's assumptions

---

## Protocol 4: Cross-Domain Pollination

The greatest breakthroughs come from applying a concept from domain A to domain B.

| Paper | Domain A | Domain B | Core Abstraction |
|---|---|---|---|
| Shannon 1948 | Thermodynamics (entropy) | Communication | Uncertainty as measurable quantity |
| Turing 1936 | Logic (formal proofs) | Computation | Mechanical symbol manipulation |
| Vaswani 2017 | Machine Translation | Vision, Speech, etc. | Position-independent relationship modeling |
| Goodfellow 2014 | Game theory (minimax) | Generative modeling | Competition as training signal |

### The Protocol

1. **Extract the abstraction**: What is your method, stripped of all domain-specific language? Write it as a VERB, not a noun. "Attention" is a noun. "Attending to relevant parts of the input" is a verb. Verbs transfer across domains; nouns do not.

2. **Map the abstraction to other domains**: For each domain below, ask: "Does this domain have something that looks like [abstraction]?"
   - Biology / evolution
   - Physics / thermodynamics
   - Economics / game theory
   - Linguistics / semiotics
   - Sociology / network theory
   - Art / design / architecture

3. **Cross**: What happens when you apply the domain-B version of the abstraction back to domain A? The result is either nonsense (discard) or a breakthrough (pursue).

### Example

Abstraction: "Selectively focusing computational resources on the most relevant parts of the input."

| Domain | Translation | Cross-Pollination |
|---|---|---|
| Biology | Visual attention in primates  --  the fovea concentrates photoreceptors on the fixation point | Could attention be HARDWARE-EFFICIENT, like the fovea? Sparse computation only where it matters? |
| Economics | Portfolio allocation  --  concentrate capital on highest-expected-return assets | Could attention weights be learned via REINFORCEMENT instead of gradient descent? |
| Sociology | Dunbar's number  --  humans maintain ~150 stable relationships, prioritizing by frequency and recency | Could attention have a HARD CAP on active connections, enforced by sparsity? |

---

## Protocol 5: The Elegance Razor  --  Remove Before Adding

Shannon could have written 80 pages. He wrote 55. Every sentence that is not indispensable WEAKENS the paper.

### The Four-Pass Removal Protocol

**Pass 1  --  Remove Redundancy**
Delete every sentence that repeats information already conveyed. If Section 3.1 and Section 5.2 both explain the same mechanism, delete one. The reader is not stupid.

**Pass 2  --  Remove Inferences**
Delete every sentence the reader could infer from what you already said. "This demonstrates that our method is effective"  --  the numbers already demonstrated it. Trust the reader to draw conclusions.

**Pass 3  --  Fuse Overlaps**
For every pair of sentences that convey overlapping information using different words, merge them into one sentence. Two weak sentences become one strong one.

**Pass 4  --  Challenge Every Remainder**
For each remaining sentence, ask: "If I delete this, does the paper become FALSE?" If the answer is no, delete it. A paper needs every sentence to be true; it does not need every sentence to exist.

### Target Length by Paper Type

| Paper Type | Target | Rationale |
|---|---|---|
| Conference (8 pages) | 6 pages of content, 2 pages of breathing room | Dense papers are hard to review. Give the reviewer space. |
| Journal (14 pages) | 12 pages of content, 2 pages of breathing room | Same principle, scaled. |
| White paper | As long as necessary, not one word longer | No page limit means you must be your own enforcer. |

---

## Protocol 6: The Anti-Paper  --  Write the Attack

Before finalizing, write a one-page abstract that argues AGAINST your paper. Be vicious. Be the reviewer who wants to reject you.

### Anti-Paper Template

```
Title: Why [Your Method] Is Not a Meaningful Contribution

Abstract:
[Your method] claims to [your claim]. However, this claim is undermined
by three fundamental weaknesses.

First, [weakness 1 — the most damaging critique you can think of].
[Two sentences elaborating.]

Second, [weakness 2 — what's the most obvious alternative explanation
for your results?]. [Two sentences elaborating.]

Third, [weakness 3 — where does your method break? What assumptions
does it make that don't hold in practice?]. [Two sentences elaborating.]

Furthermore, the experimental evaluation [specific critique about baselines,
datasets, metrics, or statistical rigor]. [Two sentences.]

We conclude that while [your method] is technically sound, it does not
represent a meaningful advance over [closest prior work].
```

### Pre-emption Checklist

For every weakness identified in the anti-paper, ensure the real paper contains one of:
- **Direct refutation**: The weakness is false, and here is the evidence.
- **Acknowledgment + mitigation**: The weakness is real, and here is how we mitigate it.
- **Honest limitation**: The weakness is real, we cannot fix it, and we state it clearly in the limitations section.

If a weakness appears in the anti-paper but NONE of these three responses appear in the real paper, you have a rejection waiting to happen.

---

## Protocol 7: The New Language  --  Name Your Concept

"Attention." "GAN." "Dropout." "Information entropy." "Turing machine." "Transformer."

The greatest papers invent CONCEPTS, not just results. A well-chosen name is worth 1,000 citations because people cite what they can NAME.

### The Naming Test

1. **Evocative**: Does the name create a mental image? "Dropout"  --  neurons literally drop out. "Attention"  --  the model pays attention. "Transformer"  --  it transforms representations.

2. **Memorable**: Can a colleague remember it after hearing it once? "Generative Adversarial Network" → GAN. Three letters, unforgettable.

3. **Hard to replace**: If someone tries to avoid using your term, does the replacement sound worse? Nobody says "stochastic unit omission"  --  they say "dropout." Good names are linguistic monopolies.

4. **Self-describing**: Does the name hint at what it does? "Backpropagation"  --  propagating errors backward. "Convolution"  --  convolving a filter across the input.

### Naming Anti-Patterns

| Bad Name | Why It Failed | Better Name |
|---|---|---|
| "Residual Networks with Identity Mappings" | Descriptive but unmemorable, no image | "ResNet"  --  stuck immediately |
| "Multi-Head Dot-Product Attention over Value Vectors" | Too technical, no image | "Attention"  --  the abstraction, not the implementation |
| "Stochastic Depth" | Evocative but never caught on because "Dropout" already owned the mental space | Pick a name that doesn't compete with an existing linguistic monopoly |
| Any name starting with "A Novel..." | "Novel" is not part of the name, yet papers do this constantly | Just say the name. "We present GradZip." Not "We present a novel gradient compression framework called GradZip." |

### If You Cannot Name It

If you genuinely cannot find a good name, your concept might not be distinct enough. Worthy concepts are easy to name because they FEEL like something. If your concept is "a modification to the training procedure that slightly improves convergence on some benchmarks"  --  the problem is not the name. The problem is the concept.

---

## Pre-Writing Decision Gate

Before loading any section writing guide, answer:

1. One-sentence insight (no jargon): ________________________
2. Why nobody before: ________________________
3. Hindsight verdict (will it be "obvious" in 10 years?): ________________________
4. Abstraction (verb form, domain-free): ________________________
5. The name (if you have one): ________________________

If any field is blank, do not start writing. Return to research until it is filled.

---

## Adapting Protocols to Non-Paper Formats

### Grant Proposals
- **Protocol 1 (Shannon Filter)**: Instead of asking "why has nobody done this?", ask "why would this not happen without funding?" If the answer is "it would happen anyway," your grant is dead.
- **Protocol 2 (Paper-First)**: Does NOT apply. You need preliminary results BEFORE writing. The grant's "paper-first" equivalent: write the Specific Aims as if you already have preliminary results, then fill in the data you have. Flag missing data as "experiments we will run if funded."
- **Protocol 3 (Territory Map)**: Grants should open questions about the FIELD's future, not your project's future. "If we succeed, here's what becomes possible" is the grant's territory map.
- **Protocol 7 (New Language)**: Grants need memorable names for the PROJECT, not the method. "The XYZ Initiative" is not a name. "Project Nightingale" is.

### White Papers
- **Protocol 1 (Shannon Filter)**: The insight is about the PROBLEM, not the solution. "The current architecture is structurally incapable of X" is a white paper insight.
- **Protocol 2 (Paper-First)**: Use "vision-first" instead. Write the executive summary describing the world AFTER the solution is adopted. Then work backward to what needs to be true.
- **Protocol 6 (Anti-Paper)**: Write the skeptic's executive summary: "Why [Your Solution] Will Not Work." Common skeptic arguments: adoption cost, migration complexity, "we tried this before," "this only works in theory."

### Books
- **Protocol 1 (Shannon Filter)**: The book's insight is the ONE mental model the reader will internalize. SICP: "A computer language is a formal medium for expressing ideas about methodology." If your book doesn't have a one-sentence thesis that changes how people think, do not write the book.
- **Protocol 2 (Paper-First)**: Write the preface and Chapter 1 first. They define the book's contract with the reader. Every subsequent chapter either delivers on that contract or does not belong.
- **Protocol 3 (Territory Map)**: Every chapter should open questions that the NEXT chapter answers. The final chapter should open questions the FIELD must answer.

---

## Integration With the Rest of the Skill

- After passing the Shannon Filter, proceed to `references/sections/abstract.md` to write the abstract.
- For non-paper formats, load `references/processes/impact.md` next  --  then the format-specific guide.
- Run Protocol 2 (Paper-First) before loading any experiments guide.
- Run Protocol 4 (Cross-Domain Pollination) if your idea feels incremental.
- Run Protocol 5 (Elegance Razor) after every full draft.
- Run Protocol 6 (Anti-Paper) alongside `references/paperreview.md` before finalizing.
- Run Protocol 3 (Territory Map) when writing the conclusion using `references/sections/conclusion.md`.
- Apply Protocol 7 (New Language) during the abstract and introduction writing phases.
