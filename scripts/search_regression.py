#!/usr/bin/env python3
"""Record diagnostic retrieval fingerprints and compare snapshot drift.

This runner does not rank-tune or enforce a quality threshold.
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = ROOT / "evaluation/search-regression-baseline.v1.json"
SOURCES = (("v2", "evaluation/corpus-qrels.v2.json"),
           ("p3", "evaluation/agent-qrels.phase3.json"))


def load_queries(root):
    rows = []
    for split, relative in SOURCES:
        data = json.loads((Path(root) / relative).read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if split == "p3" and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            rows.append({"key": "%s:%s" % (split, item["id"]),
                         "split": split, "question": item["question"],
                         "accepted": item.get("accepted", [])})
    return rows


def first_hit(results, accepted):
    wanted = {(a["path"], a.get("section_id")) for a in accepted}
    for rank, result in enumerate(results, 1):
        if (result["path"], result["section_id"]) in wanted:
            return rank
        if (result["path"], None) in wanted:
            return rank
    return None


def summarize(records):
    def one(values):
        total = len(values)
        return {
            "queries": total,
            "hit@1": round(sum(1 for x in values if x and x <= 1) / total, 4),
            "hit@3": round(sum(1 for x in values if x and x <= 3) / total, 4),
            "hit@5": round(sum(1 for x in values if x and x <= 5) / total, 4),
            "mrr": round(sum(1.0 / x for x in values if x) / total, 4),
        }
    all_values = [r["rank"] for r in records]
    return {"all": one(all_values),
            "v2": one([r["rank"] for r in records if r["split"] == "v2"]),
            "p3": one([r["rank"] for r in records if r["split"] == "p3"])}


def run(root, limit=5):
    import section_search
    import section_fts_index
    data = section_fts_index.stats(root)
    records = []
    for query in load_queries(root):
        results = section_search.search(
            root, query["question"], limit=limit, abstain=False).get(
                "results", [])
        records.append({
            "key": query["key"],
            "split": query["split"],
            "fingerprint": ["%s#%s" % (r["path"], r["section_id"])
                            for r in results],
            "rank": first_hit(results, query["accepted"]),
        })
    return {
        "schema_version": 1,
        "status": "pre-enrichment-diagnostic",
        "snapshot": data.get("snapshot") if data else None,
        "queries": {r["key"]: {"fingerprint": r["fingerprint"],
                               "rank": r["rank"]} for r in records},
        "metrics": summarize(records),
        "notice": "Diagnostic fingerprints only; no quality threshold.",
    }


def compare(baseline, current):
    old = baseline.get("queries", {})
    new = current.get("queries", {})
    changed = sorted(key for key in set(old) | set(new)
                     if old.get(key, {}).get("fingerprint")
                     != new.get(key, {}).get("fingerprint"))
    old_m = baseline.get("metrics", {})
    new_m = current.get("metrics", {})
    deltas = {}
    for scope in ("all", "v2", "p3"):
        deltas[scope] = {
            metric: round(new_m.get(scope, {}).get(metric, 0)
                          - old_m.get(scope, {}).get(metric, 0), 4)
            for metric in ("hit@1", "hit@3", "hit@5", "mrr")}
    return {"status": "drift" if changed else "unchanged",
            "changed_queries": changed,
            "metrics_delta": deltas}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--baseline", type=Path)
    ap.add_argument("--fail-on-drift", action="store_true")
    args = ap.parse_args(argv)
    current = run(args.root, args.limit)
    if args.output:
        args.output.write_text(
            json.dumps(current, indent=2, sort_keys=True) + "\n",
            encoding="utf-8")
    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        current["comparison"] = compare(baseline, current)
    print(json.dumps(current, indent=2, sort_keys=True))
    if (args.fail_on_drift and current.get("comparison", {}).get("status")
            == "drift"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
