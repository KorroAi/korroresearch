#!/usr/bin/env python3
"""
KORRO Research -- Interactive Wizard

One command. Answer questions. Get a complete document skeleton with
section prompts, a checklist, and exact next steps.

Usage:
    python scripts/wizard.py
    python scripts/wizard.py --format pitch-deck --vc yc
    python scripts/wizard.py --format paper --venue neurips
    python scripts/wizard.py --format grant --agency nsf
    python scripts/wizard.py --batch "My idea" "Why now" "Audience" "Worldview" "Name"
    python scripts/wizard.py --help
"""

import sys
import os
import re
import argparse
from pathlib import Path
from datetime import datetime

SKILL_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = SKILL_DIR / "output"

# ── File naming ─────────────────────────────────────────────────

def slugify(text):
    """Convert a title or project name into a clean filename slug.

    Rules:
      - Lowercase
      - Alphanumeric + hyphens only
      - No leading/trailing hyphens
      - Collapse consecutive hyphens
      - Truncate to 60 chars max, break at word boundary
      - Fallback: 'untitled' if empty after cleaning
    """
    if not text or text.strip().upper() in ("UNTITLED", "FILL IN", "NEEDS DEFINITION", ""):
        return "untitled"
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    if len(slug) > 60:
        slug = slug[:60].rstrip("-")
        # try to break at a word boundary
        last_hyphen = slug.rfind("-")
        if last_hyphen > 20:
            slug = slug[:last_hyphen]
    return slug or "untitled"


# ── Helpers ────────────────────────────────────────────────────
STYLE = {
    "divider": "=" * 58,
    "star": "*",
    "arrow": "->",
    "check": "[OK]",
}

def divider(): print(f"\n  {STYLE['divider']}")
def gap(): print()
def say(text): print(f"  {text}")
def star(text): print(f"\n  {STYLE['star']} {text}")
def check(text): print(f"    {STYLE['check']} {text}")
def arrow(text): print(f"    {STYLE['arrow']} {text}")

def safe_ask(prompt):
    """Ask a question, handling EOFError (non-interactive mode)."""
    try:
        return input(f"  {prompt} ").strip()
    except EOFError:
        say("\n  [NON-INTERACTIVE MODE DETECTED]")
        say("  Use --batch to skip prompts: python scripts/wizard.py --format paper --batch \"idea\" \"why\" \"audience\" \"worldview\" \"name\"")
        sys.exit(1)
    except KeyboardInterrupt:
        say("\n\n  Interrupted. No file was generated.")
        sys.exit(130)


# ── Formats ────────────────────────────────────────────────────

# ── Format targets per type ─────────────────────────────────────
# words_per_page = 280 (standard book 6x9) or 350 (8.5x11 article)
# slide_words = speaker notes, ~60 words per minute spoken

