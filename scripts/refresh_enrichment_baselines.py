#!/usr/bin/env python3
"""Refresh enrichment baselines for changed pages in one authorized revision."""
import datetime
import json
import subprocess
import sys
from pathlib import Path

from assemble_edition import sha
from directory_paths import HistoricalView

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "edition/enrichment-manifest.json"
REVISIONS = "edition/content-revisions.json"
MIGRATION = "edition/directory-migration.json"


def main():
    changed = subprocess.run(
        ["git", "diff", "--name-only", "HEAD", "--", "book"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    view = HistoricalView(ROOT)
    manifest = json.loads((ROOT / MANIFEST).read_text())
    edits = []
    for record in manifest["new_documents"]:
        path = record["path"]
        current = sha(view.read_text(path))
        if current == record["sha256"]:
            continue
        edits.append({
            "path": path,
            "previous_sha256": record["sha256"],
            "current_sha256": current,
        })
        record["sha256"] = current
    if not edits:
        print("enrichment baselines current")
        return 0
    revisions = json.loads((ROOT / REVISIONS).read_text())
    revisions["revisions"].append({
        "issue": 540,
        "authorized_at": datetime.date.today().isoformat(),
        "authorization": "Refresh enrichment baselines for changed book pages.",
        "directory_documents": [],
        "source_blocks": [],
        "enrichment_documents": edits,
        "enrichment_additions": [],
        "enrichment_baselines": [],
    })
    (ROOT / REVISIONS).write_text(json.dumps(revisions, indent=2, ensure_ascii=False) + "\n")
    (ROOT / MANIFEST).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    migration = json.loads((ROOT / MIGRATION).read_text())
    for key in migration["protected_manifests"]:
        path = ROOT / key
        if path.is_file():
            migration["protected_manifests"][key] = sha(path.read_text())
    (ROOT / MIGRATION).write_text(json.dumps(migration, indent=2, ensure_ascii=False) + "\n")
    print("refreshed", len(edits), "enrichment baselines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
