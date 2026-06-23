#!/usr/bin/env python3
"""Generate publication-ready PDF from Markdown.

Primary: weasyprint (best typography, requires GTK3 on Windows).
Fallback: fpdf2 (pure Python, works everywhere).

Usage:
    python generate_pdf.py input.md output.pdf
    python generate_pdf.py input.md output.pdf --template two-column|single-column
    python generate_pdf.py input.md output.pdf --preview    open PDF after generation
    python generate_pdf.py --help
"""

import sys
import re
import os
import tempfile
import argparse
import subprocess
from pathlib import Path

# ── Dependency checks ─────────────────────────────────────────

def _can_import(mod):
    try:
        __import__(mod)
        return True
    except (ImportError, OSError):
        return False

HAS_MARKDOWN = _can_import("markdown")
HAS_FPDF2 = _can_import("fpdf")
HAS_WEASYPRINT = False
try:
    from weasyprint import HTML
    HAS_WEASYPRINT = True
except (ImportError, OSError):
    pass


# ═══════════════════════════════════════════════════════════════
# PATH 1: weasyprint (best quality, HTML+CSS → PDF)
# ═══════════════════════════════════════════════════════════════

CSS = """
@page {
    size: A4;
    margin: 2.4cm 2.2cm 2.4cm 2.2cm;
    @bottom-center { content: counter(page); font-family: 'Times New Roman', 'STIX Two Text', serif; font-size: 8.5pt; color: #555; }
}
@page:first { @bottom-center { content: none; } }

body {
    font-family: 'Times New Roman', 'STIX Two Text', 'DejaVu Serif', Georgia, serif;
    font-size: 10pt; line-height: 1.45; color: #1a1a1a;
    text-align: justify; hyphens: auto; widows: 2; orphans: 2;
}

/* ── Typography Hierarchy (3 sizes only: 16pt / 12pt / 10pt) ── */
h1 {
    font-size: 16pt; font-weight: bold; text-align: center;
    margin-top: 0; margin-bottom: 0.5cm; column-span: all;
    page-break-before: avoid; page-break-after: avoid;
}
h2 {
    font-size: 12pt; font-weight: bold;
    margin-top: 0.7cm; margin-bottom: 0.25cm;
    page-break-after: avoid;
}
h3 {
    font-size: 10pt; font-weight: bold; font-style: italic;
    margin-top: 0.45cm; margin-bottom: 0.15cm;
    page-break-after: avoid;
}
h4 {
    font-size: 10pt; font-style: italic;
    margin-top: 0.3cm; margin-bottom: 0.1cm;
    page-break-after: avoid;
}

/* ── Body text ── */
p {
    margin: 0.15cm 0; text-indent: 0.45cm;
    text-align: justify;
}
p:first-of-type, h2 + p, h3 + p, h4 + p, blockquote + p, hr + p {
    text-indent: 0;
}
strong { font-weight: bold; }
em { font-style: italic; }

/* ── Layout helpers ── */
.two-column { column-count: 2; column-gap: 0.8cm; column-fill: balance; }
.authors { text-align: center; font-size: 10pt; margin-bottom: 0.15cm; column-span: all; }
.affiliations { text-align: center; font-size: 8.5pt; color: #555; margin-bottom: 0.5cm; column-span: all; }
.abstract {
    font-size: 9pt; line-height: 1.4;
    margin: 0.5cm 0; padding: 0.35cm 0;
    border-top: 1.5px solid #333; border-bottom: 1.5px solid #333;
    column-span: all;
}
.abstract strong:first-child { font-size: 10pt; }

/* ── Tables: booktabs style (horizontal rules only) ── */
table {
    border-collapse: collapse; margin: 0.35cm 0; font-size: 9pt;
    width: 100%; break-inside: avoid;
}
caption {
    font-weight: bold; margin-bottom: 0.12cm; text-align: left;
    font-size: 8.5pt; font-style: italic;
}
thead { border-top: 2px solid #333; border-bottom: 1px solid #666; }
tbody tr:last-child { border-bottom: 2px solid #333; }
th, td { padding: 2.5px 6px; text-align: center; font-size: 9pt; }
th { font-weight: bold; }
td:first-child, th:first-child { text-align: left; }

/* ── Figures ── */
figure { margin: 0.45cm 0; text-align: center; break-inside: avoid; }
figure img { max-width: 100%; }
figcaption {
    font-size: 8.5pt; font-style: italic; text-align: left;
    margin-top: 0.1cm; color: #444;
}

/* ── Code ── */
pre, code { font-family: 'Consolas', 'Courier New', 'DejaVu Sans Mono', monospace; font-size: 8pt; background: #f7f7f7; border-radius: 2px; }
pre { padding: 0.25cm; break-inside: avoid; line-height: 1.3; }
code { padding: 1px 3px; }
pre code { padding: 0; background: none; }

/* ── Blockquotes ── */
blockquote { margin: 0.3cm 0; padding: 0.1cm 0.6cm; border-left: 3px solid #bbb; font-style: italic; color: #444; }

/* ── Lists ── */
ol, ul { margin: 0.15cm 0; padding-left: 1.3em; }
li { margin-bottom: 0.06cm; }

/* ── References ── */
.references { font-size: 8.5pt; line-height: 1.4; }
.references ol { padding-left: 1.5em; }
.references li { margin-bottom: 0.1cm; }

/* ── Misc ── */
sup { font-size: 7.5pt; }
a { color: #2a5db0; }
hr { border: none; border-top: 0.5px solid #ccc; margin: 0.5cm 0; }
"""


