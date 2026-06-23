# LaTeX IEEE / ACM Conference Format

Generate submission ready LaTeX for top conferences.

## When to Use

- IEEE / ACM conference submissions
- Camera ready papers
- Any venue requiring LaTeX

## IEEE Template

```latex
\documentclass[conference]{IEEEtran}
\usepackage{booktabs, colortbl, xcolor}
\usepackage{graphicx, subfig}
\usepackage{amsmath, amssymb}
\usepackage{hyperref}

\begin{document}

\title{Paper Title}

\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution}
}

\maketitle

\begin{abstract}
...
\end{abstract}
```

## Tables (booktabs style, mandatory)

```latex
\begin{table}[t]
\caption{Comparison on Dataset X. Best results in \textbf{bold}.}
\label{tab:comparison}
\begin{tabular}{lcccc}
\toprule
Method & PSNR $\uparrow$ & LPIPS $\downarrow$ & Runtime (ms) $\downarrow$ \\
\midrule
Baseline A & 23.4 & 0.145 & 120 \\
Baseline B & 24.1 & 0.132 & 95 \\
\textbf{Ours} & \textbf{25.7} & \textbf{0.118} & \textbf{72} \\
\bottomrule
\end{tabular}
\end{table}
```

## Figures

```latex
\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/teaser.pdf}
\caption{Overview of our method. (a) Input. (b) Previous method fails at X. (c) Our method succeeds.}
\label{fig:teaser}
\end{figure}
```

## Quality Checklist
- [ ] IEEEtran documentclass with conference option
- [ ] All tables use booktabs (toprule/midrule/bottomrule)
- [ ] No vertical lines in tables
- [ ] Figures are vector PDF
- [ ] Captions above tables, below figures
- [ ] References in IEEE style
- [ ] No em dashes anywhere in the source
