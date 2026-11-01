import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SufficientCandidateTests(unittest.TestCase):
    def test_candidate_matrix_is_current(self):
        result = subprocess.run(
            [sys.executable, "scripts/sufficient_candidates.py", "--check"],
            cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_no_sufficient_claim(self):
        data = json.loads(
            (ROOT / "edition/patterns/sufficient-candidates.v1.json").read_text()
        )
        self.assertEqual(data["summary"]["entries"], 145)
        self.assertEqual(data["summary"]["candidates"],
                         data["summary"]["entries"] - data["summary"]["by_status"].get("needs-deeper-section", 0))
        self.assertEqual(sum(data["summary"]["by_status"].values()), 145)
        promoted = {row["pattern_id"] for row in json.loads(
            (ROOT / "edition/patterns/sufficient-promotions.v1.json").read_text()
        )["promotions"]}
        self.assertTrue(all(row["technical_coverage"] in ("partial-bounded", "partial",
                                                            "sufficient")
                            for row in data["entries"]))
        self.assertEqual({row["pattern_id"] for row in data["entries"]
                          if row["technical_coverage"] == "sufficient"}, promoted)
        gateway = next(row for row in data["entries"]
                       if row["pattern_id"] == "tycho.pattern.api-gateway")
        self.assertEqual(gateway["review"]["verdict"], "pass")
        self.assertTrue(gateway["review"]["re_reviewed"])


if __name__ == "__main__":
    unittest.main()
