# Source Manager Engine

## Supported Formats

| Format | Style | Common In |
|---|---|---|
| BibTeX | @article{key, author=..., title=..., ...} | LaTeX, CS papers |
| APA | Author (Year). Title. *Journal* | Social sciences |
| IEEE | [1] Author, "Title," *Journal*, Year | Engineering |
| ACM | Author. Year. Title. *Journal* | Computing |
| DOI | 10.xxxx/xxxxx | Universal identifier |
| arXiv | arXiv:xxxx.xxxxx | Preprints |

## Usage

```bash
python scripts/source_manager.py paper.md
python scripts/source_manager.py paper.md --format apa
python scripts/source_manager.py paper.md --verify
python scripts/source_manager.py paper.md --output references.bib
```
