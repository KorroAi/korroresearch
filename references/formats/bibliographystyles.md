# Bibliography Styles

## Available Formats

| Style | Format Example | Common In |
|---|---|---|
| APA | Author, A. A. (Year). Title. *Journal*, *Vol*(Issue), Pages. | Social sciences |
| IEEE | [1] A. Author, "Title," *Journal*, vol. X, pp. Y-Z, Year. | Engineering |
| ACM | Author A., Author B. Year. Title. *Journal* Vol, Issue (Year), Pages. | Computing |
| Chicago | Author, First. "Title." *Journal* Volume (Year): Pages. | Humanities |
| Harvard | Author, A.A. (Year) 'Title', *Journal*, Vol(Issue), pp.Pages. | Business |
| BibTeX | @article{key, author={...}, title={...}, journal={...}, year={...}} | LaTeX |

## Auto-Generation

The source manager can generate references in any format from citation keys:

```bash
python scripts/source_manager.py paper.md --format apa
python scripts/source_manager.py paper.md --format ieee
python scripts/source_manager.py paper.md --format acm
python scripts/source_manager.py paper.md --format bibtex --output refs.bib
```

## Citation Verification

With `--verify`, the engine cross-references:
- DOI against CrossRef
- arXiv IDs against arXiv API
- Author names and years against Semantic Scholar

Unverified citations are flagged for manual review.
