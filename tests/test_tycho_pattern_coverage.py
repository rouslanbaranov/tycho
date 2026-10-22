"""Adversarial checks for candidate coverage, not page coverage."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_coverage import load, validate_data

COVERAGE = ROOT / "edition/patterns/coverage-map.v1.json"
REVERSE = ROOT / "edition/patterns/reverse-map.v1.json"


class PatternCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coverage = load(COVERAGE)
        cls.reverse = load(REVERSE)

    def copy(self):
        return copy.deepcopy(self.coverage), copy.deepcopy(self.reverse)

    def check_error(self, coverage, reverse, message):
        with self.assertRaisesRegex(ValueError, message):
            validate_data(coverage, reverse, ROOT)

    def test_complete_candidate_map(self):
        result = validate_data(self.coverage, self.reverse, ROOT)
        self.assertEqual(result["entries"], 145)
        self.assertEqual(result["reverse_documents"], 76)

    def test_missing_entry_is_rejected(self):
        coverage, reverse = self.copy()
        coverage["entries"].pop()
        self.check_error(coverage, reverse, "coverage-entry-count")

    def test_unknown_pattern_is_rejected(self):
        coverage, reverse = self.copy()
        coverage["entries"][0]["pattern_id"] = "tycho.pattern.not-real"
        self.check_error(coverage, reverse, "coverage-unknown-pattern")

    def test_area_identity_is_rejected(self):
        coverage, reverse = self.copy()
        coverage["entries"][0]["candidate_area"]["document_id"] = "tycho.chapter.000000"
        self.check_error(coverage, reverse, "coverage-area-id")

    def test_summary_is_rejected(self):
        coverage, reverse = self.copy()
        coverage["summary"]["entries"] = 144
        self.check_error(coverage, reverse, "coverage-summary-entries")

    def test_registry_hash_is_rejected(self):
        coverage, reverse = self.copy()
        coverage["registry_sha256"] = "0" * 64
        self.check_error(coverage, reverse, "coverage-registry-hash")

    def test_reverse_mismatch_is_rejected(self):
        coverage, reverse = self.copy()
        reverse["documents"].pop()
        self.check_error(coverage, reverse, "reverse-map-mismatch")


if __name__ == "__main__":
    unittest.main()
