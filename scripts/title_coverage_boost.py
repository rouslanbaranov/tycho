#!/usr/bin/env python3
"""Test post-hoc title coverage boosts on qrels v4/v3."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]
ALPHAS = (0.0, 0.1, 0.25, 0.5, 1.0)


def coverage(query_terms, title):
    if not query_terms:
        return 0.0
    folded = str(title or "").casefold()
    return sum(1 for term in set(query_terms) if term in folded) / len(
        set(query_terms))


def evaluate(root, page_qrels, section_qrels, alpha):
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
    n = len(page_qrels["items"])
    for item in page_qrels["items"]:
        terms = section_search.normalize_terms(item["question"])
        result = section_search.search(
            root, item["question"], limit=20, abstain=False,
            section_rerank=False).get("results", [])
        if alpha:
            ranked = sorted(
                enumerate(result, 1),
                key=lambda pair: (
                    -pair[1].get("score", 0.0)
                    * (1.0 + alpha * coverage(terms, pair[1].get("title"))),
                    pair[0]))
            rows = [row for _, row in ranked[:5]]
        else:
            rows = result[:5]
        page_keys = [row["path"] for row in rows]
        section_keys = [row["section_key"] for row in rows]
        page_accept = set(item["accepted"])
        section_accept = set(sections[item["id"]]["accepted"])
        for index, k in enumerate((1, 3, 5)):
            counts["page"][index] += int(
                bool(set(page_keys[:k]) & page_accept))
            counts["section"][index] += int(
                bool(set(section_keys[:k]) & section_accept))
    return {level: [round(value / n, 3) for value in values]
            for level, values in counts.items()}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    output = {}
    for name, page_name, section_name in (
            ("v4", "corpus-qrels.v4.json", "section-qrels.v4.json"),
            ("v3", "corpus-qrels.v3.json", "section-qrels.v3.json")):
        page = json.loads((args.root / "evaluation" / page_name).read_text(
            encoding="utf-8"))
        section = json.loads(
            (args.root / "evaluation" / section_name).read_text(
                encoding="utf-8"))
        output[name] = {
            str(alpha): evaluate(args.root, page, section, alpha)
            for alpha in ALPHAS
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
