#!/usr/bin/env python3
"""Build v5.1 from v5 plus full-query hard-negative labels."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_labels(path_a, path_b):
    a = json.loads(path_a.read_text(encoding="utf-8"))
    b = json.loads(path_b.read_text(encoding="utf-8"))
    am = {i["id"]: i for i in a["items"]}
    bm = {i["id"]: i for i in b["items"]}
    result = {}
    for qid in am:
        for level, key in (("page", "page_grades"),
                           ("section", "section_grades")):
            for candidate, grade in am[qid].get(key, {}).items():
                result[(qid, level, candidate)] = int(grade)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    root = args.root
    page = json.loads(
        (root / "evaluation/corpus-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    section = json.loads(
        (root / "evaluation/section-qrels.v5-dense.json").read_text(
            encoding="utf-8"))
    page_by_id = {i["id"]: dict(i) for i in page["items"]}
    section_by_id = {i["id"]: dict(i) for i in section["items"]}
    candidates = {}
    for n in range(1, 16):
        batch = "HN%02d" % n
        data = json.loads(
            (root / "evaluation/hard-negatives-v5/batches" /
             (batch + ".candidates.json")).read_text(encoding="utf-8"))
        for item in data["items"]:
            candidates[item["id"]] = item
    third = json.loads(
        (root / "evaluation/hard-negatives-v5/adjudication.json").read_text(
            encoding="utf-8"))
    third_map = {(i["id"], i["level"], i["key"]): int(i["grade"])
                 for i in third["items"]}
    labels = {}
    for n in range(1, 16):
        batch = "HN%02d" % n
        labels.update(load_labels(
            root / "evaluation/hard-negatives-v5/labels" /
            (batch + "-A.json"),
            root / "evaluation/hard-negatives-v5/labels" /
            (batch + "-B.json")))
    # verify third labeler's keys are exactly the disagreements
    disagreements = set()
    for n in range(1, 16):
        batch = "HN%02d" % n
        a = json.loads((root / "evaluation/hard-negatives-v5/labels" /
                        (batch + "-A.json")).read_text(encoding="utf-8"))
        b = json.loads((root / "evaluation/hard-negatives-v5/labels" /
                        (batch + "-B.json")).read_text(encoding="utf-8"))
        am = {i["id"]: i for i in a["items"]}
        bm = {i["id"]: i for i in b["items"]}
        for qid in am:
            for level, key in (("page", "page_grades"),
                               ("section", "section_grades")):
                for candidate, grade in am[qid].get(key, {}).items():
                    if bm[qid].get(key, {}).get(candidate) != grade:
                        disagreements.add((qid, level, candidate))
    if disagreements != set(third_map):
        raise SystemExit("third labeler keys do not match disagreements")
    added = 0
    for qid, item in candidates.items():
        for level, key in (("page", "page_grades"),
                           ("section", "section_grades")):
            contribution = {}
            for candidate, a_grade in labels.items():
                if candidate[0] != qid or candidate[1] != level:
                    continue
                b_grade = labels.get(candidate)
                # labels dict already A; need B separately? store below
            # rebuilt below with explicit A/B maps
    # explicit merge
    for n in range(1, 16):
        batch = "HN%02d" % n
        a = json.loads((root / "evaluation/hard-negatives-v5/labels" /
                        (batch + "-A.json")).read_text(encoding="utf-8"))
        b = json.loads((root / "evaluation/hard-negatives-v5/labels" /
                        (batch + "-B.json")).read_text(encoding="utf-8"))
        am = {i["id"]: i for i in a["items"]}
        bm = {i["id"]: i for i in b["items"]}
        for qid, item in candidates.items():
            if qid not in am:
                continue
            for level, key, target in (
                    ("page", "page_grades", page_by_id[qid]),
                    ("section", "section_grades", section_by_id[qid])):
                for candidate, a_grade in am[qid].get(key, {}).items():
                    b_grade = bm[qid].get(key, {}).get(candidate)
                    if b_grade == a_grade:
                        grade = int(a_grade)
                    else:
                        grade = third_map[(qid, level, candidate)]
                    target["grades"][candidate] = grade
                    added += 1
    for target in page_by_id.values():
        target["accepted"] = sorted(k for k, v in target["grades"].items()
                                    if v >= 1)
        target["direct"] = sorted(k for k, v in target["grades"].items()
                                  if v == 2)
    for target in section_by_id.values():
        target["accepted"] = sorted(k for k, v in target["grades"].items()
                                    if v >= 1)
        target["direct"] = sorted(k for k, v in target["grades"].items()
                                  if v == 2)
    output = dict(page)
    output.update({"status": "ai-adjudicated-not-human",
                   "base": "qrels v5-dense",
                   "query_count": 150,
                   "items": sorted(page_by_id.values(), key=lambda i: i["id"]),
                   "limits": ("v5.1 adds one hard-negative unit per query; "
                              "not comparable to v5; AI-only.")})
    section_output = dict(output)
    section_output["level"] = "section"
    section_output["items"] = sorted(section_by_id.values(),
                                     key=lambda i: i["id"])
    (root / "evaluation/corpus-qrels.v5.1.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (root / "evaluation/section-qrels.v5.1.json").write_text(
        json.dumps(section_output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")
    print(json.dumps({"added": added, "queries": len(page_by_id)},
                     indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
