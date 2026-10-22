#!/usr/bin/env python3
"""Build or check the sufficient-coverage candidate triage.

This is a readiness report, not a sufficiency claim or review record.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from validate_pattern_owner_units import section_body

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "edition/patterns/sufficient-candidates.v1.json"
WORD_FLOOR = 120


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def build(root=ROOT):
    owner = load("edition/patterns/owner-units.v1.json")
    cards = load("edition/patterns/card-batches.v1.json")
    ledger = load("edition/patterns/reading-ledger.v1.json")
    records = {record["id"]: record for record in ledger["records"]}
    cardmap = {entry["pattern_id"]: entry
               for batch in cards["batches"] for entry in batch["entries"]}
    unit_counts = Counter((item["owner"]["path"], item["owner"]["anchor"])
                          for item in owner["entries"])
    rows = []
    for item in owner["entries"]:
        path = item["owner"]["path"]
        text = (root / path).read_text(encoding="utf-8")
        try:
            body = section_body(text, item["owner"]["heading"],
                                item["owner"]["level"], item["owner"]["line"])
        except ValueError:
            body = ""
        words = len(body.split())
        card = cardmap.get(item["pattern_id"])
        read = bool(card and records.get(card["ledger_record"], {}).get("status") == "read")
        dedicated = item["owner"]["unit_kind"] == "dedicated"
        shared = unit_counts[(path, item["owner"]["anchor"])] > 1
        if shared:
            status = "needs-dedicated-section"
        elif not dedicated:
            status = "needs-dedicated-section"
        elif words < WORD_FLOOR:
            status = "needs-deeper-section"
        elif not read:
            status = "needs-source-read"
        else:
            status = "candidate-for-independent-review"
        rows.append({
            "pattern_id": item["pattern_id"],
            "catalog_name": item["catalog_name"],
            "owner_path": path,
            "owner_heading": item["owner"]["heading"],
            "unit_kind": item["owner"]["unit_kind"],
            "section_words": words,
            "source_read": read,
            "technical_coverage": item["technical_coverage"],
            "decision_coverage": item["decision_coverage"],
            "status": status,
            "blockers": ([] if status == "candidate-for-independent-review" else [status])
                        + ["independent-review"],
        })
    counts = Counter(row["status"] for row in rows)
    return {
        "schema_version": 1,
        "generated_at": "2026-10-22",
        "scope": "Sufficient-coverage candidate triage. Not a sufficiency claim and not a review record.",
        "criteria": {
            "dedicated_unit": "owner unit heading names the pattern",
            "deep_section_words": WORD_FLOOR,
            "source_read": "reading-ledger record status read",
            "independent_review": "not recorded for these entries",
        },
        "summary": {
            "entries": len(rows),
            "by_status": dict(counts),
            "candidates": counts["candidate-for-independent-review"],
        },
        "entries": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    if args.write:
        OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                       encoding="utf-8")
        print(json.dumps(data["summary"], indent=2))
    elif args.check:
        current = json.loads(OUT.read_text(encoding="utf-8"))
        if current != data:
            raise SystemExit("sufficient-candidates-stale")
        print("PASS: sufficient candidates", data["summary"]["entries"])
    else:
        print(json.dumps(data["summary"], indent=2))


if __name__ == "__main__":
    main()
