#!/usr/bin/env python3
"""Read-only plan for a bounded book change.

Reports changed canonical pages, missing authorized revisions, stale derived
artifacts and the ordered rebuild/review steps. It never writes to the
repository and never replaces premerge_check.py, claim review or independent
review.
"""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
import shlex
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from assemble_edition import sha
from content_revisions import authorized
from directory_paths import HistoricalView
from route_index import canonical_scan
from validate_edition import inventory_members
import pattern_census
import pattern_coverage
import phase4_audit
import section_fts_index
import validate_delivery_evidence
import validate_pattern_owner_units
import validate_pattern_semantic_audit


def load(path, default=None):
    path = Path(path)
    if not path.is_file():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def diff_maps(recorded, current):
    rows = []
    for path in sorted(set(recorded) | set(current)):
        old = recorded.get(path)
        new = current.get(path)
        if old == new:
            continue
        state = "added" if old is None else "removed" if new is None else "changed"
        rows.append({"path": path, "state": state,
                     "recorded_sha256": old, "current_sha256": new})
    return rows


def changed_book_pages(root):
    inventory = load(root / "edition/inventory.json", {})
    if not inventory.get("files"):
        return []
    rows = diff_maps(inventory["files"], inventory_members(root))
    return [row for row in rows
            if row["path"].startswith("book/") and row["path"].endswith(".md")]


def directory_revision_gaps(root):
    manifest = load(root / "edition/directory-migration.json")
    if not manifest:
        return []
    view = HistoricalView(root)
    gaps = []
    for record in manifest.get("documents", []):
        old_path = record["old_path"]
        new_path = record["new_path"]
        baseline = record["baseline_sha256"]
        try:
            current = sha(view.read_text(old_path))
        except FileNotFoundError:
            continue
        if current == baseline:
            continue
        if authorized(root, "directory_documents", new_path, baseline, current):
            continue
        gaps.append({"kind": "directory_documents", "path": new_path,
                     "previous_sha256": baseline, "current_sha256": current})
    return gaps


def enrichment_revision_gaps(root):
    manifest = load(root / "edition/enrichment-manifest.json")
    if not manifest:
        return []
    view = HistoricalView(root)
    gaps = []
    for record in manifest.get("new_documents", []):
        path = record["path"]
        target = view.path(path)
        if not target.is_file():
            gaps.append({"kind": "enrichment_documents", "path": path,
                         "previous_sha256": record["sha256"],
                         "current_sha256": None})
            continue
        current = sha(view.read_text(path))
        if current != record["sha256"] and not authorized(
                root, "enrichment_documents", path, record["sha256"], current):
            gaps.append({"kind": "enrichment_documents", "path": path,
                         "previous_sha256": record["sha256"],
                         "current_sha256": current})
    for record in manifest.get("modified_documents", []):
        path = record["path"]
        target = view.path(path)
        if not target.is_file():
            gaps.append({"kind": "enrichment_additions", "path": path,
                         "previous_sha256": record["addition_sha256"],
                         "current_sha256": None})
            continue
        text = view.read_text(path)
        heading = record["addition_heading"] + "\n"
        marker = record["insertion_marker"]
        start = text.find(heading)
        end = text.find(marker, start + len(heading)) if start >= 0 else -1
        if start < 0 or end < 0:
            gaps.append({"kind": "enrichment_additions", "path": path,
                         "previous_sha256": record["addition_sha256"],
                         "current_sha256": None})
            continue
        addition = sha(text[start:end])
        baseline = sha(text[:start] + text[end:])
        if addition != record["addition_sha256"] and not authorized(
                root, "enrichment_additions", path,
                record["addition_sha256"], addition):
            gaps.append({"kind": "enrichment_additions", "path": path,
                         "previous_sha256": record["addition_sha256"],
                         "current_sha256": addition})
        if baseline != record["baseline_sha256"] and not authorized(
                root, "enrichment_baselines", path,
                record["baseline_sha256"], baseline):
            gaps.append({"kind": "enrichment_baselines", "path": path,
                         "previous_sha256": record["baseline_sha256"],
                         "current_sha256": baseline})
    return gaps


