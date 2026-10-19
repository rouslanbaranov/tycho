#!/usr/bin/env python3
"""Small, reproducible lexical *pilot*, not a production sizing benchmark.

Compares SQLite FTS5/BM25 with a parameterized SQL LIKE scan on identical
original synthetic documents and predeclared relevance labels. No network,
embedding, private data or background services. Reports measured local cost.
"""
import argparse
import json
import math
from pathlib import Path
import re
import sqlite3
import statistics
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures" / "lexical-engine-pilot.json"
WORD = re.compile(r"(?u)\w+")


def tokens(q):
    terms = WORD.findall(q.lower())
    if not terms or len(terms) > 12 or any(len(t) > 64 for t in terms):
        raise ValueError("Query must contain 1..12 bounded lexical tokens")
    return terms


def fts_query(query):
    return " OR ".join('"' + t.replace('"', '""') + '"' for t in tokens(query))


def validate_fixture(data):
    if not isinstance(data, dict) or set(data) != {"version", "scope", "documents", "questions"}:
        raise ValueError("Unexpected benchmark fields")
    if data["version"] != 1 or not isinstance(data["documents"], list):
        raise ValueError("Unsupported benchmark version")
    ids = set()
    for doc in data["documents"]:
        if set(doc) != {"id", "title", "body"} or not all(isinstance(doc[x], str) and doc[x] for x in doc):
            raise ValueError("Invalid document fixture")
        if doc["id"] in ids:
            raise ValueError("Duplicate document id")
        ids.add(doc["id"])
    if not 3 <= len(ids) <= 5000:
        raise ValueError("Bound pilot size outside expected scope")
    if not data["questions"]:
        raise ValueError("Missing relevance questions")
    for q in data["questions"]:
        if set(q) != {"query", "relevant_ids", "case"} or not isinstance(q["case"], str):
            raise ValueError("Invalid query fixture")
        tokens(q["query"])
        if not q["relevant_ids"] or not set(q["relevant_ids"]) <= ids:
            raise ValueError("Relevance labels must resolve to pilot corpus")
    return data


def build_sqlite(path, documents):
    db = sqlite3.connect(str(path))
    try:
        db.execute("CREATE TABLE pages(docid TEXT PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL)")
        db.execute("CREATE VIRTUAL TABLE fts USING fts5(docid UNINDEXED, title, body, tokenize='unicode61')")
    except sqlite3.OperationalError as exc:
        db.close()
        raise RuntimeError("SQLite FTS5 is required for the benchmark") from exc
    for d in documents:
        db.execute("INSERT INTO pages(docid,title,body) VALUES(?,?,?)", (d["id"], d["title"], d["body"]))
        db.execute("INSERT INTO fts(docid,title,body) VALUES(?,?,?)", (d["id"], d["title"], d["body"]))
    db.commit()
    return db


def search(db, query, engine, k=5):
    if not 1 <= k <= 100:
        raise ValueError("Invalid top-k")
    terms = tokens(query)
    if engine == "fts5":
        rows = db.execute(
            "SELECT docid FROM fts WHERE fts MATCH ? ORDER BY bm25(fts,0.0,5.0,1.0),docid LIMIT ?",
            (fts_query(query), k),
        ).fetchall()
    elif engine == "like":
        # Basic scan with an explicit comparable ANY-token retrieval policy.
        cond = " OR ".join(["instr(lower(title || ' ' || body), ?) > 0"] * len(terms))
        weight = " + ".join(["(5 * (length(lower(title))-length(replace(lower(title), ?, ''))) + "
                             "(length(lower(body))-length(replace(lower(body), ?, ''))))"] * len(terms))
        params = ["%" if not t else t for t in terms]
        rows = db.execute(
            "SELECT docid FROM pages WHERE " + cond + " ORDER BY (" + weight + ") DESC,docid LIMIT ?",
            tuple(params + [v for t in params for v in (t, t)] + [k]),
        ).fetchall()
    else:
        raise ValueError("Unknown engine")
    return [r[0] for r in rows]


def score(questions, retrieved):
    rr = []
    recall = []
    for q, ranked in zip(questions, retrieved):
        good = set(q["relevant_ids"])
        first = next((i for i, d in enumerate(ranked, 1) if d in good), None)
        rr.append(0.0 if first is None else 1.0 / first)
        recall.append(len(set(ranked) & good) / len(good))
    return {"mrr_at_5": round(statistics.mean(rr), 4),
            "mean_recall_at_5": round(statistics.mean(recall), 4)}


def bench(fixtures, repeats=100):
    validate_fixture(fixtures)
    if not 1 <= repeats <= 5000:
        raise ValueError("Repeat budget out of range")
    with tempfile.TemporaryDirectory(prefix="tycho-fts5-") as temp:
        path = Path(temp) / "pilot.sqlite"
        start = time.perf_counter_ns()
        db = build_sqlite(path, fixtures["documents"])
        build_ms = (time.perf_counter_ns() - start) / 1e6
        size = path.stat().st_size
        report = {}
        for engine in ("fts5", "like"):
            expected = [search(db, q["query"], engine) for q in fixtures["questions"]]
            durations = []
            # Warm-ups are real calls, excluded from latency samples.
            for q in fixtures["questions"]:
                search(db, q["query"], engine)
            for _ in range(repeats):
                for q in fixtures["questions"]:
                    t = time.perf_counter_ns()
                    search(db, q["query"], engine)
                    durations.append((time.perf_counter_ns() - t) / 1e6)
            durations.sort()
            report[engine] = {**score(fixtures["questions"], expected),
                              "median_ms": round(statistics.median(durations), 5),
                              "p95_ms": round(durations[math.ceil(0.95 * len(durations))-1], 5),
                              "results": [{"case": q["case"], "ranked_ids": x}
                                          for q, x in zip(fixtures["questions"], expected)]}
        db.close()
        return {"corpus": "original-synthetic-only",
                "documents": len(fixtures["documents"]), "queries": len(fixtures["questions"]),
                "repeats_per_query": repeats, "sqlite_version": sqlite3.sqlite_version,
                "index_and_content_db_bytes": size, "fts5_and_table_build_ms": round(build_ms, 5),
                "engines": report,
                "limits": ["tiny synthetic corpus; not production SLO or scaling evidence",
                           "cold cache and concurrency not measured",
                           "LIKE scans have different substring matching semantics",
                           "this file size includes both document table and FTS index"]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fixtures", type=Path, default=FIXTURES)
    p.add_argument("--repeats", type=int, default=100)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    if args.output and args.output.exists():
        p.error("Refuse to overwrite an existing benchmark result")
    data = json.loads(args.fixtures.read_text(encoding="utf-8"))
    result = bench(data, args.repeats)
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
