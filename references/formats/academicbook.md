# Academic Book Structure

## Required Sections

### Front Matter
1. Title page
2. Copyright page
3. Dedication (optional)
4. Table of Contents
5. List of Figures
6. List of Tables
7. Foreword (by someone else)
8. Preface (by you)
9. Acknowledgements

### Body
- Chapters (10-20 typically)
- Each chapter: introduction, body, summary, exercises

### Back Matter
1. Appendices
2. Glossary
3. Bibliography
4. Index
5. Further Reading
6. Errata / Revision History

## Consistency Requirements

For 200-600 page books, the consistency engine tracks:
- Terminology across all chapters
- Concept definitions (defined once, referenced everywhere)
- Cross-references (Chapter X, Section Y must exist)
- Duplicate paragraphs (AI repetition after 100+ pages)
- Contradictions (Chapter 5 says X, Chapter 2 says not-X)

## Chapter Template

Each chapter follows:
1. Opening quote or hook (1 paragraph)
2. "What you will learn" box (3-5 bullets)
3. Body (3-5 sections)
4. Summary table
5. Exercises (3 levels: basic, intermediate, advanced)
6. Further reading

## Usage

```bash
python scripts/wizard.py --format book
python scripts/consistency_engine.py ch*.md --batch
```
