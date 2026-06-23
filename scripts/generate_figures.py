#!/usr/bin/env python3
"""Generate publication-ready figures for academic papers.

Colorblind-friendly palette (ColorBrewer Set2). 300 DPI vector-ready output.
Requires: matplotlib

Usage:
    python generate_figures.py bar --data results.json --output bar_chart.pdf
    python generate_figures.py line --data metrics.json --output line_plot.pdf
    python generate_figures.py heatmap --data matrix.json --output heatmap.pdf
    python generate_figures.py ablation --data ablation.json --output ablation.pdf
    python generate_figures.py --help

JSON data formats:
  bar:      {"labels": [...], "values": [...], "highlight_idx": int}
  line:     {"x": [...], "series": [{"label": str, "values": [...]}]}
  heatmap:  {"labels_x": [...], "labels_y": [...], "matrix": [[...]]}
  ablation: {"labels": [...], "values": [...], "metric": str}
"""

import sys
import json
import csv
import argparse
from pathlib import Path

# Pre-flight matplotlib check
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
except ImportError:
    print("Error: matplotlib not installed. Run: pip install matplotlib", file=sys.stderr)
    sys.exit(1)

# Colorblind-friendly palette (ColorBrewer Set2 + custom)
COLORS = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666"]

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "STIX Two Text"],
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})


def load_data(path):
    p = Path(path)
    if not p.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)

    ext = p.suffix.lower()
    try:
        if ext == ".json":
            return json.loads(p.read_text(encoding="utf-8"))
        elif ext == ".csv":
            with open(p, encoding="utf-8") as f:
                return list(csv.DictReader(f))
        else:
            print(f"Error: unsupported data format: {ext}. Use .json or .csv", file=sys.stderr)
            sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Error: cannot read {path}: {e}", file=sys.stderr)
        sys.exit(1)


def _ensure_output_dir(path):
    p = Path(path)
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error: cannot create output directory: {e}", file=sys.stderr)
        sys.exit(1)


def bar_chart(data, output, title=None, xlabel=None, ylabel=None):
    labels = data.get("labels", [])
    values = data.get("values", [])
    highlight = data.get("highlight_idx", -1)

    if not labels or not values:
        print("Error: bar chart requires 'labels' and 'values' in data", file=sys.stderr)
        sys.exit(1)
    if len(labels) != len(values):
        print(f"Error: labels ({len(labels)}) and values ({len(values)}) must have same length", file=sys.stderr)
        sys.exit(1)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    colors = [COLORS[1] if i == highlight else COLORS[0] for i in range(len(values))]
    bars = ax.bar(range(len(labels)), values, color=colors, width=0.6, edgecolor="white", linewidth=0.5)

    max_val = max(values) if values else 1
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max_val * 0.01,
                str(val), ha="center", va="bottom", fontsize=9)

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=25, ha="right")
    ax.set_ylabel(ylabel or "")
    ax.set_title(title or "")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_major_locator(ticker.MaxNLocator(6))

    _ensure_output_dir(output)
    fig.tight_layout()
    fig.savefig(output)
    plt.close(fig)
    size_kb = Path(output).stat().st_size / 1024
    print(f"Bar chart saved: {output} ({size_kb:.0f} KB)")


