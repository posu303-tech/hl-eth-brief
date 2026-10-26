#!/usr/bin/env python3
"""Builds the static site from output/latest.md + output/latest.json.

No framework, no CDN: one inline stylesheet, responsive by default, readable on
a phone. `site/` is generated output and is git-ignored; CI uploads it as the
Pages artifact.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import mdmini

ROOT = Path(__file__).resolve().parent

CSS = """
:root { color-scheme: light dark; }
* { box-sizing: border-box; }
body {
  margin: 0 auto; padding: 20px 16px 48px; max-width: 760px;
  font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #1c1c1e; background: #fbfbfd;
}
@media (prefers-color-scheme: dark) {
  body { color: #e5e5ea; background: #131316; }
  .banner { background: #1d1d21 !important; border-color: #2c2c31 !important; }
  table th { border-bottom-color: #3a3a3f !important; }
  table td { border-bottom-color: #2a2a2e !important; }
  a { color: #6fb3ff; }
}
h1 { font-size: 1.45rem; line-height: 1.25; margin: 8px 0 4px; }
h2 { font-size: 1.05rem; margin: 28px 0 8px; letter-spacing: .01em; }
p { margin: 6px 0; }
ul { margin: 6px 0; padding-left: 20px; }
li { margin: 3px 0; }
table { width: 100%; border-collapse: collapse; margin: 10px 0 4px; font-size: .92rem; }
th { text-align: left; font-weight: 600; padding: 6px 8px; border-bottom: 1.5px solid #d5d5da; }
td { padding: 6px 8px; border-bottom: 1px solid #e6e6ea; vertical-align: top; }
.banner {
  display: flex; flex-wrap: wrap; gap: 6px 14px; align-items: center;
  background: #fff; border: 1px solid #e3e3e8; border-radius: 10px;
  padding: 12px 14px; margin-bottom: 14px; font-size: .9rem;
}
.badge { padding: 2px 9px; border-radius: 999px; font-weight: 600; font-size: .78rem; letter-spacing: .04em; }
.bull { background: #e3f6e8; color: #13703a; }
.bear { background: #fde8e8; color: #a11d1d; }
.flat { background: #ececf0; color: #444; }
nav { display: flex; gap: 14px; font-size: .85rem; margin-bottom: 18px; color: #6a6a72; }
nav a { text-decoration: none; }
footer { margin-top: 36px; font-size: .78rem; color: #7a7a82; }
@media (max-width: 560px) {
  body { padding: 14px 12px 40px; font-size: 15px; }
  h1 { font-size: 1.2rem; }
  table { font-size: .82rem; }
  th, td { padding: 5px 6px; }
}
"""


def _page(title: str, body: str, *, prefix: str = "", nav: bool = True) -> str:
    links = (
        f'<nav><a href="{prefix}index.html">Latest</a>'
        f'<a href="{prefix}archive.html">Archive</a></nav>'
        if nav
        else ""
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{mdmini.inline(title)}</title>
<style>{CSS}</style>
</head>
<body>
{links}
{body}
<footer>Keyless Hyperliquid data. Conditional levels, no price forecast. Not financial advice.</footer>
</body>
</html>
"""


def _offset_label(minutes: int) -> str:
    if minutes == 0:
        return "UTC"
    sign = "+" if minutes >= 0 else "-"
    total = abs(minutes)
    return f"UTC{sign}{total // 60:02d}:{total % 60:02d}"


def banner(levels: dict) -> str:
    offset = int(levels.get("display_offset_minutes") or 0)
    stamp = datetime.fromtimestamp(int(levels["as_of"]) / 1000, tz=timezone.utc) + timedelta(minutes=offset)
    bias = levels["bias"]
    tone = {"Bullish": "bull", "Bearish": "bear"}.get(bias["label"], "flat")
    return (
        '<div class="banner">'
        f'<strong>{mdmini.inline(levels["symbol"])}</strong>'
        f'<span>spot {levels["spot"]:,.2f}</span>'
        f'<span class="badge {tone}">{bias["label"].upper()} {bias["score"]:+d}</span>'
        f'<span>{mdmini.inline(levels["regime"]["label"])}</span>'
        f'<span>price {levels["regime"]["value_label"]} value</span>'
        f'<span>{stamp:%Y-%m-%d %H:%M} {_offset_label(offset)}</span>'
        "</div>"
    )


def build(output_dir: Path, site_dir: Path, *, base_path: str = "/hl-eth-brief/") -> dict:
    latest_md = (output_dir / "latest.md").read_text(encoding="utf-8")
    levels = json.loads((output_dir / "latest.json").read_text(encoding="utf-8"))

    site_dir.mkdir(parents=True, exist_ok=True)
    (site_dir / "briefs").mkdir(exist_ok=True)
    shutil.copyfile(output_dir / "latest.json", site_dir / "levels.json")

    title = f"{levels['symbol']} brief - {levels['day']}"
    (site_dir / "index.html").write_text(
        _page(title, banner(levels) + mdmini.to_html(latest_md)), encoding="utf-8"
    )

    archive_files = sorted((output_dir / "archive").glob("*.md"), reverse=True)
    for path in archive_files:
        text = path.read_text(encoding="utf-8")
        (site_dir / "briefs" / f"{path.stem}.html").write_text(
            _page(f"{levels['symbol']} brief - {path.stem}", mdmini.to_html(text), prefix="../"),
            encoding="utf-8",
        )

    def entries(prefix: str) -> str:
        return "".join(
            f'<li><a href="{prefix}{path.stem}.html">{path.stem}</a></li>' for path in archive_files
        )

    if archive_files:
        intro = "<p>One brief per UTC day, the last run before the close.</p>"
        root_body = f"<h1>Archive</h1>{intro}<ul>{entries('briefs/')}</ul>"
        briefs_body = f"<h1>Archive</h1>{intro}<ul>{entries('./')}</ul>"
    else:
        root_body = briefs_body = "<h1>Archive</h1><p>No archived briefs yet.</p>"

    (site_dir / "archive.html").write_text(_page("Archive", root_body), encoding="utf-8")

    # /briefs/index.html exists so that guessing the folder URL is not a 404.
    (site_dir / "briefs" / "index.html").write_text(
        _page("Archive", briefs_body, prefix="../"), encoding="utf-8"
    )

    (site_dir / "404.html").write_text(
        _page(
            "Not found",
            "<h1>Not found</h1>"
            "<p>That page does not exist.</p>"
            f'<p><a href="{base_path}">Latest brief</a> &middot; '
            f'<a href="{base_path}archive.html">Archive</a></p>',
            nav=False,
        ),
        encoding="utf-8",
    )

    # Pages needs a .nojekyll to serve paths verbatim and skip Jekyll processing.
    (site_dir / ".nojekyll").write_text("", encoding="utf-8")
    return {"pages": 3 + len(archive_files), "archived": len(archive_files)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the static brief site.")
    parser.add_argument("--output", default=str(ROOT / "output"))
    parser.add_argument("--site", default=str(ROOT / "site"))
    parser.add_argument(
        "--base-path",
        default="/hl-eth-brief/",
        help="public URL prefix, used only by the 404 page links",
    )
    args = parser.parse_args(argv)

    output_dir = Path(args.output)
    if not (output_dir / "latest.md").exists():
        print(f"missing {output_dir / 'latest.md'}; run eth_brief.py first", file=sys.stderr)
        return 2

    stats = build(output_dir, Path(args.site), base_path=args.base_path)
    print(f"site built: {stats['pages']} pages, {stats['archived']} archived")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
