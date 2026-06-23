# Presentation Format - Conference Talks and Pitches

Generate slide decks for conferences, investor pitches, and seminars.

## When to Use

- Conference oral presentations (15-20 min)
- Investor pitch decks
- Seminar talks
- Poster presentations

## Format Options

### Reveal.js (recommended)
Best for web distribution, easy to share, works everywhere.

```html
<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js/dist/theme/white.css">
</head><body>
<div class="reveal"><div class="slides">

<section>
  <h2>Paper Title</h2>
  <p>Author Name</p>
</section>

<section>
  <h3>The Problem</h3>
  <ul><li>Point 1</li><li>Point 2</li></ul>
</section>

<section>
  <h3>Our Solution</h3>
  <p>Key insight and method overview</p>
</section>

<section>
  <h3>Results</h3>
  <img src="results.png" alt="Results">
</section>

</div></div>
<script src="https://cdn.jsdelivr.net/npm/reveal.js/dist/reveal.js"></script>
<script>Reveal.initialize();</script>
</body></html>
```

### Beamer (LaTeX)
For academic conferences expecting PDF slides.

```latex
\documentclass{beamer}
\usetheme{Madrid}
\title{Paper Title}
\author{Author Name}
\date{\today}
\begin{document}
\frame{\titlepage}
\frame{\frametitle{The Problem} ...}
\frame{\frametitle{Our Solution} ...}
\frame{\frametitle{Results} ...}
\end{document}
```

## Slide Design Rules

1. One message per slide
2. Max 6 lines of text per slide
3. Font size 24pt minimum
4. Figures must be readable from the back of the room
5. Color scheme consistent with paper
6. No full paragraphs - use bullet points
7. Title slide: paper title + authors + venue
8. Thank you slide: contact info + link to paper/code

## Talk Structure

| Slide Range | Content | Duration |
|-------------|---------|----------|
| 1 | Title | 10 sec |
| 2-4 | Problem and motivation | 2-3 min |
| 5-8 | Method and key insight | 4-5 min |
| 9-12 | Results and demos | 4-5 min |
| 13-14 | Limitations and future | 1-2 min |
| 15 | Thank you | 10 sec |

## Quality Checklist
- [ ] Each slide has one clear message
- [ ] Font size 24pt or larger
- [ ] Figures are high resolution
- [ ] Color scheme matches paper
- [ ] Talk fits within time limit
- [ ] Backup slides prepared for questions
- [ ] No em dashes in slides
