#!/usr/bin/env python3
"""Evaluate hierarchical page-to-section reranking on qrels v5-dense."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def evaluate(root, page_qrels, section_qrels, page_depth, limit=5):
    db, _ = section_search.open_snapshot(root)
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
    try:
        for item in page_qrels["items"]:
            terms = section_search.normalize_terms(item["question"])
            base = section_search.search(
                root, item["question"], limit=page_depth, abstain=False)
            keys = [row["section_key"] for row in base.get("results", [])]
            rows = section_search.load_sections(db, keys)
            selected = []
            for key in keys:
                row = rows.get(key)
                if row is not None:
                    selected.append((0.0, "seed", None, {
                        "section_key": key, "row": row,
                        "h2_score": None, "passage": None}))
            ranked = section_search.section_rerank_candidates(
                db, terms, selected, limit, [], [],
                ",".join(f"{value:g}" for value in section_search.bm25_weights()))
            result_rows = [entry[3]["row"] for entry in ranked]
            page_keys = [row["path"] for row in result_rows]
            section_keys = [row["section_key"] for row in result_rows]
            for index, k in enumerate((1, 3, 5)):
                counts["page"][index] += int(
                    bool(set(page_keys[:k]) & set(item["accepted"])))
                counts["section"][index] += int(
                    bool(set(section_keys[:k]) &
                         set(sections[item["id"]]["accepted"])))
    finally:
        db.close()
    n = len(page_qrels["items"])
    return {level: [round(value / n, 3) for value in values]
            for level, values in counts.items()}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page = json.loads(
        (args.root / "evaluation/corpus-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    section = json.loads(
        (args.root / "evaluation/section-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    output = {}
    for depth in (5, 10, 20):
        output[str(depth)] = evaluate(args.root, page, section, depth)
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