FORMATS = {
    "1": {
        "name": "Research Paper (Conference)",
        "key": "paper",
        "page_target": "6 to 10 pages",
        "word_target": "3,500 to 4,500 words",
        "sections": [
            ("Abstract", "One paragraph: problem, why unsolved, your method, key result.",
             120, 180),
            ("Introduction", "Part A: What task and why it matters. Part B: Why existing methods fail (technical reasons). Part C: Your method and why it works.",
             800, 1200),
            ("Related Work", "Group by approach. Each paragraph = one line of work + its limitation + your advantage.",
             400, 600),
            ("Method", "Overview first. Then each component: motivation -> design -> rationale. Reproducibility: hyperparameters, hardware, seeds.",
             800, 1200),
            ("Experiments", "Q1: Better than baselines? Q2: Which modules matter (ablation)? Q3: How far does it generalize?",
             800, 1200),
            ("Conclusion", "Summary (no copy-paste). Limitations (honest). Future work (specific).",
             300, 500),
        ],
        "next_steps": [
            "Load references/sections/abstract.md to write the abstract",
            "Load references/processes/ideation.md for the Shannon Filter",
            "Load references/processes/impact.md for the unignorable document principles",
            "Run: python scripts/math_generator.py paper.md --notation",
            "Run: python scripts/hallucination_checker.py paper.md --mode classify",
            "Run: python scripts/review_engine.py paper.md --venue <name>",
            "Run: python scripts/reproducibility_checklist.py paper.md",
            "Run: python scripts/claim_checker.py paper.md --strict",
        ],
    },
    "2": {
        "name": "Pitch Deck (Investor)",
        "key": "pitch",
        "page_target": "12 slides",
        "word_target": "~800 words (speaker notes)",
        "sections": [
            ("Slide 1: One-Liner", "Company name + what you do in one sentence.",
             10, 20),
            ("Slide 2: The Problem", "Whose problem? How big? How painful? One stat + one quote.",
             40, 80),
            ("Slide 3: The Solution", "What you built. One screenshot. Three bullet points max.",
             40, 80),
            ("Slide 4: The Market", "TAM, SAM, SOM. Bottom-up calculation, not top-down.",
             60, 100),
            ("Slide 5: The Insight", "Why now? Why you? What do you know that nobody else knows?",
             50, 100),
            ("Slide 6: The Product", "2-3 screenshots with captions. One feature per visual.",
             50, 80),
            ("Slide 7: Traction", "Revenue, users, pilots, LOIs, waitlist. Graph even if small.",
             60, 100),
            ("Slide 8: Business Model", "Pricing. Unit economics. Comparables.",
             50, 80),
            ("Slide 9: Competition", "2x2 matrix with you top-right. Honest about competitors.",
             50, 80),
            ("Slide 10: Team", "3-4 people. Photo + name + role + ONE relevant credential.",
             40, 60),
            ("Slide 11: The Ask", "Amount, use of funds, current commitments.",
             40, 80),
            ("Slide 12: The Vision", "If you win, what does the world look like? One sentence.",
             20, 40),
        ],
        "next_steps": [
            "Load references/formats/pitchdeck.md for detailed slide rules",
            "Load references/formats/vctemplates.md for VC-specific templates",
            "Load references/formats/financialmodel.md for CAC, LTV, burn, runway",
            "Load references/formats/competitivelandscape.md for competitor matrix",
            "Load references/processes/impact.md -- Principle 7 (Opening) is critical for decks",
            "Run: python scripts/generate_figures.py --diagram architecture (no placeholders!)",
        ],
    },
    "3": {
        "name": "Grant Proposal",
        "key": "grant",
        "page_target": "5 to 15 pages",
        "word_target": "4,000 to 8,000 words",
        "sections": [
            ("Specific Aims (1 page)", "Para 1: The PROBLEM. Para 2: The APPROACH. Para 3: The IMPACT. Bold your hypothesis.",
             350, 450),
            ("Research Strategy", "Significance -> Innovation -> Approach. Preliminary results integrated into each aim.",
             1200, 3000),
            ("Preliminary Results", "For each: what you did, what you found, what it implies. Error bars mandatory.",
             800, 1500),
            ("Budget Justification", "Personnel, equipment, travel, materials. Every item traced to an aim.",
             400, 800),
            ("Timeline & Milestones", "Quarter by quarter. One milestone per quarter. Every risk has mitigation.",
             400, 800),
            ("Broader Impact", "Scientific impact. Societal impact. Education. Open science commitment with license + timeline.",
             400, 800),
        ],
        "next_steps": [
            "Load references/processes/grantsections.md for detailed section rules",
            "Load references/processes/impact.md -- Principle 3 (make the agency the hero)",
            "Load references/processes/audience.md -- understand the grant panel mindset",
            "Preliminary results must exist before writing. If you have none, stop and run experiments.",
        ],
    },
    "4": {
        "name": "White Paper",
        "key": "whitepaper",
        "page_target": "5 to 20 pages",
        "word_target": "3,500 to 7,000 words",
        "sections": [
            ("Executive Summary", "The crisis or opportunity. Your solution in one paragraph. The ONE thing the reader must remember.",
             200, 400),
            ("The Problem", "Quantify the pain. Show why current solutions are structurally broken.",
             600, 1200),
            ("The Architecture", "Your solution, top-down. Diagrams. Not implementation details, design principles.",
             1000, 2000),
            ("Migration Path", "How to get from current state to your architecture. Incremental steps. No rip-and-replace.",
             600, 1200),
            ("Impact & ROI", "What changes if adopted? Cost savings, speed, capability. Quantified.",
             500, 1000),
            ("Call to Action", "The first step the reader should take. Specific. Time-bound.",
             200, 400),
        ],
        "next_steps": [
            "Load references/processes/impact.md -- Principle 1 (destroy a worldview) is essential",
            "Load references/processes/audience.md -- understand the decision-maker",
            "Load references/formats/htmlpdf.md -- generate professional PDF",
            "Run: python scripts/generate_pdf.py whitepaper.md whitepaper.pdf --template single-column",
        ],
    },
    "5": {
        "name": "Magazine / Trade Article",
        "key": "magazine",
        "page_target": "2 to 4 magazine pages",
        "word_target": "1,500 to 2,500 words",
        "sections": [
            ("The Hook", "One paragraph that makes the reader NEED to know more. Anecdote, statistic, or provocation.",
             150, 300),
            ("The Context", "Why this matters NOW. What changed? What's at stake?",
             300, 500),
            ("The Deep Dive", "The technical content, explained so a smart non-expert understands. Metaphors welcome. No equations.",
             600, 1000),
            ("The Human Element", "Who benefits? Who is affected? A quote, a story, a concrete example.",
             300, 500),
            ("The Takeaway", "What should the reader do, think, or question after reading? One memorable sentence.",
             150, 200),
        ],
        "next_steps": [
            "Load references/formats/magazine.md for magazine-specific rules",
            "Load references/processes/impact.md -- Principle 7 (opening) is everything",
            "Study the target magazine's last 6 months of articles. Match their tone.",
            "Magazine articles are PITCHED before they are written. Write a 3-sentence pitch first.",
        ],
    },
    "6": {
        "name": "Academic Book",
        "key": "book",
        "page_target": "200 to 600 pages",
        "word_target": "60,000 to 120,000 words",
        "sections": [
            ("Preface", "Who is this book for? What will they be able to do after reading? Why you wrote it.",
             800, 1500),
            ("Chapter 1: The World As You Know It", "Establish shared reality. The problems the reader faces daily. Foundation chapter: the current state of the field.",
             4000, 8000),
            ("Chapter 2: The Architecture", "Deep foundation. The core concepts the reader needs before the journey. Build mental models.",
             4000, 8000),
            ("Chapter 3: The Tension (Part 1)", "First dimension of the problem. What breaks? What doesn't make sense? Evidence + narrative.",
             4000, 8000),
            ("Chapter 4: The Tension (Part 2)", "Second dimension. Deepen the crisis. Case studies. Contradictions.",
             4000, 8000),
            ("Chapter 5: The Diagnosis", "Why things break. Root cause analysis. The core mechanism. This is the book's theoretical center.",
             4000, 8000),
            ("Chapter 6: The Resolution (Part 1)", "First pillar of the solution. Framework, method, or new approach. Motivation -> mechanism -> application.",
             4000, 8000),
            ("Chapter 7: The Resolution (Part 2)", "Second pillar. Extend the framework. Address edge cases. Show it generalizes.",
             4000, 8000),
            ("Chapter 8: The Resolution (Part 3)", "Third pillar if needed, or the counter-argument chapter. Address the strongest objections.",
             4000, 8000),
            ("Chapter 9: A Framework for Action", "From theory to practice. Guidelines, checklists, decision trees. What to DO with what you learned.",
             4000, 8000),
            ("Chapter 10: The World As It Could Be", "Synthesis. Map the territory ahead. Open problems. Policies. Research agenda. The call to action.",
             4000, 8000),
            ("Appendices", "Reference material, datasets, instruments, glossary, further reading, claim-evidence map.",
             3000, 6000),
        ],
        "next_steps": [
            "Load references/processes/ideation.md -- Protocol 1 applies to books too",
            "Load references/processes/impact.md -- Principle 4 (inevitability arc) at chapter scale",
            "Load references/processes/bookconsistency.md -- CRITICAL for 100+ pages",
            "Load references/formats/academicbook.md for structure",
            "Write Chapter 1 and the final chapter FIRST. Then fill in the middle.",
            "Run: python scripts/consistency_engine.py ch*.md --batch after EVERY chapter",
            "Each chapter = 4,000-8,000 words. This is a 200-600 page book.",
        ],
    },
    "7": {
        "name": "Technical Blog Post",
        "key": "blog",
        "page_target": "5 to 10 minute read",
        "word_target": "1,200 to 2,000 words",
        "sections": [
            ("The Headline", "Specific, benefit-driven, not clickbait. Passes the 'would I click?' test.",
             1, 1),
            ("The Opening (3 sentences)", "Sentence 1: The problem. Sentence 2: The insight. Sentence 3: What you'll learn.",
             80, 120),
            ("The Problem Section", "What was broken? Quantify. Show a graph.",
             200, 400),
            ("The Solution Section", "Key insight + one diagram. Explained so a smart undergrad understands.",
             300, 600),
            ("The Results Section", "Before/after. Bold numbers. Graph that speaks for itself.",
             200, 400),
            ("The Code Section", "Runnable. Import statements included. One concept per code block.",
             200, 400),
            ("The Closing", "One-sentence summary. Link to code/paper. One question for comments.",
             80, 120),
        ],
        "next_steps": [
            "Load references/formats/blogpost.md for detailed rules",
            "Load references/sections/title.md -- the headline IS the blog post",
            "Write the tweet before the post. If the tweet doesn't work, the post won't either.",
        ],
    },
    "8": {
        "name": "Conference Talk / Keynote",
        "key": "talk",
        "page_target": "15 slides / 15-minute talk",
        "word_target": "~1,200 words (speaker notes)",
        "sections": [
            ("Slide 1: The Hook", "One image + one devastating stat.",
             20, 40),
            ("Slides 2-4: The Problem", "Why existing solutions fail. Technical reasons, not complaints.",
             150, 250),
            ("Slides 5-8: The Method", "Key insight. One diagram that explains everything. Build up step by step.",
             250, 400),
            ("Slides 9-12: Results", "Before/after. Live demo if possible. Numbers in bold.",
             250, 400),
            ("Slides 13-14: Limitations + Future", "What we don't know yet. Where the field goes next.",
             100, 200),
            ("Slide 15: Thank You", "Contact info. Link to paper/code. One question for the audience.",
             20, 40),
        ],
        "next_steps": [
            "Load references/formats/presentation.md for Beamer/Reveal.js setup",
            "Load references/processes/impact.md -- Principle 5 (memorability hooks) is critical",
            "Practice the 15-minute version. Then the 5-minute version. Then the 2-minute hallway version.",
            "Answer questions BEFORE they're asked. Have backup slides for every anticipated question.",
        ],
    },
    "9": {
        "name": "Thesis / Dissertation",
        "key": "thesis",
        "page_target": "100 to 300 pages",
        "word_target": "40,000 to 80,000 words",
        "sections": [
            ("Abstract", "Problem, methodology, key results, contribution. 300 words max.",
             200, 300),
            ("Acknowledgements", "Advisor, committee, collaborators, funding sources, family.",
             200, 400),
            ("Chapter 1: Introduction", "Problem statement, motivation, contributions, thesis outline.",
             2000, 4000),
            ("Chapter 2: Literature Review", "Systematic review, taxonomy, gap analysis, table of prior work.",
             4000, 8000),
            ("Chapter 3: Method", "Deep methodology. Reproducible. Every equation defined. Algorithm boxes.",
             4000, 8000),
            ("Chapter 4: Experiments", "Setup, baselines, main results, ablations, error analysis.",
             4000, 8000),
            ("Chapter 5: Discussion", "What it means. Limitations. Comparison to prior work. Generalizability.",
             3000, 6000),
            ("Chapter 6: Conclusion", "Summary, contributions, future work, open problems.",
             2000, 4000),
            ("Appendices", "Proofs, hyperparameters, additional results, dataset details, code listing.",
             4000, 10000),
            ("Bibliography", "APA/IEEE/ACM/Chicago/Harvard/BibTeX. Auto-generated.",
             2000, 4000),
        ],
        "next_steps": [
            "Load references/formats/bibliographystyles.md for citation format",
            "Load references/processes/bookconsistency.md -- CRITICAL for 100+ pages",
            "Load references/formats/academicbook.md for front/back matter",
            "Run: python scripts/consistency_engine.py ch*.md --batch after each chapter",
            "Run: python scripts/hallucination_checker.py thesis.md before submission",
        ],
    },
}


