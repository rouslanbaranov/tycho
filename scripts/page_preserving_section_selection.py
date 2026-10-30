#!/usr/bin/env python3
"""Rescore sections inside top pages while preserving page order."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def select_sections(db, query, paths):
    terms = section_search.normalize_terms(query)
    weight_sql = ",".join(f"{value:g}" for value in section_search.bm25_weights())
    selected = []
    for path in paths:
        sql = ("SELECT " + section_search.sections_select()
               + ",bm25(fts,0.0," + weight_sql + ") AS rank"
               " FROM fts JOIN sections s ON s.section_key = fts.section_key"
               " WHERE fts MATCH ? AND s.path = ?"
               " ORDER BY rank ASC LIMIT 200")
        rows = db.execute(
            sql, [section_search.match_expression(terms), path]).fetchall()
        scored = []
        for row in rows:
            text = (row["heading"] + " " + row["content"]).casefold()
            hits = sum(1 for term in set(terms) if term in text)
            heading_hits = sum(1 for term in set(terms)
                               if term in row["heading"].casefold())
            scored.append((hits * 1000 + heading_hits * 10 - row["rank"],
                           row["section_key"]))
        scored.sort(key=lambda item: (-item[0], item[1]))
        if scored:
            selected.append(scored[0][1])
    return selected


def evaluate(root, page_name, section_name):
    page_qrels = json.loads((root / "evaluation" / page_name).read_text(
        encoding="utf-8"))
    section_qrels = json.loads((root / "evaluation" / section_name).read_text(
        encoding="utf-8"))
    sections = {item["id"]: item for item in section_qrels["items"]}
    db, _ = section_search.open_snapshot(root)
    hits = [0, 0, 0]
    n = 0
    try:
        for item in page_qrels["items"]:
            n += 1
            base = section_search.search(
                root, item["question"], limit=5, abstain=False,
                section_rerank=False).get("results", [])
            paths = list(dict.fromkeys(row["path"] for row in base))
            keys = select_sections(db, item["question"], paths)
            accepted = set(sections[item["id"]]["accepted"])
            for index, k in enumerate((1, 3, 5)):
                hits[index] += int(bool(set(keys[:k]) & accepted))
    finally:
        db.close()
    return {"n": n, "section": [round(value / n, 3) for value in hits]}


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
