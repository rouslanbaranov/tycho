#!/usr/bin/env python3
"""Optional page-level BM25 + semantic hybrid search.

BM25 remains the production default. This module adds a diagnostic hybrid mode
and a snapshot-bound H2 embedding index. It does not modify the book, atlas or
qrels.
"""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "generated/sections-fts-v4.sqlite"
DEFAULT_EMBEDDINGS = (Path.home() / ".cache/tycho/"
                       "semantic-h2-index.npz")
DEFAULT_MODEL = "minishlab/potion-base-8M"
DEFAULT_WEIGHT = 0.1


def h2_rows(root, index_path=None):
    target = Path(index_path) if index_path else Path(root) / DEFAULT_INDEX.relative_to(ROOT)
    with sqlite3.connect("file:" + target.resolve().as_posix() + "?mode=ro",
                         uri=True) as db:
        db.row_factory = sqlite3.Row
        rows = db.execute(
            "select section_key,section_id,path,heading,title,content"
            " from sections where heading_level=2").fetchall()
    return [dict(row) for row in rows]


def build(root, model_name=DEFAULT_MODEL, output=DEFAULT_EMBEDDINGS):
    import numpy as np
    from model2vec import StaticModel
    import section_fts_index
    rows = h2_rows(root)
    model = load_model(model_name)
    matrix = np.asarray(model.encode(
        [row["heading"] + "\n" + row["content"] for row in rows],
        show_progress_bar=False), dtype="float32")
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True).clip(min=1e-9)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        output, matrix=matrix,
        section_keys=np.asarray([row["section_key"] for row in rows]),
        section_ids=np.asarray([row["section_id"] for row in rows]),
        paths=np.asarray([row["path"] for row in rows]),
        headings=np.asarray([row["heading"] for row in rows]))
    meta = {"schema_version": 1, "model": model_name,
            "snapshot": section_fts_index.stats(root)["snapshot"],
            "sections": len(rows)}
    Path(str(output) + ".json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return meta


def load_embeddings(root, model_name=DEFAULT_MODEL, path=DEFAULT_EMBEDDINGS):
    import numpy as np
    import section_fts_index
    path = Path(path)
    meta = json.loads(Path(str(path) + ".json").read_text(encoding="utf-8"))
    current = section_fts_index.stats(root)["snapshot"]
    if meta.get("snapshot") != current:
        raise RuntimeError("semantic index is stale; rebuild it")
    if meta.get("model") != model_name:
        raise RuntimeError("semantic index model mismatch")
    data = np.load(path)
    return data["matrix"], data, meta


def load_model(model_name=DEFAULT_MODEL):
    from model2vec import StaticModel
    return StaticModel.from_pretrained(model_name)


def semantic_results(root, query, model, matrix, data, limit=20):
    import numpy as np
    vector = np.asarray(model.encode([query], show_progress_bar=False)[0],
                        dtype="float32")
    vector /= max(float(np.linalg.norm(vector)), 1e-9)
    order = np.argsort(-(matrix @ vector))[:limit]
    rows = []
    for i in order:
        rows.append({
            "path": str(data["paths"][i]),
            "section_id": str(data["section_ids"][i]),
            "section_key": str(data["section_keys"][i]),
            "heading": str(data["headings"][i]),
            "score": float(matrix[i] @ vector),
        })
    return rows


def page_rrf(bm25_results, semantic_results, weight=DEFAULT_WEIGHT,
             limit=5):
    """Fuse page ranks and choose a public section per page."""
    bm_by_path = {}
    for rank, item in enumerate(bm25_results, 1):
        bm_by_path.setdefault(item["path"], (rank, item))
    sem_by_path = {}
    for rank, item in enumerate(semantic_results, 1):
        sem_by_path.setdefault(item["path"], (rank, item))
    pages = set(bm_by_path) | set(sem_by_path)
    ranked = []
    for path in pages:
        score = 0.0
        if path in bm_by_path:
            score += 1.0 / (60 + bm_by_path[path][0])
        if path in sem_by_path:
            score += weight / (60 + sem_by_path[path][0])
        ranked.append((score, path))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    out = []
    for score, path in ranked[:limit]:
        if path in bm_by_path:
            item = dict(bm_by_path[path][1])
            item["bm25_rank"] = bm_by_path[path][0]
        else:
            item = dict(sem_by_path[path][1])
            item["bm25_rank"] = None
        item["semantic_rank"] = (sem_by_path[path][0]
                                 if path in sem_by_path else None)
        item["hybrid_score"] = round(score, 6)
        item["retrieval_mode"] = "hybrid-page-rrf"
        item["citation"] = item["path"] + "#" + item["section_id"]
        out.append(item)
    return out


def page_linear(bm25_results, semantic_results, weight=DEFAULT_WEIGHT,
                limit=5):
    """Linear page fusion with per-query min-max normalization."""
    bm = {}
    for item in bm25_results:
        if item["path"] not in bm or item.get("score", 0) > bm[item["path"]].get("score", 0):
            bm[item["path"]] = item
    sem = {}
    for item in semantic_results:
        if item["path"] not in sem or item.get("score", 0) > sem[item["path"]].get("score", 0):
            sem[item["path"]] = item
    bm_values = [item.get("score", 0) for item in bm.values()] or [0]
    sem_values = [item.get("score", 0) for item in sem.values()] or [0]
    bmin, bmax = min(bm_values), max(bm_values)
    smin, smax = min(sem_values), max(sem_values)
    pages = set(bm) | set(sem)
    ordered = []
    for path in pages:
        bscore = ((bm[path].get("score", 0) - bmin) / (bmax - bmin)
                  if path in bm and bmax > bmin else (1.0 if path in bm else 0.0))
        sscore = ((sem[path].get("score", 0) - smin) / (smax - smin)
                  if path in sem and smax > smin else 0.0)
        score = (1 - weight) * bscore + weight * sscore
        ordered.append((score, path))
    ordered.sort(key=lambda item: (-item[0], item[1]))
    bm_rank = {path: rank for rank, path in enumerate(
        sorted(bm, key=lambda p: -bm[p].get("score", 0)), 1)}
    sem_rank = {path: rank for rank, path in enumerate(
        sorted(sem, key=lambda p: -sem[p].get("score", 0)), 1)}
    out = []
    for score, path in ordered[:limit]:
        item = dict(bm.get(path) or sem[path])
        item["bm25_rank"] = bm_rank.get(path)
        item["semantic_rank"] = sem_rank.get(path)
        item["hybrid_score"] = round(score, 6)
        item["retrieval_mode"] = "hybrid-page-linear"
        item["citation"] = item["path"] + "#" + item["section_id"]
        out.append(item)
    return out


def search(root, query, limit=5, weight=DEFAULT_WEIGHT,
           model_name=DEFAULT_MODEL, embeddings=DEFAULT_EMBEDDINGS,
           index_path=None, fusion="rrf"):
    import section_search
    matrix, data, _ = load_embeddings(root, model_name, embeddings)
    semantic = semantic_results(root, query, load_model(model_name),
                                matrix, data)
    bm25 = section_search.search(
        root, query, limit=20, abstain=False, index_path=index_path).get(
            "results", [])
    return {
        "status": "ok" if bm25 or semantic else "no-results",
        "query": query,
        "retrieval_mode": "hybrid-page-" + fusion,
        "weight": weight,
        "results": (page_rrf(bm25, semantic, weight, limit)
                    if fusion == "rrf"
                    else page_linear(bm25, semantic, weight, limit)),
        "notice": "BM25 remains the default; hybrid is diagnostic.",
    }


def evaluate(root, weight=DEFAULT_WEIGHT, model_name=DEFAULT_MODEL):
    import section_search
    rows = []
    for split, relative in (("v2", "evaluation/corpus-qrels.v2.json"),
                            ("p3", "evaluation/agent-qrels.phase3.json")):
        data = json.loads((Path(root) / relative).read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if split == "p3" and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            rows.append((split, item))
    matrix, data, _ = load_embeddings(root, model_name)
    model = load_model(model_name)
    values = []
    for split, item in rows:
        semantic = semantic_results(root, item["question"], model,
                                    matrix, data)
        bm25 = section_search.search(
            root, item["question"], limit=20, abstain=False).get("results", [])
        results = page_rrf(bm25, semantic, weight, 5)
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
    return {"status": "diagnostic", "weight": weight,
            "all": summary(values),
            "v2": summary([v for v in values if v[0] == "v2"]),
            "p3": summary([v for v in values if v[0] == "p3"]),
            "notice": "Stale qrels; no quality claim."}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("build", "search", "evaluate"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--query")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--weight", type=float, default=DEFAULT_WEIGHT)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--embeddings", type=Path, default=DEFAULT_EMBEDDINGS)
    ap.add_argument("--fusion", choices=("rrf", "linear"), default="rrf")
    args = ap.parse_args(argv)
    if args.action == "build":
        print(json.dumps(build(args.root, args.model, args.embeddings),
                         indent=2, sort_keys=True))
        return 0
    if args.action == "evaluate":
        print(json.dumps(evaluate(args.root, args.weight, args.model),
                         indent=2, sort_keys=True))
        return 0
    if not args.query:
        raise SystemExit("--query is required for search")
    print(json.dumps(search(args.root, args.query, args.limit, args.weight,
                            args.model, args.embeddings, fusion=args.fusion),
                     indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
