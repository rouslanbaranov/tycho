"""Tests for the post-enrichment diagnostic runner."""
import sys
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import post_enrichment_check  # noqa: E402

class PostCheckTests(unittest.TestCase):
    def test_run_combines_check_diff_verify(self):
        with patch.object(post_enrichment_check.search_reindex, "check",
                          return_value={"status":"current"}), \
             patch.object(post_enrichment_check.search_reindex, "diff_current",
                          return_value={"status":"changed"}), \
             patch.object(post_enrichment_check.search_reindex, "verify",
                          return_value={"status":"verified"}):
            report=post_enrichment_check.run(ROOT)
        self.assertEqual(report["status"],"verified")
        self.assertEqual(report["check"]["status"],"current")
        self.assertNotIn("regression",report)

    def test_optional_regression(self):
        with patch.object(post_enrichment_check.search_reindex, "check",
                          return_value={"status":"current"}), \
             patch.object(post_enrichment_check.search_reindex, "diff_current",
                          return_value={"status":"changed"}), \
             patch.object(post_enrichment_check.search_reindex, "verify",
                          return_value={"status":"verified"}):
            import search_regression
            with patch.object(search_regression, "run",
                              return_value={"status":"ok"}):
                report=post_enrichment_check.run(ROOT,regression=True)
        self.assertEqual(report["regression"]["status"],"ok")

if __name__=="__main__":
    unittest.main()
