#!/usr/bin/env python3
"""Build independent re-review packets for re-reviewed pattern entries.

Reads the reconciliation ledger, review records, candidates, route index and the
two review reports. Produces one packet per record that claims a re-review. Every
packet contains evidence and a blank verdict template; it never fills a reviewer,
verdict or findings.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

import reconcile_sufficient_reviews as reconciliation

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "edition/patterns/sufficient-candidates.v1.json"
RECORDS = ROOT / "edition/patterns/sufficient-review-records.v1.json"
RECON = ROOT / "edition/patterns/sufficient-review-reconciliation.v1.json"
ROUTE = ROOT / "generated/route-index.v1.json"
BATCH = ROOT / "authoring/INDEPENDENT-AGENT-REVIEW-BATCH-2026-10-22.md"
SUFFICIENT = ROOT / (
    "authoring/INDEPENDENT-AGENT-REVIEW-SUFFICIENT-CANDIDATES_2026-10-22.md")
REBINDS = ROOT / "edition/patterns/section-rebinds.v1.json"
OUTPUT_JSON = ROOT / "edition/patterns/sufficient-rereview-packets.v1.json"
OUTPUT_MD = ROOT / "authoring/SUFFICIENT-REREVIEW-PACKETS_2026-10-22.md"

CHECKS = [
    "Read the exact owner section and atlas card; do not rely on the summary.",
    "Check mechanism, invariant, failure/recovery, alternatives and limits.",
    "Check every material source claim against the cited public source scope.",
    "Record the exact page SHA-256 and every finding with severity.",
    "Confirm you did not author the change under review.",
    "Do not mark pass while a material finding remains.",
]
TEMPLATE = {
    "reviewer": None,
    "relationship": None,
    "reviewed_at": None,
    "page_sha256": None,
    "checks": {name: None for name in (
        "mechanism", "invariant", "failure_recovery", "alternatives",
        "limits", "sources")},
    "verdict": None,
    "findings": [],
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_batch_sections(text):
    sections = {}
    current = None
    lines = []
    for line in text.splitlines():
        heading = re.match(r"^### (.+)$", line)
        if heading:
            if current is not None:
                sections[current] = "\n".join(lines).strip()
            current = reconciliation.normalize_name(heading.group(1))
            lines = [line]
            continue
        if current is not None:
            lines.append(line)
    if current is not None:
        sections[current] = "\n".join(lines).strip()
    return sections


def parse_sufficient_sections(text):
    sections = {}
    current = None
    lines = []
    for line in text.splitlines():
        heading = re.match(
            r"^## (.+?) — (pass-with-findings|pass|reject)$", line)
        if heading:
            if current is not None:
                sections[current] = "\n".join(lines).strip()
            current = reconciliation.normalize_name(heading.group(1))
            lines = [line]
            continue
        if current is not None:
            lines.append(line)
    if current is not None:
        sections[current] = "\n".join(lines).strip()
    return sections


def find_section(name, sections):
    key = reconciliation.normalize_name(name)
    if key in sections:
        return sections[key], "exact"
    candidates = [heading for heading in sections
                  if heading.startswith(key + " ") or key.startswith(heading + " ")]
    if len(candidates) == 1:
        return sections[candidates[0]], "alias"
    return None, "missing"


def build_packet(candidate, record, recon_row, sections, route_docs, sections_source=None, rebind=None):
    if sections_source is None:
        sections_source = record["report_path"]
    page = route_docs.get(candidate["owner_path"])
    page_sha = page["sha256"] if page else None
    re_review = record.get("re_review") or {}
    delta = record.get("delta_review") or {}
    rebind = rebind or {}
    reviewed_sha = re_review.get("reviewed_page_sha256") or page_sha
    if delta.get("verdict") == "pass" and delta.get("page_sha256"):
        reviewed_sha = delta["page_sha256"]
    disk_sha = None
    if page is not None:
        path = ROOT / candidate["owner_path"]
        if path.is_file():
            disk_sha = digest(path)
    if rebind.get("page_sha256") == disk_sha:
        reviewed_sha = disk_sha
    section, _ = find_section(candidate["catalog_name"], sections)
    section_source = sections_source
    if section is None and re_review.get("report_path"):
        report_path = ROOT / re_review["report_path"]
        if report_path.is_file():
            alternate = parse_batch_sections(report_path.read_text(encoding="utf-8"))
            alternate_section, _ = find_section(candidate["catalog_name"], alternate)
            if alternate_section is not None:
                section = alternate_section
                section_source = re_review["report_path"]
    if page is None:
        status = "owner-page-missing"
    elif disk_sha is None or disk_sha != page_sha:
        status = "hash-mismatch"
    elif disk_sha != reviewed_sha:
        status = "page-changed-since-review"
    elif section is None:
        status = "report-section-missing"
    elif re_review.get("report_path"):
        status = "reviewed-by-independent-agent"
    else:
        status = "ready-for-independent-rereview"
    current_verdict = delta.get("verdict") or record["verdict"]
    return {
        "pattern_id": candidate["pattern_id"],
        "catalog_name": candidate["catalog_name"],
        "owner_path": candidate["owner_path"],
        "owner_heading": candidate["owner_heading"],
        "source_read": candidate["source_read"],
        "page_sha256": reviewed_sha,
        "current_page_sha256": page_sha,
        "disk_sha256": disk_sha,
        "packet_status": status,
        "current_verdict": current_verdict,
        "original_findings": record.get("findings", 0),
        "remediated": record.get("remediated", False),
        "re_reviewed": record.get("re_reviewed", False),
        "re_review_verdict": re_review.get("verdict"),
        "re_review_findings": re_review.get("findings"),
        "derived_state": recon_row["derived_state"],
        "report_path": record["report_path"],
        "report_section_source": section_source,
        "report_section_inherited": section_source != record["report_path"],
        "report_verdict": recon_row["report_verdict"],
        "report_match": recon_row["report_match"],
        "report_section": section,
        "rebind_report_path": rebind.get("report_path"),
        "review_checklist": CHECKS,
        "verdict_template": {**TEMPLATE,
                             "page_sha256": reviewed_sha,
                             "checks": dict(TEMPLATE["checks"])},
    }


def build_packets():
    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))["entries"]
    by_id = {entry["pattern_id"]: entry for entry in candidates}
    records = json.loads(RECORDS.read_text(encoding="utf-8"))["records"]
    recon = json.loads(RECON.read_text(encoding="utf-8"))
    recon_rows = {row["pattern_id"]: row for row in recon["records"]}
    route = json.loads(ROUTE.read_text(encoding="utf-8"))
    route_docs = {doc["path"]: doc for doc in route["documents"]}
    rebinds = {}
    if REBINDS.is_file():
        rebinds = {item["pattern_id"]: item for item in json.loads(REBINDS.read_text(encoding="utf-8"))["rebinds"]}
    batch_sections = parse_batch_sections(BATCH.read_text(encoding="utf-8"))
    sufficient_sections = parse_sufficient_sections(
        SUFFICIENT.read_text(encoding="utf-8"))
    packets = []
    for record in records:
        if not record.get("re_reviewed"):
            continue
        candidate = by_id[record["pattern_id"]]
        use_sufficient = "SUFFICIENT-CANDIDATES" in record["report_path"]
        sections = sufficient_sections if use_sufficient else batch_sections
        sections_source = (SUFFICIENT if use_sufficient else BATCH).relative_to(ROOT).as_posix()
        packets.append(build_packet(
            candidate, record, recon_rows[record["pattern_id"]],
            sections, route_docs, sections_source, rebinds.get(record["pattern_id"])))
    packets.sort(key=lambda item: item["catalog_name"].casefold())
    status_counts = {}
    for packet in packets:
        status_counts[packet["packet_status"]] = (
            status_counts.get(packet["packet_status"], 0) + 1)
    summary = {
        "packets": len(packets),
        "promoted": sum(1 for p in packets
                        if p["derived_state"] == "promoted-after-remediation"),
        "residual": sum(1 for p in packets
                        if p["derived_state"] == "residual-findings-after-re-review"),
        "page_unverified": sum(1 for p in packets
                               if p["derived_state"] == "page-unverified-after-delta"),
        "unique_owner_pages": len({p["owner_path"] for p in packets}),
        "packet_statuses": dict(sorted(status_counts.items())),
        "ready": status_counts.get("ready-for-independent-rereview", 0),
        "reviewed": status_counts.get("reviewed-by-independent-agent", 0),
        "rejected": sum(1 for p in packets
                        if p["derived_state"] == "rejected-after-review"),
    }
    sources = [
        {"path": path.relative_to(ROOT).as_posix(), "sha256": digest(path)}
        for path in (CANDIDATES, RECORDS, RECON, ROUTE, BATCH, SUFFICIENT)
    ]
    return {"schema_version": 1, "scope": (
        "Independent re-review packets for records that claim a re-review. "
        "Evidence only; no reviewer or verdict is filled."),
        "sources": sources, "summary": summary, "packets": packets}


def render_markdown(payload):
    summary = payload["summary"]
    lines = [
        "# Independent re-review packets — 2026-10-22",
        "",
        "> Issue [#304](https://github.com/rouslanbaranov/tycho/issues/304), child of #228.",
        "> These packets were the evidence input to the independent agent re-review. Their",
        "> verdict templates remain blank; verdicts live in the separate re-review report.",
        "",
        "## Summary",
        "",
        "| Measure | Value |",
        "|---|---:|",
        "| Packets | " + str(summary["packets"]) + " |",
        "| Promoted after remediation | " + str(summary["promoted"]) + " |",
        "| Residual findings after re-review | " + str(summary["residual"]) + " |",
        "| Unique owner pages | " + str(summary["unique_owner_pages"]) + " |",
        "| Ready for independent re-review | " + str(summary["ready"]) + " |",
        "| Reviewed by independent agent | " + str(summary.get("reviewed", 0)) + " |",
        "| Rejected after review | " + str(summary.get("rejected", 0)) + " |",
        "",
        "Packet statuses: " + json.dumps(summary["packet_statuses"], sort_keys=True) + ".",
        "",
        "## Review procedure",
        "",
        "1. Confirm you did not author the change under review.",
        "2. Read the exact owner section and atlas card.",
        "3. Check mechanism, invariant, failure/recovery, alternatives, limits and sources.",
        "4. Record the page SHA-256 and every finding with severity.",
        "5. Fill the verdict template as pass, pass-with-findings or reject.",
        "6. Store the signed packet as a separate report and rerun the reconciliation.",
        "",
        "## Packets",
        "",
        "Each packet contains the owner path, page SHA-256, report section, checklist and a",
        "blank verdict template in the machine-readable file.",
    ]
    for packet in payload["packets"]:
        lines.extend([
            "",
            "- **" + packet["catalog_name"] + "**",
            "  Current: " + packet["current_verdict"] + "; re-review: "
            + str(packet["re_review_verdict"]) + "; report: "
            + str(packet["report_verdict"]) + ".",
            "  Status: " + packet["packet_status"] + ".",
        ])
    lines.extend([
        "",
        "## Limits",
        "",
        "- The packet does not prove the section is correct or sufficient.",
        "- The blank template must be completed by an independent reviewer.",
        "- Human per-page review and owner acceptance remain separate gates.",
        "- No page, record or validator is changed by this packet.",
        "",
        "Machine-readable packets:",
        "[sufficient-rereview-packets.v1.json](../edition/patterns/sufficient-rereview-packets.v1.json).",
    ])
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", type=Path, default=OUTPUT_JSON)
    ap.add_argument("--markdown", type=Path, default=OUTPUT_MD)
    args = ap.parse_args(argv)
    payload = build_packets()
    args.json.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.markdown.write_text(render_markdown(payload), encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
