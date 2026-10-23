"""Structural checks for the frozen agent-adjudicated challenge set."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "evaluation/independent-agent-qrels.phase1.json"


class IndependentAgentQrelsTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(PATH.read_text(encoding="utf-8"))

    def test_frozen_counts(self):
        self.assertEqual(self.data["label_status"],
                         "agent-adjudicated-not-human")
        self.assertEqual(len(self.data["items"]), 60)
        self.assertEqual(len(self.data["unanswerable"]), 20)
        self.assertEqual(len(self.data["topics"]), 15)

    def test_answerable_items_have_sources(self):
        for item in self.data["items"]:
            self.assertEqual(item["answerability"], "answerable")
            self.assertGreaterEqual(len(item["sources"]), 2)
            self.assertGreaterEqual(len(item["key_facts"]), 2)

    def test_unanswerable_reasons_are_bounded(self):
        allowed = {"vendor-specific", "current-fact", "exact-measurement",
                   "out-of-scope"}
        for item in self.data["unanswerable"]:
            self.assertIn(item["reason"], allowed)

    def test_no_tycho_material_leaked(self):
        payload = json.dumps(self.data, ensure_ascii=False).lower()
        self.assertNotIn("book/volumes", payload)
        self.assertNotIn("tycho.pattern", payload)
        self.assertNotIn("search_snapshot", payload)


if __name__ == "__main__":
    unittest.main()
