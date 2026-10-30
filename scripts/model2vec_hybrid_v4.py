#!/usr/bin/env python3
"""Evaluate model2vec hybrid RRF weights on qrels v4."""
import argparse
import json
from pathlib import Path

import best_search
import hybrid_search
import section_search

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = (0.05, 0.1, 0.2)


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
    matrix, data, meta = hybrid_search.load_embeddings(args.root)
    model = hybrid_search.load_model(hybrid_search.DEFAULT_MODEL,
                                     "model2vec")
    labels = ["bm25"] + [str(weight) for weight in WEIGHTS]
    counts = {label: {split: {"page": [0, 0, 0], "section": [0, 0, 0]}
                      for split in ("book", "atlas", "v12", "all")}
              for label in labels}
    totals = {split: 0 for split in ("book", "atlas", "v12", "all")}
    for item in page_qrels["items"]:
        bm25 = section_search.search(
            args.root, item["question"], limit=20, abstain=False,
            section_rerank=False).get("results", [])
        is_v12 = best_search.is_v12(item["question"], bm25)
        semantic = None
        if not is_v12 and not hybrid_search.matched_coverage(
                item["question"], bm25):
            semantic = hybrid_search.semantic_results(
                args.root, item["question"], model, matrix, data)
        rows = {"bm25": bm25[:5]}
        for weight in WEIGHTS:
            if semantic is None:
                rows[str(weight)] = bm25[:5]
            else:
                rows[str(weight)] = hybrid_search.page_rrf(
                    bm25, semantic, weight, 5)
        page_accept = set(item["accepted"])
        section_accept = set(sections[item["id"]]["accepted"])
        for split in (item["split"], "all"):
            totals[split] += 1
            for label, results in rows.items():
                page_keys = [row["path"] for row in results]
                section_keys = [row["section_key"] for row in results]
                for index, k in enumerate((1, 3, 5)):
                    counts[label][split]["page"][index] += int(
                        bool(set(page_keys[:k]) & page_accept))
                    counts[label][split]["section"][index] += int(
                        bool(set(section_keys[:k]) & section_accept))
    output = {"meta": meta, "results": {}}
    for label in labels:
        output["results"][label] = {}
        for split in counts[label]:
            n = totals[split]
            output["results"][label][split] = {
                "n": n,
                "page": [round(value / n, 3)
                         for value in counts[label][split]["page"]],
                "section": [round(value / n, 3)
                            for value in counts[label][split]["section"]],
            }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
