#!/usr/bin/env python3
"""Evaluate margin-gated section_rerank on a labelled qrels file."""
import argparse
import json
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def target_set(item, level):
    raw = item.get("accepted", [])
    if not raw:
        return set(), False
    if isinstance(raw[0], dict):
        if level == "page":
            return {entry["path"] for entry in raw}, False
        return {(entry["path"], entry.get("section_id")) for entry in raw}, False
    if level == "section":
        return set(raw), True
    return set(raw), False


def paths(payload, level, key_mode=False):
    if level == "page":
        return [row["path"] for row in payload.get("results", [])]
    if key_mode:
        return [row["section_key"] for row in payload.get("results", [])]
    return [(row["path"], row.get("section_id"))
            for row in payload.get("results", [])]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--qrels", required=True)
    ap.add_argument("--level", choices=("page", "section"), default="page")
    ap.add_argument("--margin", type=float, default=0.15)
    args = ap.parse_args(argv)
    data = json.loads((args.root / args.qrels).read_text(encoding="utf-8"))
    rows = []
    for item in data["items"]:
        label = item.get("final_label")
        if label is not None and label != "answerable":
            continue
        target, key_mode = target_set(item, args.level)
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False,
            section_rerank=False)
        try:
            rerank = section_search.search(
                args.root, item["question"], limit=5, abstain=False,
                section_rerank=True)
        except section_search.SearchError:
            rerank = base
        base_paths = paths(base, args.level, key_mode)
        rerank_paths = paths(rerank, args.level, key_mode)
        scores = [row.get("score", 0) for row in base.get("results", [])]
        margin = ((scores[0] - scores[1]) / scores[0]
                  if len(scores) > 1 and scores[0] else 1.0)
        used = rerank_paths if margin < args.margin else base_paths
        row = {"id": item["id"], "split": item.get("split"),
               "margin": round(margin, 4),
               "applied": margin < args.margin}
        for name, paths_ in (("base", base_paths),
                             ("rerank", rerank_paths),
                             ("gated", used)):
            row[name] = [bool(set(paths_[:k]) & target)
                         for k in (1, 3, 5)]
        rows.append(row)
    output = {"qrels": args.qrels, "level": args.level,
              "margin": args.margin, "n": len(rows), "rows": rows}
    for split in sorted({row["split"] for row in rows} | {"all"}):
        subset = [row for row in rows if split == "all"
                  or row["split"] == split]
        if not subset:
            continue
        output[split] = {
            "n": len(subset),
            "applied": sum(1 for row in subset if row["applied"]),
            "base": [round(sum(row["base"][i] for row in subset)
                           / len(subset), 3) for i in range(3)],
            "rerank": [round(sum(row["rerank"][i] for row in subset)
                             / len(subset), 3) for i in range(3)],
            "gated": [round(sum(row["gated"][i] for row in subset)
                            / len(subset), 3) for i in range(3)],
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
