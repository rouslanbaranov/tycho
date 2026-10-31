#!/usr/bin/env python3
"""Bounded PRF query expansion comparison on v5."""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search

TOKEN = re.compile(r"[a-z0-9]+")
STOP = set("""a an and are as at be by for from how in into is it its of on or
that the their this to vs what when where which while who why with without""".split())


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
    counts = {"base": {"page": [0, 0, 0], "section": [0, 0, 0]},
              "prf2": {"page": [0, 0, 0], "section": [0, 0, 0]}}
    for item in page["items"]:
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        rows = base.get("results", [])
        words = Counter()
        query_terms = set(section_search.normalize_terms(item["question"]))
        for row in rows[:3]:
            for field in ("title", "heading"):
                for token in TOKEN.findall(str(row.get(field, "")).casefold()):
                    if len(token) > 2 and token not in STOP and token not in query_terms:
                        words[token] += 1
        additions = [word for word, _ in words.most_common(2)]
        expanded = item["question"] + " " + " ".join(additions)
        prf = section_search.search(
            args.root, expanded, limit=5, abstain=False)
        for name, result in (("base", base), ("prf2", prf)):
            result_rows = result.get("results", [])
            paths = [row["path"] for row in result_rows]
            keys = [row["section_key"] for row in result_rows]
            for index, k in enumerate((1, 3, 5)):
                counts[name]["page"][index] += int(
                    bool(set(paths[:k]) & set(item["accepted"])))
                counts[name]["section"][index] += int(
                    bool(set(keys[:k]) & set(sections[item["id"]]["accepted"])))
    n = len(page["items"])
    print(json.dumps({name: {level: [round(value / n, 3) for value in values]
                             for level, values in levels.items()}
                      for name, levels in counts.items()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
