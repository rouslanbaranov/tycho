#!/usr/bin/env python3
"""Optional semantic retrieval experiment over H2 sections.

Uses model2vec static embeddings. This is a diagnostic CLI, not the default
search path and not a quality or sufficiency claim.
"""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "generated/sections-fts-v4.sqlite"
DEFAULT_MODEL = "minishlab/potion-base-8M"


def load_sections(root):
    with sqlite3.connect(str(DEFAULT_INDEX)) as db:
        db.row_factory = sqlite3.Row
        rows = db.execute(
            "select section_key,section_id,path,heading,content"
            " from sections where heading_level=2").fetchall()
    return [dict(row) for row in rows]


def embed(model, texts):
    import numpy as np
    matrix = np.asarray(model.encode(texts, show_progress_bar=False),
                        dtype="float32")
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True).clip(min=1e-9)
    return matrix


def rank_vector(query, model, rows, matrix, limit):
    import numpy as np
    vector = np.asarray(model.encode([query], show_progress_bar=False)[0],
                        dtype="float32")
    vector /= max(float(np.linalg.norm(vector)), 1e-9)
    order = np.argsort(-(matrix @ vector))[:limit]
    return [{"path": rows[i]["path"], "section_id": rows[i]["section_id"],
             "section_key": rows[i]["section_key"]} for i in order]


def rrf(primary, vector, limit):
    scores = {}
    by_key = {item["section_key"]: item for item in primary}
    for rank, item in enumerate(primary, 1):
        scores[item["section_key"]] = scores.get(
            item["section_key"], 0.0) + 1.0 / (60 + rank)
    for rank, item in enumerate(vector, 1):
        scores[item["section_key"]] = scores.get(
            item["section_key"], 0.0) + 1.0 / (60 + rank)
    out = []
    seen_docs = set()
    for key in sorted(scores, key=scores.get, reverse=True):
        item = by_key.get(key)
        if item is None:
            item = next(x for x in vector if x["section_key"] == key)
        if item["path"] in seen_docs:
            continue
        seen_docs.add(item["path"])
        out.append(item)
        if len(out) == limit:
            break
    return out


def accepted(item):
    return {(a["path"], a["section_id"]) for a in item["accepted"]}


def hit(results, item, limit=5):
    wanted = accepted(item)
    for rank, result in enumerate(results[:limit], 1):
        if (result["path"], result["section_id"]) in wanted:
            return rank
        if (result["path"], None) in wanted:
            return rank
    return None


def evaluate(root, model_name, limit):
    from model2vec import StaticModel
    import section_search
    rows = load_sections(root)
    model = StaticModel.from_pretrained(model_name)
    matrix = embed(model, [r["heading"] + "\n" + r["content"] for r in rows])
    qrels = []
    for path in ("evaluation/corpus-qrels.v2.json",
                 "evaluation/agent-qrels.phase3.json"):
        data = json.loads((root / path).read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if path.endswith("phase3.json") and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            qrels.append({"id": item["id"], "split": path.split(".")[-2],
                          "question": item["question"],
                          "accepted": item.get("accepted", [])})
    results = {"bm25": [], "vector": [], "hybrid": []}
    for item in qrels:
        primary = section_search.search(
            root, item["question"], limit=20, abstain=False).get("results", [])
        vector = rank_vector(item["question"], model, rows, matrix, 20)
        hybrid = rrf(primary, vector, 5)
        results["bm25"].append(hit(primary[:5], item))
        results["vector"].append(hit(vector, item))
        results["hybrid"].append(hit(hybrid, item))
    def summary(values):
        return {k: round(sum(1 for rank in values if rank and rank <= k)
                         / len(values), 3) for k in (1, 3, 5)}
    return {
        "model": model_name,
        "sections": len(rows),
        "queries": len(qrels),
        "hit": {name: summary(values) for name, values in results.items()},
        "notice": "Diagnostic only; semantic default is not enabled.",
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--query")
    ap.add_argument("--evaluate", action="store_true")
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    if args.evaluate:
        print(json.dumps(evaluate(args.root, args.model, args.limit),
                         indent=2, sort_keys=True))
        return 0
    if not args.query:
        raise SystemExit("provide --query or --evaluate")
    from model2vec import StaticModel
    rows = load_sections(args.root)
    model = StaticModel.from_pretrained(args.model)
    matrix = embed(model, [r["heading"] + "\n" + r["content"] for r in rows])
    print(json.dumps(rank_vector(args.query, model, rows, matrix,
                                 args.limit), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
