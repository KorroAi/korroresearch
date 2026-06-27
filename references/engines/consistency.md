# Consistency Engine

## Global Tracking

The engine tracks these across your entire document:

1. **Terminology** - Same concept, same name, everywhere
2. **Variables** - Same symbol, same meaning, across sections
3. **Datasets** - Dataset names consistent throughout
4. **Author names** - No misspellings or variations
5. **Figure numbering** - Sequential, no gaps, no duplicates
6. **Table numbering** - Sequential, no gaps, no duplicates
7. **Abbreviations** - Defined once, used consistently
8. **Citations** - Same key, same reference, everywhere

## Multi-Chapter Mode

For books and theses, cross-references ALL chapters:
```bash
python scripts/consistency_engine.py ch1.md ch2.md ch3.md --batch
```

Detects:
- Contradictory statements (Chapter 5 vs Chapter 2)
- Duplicate paragraphs (AI repetition after ~100 pages)
- Terminology drift (same concept renamed mid-book)
- Missing cross-references
