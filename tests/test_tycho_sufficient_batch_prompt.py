import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from sufficient_batch_prompt import build_prompt


class SufficientBatchPromptTests(unittest.TestCase):
    def test_every_batch_renders_its_entries(self):
        plan = json.loads(
            (ROOT / "research/sufficient-pilot-540/batch-plan.json").read_text())
        for batch in plan["batches"]:
            prompt = build_prompt(ROOT, batch["id"])
            self.assertIn("sufficient: 0", prompt)
            for item in batch["entries"]:
                self.assertIn(item["pattern_id"], prompt)

    def test_unknown_batch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown batch"):
            build_prompt(ROOT, "B99")


if __name__ == "__main__":
    unittest.main()