def _render_weasyprint(md_text, output_path, template):
    import markdown
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "footnotes", "codehilite", "toc", "sane_lists"],
    )
    body_class = "two-column" if template == "two-column" else "single-column"
    full_html = f"<!DOCTYPE html><html lang=en><head><meta charset=UTF-8><style>{CSS}</style></head><body class={body_class}>{html_body}</body></html>"
    HTML(string=full_html).write_pdf(output_path)


# ═══════════════════════════════════════════════════════════════
# PATH 2: fpdf2 (pure Python, zero system deps)
# ═══════════════════════════════════════════════════════════════

def _strip_inline(text):
    """Strip inline markdown formatting only, preserving content."""
    t = text
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)          # bold
    t = re.sub(r'\*(.+?)\*', r'\1', t)               # italic
    t = re.sub(r'`([^`]+)`', r'\1', t)               # inline code
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)   # links
    t = re.sub(r'!\[.*?\]\([^)]+\)', '', t)           # images
    t = re.sub(r'<!--.*?-->', '', t, flags=re.DOTALL) # HTML comments
    return t


def _parse_markdown_blocks(md_text):
    """Parse markdown into typed blocks: heading, paragraph, table, code, hr, list."""
    lines = md_text.split('\n')
    blocks = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Code blocks (fenced)
        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            blocks.append(('code', '\n'.join(code_lines), lang))
            continue

        # HTML comments (standalone)
        if line.strip().startswith('<!--') and line.strip().endswith('-->'):
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^[-\*_]{3,}\s*$', line.strip()):
            blocks.append(('hr', None, None))
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,4})\s+(.+)', line)
        if m:
            blocks.append(('heading', _strip_inline(m.group(2)), len(m.group(1))))
            i += 1
            continue

        # Tables
        if '|' in line and line.strip().startswith('|'):
            table_rows = []
            while i < len(lines) and '|' in lines[i] and lines[i].strip().startswith('|'):
                row = lines[i]
                cells = [_strip_inline(c.strip()) for c in row.split('|')[1:-1]]
                # Skip separator rows like |---|---|
                if not all(re.match(r'^[:\- ]+$', c) for c in cells):
                    table_rows.append(cells)
                i += 1
            if table_rows:
                has_header = len(table_rows) > 1
                blocks.append(('table', table_rows, has_header))
            continue

        # Blank line
        if not line.strip():
            i += 1
            continue

        # List item
        list_match = re.match(r'^(\s*)[-*+]\s+(.+)', line)
        if list_match:
            list_items = []
            while i < len(lines):
                lm = re.match(r'^(\s*)[-*+]\s+(.+)', lines[i])
                if not lm:
                    break
                list_items.append(_strip_inline(lm.group(2)))
                i += 1
            blocks.append(('list', list_items, None))
            continue

        # Numbered list
        num_match = re.match(r'^(\s*)\d+\.\s+(.+)', line)
        if num_match:
            list_items = []
            while i < len(lines):
                nm = re.match(r'^(\s*)\d+\.\s+(.+)', lines[i])
                if not nm:
                    break
                list_items.append(_strip_inline(nm.group(2)))
                i += 1
            blocks.append(('ordered_list', list_items, None))
            continue

        # Paragraph: collect lines until blank line or next block marker
        para_lines = [_strip_inline(line)]
        i += 1
        while i < len(lines):
            nl = lines[i]
            if not nl.strip():
                break
            if nl.strip().startswith('```') or nl.strip().startswith('<!--'):
                break
            if re.match(r'^(#{1,4})\s', nl):
                break
            if re.match(r'^[-\*_]{3,}\s*$', nl.strip()):
                break
            if '|' in nl and nl.strip().startswith('|'):
                break
            if re.match(r'^(\s*)[-*+]\s+', nl) or re.match(r'^(\s*)\d+\.\s+', nl):
                break
            para_lines.append(_strip_inline(nl))
            i += 1

        text = ' '.join(p.strip() for p in para_lines if p.strip())
        if text:
            blocks.append(('paragraph', text, None))
        continue

    return blocks


