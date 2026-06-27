# VC-Specific Pitch Deck Templates

## Y Combinator Style

**Philosophy**: 30 seconds to impress. Build something people want.

Slide order:
1. **One-liner** - What you do in 8 words
2. **Problem** - Who has this problem? How big?
3. **Solution** - Demo or screenshot
4. **Traction** - Revenue, users, growth (MOST IMPORTANT)
5. **Team** - Why YOU can build this
6. **Market** - TAM, SAM, SOM
7. **Business Model** - How you make money
8. **Ask** - How much and for what

Tone: Punchy. Numbers-forward. No corporate jargon.

## Sequoia Style

**Philosophy**: Why now? What changed?

Slide order:
1. **Company Purpose** - One sentence
2. **Problem** - The pain point
3. **Solution** - Your approach
4. **Why Now?** - The timing question (Sequoia's signature slide)
5. **Market Size** - Bottom-up calculation
6. **Competition** - Why you win
7. **Product** - How it works
8. **Business Model** - Unit economics
9. **Team** - Relevant experience
10. **Financials** - Projections and assumptions

Tone: Analytical. Timing-focused. Competitive-aware.

## a16z Style

**Philosophy**: Software eats the world. What's the network effect?

Slide order:
1. **The Big Idea** - Paradigm shift
2. **Market Opportunity** - Trillion-dollar market?
3. **Product** - What you built
4. **Technology** - Why it's hard to copy
5. **Go-to-Market** - How you win distribution
6. **Network Effects** - How you get stronger with scale
7. **Team** - Founders who've done it before
8. **Roadmap** - What's next

Tone: Visionary. Technology-deep. Network-effect focused.

## Accel Style

**Philosophy**: Prepared mind. European-style due diligence.

Slide order:
1. **Executive Summary** - 3-paragraph overview
2. **Problem & Market** - Evidence of pain
3. **Solution** - Product demo
4. **Traction** - Customer logos, revenue, churn
5. **Go-to-Market** - Sales strategy, CAC, payback
6. **Competition** - Detailed matrix
7. **Team** - Why this team
8. **Financials** - 3-year model with assumptions
9. **Use of Funds** - Exactly how you'll spend the money

Tone: Thorough. Evidence-heavy. Risk-aware.

## Usage

```bash
python scripts/wizard.py --format pitch-deck --vc yc
python scripts/wizard.py --format pitch-deck --vc sequoia
python scripts/wizard.py --format pitch-deck --vc a16z
python scripts/wizard.py --format pitch-deck --vc accel
```
