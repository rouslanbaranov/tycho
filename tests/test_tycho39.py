"""Purely mechanical review of Tycho's source-backed outbox chapter.

This validates navigation and illustration invariants, not real DB/broker behavior.
"""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "book/distributed/transactional-outbox-and-idempotency.md"
LANDING = ROOT / "book/distributed/README.md"


class OutboxBookTests(unittest.TestCase):
    def test_contract_and_mermaid_diagrams(self):
        s = CHAPTER.read_text()
        self.assertGreaterEqual(s.count("```mermaid"), 3)
        self.assertIn("sequenceDiagram", s)
        self.assertIn("flowchart TD", s)
        self.assertIn("Text alternative:", s)
        self.assertEqual(s.count("```mermaid"), 4)

    def test_unique_identity_explanations(self):
        s = CHAPTER.read_text()
        for term in ("Client request key K", "Business entity ID R",
                     "Event ID E", "outbox", "deduplication"):
            with self.subTest(term=term):
                self.assertIn(term, s)

    def test_exact_public_provenance_and_failures(self):
        s = CHAPTER.read_text()
        for uri in ("www.postgresql.org/docs/17/transaction-iso.html",
                    "debezium.io/documentation/reference/3.6/",
                    "www.rfc-editor.org/rfc/rfc9110.html",
                    "aws.amazon.com/builders-library/"):
            self.assertIn(uri, s)
        self.assertIn("## 4. Failure and recovery matrix", s)
        self.assertIn("Insufficient-evidence", s)
        self.assertIn("(transactional-outbox-and-idempotency.md)", LANDING.read_text())


if __name__ == "__main__":
    unittest.main()
