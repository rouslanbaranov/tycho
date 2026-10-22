"""Offline evidence-resolution tests over the canonical claim and source records.

No network, source reading, book mutation or graph traversal is involved.
"""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_evidence as evidence  # noqa: E402


class EvidenceResolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store = evidence.build_store()

    def test_supported_claim_resolves_sources_and_owner(self):
        result = evidence.resolve_claim(self.store, "claim.same-intent-retry")
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["claim"]["status"], "evidence-linked")
        self.assertEqual(result["claim"]["relations"], ["qualifies", "supports"])
        self.assertEqual(len(result["claim"]["evidence"]), 2)
        self.assertIsNotNone(result["owner_document"])
        self.assertIn("does not declare this claim ID", " ".join(result["warnings"]))

    def test_contested_claim_exposes_contradiction(self):
        result = evidence.resolve_claim(
            self.store, "claim.http-idempotence-is-not-global-exactly-once")
        self.assertEqual(result["claim"]["status"], "contested")
        self.assertEqual(len(result["claim"]["contradictions"]), 1)
        self.assertIn("contested", " ".join(result["warnings"]).casefold())

    def test_unavailable_claim_is_not_presented_as_inspection(self):
        result = evidence.resolve_claim(
            self.store, "claim.jep491-full-text-unavailable")
        self.assertEqual(result["claim"]["status"], "insufficient-evidence")
        entry = result["claim"]["evidence"][0]
        self.assertEqual(entry["relation"], "unavailable")
        self.assertEqual(entry["source"]["admission"], "pending-content-access")
        self.assertIsNone(entry["location"])
        self.assertFalse(entry["allowed_as_inspected_evidence"])
        self.assertIsNone(result["owner_document"])
        self.assertIn("outside the book route index", " ".join(result["warnings"]))

    def test_source_lists_claim_relations(self):
        result = evidence.resolve_source(self.store, "src.http-semantics")
        self.assertEqual(result["status"], "ok")
        relations = {item["relation"] for item in result["claims"]}
        self.assertEqual(relations, {"contradicts", "qualifies"})
        self.assertTrue(result["source"]["inspection_claim_allowed"])

    def test_document_shows_frontmatter_and_ledger(self):
        result = evidence.resolve_document(
            self.store, "tycho.page.ace968ab1de8409383c6a9b22a00d006")
        self.assertEqual(result["document"]["path"],
                         "book/distributed/transactional-outbox-and-idempotency.md")
        self.assertEqual(result["frontmatter_claims"], [])
        self.assertEqual({item["claim_id"] for item in result["ledger_claims"]},
                         {"claim.same-intent-retry",
                          "claim.http-idempotence-is-not-global-exactly-once"})
        self.assertIn("absent from frontmatter", " ".join(result["warnings"]))
        self.assertEqual({item["source_id"] for item in result["sources"]},
                         {"src.aws-idempotency", "src.http-semantics"})

    def test_decision_returns_direct_references_only(self):
        result = evidence.resolve_decision(
            self.store, "tycho.decision.054f312b9e744575ac80632f4acf72fa")
        self.assertEqual(result["decision"]["kind"], "decision")
        self.assertGreater(len(result["direct_references"]), 0)
        self.assertIn("no graph traversal", " ".join(result["warnings"]))

    def test_snapshot_accepts_current_and_refuses_other(self):
        same = evidence.resolve_claim(
            self.store, "claim.same-intent-retry",
            expected_snapshot=self.store["snapshot"])
        self.assertEqual(same["snapshot"], self.store["snapshot"])
        with self.assertRaises(evidence.EvidenceError) as caught:
            evidence.resolve_claim(self.store, "claim.same-intent-retry",
                                   expected_snapshot="0" * 64)
        self.assertEqual(caught.exception.status, "snapshot-mismatch")

    def test_unknown_ids_and_wrong_kind(self):
        for action, value in (
                (evidence.resolve_claim, "claim.missing"),
                (evidence.resolve_source, "src.missing"),
                (evidence.resolve_document, "tycho.page.missing"),
                (evidence.resolve_decision, "tycho.decision.missing")):
            with self.assertRaises(evidence.EvidenceError) as caught:
                action(self.store, value)
            self.assertEqual(caught.exception.status, "not-found")
        with self.assertRaises(evidence.EvidenceError) as caught:
            evidence.resolve_decision(
                self.store, "tycho.page.ace968ab1de8409383c6a9b22a00d006")
        self.assertEqual(caught.exception.status, "invalid-request")

    def test_invalid_ledger_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "claims.json"
            path.write_text(json.dumps({"schema_version": 1, "claims": []}),
                            encoding="utf-8")
            with self.assertRaises(evidence.EvidenceError) as caught:
                evidence.build_store(
                    claims_path=path,
                    register_path=evidence.DEFAULT_REGISTER,
                    lock_path=evidence.DEFAULT_LOCK,
                    route_path=evidence.DEFAULT_ROUTE)
            self.assertEqual(caught.exception.status, "not-available")


if __name__ == "__main__":
    unittest.main()
