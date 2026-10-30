#!/usr/bin/env python3
"""Merge 15 qrels v4.1 batches and run the full expansion validator."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BATCHES = [f"B{index:02d}" for index in range(1, 16)]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--batch-dir", type=Path, required=True)
    args = ap.parse_args(argv)
    folder = args.batch_dir if args.batch_dir.is_absolute() else (
        args.root / args.batch_dir)
    pages = []
    sections = []
    for name in BATCHES:
        page_path = folder / (name + ".page.json")
        section_path = folder / (name + ".section.json")
        if not page_path.is_file() or not section_path.is_file():
            raise SystemExit("missing batch " + name)
        pages.append(json.loads(page_path.read_text(encoding="utf-8")))
        sections.append(json.loads(section_path.read_text(encoding="utf-8")))
    snapshots = {item["snapshot"] for item in pages + sections}
    commits = {item["content_commit"] for item in pages + sections}
    if len(snapshots) != 1 or len(commits) != 1:
        raise SystemExit("batch snapshot/commit mismatch")
    page_items = [item for batch in pages for item in batch["items"]]
    section_items = [item for batch in sections for item in batch["items"]]
    if len(page_items) != 150 or len(section_items) != 150:
        raise SystemExit("expected 150 queries")
    page_ids = {item["id"] for item in page_items}
    section_ids = {item["id"] for item in section_items}
    if len(page_ids) != 150 or page_ids != section_ids:
        raise SystemExit("query ID coverage mismatch")
    reviewers = set()
    for batch in pages:
        reviewer = batch.get("reviewer")
        if isinstance(reviewer, list):
            reviewers.update(str(item) for item in reviewer)
        elif reviewer:
            reviewers.add(str(reviewer))
    output = {
        "schema_version": 4,
        "status": "ai-adjudicated-not-human",
        "level": "page",
        "snapshot": snapshots.pop(),
        "content_commit": commits.pop(),
        "query_count": 150,
        "reviewer": sorted(reviewers),
        "items": page_items,
        "limits": ("Pool-expanded AI qrels; not human review, CI, owner "
                   "acceptance or sufficient coverage."),
    }
    section_output = dict(output)
    section_output["level"] = "section"
    section_output["items"] = section_items
    page_target = args.root / "evaluation/corpus-qrels.v4.1.json"
    section_target = args.root / "evaluation/section-qrels.v4.1.json"
    page_target.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    section_target.write_text(
        json.dumps(section_output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")
    check = subprocess.run(
        [sys.executable, "scripts/validate_qrels_v41.py",
         "--page", str(page_target), "--section", str(section_target),
         "--baseline-page", "evaluation/corpus-qrels.v4.json",
         "--baseline-section", "evaluation/section-qrels.v4.json"],
        cwd=args.root)
    return check.returncode


if __name__ == "__main__":
    raise SystemExit(main())
