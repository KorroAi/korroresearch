# Audience Analysis  --  Who Reads This, And What Makes Them Say Yes?

## Goal

Before writing a single word, understand who will read your document, what they currently believe, what they fear, and what makes them say yes. Every document type has a different decision-maker with different incentives. Writing without audience analysis is writing blind.

## The Three Questions

1. **Who** is the decision-maker? (Not "who reads it"  --  who DECIDES?)
2. **What** does this person believe that you must change?
3. **What** makes them say yes? (And what makes them say no?)

---

## Audience Profiles by Format

### Conference Paper Reviewer
| Dimension | Answer |
|---|---|
| Who decides | 3 reviewers (typically PhD students, postdocs, or junior faculty) + 1 area chair |
| What they believe | "Most papers are incremental. I need to find 3 papers to accept out of 20 assigned." |
| What makes them say YES | A clear problem they recognize, a solution that feels inevitable, evidence that leaves no doubt |
| What makes them say NO | Unclear contribution, missing baselines, overclaiming, poor writing that wastes their time |
| Time they spend | 1-2 hours on first read, 30 min on revision |
| How to research them | Read their recent papers. They will compare your work to their own. |

### Grant Reviewer (NSF, ERC, NIH)
| Dimension | Answer |
|---|---|
| Who decides | Panel of 10-20 senior researchers + program officer |
| What they believe | "There are 50 proposals and 8 get funded. Most are good. Which ones MUST happen?" |
| What makes them say YES | A problem where NOT funding feels irresponsible, preliminary results proving feasibility, a team that clearly can execute |
| What makes them say NO | Vague methodology, no preliminary data, an idea that could be done without funding, a problem that does not feel urgent |
| Time they spend | 5-10 min on first pass (often just abstract + budget), 30 min if shortlisted |
| How to research them | Read the program description. Use their language. Cite their priorities back to them. |

### Investor (Pitch Deck)
| Dimension | Answer |
|---|---|
| Who decides | Partner at a VC firm or angel investor |
| What they believe | "I see 500 decks a year. I invest in 5. Most ideas are not businesses." |
| What makes them say YES | Massive market, unique insight, traction that proves demand, team that has done it before |
| What makes them say NO | No clear go-to-market, solution looking for a problem, "we have no competitors" (means no market) |
| Time they spend | 30 seconds on first pass (often just the email + first slide), 3 min if the deck is opened |
| How to research them | Look at their portfolio. Frame your company as the natural extension of what they already believe in. |

### White Paper Reader (Decision-Maker)
| Dimension | Answer |
|---|---|
| Who decides | CTO, VP Engineering, or Director of Product |
| What they believe | "I have 10 problems. If this document does not solve one of them, I am not reading it." |
| What makes them say YES | A problem they feel acutely, a solution that fits their existing infrastructure, a migration path that is not disruptive |
| What makes them say NO | Hand-waving about technical details, no clear ROI, "rip and replace" proposals |
| Time they spend | 2-3 min scanning executive summary and figures, 15 min if hooked |
| How to research them | Understand their tech stack, their pain points, their recent public statements. |

### Thesis Committee
| Dimension | Answer |
|---|---|
| Who decides | 3-5 professors, one of whom is your advisor |
| What they believe | "This student needs to demonstrate they are the world expert on a specific question." |
| What makes them say YES | Depth (nobody knows more about X), rigor (methodology is sound), contribution (advances the field) |
| What makes them say NO | Breadth without depth, sloppy methodology, failure to acknowledge limitations |
| Time they spend | They read the whole thing (rare among all document types) |
| How to research them | They are your committee. You already know what they value. Address it explicitly. |

### Blog Post Reader (Technical Audience)
| Dimension | Answer |
|---|---|
| Who decides | Individual engineer or researcher deciding whether to read, share, or apply |
| What they believe | "I have 5 minutes. Teach me something I can use today." |
| What makes them say YES | One clear insight, code they can copy, a mental model that changes how they think |
| What makes them say NO | Vague advice, no code, "10 tips for X" listicles, content that could be ChatGPT output |
| Time they spend | 30 seconds on the headline, 2 min scanning, 5-8 min if good |
| How to research them | Hacker News comments, r/MachineLearning, Twitter discourse. |

---

## The Worldview Research Protocol

For each audience, answer these before writing:

### 1. The Canonical Belief
What is the single sentence that summarizes what this audience currently believes about your topic?

*Example (conference paper on gradient compression)*: "The reviewer believes gradient compression is a solved problem  --  QSGD and Top-k are good enough, and lossless schemes are too slow to matter."

### 2. The Evidence They Would Accept
What kind of evidence would change their mind?

*Example*: "They would need to see: (a) lossless compression can match lossy ratios, (b) the overhead is negligible, (c) accuracy is identical to uncompressed training."

### 3. The Fatal Objection
What is the one objection that, if unaddressed, guarantees rejection?

*Example*: "If they believe the profiling overhead makes the scheme impractical for real training, the paper is dead. The experiment section MUST address wall-clock time, not just compression ratio."

### 4. The Ally
What prior work or belief does this audience hold that SUPPORTS your argument?

*Example*: "They already believe per-layer behavior varies (batch norm vs conv layers). Use this as the foundation for the per-tensor encoding argument."

### 5. The Hidden Agenda
What does the audience want that they will not explicitly state?

*Examples*: 
- Reviewer: "I want to be the one who found the flaw. Give me something minor to catch so I don't dig for something major."
- Investor: "I want to believe I discovered you before other VCs."
- Committee: "I want to feel smart when I ask a question you answer perfectly."

---

## Audience Mapping Template

Before writing, fill this out:

```
Document type: __________________
Decision-maker: __________________
What they believe now: __________________
What they must believe after reading: __________________
Fatal objection (unaddressed = dead): __________________
Evidence that will change their mind: __________________
Ally (existing belief you can leverage): __________________
Hidden agenda: __________________
Time budget (seconds before they decide): __________________
```

If any field is blank, you are not ready to write.
