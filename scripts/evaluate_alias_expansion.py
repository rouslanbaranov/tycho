#!/usr/bin/env python3
"""Evaluate query expansion with external pattern-registry aliases."""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    registry = json.loads(
        (args.root / "edition/patterns/registry.v1.json").read_text(
            encoding="utf-8"))
    aliases = {}
    for pattern in registry["patterns"]:
        names = [pattern["catalog_name"]] + list(pattern.get("aliases") or [])
        for name in names:
            if len(name) < 3:
                continue
            aliases.setdefault(name.casefold(), set()).update(names)
    page = json.loads(
        (args.root / "evaluation/corpus-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    section = json.loads(
        (args.root / "evaluation/section-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section["items"]}
    counts = {"base": {"page": [0, 0, 0], "section": [0, 0, 0]},
              "alias": {"page": [0, 0, 0], "section": [0, 0, 0]}}
    expanded = 0
    for item in page["items"]:
        text = item["question"].casefold()
        additions = []
        for alias, names in aliases.items():
            if re.search(r"\b" + re.escape(alias) + r"\b", text):
                for name in names:
                    if name.casefold() not in text and name not in additions:
                        additions.append(name)
        query = item["question"]
        if additions:
            query += " " + " ".join(additions[:6])
            expanded += 1
        base = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        expanded_run = section_search.search(
            args.root, query, limit=5, abstain=False)
        for name, payload in (("base", base), ("alias", expanded_run)):
            rows = payload.get("results", [])
            paths = [row["path"] for row in rows]
            keys = [row["section_key"] for row in rows]
            for index, k in enumerate((1, 3, 5)):
                counts[name]["page"][index] += int(
                    bool(set(paths[:k]) & set(item["accepted"])))
                counts[name]["section"][index] += int(
                    bool(set(keys[:k]) & set(sections[item["id"]]["accepted"])))
    n = len(page["items"])
    output = {"expanded_queries": expanded,
              "metrics": {name: {level: [round(value / n, 3)
                                         for value in values]
                                 for level, values in levels.items()}
                          for name, levels in counts.items()}}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
