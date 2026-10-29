"""Regression guards for the 2026-10-29 B4 review remediation.

The B4 split suspended promotions for Self-Contained Service, Sidecar and
Ambassador. This test pins their current state to awaiting external review and
keeps the earlier passes only as historical evidence. It also pins the Ambassador
priority/binding fixes and the static-stability shared-page metadata.
"""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
THREE = (
    "tycho.pattern.self-contained-service",
    "tycho.pattern.sidecar",
    "tycho.pattern.ambassador",
)


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


class ReviewRecordTests(unittest.TestCase):
    def setUp(self):
        self.records = {r["pattern_id"]: r for r in load(
            "edition/patterns/sufficient-review-records.v1.json")["records"]}

    def test_three_await_current_external_review(self):
        for pattern_id in THREE:
            record = self.records[pattern_id]
            self.assertNotIn("verdict", record)
            self.assertNotIn("report_path", record)
            self.assertEqual(record["current_state"],
                             "awaiting-current-external-review")
            self.assertEqual(record["current_state_as_of"], "2026-10-29")
            self.assertEqual(record["historical_verdict"], "pass")

    def test_historical_passes_are_pinned(self):
        for pattern_id in THREE:
            record = self.records[pattern_id]
            reviews = record["historical_reviews"]
            self.assertTrue(reviews)
            self.assertTrue(any(item["verdict"] == "pass" for item in reviews))
            for item in reviews:
                self.assertEqual(item["status"],
                                 "historical-pinned-not-current")
                self.assertEqual(sha(item["report_path"]),
                                 item["report_sha256"])
                if "page_sha256" in item:
                    self.assertRegex(item["page_sha256"], r"^[0-9a-f]{64}$")

    def test_three_stay_partial_bounded(self):
        owners = {r["pattern_id"]: r for r in load(
            "edition/patterns/owner-units.v1.json")["entries"]}
        registry = {r["id"]: r for r in load(
            "edition/patterns/registry.v1.json")["patterns"]}
        promotions = {p["pattern_id"] for p in load(
            "edition/patterns/sufficient-promotions.v1.json")["promotions"]}
        for pattern_id in THREE:
            self.assertEqual(owners[pattern_id]["technical_coverage"],
                             "partial-bounded")
            self.assertEqual(owners[pattern_id]["decision_coverage"],
                             "partial-bounded")
            self.assertEqual(registry[pattern_id]["coverage"],
                             {"technical": "partial-bounded",
                              "decision": "partial-bounded",
                              "overall": "partial-bounded"})
            self.assertNotIn(pattern_id, promotions)


class DerivedArtifactTests(unittest.TestCase):
    def test_reconciliation_has_no_promoted_label(self):
        ledger = load("edition/patterns/sufficient-review-reconciliation.v1.json")
        rows = {r["pattern_id"]: r for r in ledger["records"]}
        for pattern_id in THREE:
            row = rows[pattern_id]
            self.assertEqual(row["current_verdict"],
                             "awaiting-current-external-review")
            self.assertEqual(row["derived_state"],
                             "awaiting-current-external-review")
            self.assertNotEqual(row["derived_state"],
                                "promoted-after-remediation")
            self.assertEqual(row["historical_verdict"], "pass")
            self.assertTrue(row["historical_reviews"])
        self.assertEqual(
            ledger["summary"]["derived_states"].get(
                "awaiting-current-external-review"), 3)
        self.assertEqual(
            ledger["summary"]["awaiting_current_external_review"], 3)

    def test_packets_await_review_with_blank_templates(self):
        payload = load("edition/patterns/sufficient-rereview-packets.v1.json")
        packets = {p["pattern_id"]: p for p in payload["packets"]}
        for pattern_id in THREE:
            packet = packets[pattern_id]
            self.assertEqual(packet["packet_status"],
                             "awaiting-current-external-review")
            self.assertEqual(packet["current_verdict"],
                             "awaiting-current-external-review")
            self.assertEqual(packet["derived_state"],
                             "awaiting-current-external-review")
            self.assertEqual(packet["historical_verdict"], "pass")
            self.assertTrue(packet["historical_reviews"])
            template = packet["verdict_template"]
            self.assertIsNone(template["reviewer"])
            self.assertIsNone(template["verdict"])
            self.assertEqual(template["findings"], [])
        self.assertEqual(
            payload["summary"]["awaiting_current_external_review"], 3)


class AmbassadorTests(unittest.TestCase):
    def test_card_priority_matches_registry_and_source_plan(self):
        card = (ROOT / "book/volumes/v11-pattern-atlas/c01-application-boundaries/"
                "ambassador.md").read_text(encoding="utf-8")
        priority = re.search(r"priority ([a-z]+)\.", card).group(1)
        registry = {r["id"]: r for r in load(
            "edition/patterns/registry.v1.json")["patterns"]}
        plan = {r["pattern_id"]: r for r in load(
            "edition/patterns/source-plan.v1.json")["entries"]}
        self.assertEqual(priority, "advanced")
        self.assertEqual(registry["tycho.pattern.ambassador"]["priority"],
                         priority)
        self.assertEqual(plan["tycho.pattern.ambassador"]["priority"],
                         priority)

    def test_bindings_use_the_page_introduction(self):
        owners = {r["pattern_id"]: r for r in load(
            "edition/patterns/owner-units.v1.json")["entries"]}
        evidence = owners["tycho.pattern.ambassador"]["technical_evidence"]
        for name in ("mechanism", "invariant"):
            binding = evidence[name]["binding"]
            self.assertEqual(binding["section"], "Ambassador pattern")
            self.assertNotEqual(binding["section"], "Solution")
        invariant = evidence["invariant"]["binding"]["quote"]
        self.assertIn("offload common client connectivity tasks", invariant)
        self.assertIn("monitoring, logging, routing", invariant)


class StaticStabilityTests(unittest.TestCase):
    def setUp(self):
        self.path = ("book/volumes/v08-delivery-deployment-and-recovery/"
                     "c03-vms-containers-orchestration-and-serverless/"
                     "static-stability.md")
        self.text = (ROOT / self.path).read_text(encoding="utf-8")

    def test_shared_page_is_two_patterns_and_records_removal(self):
        shared = load("edition/patterns/owner-units.v1.json")["shared_pages"]
        page = next(item for item in shared if item["path"] == self.path)
        self.assertEqual(page["pattern_count"], 2)
        self.assertEqual(page["pattern_ids"],
                         ["tycho.pattern.ambassador", "tycho.pattern.sidecar"])
        self.assertEqual(page["unit_count"], 2)
        self.assertIn("Two colocated-helper patterns", page["rationale"])
        self.assertIn("Immutable Infrastructure", page["rationale"])
        self.assertIn("2026-10-29", page["rationale"])
        self.assertNotIn("Three control-plane patterns", page["rationale"])

    def test_metadata_records_the_change_date(self):
        self.assertIn('updated_at: "2026-10-29"', self.text)
        reviewed = re.search(
            r'content_review:\n  status: "self-checked"\n'
            r'  reviewed_at: "([0-9-]+)"', self.text)
        self.assertEqual(reviewed.group(1), "2026-10-29")


if __name__ == "__main__":
    unittest.main()
