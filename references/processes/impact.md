# Impact, How To Make Any Document Unignorable

## Goal

This guide applies to EVERY format the skill covers. Research paper, grant proposal, white paper, book, thesis, pitch deck, conference talk. The principles of being unignorable are format-agnostic and domain-agnostic. Apply them all, every time.

**Cross-domain note**: The examples below draw from CS/ML and business because these domains have the most publicly-documented case studies of breakthrough documents. The principles are universal. A biology grant destroys the worldview "this disease pathway is understood." A history thesis destroys the worldview "this period has been adequately studied." An architecture white paper destroys the worldview "buildings must be designed the way they have always been designed." The domain changes. The principles do not.

## The One Law

**The worst sin is not being wrong. The worst sin is being forgettable.**

A flawed but unforgettable document changes the world. A correct but boring document changes nothing. Reviewers, investors, readers, they read 50+ documents a week. Yours either HAUNTS them or vanishes. There is no middle ground.

---

## Principle 1: Destroy a Worldview

Every great document starts by identifying a belief the audience holds, and then proving it false.

| Document Type | The Belief You Destroy | The New Belief You Install |
|---|---|---|
| Research paper | "X is the best way to solve this problem." | "X is fundamentally limited. Y is the correct approach." |
| Grant proposal | "This problem is being addressed adequately." | "This problem is being IGNORED, and the consequences are severe." |
| White paper | "The current system works fine." | "The current system is structurally broken. Here is the architecture of the replacement." |
| Investor pitch | "This market is niche / saturated / stable." | "This market is about to undergo a phase transition. We are positioned at the inflection point." |
| Academic book | "This field is a collection of techniques." | "This field has an underlying structure you have never seen. Once you see it, you cannot unsee it." |
| Thesis | "This question has been explored." | "This question has never been asked properly. I am asking it properly, and here is everything that follows." |

**How to find the worldview to destroy**: Ask "What does everyone in my field believe that is actually an assumption, not a fact?" The answer is your target.

---

## Principle 2: One Irreducible Insight

Every great document is about ONE thing. Everything else is scaffolding.

| Document | The ONE Thing |
|---|---|
| Shannon 1948 | Information can be measured mathematically. |
| Bitcoin whitepaper | A peer-to-peer electronic cash system without trusted third parties. |
| SICP (Abelson & Sussman) | A computer language is not just a way to instruct a computer, it is a novel formal medium for expressing ideas about methodology. |
| Airbnb seed deck | People will pay to sleep in strangers' homes if the experience feels safe and curated. |
| NIH R01 grant | If we answer THIS question, everything in THIS field changes. |
| Steve Jobs iPhone keynote | Your phone is broken. Here is what a phone should be. |

**Test**: Can every section, every paragraph, every figure trace its lineage back to the ONE thing? If a section exists for any other reason (tradition, "reviewers expect it," "papers in this field always include X"), cut it or subordinate it to the ONE thing.

---

## Principle 3: Make the Audience the Hero

Bad documents say "Look what I did." Great documents say "Look what YOU can now do."

| Document Type | Who Is the Hero? | What Do They Gain? |
|---|---|---|
| Research paper | Other researchers | "With this insight, YOU can build things that were impossible before." |
| Grant proposal | The funding agency | "By funding this, YOU enable a breakthrough that would not happen otherwise." |
| White paper | Decision-makers | "With this framework, YOU can make decisions that were previously guesswork." |
| Academic book | Students and practitioners | "After reading this, YOU will see the entire field differently." |
| Thesis | The committee | "After reading this, YOU will know something nobody else in the world knows." |
| Investor pitch | Investors | "By investing, YOU capture value from a market shift nobody else sees yet." |
| Conference talk | The audience | "In the next 15 minutes, YOU will learn one thing that changes how you work." |

**Implementation**: Count the ratio of "we" / "our method" to "you" / "practitioners can" / "this enables." If "we" dominates, rewrite every sentence from the reader's perspective.

---

## Principle 4: The Inevitability Arc

Great documents feel INEVITABLE. Not "here is a thing we discovered" but "given what we know, this HAD to be true, and now that you've seen it, you realize it too."

### The Arc Structure

```
Phase 1: "Here is the world as you know it." (Establish shared reality)
Phase 2: "Here is something that does not make sense in that world." (Introduce tension)
Phase 3: "Here is why it does not make sense." (Diagnose the root cause)
Phase 4: "Here is what the world looks like when you fix that." (Present the resolution)
Phase 5: "Here is everything that now becomes possible." (Map the new territory)
```

Every section of your document should be clearly assigned to one of these five phases. If a section cannot be assigned, it does not belong.

### Books Are Different

Books follow the same arc but at chapter granularity:
- **Chapters 1-2**: Phase 1 (establish the world)
- **Chapters 3-5**: Phase 2-3 (tension and diagnosis)
- **Chapters 6-8**: Phase 4 (resolution, the new framework)
- **Chapters 9-10**: Phase 5 (applications, open problems, what comes next)

---

## Principle 5: The Memorability Hook

People remember DOCUMENTS through specific mechanisms. Engineer yours deliberately.