def resolve_format(value):
    """Resolve a format by key, number, or name prefix. Returns (choice_key, format_info)."""
    # By number
    if value in FORMATS:
        return value, FORMATS[value]

    # By key
    by_key = {v["key"]: (k, v) for k, v in FORMATS.items()}
    if value in by_key:
        return by_key[value]

    # By name (case-insensitive prefix match)
    value_lower = value.lower()
    for k, v in FORMATS.items():
        if value_lower in v["name"].lower():
            return k, v

    # Fallback: show available formats
    print(f"  Unknown format: '{value}'. Available formats:", file=sys.stderr)
    for k, v in FORMATS.items():
        print(f"    [{k}] {v['name']}  (--format {v['key']})", file=sys.stderr)
    sys.exit(1)


# ── Generation ─────────────────────────────────────────────────

def generate_skeleton(format_info, ideation):
    fmt_name = format_info["name"]
    sections = format_info["sections"]
    page_target = format_info.get("page_target", "TBD")
    word_target = format_info.get("word_target", "TBD")
    idea = ideation

    output = [f"# {idea.get('name') or 'UNTITLED'}", ""]
    output.append("<!-- Generated by KORRO Research Wizard -->")
    output.append(f"<!-- Format: {fmt_name} -->")
    output.append(f"<!-- Target: {page_target} | ~{word_target} -->")
    output.append(f"<!-- Date: {datetime.now().strftime('%Y-%m-%d %H:%M')} -->")
    output.append(f"<!-- Insight: {idea.get('insight') or 'FILL IN'} -->")
    output.append("")
    output.append(f"> **FORMAT TARGET**: {page_target}")
    output.append(f"> **WORD COUNT**: {word_target}")
    output.append(f"> **Sections**: {len(sections)}")
    output.append("")

    total_min = 0
    total_max = 0
    for section_title, section_prompt, wmin, wmax in sections:
        total_min += wmin
        total_max += wmax
        output.append(f"## {section_title}")
        output.append("")
        output.append(f"> **Words**: {wmin} to {wmax}")
        output.append(f"> **Prompt**: {section_prompt}")
        output.append("")
        output.append(f"<!-- Write {wmin}-{wmax} words for this section. -->")
        output.append("")
        output.append("[START WRITING HERE]")
        output.append("")

    output.append("---")
    output.append("")
    output.append("## TARGET SUMMARY")
    output.append("")
    output.append(f"| Metric | Target |")
    output.append(f"|---|---|")
    output.append(f"| Format | {fmt_name} |")
    output.append(f"| Pages | {page_target} |")
    output.append(f"| Words | {word_target} |")
    output.append(f"| Section word range | {total_min:,} to {total_max:,} |")
    output.append(f"| Sections | {len(sections)} |")
    output.append("")
    output.append("---")
    output.append("")
    output.append("## IDEATION NOTES (delete before submitting)")
    output.append("")
    output.append(f"- **One-sentence insight**: {idea.get('insight') or 'NEEDS DEFINITION'}")
    output.append(f"- **Why now**: {idea.get('why_now') or 'NEEDS DEFINITION'}")
    output.append(f"- **Decision-maker**: {idea.get('audience') or 'NEEDS DEFINITION'}")
    output.append(f"- **Worldview to destroy**: {idea.get('worldview') or 'NEEDS DEFINITION'}")
    output.append(f"- **Name**: {idea.get('name') or 'NEEDS DEFINITION'}")
    output.append("")

    return "\n".join(output)


