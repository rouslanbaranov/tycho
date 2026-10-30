#!/usr/bin/env python3
"""Stable atlas rank prior on qrels v4/v3."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]
BOOSTS = (1.0, 1.1, 1.25, 1.5)
ATLAS = "book/volumes/v11-pattern-atlas/"


def evaluate(root, page_name, section_name, boost):
    page_qrels = json.loads((root / "evaluation" / page_name).read_text(
        encoding="utf-8"))
    section_qrels = json.loads((root / "evaluation" / section_name).read_text(
        encoding="utf-8"))
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
    n = len(page_qrels["items"])
    for item in page_qrels["items"]:
        base = section_search.search(
            root, item["question"], limit=20, abstain=False,
            section_rerank=False).get("results", [])
        ranked = sorted(
            enumerate(base, 1),
            key=lambda pair: (pair[0] / (
                boost if pair[1]["path"].startswith(ATLAS) else 1.0),
                pair[0]))
        rows = [row for _, row in ranked[:5]]
        page_keys = [row["path"] for row in rows]
        section_keys = [row["section_key"] for row in rows]
        page_accept = set(item["accepted"])
        section_accept = set(sections[item["id"]]["accepted"])
        for index, k in enumerate((1, 3, 5)):
            counts["page"][index] += int(
                bool(set(page_keys[:k]) & page_accept))
            counts["section"][index] += int(
                bool(set(section_keys[:k]) & section_accept))
    return {"n": n, **{level: [round(value / n, 3) for value in values]
                       for level, values in counts.items()}}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    output = {}
    for name, page, section in (
            ("v4", "corpus-qrels.v4.json", "section-qrels.v4.json"),
            ("v3", "corpus-qrels.v3.json", "section-qrels.v3.json")):
        output[name] = {str(boost): evaluate(args.root, page, section, boost)
                        for boost in BOOSTS}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
