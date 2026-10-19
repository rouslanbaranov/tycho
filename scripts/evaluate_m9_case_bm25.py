#!/usr/bin/env python3
"""Offline *diagnostic* BM25 candidate recall for Tycho M9 public case drafts.

This intentionally does NOT create a production index, execute MCP, answer
questions, validate company claims or measure tokens/latency. Its intended use
is as a reproducible lexical baseline before K18–K23 retrieval exists.

From the repository root:
    python3 scripts/evaluate_m9_case_bm25.py
    python3 scripts/evaluate_m9_case_bm25.py --output /tmp/m9-bm25.json
"""
from __future__ import annotations

import argparse
import collections
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STOP = set("a an and are as at be been by can could did do does for from had "
           "has have how in into is it its of on or our should that the their "
           "then these this to was were what when where which while why will with "
           "would we you your after before than using use about same through only "
           "any all one more what exact".split())
CASE_RE = re.compile(r"case\.[a-z][a-z0-9-]*\.[a-z][a-z0-9-]*")
K1 = 1.2
B = 0.75
KINDS = ("answerable", "reject_false_claim", "insufficient_evidence")


def tokenize(text: str) -> list[str]:
    return [term for term in re.findall(r"[a-z0-9]+", text.lower())
            if len(term) >= 3 and term not in STOP]


def source_tokens(text: str) -> list[str]:
    # Exact same minimal link/path masking as the captured 2026-10-19 JS pilot.
    text = re.sub(r"\]\([^)]*\)", "]", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"case\.[a-z0-9.-]+", "", text)
    return tokenize(text)


def collect(root: Path, fixtures: list[dict]) -> list[dict]:
    index = (root / "book/cases/README.md").read_text(encoding="utf-8")
    relative = re.findall(r"\]\(([^)#]+\.md)\)", index)
    paths = [x for x in relative if not x.startswith("../") and not x.startswith("decisions/")]
    assert len(paths) == len(set(paths)), "duplicate case filenames"
    assert paths, "empty case index"
    words = {t for q in fixtures for t in tokenize(q["query"])}
    docs = []
    for filename in paths:
        data = (root / "book/cases" / filename).read_text(encoding="utf-8")
        match = CASE_RE.search(data)
        if match is None:
            raise ValueError(filename + ": no stable case ID")
        body_tokens = source_tokens(data)
        tf = collections.Counter(t for t in body_tokens if t in words)
        docs.append(dict(id=match.group(), path=filename, length=len(body_tokens), tf=tf))
    if len({d["id"] for d in docs}) != len(docs):
        raise ValueError("duplicate case IDs")
    return docs


def rank(q: str, docs: list[dict], df: dict[str, int], avglen: float) -> list[str]:
    count = len(docs)
    scored = []
    for d in docs:
        score = 0.0
        for t in set(tokenize(q)):
            f = d["tf"].get(t, 0)
            if f:
                n = df[t]
                idf = math.log(1.0 + (count - n + 0.5) / (n + 0.5))
                score += idf * (f * (K1 + 1.0)) / (
                    f + K1 * (1.0 - B + B * d["length"] / avglen))
        scored.append((d["id"], score))
    # Stable tie ordering is necessary for identical zero-score candidates.
    return [cid for cid, _ in sorted(scored, key=lambda item: (-item[1], item[0]))]


def measure(rows: list[dict]) -> dict:
    eligible = [r for r in rows if r["expected"]]
    out = {"queries": len(rows), "with_expected_case": len(eligible)}
    gold_total = sum(len(r["expected"]) for r in eligible)
    for k in (1, 3, 5, 10):
        hits = sum(any(rank <= k for rank in r["ranks"]) for r in eligible)
        found_pairs = sum(sum(rank <= k for rank in r["ranks"]) for r in eligible)
        out["hit_at_" + str(k)] = hits
        out["hit_rate_at_" + str(k)] = round(hits / len(eligible), 4) if eligible else None
        out["gold_pair_recall_at_" + str(k)] = (
            round(found_pairs / gold_total, 4) if gold_total else None)
    out["mrr"] = (round(sum(1.0 / min(r["ranks"]) for r in eligible)
                        / len(eligible), 4) if eligible else None)
    return out


def evaluate(root: Path) -> dict:
    fixtures = json.loads((root / "tests/fixtures/m9-case-queries.json")
                          .read_text(encoding="utf-8"))["questions"]
    docs = collect(root, fixtures)
    df: collections.Counter[str] = collections.Counter()
    for d in docs:
        df.update(d["tf"].keys())
    avglen = sum(d["length"] for d in docs) / len(docs)
    known = {d["id"] for d in docs}
    rows = []
    for fixture in fixtures:
        wanted = fixture["expected_case_ids"]
        if any(cid not in known for cid in wanted):
            raise ValueError(fixture["id"] + ": unknown case ID")
        ranked = rank(fixture["query"], docs, df, avglen)
        rows.append(dict(id=fixture["id"], behavior=fixture["expected_behavior"],
                         expected=wanted, ranks=[ranked.index(cid) + 1 for cid in wanted],
                         top3=ranked[:3]))
    if any(r["behavior"] not in KINDS for r in rows):
        raise ValueError("unknown fixture behavior")
    result = {
        "experiment": "Offline lexical candidate retrieval only (NOT MCP/answer quality)",
        "case_docs": len(docs),
        "fixture_count": len(fixtures),
        "tokenizer": "ASCII alphanumeric >=3 after fixed stopwords and URL/case-ID masking",
        "ranker": "BM25 k1=1.2 b=0.75, unique query terms, ties by case ID",
        "all": measure(rows),
        "by_behavior": {kind: measure([r for r in rows if r["behavior"] == kind])
                        for kind in KINDS},
        "answerable_misses_at_3": [
            dict(id=r["id"], expected_ranks=r["ranks"], top3=r["top3"])
            for r in rows if r["behavior"] == "answerable"
            and r["expected"] and not any(rank <= 3 for rank in r["ranks"])],
        "per_query": rows,
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    options = parser.parse_args()
    result = evaluate(ROOT)
    pretty = json.dumps(result, indent=2) + "\n"
    if options.output:
        options.output.write_text(pretty, encoding="utf-8")
    print(pretty)


if __name__ == "__main__":
    main()
