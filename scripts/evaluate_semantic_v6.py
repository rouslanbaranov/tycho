#!/usr/bin/env python3
"""Evaluate chunk-semantic hybrid retrieval and cross-encoder rerank."""
import argparse
import json
from pathlib import Path
import statistics
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import hybrid_rerank
import section_search
import semantic_chunk_index


def load_qrels(root):
    page = json.loads((Path(root) / "evaluation/corpus-qrels.v5-dense.json")
                      .read_text(encoding="utf-8"))["items"]
    section = json.loads((Path(root) / "evaluation/section-qrels.v5-dense.json")
                         .read_text(encoding="utf-8"))["items"]
    by_id = {item["id"]: item for item in section}
    return page, by_id


def rank_metrics(rows, accepted_paths, accepted_sections):
    page_rank = None
    section_rank = None
    for number, row in enumerate(rows, 1):
        if page_rank is None and row.get("path") in accepted_paths:
            page_rank = number
        if section_rank is None and row.get("section_key") in accepted_sections:
            section_rank = number
        if page_rank and section_rank:
            break
    return page_rank, section_rank


def summarize(values):
    n = len(values)
    return {
        "page": {k: round(sum(1 for p, _ in values if p and p <= k) / n, 3)
                 for k in (1, 3, 5)},
        "section": {k: round(sum(1 for _, s in values if s and s <= k) / n, 3)
                    for k in (1, 3, 5)},
        "mrr_page": round(sum(1 / p for p, _ in values if p) / n, 3),
        "mrr_section": round(sum(1 / s for _, s in values if s) / n, 3),
    }


def evaluate(root, weights, model, path, backend):
    page_qrels, section_qrels = load_qrels(root)
    methods = {"bm25": [], "semantic": []}
    for weight in weights:
        methods["hybrid-" + str(weight)] = []
    hybrid_strict = []
    for item in page_qrels:
        accepted_paths = set(item["accepted"])
        accepted_sections = set(section_qrels[item["id"]]["accepted"])
        bm25 = section_search.search(
            root, item["question"], limit=20, abstain=False)["results"]
        semantic, _ = semantic_chunk_index.search(
            root, item["question"], limit=20, model_name=model,
            path=path, backend=backend)
        methods["bm25"].append(rank_metrics(bm25, accepted_paths,
                                             accepted_sections))
        methods["semantic"].append(rank_metrics(semantic, accepted_paths,
                                                 accepted_sections))
        for weight in weights:
            fused = hybrid_rerank.fuse(bm25, semantic, weight, 20)
            methods["hybrid-" + str(weight)].append(
                rank_metrics(fused, accepted_paths, accepted_sections))
        hybrid_strict.append((bm25, semantic, accepted_paths,
                              accepted_sections))
    return page_qrels, methods, hybrid_strict


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--weights", default="0.25,0.5,0.75,1.0")
    parser.add_argument("--rerank-weight", type=float, default=None)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--model", default=semantic_chunk_index.DEFAULT_MODEL)
    parser.add_argument("--backend", default="model2vec")
    parser.add_argument("--embeddings", type=Path, default=None)
    args = parser.parse_args(argv)
    weights = [float(x) for x in args.weights.split(",")]
    page_qrels, methods, hybrid_rows = evaluate(
        args.root, weights, args.model, args.embeddings, args.backend)
    output = {name: summarize(values) for name, values in methods.items()}
    if args.rerank_weight is not None:
        weight = args.rerank_weight
        reranked = []
        started = time.perf_counter()
        for index, (bm25, semantic, paths, sections) in enumerate(hybrid_rows):
            fused = hybrid_rerank.fuse(bm25, semantic, weight, 20)
            rows, _ = hybrid_rerank.rerank(
                args.root, page_qrels[index]["question"], fused,
                limit=args.limit)
            reranked.append(rank_metrics(rows, paths, sections))
        output["hybrid-" + str(weight) + "-rerank"] = summarize(reranked)
        output["rerank_seconds"] = round(time.perf_counter() - started, 2)
    print(json.dumps({"queries": len(page_qrels), "metrics": output},
                     indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
