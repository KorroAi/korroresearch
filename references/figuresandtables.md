# Figures and Tables - Publication Ready Visuals

## Core Philosophy

Visuals are read FIRST. A reviewer who skims only figures and tables should understand your paper's story.

## Figure Design Rules

### Message First
Every figure must answer: "What should the reader conclude from this?"

Before creating any figure, write the one sentence message. If you cannot, the figure has no purpose.

### Types and Standards

**Teaser Figure (Figure 1)**
- Shows the problem AND your solution in one glance
- Side by side: input -> previous method (fails) -> our method (succeeds)
- Or: conceptual diagram showing the key insight
- Must be comprehensible in 10 seconds

**Architecture/ Pipeline Figure**
- Top down flow showing data through components
- Consistent shapes for consistent concepts
- Color coded modules that match ablation table colors
- Minimal text: label components, let captions explain

**Results Charts**
- Bar charts: sorted by value, include error bars
- Line charts: max 5 6 series, distinct markers + colors
- Scatter plots: use alpha for density
- Heatmaps: include colorbar with units
- Confusion matrices: normalize, show percentages

**Qualitative Results**
- Show representative examples (best, median, failure cases)
- Side by side with ground truth and baselines
- Zoomed insets for details
- Consistent colormap across all examples

### Color Standards
- **Colorblind safe palette**: viridis, cividis, plasma, inferno (matplotlib built in)
- **Avoid**: red green pairs, rainbow colormaps
- **Highlight color**: a single distinct color (orange or blue) for YOUR method
- **Baseline colors**: muted grays, blues
- **Black text on white background**: never colored text on colored background

### Typography in Figures
- Font size: at least as large as body text
- Sans serif (Arial, Helvetica) for figure text
- No title inside the figure (use caption)
- Axis labels with units: "PSNR (dB)", "Runtime (ms)", "Memory (GB)"
- Legend inside or beside plot area, never covering data

### Resolution and Formats
- Vector: PDF, SVG, EPS for diagrams and charts
- Raster: PNG at 300+ DPI for photos/screenshots
- Never JPEG for text or line art

## Table Design Rules

### Structure
```
\caption{Comparison on Dataset X. Best in \textbf{bold}, second-best \underline{underlined}.}
\label{tab:comparison}
\begin{tabular}{lcccc}
\toprule
Method & Metric A ↑ & Metric B ↓ & Metric C ↑ & Avg Rank ↓ \\
\midrule
Baseline 1 & 23.4 & 0.145 & 0.892 & 3.8 \\
Baseline 2 & 24.1 & 0.132 & 0.901 & 3.2 \\
\textbf{Ours} & \textbf{25.7} & \textbf{0.118} & \textbf{0.923} & \textbf{1.4} \\
\bottomrule
\end{tabular}
```

### Formatting Rules
1. Caption ABOVE the table
2. No vertical lines
3. \toprule, \midrule, \bottomrule only
4. Bold for best values
5. Arrow indicators in headers: PSNR ↑, LPIPS ↓
6. Consistent decimal places
7. Left align text, right align or center numbers
8. Use \pm for standard deviation: 23.4 \pm 1.2

### Multi Dataset Tables
Use \multicolumn and \cmidrule to group:
```
& \multicolumn{2}{c}{Dataset A} & \multicolumn{2}{c}{Dataset B} \\
\cmidrule(lr){2-3} \cmidrule(lr){4-5}
Method & Metric 1 & Metric 2 & Metric 1 & Metric 2 \\
```

### Ablation Table Structure
```
\toprule
Configuration & Metric A ↑ & Metric B ↓ & Delta \\
\midrule
Full model (ours) & 25.7 & 0.118 & - \\
- Module X & 24.1 & 0.135 & -1.6 \\
- Module Y & 24.9 & 0.125 & -0.8 \\
- Both X and Y & 23.2 & 0.152 & -2.5 \\
\bottomrule
```

## Caption Writing

### Figure Captions
Structure: **What to observe. Key conclusion.**
```
Figure 1: Comparison on [dataset]. Our method (c) recovers fine details
that [baseline] (b) loses, particularly in [specific region]. The improvement
is consistent across all [N] test cases (see supplement for full results).
```

