"""Offline checks for the public, self-contained CISSP Domain Atlas."""
import base64
import hashlib
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
        self.mark_controls = []
        self.heading_ids = set()
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "article" and "data-card" in data:
            self.cards += 1
        if tag == "a" and data.get("href", "").startswith("domains/domain-"):
            self.chapter_links.append(data["href"])
        if tag == "script" and "src" in data:
            self.external_code.append(data["src"])
        if tag == "link" and data.get("rel") == "stylesheet":
            self.external_code.append(data.get("href", ""))
        if "id" in data:
            self.ids.add(data["id"])
        if tag == "h3" and "id" in data:
            self.heading_ids.add(data["id"])
        if tag == "button" and "mark" in data.get("class", "").split():
            self.mark_controls.append(data)

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
            self.assertTrue(link.startswith("domains/domain-"), link)
            self.assertNotIn("..", link)
            self.assertTrue((ROOT / link).is_file(), link)

    def test_readme_direct_chapters_and_flashcards(self):
        guide = (ROOT / "README.md").read_text(encoding="utf-8")
        chapters = re.findall(r"\]\((domains/domain-\d{2}-[^)]+\.md)\)", guide)
        flashcards = re.findall(r"\]\((flashcards/domain-\d{2}-flashcards\.md)\)", guide)
        self.assertEqual(len(chapters), 8)
        self.assertEqual(len(set(chapters)), 8)
        self.assertEqual(len(flashcards), 8)
        self.assertEqual(len(set(flashcards)), 8)
        for item in chapters + flashcards:
            self.assertTrue((ROOT / item).is_file(), item)
        for path in ("accelerated", "standard", "extended"):
            self.assertIn(f"](study-system/{path}-study-path.md)", guide)
            self.assertTrue((ROOT / "study-system" / f"{path}-study-path.md").is_file())

    def test_navigation_and_controls(self):
        self.assertIn('lang="en"', self.source)
        self.assertTrue({"hero-title", "atlas", "domain-search", "domain-grid", "visible-count", "explored-count", "empty-state"}.issubset(self.parser.ids))
        self.assertIn("aria-pressed", self.source)
        self.assertIn("prefers-reduced-motion", self.source)

    def test_mark_buttons_have_stateful_accessible_names(self):
        self.assertEqual(len(self.parser.mark_controls), 8)
        for n, data in enumerate(self.parser.mark_controls, start=1):
            with self.subTest(domain=n):
                ident = f"domain-{n:02d}"
                self.assertEqual(data.get("id"), f"{ident}-mark")
                self.assertEqual(data.get("aria-labelledby"),
                                 f"{ident}-mark {ident}-title")
                self.assertIn(f"{ident}-title", self.parser.heading_ids)
                self.assertEqual(data.get("aria-pressed"), "false")
                self.assertNotIn("aria-label", data,
                                 "A fixed accessible name would mask the updated button text")

    def test_no_remote_runtime_or_local_tracking(self):
        self.assertFalse(self.parser.external_code)
        for forbidden in ("localStorage", "sessionStorage", "sendBeacon", "XMLHttpRequest", "document.cookie", "fetch("):
            self.assertNotIn(forbidden, self.source)
        self.assertNotRegex(self.source, r"<(?:iframe|form)\b")

    def test_self_contained_atlas_hash_bound_content_security_policy(self):
        match = re.search(
            r'<meta http-equiv="Content-Security-Policy" content="([^"]+)">',
            self.source,
        )
        self.assertIsNotNone(match, "Missing deployable CSP metadata")
        policy = match.group(1)
        for directive in (
            "default-src 'none'", "connect-src 'none'", "object-src 'none'",
            "form-action 'none'", "frame-src 'none'", "base-uri 'none'",
        ):
            self.assertIn(directive, policy)
        self.assertNotIn("'unsafe-inline'", policy)
        self.assertNotIn("'unsafe-eval'", policy)
        self.assertIn('<meta name="referrer" content="no-referrer">', self.source)
        for tag, directive in (("script", "script-src"), ("style", "style-src")):
            with self.subTest(tag=tag):
                blocks = re.findall(rf"<{tag}>(.*?)</{tag}>", self.source, re.DOTALL)
                self.assertEqual(len(blocks), 1, "Unexpected active content blocks")
                digest = base64.b64encode(
                    hashlib.sha256(blocks[0].encode("utf-8")).digest()
                ).decode("ascii")
                expected = f"{directive} 'sha256-{digest}'"
                self.assertIn(expected, policy, "CSP hash does not match source bytes")
        self.assertNotRegex(self.source, r"\bon(?:click|load|error|input|change)=")
        self.assertNotIn("javascript:", self.source.lower())

    @unittest.skipUnless(shutil.which("node"), "Node.js not installed")
    def test_embedded_javascript_syntax(self):
        match = re.search(r"<script>\s*(.*?)\s*</script>", self.source, re.DOTALL)
        self.assertIsNotNone(match)
        with tempfile.TemporaryDirectory() as temp:
            script = Path(temp) / "atlas.js"
            script.write_text(match.group(1), encoding="utf-8")
            p = subprocess.run(["node", "--check", str(script)], capture_output=True, text=True, check=False)
            self.assertEqual(p.returncode, 0, p.stderr[:400])

if __name__ == "__main__":
    unittest.main()
