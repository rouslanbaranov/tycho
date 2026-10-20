"""Structural and synthetic contract verification for Issue TYCHO-80.

No actual Raft deployment, database test or independently validated claim.
"""
from pathlib import Path
import unittest
from edition_paths import canonical_path, relative_link

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "book/distributed"
PAGES = {
    "causality-ordering-and-consensus.md": (
        "raft.github.io", "microsoft.com/en-us/research/publication/time-clocks",
        "stateDiagram-v2", "consensus"),
    "transaction-isolation-and-sagas.md": (
        "postgresql.org/docs/17/transaction-iso.html",
        "microservices.io/patterns/data/saga.html",
        "stateDiagram-v2", "compensation"),
    "cqrs-event-sourcing-and-projections.md": (
        "martinfowler.com/bliki/CQRS.html",
        "martinfowler.com/eaaDev/EventSourcing.html",
        "stateDiagram-v2", "projection"),
}


class DistributedResearchChecks(unittest.TestCase):
    def test_pages_include_visuals_and_precise_sources(self):
        for page, references in PAGES.items():
            with self.subTest(page=page):
                content = canonical_path(BASE / page).read_text(encoding="utf-8")
                self.assertGreater(len(content), 8000)
                self.assertGreaterEqual(content.count("```mermaid"), 3)
                self.assertGreaterEqual(content.count("Text alternative:"), 3)
                self.assertEqual(content.count("```") % 2, 0)
                for reference in references:
                    self.assertIn(reference.lower(), content.lower())
                self.assertIn("insufficient", content.lower())

    def test_navigation_points_to_existing_content(self):
        landing = (BASE / "README.md").read_text()
        for name in list(PAGES) + ["transactional-outbox-and-idempotency.md"]:
            self.assertIn("(" + relative_link(BASE / "README.md", BASE / name) + ")", landing)
            self.assertTrue(canonical_path(BASE / name).is_file())
        self.assertIn("```mermaid", landing)

    def test_synthetic_arithmetic_only(self):
        # Event-sourcing projection illustration: 2 confirms then 1 cancel.
        self.assertEqual(1 + 1 - 1, 1)
        # Fixed five-member voter group requires a three-node majority.
        members = 5
        self.assertEqual(members // 2 + 1, 3)
        self.assertLess(2, members // 2 + 1)


if __name__ == "__main__":
    unittest.main()
