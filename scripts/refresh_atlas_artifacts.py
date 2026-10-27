#!/usr/bin/env python3
"""Refresh every derived atlas artifact, optionally authorizing mechanical revisions."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args, check=True):
    return subprocess.run([sys.executable, *args], cwd=ROOT,
                          capture_output=True, text=True, check=check)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sync_json(path, update):
    p = ROOT / path
    data = json.loads(p.read_text())
    update(data)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def authorize_missing(reason):
    plan = run("scripts/book_change.py", "--plan", check=False).stdout + run(
        "scripts/book_change.py", "--plan", check=False).stderr
    lines = plan.splitlines()
    entries = {"directory_documents": [], "enrichment_documents": [],
               "enrichment_baselines": []}
    i = 0
    while i < len(lines):
        m = re.match(r"- (directory_documents|enrichment_documents|enrichment_baselines): (.+)",
                     lines[i].strip())
        if m and i + 2 < len(lines):
            prev = re.search(r"previous_sha256:\s*([0-9a-f]+)", lines[i + 1])
            cur = re.search(r"current_sha256:\s*([0-9a-f]+)", lines[i + 2])
            if prev and cur:
                entries[m.group(1)].append({
                    "path": m.group(2).strip(),
                    "previous_sha256": prev.group(1),
                    "current_sha256": cur.group(1),
                })
                i += 3
                continue
        i += 1
    total = sum(len(v) for v in entries.values())
    if not total:
        return 0
    if not reason:
        print("book change requires authorized revisions; pass --authorize REASON")
        return 1
    revisions = json.loads((ROOT / "edition/content-revisions.json").read_text())
    revisions["revisions"].append({
        "issue": 540,
        "authorized_at": "2026-10-27",
        "authorization": reason,
        "directory_documents": entries["directory_documents"],
        "source_blocks": [],
        "enrichment_documents": entries["enrichment_documents"],
        "enrichment_additions": [],
        "enrichment_baselines": entries["enrichment_baselines"],
    })
    (ROOT / "edition/content-revisions.json").write_text(
        json.dumps(revisions, indent=2, ensure_ascii=False) + "\n")
    print("authorized", total, "revisions")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--authorize", default=None,
                        help="reason for authorizing pending book revisions")
    args = parser.parse_args()

    run("scripts/refresh_enrichment_baselines.py")
    if authorize_missing(args.authorize):
        return 1
    run("scripts/route_index.py", "build")
    run("scripts/section_fts_index.py", "build")
    run("scripts/pattern_census.py", "--write")
    run("scripts/pattern_coverage.py", "--write")
    run("scripts/phase4_audit.py")

    phase4 = json.loads((ROOT / "edition/patterns/phase4.v1.json").read_text())["summary"]
    route_snapshot = json.loads((ROOT / "generated/route-index.v1.json").read_text())["snapshot_sha256"]

    def atlas(data):
        for item in data["documents"]:
            if item.get("path"):
                item["sha256"] = sha(ROOT / item["path"])
    sync_json("edition/atlas-manifest.json", atlas)

    def semantic(data):
        for page in data["pages"]:
            page["sha256"] = sha(ROOT / page["path"])
        data["summary"]["pages"] = len(data["pages"])
        data["summary"]["by_tier"]["atlas"] = sum(
            1 for p in data["pages"] if p["tier"] == "atlas")
        data["summary"]["by_disposition"]["sound"] = sum(
            1 for p in data["pages"] if p["review"]["disposition"] == "sound")
    sync_json("edition/patterns/semantic-audit.v1.json", semantic)

    def delivery(data):
        s = data["summary"]
        s["pages"] = phase4["pages"]
        s["routes"] = phase4["routes"]
        s["related_labels"] = phase4["related_labels"]
        s["non_routes"] = phase4["non_routes"]
        s["cards"] = phase4["cards"]
        s["entries"] = phase4["entries"]
        s["retrieval_questions"] = phase4["retrieval_questions"]
        s["semantic_pages"] = len(json.loads(
            (ROOT / "edition/patterns/semantic-audit.v1.json").read_text())["pages"])
    sync_json("edition/patterns/delivery-evidence.v1.json", delivery)

    for name in ("corpus-qrels.v1.json", "corpus-qrels.v2.json"):
        def qrels(data):
            data["snapshot"]["document_count"] = phase4["pages"]
            data["snapshot"]["route_index_snapshot"] = route_snapshot
        sync_json("evaluation/" + name, qrels)

    registry_sha = sha(ROOT / "edition/patterns/registry.v1.json")
    for path in ("edition/patterns/source-plan.v1.json", "edition/atlas-manifest.json"):
        def bind(data):
            data["registry_sha256"] = registry_sha
        sync_json(path, bind)

    def source_plan(data):
        data["route_index_snapshot"] = route_snapshot
    sync_json("edition/patterns/source-plan.v1.json", source_plan)

    run("scripts/validate_edition.py", "--write-inventory")
    run("scripts/sufficient_candidates.py", "--write")
    candidates = json.loads((ROOT / "edition/patterns/sufficient-candidates.v1.json").read_text())
    deeper = [e["pattern_id"] for e in candidates["entries"]
              if e["status"] != "candidate-for-independent-review"]
    if deeper:
        print("candidate threshold not met:", ", ".join(deeper))
        return 1
    run("scripts/build_rereview_scope.py", "--write")
    run("scripts/build_rereview_packets.py")
    print("atlas artifacts refreshed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