### Table Captions
Structure: **Setting and protocol. Highlight key numbers.**
```
Table 2: Ablation study on [dataset]. Removing [module X] causes a [Y%]
drop in performance, confirming its importance for [specific function].
Best results in bold.
```

## Anti-Patterns Gallery  --  What NOT to Do

### Table Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Double rules (`\hline\hline`) | Creates a chunky, unprofessional look | Use `\toprule`, `\midrule`, `\bottomrule` |
| Vertical lines (`\|`) in tables | Distracts from the data; looks like Excel, not a publication | Remove all vertical lines |
| "±" without std dev explanation | "23.4 ± 1.2"  --  is that std dev? std error? CI? | Specify: "Mean ± Std Dev" in the caption |
| No metric direction | "PSNR"  --  higher is better, but does a reader unfamiliar with the metric know? | "PSNR ↑" |
| Unlabeled units | "Runtime: 120"  --  milliseconds? seconds? GPU-hours? | "Runtime (ms) ↓" |
| Inconsistent decimal places | One row shows "23.4", next shows "25.71", next "24" | Pick a precision, apply to all |
| Center-aligning text columns | Method names centered makes left-to-right scanning impossible | Left-align text columns, center numbers |
| Crowded table | 10+ columns on a single page | Split into sub-tables with clear captions |
| Heavy grid lines on every row | The reader sees lines, not data | Use subtle spacing. `\midrule` only between header and body. |

### Figure Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Rainbow colormap (jet) | Perceptually non-uniform, colorblind-unfriendly | Use viridis, cividis, magma, or ColorBrewer |
| Red-green pairs | 8% of males are red-green colorblind | Use blue-orange or a colorblind-safe palette |
| Title inside the figure | Duplicates the caption. Wastes space. | Remove the title. Let the caption do the work. |
| Unlabeled axes | "What am I looking at?" | Every axis must have a label with units |
| Illegible font size | Conference figures are printed small. 8pt text becomes invisible. | Minimum 9pt in figures. Test by printing at 50% scale. |
| JPEG for line art | Compression artifacts make text and lines blurry | PDF for vector, PNG at 300dpi for raster |
| Missing legend | Multiple series with no identification | Legend inside or beside plot, never covering data |
| 10+ series on one chart | Unreadable | Max 5-6 series. Group the rest as "Others" |
| Unlabeled colorbar | Heatmap shows values but no one knows what they mean | Colorbar with units: "PSNR (dB)" |
| 3D bar charts | Perspective distortion makes values impossible to compare accurately | 2D bars. Always. |

### Before/After Example  --  Table

```
BEFORE (anti-pattern):
┌──────────┬────────┬────────┬──────────┐
│ Method   │ PSNR   │ LPIPS  │ Runtime  │
├──────────┼────────┼────────┼──────────┤
│ Baseline │ 23.4   │ 0.145  │    120   │
├──────────┼────────┼────────┼──────────┤
│ Ours     │ 25.71  │ 0.118  │     72.3 │
└──────────┴────────┴────────┴──────────┘
Vertical lines, double rules, inconsistent decimals, no units, no metric direction.

AFTER (correct):
\toprule
Method & PSNR ↑ (dB) & LPIPS ↓ & Runtime ↓ (ms) \\
\midrule
Baseline & 23.40 & 0.145 & 120.0 \\
\textbf{Ours} & \textbf{25.71} & \textbf{0.118} & \textbf{72.3} \\
\bottomrule
Booktabs, bold best, arrow indicators, units, consistent decimals.
```

---

## Quality Checklist

### Every Figure
- [ ] Clear message understandable without caption?
- [ ] Colorblind safe palette?
- [ ] Axis labels with units?
- [ ] Font size >= body text?
- [ ] No title inside figure?
- [ ] Vector format for diagrams?

### Every Table
- [ ] Caption above?
- [ ] Booktabs style (toprule/midrule/bottomrule)?
- [ ] No vertical lines?
- [ ] Metric direction labeled?
- [ ] Best values highlighted?
- [ ] Consistent decimal places?
- [ ] One message per table?
