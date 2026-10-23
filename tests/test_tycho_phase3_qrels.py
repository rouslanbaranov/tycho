"""Structural checks for phase-3 topic-isolated qrels and human sample."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
QRELS = ROOT / "evaluation/agent-qrels.phase3.json"
SAMPLE = ROOT / "evaluation/phase3-human-sample.json"


class Phase3QrelsTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(QRELS.read_text(encoding="utf-8"))
        self.sample = json.loads(SAMPLE.read_text(encoding="utf-8"))

    def test_topic_counts_and_split(self):
        self.assertEqual(len(self.data["items"]), 72)
        labels = [item["final_label"] for item in self.data["items"]]
        self.assertEqual(labels.count("answerable"), 19)
        self.assertEqual(labels.count("unanswerable"), 53)
        self.assertEqual(
            sum(1 for item in self.data["items"] if item["split"] == "dev"),
            36)
        self.assertEqual(
            sum(1 for item in self.data["items"]
                if item["split"] == "heldout"), 36)
        self.assertEqual(
            {item["topic_id"] for item in self.data["items"]},
            {"T1", "T2", "T3", "T4", "T5", "T6"})

    def test_label_changes_are_recorded(self):
        changed = [item for item in self.data["items"]
                   if item["phase3_label"] != item["final_label"]]
        self.assertEqual(len(changed), 29)
        for item in changed:
            self.assertEqual(item["phase3_label"], "answerable")
            self.assertEqual(item["final_label"], "unanswerable")
            self.assertEqual(item["accepted"], [])

    def test_answerable_support_is_verbatim(self):
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

    def test_human_sample_is_pending_and_stratified(self):
        self.assertEqual(self.sample["sample_size"], 15)
        self.assertAlmostEqual(self.sample["fraction"], 15 / 72, places=3)
        self.assertEqual(self.sample["status"], "human-review-pending")
        self.assertTrue(all(item["human_verdict"] is None
                            for item in self.sample["items"]))
        labels = [item["adjudicated_label"] for item in self.sample["items"]]
        self.assertEqual(labels.count("answerable"), 5)
        self.assertEqual(labels.count("unanswerable"), 10)


if __name__ == "__main__":
    unittest.main()
