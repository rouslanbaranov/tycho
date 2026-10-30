#!/usr/bin/env python3
"""Merge ten reviewed qrels v4 batches into final page/section files."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--batch-dir", type=Path, required=True)
    args = ap.parse_args(argv)
    batch_dir = args.batch_dir if args.batch_dir.is_absolute() else (
        args.root / args.batch_dir)
    page_files = sorted(batch_dir.glob("*.page.json"))
    section_files = sorted(batch_dir.glob("*.section.json"))
    if len(page_files) != 10 or len(section_files) != 10:
        raise SystemExit("expected 10 page and 10 section batches")
    pages = []
    sections = []
    for path in page_files:
        pages.append(json.loads(path.read_text(encoding="utf-8")))
    for path in section_files:
        sections.append(json.loads(path.read_text(encoding="utf-8")))
    snapshots = {item["snapshot"] for item in pages + sections}
    commits = {item["content_commit"] for item in pages + sections}
    if len(snapshots) != 1 or len(commits) != 1:
        raise SystemExit("batch snapshot/content_commit mismatch")
    page_items = [item for batch in pages for item in batch["items"]]
    section_items = [item for batch in sections for item in batch["items"]]
    if len(page_items) != 150 or len(section_items) != 150:
        raise SystemExit("expected 150 queries")
    page_ids = [item["id"] for item in page_items]
    section_ids = [item["id"] for item in section_items]
    if len(set(page_ids)) != 150 or len(set(section_ids)) != 150:
        raise SystemExit("duplicate query ids")
    if set(page_ids) != set(section_ids):
        raise SystemExit("page/section query coverage mismatch")
    page_output = {
        "schema_version": 4, "status": "ai-adjudicated-not-human",
        "level": "page", "snapshot": snapshots.pop(),
        "content_commit": commits.pop(), "query_count": 150,
        "reviewer": sorted({batch.get("reviewer", "") for batch in pages}),
        "items": page_items,
        "limits": ("AI-adjudicated qrels v4; not human review, CI, owner "
                   "acceptance or sufficient coverage."),
    }
    section_output = dict(page_output)
    section_output["level"] = "section"
    section_output["items"] = section_items
    page_target = args.root / "evaluation/corpus-qrels.v4.json"
    section_target = args.root / "evaluation/section-qrels.v4.json"
    page_target.write_text(json.dumps(page_output, indent=2, sort_keys=True)
                           + "\n", encoding="utf-8")
    section_target.write_text(
        json.dumps(section_output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")
    check = subprocess.run(
        [sys.executable, "scripts/validate_qrels_v4.py",
         "--page", str(page_target), "--section", str(section_target)],
        cwd=args.root)
    return check.returncode


if __name__ == "__main__":
    sys.exit(main())
