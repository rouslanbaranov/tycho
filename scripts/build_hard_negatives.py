#!/usr/bin/env python3
"""Build hard-negative candidates from search top-5 outside v5 labels."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--sample-every", type=int, default=5)
    args = ap.parse_args(argv)
    page = json.loads(
        (args.root / "evaluation/corpus-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    section = json.loads(
        (args.root / "evaluation/section-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    sections = {item["id"]: item for item in section["items"]}
    items = []
    selected = 0
    for index, item in enumerate(page["items"]):
        if index % args.sample_every != 0:
            continue
        selected += 1
        result = section_search.search(
            args.root, item["question"], limit=5, abstain=False)
        rows = result.get("results", [])
        page_grades = set(item["grades"])
        section_grades = set(sections[item["id"]]["grades"])
        page_new = []
        section_new = []
        for row in rows:
            if row["path"] not in page_grades:
                page_new.append({"path": row["path"],
                                 "title": row.get("title", ""),
                                 "excerpt": row.get("content", "")[:500]})
            if row["section_key"] not in section_grades:
                section_new.append(
                    {"section_key": row["section_key"],
                     "path": row["path"],
                     "heading": row.get("heading", ""),
                     "excerpt": row.get("content", "")[:500]})
        items.append({
            "id": item["id"], "split": item["split"],
            "question": item["question"],
            "page_new": page_new, "section_new": section_new,
        })
    batches = {}
    for idx, item in enumerate(items):
        batches.setdefault("HN%02d" % (idx // 5 + 1), []).append(item)
    target = args.root / "evaluation/hard-negatives-v5"
    (target / "batches").mkdir(parents=True, exist_ok=True)
    (target / "candidates.json").write_text(
        json.dumps({"queries": len(items), "items": items},
                   indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for batch, batch_items in batches.items():
        (target / "batches" / (batch + ".candidates.json")).write_text(
            json.dumps({"batch": batch, "items": batch_items},
                       indent=2, sort_keys=True) + "\n",
            encoding="utf-8")
    print(json.dumps({"queries": len(items), "batches": len(batches),
                      "page": sum(len(i["page_new"]) for i in items),
                      "section": sum(len(i["section_new"]) for i in items)},
                     indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
