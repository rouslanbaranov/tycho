#!/usr/bin/env python3
"""Page-level evaluation of guarded section_rerank on qrels v3."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/corpus-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    counts = {"all": {"n": 0, "base": [0, 0, 0], "rerank": [0, 0, 0],
                      "guarded": [0, 0, 0], "guarded_queries": 0}}
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False,
            section_rerank=False)
        base_paths = [row["path"] for row in base.get("results", [])]
        top_volume = (base.get("results") or [{}])[0].get("volume")
        guarded = ("v12" in item["question"].casefold()
                   or top_volume == "v12")
        if guarded:
            rerank_paths = base_paths
        else:
            rerank = section_search.search(
                args.root, item["question"], limit=5, abstain=False,
                section_rerank=True)
            rerank_paths = [row["path"] for row in rerank.get("results", [])]
        guarded_paths = base_paths if guarded else rerank_paths
        for split in (item["split"], "all"):
            bucket = counts.setdefault(split, {
                "n": 0, "base": [0, 0, 0], "rerank": [0, 0, 0],
                "guarded": [0, 0, 0], "guarded_queries": 0})
            bucket["n"] += 1
            bucket["guarded_queries"] += int(guarded)
            for index, k in enumerate((1, 3, 5)):
                bucket["base"][index] += int(
                    bool(set(base_paths[:k]) & accepted))
                bucket["rerank"][index] += int(
                    bool(set(rerank_paths[:k]) & accepted))
                bucket["guarded"][index] += int(
                    bool(set(guarded_paths[:k]) & accepted))
    output = {"qrels": "evaluation/corpus-qrels.v3.json", "splits": {}}
    for split, bucket in counts.items():
        n = bucket["n"]
        output["splits"][split] = {
            "n": n, "guarded_queries": bucket["guarded_queries"],
            "base": [round(v / n, 3) for v in bucket["base"]],
            "rerank": [round(v / n, 3) for v in bucket["rerank"]],
            "guarded": [round(v / n, 3) for v in bucket["guarded"]],
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
