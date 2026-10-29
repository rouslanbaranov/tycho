"""V12 search namespace, reverse index and one-way-link regressions."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_v12_index
import validate_v12


def load(path):
    return json.loads((ROOT / path).read_text())


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.index = load("generated/v12-index.v1.json")
        self.registry = load("edition/v12/registry.json")
        self.reverse = load("edition/v12/reverse-index.v1.json")

    def test_index_contains_only_v12_documents(self):
        self.assertEqual(self.index["volume"], "v12")
        self.assertEqual(len(self.index["documents"]), 54)
        for document in self.index["documents"]:
            if document["artifact_type"] == "document":
                self.assertTrue(document["path"].startswith(
                    "book/volumes/v12-modeling-simulation-and-decision-validation/"))
            else:
                self.assertTrue(document["path"].startswith("edition/v12/"))
        self.assertNotIn("book/volumes/v11-pattern-atlas", json.dumps(self.index["documents"]))

    def test_reverse_index_is_derived(self):
        self.assertEqual(self.reverse["patterns"], self.registry["reverse_index"])
        expected = {}
        for collection in self.registry["artifacts"].values():
            for artifact in collection:
                for pattern_id in artifact["pattern_ids"]:
                    expected.setdefault(pattern_id, []).append(artifact["id"])
        actual = {key: [entry["id"] for entry in value]
                  for key, value in self.reverse["patterns"].items()}
        self.assertEqual(expected, actual)

    def test_pattern_query_prefers_canonical_owner(self):
        result = build_v12_index.query("queue-based load leveling")
        self.assertGreater(result["returned"], 0)
        self.assertEqual(result["results"][0]["artifact_type"], "pattern")
        self.assertIn("v07-performance-scale-and-resilience", result["results"][0]["path"])

    def test_modeling_query_returns_v12_documents(self):
        result = build_v12_index.query("monte carlo convergence", limit=10)
        ids = {entry["id"] for entry in result["results"]}
        self.assertTrue(any(i.startswith("tycho.page.") for i in ids))
        self.assertTrue(any(i.startswith("tycho.run.") for i in ids))

    def test_iron_rule_scan_has_no_v12_leak(self):
        result = validate_v12.validate(ROOT)
        self.assertEqual(result["protected"]["leaked"], 0)
        self.assertEqual(result["protected"]["changed"], 0)


if __name__ == "__main__":
    unittest.main()
