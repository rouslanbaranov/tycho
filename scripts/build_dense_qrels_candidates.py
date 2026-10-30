#!/usr/bin/env python3
"""Build a dense, search-independent candidate pool for qrels v5-dense."""
import argparse
import json
from pathlib import Path
import random
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
TARGET = 30


def split_for(path):
    if path.startswith("book/volumes/v11-pattern-atlas/"):
        return "atlas"
    if path.startswith("book/volumes/v12-"):
        return "v12"
    return "book"


def excerpt(text, limit=420):
    text = " ".join(str(text or "").split())
    return text[:limit]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--target", type=int, default=TARGET)
    args = ap.parse_args(argv)
    page_qrels = json.loads(
        (args.root / "evaluation/corpus-qrels.v4.1.json").read_text(
            encoding="utf-8"))
    section_qrels = json.loads(
        (args.root / "evaluation/section-qrels.v4.1.json").read_text(
            encoding="utf-8"))
    page_by_id = {item["id"]: item for item in page_qrels["items"]}
    section_by_id = {item["id"]: item for item in section_qrels["items"]}
    con = sqlite3.connect(args.root / "generated/sections-fts-v5.sqlite")
    con.row_factory = sqlite3.Row
    rows = [dict(row) for row in con.execute(
        "select path, section_key, heading, title, content from sections")]
    pages = {}
    sections = {}
    for row in rows:
        path = row["path"]
        pages.setdefault(path, row)
        sections[row["section_key"]] = row
    page_paths = sorted(pages)
    section_keys = sorted(sections)
    page_chapter = lambda path: str(Path(path).parent)
    page_volume = lambda path: "/".join(path.split("/")[:3])
    batches = {}
    items = []
    for index, qid in enumerate(sorted(page_by_id), 1):
        page = page_by_id[qid]
        section = section_by_id[qid]
        existing_pages = set(page["grades"])
        existing_sections = set(section["grades"])
        split = page["split"]
        rng = random.Random("v5:" + qid)
        split_pages = [p for p in page_paths if split_for(p) == split]
        structural = []
        for path in existing_pages:
            chapter = page_chapter(path)
            volume = page_volume(path)
            structural.extend(p for p in split_pages
                              if page_chapter(p) == chapter)
            structural.extend(p for p in split_pages
                              if p.startswith(volume + "/"))
        structural = [p for p in dict.fromkeys(structural)
                      if p not in existing_pages]
        rng.shuffle(structural)
        random_pages = [p for p in split_pages if p not in existing_pages]
        rng.shuffle(random_pages)
        new_pages = list(dict.fromkeys(structural + random_pages))[:(
            args.target - len(existing_pages))]
        section_pool = []
        for path in new_pages:
            section_pool.extend(k for k, row in sections.items()
                                if row["path"] == path)
        for path in existing_pages:
            chapter = page_chapter(path)
            section_pool.extend(k for k, row in sections.items()
                                if page_chapter(row["path"]) == chapter)
        section_pool = [k for k in dict.fromkeys(section_pool)
                        if k not in existing_sections]
        rng.shuffle(section_pool)
        fallback_sections = [k for k in section_keys
                             if split_for(sections[k]["path"]) == split
                             and k not in existing_sections]
        rng.shuffle(fallback_sections)
        new_sections = list(dict.fromkeys(section_pool + fallback_sections))[:(
            args.target - len(existing_sections))]
        page_new = [{"path": path,
                     "title": pages[path]["title"] or "",
                     "excerpt": excerpt(pages[path]["content"])}
                    for path in new_pages]
        section_new = [{"section_key": key,
                        "path": sections[key]["path"],
                        "heading": sections[key]["heading"] or "",
                        "excerpt": excerpt(sections[key]["content"])}
                       for key in new_sections]
        if len(page_new) != args.target - len(existing_pages):
            raise SystemExit("page candidates short for " + qid)
        if len(section_new) != args.target - len(existing_sections):
            raise SystemExit("section candidates short for " + qid)
        item = {
            "id": qid,
            "question": page["question"],
            "split": split,
            "page_existing": sorted(existing_pages),
            "section_existing": sorted(existing_sections),
            "page_new": page_new,
            "section_new": section_new,
        }
        items.append(item)
        batch = "D%02d" % ((index - 1) // 5 + 1)
        batches.setdefault(batch, []).append(item)
    target_dir = args.root / "evaluation/qrels-v5-dense"
    (target_dir / "batches").mkdir(parents=True, exist_ok=True)
    output = {
        "schema_version": 5,
        "status": "pool-pending",
        "base": "qrels v4.1",
        "target_candidates": args.target,
        "snapshot": page_qrels["snapshot"],
        "content_commit": page_qrels["content_commit"],
        "items": items,
    }
    (target_dir / "candidates.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for batch, batch_items in batches.items():
        (target_dir / "batches" / (batch + ".candidates.json")).write_text(
            json.dumps({"batch": batch, "items": batch_items}, indent=2,
                       sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"batches": len(batches), "queries": len(items),
                      "page_new": sum(len(i["page_new"]) for i in items),
                      "section_new": sum(len(i["section_new"]) for i in items)},
                     indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