def show_next_steps(format_info):
    star("NEXT STEPS")
    for step in format_info.get("next_steps", []):
        check(step)
    gap()


# ── Main ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="KORRO Research Wizard -- generate document skeletons",
        add_help=False,
    )
    parser.add_argument("--help", action="store_true", help="Show this help")
    parser.add_argument("--format", type=str, help="Format key (paper, pitch, grant, whitepaper, magazine, book, blog, talk, thesis)")
    parser.add_argument("--venue", type=str, choices=["neurips", "icml", "cvpr", "eccv", "iccv", "acl", "emnlp"],
                       help="Target conference venue (for --format paper)")
    parser.add_argument("--vc", type=str, choices=["yc", "sequoia", "a16z", "accel"],
                       help="VC firm template (for --format pitch)")
    parser.add_argument("--agency", type=str, choices=["nsf", "nih", "erc", "horizon", "darpa"],
                       help="Funding agency template (for --format grant)")
    parser.add_argument("--style", type=str, choices=["nature", "neurips", "mit", "google", "mckinsey", "yc", "nsf"],
                       help="Style preset for tone/terminology/formatting")
    parser.add_argument("--export", type=str, choices=["beamer", "pptx", "revealjs", "googleslides", "medium", "devto", "hashnode", "substack", "ghost"],
                       help="Export target platform")
    parser.add_argument("--batch", nargs=5, metavar=("INSIGHT", "WHY_NOW", "AUDIENCE", "WORLDVIEW", "NAME"),
                        help="Non-interactive: provide all 5 ideation answers at once")

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    if args.help:
        parser.print_help()
        print("\nFormats:")
        for k, v in FORMATS.items():
            print(f"  [{k}] {v['name']}  (--format {v['key']})")
        print("\nOptions:")
        print("  --venue    neurips|icml|cvpr|eccv|iccv|acl|emnlp  (paper)")
        print("  --vc       yc|sequoia|a16z|accel                   (pitch)")
        print("  --agency   nsf|nih|erc|horizon|darpa               (grant)")
        print("  --style    nature|neurips|mit|google|mckinsey|yc|nsf")
        print("  --export   beamer|pptx|revealjs|medium|devto|...")
        print("\nExamples:")
        print("  python scripts/wizard.py")
        print("  python scripts/wizard.py --format paper --venue neurips")
        print("  python scripts/wizard.py --format pitch --vc yc")
        print("  python scripts/wizard.py --format grant --agency nsf")
        print("  python scripts/wizard.py --format paper --batch 'My insight' 'Why now' 'Reviewers' 'Old belief' 'ProjectName'")
        return 0

    gap()
    print("  " + "=" * 60)
    print("  |      KORRO RESEARCH -- Interactive Wizard                |")
    print("  |      One command. Answer questions. Get a document.     |")
    print("  " + "=" * 60)

    # Step 1: Choose format
    if args.format:
        _, format_info = resolve_format(args.format)
    else:
        star("CHOOSE YOUR FORMAT")
        say("What are you creating today?")
        say("  Beginner-friendly: [1] [2] [7]\n")
        for key, fmt in FORMATS.items():
            label = "[B]" if key in ("1", "2", "7") else "   "
            say(f"  [{key}] {label} {fmt['name']}")
        gap()
        choice = safe_ask(f"Enter number (1-{len(FORMATS)}):") or "1"
        _, format_info = resolve_format(choice)

    divider()
    star(f"SELECTED: {format_info['name']}")
    say(f"Sections: {len(format_info['sections'])}")
    divider()

    # Step 2: Ideation
    if args.batch:
        ideation = {
            "insight": args.batch[0],
            "why_now": args.batch[1],
            "audience": args.batch[2],
            "worldview": args.batch[3],
            "name": args.batch[4],
        }
        star("IDEATION (--batch mode)")
        check(f"Insight: {ideation['insight'][:60]}...")
        check(f"Why now: {ideation['why_now'][:60]}...")
        check(f"Audience: {ideation['audience'][:60]}...")
        check(f"Worldview: {ideation['worldview'][:60]}...")
        check(f"Name: {ideation['name']}")
    else:
        star("IDEATION -- The Shannon Filter")
        say("Don't worry if you don't have perfect answers. Type what you know.")
        say("Type 'skip' on any question you're not ready for.\n")

        say("Example: 'We built a system that cuts AI training costs by 60%.'")
        say("Example: 'People will pay to sleep in strangers' homes if it feels safe.'")
        insight = safe_ask("What's your ONE big idea? (one sentence, no jargon):")
        gap()

        say("Examples: 'Nobody thought to apply X to Y before.'")
        say("          'The technology to do this didn't exist until last year.'")
        say("          'I don't know yet -- that's what I need to figure out.'")
        why_now = safe_ask("Why hasn't this been done before?")
        gap()

        say("Examples: 'Conference reviewers in machine learning.'")
        say("          'A venture capitalist who invests in AI infrastructure.'")
        say("          'The NSF grant panel.'")
        audience = safe_ask("Who decides if this succeeds? (reviewer, investor, grant panel, etc.):")
        gap()

        say("Example: 'They believe X is already solved. I will show it is not.'")
        say("Example: 'They think this market is too small. My data says otherwise.'")
        say("(This is the hardest question. 'skip' is fine.)")
        worldview = safe_ask("What belief does your audience hold that you will prove wrong?")
        gap()

        name = safe_ask("What is your project/method/company called? (or a working title):")

        ideation = {
            "insight": insight,
            "why_now": why_now,
            "audience": audience,
            "worldview": worldview,
            "name": name,
        }

    divider()

    # Step 3: Generate
    star("GENERATING DOCUMENT SKELETON")
    skeleton = generate_skeleton(format_info, ideation)

    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"\n  Error: Cannot create output directory: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate professional filename: {Title_Slug}_{format_key}_{YYYY-MM-DD}.md
    doc_slug = slugify(ideation.get("name") or ideation.get("insight", ""))
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    out_path = OUTPUT_DIR / f"{doc_slug}_{format_info['key']}_{date_stamp}.md"
    try:
        out_path.write_text(skeleton, encoding="utf-8")
    except OSError as e:
        print(f"\n  Error: Cannot write output file: {e}", file=sys.stderr)
        sys.exit(1)

    check(f"Saved: {out_path}")
    say(f"  {len(skeleton.splitlines())} lines generated")
    divider()

    # Step 4: Show what was generated
    star("DOCUMENT STRUCTURE")
    say(f"Target: {format_info.get('page_target', 'TBD')} | ~{format_info.get('word_target', 'TBD')}")
    for sec_title, *_ in format_info["sections"]:
        arrow(sec_title)
    divider()

    # Step 5: Next steps
    show_next_steps(format_info)

    star("YOU ARE READY")
    say("Open the generated file. Each section has prompts and tips in comments.")
    say("New to this? Open QUICKSTART.md -> PATH 0. It walks you through everything.")
    say("Start with the easiest section. Build momentum. You've got this.")
    gap()

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n  Interrupted. No file was generated.")
        sys.exit(130)
