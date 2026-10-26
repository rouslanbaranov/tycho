#!/usr/bin/env python3
"""Validate the six-entry sufficient pilot inputs without reviewing them."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path("research/sufficient-pilot-540/manifest.json")
PLAN = Path("research/sufficient-pilot-540/batch-plan.json")
PROMOTIONS = Path("edition/patterns/sufficient-promotions.v1.json")
OWNER = Path("edition/patterns/owner-units.v1.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
SOURCE = Path("edition/patterns/source-plan.v1.json")
LEDGER = Path("edition/patterns/reading-ledger.v1.json")
BATCHES = Path("edition/patterns/card-batches.v1.json")
ATLAS = Path("edition/atlas-manifest.json")
DIMENSIONS = ("mechanism", "invariant", "failure_recovery", "alternative")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate(root=ROOT):
    root = Path(root).resolve()
    manifest = load(root / MANIFEST)
    entries = manifest["entries"]
    require(len(entries) == 6, "pilot-entry-count")
    owners = {item["pattern_id"]: item
              for item in load(root / OWNER)["entries"]}
    patterns = {item["id"]: item
                for item in load(root / REGISTRY)["patterns"]}
    sources = {item["pattern_id"]: item
               for item in load(root / SOURCE)["entries"]}
    ledger = {item["id"]: item
              for item in load(root / LEDGER)["records"]}
    promoted = {item["pattern_id"]
                for item in load(root / PROMOTIONS)["promotions"]}
    batches = load(root / BATCHES)["batches"]
    chapters = {item["code"]: item
                for item in load(root / ATLAS)["chapters"]}
    card_paths = {}
    for batch in batches:
        chapter = chapters[batch["chapter"]]
        for item in batch["entries"]:
            card_paths[item["pattern_id"]] = chapter["path"]
    seen = set()
    for entry in entries:
        pid = entry["pattern_id"]
        require(pid not in seen, "pilot-duplicate: " + pid)
        seen.add(pid)
        require(pid in owners and pid in patterns and pid in sources,
                "pilot-unknown-pattern: " + pid)
        owner = owners[pid]
        require(entry["owner_path"] == owner["owner"]["path"],
                "pilot-owner-path: " + pid)
        require(entry["owner_heading"] == owner["owner"]["heading"],
                "pilot-owner-heading: " + pid)
        require(entry["owner_page_sha256"] == sha(root / entry["owner_path"]),
                "pilot-owner-hash: " + pid)
        require(entry["card_path"] == card_paths[pid],
                "pilot-card-path: " + pid)
        require(entry["card_sha256"] == sha(root / entry["card_path"]),
                "pilot-card-hash: " + pid)
        require(entry["sources"] == [unit["source_id"]
                                     for unit in sources[pid]["required_units"]],
                "pilot-sources: " + pid)
        record = ledger.get(entry["ledger_record"])
        require(record is not None, "pilot-ledger-missing: " + pid)
        require(record["status"] == "read", "pilot-ledger-status: " + pid)
        require(record["source_id"] in entry["sources"],
                "pilot-ledger-source: " + pid)
        status = entry["review_status"]
        require(status in ("pending-independent-external-ai-review",
                           "rejected", "passed"),
                "pilot-review-status: " + pid)
        if status == "pending-independent-external-ai-review":
            require(all(owner["technical_evidence"][name]["state"] == "supported"
                        for name in DIMENSIONS),
                    "pilot-dimension: " + pid)
        if status == "rejected":
            require(entry["promotion_status"] == "blocked",
                    "pilot-rejected-promotion: " + pid)
            require(pid not in promoted, "pilot-rejected-promoted: " + pid)
            require(entry.get("review_report"), "pilot-review-report: " + pid)
            report = root / entry["review_report"]
            require(report.is_file(), "pilot-review-report-missing: " + pid)
            require(sha(report) == entry["review_report_sha256"],
                    "pilot-review-report-hash: " + pid)
        require(owner["decision_evidence"]["card_components"] == 10,
                "pilot-card-components: " + pid)
        card = (root / entry["card_path"]).read_text(encoding="utf-8")
        require(chr(96) + "sufficient" + chr(96) not in card,
                "pilot-sufficient-claim: " + pid)
    plan = load(root / PLAN)
    require(set(plan["pilot_entries"]) == seen, "pilot-plan-mismatch")
    planned = [item["pattern_id"] for batch in plan["batches"]
               for item in batch["entries"]]
    require(len(planned) == len(set(planned)), "pilot-plan-duplicate")
    require(len(planned) == plan["remaining_entries"], "pilot-plan-count")
    require(all(1 <= len(batch["entries"]) <= plan["batch_size"]
                for batch in plan["batches"]), "pilot-plan-size")
    require(set(planned) == set(patterns) - seen, "pilot-plan-partition")
    for pid in planned:
        owner = owners[pid]
        require(all(owner["technical_evidence"][name]["state"] == "supported"
                    for name in DIMENSIONS),
                "batch-dimension: " + pid)
        require(owner["technical_coverage"]
                in ("partial-bounded", "partial", "sufficient"),
                "batch-coverage: " + pid)
        require(pid not in promoted, "batch-premature-promotion: " + pid)
    return {"entries": len(entries), "batches": len(plan["batches"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        return 1
    print("PASS: sufficient pilot inputs", result["entries"],
          "entries;", result["batches"], "remaining batches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
