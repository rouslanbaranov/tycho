#!/usr/bin/env python3
"""Compute precision, recall, MRR and NDCG on v5-dense."""
import argparse
import json
import math
import os
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

PROFILES = {"10,5,1": "10,5,1", "5,2,.5": "5,2,0.5",
            "3,2,1": "3,2,1"}


def ndcg(keys, grades, k=5):
    gains = [2 ** grades.get(key, 0) - 1 for key in keys[:k]]
    dcg = sum(gain / math.log2(index + 2)
              for index, gain in enumerate(gains))
    ideal = sorted((2 ** grade - 1 for grade in grades.values()),
                   reverse=True)[:k]
    idcg = sum(gain / math.log2(index + 2)
               for index, gain in enumerate(ideal))
    return dcg / idcg if idcg else 0.0


def one_level(page_qrels, section_qrels, rows_by_id, level):
    sections = {item["id"]: item for item in section_qrels["items"]}
    values = defaultdict(float)
    split_values = defaultdict(float)
    count = 0
    split_counts = defaultdict(int)
    for item in page_qrels["items"]:
        if level == "page":
            item_level = item
            keys = [row["path"] for row in rows_by_id[item["id"]]]
        else:
            item_level = sections[item["id"]]
            keys = [row["section_key"]
                    for row in rows_by_id[item["id"]]]
        grades = item_level["grades"]
        accepted = set(item_level["accepted"])
        hits = [1 if key in accepted else 0 for key in keys]
        metrics = {
            "p@5": sum(hits) / 5.0,
            "r@5": sum(hits) / len(accepted) if accepted else 0.0,
            "mrr": 0.0,
            "ndcg@5": ndcg(keys, grades),
        }
        for index, hit in enumerate(hits, 1):
            if hit:
                metrics["mrr"] = 1.0 / index
                break
        for name, value in metrics.items():
            values[name] += value
            split_values[(item["split"], name)] += value
        count += 1
        split_counts[item["split"]] += 1
    output = {name: round(values[name] / count, 4)
              for name in ("p@5", "r@5", "mrr", "ndcg@5")}
    split = {}
    for split_name, total in split_counts.items():
        split[split_name] = {
            name: round(split_values[(split_name, name)] / total, 4)
            for name in ("p@5", "r@5", "mrr", "ndcg@5")}
    return output, split


def evaluate(root, page_qrels, section_qrels, profile):
    os.environ["TYCHO_BM25_WEIGHTS"] = profile
    rows_by_id = {}
    for item in page_qrels["items"]:
        result = section_search.search(
            root, item["question"], limit=5, abstain=False)
        rows_by_id[item["id"]] = result.get("results", [])
    page, page_split = one_level(
        page_qrels, section_qrels, rows_by_id, "page")
    section, section_split = one_level(
        page_qrels, section_qrels, rows_by_id, "section")
    return {"profile": profile, "overall": {"page": page,
                                            "section": section},
            "split": {"page": page_split, "section": section_split}}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--page-qrels",
                    default="evaluation/corpus-qrels.v5-dense.json")
    ap.add_argument("--section-qrels",
                    default="evaluation/section-qrels.v5-dense.json")
    args = ap.parse_args(argv)
    page = json.loads((args.root / args.page_qrels).read_text(
        encoding="utf-8"))
    section = json.loads((args.root / args.section_qrels).read_text(
        encoding="utf-8"))
    print(json.dumps({name: evaluate(args.root, page, section, profile)
                      for name, profile in PROFILES.items()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
