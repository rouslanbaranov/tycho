#!/usr/bin/env python3
"""Evaluate BM25, production margin gate and best mode on qrels v4."""
import argparse
import json
from pathlib import Path

import best_search
import section_search

ROOT = Path(__file__).resolve().parents[1]
SPLITS = ("book", "atlas", "v12", "all")


def hits(results, accepted, level, k):
    if level == "page":
        keys = [row["path"] for row in results]
    else:
        keys = [row["section_key"] for row in results]
    return bool(set(keys[:k]) & accepted)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page_qrels = json.loads(
        (args.root / "evaluation/corpus-qrels.v4.json").read_text(
            encoding="utf-8"))
    section_qrels = json.loads(
        (args.root / "evaluation/section-qrels.v4.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {split: {mode: {level: [0, 0, 0]
                             for level in ("page", "section")}
                      for mode in ("bm25", "margin", "best")}
              for split in SPLITS}
    for item in page_qrels["items"]:
        split = item["split"]
        qid = item["id"]
        page_accepted = set(item["accepted"])
        section_item = sections[qid]
        section_accepted = set(section_item["accepted"])
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False,
            section_rerank=False)
        try:
            margin = section_search.search(
                args.root, item["question"], limit=5, abstain=False,
                section_rerank=True, section_rerank_margin=0.15)
        except section_search.SearchError:
            margin = base
        best = best_search.best_search(
            args.root, item["question"], limit=5)
        for mode, payload in (("bm25", base), ("margin", margin),
                              ("best", best)):
            results = payload.get("results", [])
            for level, accepted in (("page", page_accepted),
                                    ("section", section_accepted)):
                for index, k in enumerate((1, 3, 5)):
                    for target in (split, "all"):
                        counts[target][mode][level][index] += int(
                            hits(results, accepted, level, k))
    output = {"qrels": "evaluation/corpus-qrels.v4.json",
              "status": page_qrels["status"], "splits": {}}
    totals = {split: sum(1 for item in page_qrels["items"]
                         if split == "all" or item["split"] == split)
              for split in SPLITS}
    for split in SPLITS:
        n = totals[split]
        output["splits"][split] = {"n": n}
        for mode in ("bm25", "margin", "best"):
            output["splits"][split][mode] = {}
            for level in ("page", "section"):
                output["splits"][split][mode][level] = [
                    round(value / n, 3)
                    for value in counts[split][mode][level]]
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
