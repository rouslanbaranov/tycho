"""Tests for diagnostic retrieval fingerprint summaries."""
import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import search_regression  # noqa: E402

class RegressionTests(unittest.TestCase):
    def test_summary_and_drift(self):
        records=[
            {"key":"v2:a","split":"v2","fingerprint":["a#1"],"rank":1},
            {"key":"v2:b","split":"v2","fingerprint":["b#1"],"rank":3},
            {"key":"p3:c","split":"p3","fingerprint":["c#1"],"rank":None},
        ]
        metrics=search_regression.summarize(records)
        self.assertEqual(metrics["all"]["queries"],3)
        self.assertEqual(metrics["all"]["hit@1"],0.3333)
        self.assertEqual(metrics["all"]["hit@3"],0.6667)
        base={"queries":{"v2:a":{"fingerprint":["old#1"]}},"metrics":metrics}
        cur={"queries":{x["key"]:{"fingerprint":x["fingerprint"]}
                        for x in records},"metrics":metrics}
        self.assertEqual(search_regression.compare(base,cur)["status"],"drift")

if __name__=="__main__":
    unittest.main()
