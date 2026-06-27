# Blog Post Export Options

## Platform-Specific Formatting

| Platform | Max Words | Special Features | Style |
|---|---|---|---|
| Medium | No limit | Claps, responses, publications | Narrative, personal |
| Dev.to | No limit | Reactions, series, listings | Technical, community |
| Hashnode | No limit | Custom domain, newsletter | Technical, SEO-first |
| Substack | No limit | Email, paid subscriptions | Newsletter, personal |
| Ghost | No limit | Membership, custom themes | Professional, brand |

## Export Checklist per Platform

### Medium
- Canonical URL if cross-posted
- Tags (max 5)
- Featured image (1600x840)
- Subtitle and kicker

### Dev.to
- Tags (max 4)
- Series if multi-part
- Cover image (1000x420)
- Liquid tags for embeds

### Hashnode
- Custom domain option
- Series and table of contents
- Newsletter integration
- Dark/light mode

### Substack
- Newsletter subject line
- Preview text (140 chars)
- Paid/free segmentation
- Comments on by default

### Ghost
- Member-only option
- Custom excerpt
- Meta title and description
- Feature image

## Cross-Platform SEO

- Schema.org Article markup
- Open Graph tags (title, description, image)
- Twitter Card metadata
- Canonical URL (if cross-posting)

## Usage

```bash
python scripts/wizard.py --format blog --export medium
python scripts/wizard.py --format blog --export devto
```
