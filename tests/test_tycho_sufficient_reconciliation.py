"""Offline tests for the sufficient-candidate review reconciliation."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import reconcile_sufficient_reviews as reconciliation  # noqa: E402

BATCH = "### Alpha\nVerdict: **pass-with-findings**\n"
SUFFICIENT = "## Beta — pass\n"
PROTOCOL = "| Pass | 1 |\n| Pass with findings | 1 |\n| Reject | 0 |\n"


def candidate(pid, name):
    return {"pattern_id": pid, "catalog_name": name, "owner_path": "book/a.md"}


def record(pid, verdict, report_path, findings=0, remediated=False,
           re_reviewed=False, re_review=None):
    return {
        "pattern_id": pid,
        "verdict": verdict,
        "report_path": report_path,
        "findings": findings,
        "remediated": remediated,
        "re_reviewed": re_reviewed,
        "re_review": re_review,
    }


class ReportParsingTests(unittest.TestCase):
    def test_batch_and_sufficient_parsers(self):
        self.assertEqual(reconciliation.parse_batch_report(BATCH),
                         {"alpha": "pass-with-findings"})
        self.assertEqual(reconciliation.parse_sufficient_report(SUFFICIENT),
                         {"beta": "pass"})
        self.assertEqual(reconciliation.parse_protocol_counts(PROTOCOL),
                         {"pass": 1, "pass_with_findings": 1, "reject": 0})

    def test_unique_alias_match_and_missing(self):
        reports = {"cache aside": "pass"}
        self.assertEqual(
            reconciliation.find_report_verdict("Cache-Aside / Lazy Loading", reports),
            ("pass", "alias"))
        self.assertEqual(
            reconciliation.find_report_verdict("Unrelated Name", reports),
            (None, "missing"))


class StateTests(unittest.TestCase):
    def test_state_derivation(self):
        self.assertEqual(reconciliation.derive_state(record(
            "tycho.pattern.a", "pass", BATCH, findings=0)), "initial-pass-no-findings")
        self.assertEqual(reconciliation.derive_state(record(
            "tycho.pattern.a", "pass", BATCH, findings=2, remediated=True,
            re_reviewed=True, re_review={"verdict": "pass", "findings": 0})),
            "promoted-after-remediation")
        self.assertEqual(reconciliation.derive_state(record(
            "tycho.pattern.a", "pass-with-findings", BATCH, findings=2,
            remediated=True)), "remediated-needs-re-review")
        self.assertEqual(reconciliation.derive_state(record(
            "tycho.pattern.a", "pass-with-findings", BATCH, findings=2)),
            "needs-remediation-and-re-review")
        self.assertEqual(reconciliation.derive_state(record(
            "tycho.pattern.a", "pass-with-findings", BATCH, findings=2,
            re_reviewed=True, re_review={"verdict": "pass-with-findings", "findings": 2})),
            "residual-findings-after-re-review")
        self.assertEqual(reconciliation.derive_state(record(
            "tycho.pattern.a", "pass-with-findings", BATCH, findings=2,
            re_reviewed=True, re_review={"verdict": "pass-with-findings", "findings": 0,
                                         "verification_gap": "page not re-read"})),
            "page-unverified-after-delta")
        self.assertEqual(reconciliation.derive_state(record(
            "tycho.pattern.a", "reject", BATCH, findings=2, re_reviewed=True,
            re_review={"verdict": "reject", "report_path": "report.md"})),
            "rejected-after-review")

    def test_mismatch_and_alias_are_reported(self):
        candidates = {"entries": [candidate("tycho.pattern.alpha", "Alpha"),
                                  candidate("tycho.pattern.beta", "Cache-Aside / Lazy Loading")]}
        records = {"records": [
            record("tycho.pattern.alpha", "pass", "batch.md"),
            record("tycho.pattern.beta", "pass", "sufficient.md"),
        ]}
        result = reconciliation.reconcile(
            candidates, records,
            BATCH + "### Cache-Aside\nVerdict: **pass**\n",
            SUFFICIENT, PROTOCOL)
        rows = {row["pattern_id"]: row for row in result["rows"]}
        self.assertEqual(rows["tycho.pattern.alpha"]["report_match"], "verdict-mismatch")
        self.assertIn("report-verdict-mismatch", rows["tycho.pattern.alpha"]["issues"])
        self.assertEqual(rows["tycho.pattern.beta"]["report_name_match"], "alias")
        self.assertIn("report-name-alias", rows["tycho.pattern.beta"]["issues"])
        self.assertEqual(result["summary"]["records"], 2)


class AuditIntegrationTests(unittest.TestCase):
    def test_records_reference_phase_a_v3(self):
        records = json.loads((
            ROOT / "edition/patterns/sufficient-review-records.v1.json"
        ).read_text())["records"]
        owners = json.loads((
            ROOT / "edition/patterns/owner-units.v1.json"
        ).read_text())["entries"]
        owner_path = {item["pattern_id"]: item["owner"]["path"] for item in owners}
        reports = {
            "authoring/INDEPENDENT-AGENT-REREVIEW-2026-10-22-phase-a-v3.md",
            "authoring/INDEPENDENT-AGENT-REREVIEW-2026-10-23-phase-a-gap-v6.md",
        }
        phase_a = [r for r in records
                   if (r.get("re_review") or {}).get("report_path") in reports]
        self.assertEqual(len(phase_a), 52)
        self.assertEqual(sum(1 for r in phase_a if r["verdict"] == "pass"), 52)
        self.assertEqual(sum(1 for r in phase_a
                               if r["verdict"] == "pass-with-findings"), 0)
        for record in phase_a:
            path = ROOT / owner_path[record["pattern_id"]]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),
                             record["re_review"]["page_sha256"])


class CommittedLedgerTests(unittest.TestCase):
    def test_committed_ledger_counts(self):
        ledger = json.loads((
            ROOT / "edition/patterns/sufficient-review-reconciliation.v1.json"
        ).read_text())
        summary = ledger["summary"]
        self.assertEqual(summary["records"], 145)
        self.assertEqual(summary["current_verdicts"],
                         {"pass": 138, "pass-with-findings": 7})
        self.assertEqual(summary["verdict_mismatches"], 123)
        self.assertEqual(summary["re_reviewed"], 145)
        self.assertEqual(summary["re_review_with_separate_report"], 145)
        self.assertEqual(summary["re_review_without_separate_report"], 0)
        self.assertEqual(summary["report_reject_conflicts"], 6)
        self.assertEqual(summary["derived_states"].get("needs-remediation-and-re-review", 0), 0)
        self.assertEqual(summary["derived_states"].get("remediated-needs-re-review", 0), 0)
        self.assertEqual(summary["derived_states"].get("page-unverified-after-delta", 0), 0)
        self.assertEqual(summary["derived_states"].get("residual-findings-after-re-review", 0), 7)
        self.assertEqual(summary["derived_states"].get("rejected-after-review", 0), 0)
        self.assertEqual(summary["derived_states"]["promoted-after-remediation"], 138)
        self.assertEqual(summary["report_name_matches"]["alias"], 1)

    def test_generation_is_deterministic(self):
        first = reconciliation.build_output(None)
        second = reconciliation.build_output(None)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