def atlas_changes(root):
    manifest = load(root / "edition/atlas-manifest.json")
    if not manifest:
        return []
    rows = []
    for record in manifest.get("documents", []):
        target = root / record["path"]
        current = sha(target.read_text(encoding="utf-8")) if target.is_file() else None
        if current != record["sha256"]:
            rows.append({"path": record["path"],
                         "recorded_sha256": record["sha256"],
                         "current_sha256": current})
    return rows


def semantic_changes(root, route=None):
    audit = load(root / "edition/patterns/semantic-audit.v1.json")
    if not audit:
        return []
    rows = []
    for page in audit.get("pages", []):
        target = root / page["path"]
        current = sha(target.read_text(encoding="utf-8")) if target.is_file() else None
        if current != page["sha256"]:
            rows.append({"path": page["path"], "state": "hash-differs",
                         "recorded_sha256": page["sha256"],
                         "current_sha256": current})
    if route is not None:
        audit_paths = {page["path"] for page in audit.get("pages", [])}
        route_paths = {doc["path"] for doc in route["documents"]}
        for path in sorted(route_paths - audit_paths):
            rows.append({"path": path, "state": "missing-from-audit",
                         "recorded_sha256": None, "current_sha256": None})
        for path in sorted(audit_paths - route_paths):
            rows.append({"path": path, "state": "stale-audit-entry",
                         "recorded_sha256": None, "current_sha256": None})
    return rows


def state(artifact, value, reason, action=None, blocking=False, mode="auto"):
    return {"artifact": artifact, "state": value, "reason": reason,
            "action": action, "mode": mode, "blocking": blocking}


def validator_state(artifact, exc, action):
    message = str(exc)
    git_failure = ("not a git repository" in message
                   or "source-commit-not-ancestor" in message
                   or "returned non-zero exit status 128" in message)
    if git_failure:
        return state(artifact, "unavailable", message,
                     "run in a full git checkout with commit history", True, "manual")
    return state(artifact, "stale", message, action, True, "manual")


def semantic_audit_state(root, route):
    artifact = "edition/patterns/semantic-audit.v1.json"
    if load(root / artifact) is None:
        return state(artifact, "missing", "semantic audit is absent",
                     "restore or re-review the semantic audit", True, "manual")
    try:
        validate_pattern_semantic_audit.validate(root)
    except Exception as exc:  # noqa: BLE001 - validators fail with readable codes
        return validator_state(artifact, exc,
                               "re-review changed pages and update sha/review")
    changes = semantic_changes(root, route)
    if changes:
        return state(artifact, "stale",
                     str(len(changes)) + " page hashes or memberships differ",
                     "re-review changed pages and update sha/review", True, "manual")
    return state(artifact, "fresh", "validator and page hashes match")


def owner_units_state(root):
    artifact = "edition/patterns/owner-units.v1.json"
    if load(root / artifact) is None:
        return state(artifact, "missing", "owner units are absent",
                     "restore or re-audit the owner units", True, "manual")
    try:
        validate_pattern_owner_units.validate(root)
    except Exception as exc:  # noqa: BLE001 - validators fail with readable codes
        return validator_state(artifact, exc,
                               "re-audit the owner units and rebind evidence")
    return state(artifact, "fresh", "validator matches the current pages")


def route_state(root, route):
    artifact = "generated/route-index.v1.json"
    recorded = load(root / artifact)
    if recorded is None:
        return state(artifact, "missing", "route index is absent",
                     "python3 scripts/route_index.py build", True)
    if recorded != route:
        return state(artifact, "stale", "documents or snapshot differ",
                     "python3 scripts/route_index.py build", True)
    return state(artifact, "fresh", "matches the current book tree")


def fts_state(root, route):
    artifact = "generated/" + section_fts_index.INDEX_NAME
    path = root / artifact
    if not path.is_file():
        return state(artifact, "not-built", "the local section index is absent",
                     "python3 scripts/section_fts_index.py build", False, "advisory")
    try:
        with sqlite3.connect("file:" + path.as_posix() + "?mode=ro", uri=True) as con:
            row = con.execute("select value from meta where key = 'manifest'").fetchone()
        manifest = json.loads(row[0]) if row else {}
    except (sqlite3.Error, json.JSONDecodeError):
        return state(artifact, "stale", "the local section index is unreadable",
                     "python3 scripts/section_fts_index.py build", True)
    if manifest.get("route_snapshot_sha256") != route["snapshot_sha256"]:
        return state(artifact, "stale", "route snapshot differs",
                     "python3 scripts/section_fts_index.py build", True)
    return state(artifact, "fresh", "matches the current route snapshot")


