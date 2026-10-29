#!/usr/bin/env python3
"""Merge independently reviewed qrels v3 packets into the final artifact."""
import argparse
import glob
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "evaluation/corpus-qrels.v3.pool.json"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--labels", type=Path, required=True)
    args = ap.parse_args(argv)
    pool = json.loads((args.root / "evaluation/corpus-qrels.v3.pool.json")
                      .read_text(encoding="utf-8"))
    files = sorted(glob.glob(str(args.labels / "packet-*.reviewed.json")))
    if len(files) != 10:
        raise SystemExit("expected 10 reviewed packets")
    grades = {}
    reviewers = []
    for filename in files:
        review = json.loads(Path(filename).read_text(encoding="utf-8"))
        reviewers.append(review.get("reviewer"))
        for query_id, values in review.get("grades", {}).items():
            if query_id in grades:
                raise SystemExit("duplicate query review: " + query_id)
            grades[query_id] = values
    items = []
    for row in pool["queries"]:
        if row["id"] not in grades:
            raise SystemExit("missing query: " + row["id"])
        values = grades[row["id"]]
        wanted = {entry["path"] for entry in row["candidates"]}
        if set(values) != wanted:
            raise SystemExit("candidate grade mismatch: " + row["id"])
        if any(grade not in (0, 1, 2) for grade in values.values()):
            raise SystemExit("invalid grade: " + row["id"])
        accepted = sorted(path for path, grade in values.items() if grade >= 1)
        direct = sorted(path for path, grade in values.items() if grade == 2)
        items.append({"id": row["id"], "split": row["split"],
                      "question": row["question"], "grades": values,
                      "accepted": accepted, "direct": direct})
    result = {
        "schema_version": 3,
        "status": "independent-adjudicated",
        "level": "page",
        "snapshot": pool["snapshot"],
        "query_count": len(items),
        "candidate_count": pool["candidate_count"],
        "reviewers": reviewers,
        "items": items,
        "limits": "Page-level pooled qrels; independent reviewer reports required.",
    }
    target = args.root / "evaluation/corpus-qrels.v3.json"
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                      encoding="utf-8")
    print("wrote", target, len(items), "queries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
