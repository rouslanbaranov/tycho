#!/usr/bin/env python3
"""Build v5.2 page qrels from top-1 page audit."""
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    root = args.root
    page = json.loads((root / "evaluation/corpus-qrels.v5-dense.json").read_text())
    target = {i["id"]: dict(i) for i in page["items"]}
    third = json.loads((root / "evaluation/hard-negatives-page-v5/adjudication.json").read_text())
    third_map = {(i["id"], i["path"]): int(i["grade"]) for i in third["items"]}
    extra = json.loads((root / "evaluation/hard-negatives-page-v5" /
                        "adjudication-extra.json").read_text())
    third_map.update({(i["id"], i["path"]): int(i["grade"])
                      for i in extra["items"]})
    added = 0
    for n in range(1, 16):
        batch = "PG%02d" % n
        cand = json.loads((root / "evaluation/hard-negatives-page-v5/batches" / (batch + ".candidates.json")).read_text())
        a = json.loads((root / "evaluation/hard-negatives-page-v5/labels" / (batch + "-A.json")).read_text())
        b = json.loads((root / "evaluation/hard-negatives-page-v5/labels" / (batch + "-B.json")).read_text())
        am = {i["id"]: i for i in a["items"]}
        bm = {i["id"]: i for i in b["items"]}
        for item in cand["items"]:
            qid = item["id"]
            for entry in item["page_new"]:
                path = entry["path"]
                x = am[qid].get("page_grades", {}).get(path)
                y = bm[qid].get("page_grades", {}).get(path)
                if x is None or y is None:
                    continue
                grade = int(x) if x == y else third_map[(qid, path)]
                target[qid]["grades"][path] = grade
                added += 1
    for item in target.values():
        item["accepted"] = sorted(k for k, v in item["grades"].items() if v >= 1)
        item["direct"] = sorted(k for k, v in item["grades"].items() if v == 2)
    out = dict(page)
    out.update({"status": "ai-adjudicated-not-human",
                "base": "qrels v5-dense",
                "query_count": 150,
                "items": sorted(target.values(), key=lambda i: i["id"]),
                "limits": ("v5.2 page adds one audited page per query; "
                           "not comparable to v5; AI-only.")})
    (root / "evaluation/corpus-qrels.v5.2-page.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"added": added}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
