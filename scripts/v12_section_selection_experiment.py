#!/usr/bin/env python3
"""Test section reranking inside top V12 pages on qrels v4/v3."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def rerank_sections(db, query, paths):
    terms = section_search.normalize_terms(query)
    weight_sql = ",".join(f"{value:g}" for value in section_search.bm25_weights())
    placeholders = ",".join("?" * len(paths))
    sql = ("SELECT " + section_search.sections_select()
           + ",bm25(fts,0.0," + weight_sql + ") AS rank"
           " FROM fts JOIN sections s ON s.section_key = fts.section_key"
           " WHERE fts MATCH ? AND s.volume = 'v12'"
           " AND s.path IN (" + placeholders + ")"
           " ORDER BY rank ASC LIMIT 200")
    rows = db.execute(
        sql, [section_search.match_expression(terms)] + paths).fetchall()
    scored = []
    for row in rows:
        text = (row["heading"] + " " + row["content"]).casefold()
        hits = sum(1 for term in set(terms) if term in text)
        heading_hits = sum(1 for term in set(terms)
                           if term in row["heading"].casefold())
        scored.append((hits * 1000 + heading_hits * 10 - row["rank"],
                       row["section_key"]))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [key for _, key in scored[:5]]


def evaluate(root, qrels_name, section_name):
    page_qrels = json.loads((root / "evaluation" / qrels_name).read_text(
        encoding="utf-8"))
    section_qrels = json.loads((root / "evaluation" / section_name).read_text(
        encoding="utf-8"))
    sections = {item["id"]: item for item in section_qrels["items"]}
    db, _ = section_search.open_snapshot(root)
    base = [0, 0, 0]
    reranked = [0, 0, 0]
    n = 0
    try:
        for item in page_qrels["items"]:
            if item["split"] != "v12":
                continue
            n += 1
            result = section_search.search(
                root, item["question"], limit=5, abstain=False,
                section_rerank=False, volume="v12")
            paths = list(dict.fromkeys(
                row["path"] for row in result.get("results", [])))
            keys = [row["section_key"] for row in result.get("results", [])]
            accepted = set(sections[item["id"]]["accepted"])
            new_keys = rerank_sections(db, item["question"], paths)
            for index, k in enumerate((1, 3, 5)):
                base[index] += int(bool(set(keys[:k]) & accepted))
                reranked[index] += int(bool(set(new_keys[:k]) & accepted))
    finally:
        db.close()
    return {"n": n, "base": [round(v / n, 3) for v in base],
            "reranked": [round(v / n, 3) for v in reranked]}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    output = {
        "v4": evaluate(args.root, "corpus-qrels.v4.json",
                       "section-qrels.v4.json"),
        "v3": evaluate(args.root, "corpus-qrels.v3.json",
                       "section-qrels.v3.json"),
    }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
