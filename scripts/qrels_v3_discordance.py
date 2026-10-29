#!/usr/bin/env python3
"""List BM25/best top-1 discordance on qrels v3."""
import argparse
import json
from pathlib import Path

import best_search
import section_search

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    rows = []
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        direct = set(item["direct"])
        bm25 = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        best = best_search.best_search(args.root, item["question"], limit=5)
        bm25_paths = [row["path"] for row in bm25.get("results", [])]
        best_paths = [row["path"] for row in best.get("results", [])]
        bm25_ok = bool(set(bm25_paths[:1]) & accepted)
        best_ok = bool(set(best_paths[:1]) & accepted)
        if bm25_ok == best_ok:
            continue
        rows.append({
            "id": item["id"], "split": item["split"],
            "question": item["question"],
            "bm25_top1": bm25_paths[0] if bm25_paths else None,
            "best_top1": best_paths[0] if best_paths else None,
            "bm25_correct": bm25_ok, "best_correct": best_ok,
            "best_direct": bool(set(best_paths[:1]) & direct),
            "accepted": sorted(accepted),
            "direct": sorted(direct),
            "retrieval_mode": best.get("retrieval_mode"),
            "rerank": best.get("rerank"),
        })
    print(json.dumps({"n": len(rows), "rows": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
