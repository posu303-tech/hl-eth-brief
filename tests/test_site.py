"""Site tests: the mini renderer, and a real build from the recorded payload."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import brief
import levels as lv
import make_site
import mdmini
from fixtures_helper import available, build_book_from_fixtures


class MarkdownTests(unittest.TestCase):
    SAMPLE = "\n".join(
        [
            "# Title",
            "",
            "## 1) Section",
            "",
            "| a | b |",
            "|---|---|",
            "| 1 | 2 |",
            "",
            "- first **bold** bullet",
            "- second bullet",
            "",
            "_footer note_",
        ]
    )

    def test_block_structure(self):
        html = mdmini.to_html(self.SAMPLE)
        self.assertIn("<h1>Title</h1>", html)
        self.assertIn("<h2>1) Section</h2>", html)
        self.assertIn("<table>", html)
        self.assertIn("<thead><tr><th>a</th><th>b</th></tr></thead>", html)
        self.assertIn("<td>1</td><td>2</td>", html)
        self.assertIn("<ul><li>first <strong>bold</strong> bullet</li>", html)
        self.assertIn("<em>footer note</em>", html)

    def test_separator_row_is_not_a_body_row(self):
        html = mdmini.to_html(self.SAMPLE)
        self.assertNotIn("<td>---</td>", html)

    def test_html_is_escaped(self):
        html = mdmini.to_html("<script>alert(1)</script> and a & b")
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertIn("&amp;", html)

    def test_ragged_row_is_padded(self):
        html = mdmini.to_html("| a | b |\n|---|---|\n| 1 |")
        self.assertIn("<td>1</td><td></td>", html)


@unittest.skipUnless(available(), "no recorded fixtures in tests/fixtures")
class SiteBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        cls.output = root / "output"
        cls.site = root / "site"
        cls.output.mkdir()
        (cls.output / "archive").mkdir()

        book = build_book_from_fixtures()
        text = brief.render(book, display_offset_minutes=330)
        plan = lv.build_levels(book, display_offset_minutes=330)
        (cls.output / "latest.md").write_text(text, encoding="utf-8")
        (cls.output / "latest.json").write_text(json.dumps(plan), encoding="utf-8")
        (cls.output / "archive" / f"{plan['day']}.md").write_text(text, encoding="utf-8")

        cls.stats = make_site.build(cls.output, cls.site)
        cls.index = (cls.site / "index.html").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_index_has_all_four_sections(self):
        for header in ("1) HTF bias", "2) Intraday regime", "3) Setups", "4) Risk note"):
            self.assertIn(header, self.index)
        self.assertEqual(self.index.count("<h2>"), 4)

    def test_mobile_meta_present(self):
        self.assertIn('name="viewport"', self.index)
        self.assertIn("max-width: 760px", self.index)

    def test_banner_shows_local_offset(self):
        self.assertIn("UTC+05:30", self.index)

    def test_levels_json_is_published(self):
        published = json.loads((self.site / "levels.json").read_text(encoding="utf-8"))
        self.assertEqual(len(published["setups"]), 3)
        self.assertIn("value_area", published)

    def test_archive_page_links_the_day(self):
        archive = (self.site / "archive.html").read_text(encoding="utf-8")
        self.assertIn("briefs/", archive)
        self.assertTrue(list((self.site / "briefs").glob("*.html")))

    def test_nojekyll_written(self):
        self.assertTrue((self.site / ".nojekyll").exists())

    def test_stats_count_pages(self):
        self.assertGreaterEqual(self.stats["pages"], 3)
        self.assertEqual(self.stats["archived"], 1)


if __name__ == "__main__":
    unittest.main()
