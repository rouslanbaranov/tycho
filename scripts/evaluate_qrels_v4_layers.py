#!/usr/bin/env python3
"""BM25 page/section metrics with atlas/V12 volume scoping."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]
VOLUME = {"atlas": "v11", "v12": "v12"}


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
    hits = {split: {"page": [0, 0, 0], "section": [0, 0, 0]}
            for split in ("book", "atlas", "v12", "all")}
    totals = {split: 0 for split in hits}
    for item in page_qrels["items"]:
        result = section_search.search(
            args.root, item["question"], limit=5, abstain=False,
            section_rerank=False, volume=VOLUME.get(item["split"]))
        page_keys = [row["path"] for row in result.get("results", [])]
        section_keys = [row["section_key"]
                        for row in result.get("results", [])]
        page_accept = set(item["accepted"])
        section_accept = set(sections[item["id"]]["accepted"])
        for split in (item["split"], "all"):
            totals[split] += 1
            for index, k in enumerate((1, 3, 5)):
                hits[split]["page"][index] += int(
                    bool(set(page_keys[:k]) & page_accept))
                hits[split]["section"][index] += int(
                    bool(set(section_keys[:k]) & section_accept))
    output = {"scope": "layer", "volumes": VOLUME, "splits": {}}
    for split in hits:
        n = totals[split]
        output["splits"][split] = {
            "n": n,
            "page": [round(value / n, 3) for value in hits[split]["page"]],
            "section": [round(value / n, 3)
                        for value in hits[split]["section"]],
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
