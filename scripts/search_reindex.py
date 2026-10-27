#!/usr/bin/env python3
"""Freeze and revalidate the Tycho search snapshot across book enrichment.

The harness never edits the book or rewrites qrels labels. It rebuilds derived
route/section indexes, reports stale evidence, and fails closed when the content
or qrels no longer match the frozen pre-enrichment manifest.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import route_index
import section_fts_index

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "edition/patterns/search-pre-enrichment.v1.json"
ROUTE_INDEX = ROOT / "generated/route-index.v1.json"
DEFAULT_INDEX = ROOT / "generated/sections-fts-v4.sqlite"
QRELS = (
    "evaluation/corpus-qrels.v2.json",
    "evaluation/independent-agent-qrels.phase1.json",
    "evaluation/agent-qrels.phase2.json",
    "evaluation/agent-qrels.phase3.json",
    "evaluation/phase3-human-sample.json",
)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def content_digest(root):
    root = Path(root)
    rows = []
    for path in sorted((root / "book").rglob("*.md")):
        rows.append((path.relative_to(root).as_posix(), sha(path)))
    payload = json.dumps(rows, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest(), len(rows)


def git_commit(root):
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def qrels_state(root):
    rows = []
    for relative in QRELS:
        path = Path(root) / relative
        if not path.is_file():
            continue
        data = load(path)
        items = data.get("items", [])
        route = data.get("snapshot", {}).get("route_index_snapshot")
        if route is None:
            route = data.get("snapshot")
        rows.append({
            "path": relative,
            "sha256": sha(path),
            "status": data.get("status") or data.get("label_status"),
            "items": len(items),
            "excluded": len(data.get("excluded", [])),
            "human_sample": data.get("human_sample"),
            "route_index_snapshot": route,
        })
    return rows


def build(root, allow_partial=False):
    root = Path(root).resolve()
    route = route_index.canonical_scan(root, allow_partial=allow_partial)
    ROUTE_INDEX.parent.mkdir(parents=True, exist_ok=True)
    ROUTE_INDEX.write_text(
        json.dumps(route, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    result = section_fts_index.publish(
        root, full=True, allow_partial=allow_partial)
    stats = section_fts_index.stats(root)
    return route, result, stats


def make_manifest(root, route, result, stats):
    digest, files = content_digest(root)
    qrels = qrels_state(root)
    stale = [row["path"] for row in qrels
             if row["route_index_snapshot"]
             and row["route_index_snapshot"] != route["snapshot_sha256"]]
    return {
        "schema_version": 1,
        "kind": "pre-enrichment-search-snapshot",
        "created": "2026-10-27",
        "git_commit": git_commit(root),
        "content": {"sha256": digest, "files": files},
        "route": {
            "snapshot": route["snapshot_sha256"],
            "documents": len(route["documents"]),
            "coverage": route["coverage"],
        },
        "section_index": {
            "snapshot": result["snapshot"],
            "sections": stats["sections"],
            "passages": stats["passages"],
            "bytes": stats["bytes"],
        },
        "qrels": qrels,
        "qrels_stale": stale,
        "status": "frozen-with-stale-qrels" if stale else "frozen",
        "quality_claims": "suspended-until-post-enrichment-revalidation",
        "protocol": (
            "Run check after every book change. Rebuild route/section indexes; "
            "do not rewrite qrels. Re-adjudicate accepted answers and the "
            "excluded/phase-3 sample before any quality claim."
        ),
    }


def check(root, manifest_path=DEFAULT_MANIFEST):
    root = Path(root).resolve()
    manifest = load(manifest_path)
    digest, files = content_digest(root)
    route = route_index.canonical_scan(root, allow_partial=True)
    issues = []
    if digest != manifest["content"]["sha256"]:
        issues.append("content-changed")
    if route["snapshot_sha256"] != manifest["route"]["snapshot"]:
        issues.append("route-changed")
    try:
        stats = section_fts_index.stats(root)
        if stats["snapshot"] != manifest["section_index"]["snapshot"]:
            issues.append("index-stale")
        if stats["sections"] != manifest["section_index"]["sections"]:
            issues.append("section-count-changed")
        if stats["passages"] != manifest["section_index"]["passages"]:
            issues.append("passage-count-changed")
    except (OSError, ValueError, RuntimeError):
        issues.append("index-missing")
    stale = []
    current_route = route["snapshot_sha256"]
    for row in manifest["qrels"]:
        path = root / row["path"]
        if not path.is_file() or sha(path) != row["sha256"]:
            stale.append(row["path"])
            continue
        data = load(path)
        route_value = data.get("snapshot", {}).get("route_index_snapshot")
        if route_value is None:
            route_value = data.get("snapshot")
        if route_value is not None and route_value != current_route:
            stale.append(row["path"])
    if stale:
        issues.append("qrels-stale")
    status = "current" if not issues else "stale"
    if issues == ["qrels-stale"]:
        status = "current-with-stale-qrels"
    return {
        "status": status,
        "issues": sorted(set(issues)),
        "qrels_stale": sorted(set(stale)),
        "content_files": files,
        "route": current_route,
        "manifest": str(manifest_path),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("snapshot", "check", "rebuild"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--allow-partial", action="store_true")
    args = ap.parse_args(argv)
    if args.action == "snapshot":
        route, result, stats = build(args.root, args.allow_partial)
        manifest = make_manifest(args.root, route, result, stats)
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(
            json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False)
            + "\n", encoding="utf-8")
        print(json.dumps(manifest, indent=2, sort_keys=True))
        return 0
    if args.action == "check":
        report = check(args.root, args.manifest)
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["status"] == "current" else 1
    route, result, stats = build(args.root, args.allow_partial)
    report = {
        "status": "rebuilt",
        "route": route["snapshot_sha256"],
        "section_index": result["snapshot"],
        "sections": stats["sections"],
        "passages": stats["passages"],
        "qrels_stale": (check(args.root, args.manifest).get("qrels_stale", [])
                        if args.manifest.is_file() else []),
        "quality_claims": "suspended-until-qrels-revalidation",
    }
    Path("generated/search-reindex-report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}))
        sys.exit(1)