def _register_unicode_font(pdf):
    """Register a Unicode-capable TTF font for fpdf2. Falls back to built-in if unavailable."""
    # Try common Unicode font paths
    candidates = [
        r'C:\Windows\Fonts\DejaVuSans.ttf',
        r'C:\Windows\Fonts\DejaVuSerif.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/System/Library/Fonts/Times.ttc',
    ]
    regular = bold = italic = bold_italic = None
    for c in candidates:
        p = Path(c)
        if p.exists():
            regular = str(p)
            # Try companion files
            d = p.parent
            n = p.stem
            for variant, suffix, style in [
                ('Bold', '-Bold', 'B'),
                ('Oblique', '-Oblique', 'I'),
                ('BoldOblique', '-BoldOblique', 'BI'),
            ]:
                vpath = d / f'{n}{suffix}{p.suffix}'
                if vpath.exists():
                    if style == 'B': bold = str(vpath)
                    elif style == 'I': italic = str(vpath)
                    elif style == 'BI': bold_italic = str(vpath)
            break

    if regular:
        pdf.add_font('Unicode', '', regular)
        if bold: pdf.add_font('Unicode', 'B', bold)
        if italic: pdf.add_font('Unicode', 'I', italic)
        if bold_italic: pdf.add_font('Unicode', 'BI', bold_italic)
        return 'Unicode'
    return None  # Fallback to built-in Times (latin-1 only)


def _clean_markdown_for_pdf(md_text):
    """Remove dashes and problematic Unicode chars before PDF rendering."""
    import subprocess
    import tempfile
    # Write to temp file, clean, read back
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_text)
        tmp_in = f.name
    tmp_out = tmp_in.replace('.md', '_clean.md')
    clean_script = Path(__file__).resolve().parent / 'clean_dashes.py'
    try:
        subprocess.run([sys.executable, str(clean_script), tmp_in], check=True, capture_output=True)
        with open(tmp_in, 'r', encoding='utf-8') as f:
            cleaned = f.read()
    except Exception:
        cleaned = md_text  # if cleaning fails, use original
    finally:
        for p in [tmp_in, tmp_out]:
            try: os.unlink(p)
            except OSError: pass
    return cleaned


