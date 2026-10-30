#!/usr/bin/env python3
"""Merge v5-dense label batches with frozen v4.1 labels."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    root = args.root
    base_page = json.loads(
        (root / "evaluation/corpus-qrels.v4.1.json").read_text(
            encoding="utf-8"))
    base_section = json.loads(
        (root / "evaluation/section-qrels.v4.1.json").read_text(
            encoding="utf-8"))
    page_base = {item["id"]: item for item in base_page["items"]}
    section_base = {item["id"]: item for item in base_section["items"]}
    candidates = json.loads(
        (root / "evaluation/qrels-v5-dense/candidates.json").read_text(
            encoding="utf-8"))
    labels = {}
    for batch in range(1, 31):
        name = "D%02d" % batch
        path = root / "evaluation/qrels-v5-dense/labels" / (name + ".json")
        if not path.is_file():
            raise SystemExit("missing labels " + name)
        data = json.loads(path.read_text(encoding="utf-8"))
        labels.update({item["id"]: item for item in data["items"]})
    page_items = []
    section_items = []
    for item in candidates["items"]:
        qid = item["id"]
        page_grades = dict(page_base[qid]["grades"])
        section_grades = dict(section_base[qid]["grades"])
        page_grades.update(labels[qid]["page_grades"])
        section_grades.update(labels[qid]["section_grades"])
        for level, grades, base in (("page", page_grades, page_base[qid]),
                                    ("section", section_grades,
                                     section_base[qid])):
            if set(base["grades"]) - set(grades):
                raise SystemExit(qid + ": lost baseline " + level)
            accepted = sorted(key for key, value in grades.items()
                              if value >= 1)
            direct = sorted(key for key, value in grades.items()
                            if value == 2)
            if not direct:
                raise SystemExit(qid + ": no direct " + level)
            target = {"id": qid, "question": base["question"],
                      "split": base["split"], "grades": grades,
                      "accepted": accepted, "direct": direct}
            (page_items if level == "page" else section_items).append(target)
    output = {
        "schema_version": 5,
        "status": "ai-adjudicated-not-human",
        "base": "qrels v4.1",
        "snapshot": base_page["snapshot"],
        "content_commit": base_page["content_commit"],
        "query_count": 150,
        "items": page_items,
        "limits": ("Dense AI pool; structural/random candidates; not human "
                   "review, CI, owner acceptance or sufficient coverage."),
    }
    section_output = dict(output)
    section_output["level"] = "section"
    section_output["items"] = section_items
    page_target = root / "evaluation/corpus-qrels.v5-dense.json"
    section_target = root / "evaluation/section-qrels.v5-dense.json"
    page_target.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    section_target.write_text(
        json.dumps(section_output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")
    check = subprocess.run(
        [sys.executable, "scripts/validate_qrels_v5.py",
         "--page", str(page_target), "--section", str(section_target)],
        cwd=root)
    return check.returncode


if __name__ == "__main__":
    raise SystemExit(main())
