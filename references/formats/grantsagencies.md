# Grant Agency Templates

## NSF (National Science Foundation)

**Core requirement**: Intellectual Merit + Broader Impacts

Sections:
1. **Project Summary** (1 page) - Overview, intellectual merit, broader impacts
2. **Project Description** (15 pages max) - Problem, significance, approach, timeline
3. **References Cited**
4. **Biographical Sketches** (2 pages per PI)
5. **Budget & Budget Justification**
6. **Current & Pending Support**
7. **Facilities, Equipment & Other Resources**
8. **Data Management Plan** (2 pages)
9. **Postdoctoral Mentoring Plan** (if applicable)

Broader impacts must address: education, diversity, infrastructure, public benefit.

## NIH (National Institutes of Health)

**Core requirement**: Specific Aims + Significance + Approach

Sections:
1. **Specific Aims** (1 page) - What you will accomplish
2. **Research Strategy** (6-12 pages):
   a. Significance - Why this problem matters for health
   b. Innovation - What's new about your approach
   c. Approach - Detailed methods, preliminary data
3. **Human Subjects / Vertebrate Animals**
4. **Budget** - Modular or detailed
5. **Biosketches** (5 pages each)

NIH specific: Human subjects section required. Inclusion of women and minorities.

## ERC (European Research Council)

**Core requirement**: Groundbreaking, high-risk/high-gain

Sections:
1. **Extended Synopsis** (5 pages) - State-of-the-art, objectives, methodology, resources
2. **CV** (2 pages) - Academic record, key publications
3. **Track Record** (2 pages) - Early achievements, leadership
4. **Full Proposal** (15 pages) - Detailed research plan

ERC specific: Focus on the PI, not the team. "High-risk/high-gain" mandatory framing.

## Horizon Europe

**Core requirement**: Impact + Excellence + Implementation

Sections:
1. **Excellence** - Objectives, methodology, innovation
2. **Impact** - Expected outcomes, dissemination, exploitation
3. **Implementation** - Work plan, work packages, consortium, budget

Horizon specific: Consortium required (3+ entities from 3+ countries). Industrial partner preferred.

## DARPA

**Core requirement**: Heilmeier Catechism

Answer these 8 questions:
1. What are you trying to do? (no jargon)
2. How is it done today? What are the limits of current practice?
3. What is new in your approach? Why will it succeed?
4. Who cares? If successful, what difference will it make?
5. What are the risks and the payoffs?
6. How much will it cost? How long will it take?
7. What are the midterm and final exams to check for success?
8. What are the transition paths?

DARPA specific: Revolutionary, not incremental. Must show why current approaches CANNOT work.

## Usage

```bash
python scripts/wizard.py --format grant --agency nsf
python scripts/wizard.py --format grant --agency nih
python scripts/wizard.py --format grant --agency erc
python scripts/wizard.py --format grant --agency horizon
python scripts/wizard.py --format grant --agency darpa
```
