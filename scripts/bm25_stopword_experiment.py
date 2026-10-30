#!/usr/bin/env python3
"""Compare BM25 with and without common query stopwords."""
import argparse
import json
import re
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]
STOP = frozenset("""
a an and are as at be been being but by can could did do does for from had has
have how if in into is it its may might must not of on or should so than that
the their them then there these they this those to was were what when where
which who why will with would you your
""".split())


def strip_query(query):
    words = re.findall(r"[A-Za-z0-9]+", query)
    kept = [word for word in words if word.casefold() not in STOP]
    return " ".join(kept) or query


def evaluate(root, page_qrels, section_qrels, strip):
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
    n = len(page_qrels["items"])
    for item in page_qrels["items"]:
        query = strip_query(item["question"]) if strip else item["question"]
        result = section_search.search(
            root, query, limit=5, abstain=False, section_rerank=False)
        page_keys = [row["path"] for row in result.get("results", [])]
        section_keys = [row["section_key"]
                        for row in result.get("results", [])]
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
            "baseline": evaluate(args.root, page, section, False),
            "stopwords": evaluate(args.root, page, section, True),
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
