#!/usr/bin/env python3
"""Section-level BM25 + chunk-semantic fusion with optional cross-encoder rerank."""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search
import semantic_chunk_index

DEFAULT_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
CROSS_CACHE = {}


def section_content(root, keys, index_path=None):
    target = Path(index_path) if index_path else Path(root) / "generated/sections-fts-v5.sqlite"
    if not keys:
        return {}
    marks = ",".join("?" for _ in keys)
    with sqlite3.connect("file:" + target.resolve().as_posix() + "?mode=ro",
                         uri=True) as db:
        rows = db.execute(
            "select section_key,title,heading,content from sections"
            " where section_key in (" + marks + ")", tuple(keys)).fetchall()
    return {row[0]: {"title": row[1], "heading": row[2], "content": row[3]}
            for row in rows}


def fuse(bm25, semantic, weight=0.5, limit=20):
    by_key = {}
    bm_rank = {}
    sem_rank = {}
    for rank, item in enumerate(bm25, 1):
        key = item["section_key"]
        if key not in by_key:
            by_key[key] = dict(item)
        bm_rank[key] = rank
    for rank, item in enumerate(semantic, 1):
        key = item["section_key"]
        if key not in by_key:
            by_key[key] = {
                "section_key": key,
                "section_id": item["section_id"],
                "path": item["path"],
                "heading": item["heading"],
                "semantic_chunk": item["chunk_id"],
                "semantic_score": item["score"],
            }
        else:
            by_key[key]["semantic_chunk"] = item["chunk_id"]
            by_key[key]["semantic_score"] = item["score"]
        sem_rank[key] = rank
    scored = []
    for key, item in by_key.items():
        score = 0.0
        if key in bm_rank:
            score += 1.0 / (60 + bm_rank[key])
        if key in sem_rank:
            score += weight / (60 + sem_rank[key])
        item["hybrid_score"] = round(score, 8)
        item["bm25_rank"] = bm_rank.get(key)
        item["semantic_rank"] = sem_rank.get(key)
        item["retrieval_mode"] = "hybrid-section-rrf"
        item["citation"] = item["path"] + "#" + item["section_id"]
        scored.append(item)
    scored.sort(key=lambda x: (-x["hybrid_score"], x["section_key"]))
    return scored[:limit]


def load_cross(model_name=DEFAULT_MODEL):
    if model_name not in CROSS_CACHE:
        from sentence_transformers import CrossEncoder
        CROSS_CACHE[model_name] = CrossEncoder(model_name)
    return CROSS_CACHE[model_name]


def rerank(root, query, candidates, model_name=DEFAULT_MODEL, limit=5,
           index_path=None):
    if not candidates:
        return [], "no-candidates"
    model = load_cross(model_name)
    texts = section_content(root, [c["section_key"] for c in candidates],
                            index_path)
    pairs = []
    for item in candidates:
        body = texts.get(item["section_key"], {})
        text = " ".join(str(body.get(k, "")) for k in
                        ("title", "heading", "content"))[:4000]
        pairs.append((query, text or item.get("heading", "")))
    scores = model.predict(pairs, show_progress_bar=False)
    order = sorted(range(len(candidates)),
                   key=lambda i: (-float(scores[i]),
                                  candidates[i]["section_key"]))
    out = []
    for index in order[:limit]:
        item = dict(candidates[index])
        item["rerank_score"] = round(float(scores[index]), 6)
        item["rerank_mode"] = "cross-encoder"
        out.append(item)
    return out, "reranked"


def search(root, query, limit=5, candidates=20, weight=0.5,
           rerank_results=True, model_name=DEFAULT_MODEL,
           index_path=None):
    bm25 = section_search.search(
        root, query, limit=candidates, abstain=False).get("results", [])
    semantic, _ = semantic_chunk_index.search(
        root, query, limit=candidates)
    fused = fuse(bm25, semantic, weight, candidates)
    if rerank_results:
        return rerank(root, query, fused, model_name, limit, index_path)
    return fused[:limit], "no-rerank"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--candidates", type=int, default=20)
    parser.add_argument("--weight", type=float, default=0.5)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--no-rerank", action="store_true")
    args = parser.parse_args(argv)
    results, mode = search(args.root, args.query, args.limit,
                           args.candidates, args.weight,
                           not args.no_rerank, args.model)
    print(json.dumps({"query": args.query, "mode": mode,
                      "results": results}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
