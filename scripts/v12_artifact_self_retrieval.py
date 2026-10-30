#!/usr/bin/env python3
"""Self-retrieval diagnostic for query-aware V12 artifacts."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    artifacts = section_search.load_v12_artifacts(args.root)
    hits = {1: 0, 3: 0, 5: 0}
    n = 0
    misses = []
    for artifact in artifacts:
        for question in artifact.get("questions") or []:
            n += 1
            terms = section_search.normalize_terms(question)
            payload = section_search.v12_artifacts(
                args.root, limit=5, terms=terms)
            ids = [item["id"] for item in payload["artifacts"]]
            for k in hits:
                hits[k] += int(artifact["id"] in ids[:k])
            if not ids or ids[0] != artifact["id"]:
                misses.append({
                    "expected": artifact["id"],
                    "question": question,
                    "returned": ids,
                })
    print(json.dumps({
        "n": n,
        "top1": round(hits[1] / n, 3),
        "top3": round(hits[3] / n, 3),
        "top5": round(hits[5] / n, 3),
        "misses": misses[:10],
        "notice": ("Self-retrieval diagnostic, not independent qrels; "
                   "no human review or sufficient coverage."),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
