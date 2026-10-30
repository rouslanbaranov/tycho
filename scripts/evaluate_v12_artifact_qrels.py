#!/usr/bin/env python3
"""Evaluate externally adjudicated V12 artifact qrels."""
import argparse
import collections
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def artifact_type(item):
    direct = item.get("direct") or []
    if not direct:
        return "unknown"
    return direct[0].split(".")[1] if "." in direct[0] else "unknown"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    data = json.loads((args.root / "evaluation/v12-artifact-qrels.v1.json")
                      .read_text(encoding="utf-8"))
    rows = []
    for item in data["items"]:
        terms = section_search.normalize_terms(item["question"])
        payload = section_search.v12_artifacts(
            args.root, limit=10, terms=terms)
        rows.append((artifact_type(item),
                     [a["id"] for a in payload["artifacts"]],
                     set(item["accepted"]), set(item["direct"])))
    def summary(subset, use_direct):
        hits = {1: 0, 3: 0, 5: 0}
        for _, ids, accepted, direct in subset:
            target = direct if use_direct else accepted
            for k in hits:
                hits[k] += int(bool(set(ids[:k]) & target))
        n = len(subset)
        return {str(k): round(hits[k] / n, 3) for k in hits}
    types = sorted(set(row[0] for row in rows))
    output = {
        "status": data.get("status"),
        "queries": len(rows),
        "candidate_pool_sizes": dict(collections.Counter(
            len(item["grades"]) for item in data["items"])),
        "accepted": summary(rows, False),
        "direct": summary(rows, True),
        "by_type": {
            name: summary([row for row in rows if row[0] == name], False)
            for name in types
        },
        "type_counts": {name: sum(1 for row in rows if row[0] == name)
                        for name in types},
        "limits": data.get("limits"),
    }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
