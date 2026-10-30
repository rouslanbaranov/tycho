#!/usr/bin/env python3
"""Test atlas auto-routing against qrels v4."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

ATLAS = "book/volumes/v11-pattern-atlas/"


def text_score(terms, document):
    text = " ".join([
        str(document.get("title") or ""),
        str(document.get("summary") or ""),
        " ".join(document.get("questions") or []),
        " ".join(document.get("keywords") or []),
    ]).casefold()
    return sum(1 for term in set(terms) if term in text)


def classify(terms, atlas_docs, book_docs, threshold):
    atlas = max((text_score(terms, d) for d in atlas_docs), default=0)
    book = max((text_score(terms, d) for d in book_docs), default=0)
    return atlas >= threshold and atlas > book


def evaluate(root, page_qrels, section_qrels, mode, threshold):
    sections = {item["id"]: item for item in section_qrels["items"]}
    route_docs = json.loads(
        (root / "generated/route-index.v1.json").read_text(
            encoding="utf-8"))["documents"]
    atlas_docs = [d for d in route_docs if str(d.get("path", "")).startswith(ATLAS)]
    book_docs = [d for d in route_docs if not str(d.get("path", "")).startswith(ATLAS)]
    counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
    n = len(page_qrels["items"])
    routed = 0
    for item in page_qrels["items"]:
        terms = section_search.normalize_terms(item["question"])
        volume = None
        if mode == "oracle":
            volume = "v11" if item["split"] == "atlas" else None
        elif mode == "auto" and classify(terms, atlas_docs, book_docs, threshold):
            volume = "v11"
            routed += 1
        result = section_search.search(
            root, item["question"], limit=5, abstain=False,
            section_rerank=False, volume=volume)
        page_keys = [row["path"] for row in result.get("results", [])]
        section_keys = [row["section_key"] for row in result.get("results", [])]
        page_accept = set(item["accepted"])
        section_accept = set(sections[item["id"]]["accepted"])
        for index, k in enumerate((1, 3, 5)):
            counts["page"][index] += int(
                bool(set(page_keys[:k]) & page_accept))
            counts["section"][index] += int(
                bool(set(section_keys[:k]) & section_accept))
    return {"n": n, "routed": routed,
            **{level: [round(value / n, 3) for value in values]
               for level, values in counts.items()}}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page = json.loads((args.root / "evaluation/corpus-qrels.v4.json")
                      .read_text(encoding="utf-8"))
    section = json.loads((args.root / "evaluation/section-qrels.v4.json")
                         .read_text(encoding="utf-8"))
    output = {}
    for threshold in (1, 2, 3, 4):
        output[str(threshold)] = evaluate(
            args.root, page, section, "auto", threshold)
    output["oracle"] = evaluate(args.root, page, section, "oracle", 0)
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
