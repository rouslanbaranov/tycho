#!/usr/bin/env python3
"""Evaluate BM25 field-weight profiles on qrels v5-dense."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

PROFILES = {
    "5,2,.5": "5,2,0.5",
    "3,2,1": "3,2,1",
    "5,2,1": "5,2,1",
    "5,5,.5": "5,5,0.5",
    "10,1,.2": "10,1,0.2",
    "2,10,.2": "2,10,0.2",
    "1,1,5": "1,1,5",
    "10,5,1": "10,5,1",
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    page = json.loads(
        (args.root / "evaluation/corpus-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    section = json.loads(
        (args.root / "evaluation/section-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section["items"]}
    output = {}
    for label, raw in PROFILES.items():
        os.environ["TYCHO_BM25_WEIGHTS"] = raw
        counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
        by_split = {}
        for item in page["items"]:
            result = section_search.search(
                args.root, item["question"], limit=5, abstain=False)
            rows = result.get("results", [])
            page_keys = [row["path"] for row in rows]
            section_keys = [row["section_key"] for row in rows]
            split = by_split.setdefault(item["split"],
                                        {"page": [0, 0, 0],
                                         "section": [0, 0, 0]})
            for index, k in enumerate((1, 3, 5)):
                page_hit = int(bool(set(page_keys[:k]) & set(item["accepted"])))
                section_hit = int(bool(
                    set(section_keys[:k]) &
                    set(sections[item["id"]]["accepted"])))
                counts["page"][index] += page_hit
                counts["section"][index] += section_hit
                split["page"][index] += page_hit
                split["section"][index] += section_hit
        n = len(page["items"])
        output[label] = {
            "all": {level: [round(value / n, 3) for value in values]
                    for level, values in counts.items()},
            "split": {name: {level: [round(value / total, 3)
                                    for value in values]
                             for level, values in levels.items()}
                      for name, levels in by_split.items()
                      for total in [sum(1 for item in page["items"]
                                       if item["split"] == name)]},
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
