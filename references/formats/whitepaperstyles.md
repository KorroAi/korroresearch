# White Paper Style Templates

## Gartner Style

Analyst-focused. Magic Quadrant positioning.

Structure:
1. **Executive Summary** - Key findings in 3 bullets
2. **Market Definition** - What space are you in
3. **Market Drivers** - Why this space is growing
4. **Vendor Landscape** - Who competes (position yourself)
5. **Technology Analysis** - Deep dive into your approach
6. **Recommendations** - What enterprises should do

Tone: Objective. Data-backed. Vendor-neutral framing.

## Microsoft Style

Developer-focused. Technical depth.

Structure:
1. **Executive Summary** - What we built and why
2. **Technical Architecture** - Diagrams, components, data flow
3. **Getting Started** - Code samples, SDKs
4. **Performance** - Benchmarks against alternatives
5. **Migration Guide** - How to switch from competitors
6. **Roadmap** - What's coming next

Tone: Technical. Code-heavy. Practical. "Developers, developers, developers."

## AWS Style

Product-focused. Service-oriented.

Structure:
1. **What is [Product]?** - One-sentence definition
2. **Why [Product]?** - Pain points it solves
3. **How It Works** - Architecture diagram
4. **Features** - Bulleted capability list
5. **Pricing** - Clear cost structure
6. **Getting Started** - 5-minute quickstart

Tone: Customer-obsessed. Benefit-focused. Diagrams everywhere.

## Google Cloud Style

Research-forward. Data-driven.

Structure:
1. **The Research Behind [Product]** - What we discovered
2. **Technical Innovation** - The novel approach
3. **Benchmarks** - Performance data
4. **Case Studies** - Who's using it and results
5. **Open Source** - What we're contributing back
6. **What's Next** - Research roadmap

Tone: Research-backed. Open. Thought leadership.

## Usage

```bash
python scripts/wizard.py --format white-paper --style gartner
python scripts/wizard.py --format white-paper --style microsoft
python scripts/wizard.py --format white-paper --style aws
python scripts/wizard.py --format white-paper --style google-cloud
```