def line_plot(data, output, title=None, xlabel=None, ylabel=None):
    series_list = data.get("series", [])
    if not series_list:
        print("Error: line plot requires 'series' in data", file=sys.stderr)
        sys.exit(1)

    x = data.get("x", list(range(len(series_list[0].get("values", [])))))

    fig, ax = plt.subplots(figsize=(6, 3.5))
    for i, series in enumerate(series_list):
        color = COLORS[1] if i == 0 else COLORS[i % len(COLORS)]
        ax.plot(x, series.get("values", []), label=series.get("label", f"Series {i}"),
                color=color, linewidth=1.5, marker="o", markersize=4)

    ax.set_xlabel(xlabel or "")
    ax.set_ylabel(ylabel or "")
    ax.set_title(title or "")
    ax.legend(frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    _ensure_output_dir(output)
    fig.tight_layout()
    fig.savefig(output)
    plt.close(fig)
    size_kb = Path(output).stat().st_size / 1024
    print(f"Line plot saved: {output} ({size_kb:.0f} KB)")


def heatmap(data, output, title=None):
    matrix = data.get("matrix", [[]])
    labels_x = data.get("labels_x", [])
    labels_y = data.get("labels_y", [])

    if not matrix or not matrix[0]:
        print("Error: heatmap requires a non-empty 'matrix' in data", file=sys.stderr)
        sys.exit(1)

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(matrix, cmap="YlOrRd", aspect="auto")

    ax.set_xticks(range(len(labels_x)))
    ax.set_yticks(range(len(labels_y)))
    ax.set_xticklabels(labels_x, rotation=45, ha="right")
    ax.set_yticklabels(labels_y)

    max_val = max(max(r) for r in matrix) if matrix else 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text_color = "white" if matrix[i][j] > 0.7 * max_val else "black"
            ax.text(j, i, str(matrix[i][j]), ha="center", va="center", fontsize=9, color=text_color)

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    ax.set_title(title or "")
    _ensure_output_dir(output)
    fig.tight_layout()
    fig.savefig(output)
    plt.close(fig)
    size_kb = Path(output).stat().st_size / 1024
    print(f"Heatmap saved: {output} ({size_kb:.0f} KB)")


def ablation_chart(data, output, title=None):
    labels = data.get("labels", [])
    values = data.get("values", [])
    metric = data.get("metric", "")

    if not labels or not values:
        print("Error: ablation chart requires 'labels' and 'values' in data", file=sys.stderr)
        sys.exit(1)

    fig, ax = plt.subplots(figsize=(6, 3))
    colors = [COLORS[1] if i == 0 else "#cccccc" for i in range(len(values))]
    bars = ax.barh(range(len(labels)), values, color=colors, height=0.5)

    max_val = max(values) if values else 1
    for bar, val in zip(bars, values):
        delta = val - values[0] if values else 0
        delta_str = f" ({delta:+.1f})" if delta != 0 else ""
        ax.text(bar.get_width() + max_val * 0.01, bar.get_y() + bar.get_height() / 2,
                f"{val}{delta_str}", va="center", fontsize=9)

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel(metric)
    ax.set_title(title or "Ablation Study")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    _ensure_output_dir(output)
    fig.tight_layout()
    fig.savefig(output)
    plt.close(fig)
    size_kb = Path(output).stat().st_size / 1024
    print(f"Ablation chart saved: {output} ({size_kb:.0f} KB)")


COMMANDS = {
    "bar": bar_chart,
    "line": line_plot,
    "heatmap": heatmap,
    "ablation": ablation_chart,
}


def main():
    parser = argparse.ArgumentParser(
        description="Generate publication-ready figures for academic papers",
        add_help=False,
    )
    parser.add_argument("--help", action="store_true", help="Show this help")
    parser.add_argument("command", nargs="?", choices=list(COMMANDS.keys()),
                        help=f"Chart type: {', '.join(COMMANDS.keys())}")
    parser.add_argument("--data", type=str, help="JSON or CSV data file")
    parser.add_argument("--output", type=str, help="Output file (.pdf, .png, .svg)")
    parser.add_argument("--title", type=str, help="Chart title")

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    if args.help or not args.command:
        parser.print_help()
        print(f"\nChart types: {', '.join(COMMANDS.keys())}")
        print("\nJSON data formats:")
        print("  bar:      {\"labels\": [...], \"values\": [...], \"highlight_idx\": int}")
        print("  line:     {\"x\": [...], \"series\": [{\"label\": str, \"values\": [...]}]}")
        print("  heatmap:  {\"labels_x\": [...], \"labels_y\": [...], \"matrix\": [[...]]}")
        print("  ablation: {\"labels\": [...], \"values\": [...], \"metric\": str}")
        print("\nExample:")
        print("  python generate_figures.py bar --data results.json --output figure1.pdf --title \"Results\"")
        return 0

    if not args.data:
        print("Error: --data is required", file=sys.stderr)
        return 1
    if not args.output:
        print("Error: --output is required", file=sys.stderr)
        return 1

    data = load_data(args.data)
    func = COMMANDS[args.command]
    try:
        func(data, args.output, title=args.title)
    except Exception as e:
        print(f"Error generating figure: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
