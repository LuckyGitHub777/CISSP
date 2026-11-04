"""Offline checks for the public, self-contained CISSP Domain Atlas."""
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"

class AtlasParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = 0
        self.chapter_links = []
        self.external_code = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "article" and "data-card" in data:
            self.cards += 1
        if tag == "a" and "/cissp/blob/main/domains/" in data.get("href", ""):
            self.chapter_links.append(data["href"])
        if tag == "script" and "src" in data:
            self.external_code.append(data["src"])
        if tag == "link" and data.get("rel") == "stylesheet":
            self.external_code.append(data.get("href", ""))
        if "id" in data:
            self.ids.add(data["id"])

class AtlasChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = HTML.read_text(encoding="utf-8")
        cls.parser = AtlasParser()
        cls.parser.feed(cls.source)

    def test_eight_distinct_existing_chapters(self):
        links = self.parser.chapter_links
        self.assertEqual(self.parser.cards, 8)
        self.assertEqual(len(links), 8)
        self.assertEqual(len(set(links)), 8)
        for link in links:
            filename = link.rsplit("/", 1)[-1]
            self.assertTrue((ROOT / "domains" / filename).is_file(), filename)

    def test_navigation_and_controls(self):
        self.assertIn('lang="en"', self.source)
        self.assertTrue({"hero-title", "atlas", "domain-search", "domain-grid", "visible-count", "explored-count"}.issubset(self.parser.ids))
        self.assertIn("aria-pressed", self.source)
        self.assertIn("prefers-reduced-motion", self.source)

    def test_no_remote_runtime_or_local_tracking(self):
        self.assertFalse(self.parser.external_code)
        for forbidden in ("localStorage", "sessionStorage", "sendBeacon", "XMLHttpRequest", "document.cookie", "fetch("):
            self.assertNotIn(forbidden, self.source)
        self.assertNotRegex(self.source, r"<(?:iframe|form)\\b")

    @unittest.skipUnless(shutil.which("node"), "Node.js not installed")
    def test_embedded_javascript_syntax(self):
        match = re.search(r"<script>\\s*(.*?)\\s*</script>", self.source, re.DOTALL)
        self.assertIsNotNone(match)
        with tempfile.TemporaryDirectory() as temp:
            script = Path(temp) / "atlas.js"
            script.write_text(match.group(1), encoding="utf-8")
            p = subprocess.run(["node", "--check", str(script)], capture_output=True, text=True, check=False)
            self.assertEqual(p.returncode, 0, p.stderr[:400])

if __name__ == "__main__":
    unittest.main()
