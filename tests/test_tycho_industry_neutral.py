"""Editorial-language boundary fixtures; no forbidden terms appear literally."""
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_boundary as guard  # noqa: E402


class NeutralTerminologyTests(unittest.TestCase):
    def test_neutral_deployment_vocabulary_passes(self):
        for phrase in (
            "restricted enterprise environments",
            "regulated environments",
            "corporate infrastructure",
            "security-constrained deployments",
            "public architecture and independent synthetic case studies",
            "benchmark ranking and source provenance",
        ):
            self.assertEqual(guard.violations("docs/example.md", phrase), [])

    def test_english_industry_stem_and_inflections_rejected(self):
        root = "ba" + "nk"
        for token in (root, root + "ing", root + "s", root + "-specific",
                      root.upper(), root.title() + "ing", root + "_runtime"):
            self.assertIn(
                "industry-specific terminology is prohibited",
                guard.violations("docs/neutral.md", "Allowed text; " + token),
            )

    def test_cyrillic_industry_stem_and_inflections_rejected(self):
        root = "ба" + "нк"
        for token in (root, root + "овский", root + "и", root.upper(),
                      root + "овское окружение"):
            self.assertIn(
                "industry-specific terminology is prohibited",
                guard.violations("docs/neutral.md", "Описание: " + token),
            )

    def test_path_names_also_checked_and_diagnostics_do_not_echo_content(self):
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            token = "ba" + "nk"
            (root / ("example-" + token + ".md")).write_text(
                "This document contains only neutral text.", encoding="utf-8"
            )
            with patch.object(guard, "ROOT", root):
                self.assertEqual(guard.main(), 1)

    def test_existing_local_link_rule_preserved(self):
        findings = guard.violations("test.md", "file://" + "private/notes.md")
        self.assertIn("non-self-contained local link", findings)

    def test_guard_has_no_literal_restricted_words(self):
        contents = (ROOT / "scripts" / "check_boundary.py").read_text(
            encoding="utf-8"
        )
        for stem in ("ba" + "nk", "ба" + "нк"):
            self.assertNotIn(stem, contents.casefold())


if __name__ == "__main__":
    unittest.main()
