"""Bounded structural regression checks for application architecture research pages.

Not a software benchmark or independent source-claim accuracy review.
"""
from pathlib import Path
import unittest
from edition_paths import canonical_path, relative_link

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "book/application"
PAGES = (
    "quality-drivers-and-architecture-views.md",
    "architecture-styles-and-module-boundaries.md",
    "architecture-evolution-and-extraction.md",
)


class ApplicationArchitectureResearchTests(unittest.TestCase):
    def test_pages_are_substantive_and_explanatory(self):
        for name in PAGES:
            with self.subTest(page=name):
                text = canonical_path(DIRECTORY / name).read_text(encoding="utf-8")
                self.assertGreater(len(text), 7000)
                self.assertGreaterEqual(text.count("```mermaid"), 3)
                self.assertGreaterEqual(text.count("Text alternative:"), 3)
                self.assertIn("Evidence", text)
                self.assertIn("Insufficient", text)

    def test_primary_public_origins_are_cited(self):
        style = canonical_path(DIRECTORY / PAGES[1]).read_text()
        for origin in (
            "martinfowler.com/articles/microservices.html",
            "martinfowler.com/bliki/BoundedContext.html",
            "alistair.cockburn.us/hexagonal-architecture",
            "docs.oasis-open.org/soa-rm/v1.0/soa-rm.html",
            "docs.spring.io/spring-modulith/reference/1.3/verification.html",
        ):
            self.assertIn(origin, style)
        quality = canonical_path(DIRECTORY / PAGES[0]).read_text()
        for origin in (
            "docs.arc42.org/section-1/",
            "c4model.com/introduction",
            "sre.google/workbook/implementing-slos/",
        ):
            self.assertIn(origin, quality)

    def test_navigation_links_to_actual_pages(self):
        landing = (DIRECTORY / "README.md").read_text()
        self.assertIn("```mermaid", landing)
        for name in PAGES:
            self.assertTrue(canonical_path(DIRECTORY / name).is_file())
            self.assertIn("(" + relative_link(DIRECTORY / "README.md", DIRECTORY / name) + ")", landing)


if __name__ == "__main__":
    unittest.main()
