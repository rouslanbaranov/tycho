#!/usr/bin/env python3
"""Freeze and revalidate the Tycho search snapshot across book enrichment.

The harness never edits the book or rewrites qrels labels. It rebuilds derived
route/section indexes, reports stale evidence, and fails closed when the content
or qrels no longer match the frozen pre-enrichment manifest.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys

import route_index
import section_fts_index

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "edition/patterns/search-pre-enrichment.v1.json"
ROUTE_INDEX = ROOT / "generated/route-index.v1.json"
DEFAULT_INDEX = ROOT / "generated/sections-fts-v5.sqlite"
QRELS = (
    "evaluation/corpus-qrels.v2.json",
    "evaluation/independent-agent-qrels.phase1.json",
    "evaluation/agent-qrels.phase2.json",
    "evaluation/agent-qrels.phase3.json",
    "evaluation/phase3-human-sample.json",
    "evaluation/v12-simulation-qrels.v1.json",
)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def content_files(root):
    root = Path(root)
    return {
        path.relative_to(root).as_posix(): sha(path)
        for path in sorted((root / "book").rglob("*.md"))
    }


def section_inventory(root):
    target = Path(root) / DEFAULT_INDEX.relative_to(ROOT)
    if not target.is_file():
        return {}
    with sqlite3.connect("file:" + target.resolve().as_posix() + "?mode=ro",
                        uri=True) as db:
        rows = db.execute(
            "select path,section_key from sections order by path,section_key")
        grouped = {}
        for path, key in rows:
            grouped.setdefault(path, []).append(key)
    return grouped


def content_digest(root):
    rows = sorted(content_files(root).items())
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


class reindex_lock:
    """Exclusive lock so two rebuilds cannot publish one snapshot."""

    def __init__(self, root):
        self.path = Path(root) / "generated/.search-reindex.lock"
        self.fd = None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            self.fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError as exc:
            raise RuntimeError("reindex already running") from exc
        return self

    def __exit__(self, exc_type, exc, tb):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
        try:
            self.path.unlink()
        except FileNotFoundError:
            pass
        return False


def build(root, allow_partial=False, full=True):
    root = Path(root).resolve()
    with reindex_lock(root):
        route = route_index.canonical_scan(root, allow_partial=allow_partial)
        ROUTE_INDEX.parent.mkdir(parents=True, exist_ok=True)
        temp = ROUTE_INDEX.with_suffix(".json.tmp")
        temp.write_text(
            json.dumps(route, sort_keys=True, indent=2, ensure_ascii=False)
            + "\n", encoding="utf-8")
        os.replace(temp, ROUTE_INDEX)
        result = section_fts_index.publish(
            root, full=full, allow_partial=allow_partial)
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
        "content": {"sha256": digest, "files": files,
                    "files_sha256": content_files(root)},
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
            "sections_by_path": section_inventory(root),
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


def diff_manifests(old, new):
    old_files = old.get("content", {}).get("files_sha256", {})
    new_files = new.get("content", {}).get("files_sha256", {})
    old_keys, new_keys = set(old_files), set(new_files)
    added = sorted(new_keys - old_keys)
    removed = sorted(old_keys - new_keys)
    changed = sorted(
        key for key in old_keys & new_keys
        if old_files[key] != new_files[key])
    old_qrels = {row["path"]: row for row in old.get("qrels", [])}
    new_qrels = {row["path"]: row for row in new.get("qrels", [])}
    qrels_changed = sorted(
        path for path in set(old_qrels) | set(new_qrels)
        if old_qrels.get(path) != new_qrels.get(path))
    old_sections = old.get("section_index", {}).get("sections")
    new_sections = new.get("section_index", {}).get("sections")
    old_passages = old.get("section_index", {}).get("passages")
    new_passages = new.get("section_index", {}).get("passages")
    old_map = old.get("section_index", {}).get("sections_by_path", {})
    new_map = new.get("section_index", {}).get("sections_by_path", {})
    added_sections = sorted(
        key for path in new_map for key in new_map[path]
        if key not in old_map.get(path, []))
    removed_sections = sorted(
        key for path in old_map for key in old_map[path]
        if key not in new_map.get(path, []))
    section_changed_pages = sorted(
        path for path in set(old_map) | set(new_map)
        if old_map.get(path, []) != new_map.get(path, []))
    changed_all = (added or removed or changed or qrels_changed
                   or old_sections != new_sections
                   or old_passages != new_passages
                   or added_sections or removed_sections)
    return {
        "status": "changed" if changed_all else "unchanged",
        "added_pages": added,
        "removed_pages": removed,
        "changed_pages": changed,
        "qrels_changed": qrels_changed,
        "sections": {"old": old_sections, "new": new_sections},
        "passages": {"old": old_passages, "new": new_passages},
        "added_sections": added_sections,
        "removed_sections": removed_sections,
        "section_changed_pages": section_changed_pages,
    }


def diff_current(root, manifest_path=DEFAULT_MANIFEST):
    old = load(manifest_path)
    new = {
        "content": {"files": len(content_files(root)),
                    "files_sha256": content_files(root)},
        "qrels": qrels_state(root),
        "section_index": {},
    }
    try:
        stats = section_fts_index.stats(root)
        new["section_index"] = {
            "sections": stats["sections"], "passages": stats["passages"],
            "sections_by_path": section_inventory(root)}
    except (OSError, ValueError, RuntimeError, sqlite3.DatabaseError):
        pass
    report = diff_manifests(old, new)
    report["manifest"] = str(manifest_path)
    report["qrels_stale"] = check(root, manifest_path).get("qrels_stale", [])
    return report


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
    except (OSError, ValueError, RuntimeError, sqlite3.DatabaseError):
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


def verify(root, manifest_path=DEFAULT_MANIFEST):
    result = section_fts_index.verify(Path(root))
    result["status"] = "verified"
    if Path(manifest_path).is_file():
        result["qrels_stale"] = check(root, manifest_path).get(
            "qrels_stale", [])
    else:
        result["qrels_stale"] = []
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("snapshot", "check", "rebuild", "diff",
                                      "verify"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--allow-partial", action="store_true")
    ap.add_argument("--full", action="store_true",
                    help="reparse every document (snapshot is always full)")
    args = ap.parse_args(argv)
    if args.action == "snapshot":
        route, result, stats = build(
            args.root, args.allow_partial, full=True)
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
    if args.action == "diff":
        report = diff_current(args.root, args.manifest)
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["status"] == "unchanged" else 1
    if args.action == "verify":
        report = verify(args.root, args.manifest)
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    route, result, stats = build(
        args.root, args.allow_partial, full=args.full)
    report = {
        "status": "rebuilt",
        "mode": "full" if args.full else "incremental",
        "reused_documents": result.get("reused_documents"),
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
