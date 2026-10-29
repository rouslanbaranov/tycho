#!/usr/bin/env python3
"""Read-only H3 parent coverage diagnostics for the section index."""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "generated/sections-fts-v5.sqlite"


def summarize(sections, passages, limit=20):
    h2 = [row for row in sections if row["heading_level"] == 2]
    h2_keys = {row["section_key"] for row in h2}
    section_keys = {row["section_key"] for row in sections}
    by_parent = defaultdict(int)
    for passage in passages:
        by_parent[passage["parent_section_key"]] += 1
    without = [row for row in h2 if by_parent[row["section_key"]] == 0]
    orphan = [row for row in passages
              if row["parent_section_key"] not in section_keys]
    duplicate_sections = [key for key, count in
                          Counter(row["section_key"] for row in sections).items()
                          if count > 1]
    duplicate_passages = [key for key, count in
                          Counter(row["passage_key"] for row in passages).items()
                          if count > 1]
    anchors = Counter((row["path"], row["section_id"]) for row in sections)
    duplicate_anchors = ["%s#%s" % key for key, count in anchors.items()
                         if count > 1]
    per_page = defaultdict(int)
    for passage in passages:
        per_page[passage["path"]] += 1
    pages_without = sorted({
        row["path"] for row in h2 if per_page[row["path"]] == 0})
    counts = [by_parent[row["section_key"]] for row in h2]
    ordered = sorted(counts)
    median = ordered[len(ordered) // 2] if ordered else 0
    return {
        "documents": len({row["path"] for row in sections}),
        "h2_sections": len(h2),
        "h3_passages": len(passages),
        "h2_with_h3": len(h2) - len(without),
        "h2_without_h3": len(without),
        "pages_without_h3": len(pages_without),
        "orphan_h3": len(orphan),
        "duplicate_section_keys": len(duplicate_sections),
        "duplicate_passage_keys": len(duplicate_passages),
        "duplicate_anchors": len(duplicate_anchors),
        "h3_per_h2": {"min": min(counts) if counts else 0,
                      "median": median,
                      "max": max(counts) if counts else 0},
        "without_h3_sample": [
            {"path": row["path"], "section_id": row["section_id"],
             "heading": row["heading"]} for row in without[:limit]],
        "orphan_sample": [
            {"passage_key": row["passage_key"],
             "parent_section_key": row["parent_section_key"]}
            for row in orphan[:limit]],
        "duplicate_anchor_sample": duplicate_anchors[:limit],
        "pages_without_h3_sample": pages_without[:limit],
    }


def targets(sections, passages, limit=50):
    h2 = [row for row in sections if row["heading_level"] == 2]
    with_h3 = {row["parent_section_key"] for row in passages}
    grouped = defaultdict(list)
    for row in h2:
        if row["section_key"] not in with_h3:
            grouped[row["path"]].append(row["section_id"])
    rows = [{"path": path, "missing_h2": len(ids),
             "section_ids": ids} for path, ids in grouped.items()]
    rows.sort(key=lambda row: (-row["missing_h2"], row["path"]))
    return rows[:limit]


def load(root, index_path=None, include_targets=False):
    target = Path(index_path) if index_path else Path(root) / DEFAULT_INDEX.relative_to(ROOT)
    if not target.is_file():
        raise SystemExit("section index missing: %s" % target)
    with sqlite3.connect("file:" + target.resolve().as_posix() + "?mode=ro",
                        uri=True) as db:
        db.row_factory = sqlite3.Row
        sections = [dict(row) for row in db.execute(
            "select section_key,section_id,path,heading,heading_level"
            " from sections")]
        passages = [dict(row) for row in db.execute(
            "select passage_key,parent_section_key,parent_section_id,path"
            " from passages")]
    result = summarize(sections, passages)
    if include_targets:
        result["targets"] = targets(sections, passages)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--index", type=Path)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--targets", action="store_true")
    args = ap.parse_args(argv)
    result = load(args.root, args.index, include_targets=args.targets)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
