"""Bounded guards for the B47 Consistent Hashing review evidence."""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNITS = ROOT / "edition/patterns/owner-units.v1.json"
LEDGER = ROOT / "edition/patterns/reading-ledger.v1.json"
RECORDS = ROOT / "edition/patterns/sufficient-review-records.v1.json"
PACKETS = ROOT / "edition/patterns/sufficient-rereview-packets.v1.json"
PROMOTIONS = ROOT / "edition/patterns/sufficient-promotions.v1.json"
CARDS = ROOT / "edition/patterns/card-batches.v1.json"
PATTERN = "tycho.pattern.consistent-hashing"
DIMS = ("mechanism", "invariant", "failure_recovery", "alternative")
HISTORICAL_PAGE = (
    "20fad2cfe4434e75abac7d4a17774040f44cd4a0ba6955b0e360a0fdb40b6509"
)


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


class B47ConsistentHashingReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        units = json.loads(UNITS.read_text(encoding="utf-8"))
        cls.entry = next(item for item in units["entries"]
                         if item["pattern_id"] == PATTERN)
        cls.owner = (ROOT / cls.entry["owner"]["path"]).read_text(encoding="utf-8")
        cls.owner_norm = norm(cls.owner)
        cls.ledger = {
            item["id"]: item
            for item in json.loads(LEDGER.read_text(encoding="utf-8"))["records"]
        }

    def test_four_dimensions_bind_read_sections_and_revisions(self):
        for dim in DIMS:
            row = self.entry["technical_evidence"][dim]
            self.assertEqual(row["state"], "supported", dim)
            binding = row["binding"]
            record = self.ledger[binding["ledger_record"]]
            self.assertEqual(record["status"], "read", dim)
            self.assertEqual(record["source_id"], binding["source_id"], dim)
            self.assertIn(binding["section"], record["sections_read"], dim)
            self.assertEqual(binding["revision"], record["content_sha256"], dim)
            claims = norm(" ".join(record["claims_supported"]))
            self.assertIn(norm(binding["quote"]), claims, dim)

    def test_invariant_is_qualified_as_an_expectation(self):
        quote = self.entry["technical_evidence"]["invariant"]["quote"]
        self.assertIn(norm(quote), self.owner_norm)
        self.assertIn("measure the actual moved fraction", self.owner_norm)
        self.assertIn("not a guarantee", self.owner_norm)
        self.assertIn("the joining or leaving node's share", self.owner_norm)

    def test_dynamo_token_quote_is_bound_to_partitioning_section(self):
        support = self.entry["technical_evidence"]["mechanism"]["supporting_bindings"]
        binding = next(item for item in support
                       if item["quote"].startswith("instead of mapping a node"))
        self.assertEqual(binding["section"], "4.2 Partitioning Algorithm")

    def test_register_scopes_include_b47_units(self):
        sources = {item["id"]: item for item in json.loads(
            (ROOT / "sources/register.json").read_text(encoding="utf-8"))["sources"]}
        self.assertEqual(sources["src.dynamo"]["content_verified"], "2026-10-31")
        self.assertIn("4.2 Partitioning Algorithm",
                      sources["src.dynamo"]["verification_scope"])
        self.assertIn("Dataset Partitioning: Consistent Hashing",
                      sources["src.cassandra"]["verification_scope"])
        self.assertIn("Vnodes", sources["src.riak"]["verification_scope"])

    def test_alternative_keeps_synthesis_labels(self):
        alt = self.entry["technical_evidence"]["alternative"]
        self.assertEqual(alt["binding"]["source_id"], "src.cassandra")
        self.assertIn("Only the modulo contrast is source-bound here", self.owner_norm)
        self.assertIn("Tycho's rule is stricter than any single source", self.owner_norm)

    def test_historical_review_is_not_bound_to_current_page(self):
        records = json.loads(RECORDS.read_text(encoding="utf-8"))["records"]
        record = next(item for item in records if item["pattern_id"] == PATTERN)
        self.assertEqual(record["re_review"]["reviewed_page_sha256"], HISTORICAL_PAGE)
        packets = json.loads(PACKETS.read_text(encoding="utf-8"))["packets"]
        packet = next(item for item in packets if item["pattern_id"] == PATTERN)
        self.assertEqual(packet["packet_status"], "page-changed-since-review")
        self.assertEqual(packet["page_sha256"], HISTORICAL_PAGE)

    def test_promotion_record_matches_current_artifacts(self):
        promotions = json.loads(
            PROMOTIONS.read_text(encoding="utf-8"))["promotions"]
        promotion = next(item for item in promotions
                         if item["pattern_id"] == PATTERN)
        batches = json.loads(CARDS.read_text(encoding="utf-8"))["batches"]
        card_path = next(entry["card_path"]
                         for batch in batches for entry in batch["entries"]
                         if entry["pattern_id"] == PATTERN)
        self.assertEqual(promotion["owner_page_sha256"], sha(self.entry["owner"]["path"]))
        self.assertEqual(promotion["card_sha256"], sha(card_path))
        report = ROOT / promotion["report_path"]
        self.assertEqual(promotion["report_sha256"], sha(promotion["report_path"]))
        self.assertTrue(report.is_file())


if __name__ == "__main__":
    unittest.main()
