#!/usr/bin/env python3
"""Build or check the independent re-review scope manifest.

The manifest is a snapshot index, not a review or a promotion. It lists the
52 previously audited entries and the 93 deferred entries with current page
hashes, owner/card bindings and read source units.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path("edition/patterns/independent-rereview-scope-2026-10-22.v2.json")
PRIOR_AUDIT = Path("edition/patterns/independent-agent-rereview-2026-10-22.v1.json")
RECORDS = Path("edition/patterns/sufficient-review-records.v1.json")
RECON = Path("edition/patterns/sufficient-review-reconciliation.v1.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
OWNER_UNITS = Path("edition/patterns/owner-units.v1.json")
CARDS = Path("edition/patterns/card-batches.v1.json")
SOURCE_PLAN = Path("edition/patterns/source-plan.v1.json")
DELIVERY = Path("edition/patterns/delivery-evidence.v1.json")
V11 = Path("book/volumes/v11-pattern-atlas")


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def chapter_map():
    mapping = {}
    for path in sorted(V11.iterdir()):
        if not path.is_dir():
            continue
        match = re.match(r"c(\d{2})-", path.name)
        if match:
            mapping["V11/C" + match.group(1)] = path.name
    return mapping


def heading_slug(text):
    value = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"\s", "-", value.strip())


def norm_heading(text):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def build():
    audit = load(PRIOR_AUDIT)
    records = load(RECORDS)["records"]
    recon = {r["pattern_id"]: r for r in load(RECON)["records"]}
    owners = {r["pattern_id"]: r for r in load(OWNER_UNITS)["entries"]}
    plan = {r["pattern_id"]: r for r in load(SOURCE_PLAN)["entries"]}
    registry = {r["id"]: r for r in load(REGISTRY)["patterns"]}
    delivery = load(DELIVERY)
    chapters = chapter_map()
    card_map = {}
    for batch in load(CARDS)["batches"]:
        chapter = batch["chapter"]
        directory = chapters.get(chapter)
        for entry in batch["entries"]:
            card_path = entry.get("card_path") or (str(V11 / directory / "README.md") if directory else None)
            anchor = entry["atlas_section"]
            if card_path:
                card_text = (ROOT / card_path).read_text(encoding="utf-8")
                name = registry[entry["pattern_id"]]["catalog_name"]
                headings = [line[4:].strip() for line in card_text.splitlines()
                            if line.startswith("### ")]
                heading = next((item for item in headings
                                if norm_heading(item) == norm_heading(name)), None)
                if heading is None:
                    heading = next((item for item in headings
                                    if heading_slug(item).replace("--", "-")
                                    == anchor.replace("--", "-")), None)
                if heading:
                    anchor = heading_slug(heading)
            card_map[entry["pattern_id"]] = {
                "card_path": card_path,
                "card_anchor": anchor,
            }
    audited = {p["pattern_id"] for p in audit["packets"]}
    phase_a = []
    for packet in audit["packets"]:
        pid = packet["pattern_id"]
        record = next(r for r in records if r["pattern_id"] == pid)
        owner = owners[pid]
        card = card_map.get(pid, {"card_path": None, "card_anchor": None})
        units = []
        for unit in plan[pid]["required_units"]:
            if unit["status"] != "read":
                continue
            units.append({
                "source_id": unit["source_id"],
                "unit": unit["unit"],
                "read_record_id": unit["read_record_id"],
                "sections": unit["sections"],
            })
        phase_a.append({
            "pattern_id": pid,
            "catalog_name": packet["catalog_name"],
            "prior_verdict": packet["audit_verdict"],
            "prior_finding_ids": packet["finding_ids"],
            "prior_page_sha256": packet["page_sha256"],
            "current_page_sha256": sha(owner["owner"]["path"]),
            "current_page_path": owner["owner"]["path"],
            "owner_anchor": owner["owner"]["anchor"],
            "owner_heading": owner["owner"]["heading"],
            "owner_line": owner["owner"]["line"],
            "card_path": card["card_path"],
            "card_anchor": card["card_anchor"],
            "record_verdict": record["verdict"],
            "record_findings": record["findings"],
            "record_report_path": record["report_path"],
            "re_review_verdict": (record.get("re_review") or {}).get("verdict"),
            "re_review_report_path": (record.get("re_review") or {}).get("report_path"),
            "source_units": units,
        })
    phase_b = []
    for record in records:
        pid = record["pattern_id"]
        if pid in audited:
            continue
        owner = owners[pid]
        card = card_map.get(pid, {"card_path": None, "card_anchor": None})
        state = recon[pid]["derived_state"]
        units = []
        for unit in plan[pid]["required_units"]:
            if unit["status"] != "read":
                continue
            units.append({
                "source_id": unit["source_id"],
                "unit": unit["unit"],
                "read_record_id": unit["read_record_id"],
                "sections": unit["sections"],
            })
        phase_b.append({
            "pattern_id": pid,
            "catalog_name": registry[pid]["catalog_name"],
            "record_verdict": record["verdict"],
            "record_findings": record["findings"],
            "remediated": record["remediated"],
            "re_reviewed": record["re_reviewed"],
            "derived_state": state,
            "current_page_sha256": sha(owner["owner"]["path"]),
            "current_page_path": owner["owner"]["path"],
            "owner_anchor": owner["owner"]["anchor"],
            "owner_heading": owner["owner"]["heading"],
            "owner_line": owner["owner"]["line"],
            "card_path": card["card_path"],
            "card_anchor": card["card_anchor"],
            "source_units": units,
        })
    a_counts = {}
    for entry in phase_a:
        a_counts[entry["prior_verdict"]] = a_counts.get(entry["prior_verdict"], 0) + 1
    b_counts = {}
    for entry in phase_b:
        b_counts[entry["derived_state"]] = b_counts.get(entry["derived_state"], 0) + 1
    return {
        "schema_version": 1,
        "generated_at": "2026-10-22",
        "content_commit": delivery["source_commit"],
        "prior_audit_head": audit["head"],
        "prior_audit_report": "authoring/INDEPENDENT-AGENT-REREVIEW-2026-10-22.md",
        "integration_report": "authoring/SUFFICIENT-REVIEW-INTEGRATION_2026-10-22.md",
        "scope": "52 mandatory re-reviews at current page hashes and 93 deferred entries",
        "counts": {
            "records": len(records),
            "phase_a": len(phase_a),
            "phase_b": len(phase_b),
            "phase_a_verdicts": a_counts,
            "phase_b_states": b_counts,
        },
        "phase_a": phase_a,
        "phase_b": phase_b,
        "nonclaims": [
            "Index only; not a review, promotion, human review or owner acceptance.",
            "Page hashes are a snapshot; recompute them at the actual hand-off HEAD.",
            "Phase B entries were not in the 52-packet audit.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    path = ROOT / OUT
    if args.write:
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
        print(json.dumps(payload["counts"], indent=2))
        return
    if not path.is_file():
        raise SystemExit("scope-manifest-missing")
    committed = json.loads(path.read_text(encoding="utf-8"))
    if committed != payload:
        raise SystemExit("scope-manifest-stale")
    print(json.dumps(payload["counts"], indent=2))
    print("PASS: scope manifest current")


if __name__ == "__main__":
    main()
