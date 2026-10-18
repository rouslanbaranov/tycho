"""Regression tests for Tycho's pilot-only question/routing evaluation."""
import importlib.util
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("smoke", ROOT / "scripts/pilot_lexical_smoke.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class PilotEvaluationTests(unittest.TestCase):
    def test_question_set_is_bounded_and_diverse(self):
        data = json.loads((ROOT / "evaluation/pilot-questions.json").read_text())
        items = data["items"]
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(len(items), 25)
        self.assertEqual(len({x["id"] for x in items}), 25)
        categories = Counter(x["category"] for x in items)
        for cat in ("fact", "synthesis", "tradeoff", "failure",
                    "change_impact", "contradiction", "unanswerable"):
            self.assertGreaterEqual(categories[cat], 2)
        for item in items:
            self.assertTrue((ROOT / item["canonical_page"]).is_file())
            self.assertTrue(item["expected_elements"])
            self.assertTrue(item["evidence_basis"])
            self.assertTrue(item["forbidden_unsupported_claim"])

    def test_tiny_lexical_smoke_not_a_quality_benchmark(self):
        rows = MOD.evaluate()
        self.assertEqual(len(rows), 25)
        # Deliberately in-sample, only three distinct pages: no generalization.
        self.assertEqual(len({r["expected"] for r in rows}), 3)
        self.assertGreaterEqual(sum(r["correct"] for r in rows), 23)


if __name__ == "__main__":
    unittest.main()
