"""Offline tests for independent re-review packet generation."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_rereview_packets as packets  # noqa: E402

CANDIDATES = json.loads(
    (ROOT / "edition/patterns/sufficient-candidates.v1.json").read_text())["entries"]
RECORDS = json.loads(
    (ROOT / "edition/patterns/sufficient-review-records.v1.json").read_text())["records"]


class SectionParsingTests(unittest.TestCase):
    def test_batch_and_sufficient_sections(self):
        batch = ("### Alpha\nVerdict: **pass**\n- finding one\n"
                 "### Beta\nVerdict: **reject**\n- finding two\n")
        sections = packets.parse_batch_sections(batch)
        self.assertIn("alpha", sections)
        self.assertIn("finding one", sections["alpha"])
        self.assertIn("beta", sections)

        sufficient = ("## Alpha — pass\nOriginal finding one.\n"
                      "## Beta — pass-with-findings\nOriginal finding two.\n")
        sections = packets.parse_sufficient_sections(sufficient)
        self.assertEqual(set(sections), {"alpha", "beta"})
        self.assertIn("Original finding two", sections["beta"])

    def test_alias_section_resolution(self):
        section, kind = packets.find_section(
            "Cache-Aside / Lazy Loading", {"cache aside": "section text"})
        self.assertEqual(section, "section text")
        self.assertEqual(kind, "alias")


class PacketTests(unittest.TestCase):
    def setUp(self):
        record = next(r for r in RECORDS if r.get("re_reviewed"))
        # The synthetic route below pins the current page, so drop a historical
        # pin that would otherwise mark the fixture as changed since review.
        review = {key: value for key, value in record["re_review"].items()
                  if key != "reviewed_page_sha256"}
        self.record = {**record, "re_review": review}
        self.candidate = next(c for c in CANDIDATES
                              if c["pattern_id"] == record["pattern_id"])
        self.recon = {
            "derived_state": "promoted-after-remediation",
            "report_verdict": "pass",
            "report_match": "exact",
        }
        self.sections = {packets.reconciliation.normalize_name(
            self.candidate["catalog_name"]): "report section"}
        self.sha = packets.digest(ROOT / self.candidate["owner_path"])
        self.route = {self.candidate["owner_path"]: {"sha256": self.sha}}

    def test_reviewed_packet_has_no_filled_verdict(self):
        packet = packets.build_packet(
            self.candidate, self.record, self.recon, self.sections, self.route)
        self.assertEqual(packet["packet_status"], "reviewed-by-independent-agent")
        self.assertEqual(packet["page_sha256"], self.sha)
        template = packet["verdict_template"]
        self.assertIsNone(template["reviewer"])
        self.assertIsNone(template["verdict"])
        self.assertEqual(template["findings"], [])
        self.assertTrue(all(value is None for value in template["checks"].values()))

    def test_unreviewed_record_stays_ready(self):
        unreviewed = dict(self.record)
        unreviewed["re_review"] = {"verdict": "pass", "findings": 0}
        packet = packets.build_packet(
            self.candidate, unreviewed, self.recon, self.sections, self.route)
        self.assertEqual(packet["packet_status"],
                         "ready-for-independent-rereview")

    def test_hash_mismatch_and_missing_page(self):
        bad = {self.candidate["owner_path"]: {"sha256": "0" * 64}}
        packet = packets.build_packet(
            self.candidate, self.record, self.recon, self.sections, bad)
        self.assertEqual(packet["packet_status"], "hash-mismatch")
        packet = packets.build_packet(
            self.candidate, self.record, self.recon, self.sections, {})
        self.assertEqual(packet["packet_status"], "owner-page-missing")
        self.assertIsNone(packet["page_sha256"])

    def test_missing_report_section_is_blocked(self):
        packet = packets.build_packet(
            self.candidate, self.record, self.recon, {}, self.route)
        self.assertEqual(packet["packet_status"], "report-section-missing")


class CommittedPacketTests(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads((
            ROOT / "edition/patterns/sufficient-rereview-packets.v1.json"
        ).read_text())

    def test_committed_counts(self):
        summary = self.payload["summary"]
        self.assertEqual(summary["packets"], 145)
        self.assertEqual(summary["promoted"], 135)
        self.assertEqual(summary["residual"], 0)
        self.assertEqual(summary["page_unverified"], 0)
        self.assertEqual(summary["rejected"], 0)
        self.assertEqual(summary["unique_owner_pages"], 81)
        self.assertEqual(summary["ready"], 0)
        self.assertEqual(summary["reviewed"], 81)
        self.assertEqual(summary["awaiting_current_external_review"], 10)
        self.assertEqual(summary["packet_statuses"],
                         {"awaiting-current-external-review": 10,
                          "page-changed-since-review": 54,
                          "reviewed-by-independent-agent": 81})

    def test_no_packet_contains_a_verdict(self):
        for packet in self.payload["packets"]:
            template = packet["verdict_template"]
            self.assertIsNone(template["reviewer"])
            self.assertIsNone(template["verdict"])
            self.assertEqual(template["findings"], [])
            if packet["report_section"] is not None:
                self.assertTrue(packet["report_section"])
            self.assertTrue(packet["page_sha256"])

    def test_generation_is_deterministic(self):
        self.assertEqual(packets.build_packets(), self.payload)


if __name__ == "__main__":
    unittest.main()
