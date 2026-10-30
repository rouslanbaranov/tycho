#!/usr/bin/env python3
"""Evaluate section reranking variants on v5-dense."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def evaluate(root, page_qrels, section_qrels, modes):
    sections = {item["id"]: item for item in section_qrels["items"]}
    counts = {mode: {"page": [0, 0, 0], "section": [0, 0, 0]}
              for mode in modes}
    for item in page_qrels["items"]:
        section_item = sections[item["id"]]
        for mode, kwargs in modes.items():
            try:
                result = section_search.search(
                    root, item["question"], limit=5, abstain=False, **kwargs)
            except section_search.SearchError:
                result = section_search.search(
                    root, item["question"], limit=5, abstain=False)
            rows = result.get("results", [])
            page_keys = [row["path"] for row in rows]
            section_keys = [row["section_key"] for row in rows]
            if page_qrels["items"]:
                for index, k in enumerate((1, 3, 5)):
                    counts[mode]["page"][index] += int(
                        bool(set(page_keys[:k]) & set(item["accepted"])))
                    counts[mode]["section"][index] += int(
                        bool(set(section_keys[:k]) &
                             set(section_item["accepted"])))
    n = len(page_qrels["items"])
    return {mode: {level: [round(value / n, 3) for value in values]
                   for level, values in levels.items()}
            for mode, levels in counts.items()}


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
    modes = {"bm25": {"section_rerank": False},
             "always": {"section_rerank": True}}
    for margin in (0.02, 0.05, 0.10, 0.20):
        modes["m%.2f" % margin] = {
            "section_rerank": True, "section_rerank_margin": margin}
    print(json.dumps(evaluate(args.root, page, section, modes), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