def _render_fpdf2(md_text, output_path):
    from fpdf import FPDF

    # Auto-clean dashes and problematic Unicode before rendering
    md_text = _clean_markdown_for_pdf(md_text)

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(True, 22)
    pdf.set_margins(22, 22, 22)
    pdf.add_page()

    # Try Unicode font first, fall back to Times
    font_name = _register_unicode_font(pdf) or 'Times'
    page_w = pdf.w - pdf.l_margin - pdf.r_margin  # usable width
    blocks = _parse_markdown_blocks(md_text)

    for block_type, content, meta in blocks:

        if block_type == 'heading':
            if meta == 1:
                pdf.ln(4)
                pdf.set_font(font_name, 'B', 18)
                pdf.multi_cell(page_w, 8, content, align='C')
                pdf.ln(3)
            elif meta == 2:
                pdf.ln(3)
                pdf.set_font(font_name, 'B', 13)
                pdf.multi_cell(page_w, 6, content, align='L')
                pdf.ln(2)
            elif meta == 3:
                pdf.ln(2)
                pdf.set_font(font_name, 'BI', 11)
                pdf.multi_cell(page_w, 5.5, content, align='L')
                pdf.ln(1)
            else:
                pdf.ln(1)
                pdf.set_font(font_name, 'I', 10)
                pdf.multi_cell(page_w, 5, content, align='L')
                pdf.ln(1)

        elif block_type == 'paragraph':
            pdf.set_font(font_name, '', 10)
            pdf.multi_cell(page_w, 5, content, align='J')
            pdf.ln(2)

        elif block_type == 'table':
            rows = content
            has_header = meta
            ncols = max(len(r) for r in rows) if rows else 1

            # Calculate column widths based on content
            col_widths = [page_w / ncols] * ncols
            for r in rows:
                for ci in range(min(len(r), ncols)):
                    # Estimate: ~2mm per character for 10pt font
                    est_w = min(len(r[ci]) * 1.8 + 4, page_w * 0.45)
                    if est_w > col_widths[ci]:
                        col_widths[ci] = est_w
            # Normalize to fit page width
            total = sum(col_widths)
            if total > page_w:
                col_widths = [w * page_w / total for w in col_widths]

            pdf.set_font(font_name, 'B', 8)
            line_h = 5.5

            # Header
            if has_header:
                pdf.set_draw_color(50, 50, 50)
                y0 = pdf.get_y()
                pdf.line(pdf.l_margin, y0, pdf.w - pdf.r_margin, y0)

                for ci in range(min(len(rows[0]), ncols)):
                    w = col_widths[ci] if ci < ncols - 1 else page_w - sum(col_widths[:ci])
                    pdf.cell(w, line_h, rows[0][ci][:50], border=0, align='C' if ci > 0 else 'L')
                pdf.ln()
                y1 = pdf.get_y()
                pdf.line(pdf.l_margin, y1, pdf.w - pdf.r_margin, y1)
                rows = rows[1:]

            # Body
            for ri, row in enumerate(rows):
                if pdf.get_y() + line_h > pdf.h - pdf.b_margin:
                    pdf.add_page()
                pdf.set_font(font_name, '', 8)
                for ci in range(min(len(row), ncols)):
                    w = col_widths[ci] if ci < ncols - 1 else page_w - sum(col_widths[:ci])
                    cell_text = row[ci][:60]
                    align = 'C' if ci > 0 else 'L'
                    pdf.cell(w, line_h, cell_text, border=0, align=align)
                pdf.ln()

            # Footer line
            pdf.set_draw_color(50, 50, 50)
            yf = pdf.get_y()
            pdf.line(pdf.l_margin, yf, pdf.w - pdf.r_margin, yf)
            pdf.ln(3)

        elif block_type == 'code':
            pdf.set_font('Courier', '', 7.5)
            pdf.set_fill_color(245, 245, 245)
            for cl in content.split('\n'):
                if pdf.get_y() + 4 > pdf.h - pdf.b_margin:
                    pdf.add_page()
                pdf.cell(page_w, 4, cl[:110], fill=True, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(3)

        elif block_type == 'hr':
            pdf.ln(2)
            pdf.set_draw_color(180, 180, 180)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(2)

        elif block_type == 'list':
            pdf.set_font(font_name, '', 10)
            for item in content:
                bullet = '\x95'
                pdf.cell(6, 5, bullet, align='R')
                pdf.multi_cell(page_w - 6, 5, item, align='J')
                pdf.ln(0.5)
            pdf.ln(1)

        elif block_type == 'ordered_list':
            pdf.set_font(font_name, '', 10)
            for idx, item in enumerate(content, 1):
                num = f'{idx}.'
                pdf.cell(8, 5, num, align='R')
                pdf.multi_cell(page_w - 8, 5, item, align='J')
                pdf.ln(0.5)
            pdf.ln(1)

    # Page numbers
    total_pages = pdf.page_no()
    for pg in range(1, total_pages + 1):
        pdf.page = pg
        pdf.set_font(font_name, '', 8)
        pdf.set_y(pdf.h - 14)
        pdf.cell(page_w, 4, str(pg), align='C')

    pdf.output(output_path)


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def _open_file(path):
    """Open file with default system viewer."""
    try:
        if sys.platform == 'win32':
            os.startfile(str(path))
        elif sys.platform == 'darwin':
            subprocess.run(['open', str(path)], check=False)
        else:
            subprocess.run(['xdg-open', str(path)], check=False)
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', action='store_true')
    parser.add_argument('input', nargs='?')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--template', choices=['two-column', 'single-column'], default='two-column')
    parser.add_argument('--preview', action='store_true', help='Open PDF after generation')

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    if args.help or not args.input:
        parser.print_help()
        print("\nExamples:")
        print("  python generate_pdf.py paper.md paper.pdf")
        print("  python generate_pdf.py paper.md paper.pdf --template single-column")
        print("  python generate_pdf.py paper.md paper.pdf --preview")
        return 0

    inp = Path(args.input)
    if not inp.exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        return 1

    if not inp.suffix.lower() in ('.md', '.markdown', '.txt'):
        print(f"Warning: {args.input} is not .md — attempting anyway", file=sys.stderr)

    try:
        md_text = inp.read_text(encoding='utf-8')
    except UnicodeDecodeError as e:
        print(f"Error: not valid UTF-8: {e}", file=sys.stderr)
        return 1

    if not md_text.strip():
        print(f"Error: {args.input} is empty", file=sys.stderr)
        return 1

    out = args.output or str(inp.with_suffix('.pdf'))

    # Pre-flight: check markdown module (needed by both paths)
    if not HAS_MARKDOWN:
        print("Error: 'markdown' package not installed. Run: pip install markdown", file=sys.stderr)
        return 1

    # Path 1: weasyprint
    if HAS_WEASYPRINT:
        _render_weasyprint(md_text, out, args.template)
        size_kb = Path(out).stat().st_size / 1024
        print(f"PDF (weasyprint): {out} ({size_kb:.0f} KB, {args.template})")
        if args.preview:
            _open_file(out)
        return 0

    # Path 2: fpdf2
    if HAS_FPDF2:
        _render_fpdf2(md_text, out)
        size_kb = Path(out).stat().st_size / 1024
        print(f"PDF (fpdf2): {out} ({size_kb:.0f} KB)")
        print("  Note: weasyprint not available (needs GTK3). Install GTK3 for best typography:")
        print("  https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows")
        if args.preview:
            _open_file(out)
        return 0

    print("Error: no PDF engine. Install: pip install fpdf2", file=sys.stderr)
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
