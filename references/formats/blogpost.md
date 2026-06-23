# Blog Post Format  --  Technical Essays People Actually Read

## Goal

A technical blog post that teaches one thing so well the reader shares it immediately. Not a tutorial. Not a paper summary. A self-contained insight delivered with clarity and depth.

## When to Use

- Company engineering blogs (FAANG-style)
- Personal technical blog
- Distill.pub-style interactive articles
- "We solved X" posts that double as recruiting content
- Conference blog tracks (NeurIPS, ICML blog post tracks)

## The Two Types

### Type A: The Insight Post
"I discovered something interesting and here is why it matters."
- Best for: research findings, technical deep dives, "how X actually works" explainers.
- Length: 1500-3000 words.
- Structure: problem → insight → evidence → implications.

### Type B: The How-To Post
"I built something and here is how you can too."
- Best for: implementation walkthroughs, "we migrated from X to Y", "how we reduced Z by 50%."
- Length: 1000-2500 words.
- Structure: goal → approach → steps → results → code.

---

## The Structure

### 1. The Headline
Must pass the "would I click?" test. See `title.md` Protocol.
```
Bad:  "An Analysis of Gradient Compression Techniques"
Good: "We Cut Our Training Costs by 60% by Not Sending Every Gradient"
```
The bad title describes the topic. The good title promises a benefit.

### 2. The Opening Paragraph
The first 3 sentences determine whether they keep reading.
```
Sentence 1: The problem or context (make it relatable).
Sentence 2: The insight or result (the payoff).
Sentence 3: What the reader will learn (the structure).
```
```
Example:
"Training a large language model costs millions of dollars in compute.
We discovered that 80% of that cost comes from moving gradients between
GPUs — not from computing them. Here is how we eliminated that cost,
and how you can apply the same technique to your own training pipeline."
```

### 3. The Body
Each section = one sub-insight.

```
## Section 1: The Problem (with numbers)
What was broken? Quantify the pain. Show a graph.

## Section 2: Why Existing Solutions Did Not Work
Be fair but clear. "We tried X. It helped Y% but broke Z."

## Section 3: Our Approach
The key insight, explained so a smart undergrad could understand.
One diagram is worth 500 words here.

## Section 4: Results
Before/after comparison. Numbers in bold. A graph that speaks.

## Section 5: How You Can Do This
Code snippet. Configuration snippet. Gotchas we hit and how to avoid them.
```

### 4. The Closing
```
- One sentence summary of what the reader learned.
- Link to code / paper / product.
- One question for the comments section (drives engagement).
```

---

## Blog Post Rules

### Writing
1. **One insight per post.** If you have three insights, write three posts.
2. **Short paragraphs.** 2-4 sentences max. Walls of text kill engagement.
3. **Bold the key sentence in each paragraph.** Skimmers read only bold text. Make it work standalone.
4. **No academic hedging.** "Our results suggest" → "We found." Blog posts are not papers.
5. **Use "you" not "we."** "Here is what you need to know" not "We will now demonstrate."

### Code
1. **Every claim backed by runnable code.** If you say "3x faster," show the benchmark script.
2. **Syntax-highlighted.** Use proper markdown code fences with language tag.
3. **Complete, not fragmentary.** Import statements included. The reader should be able to copy-paste-run.
4. **One code block per concept.** Do not dump 100 lines. Break it up.

### Visuals
1. **Hero image at the top.** The social media preview depends on it.
2. **At least one original diagram.** Stock photos signal low effort.
3. **Graphs with labeled axes and a takeaway in the caption.**
4. **Dark mode compatible.** Transparent backgrounds on diagrams.

### Distribution
1. **The headline IS the tweet.** Write the tweet before the post.
2. **Post on Tuesday-Thursday morning** (US time) for maximum reach.
3. **Submit to Hacker News, Reddit, and relevant newsletters.**
4. **Respond to every comment for the first 24 hours.**

---

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| "10 Tips for X" | Listicles signal low effort. One deep insight > ten shallow tips. |
| Academic abstract as opening | Nobody reads past the first paragraph of a paper-style opening. |
| No code | If you claim a result but show no code, readers assume you are hiding something. |
| Walls of text | If your paragraph is more than 5 lines on mobile, split it. |
| No visual break | After every 300 words, the reader needs a code block, a diagram, or a section header. |
| "In this blog post, we..." | Redundant. Of course it is a blog post. Start with the problem. |

---

## Quality Checklist
- [ ] Headline passes the click test (specific, benefit-driven, not clickbait)
- [ ] Opening paragraph states problem + result + what you will learn
- [ ] One clear insight supported by evidence and code
- [ ] Short paragraphs (2-4 sentences)
- [ ] Code is runnable (imports included, can be copy-pasted)
- [ ] At least one original diagram
- [ ] Hero image set for social media preview
- [ ] Closing asks a question for comments
