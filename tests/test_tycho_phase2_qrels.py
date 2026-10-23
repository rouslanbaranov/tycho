"""Structural checks for the phase-2 agent-adjudicated qrels."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
QRELS = ROOT / "evaluation/agent-qrels.phase2.json"
PHASE1 = ROOT / "evaluation/independent-agent-qrels.phase1.json"


class Phase2QrelsTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(QRELS.read_text(encoding="utf-8"))
        self.phase1 = json.loads(PHASE1.read_text(encoding="utf-8"))

    def test_counts_and_split(self):
        self.assertEqual(len(self.data["items"]), 80)
        labels = [item["final_label"] for item in self.data["items"]]
        self.assertEqual(labels.count("answerable"), 54)
        self.assertEqual(labels.count("unanswerable"), 26)
        self.assertEqual(self.data["summary"]["unsupported"], 6)
        self.assertEqual(
            sum(1 for item in self.data["items"] if item["split"] == "dev"), 40)
        self.assertEqual(
            sum(1 for item in self.data["items"]
                if item["split"] == "heldout"), 40)

    def test_questions_are_unchanged(self):
        phase1 = {item["id"]: item["question"]
                  for item in self.phase1["items"] + self.phase1["unanswerable"]}
        for item in self.data["items"]:
            self.assertEqual(item["question"], phase1[item["id"]])

    def test_answerable_items_have_support_in_pages(self):
        for item in self.data["items"]:
            if item["final_label"] != "answerable":
                continue
            self.assertTrue(item["accepted"], item["id"])
            for answer in item["accepted"]:
                path = ROOT / answer["path"]
                self.assertTrue(path.is_file(), item["id"])
                quote = " ".join(answer["quote"].split())
                body = " ".join(path.read_text(encoding="utf-8").split())
                self.assertIn(quote, body, item["id"])
                if answer["section_id"] is not None:
                    self.assertRegex(
                        answer["section_id"], r"^[a-z0-9][a-z0-9-]{0,119}$")

    def test_unanswerable_items_have_no_accepted_pages(self):
        for item in self.data["items"]:
            if item["final_label"] == "unanswerable":
                self.assertEqual(item["accepted"], [], item["id"])


if __name__ == "__main__":
    unittest.main()
