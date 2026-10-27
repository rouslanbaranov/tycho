"""Offline tests for the independent re-review scope manifest."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_rereview_scope as scope  # noqa: E402

MANIFEST = ROOT / scope.OUT
LEDGER = json.loads(
    (ROOT / "edition/patterns/reading-ledger.v1.json").read_text())["records"]
READ_IDS = {record["id"] for record in LEDGER}


class ScopeManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(MANIFEST.read_text())

    def test_counts(self):
        counts = self.payload["counts"]
        self.assertEqual(counts["records"], 145)
        self.assertEqual(counts["phase_a"], 52)
        self.assertEqual(counts["phase_b"], 93)
        self.assertEqual(counts["phase_a_verdicts"],
                         {"pass": 33, "pass-with-findings": 16, "reject": 3})
        self.assertEqual(counts["phase_b_states"]["promoted-after-remediation"], 87)
        self.assertEqual(counts["phase_b_states"].get("residual-findings-after-re-review", 0), 0)

    def test_current_page_hashes(self):
        for entry in self.payload["phase_a"] + self.payload["phase_b"]:
            path = ROOT / entry["current_page_path"]
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                entry["current_page_sha256"], entry["pattern_id"])

    def test_card_and_source_bindings(self):
        for entry in self.payload["phase_a"]:
            self.assertTrue((ROOT / entry["card_path"]).is_file(),
                            entry["pattern_id"])
            self.assertTrue(entry["source_units"], entry["pattern_id"])
            for unit in entry["source_units"]:
                self.assertIn(unit["read_record_id"], READ_IDS)

    def test_slash_heading_anchors(self):
        anchors = {entry["pattern_id"]: entry["card_anchor"]
                   for entry in self.payload["phase_a"]}
        self.assertEqual(anchors["tycho.pattern.cache-aside-lazy-loading"],
                         "cache-aside--lazy-loading")
        self.assertEqual(anchors["tycho.pattern.dead-letter-channel-dlq"],
                         "dead-letter-channel--dlq")

    def test_manifest_is_current(self):
        self.assertEqual(scope.build(), self.payload)


if __name__ == "__main__":
    unittest.main()
