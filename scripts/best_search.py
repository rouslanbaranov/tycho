#!/usr/bin/env python3
"""Optional best-mode composition: adaptive hybrid plus top-1 reranker.

BM25 remains the default. V12 results are left on BM25.
"""
import argparse
import json
from pathlib import Path
import sys

import hybrid_search
import top1_rerank

ROOT = Path(__file__).resolve().parents[1]


def is_v12(query, results):
    return ("v12" in str(query).casefold()
            or bool(results and results[0].get("volume") == "v12"))


def best_search(root, query, limit=5, weight=0.1,
                backend="sentence-transformers",
                model_name="sentence-transformers/all-MiniLM-L6-v2",
                bundle=None):
    import section_search
    bm25 = section_search.search(
        root, query, limit=20, abstain=False).get("results", [])
    if is_v12(query, bm25):
        return {"status": "ok", "retrieval_mode": "v12-bm25",
                "results": bm25[:limit], "rerank": "skipped-v12"}
    if hybrid_search.matched_coverage(query, bm25):
        base = bm25[:limit]
        mode = "bm25"
    else:
        if bundle is None:
            matrix, data, _ = hybrid_search.load_embeddings(
                root, model_name, backend=backend)
            model = hybrid_search.load_model(model_name, backend)
        else:
            matrix, data, model = bundle
        semantic = hybrid_search.semantic_results(
            root, query, model, matrix, data)
        base = hybrid_search.page_rrf(bm25, semantic, weight, limit)
        mode = "hybrid-page-rrf"
    results, reason = top1_rerank.rerank(
        query, base, top1_rerank.load_model())
    return {"status": "ok" if results else "no-results",
            "retrieval_mode": mode, "rerank": reason,
            "results": results,
            "notice": "Optional composition; BM25 remains default."}


def qrels(root):
    rows = []
    for split, relative in (("v2", "evaluation/corpus-qrels.v2.json"),
                            ("p3", "evaluation/agent-qrels.phase3.json"),
                            ("v12", "evaluation/v12-simulation-qrels.v1.json")):
        data = json.loads((Path(root) / relative).read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if split == "p3" and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            rows.append((split, item))
    return rows


def evaluate(root):
    matrix, data, _ = hybrid_search.load_embeddings(
        root, "sentence-transformers/all-MiniLM-L6-v2",
        backend="sentence-transformers")
    bundle = (matrix, data, hybrid_search.load_model(
        "sentence-transformers/all-MiniLM-L6-v2", "sentence-transformers"))
    values = []
    for split, item in qrels(root):
        results = best_search(root, item["question"], bundle=bundle)["results"]
        accepted = {(a["path"], a.get("section_id"))
                    for a in item.get("accepted", [])}
        rank = None
        for number, result in enumerate(results, 1):
            if ((result["path"], result["section_id"]) in accepted
                    or (result["path"], None) in accepted):
                rank = number
                break
        values.append((split, rank))
    def summary(rows):
        n = len(rows)
        return {k: round(sum(1 for _, rank in rows if rank and rank <= k) / n, 3)
                for k in (1, 3, 5)}
    return {"status": "diagnostic", "all": summary(values),
            "v2": summary([v for v in values if v[0] == "v2"]),
            "p3": summary([v for v in values if v[0] == "p3"]),
            "v12": summary([v for v in values if v[0] == "v12"]),
            "notice": "Optional composition; stale qrels; no quality claim."}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("search", "evaluate"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--query")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--weight", type=float, default=0.1)
    ap.add_argument("--backend", default="sentence-transformers")
    ap.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    args = ap.parse_args(argv)
    if args.action == "evaluate":
        print(json.dumps(evaluate(args.root), indent=2, sort_keys=True))
        return 0
    if not args.query:
        raise SystemExit("--query is required")
    print(json.dumps(best_search(args.root, args.query, args.limit,
                                 args.weight, args.backend, args.model),
                     indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
