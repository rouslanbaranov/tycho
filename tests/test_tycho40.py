"""Structural and synthetic arithmetic checks, not a tested deployment."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "book/delivery/safe-rollout-and-recovery.md"
LANDING = ROOT / "book/delivery/README.md"


class DeliveryResearchTests(unittest.TestCase):
    def test_synthetic_backlog_is_consistent(self):
        self.assertEqual((120 - 90) * 30, 900)

    def test_mermaid_and_text_alternatives(self):
        text = CHAPTER.read_text()
        self.assertGreaterEqual(text.count("```mermaid"), 4)
        self.assertIn("stateDiagram-v2", text)
        self.assertIn("sequenceDiagram", text)
        self.assertGreaterEqual(text.count("Text alternative:"), 4)
        self.assertIn("```mermaid", LANDING.read_text())
        self.assertIn("(safe-rollout-and-recovery.md)", LANDING.read_text())

    def test_evidence_and_unanswerable_recovery(self):
        text = CHAPTER.read_text()
        for source in ("kubernetes.io/docs/concepts/workloads/controllers/deployment/",
                       "argo-rollouts.readthedocs.io/en/stable/features/",
                       "docs.aws.amazon.com/whitepapers/latest/",
                       "sre.google/sre-book/addressing-cascading-failures/"):
            self.assertIn(source, text)
        for word in ("RTO", "RPO", "rollback", "forward", "Insufficient-evidence"):
            self.assertIn(word, text)
        self.assertIn("No live cluster/database", text)


if __name__ == "__main__":
    unittest.main()
