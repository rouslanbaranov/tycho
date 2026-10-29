#!/usr/bin/env python3
"""Compare page and section hit rates on phase3 qrels."""
import argparse
import json
from pathlib import Path

import best_search
import section_search

ROOT = Path(__file__).resolve().parents[1]


def rate(rows, key, k):
    index = {1: 0, 3: 1, 5: 2}[k]
    return round(sum(1 for row in rows if row[key][index]) / len(rows), 3)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    data = json.loads((args.root / "evaluation/agent-qrels.phase3.json")
                      .read_text(encoding="utf-8"))
    rows = []
    for item in data.get("items", []):
        if item.get("final_label") != "answerable":
            continue
        accepted = {(entry["path"], entry.get("section_id"))
                    for entry in item.get("accepted", [])}
        accepted_pages = {entry["path"] for entry in item.get("accepted", [])}
        bm25 = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        best = best_search.best_search(args.root, item["question"], limit=5)
        def pairs(results):
            return [(row["path"], row.get("section_id"))
                    for row in results.get("results", [])]
        bm25_pairs = pairs(bm25)
        best_pairs = pairs(best)
        bm25_section = [bool(set(bm25_pairs[:k]) & accepted)
                        for k in (1, 3, 5)]
        best_section = [bool(set(best_pairs[:k]) & accepted)
                        for k in (1, 3, 5)]
        bm25_page = [bool(set(path for path, _ in bm25_pairs[:k])
                          & accepted_pages) for k in (1, 3, 5)]
        best_page = [bool(set(path for path, _ in best_pairs[:k])
                          & accepted_pages) for k in (1, 3, 5)]
        rows.append({"id": item["id"], "question": item["question"],
                     "bm25_section": bm25_section,
                     "best_section": best_section,
                     "bm25_page": bm25_page, "best_page": best_page,
                     "retrieval_mode": best.get("retrieval_mode")})
    output = {"n": len(rows),
              "bm25_section": [rate(rows, "bm25_section", k)
                               for k in (1, 3, 5)],
              "best_section": [rate(rows, "best_section", k)
                               for k in (1, 3, 5)],
              "bm25_page": [rate(rows, "bm25_page", k) for k in (1, 3, 5)],
              "best_page": [rate(rows, "best_page", k) for k in (1, 3, 5)],
              "rows": rows}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
