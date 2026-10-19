"""Offline fixture tests for local Markdown navigation and structural checks."""
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_book_navigation as nav  # noqa: E402


class BookNavigationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "book").mkdir()
        self.write("book/README.md", "# Synthetic book\n\n## Purpose and mission\n\n"
                   "[Visit page](chapter.md#what-it-does)\n")
        self.write("book/chapter.md", "# Chapter\n\n## What it does\n\nOriginal fixture.\n")

    def write(self, rel, data):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data)
        return path

    def reasons(self):
        return [e["rule"] for e in nav.validate_tree(self.root)["issues"]]

    def test_valid_local_navigation(self):
        self.assertEqual(nav.validate_tree(self.root)["issue_count"], 0)

    def test_missing_link_target_reported_without_content(self):
        self.write("book/chapter.md", "# Chapter\n\n[Missing](unknown.md)\n")
        report = nav.validate_tree(self.root)
        self.assertIn("missing-local-target", self.reasons())
        self.assertTrue(all(set(x)=={"path", "line", "rule"} for x in report["issues"]))

    def test_missing_local_anchor_identified(self):
        self.write("book/README.md", "# Synthetic book\n## Purpose and mission\n"
                   "[Page](chapter.md#no-such-heading)\n")
        self.assertIn("missing-local-anchor", self.reasons())

    def test_duplicate_heading_anchors_have_suffixes(self):
        headings, links, errs = nav.parse_document(
            "# Test\n## Same heading\n## Same heading\n")
        self.assertIn("same-heading", headings)
        self.assertIn("same-heading-1", headings)
        self.assertEqual(errs, [])

    def test_mermaid_fence_skips_links_and_balances(self):
        self.write("book/chapter.md",
                   "# Page\n## What it does\n```mermaid\nflowchart LR\n A[Missing](absent.md) --> B[OK]\n```\n")
        self.assertEqual(self.reasons(), [])

    def test_unclosed_fence_is_reported(self):
        self.write("book/chapter.md", "# Chapter\n```python\nprint('hello')\n")
        self.assertIn("unclosed-fence", self.reasons())

    def test_relative_parent_link_inside_repository_allowed(self):
        self.write("authoring/reference.md", "# Verified reference\n")
        self.write("book/chapter.md", "# Chapter\n## What it does\n[Public reference](../authoring/reference.md)\n")
        self.assertEqual(self.reasons(), [])

    def test_repo_escape_is_rejected(self):
        self.write("book/chapter.md", "# Chapter\n[Bad](../../private.md)\n")
        self.assertIn("escapes-repository", self.reasons())

    def test_landing_requires_purpose_mission_and_route(self):
        self.write("book/README.md", "# Root\nNo reader mission or links.\n")
        self.assertIn("landing-missing-purpose-mission", self.reasons())
        self.assertIn("landing-missing-internal-navigation", self.reasons())

    def test_page_size_cap_is_explicit(self):
        self.write("book/chapter.md", "# Chapter\n" + "filler " * 300)
        self.assertIn("page-size-safety-cap",
                      [x["rule"] for x in nav.validate_tree(self.root, 1000)["issues"]])


if __name__ == "__main__":
    unittest.main()
