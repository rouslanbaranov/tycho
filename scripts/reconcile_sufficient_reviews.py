#!/usr/bin/env python3
"""Reconcile sufficient-candidate review records with their cited reports.

Reads the candidate ledger, the machine-readable review records and the two review
reports. Produces a deterministic per-record reconciliation and summary. It never
promotes an entry, edits a page, relaxes a validator or creates a review.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "edition/patterns/sufficient-candidates.v1.json"
RECORDS = ROOT / "edition/patterns/sufficient-review-records.v1.json"
BATCH = ROOT / "authoring/INDEPENDENT-AGENT-REVIEW-BATCH-2026-10-22.md"
SUFFICIENT = ROOT / (
    "authoring/INDEPENDENT-AGENT-REVIEW-SUFFICIENT-CANDIDATES_2026-10-22.md")
PROTOCOL = ROOT / "authoring/SUFFICIENT-COVERAGE-PROTOCOL_2026-10-22.md"
OUTPUT = ROOT / "edition/patterns/sufficient-review-reconciliation.v1.json"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalize_name(value):
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def parse_batch_report(text):
    """Parse '### Name' followed by 'Verdict: **verdict**'."""
    verdicts = {}
    current = None
    for line in text.splitlines():
        heading = re.match(r"^### (.+)$", line)
        if heading:
            current = normalize_name(heading.group(1))
            continue
        verdict = re.match(r"^Verdict:\s*\*\*(pass-with-findings|pass|reject)\*\*", line)
        if verdict and current:
            verdicts[current] = verdict.group(1)
            current = None
    return verdicts


def parse_sufficient_report(text):
    """Parse '## Name — verdict' headings."""
    verdicts = {}
    for line in text.splitlines():
        heading = re.match(
            r"^## (.+?) — (pass-with-findings|pass|reject)$", line)
        if heading:
            verdicts[normalize_name(heading.group(1))] = heading.group(2)
    return verdicts


def parse_protocol_counts(text):
    counts = {}
    for line in text.splitlines():
        match = re.match(
            r"^\| (Pass|Pass with findings|Reject) \| (\d+) \|$", line)
        if match:
            key = match.group(1).casefold().replace(" ", "_")
            counts[key] = int(match.group(2))
    return counts


def find_report_verdict(name, verdicts):
    key = normalize_name(name)
    if key in verdicts:
        return verdicts[key], "exact"
    candidates = [heading for heading in verdicts
                  if heading.startswith(key + " ") or key.startswith(heading + " ")]
    if len(candidates) == 1:
        return verdicts[candidates[0]], "alias"
    return None, "missing"


def derive_state(record):
    verdict = record["verdict"]
    remediated = record.get("remediated", False)
    re_reviewed = record.get("re_reviewed", False)
    re_review = record.get("re_review") or {}
    if verdict == "pass":
        if record.get("findings", 0) == 0 and not remediated and not re_reviewed:
            return "initial-pass-no-findings"
        if re_reviewed and re_review.get("verdict") == "pass":
            return "promoted-after-remediation"
        return "pass-without-review-evidence"
    if re_reviewed and re_review.get("verdict") == "pass-with-findings":
        return "residual-findings-after-re-review"
    if remediated and not re_reviewed:
        return "remediated-needs-re-review"
    if not remediated and not re_reviewed:
        return "needs-remediation-and-re-review"
    return "other"


def reconcile(candidates, records, batch_text, sufficient_text, protocol_text):
    catalog = {entry["pattern_id"]: entry for entry in candidates["entries"]}
    batch = parse_batch_report(batch_text)
    sufficient = parse_sufficient_report(sufficient_text)
    protocol = parse_protocol_counts(protocol_text)
    rows = []
    for record in records["records"]:
        entry = catalog.get(record["pattern_id"])
        if entry is None:
            raise ValueError("review record without candidate: " + record["pattern_id"])
        use_sufficient = "SUFFICIENT-CANDIDATES" in record["report_path"]
        report = sufficient if use_sufficient else batch
        report_verdict, match_kind = find_report_verdict(entry["catalog_name"], report)
        if match_kind == "missing":
            report_match = "missing"
        elif report_verdict != record["verdict"]:
            report_match = "verdict-mismatch"
        else:
            report_match = match_kind
        state = derive_state(record)
        issues = []
        if report_match == "missing":
            issues.append("report-missing")
        elif report_match == "verdict-mismatch":
            issues.append("report-verdict-mismatch")
        elif report_match == "alias":
            issues.append("report-name-alias")
        if record.get("re_reviewed"):
            issues.append("re-review-without-report")
        if state in {"residual-findings-after-re-review",
                     "remediated-needs-re-review",
                     "needs-remediation-and-re-review",
                     "pass-without-review-evidence"}:
            issues.append(state)
        re_review = record.get("re_review") or {}
        rows.append({
            "pattern_id": record["pattern_id"],
            "catalog_name": entry["catalog_name"],
            "owner_path": entry["owner_path"],
            "current_verdict": record["verdict"],
            "findings": record.get("findings", 0),
            "remediated": record.get("remediated", False),
            "re_reviewed": record.get("re_reviewed", False),
            "re_review_verdict": re_review.get("verdict"),
            "re_review_findings": re_review.get("findings"),
            "report_path": record["report_path"],
            "report_verdict": report_verdict,
            "report_name_match": match_kind,
            "report_match": report_match,
            "derived_state": state,
            "issues": sorted(issues),
        })

    from collections import Counter
    current = Counter(row["current_verdict"] for row in rows)
    states = Counter(row["derived_state"] for row in rows)
    matches = Counter(row["report_match"] for row in rows)
    name_matches = Counter(row["report_name_match"] for row in rows)
    re_reviewed = [row for row in rows if row["re_reviewed"]]
    reject_conflicts = [row for row in rows if row["report_verdict"] == "reject"]
    supported = [row for row in rows
                 if row["report_match"] in {"exact", "alias"}]
    promoted_from_findings = sum(
        1 for row in rows if row["derived_state"] == "promoted-after-remediation"
        and row["report_verdict"] == "pass-with-findings")
    summary = {
        "records": len(rows),
        "current_verdicts": dict(sorted(current.items())),
        "derived_states": dict(sorted(states.items())),
        "report_matches": dict(sorted(matches.items())),
        "report_name_matches": dict(sorted(name_matches.items())),
        "current_verdicts_supported_by_cited_report": len(supported),
        "verdict_mismatches": matches["verdict-mismatch"],
        "promoted_from_findings": promoted_from_findings,
        "report_reject_conflicts": len(reject_conflicts),
        "re_reviewed": len(re_reviewed),
        "re_review_without_separate_report": sum(
            1 for row in re_reviewed if "re-review-without-report" in row["issues"]),
        "protocol_counts": dict(sorted(protocol.items())),
        "protocol_divergence": {
            "pass_delta": current.get("pass", 0) - protocol.get("pass", 0),
            "pass_with_findings_delta": (
                current.get("pass-with-findings", 0)
                - protocol.get("pass_with_findings", 0)),
        },
    }
    return {"summary": summary, "rows": rows}


def build_output(base):
    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    records = json.loads(RECORDS.read_text(encoding="utf-8"))
    batch_text = BATCH.read_text(encoding="utf-8")
    sufficient_text = SUFFICIENT.read_text(encoding="utf-8")
    protocol_text = PROTOCOL.read_text(encoding="utf-8")
    result = reconcile(candidates, records, batch_text, sufficient_text, protocol_text)
    return {
        "schema_version": 1,
        "scope": ("Read-only reconciliation of sufficient-candidate review records "
                  "against cited reports. Not a review, sufficiency claim or promotion."),
        "sources": [
            {"path": path.relative_to(ROOT).as_posix(), "sha256": digest(path)}
            for path in (CANDIDATES, RECORDS, BATCH, SUFFICIENT, PROTOCOL)
        ],
        "summary": result["summary"],
        "records": result["rows"],
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=OUTPUT)
    args = ap.parse_args(argv)
    payload = build_output(None)
    args.output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
