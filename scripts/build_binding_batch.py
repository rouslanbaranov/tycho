#!/usr/bin/env python3
"""Build a binding-extraction manifest for one batch."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
OWNER = Path("edition/patterns/owner-units.v1.json")
PLAN = Path("edition/patterns/source-plan.v1.json")
LEDGER = Path("edition/patterns/reading-ledger.v1.json")
BATCHES = Path("research/sufficient-pilot-540/batch-plan.json")
OUT = Path("research/sufficient-pilot-540/binding-batches")


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", required=True)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    owners = {item["pattern_id"]: item for item in load(root / OWNER)["entries"]}
    plan = {item["pattern_id"]: item for item in load(root / PLAN)["entries"]}
    ledger = {item["id"]: item for item in load(root / LEDGER)["records"]}
    batches = load(root / BATCHES)["batches"]
    batch = next((item for item in batches if item["id"] == args.batch), None)
    if batch is None:
        raise SystemExit("unknown batch")
    rows = []
    for entry in batch["entries"]:
        pid = entry["pattern_id"]
        owner = owners[pid]
        support = owner["source_support"]
        unit = next(item for item in plan[pid]["required_units"]
                    if item["source_id"] == support["source_id"])
        record = ledger[support["ledger_record"]]
        dimensions = {name: {"state": value["state"],
                            "owner_quote": value.get("quote", ""),
                            "reason": value.get("reason", "")}
                      for name, value in owner["technical_evidence"].items()}
        rows.append({"pattern_id": pid, "catalog_name": owner["catalog_name"],
                     "owner_path": owner["owner"]["path"],
                     "owner_heading": owner["owner"]["heading"],
                     "source_id": support["source_id"],
                     "ledger_record": support["ledger_record"],
                     "url": unit["url"], "unit": unit["unit"],
                     "sections": record["sections_read"],
                     "revision": record["content_sha256"],
                     "dimensions": dimensions})
    out = root / OUT / (args.batch + ".json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"batch": args.batch, "entries": rows},
                              indent=2, ensure_ascii=False) + "\n")
    print("PASS:", len(rows), "entries", sum(len(x["dimensions"]) for x in rows), "dimensions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