def census_state(root, route_state_value):
    artifact = "edition/patterns/page-census.v1.json"
    if route_state_value != "fresh":
        return state(artifact, "deferred", "rebuild after the route index",
                     "python3 scripts/pattern_census.py --write", False)
    recorded = load(root / artifact)
    if recorded is None:
        return state(artifact, "missing", "page census is absent",
                     "python3 scripts/pattern_census.py --write", True)
    if recorded != pattern_census.build(root):
        return state(artifact, "stale", "documents or hashes differ",
                     "python3 scripts/pattern_census.py --write", True)
    return state(artifact, "fresh", "matches the current book tree")


def coverage_state(root, route_state_value):
    artifact = "edition/patterns/coverage-map.v1.json"
    reverse_artifact = "edition/patterns/reverse-map.v1.json"
    if route_state_value != "fresh":
        return state(artifact, "deferred", "rebuild after the route index",
                     "python3 scripts/pattern_coverage.py --write", False)
    recorded = load(root / artifact)
    reverse = load(root / reverse_artifact)
    if recorded is None or reverse is None:
        return state(artifact, "missing", "coverage artifacts are absent",
                     "python3 scripts/pattern_coverage.py --write", True)
    current, current_reverse = pattern_coverage.build(root)
    if recorded != current or reverse != current_reverse:
        return state(artifact, "stale", "coverage or reverse map differs",
                     "python3 scripts/pattern_coverage.py --write", True)
    return state(artifact, "fresh", "matches the current route snapshot")


def phase4_state(root, route_state_value, coverage_state_value):
    artifact = "edition/patterns/phase4.v1.json"
    if route_state_value != "fresh" or coverage_state_value != "fresh":
        return state(artifact, "deferred", "rebuild after route and coverage",
                     "python3 scripts/phase4_audit.py", False)
    recorded = load(root / artifact)
    if recorded is None:
        return state(artifact, "missing", "phase 4 artifact is absent",
                     "python3 scripts/phase4_audit.py", True)
    if recorded != phase4_audit.build(root):
        return state(artifact, "stale", "page dispositions or hashes differ",
                     "python3 scripts/phase4_audit.py", True)
    return state(artifact, "fresh", "matches the current inputs")


def source_plan_state(root, route):
    artifact = "edition/patterns/source-plan.v1.json"
    plan = load(root / artifact)
    if plan is None:
        return state(artifact, "missing", "source plan is absent",
                     "manual rebind after registry and ledger review", True, "manual")
    reasons = []
    if plan.get("route_index_snapshot") != route["snapshot_sha256"]:
        reasons.append("route snapshot differs")
    if plan.get("registry_sha256") != sha(
            (root / "edition/patterns/registry.v1.json").read_text(encoding="utf-8")):
        reasons.append("registry hash differs")
    ledger = load(root / "edition/patterns/reading-ledger.v1.json", {"records": []})
    if plan.get("summary", {}).get("ledger_records") != len(ledger.get("records", [])):
        reasons.append("ledger record count differs")
    if reasons:
        return state(artifact, "stale", "; ".join(reasons),
                     "manual rebind of snapshot, registry hash and ledger count",
                     True, "manual")
    return state(artifact, "fresh", "matches route, registry and ledger")


