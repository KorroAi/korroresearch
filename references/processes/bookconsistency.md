# Book Consistency Process

## The Problem

AI-generated long-form content has a predictable failure mode: after about 100 pages, it starts repeating itself. Paragraphs reappear. Concepts get renamed. Chapter 5 contradicts Chapter 2. This is fatal for books and theses.

## The Solution: Global Memory

The consistency engine maintains a global memory across all chapters:

### What It Tracks
- **Terminology map** - Every term and its canonical name
- **Concept registry** - Every concept, its definition, and its introduction point
- **Citation index** - Every cited work across all chapters
- **Variable map** - Every mathematical symbol and its meaning
- **Figure/Table counter** - Sequential numbering across chapters
- **Paragraph fingerprint** - Detect duplicate paragraphs

### How to Use

1. Write Chapter 1 normally
2. Run: `python scripts/consistency_engine.py ch1.md`
3. Write Chapter 2, referencing the consistency report
4. Run: `python scripts/consistency_engine.py ch1.md ch2.md --batch`
5. Fix any flagged issues
6. Continue for all chapters

### When Writing Long Documents

- Run the consistency engine after EVERY chapter
- Fix terminology drift immediately (don't let it accumulate)
- If the engine flags a duplicate paragraph, rewrite it completely
- Keep a glossary file updated manually as a fallback

## Anti-Patterns

- DON'T write all chapters in one session (increases repetition)
- DON'T ignore consistency warnings (they compound)
- DON'T rename concepts mid-book without updating all chapters
- DON'T skip the consistency check before submission
