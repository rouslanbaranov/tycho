#!/usr/bin/env python3
"""Recall@k on frozen qrels using the section FTS index."""
import argparse, json
from pathlib import Path
import section_search

ROOT = Path(__file__).resolve().parents[1]

def load_qrels(path):
    return json.loads(Path(path).read_text())

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--qrels", type=Path, required=True)
    ap.add_argument("--level", choices=("page", "section"), required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--ks", default="5,10,20,50")
    args = ap.parse_args(argv)
    ks = [int(x) for x in args.ks.split(",")]
    data = load_qrels(args.qrels)
    db, manifest = section_search.open_snapshot(args.root, None)
    weight_sql = ",".join(f"{v:g}" for v in section_search.bm25_weights())
    sql = ("SELECT s.section_key, s.path, bm25(fts,0.0," + weight_sql + ") AS rank"
           " FROM fts JOIN sections s ON s.section_key = fts.section_key"
           " WHERE fts MATCH ? ORDER BY rank ASC, s.section_key ASC LIMIT ?")
    totals = {k: 0 for k in ks}; hits = {k: 0 for k in ks}; denom = 0
    per = {}
    try:
        for item in data["items"]:
            terms = section_search.normalize_terms(item["question"])
            rows = db.execute(sql, [section_search.match_expression(terms), max(ks)]).fetchall()
            returned = [(r["section_key"], r["path"]) for r in rows]
            accepted = item.get("accepted", [])
            denom += len(accepted)
            rec = {"accepted": len(accepted), "retrieved": len(returned)}
            for k in ks:
                window = returned[:k]
                if args.level == "page":
                    got = {p for _, p in window}
                    want = set(accepted)
                else:
                    got = {s for s, _ in window}
                    want = set(accepted)
                hit = len(got & want)
                totals[k] += hit; hits[k] += hit
                rec["recall@%d" % k] = round(hit / len(want), 4) if want else 0.0
                rec["hit@%d" % k] = hit
            per[item["id"]] = rec
    finally:
        db.close()
    out = {"qrels": str(args.qrels), "level": args.level,
           "snapshot": manifest["snapshot_id"], "ks": ks,
           "micro_recall": {str(k): round(hits[k] / denom, 6) for k in ks},
           "accepted_total": denom, "items": per,
           "limits": "AI qrels, pool-relative; offline FTS, no rerank."}
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
