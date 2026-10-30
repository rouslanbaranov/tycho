#!/usr/bin/env python3
"""Paired uncertainty for BM25 body weight .5 vs .25 on qrels v4/v3."""
import argparse
import json
import math
import os
import random
from pathlib import Path

import section_search

ROOT = Path(__file__).resolve().parents[1]


def mcnemar(b01, b10):
    n = b01 + b10
    if not n:
        return 1.0
    tail = sum(math.comb(n, k) for k in range(min(b01, b10) + 1))
    return min(1.0, 2.0 * tail / (2 ** n))


def pct(values, fraction):
    ordered = sorted(values)
    return ordered[int(round((len(ordered) - 1) * fraction))]


def run(root, page_qrels, section_qrels):
    sections = {item["id"]: item for item in section_qrels["items"]}
    rows = []
    for weights in ((5.0, 2.0, 0.25), (5.0, 2.0, 0.5)):
        os.environ["TYCHO_BM25_WEIGHTS"] = ",".join(
            f"{value:g}" for value in weights)
        result_rows = {}
        for item in page_qrels["items"]:
            with section_search._QUERY_CACHE_LOCK:
                section_search._QUERY_CACHE.clear()
            result = section_search.search(
                root, item["question"], limit=5, abstain=False,
                section_rerank=False)
            page_keys = [row["path"] for row in result.get("results", [])]
            section_keys = [row["section_key"]
                            for row in result.get("results", [])]
            result_rows[item["id"]] = {
                "page": (page_keys, set(item["accepted"])),
                "section": (section_keys,
                            set(sections[item["id"]]["accepted"])),
            }
        rows.append(result_rows)
    rng = random.Random(20261030)
    output = {}
    for level in ("page", "section"):
        output[level] = {}
        for k in (1, 5):
            values = []
            for item in page_qrels["items"]:
                pair = tuple(
                    bool(set(rows[index][item["id"]][level][0][:k])
                         & rows[index][item["id"]][level][1])
                    for index in (0, 1))
                values.append(pair)
            n = len(values)
            base = sum(pair[0] for pair in values) / n
            body = sum(pair[1] for pair in values) / n
            b01 = sum(1 for pair in values if not pair[0] and pair[1])
            b10 = sum(1 for pair in values if pair[0] and not pair[1])
            diffs = []
            for _ in range(5000):
                sample = [values[rng.randrange(n)] for _ in range(n)]
                diffs.append(sum(pair[1] for pair in sample) / n
                              - sum(pair[0] for pair in sample) / n)
            output[level][f"top{k}"] = {
                "base": round(base, 4), "body": round(body, 4),
                "diff": round(body - base, 4),
                "ci95": [round(pct(diffs, .025), 4),
                         round(pct(diffs, .975), 4)],
                "b01": b01, "b10": b10,
                "p": round(mcnemar(b01, b10), 6),
            }
    return output


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    output = {}
    for name, page_name, section_name in (
            ("v4", "corpus-qrels.v4.json", "section-qrels.v4.json"),
            ("v3", "corpus-qrels.v3.json", "section-qrels.v3.json")):
        page_qrels = json.loads(
            (args.root / "evaluation" / page_name).read_text(encoding="utf-8"))
        section_qrels = json.loads(
            (args.root / "evaluation" / section_name).read_text(
                encoding="utf-8"))
        output[name] = run(args.root, page_qrels, section_qrels)
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
