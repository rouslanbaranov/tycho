"""Pure tests for the calibrated refusal policy and its summary."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import answerability  # noqa: E402
import evaluate_abstention as evaluation  # noqa: E402


class AnswerabilityTests(unittest.TestCase):
    def test_scope_intent_abstains(self):
        result = answerability.assess(
            "How do I configure a specific vendor cache policy?", 20.0, 0.0)
        self.assertTrue(result["no_confident_answer"])
        self.assertEqual(result["basis"], "out-of-scope-intent")

    def test_low_score_abstains(self):
        result = answerability.assess("cache invalidation", 7.49, 0.0)
        self.assertTrue(result["no_confident_answer"])
        self.assertEqual(result["basis"], "low-lexical-score")

    def test_unknown_terms_abstain(self):
        result = answerability.assess("cache invalidation", 12.0, 0.6)
        self.assertTrue(result["no_confident_answer"])
        self.assertEqual(result["basis"], "unknown-terms")

    def test_confident_lexical_hit_does_not_abstain(self):
        result = answerability.assess("cache invalidation", 12.0, 0.2)
        self.assertFalse(result["no_confident_answer"])
        self.assertEqual(result["basis"], "no-abstention-signal")
        self.assertIsNone(result["answerable"])

    def test_summary_counts_refusal_and_retention(self):
        rows = [
            {"unanswerable": True, "abstained": True, "basis": "scope"},
            {"unanswerable": True, "abstained": False, "basis": "none"},
            {"unanswerable": False, "abstained": True, "basis": "score"},
            {"unanswerable": False, "abstained": False, "basis": "none"},
        ]
        summary = evaluation.summarize(rows)
        self.assertEqual(summary["unanswerable_abstained"], 1)
        self.assertEqual(summary["unanswerable_false_answer"], 1)
        self.assertEqual(summary["answerable_false_abstain"], 1)
        self.assertEqual(summary["answerable_retention"], 0.5)
        self.assertEqual(summary["abstention_precision"], 0.5)


if __name__ == "__main__":
    unittest.main()
