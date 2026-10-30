#!/usr/bin/env python3
"""Compare BM25 field weights across frozen qrels versions."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

WEIGHTS = {"5,2,.5": "5,2,0.5", "3,2,1": "3,2,1", "5,2,1": "5,2,1",
           "10,5,1": "10,5,1"}
DATASETS = {
    "v4": ("evaluation/corpus-qrels.v4.json",
           "evaluation/section-qrels.v4.json"),
    "v4.1": ("evaluation/corpus-qrels.v4.1.json",
             "evaluation/section-qrels.v4.1.json"),
    "v5": ("evaluation/corpus-qrels.v5-dense.json",
           "evaluation/section-qrels.v5-dense.json"),
    "v3": ("evaluation/corpus-qrels.v3.json",
           "evaluation/section-qrels.v3.json"),
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    output = {}
    for dataset, (page_name, section_name) in DATASETS.items():
        page_path = args.root / page_name
        section_path = args.root / section_name
        if not page_path.is_file() or not section_path.is_file():
            continue
        page = json.loads(page_path.read_text(encoding="utf-8"))
        section = json.loads(section_path.read_text(encoding="utf-8"))
        sections = {item["id"]: item for item in section["items"]}
        output[dataset] = {}
        for label, raw in WEIGHTS.items():
            os.environ["TYCHO_BM25_WEIGHTS"] = raw
            counts = {"page": [0, 0, 0], "section": [0, 0, 0]}
            for item in page["items"]:
                result = section_search.search(
                    args.root, item["question"], limit=5, abstain=False)
                rows = result.get("results", [])
                paths = [row["path"] for row in rows]
                keys = [row["section_key"] for row in rows]
                for index, k in enumerate((1, 3, 5)):
                    counts["page"][index] += int(
                        bool(set(paths[:k]) & set(item["accepted"])))
                    counts["section"][index] += int(
                        bool(set(keys[:k]) &
                             set(sections[item["id"]]["accepted"])))
            n = len(page["items"])
            output[dataset][label] = {
                level: [round(value / n, 3) for value in values]
                for level, values in counts.items()}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