def delivery_state(root, route):
    artifact = "edition/patterns/delivery-evidence.v1.json"
    data = load(root / artifact)
    if data is None:
        return state(artifact, "missing", "delivery evidence is absent",
                     "manual rebind after counts stabilize", True, "manual")
    kinds = Counter(doc["kind"] for doc in route["documents"])
    sources = load(root / "sources/register.json", {"sources": []})
    ledger = load(root / "edition/patterns/reading-ledger.v1.json", {"records": []})
    registry = load(root / "edition/patterns/registry.v1.json", {"patterns": []})
    expected = {
        "pages": len(route["documents"]),
        "volumes": kinds["volume"],
        "chapters": kinds["chapter"],
        "entries": len(registry.get("patterns", [])),
        "sources": len(sources.get("sources", [])),
        "ledger_records": len(ledger.get("records", [])),
    }
    summary = data.get("summary", {})
    reasons = [key + " differs" for key, value in expected.items()
               if summary.get(key) != value]
    if reasons:
        return state(artifact, "stale", "; ".join(reasons),
                     "manual rebind after counts stabilize", True, "manual")
    try:
        validate_delivery_evidence.validate(root)
    except Exception as exc:  # noqa: BLE001 - validators fail with readable codes
        return validator_state(artifact, exc,
                               "manual rebind after the cited artifact is repaired")
    return state(artifact, "fresh", "summary and validator match the current tree")


def inventory_state(root):
    artifact = "edition/inventory.json"
    recorded = load(root / artifact)
    if recorded is None:
        return state(artifact, "missing", "edition inventory is absent",
                     "python3 scripts/validate_edition.py --write-inventory", True)
    rows = diff_maps(recorded.get("files", {}), inventory_members(root))
    if rows:
        return state(artifact, "stale", str(len(rows)) + " file hashes differ",
                     "python3 scripts/validate_edition.py --write-inventory", True)
    return state(artifact, "fresh", "file hashes match the current tree")


def error_plan(root, message):
    return {
        "clean": False,
        "blocking": True,
        "error": message,
        "root": str(root),
        "changed_pages": [],
        "missing_revisions": [],
        "atlas_changes": [],
        "semantic_changes": [],
        "artifacts": [],
        "steps": [
            {"kind": "review", "description": "Fix the reported error and rerun the plan",
             "command": None},
            {"kind": "check", "description": "Run the local premerge gate",
             "command": "python3 scripts/premerge_check.py --branch <branch> "
                        "--issue-title '<issue title>'"},
        ],
        "limits": [
            "Read-only plan; it does not validate claims, authorize revisions or replace premerge.",
            "The plan stopped before computing artifact states; no clean verdict is implied.",
        ],
    }


