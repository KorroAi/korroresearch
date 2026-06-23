# LaTeX NeurIPS / ICML / ACL Format

Generate submission-ready LaTeX for top ML and NLP conferences. Complements `latexieee.md` which covers IEEE/ACM engineering conferences.

## When to Use

- NeurIPS, ICML, ICLR (ML conferences)
- ACL, EMNLP, NAACL (NLP conferences)
- CVPR, ICCV, ECCV (vision conferences  --  similar to ICML style)
- Any venue using their own `.sty` file (not IEEEtran)

## Key Differences from IEEE

| Aspect | IEEE/ACM | NeurIPS/ICML/ACL |
|---|---|---|
| Column layout | Two-column | Single-column (NeurIPS, ICML) or two-column (ACL, CVPR) |
| Abstract | Standard | NeurIPS: abstract + checklist required |
| Page limit | 8-10 pages | NeurIPS: 9 pages + unlimited references. ICML: 8 pages + references. |
| Author block | Standard | NeurIPS: anonymous by default (double-blind) |
| Template | IEEEtran.cls | Conference-provided `.sty` file |
| Citation style | IEEE numeric | Author-year (NeurIPS/ICML) or ACL numeric |

## NeurIPS Template

```latex
\documentclass{article}
\usepackage[preprint]{neurips_2026}  % Use [final] for camera-ready, [preprint] for submission

\title{Paper Title}

\author{
  Anonymous Author(s)  % Remove for camera-ready
}

\begin{document}
\maketitle

\begin{abstract}
...
\end{abstract}

% NeurIPS checklist is required and counts toward page limit
\section*{Checklist}
\begin{enumerate}
\item For all authors...
\item Did you include the license? See Section~\ref{sec:code}.
\end{enumerate}

\section{Introduction}
...
```

## ICML Template

```latex
\documentclass{article}
\usepackage{icml2026}

\icmltitle{Paper Title}
\icmlauthor{Author Name}{affiliation@email.com}

\begin{document}
\maketitle

\begin{abstract}
...
\end{abstract}
```

## ACL Template

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[hyperref]{acl2026}

\title{Paper Title}
\author{Author Name \\ Affiliation \\ \texttt{email@domain}}

\begin{document}
\maketitle

\begin{abstract}
...
\end{abstract}
```

## Tables (booktabs style — same rules as IEEE)

```latex
\begin{table}[t]
\caption{Comparison on Dataset X. Best in \textbf{bold}.}
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

## Figures (same as IEEE — vector PDFs)

```latex
\begin{figure}[t]
\centering
\includegraphics[width=\textwidth]{figures/teaser.pdf}
\caption{Overview of our method. (a) Input. (b) Previous method fails at X.
(c) Our method succeeds at X because Y.}
\label{fig:teaser}
\end{figure}
```

## NeurIPS-Specific: The Checklist

The NeurIPS paper checklist is required. Categories include:
1. **Claims**: Do claims match experimental evidence?
2. **Limitations**: Are limitations discussed?
3. **Theory**: Are theoretical results clearly stated with assumptions?
4. **Experiments**: Are experimental details sufficient for reproducibility?
5. **Code & Data**: Are code and data available?
6. **Ethics**: IRB approval, data privacy, potential misuse?

Answer every question honestly. Vague answers are worse than honest "no" answers with explanations.

## Double-Blind Rules (NeurIPS, ICML, ICLR, ACL)

- Remove author names, affiliations, and acknowledgments from submission.
- Cite your own prior work in the third person: "Smith et al. (2025) showed..." not "We previously showed..."
- Do not include links to your GitHub in the paper body. Use anonymous repositories.
- Do not thank specific people or funding sources in the submission.
- After acceptance: add everything back for the camera-ready.

## Quality Checklist
- [ ] Correct template downloaded from official conference website
- [ ] Page limit respected (check whether references count)
- [ ] Double-blind rules followed (if applicable)
- [ ] NeurIPS checklist completed (if applicable)
- [ ] All tables use booktabs (toprule/midrule/bottomrule)
- [ ] No vertical lines in tables
- [ ] Figures are vector PDFs
- [ ] Captions above tables, below figures
- [ ] No em dashes in source
- [ ] References formatted per venue style
