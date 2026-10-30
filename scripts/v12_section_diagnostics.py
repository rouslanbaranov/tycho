#!/usr/bin/env python3
"""V12 section rank diagnostics on qrels v4."""
import argparse
import json
from collections import Counter
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def first_rank(keys, accepted):
    for index, key in enumerate(keys, 1):
        if key in accepted:
            return index
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page_qrels = json.loads(
        (args.root / "evaluation/corpus-qrels.v4.json").read_text(
            encoding="utf-8"))
    section_qrels = json.loads(
        (args.root / "evaluation/section-qrels.v4.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section_qrels["items"]}
    rows = []
    for item in page_qrels["items"]:
        if item["split"] != "v12":
            continue
        section_item = sections[item["id"]]
        result = section_search.search(
            args.root, item["question"], limit=10, abstain=False,
            section_rerank=False, volume="v12")
        paths = [row["path"] for row in result.get("results", [])]
        keys = [row["section_key"] for row in result.get("results", [])]
        page_accepted = set(item["accepted"])
        section_accepted = set(section_item["accepted"])
        rows.append({
            "id": item["id"],
            "question": item["question"],
            "section_rank": first_rank(keys, section_accepted),
            "page_rank": first_rank(paths, page_accepted),
            "top1_page_accepted": bool(paths and paths[0] in page_accepted),
            "top1_section_accepted": bool(keys and keys[0] in section_accepted),
            "top1_section": keys[0] if keys else None,
            "accepted_sections": sorted(section_accepted),
            "accepted_pages": sorted(page_accepted),
        })
    summary = {
        "n": len(rows),
        "top1_section": sum(1 for row in rows if row["top1_section_accepted"]),
        "top1_page": sum(1 for row in rows if row["top1_page_accepted"]),
        "section_rank": dict(sorted(Counter(
            row["section_rank"] for row in rows).items())),
        "page_rank": dict(sorted(Counter(
            row["page_rank"] for row in rows).items())),
        "section_miss_with_page_top1": sum(
            1 for row in rows
            if row["top1_page_accepted"] and not row["top1_section_accepted"]),
        "misses": [row for row in rows if not row["top1_section_accepted"]],
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
