#!/usr/bin/env python3
"""Validate the pooled qrels v3 candidate set and packet coverage."""
import argparse
import glob
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "evaluation/corpus-qrels.v3.pool.json"
PACKETS = ROOT / "evaluation/qrels-v3"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    pool = json.loads((args.root / "evaluation/corpus-qrels.v3.pool.json")
                      .read_text(encoding="utf-8"))
    errors = []
    ids = [row["id"] for row in pool["queries"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate query ids")
    if pool["query_count"] != len(ids):
        errors.append("query_count mismatch")
    if pool["candidate_count"] != sum(
            len(row["candidates"]) for row in pool["queries"]):
        errors.append("candidate_count mismatch")
    for row in pool["queries"]:
        paths = [entry["path"] for entry in row["candidates"]]
        if len(paths) != len(set(paths)):
            errors.append("duplicate candidate: " + row["id"])
        for path in paths:
            if not (args.root / path).is_file():
                errors.append("missing candidate: " + path)
        for path in row["prior_paths"]:
            if path not in paths:
                errors.append("prior not in candidates: " + row["id"])
    files = sorted(glob.glob(str(args.root / "evaluation/qrels-v3/"
                                "packet-*.json")))
    if len(files) != 10:
        errors.append("expected 10 packets, found " + str(len(files)))
    packet_ids = set()
    for filename in files:
        packet = json.loads(Path(filename).read_text(encoding="utf-8"))
        if packet.get("status") != "unreviewed":
            errors.append("packet status: " + filename)
        for row in packet["queries"]:
            packet_ids.add(row["id"])
    if packet_ids != set(ids):
        errors.append("packet/query coverage mismatch")
    print(json.dumps({"status": "ok" if not errors else "fail",
                      "queries": len(ids), "candidates":
                      pool["candidate_count"], "packets": len(files),
                      "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
