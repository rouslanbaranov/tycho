#!/usr/bin/env python3
"""Evaluate fixed section-aware reranking on a section-labelled qrels file."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--qrels", required=True)
    ap.add_argument("--answerable-field", default="final_label")
    ap.add_argument("--pages", type=int, default=5)
    ap.add_argument("--sections", type=int, default=5)
    args = ap.parse_args(argv)
    weights = ",".join(f"{value:g}" for value in section_search.bm25_weights())
    data = json.loads((args.root / args.qrels).read_text(encoding="utf-8"))
    db, _ = section_search.open_snapshot(args.root)
    rows = []
    for item in data["items"]:
        if item.get(args.answerable_field) != "answerable":
            continue
        terms = section_search.normalize_terms(item["question"])
        expression = section_search.match_expression(terms)
        accepted = {(entry["path"], entry.get("section_id"))
                    for entry in item.get("accepted", [])}
        base = section_search.search(
            args.root, item["question"], limit=args.pages, abstain=False)
        pages = [row["path"] for row in base.get("results", [])]
        candidates = []
        for page in pages:
            sql = ("SELECT s.section_id,s.heading,s.content,"
                   "bm25(fts,0.0," + weights + ") AS rank"
                   " FROM fts JOIN sections s ON s.section_key=fts.section_key"
                   " WHERE fts MATCH ? AND s.path=? ORDER BY rank LIMIT 100")
            for result in db.execute(sql, [expression, page]).fetchall():
                text = (result["heading"] + " " + result["content"]).casefold()
                hits = sum(1 for term in set(terms) if term in text)
                heading = sum(1 for term in set(terms)
                              if term in result["heading"].casefold())
                candidates.append((hits, heading, -result["rank"],
                                   page, result["section_id"]))
        candidates.sort(reverse=True)
        chosen = [(page, section) for _, _, _, page, section
                  in candidates[:args.sections]]
        base_pairs = [(row["path"], row.get("section_id"))
                      for row in base.get("results", [])]
        def hit(pairs, k):
            return bool(set(pairs[:k]) & accepted)
        rows.append({"id": item["id"],
                     "base": [hit(base_pairs, k) for k in (1, 3, 5)],
                     "reranked": [hit(chosen, k) for k in (1, 3, 5)]})
    db.close()

    def rate(key, index):
        return round(sum(row[key][index] for row in rows) / len(rows), 3)

    output = {"qrels": args.qrels, "n": len(rows),
              "base": [rate("base", i) for i in range(3)],
              "reranked": [rate("reranked", i) for i in range(3)],
              "rows": rows,
              "limits": "Section-labelled qrels; diagnostic, not production."}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