def build_plan(root, branch=None, issue_title=None):
    root = Path(root).resolve()
    try:
        route = canonical_scan(root)
    except Exception as exc:  # noqa: BLE001 - fail closed with a readable plan
        return error_plan(root, str(exc))

    artifacts = []

    def item(label, action, fn):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 - validators/builders fail with codes
            return state(label, "unavailable", str(exc), action, True, "manual")

    def rows(label, action, fn):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 - fail closed and keep the plan
            artifacts.append(state(label, "unavailable", str(exc), action, True, "manual"))
            return []

    changed = rows("book inventory", "inspect the error and refresh the inventory",
                   lambda: changed_book_pages(root))
    revisions = rows("content revisions", "inspect the error and record authorized revisions",
                     lambda: directory_revision_gaps(root) + enrichment_revision_gaps(root))
    atlas = rows("atlas manifest", "inspect the error and update the atlas manifest",
                 lambda: atlas_changes(root))
    semantic = rows("semantic audit", "inspect the error and re-review changed pages",
                    lambda: semantic_changes(root, route))
    if load(root / "edition/atlas-manifest.json") is None:
        artifacts.append(state("edition/atlas-manifest.json", "missing",
                               "atlas manifest is absent",
                               "restore or rebuild the atlas manifest", True, "manual"))

    route_item = item("generated/route-index.v1.json",
                      "python3 scripts/route_index.py build",
                      lambda: route_state(root, route))
    fts_item = item("generated/" + section_fts_index.INDEX_NAME,
                    "python3 scripts/section_fts_index.py build",
                    lambda: fts_state(root, route))
    census_item = item("edition/patterns/page-census.v1.json",
                       "python3 scripts/pattern_census.py --write",
                       lambda: census_state(root, route_item["state"]))
    coverage_item = item("edition/patterns/coverage-map.v1.json",
                         "python3 scripts/pattern_coverage.py --write",
                         lambda: coverage_state(root, route_item["state"]))
    phase4_item = item("edition/patterns/phase4.v1.json",
                       "python3 scripts/phase4_audit.py",
                       lambda: phase4_state(root, route_item["state"],
                                            coverage_item["state"]))
    plan_item = item("edition/patterns/source-plan.v1.json",
                     "manual rebind of snapshot, registry hash and ledger count",
                     lambda: source_plan_state(root, route))
    delivery_item = item("edition/patterns/delivery-evidence.v1.json",
                         "manual rebind after counts stabilize",
                         lambda: delivery_state(root, route))
    owner_item = item("edition/patterns/owner-units.v1.json",
                      "re-audit the owner units and rebind evidence",
                      lambda: owner_units_state(root))
    semantic_item = item("edition/patterns/semantic-audit.v1.json",
                         "restore or re-review the semantic audit",
                         lambda: semantic_audit_state(root, route))
    inventory_item = item("edition/inventory.json",
                          "python3 scripts/validate_edition.py --write-inventory",
                          lambda: inventory_state(root))

    artifacts.extend([route_item, fts_item, census_item, coverage_item, phase4_item,
                      plan_item, delivery_item, owner_item, semantic_item,
                      inventory_item])
    blocking = any(row["blocking"] for row in artifacts)
    blocking = blocking or bool(revisions) or bool(atlas) or bool(semantic)

    steps = []
    def add(kind, description, command=None):
        steps.append({"kind": kind, "description": description, "command": command})

    if revisions:
        add("review", "Record authorized revision(s) in edition/content-revisions.json")
    if atlas:
        add("review", "Update edition/atlas-manifest.json and re-review V11 pages")
    if any(row["artifact"] == "edition/atlas-manifest.json" and row["state"] == "missing"
           for row in artifacts):
        add("review", "Restore the atlas manifest and re-review V11 pages")
    if route_item["state"] in ("stale", "missing", "unavailable"):
        add("rebuild", "Rebuild the route index", "python3 scripts/route_index.py build")
    if fts_item["state"] == "stale":
        add("rebuild", "Rebuild the section FTS index",
            "python3 scripts/section_fts_index.py build")
    if fts_item["state"] == "not-built":
        add("optional", "Build the local section index if section search is used",
            "python3 scripts/section_fts_index.py build")
    if census_item["state"] in ("stale", "missing", "deferred", "unavailable"):
        add("rebuild", "Rebuild the page census",
            "python3 scripts/pattern_census.py --write")
    if coverage_item["state"] in ("stale", "missing", "deferred", "unavailable"):
        add("rebuild", "Rebuild coverage and reverse maps",
            "python3 scripts/pattern_coverage.py --write")
    if phase4_item["state"] in ("stale", "missing", "deferred", "unavailable"):
        add("rebuild", "Rebuild the phase 4 artifact", "python3 scripts/phase4_audit.py")
    if semantic or semantic_item["state"] != "fresh":
        add("review", "Restore or re-review the semantic audit and update sha/review")
    if plan_item["state"] in ("stale", "missing", "unavailable"):
        add("review", "Rebind the source plan snapshot, registry hash and ledger count")
    if delivery_item["state"] in ("stale", "missing", "unavailable"):
        add("review", "Rebind delivery-evidence counts and source commit")
    if owner_item["state"] in ("stale", "missing", "unavailable"):
        add("review", "Re-audit owner units and rebind delivery evidence")
    if inventory_item["state"] in ("stale", "missing", "unavailable"):
        add("rebuild", "Refresh the edition inventory after review",
            "python3 scripts/validate_edition.py --write-inventory")
    if any(row["state"] == "unavailable" for row in artifacts):
        add("review", "Inspect the reported unavailable artifact before rebuilding")
    add("check", "Run lexical boundary and line-length checks",
        "python3 scripts/check_boundary.py && python3 scripts/check_markdown_line_length.py")
    branch_arg = branch or "<branch>"
    title_arg = issue_title or "<issue title>"
    add("check", "Run the local premerge gate",
        "python3 scripts/premerge_check.py --branch " + shlex.quote(branch_arg) +
        " --issue-title " + shlex.quote(title_arg))
    add("check", "Run the test suite",
        "python3 -m unittest discover -s tests -p 'test_tycho*.py'")

    return {
        "clean": not blocking,
        "blocking": blocking,
        "root": str(root),
        "changed_pages": changed,
        "missing_revisions": revisions,
        "atlas_changes": atlas,
        "semantic_changes": semantic,
        "artifacts": artifacts,
        "steps": steps,
        "limits": [
            "Read-only plan; it does not validate claims, authorize revisions or replace premerge.",
            "New or removed pages also change outline, membership and counts; premerge remains the gate.",
            "Decomposition source-block revisions are not enumerated; premerge and its tests remain the gate.",
            "Source-commit ancestry checks need a full git checkout with history; export or shallow copies report unavailable.",
            "A not-built local section index is advisory and does not block a book change.",
            "Manual steps must be reviewed by a human or agent; the plan does not accept them.",
        ],
    }


