"""Tests for read-only H3 coverage diagnostics."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import h3_coverage  # noqa: E402


class H3CoverageTests(unittest.TestCase):
    def test_summary_detects_gaps_and_orphans(self):
        sections = [
            {"section_key": "a#1", "section_id": "1", "path": "a",
             "heading": "One", "heading_level": 2},
            {"section_key": "a#2", "section_id": "2", "path": "a",
             "heading": "Two", "heading_level": 2},
            {"section_key": "b#1", "section_id": "1", "path": "b",
             "heading": "One", "heading_level": 2},
        ]
        passages = [
            {"passage_key": "a#1~x", "parent_section_key": "a#1", "path": "a"},
            {"passage_key": "orphan~x", "parent_section_key": "missing",
             "path": "c"},
        ]
        report = h3_coverage.summarize(sections, passages)
        self.assertEqual(report["h2_sections"], 3)
        self.assertEqual(report["h2_with_h3"], 1)
        self.assertEqual(report["h2_without_h3"], 2)
        self.assertEqual(report["orphan_h3"], 1)
        self.assertEqual(report["pages_without_h3"], 1)
        grouped = h3_coverage.targets(sections, passages, limit=5)
        self.assertEqual(sum(row["missing_h2"] for row in grouped), 2)
        self.assertEqual(grouped[0]["path"], "a")


if __name__ == "__main__":
    unittest.main()
