# Title Writing Guide

## Goal

The title is the most-read part of any document. 5x more people read the title than the abstract. 50x more than the full paper. A bad title buries a good paper. A great title makes a paper unignorable.

## The Three Types of Great Titles

### Type 1: The Provocation
States a counter-intuitive claim that demands explanation.

| Title | Why It Works |
|---|---|
| "Attention Is All You Need" | States something that sounds impossible. Forces the reader to ask "how?" |
| "ImageNet Classification with Deep Convolutional Neural Networks" | Not a provocation per se, but the combination "ImageNet" (known hard) + "Deep CNNs" (new at the time) created curiosity. |
| "Deep Residual Learning for Image Recognition" | "Residual learning"  --  a new concept name that hints at the insight. |
| "Generative Adversarial Nets" | "Adversarial" + "Generative"  --  two words that should not go together. The tension IS the title. |
| "The End of History?" | (Fukuyama) A question that cannot be ignored. |

**Use when**: Your core insight is genuinely surprising or counter-intuitive.

### Type 2: The Concept Name
Introduces a new term that becomes linguistic currency.

| Title | Why It Works |
|---|---|
| "Dropout: A Simple Way to Prevent Neural Networks from Overfitting" | Names the technique with a perfect metaphor. The colon lets the subtitle explain. |
| "Adam: A Method for Stochastic Optimization" | Short, memorable, biblical connotations (the first man). |
| "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" | BERT became the name everyone uses. The acronym IS the title. |
| "GPT-4 Technical Report" | The name is the brand. The title is just the name. |
| "MapReduce: Simplified Data Processing on Large Clusters" | Names the abstraction (Map then Reduce) that became a verb. |

**Use when**: Your contribution is a new technique, architecture, or framework that deserves a name. The name goes FIRST, colon, then the descriptive subtitle.

### Type 3: The Descriptive Precision
States exactly what was done with clinical precision. Works for incremental but solid work.

| Title | Why It Works |
|---|---|
| "A Mathematical Theory of Communication" | Understated. Almost boring. Then you read it and realize it created information theory. |
| "On Computable Numbers, with an Application to the Entscheidungsproblem" | Turing. Precise. Humble. World-changing. |
| "Learning representations by back-propagating errors" | (Rumelhart, Hinton, Williams 1986) Describes exactly what the paper does. No hype. |

**Use when**: The work is so significant that a humble title signals confidence. Do NOT use for incremental work  --  a humble title on an incremental paper guarantees it will be ignored.

---

## Title Anti-Patterns

| Anti-Pattern | Example | Why It Fails |
|---|---|---|
| **"A Novel Approach to..."** | "A Novel Approach to Gradient Compression" | "Novel" is a claim your paper should prove, not your title should assert. |
| **"Towards..."** | "Towards Better Gradient Compression" | Signals incompleteness. "We did not actually solve it, but we moved towards it." |
| **Question titles (usually)** | "Can Attention Replace Recurrence?" | The answer is in the paper. State it. ("Attention Replaces Recurrence" is stronger. Or better: "Attention Is All You Need.") |
| **"On the..."** | "On the Compression of Gradients in Deep Learning" | Archaic. Unless you are Shannon or Turing, avoid. |
| **The colon dump** | "GradZip: A Novel Lossless Gradient Compression Framework for Distributed Deep Neural Network Training via Per-Tensor Variable-Width Adaptive Encoding" | The part after the colon should be SHORTER than the part before. The name is GradZip. The subtitle is "Lossless Gradient Compression." Stop. |
| **Keywords stuffed for SEO** | "Deep Learning Gradient Compression Distributed Training Neural Network Optimization" | This is not a title. This is a search query. |

---

## The Title Protocol

### Step 1: Write the one-sentence insight first.
If you cannot state your contribution in one sentence, you are not ready to write the title. Start there.

### Step 2: Try all three types.
Write one title of each type. Even if you think your paper is Type 2, write a Type 1 and Type 3 version. The best title is often the one you initially rejected.

### Step 3: Test with colleagues.
Send 3 candidate titles to 3 colleagues. Ask: "Which would you click on?" Do not ask "which is more accurate." Titles are marketing. Accuracy matters, but if nobody clicks, accuracy is irrelevant.

### Step 4: Check for uniqueness.
Google your title (in quotes). If another paper has the same or similar title, change yours. A title collision signals that your contribution is not distinct.

### Step 5: Read it aloud.
Does it sound natural? Does it have rhythm? "At-ten-tion Is All You Need"  --  four stressed syllables, perfect rhythm. Great titles are poems.

---

## Format-Specific Title Rules

| Format | Title Rule |
|---|---|
| Conference paper | 6-12 words. The title is read in a program listing alongside 100 others. Must stand out. |
| Journal paper | 8-15 words. More descriptive OK. |
| Grant proposal | Descriptive and clear. "CAREER: [Your Research Program]" for NSF. No jokes, no provocation. |
| White paper | Action-oriented. "Why [X] Needs to Change" or "The [Y] Architecture" |
| Blog post | Click-worthy but not clickbait. "How We Reduced Training Costs by 3x" beats "Gradient Compression: A Technical Overview" |
| Pitch deck | The company name or the one-sentence value prop. Not a paper title. |

---

## Title Quality Checklist
- [ ] Passes the "would I click on this?" test
- [ ] Under 15 words (conference) or 20 words (journal)
- [ ] No "Novel", "Towards", "On the", "A Study of"
- [ ] Colon used correctly: Name: Short Subtitle (not Name: Long Meandering Description)
- [ ] Unique (no other paper has this title)
- [ ] Readable aloud without stumbling
- [ ] Matches the document type's tone (provocative for papers, clear for grants, clickable for blogs)
