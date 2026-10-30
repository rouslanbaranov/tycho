#!/usr/bin/env python3
"""Atlas rank diagnostics on qrels v4."""
import argparse
import json
from collections import Counter
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def first_rank(paths, accepted):
    for index, path in enumerate(paths, 1):
        if path in accepted:
            return index
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v4.json")
                       .read_text(encoding="utf-8"))
    rows = []
    for item in qrels["items"]:
        if item["split"] != "atlas":
            continue
        result = section_search.search(
            args.root, item["question"], limit=10, abstain=False,
            section_rerank=False)
        paths = [row["path"] for row in result.get("results", [])]
        accepted = set(item["accepted"])
        direct = set(item["direct"])
        rows.append({
            "id": item["id"],
            "question": item["question"],
            "first_accepted_rank": first_rank(paths, accepted),
            "first_direct_rank": first_rank(paths, direct),
            "top1_path": paths[0] if paths else None,
            "top1_accepted": bool(paths and paths[0] in accepted),
            "accepted": sorted(accepted),
            "direct": sorted(direct),
        })
    summary = {
        "n": len(rows),
        "top1_accepted": sum(1 for row in rows if row["top1_accepted"]),
        "accepted_rank": dict(sorted(Counter(
            row["first_accepted_rank"] for row in rows).items())),
        "direct_rank": dict(sorted(Counter(
            row["first_direct_rank"] for row in rows).items())),
        "misses": [row for row in rows if not row["top1_accepted"]],
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
