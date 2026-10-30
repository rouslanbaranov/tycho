#!/usr/bin/env python3
"""Evaluate a cross-encoder reranker over BM25 top-20 on v5-dense."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--model", default="cross-encoder/ms-marco-MiniLM-L-6-v2")
    args = ap.parse_args(argv)
    from sentence_transformers import CrossEncoder
    page = json.loads(
        (args.root / "evaluation/corpus-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    section = json.loads(
        (args.root / "evaluation/section-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section["items"]}
    model = CrossEncoder(args.model)
    counts = {"bm25": {"page": [0, 0, 0], "section": [0, 0, 0]},
              "cross": {"page": [0, 0, 0], "section": [0, 0, 0]}}
    for item in page["items"]:
        base = section_search.search(
            args.root, item["question"], limit=20, abstain=False)
        rows = base.get("results", [])
        base_keys = [row["section_key"] for row in rows]
        base_paths = [row["path"] for row in rows]
        section_accepted = set(sections[item["id"]]["accepted"])
        page_accepted = set(item["accepted"])
        for index, k in enumerate((1, 3, 5)):
            counts["bm25"]["page"][index] += int(
                bool(set(base_paths[:k]) & page_accepted))
            counts["bm25"]["section"][index] += int(
                bool(set(base_keys[:k]) & section_accepted))
        pairs = [(item["question"],
                  " ".join(str(row.get(key, "")) for key in
                           ("title", "heading", "content"))[:4000])
                 for row in rows]
        scores = model.predict(pairs, show_progress_bar=False)
        order = sorted(range(len(rows)), key=lambda i: (-float(scores[i]),
                                                        rows[i]["section_key"]))
        ranked = [rows[i] for i in order]
        keys = [row["section_key"] for row in ranked]
        paths = [row["path"] for row in ranked]
        for index, k in enumerate((1, 3, 5)):
            counts["cross"]["page"][index] += int(
                bool(set(paths[:k]) & page_accepted))
            counts["cross"]["section"][index] += int(
                bool(set(keys[:k]) & section_accepted))
    n = len(page["items"])
    output = {name: {level: [round(value / n, 3) for value in values]
                     for level, values in levels.items()}
              for name, levels in counts.items()}
    print(json.dumps({"model": args.model, "metrics": output}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