def render_text(plan):
    lines = ["Book change plan (read-only)", "Repository: " + plan["root"], ""]
    if plan.get("error"):
        lines.append("Plan failed: " + plan["error"])
        lines.append("")
    if plan["clean"]:
        lines.append("Clean: no changed pages, missing revisions or stale artifacts detected.")
    else:
        lines.append("Blocking: changed pages, missing revisions or stale artifacts require work.")
    lines.append("Changed book pages: " + str(len(plan["changed_pages"])))
    lines.append("Missing authorized revisions: " + str(len(plan["missing_revisions"])))
    lines.append("Atlas page changes: " + str(len(plan["atlas_changes"])))
    lines.append("Semantic-audit page changes: " + str(len(plan["semantic_changes"])))
    lines.append("")
    if plan["changed_pages"]:
        lines.append("Changed pages:")
        for row in plan["changed_pages"]:
            lines.append("- " + row["path"] + " (" + row["state"] + ")")
        lines.append("")
    if plan["missing_revisions"]:
        lines.append("Missing revisions:")
        for row in plan["missing_revisions"]:
            lines.append("- " + row["kind"] + ": " + row["path"])
            lines.append("  previous_sha256: " + str(row["previous_sha256"]))
            lines.append("  current_sha256:  " + str(row["current_sha256"]))
        lines.append("")
    if plan["atlas_changes"]:
        lines.append("Atlas pages to rebind:")
        for row in plan["atlas_changes"]:
            lines.append("- " + row["path"])
        lines.append("")
    stale = [item for item in plan["artifacts"]
             if item["state"] not in ("fresh", "not-built")]
    optional = [item for item in plan["artifacts"] if item["state"] == "not-built"]
    if stale:
        lines.append("Artifacts:")
        for item in stale:
            lines.append("- " + item["artifact"] + ": " + item["state"] + " (" +
                         item["reason"] + ")")
            if item["action"]:
                lines.append("  action: " + item["action"])
        lines.append("")
    if optional:
        lines.append("Optional:")
        for item in optional:
            lines.append("- " + item["artifact"] + ": " + item["state"])
            if item["action"]:
                lines.append("  action: " + item["action"])
        lines.append("")
    if plan["semantic_changes"]:
        lines.append("Semantic review required:")
        for row in plan["semantic_changes"]:
            lines.append("- " + row["path"] + " (" + row.get("state", "changed") + ")")
        lines.append("")
    if plan["steps"]:
        lines.append("Suggested order:")
        for number, step in enumerate(plan["steps"], 1):
            line = str(number) + ". [" + step["kind"] + "] " + step["description"]
            if step["command"]:
                line += "\n   " + step["command"]
            lines.append(line)
        lines.append("")
    lines.append("Limits:")
    for limit in plan["limits"]:
        lines.append("- " + limit)
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--plan", action="store_true", help="print the plan (default)")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero while blocking work remains")
    parser.add_argument("--branch", help="branch for the premerge command")
    parser.add_argument("--issue-title", help="issue title for the premerge command")
    args = parser.parse_args(argv)
    try:
        plan = build_plan(args.root, args.branch, args.issue_title)
    except Exception as exc:  # noqa: BLE001 - a plan must fail closed with a readable error
        plan = error_plan(Path(args.root).resolve(), str(exc))
    if args.json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    else:
        print(render_text(plan))
    return 1 if plan.get("error") or (args.strict and plan["blocking"]) else 0


if __name__ == "__main__":
    sys.exit(main())
