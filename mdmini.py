"""A deliberately small Markdown -> HTML converter for this project's own output.

The brief renders from a fixed grammar (h1/h2, pipe tables, dash bullets, bold,
italic), so a full Markdown library would be a dependency for no benefit.
Anything outside that grammar passes through as a paragraph.
"""

from __future__ import annotations

import html
import re

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<!_)_([^_]+)_(?!_)")


def inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = _BOLD.sub(r"<strong>\1</strong>", escaped)
    escaped = _ITALIC.sub(r"<em>\1</em>", escaped)
    return escaped


def _cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.strip().strip("|").split("|")]


def _is_separator(row: str) -> bool:
    cells = _cells(row)
    return bool(cells) and all(cell and set(cell) <= set("-: ") for cell in cells)


def table(rows: list[str]) -> str:
    header = _cells(rows[0])
    body = rows[1:]
    if body and _is_separator(body[0]):
        body = body[1:]
    head = "".join(f"<th>{inline(cell)}</th>" for cell in header)
    out = ["<table>", f"<thead><tr>{head}</tr></thead>", "<tbody>"]
    for row in body:
        cells = _cells(row)
        if len(cells) < len(header):
            cells += [""] * (len(header) - len(cells))
        out.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]

        if line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("|"):
            block = []
            while index < len(lines) and lines[index].startswith("|"):
                block.append(lines[index])
                index += 1
            out.append(table(block))
            continue
        elif line.startswith("- "):
            items = []
            while index < len(lines) and lines[index].startswith("- "):
                items.append(f"<li>{inline(lines[index][2:])}</li>")
                index += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif line.strip():
            out.append(f"<p>{inline(line)}</p>")
        index += 1
    return "\n".join(out)
