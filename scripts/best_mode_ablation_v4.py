#!/usr/bin/env python3
"""Ablate best-mode hybrid RRF and top1 rerank on qrels v4."""
import argparse
import json
from pathlib import Path

import best_search
import hybrid_search
import section_search
import top1_rerank

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--weight", type=float, default=0.1)
    args = ap.parse_args(argv)
    page_qrels = json.loads(
        (args.root / "evaluation/corpus-qrels.v4.json").read_text(
            encoding="utf-8"))
    section_qrels = json.loads(
        (args.root / "evaluation/section-qrels.v4.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section_qrels["items"]}
    matrix, data, _ = hybrid_search.load_embeddings(
        args.root, "sentence-transformers/all-MiniLM-L6-v2",
        backend="sentence-transformers")
    semantic_model = hybrid_search.load_model(
        "sentence-transformers/all-MiniLM-L6-v2", "sentence-transformers")
    rerank_model = top1_rerank.load_model()
    modes = ("bm25", "hybrid", "bm25_rerank", "hybrid_rerank")
    hits = {mode: {split: {"page": [0, 0, 0], "section": [0, 0, 0]}
                   for split in ("book", "atlas", "v12", "all")}
            for mode in modes}
    totals = {split: 0 for split in ("book", "atlas", "v12", "all")}
    for item in page_qrels["items"]:
        bm25 = section_search.search(
            args.root, item["question"], limit=20, abstain=False,
            section_rerank=False).get("results", [])
        is_v12 = best_search.is_v12(item["question"], bm25)
        if is_v12:
            hybrid = bm25
        elif hybrid_search.matched_coverage(item["question"], bm25):
            hybrid = bm25
        else:
            semantic = hybrid_search.semantic_results(
                args.root, item["question"], semantic_model, matrix, data)
            hybrid = hybrid_search.page_rrf(
                bm25, semantic, args.weight, 20)
        bm25_rerank, _ = top1_rerank.rerank(
            item["question"], bm25, rerank_model)
        hybrid_rerank, _ = top1_rerank.rerank(
            item["question"], hybrid, rerank_model)
        rows = {
            "bm25": bm25[:5],
            "hybrid": hybrid[:5],
            "bm25_rerank": bm25_rerank[:5],
            "hybrid_rerank": hybrid_rerank[:5],
        }
        page_accept = set(item["accepted"])
        section_accept = set(sections[item["id"]]["accepted"])
        for split in (item["split"], "all"):
            totals[split] += 1
            for mode, results in rows.items():
                page_keys = [row["path"] for row in results]
                section_keys = [row["section_key"] for row in results]
                for index, k in enumerate((1, 3, 5)):
                    hits[mode][split]["page"][index] += int(
                        bool(set(page_keys[:k]) & page_accept))
                    hits[mode][split]["section"][index] += int(
                        bool(set(section_keys[:k]) & section_accept))
    output = {}
    for mode in modes:
        output[mode] = {}
        for split in hits[mode]:
            n = totals[split]
            output[mode][split] = {
                "n": n,
                "page": [round(value / n, 3)
                         for value in hits[mode][split]["page"]],
                "section": [round(value / n, 3)
                            for value in hits[mode][split]["section"]],
            }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