| Mechanism | How It Works | Example |
|---|---|---|
| **The Name** | A single word or phrase that encapsulates the entire idea. Becomes linguistic currency. | "Dropout." "Attention." "Bitcoin." "The Feynman Lectures." |
| **The Visual** | One figure or diagram that, once seen, cannot be unseen. The idea IS the image. | Shannon's communication diagram. The transformer attention visualization. Bitcoin's chain of blocks. |
| **The Number** | One statistic so striking it gets repeated in every citation. | "3.2x faster." "92% of developers." "57% of tasks resolved before any API call." |
| **The Analogy** | A comparison that makes the unfamiliar instantly familiar. | "Neural networks are like the brain." (Wrong but sticky.) "Attention is like looking at the most relevant parts of a painting." |
| **The Provocation** | A statement that makes people ARGUE. Controversy creates memory. | "Attention Is All You Need." (The title IS the provocation.) "The End of History." "Programming is the new literacy." |

**Rule**: Every document must deploy at least TWO of these mechanisms. Preferably three. Zero is not acceptable.

---

## Principle 6: Density Over Length

The reader's attention is a depleting resource. Every paragraph that does not deliver insight CONSUMES attention that a later paragraph needs.

### The Attention Budget

| Document Type | Total Attention Budget | Cost Per Paragraph |
|---|---|---|
| Abstract | 30 seconds | Every sentence costs 3-5 seconds |
| Introduction | 3 minutes | Every paragraph costs 20-30 seconds |
| Full paper | 20 minutes (skimming) | Every section costs 2-3 minutes |
| Grant proposal | 10 minutes (first pass) | Every page costs 1 minute |
| Pitch deck | 3 minutes (10 slides) | Every slide costs 18 seconds |
| Conference talk | 15 minutes | Every slide costs 45-90 seconds |

**Implication**: A paragraph that takes 30 seconds to read but delivers zero new information has STOLEN 30 seconds from a paragraph that needed it. Be ruthless. Every paragraph is competing for a finite resource.

### The Density Test

For each paragraph: "What does the reader know after reading this that they did not know before?" If the answer is "nothing" or "the same thing they learned from the previous paragraph", delete it.

---

## Principle 7: The Opening That Cannot Be Skipped

Most readers decide whether to engage in the first 30 seconds. If your opening does not create a compulsion to continue, nothing else matters.

### Opening Formulas by Format

**Research Paper, Abstract, Sentence 1**
```
Bad:  "In this paper, we present a novel approach to..."
Good: "Single-model AI coding assistants share a fundamental
       limitation: when the same model generates AND reviews
       code, it cannot detect its own blind spots."
```
The good version states a PROBLEM that feels urgent. The bad version states a FACT that feels administrative.

**Grant Proposal, First Paragraph**
```
Bad:  "This proposal requests funding to investigate..."
Good: "Every year, 50,000 patients die from [condition] because
       we lack the ability to [specific capability]. We have
       preliminary evidence that [approach] can provide this
       capability. This proposal would validate it at scale."
```
The good version makes the reader feel the COST of not funding. The bad version is a formality.

**White Paper, Executive Summary**
```
Bad:  "This white paper describes the architecture of..."
Good: "The [industry] runs on infrastructure designed in 2005
       for problems that existed in 1995. This document describes
       the architecture of a replacement — one built for the
       problems of 2026."
```
The good version creates a sense of OBSOLESCENCE. The bad version is a table of contents.

**Talk, First Slide After Title**
```
Bad:  "Outline: 1. Motivation 2. Method 3. Results..."
Good: [Single image showing the problem with one devastating
       statistic overlaid] "This is what we are here to fix."
```
The good version creates EMOTION. The bad version is an agenda.

---

## Principle 8: The Call to Action

Every document must end by telling the audience what to DO with what they just learned. Not "conclusions were drawn", specific, actionable next steps.

| Document Type | Call to Action |
|---|---|
| Research paper | "We have released the code and models. The three open problems in Section 6 are ready to be solved." |
| Grant proposal | "With [amount] over [timeline], we will deliver [specific outputs] by [specific dates]." |
| White paper | "The migration from [old system] to [new architecture] should begin with [first step], which can be completed in [timeline]." |
| Book | "If you remember one thing from this book: [one sentence]. Now go apply it to [specific context]." |
| Thesis | "I have established [claim]. The field is now positioned to investigate [specific next questions]." |
| Pitch deck | "We are raising [amount] at [terms]. Our current traction: [metric]. Join us." |

---

## Cross-Format Diagnostic

Before finalizing ANY document, answer:

1. **Worldview destroyed**: What belief did the reader hold before that they no longer hold?
2. **One thing**: What is the single sentence a reader will repeat to a colleague?
3. **Hero**: Who is the hero of this document? (If it's you, rewrite.)
4. **Inevitability**: Does the conclusion feel like the only possible outcome of the evidence?
5. **Memorability**: Name (does it exist?), Visual (what's the one figure?), Number (what's the one stat?), Analogy (what's the comparison?)
6. **Density**: What did you delete? (If nothing was deleted, the document is not finished.)
7. **Opening**: Does the first 30 seconds create compulsion?
8. **Call to action**: What should the reader DO tomorrow?

If any answer is blank, the document is not finished.

---

## Integration With the Skill

- Apply these 8 principles BEFORE loading any section guide.
- Principles 1-4 (Worldview, One Thing, Hero, Inevitability) shape WHAT you write.
- Principles 5-6 (Memorability, Density) shape HOW you write.
- Principles 7-8 (Opening, Call to Action) shape your FIRST and LAST 30 seconds.
- For research papers, run this AFTER `ideation.md` (idea quality) but BEFORE section writing.
- For grants, pitches, and white papers, run this FIRST, before any template.
