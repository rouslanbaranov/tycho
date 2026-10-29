#!/usr/bin/env python3
"""Build or check the Phase 4 page/entry audit and route artifact."""
import argparse
import hashlib
import json
import posixpath
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assemble_edition import split
from validate_pattern_registry import slug_heading
from route_index import legacy_scope

ARTIFACT = Path("edition/patterns/phase4.v1.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
LEDGER = Path("edition/patterns/reading-ledger.v1.json")
BATCHES = Path("edition/patterns/card-batches.v1.json")
ROUTE = Path("generated/route-index.v1.json")
COVERAGE = Path("edition/patterns/coverage-map.v1.json")
MANIFEST = Path("edition/atlas-manifest.json")
DIMENSIONS = [
    "identity", "decision_question", "good_fit", "contraindications",
    "competing_alternative", "failure_recovery", "technical_owner",
    "owner_anchor", "backlink", "source_ledger", "read_source",
    "decision_state", "technical_coverage", "decision_coverage",
]


def load(root, path):
    return json.loads((Path(root) / path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def norm(value):
    value = value.lower().replace("&", " and ").replace("/", " ").replace("-", " ")
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def github_slug(label):
    text = re.sub(r"<[^>]*>", "", label)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = text.strip().rstrip("#").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s", "-", text)


def section(body, slug):
    return section_with_anchor(body, slug)[0]


def section_with_anchor(body, slug):
    """Return the bounded section and its rendered GitHub heading anchor."""
    lines = body.splitlines()
    seen = {}
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        level, label = match.group(1), match.group(2)
        base = github_slug(label)
        count = seen.get(base, 0)
        actual = base if count == 0 else f"{base}-{count}"
        seen[base] = count + 1
        if level not in ("###", "#"):
            continue
        if (slug_heading(label) == slug
                or actual.replace("--", "-") == slug.replace("--", "-")):
            start = index + 1
            end = len(lines)
            for cursor in range(start, len(lines)):
                if lines[cursor].startswith("### ") or lines[cursor].startswith("## "):
                    end = cursor
                    break
            return "\n".join(lines[start:end]), actual
    return "", slug


def field(text, label):
    match = re.search(r"\*\*" + label + r"\.\*\*\s*(.+?)(?:\n\n|\Z)", text, re.S)
    return " ".join(match.group(1).split()) if match else ""


def page_disposition(document, owner_paths, candidate_paths):
    path = document["path"]
    kind = document["kind"]
    if path.startswith("book/volumes/v11-pattern-atlas/"):
        return "atlas-decision", "V11 decision layer"
    if path in owner_paths:
        return "technical-owner", "linked by a pattern card"
    if path in candidate_paths:
        return "candidate-owner", "strong/medium routing candidate, not audited owner"
    if kind in ("volume", "chapter", "landing"):
        return "navigation", "volume/chapter/landing navigation"
    if any(path.startswith(prefix) for prefix in (
            "book/distributed/", "book/scaling/", "book/delivery/",
            "book/observability/", "book/application/", "book/cases/")):
        return "legacy-cross-volume", "cross-volume supporting page"
    return "canonical-technical-page", "canonical page not linked as a pattern owner"


def build(root=ROOT):
    root = Path(root).resolve()
    registry = load(root, REGISTRY)
    ledger = load(root, LEDGER)
    batches = load(root, BATCHES)
    route = legacy_scope(load(root, ROUTE))
    coverage = load(root, COVERAGE)
    manifest = load(root, MANIFEST)
    documents = route["documents"]
    if len(documents) < 423:
        raise ValueError("phase4-page-count")
    chapters = {chapter["code"]: chapter for chapter in manifest["chapters"]}
    records = {record["id"]: record for record in ledger["records"]}
    patterns = {pattern["id"]: pattern for pattern in registry["patterns"]}
    owner_paths = {p["technical_owner"]["path"] for p in patterns.values()
                   if p["technical_owner"].get("path")}
    candidate_paths = {page["path"] for entry in coverage["entries"]
                       for page in entry["candidate_pages"]
                       if page["confidence"] in ("strong", "medium")}
    dispositions = []
    for document in sorted(documents, key=lambda item: item["path"]):
        disposition, reason = page_disposition(document, owner_paths, candidate_paths)
        dispositions.append({"document_id": document["id"], "path": document["path"],
                             "kind": document["kind"], "disposition": disposition,
                             "reason": reason})
    aliases = {}
    for pattern in patterns.values():
        for label in [pattern["catalog_name"], *pattern.get("aliases", [])]:
            aliases[norm(label)] = pattern["id"]
    manual = {
        "cqrs": "tycho.pattern.command-query-responsibility-segregation-cqrs",
        "cdn edge caching": "tycho.pattern.cdn-edge-caching",
        "sli slo error budgets": "tycho.pattern.sli-slo-and-error-budgets",
        "health readiness liveness checks": "tycho.pattern.health-readiness-and-liveness-checks",
        "message broker": "tycho.pattern.message-broker-messaging-bridge",
        "process manager": "tycho.pattern.process-manager-routing-slip",
        "dead letter channel": "tycho.pattern.dead-letter-channel-dlq",
        "db per service": "tycho.pattern.database-per-service",
        "hexagonal architecture": "tycho.pattern.hexagonal-architecture-ports-and-adapters",
        "blue green": "tycho.pattern.blue-green-deployment",
        "tenant isolation": "tycho.pattern.tenant-based-resource-isolation",
        "backup pitr": "tycho.pattern.backup-pitr-and-restore",
        "dark launching": "tycho.pattern.dark-launching-shadow-traffic",
        "quorum": "tycho.pattern.quorum-coordination",
        "write through": "tycho.pattern.write-through-cache",
        "request reply": "tycho.pattern.request-reply-messaging",
        "sli slo": "tycho.pattern.sli-slo-and-error-budgets",
        "backend for frontend": "tycho.pattern.backend-for-frontend-bff",
        "service oriented architecture": "tycho.pattern.service-oriented-architecture-soa",
        "health checks": "tycho.pattern.health-readiness-and-liveness-checks",
        "readiness probes": "tycho.pattern.health-readiness-and-liveness-checks",
    }
    aliases.update(manual)
    card_entries = []
    for batch in batches["batches"]:
        chapter = chapters[batch["chapter"]]
        for entry in batch["entries"]:
            card_path = entry.get("card_path", chapter["path"])
            _, body = split((root / card_path).read_text(encoding="utf-8"))
            text, card_anchor = section_with_anchor(body, entry["atlas_section"])
            owner = patterns[entry["pattern_id"]]["technical_owner"]
            owner_file = root / owner["path"]
            owner_text = owner_file.read_text(encoding="utf-8") if owner_file.is_file() else ""
            atlas_links = [card_path.split("book/volumes/", 1)[-1] + "#" + card_anchor]
            if card_path != chapter["path"]:
                _, chapter_body = split((root / chapter["path"]).read_text(encoding="utf-8"))
                chapter_text = section(chapter_body, entry["atlas_section"])
                chapter_target = posixpath.relpath(card_path,
                                                   posixpath.dirname(chapter["path"]))
                if "](" + chapter_target + ")" in chapter_text:
                    atlas_links.append(chapter["path"].split("book/volumes/", 1)[-1]
                                       + "#" + entry["atlas_section"])
            record = records.get(entry["ledger_record"])
            dimensions = {
                "identity": "pass" if "**Identity.**" in text else "missing",
                "decision_question": "pass" if "**Decision question.**" in text else "missing",
                "good_fit": "pass" if "**Good-fit conditions.**" in text else "missing",
                "contraindications": "pass" if "**Hard contraindications.**" in text else "missing",
                "competing_alternative": "pass" if "**Competing alternative.**" in text else "missing",
                "failure_recovery": "pass" if "**Failure and recovery.**" in text else "missing",
                "technical_owner": ("partial" if owner.get("state") in (
                    "partial", "partial-bounded", "partial-reviewed")
                    else owner.get("state", "missing")),
                "owner_anchor": "pass" if owner.get("anchor") else "missing",
                "backlink": ("pass" if any(link in owner_text for link in atlas_links)
                             else "missing"),
                "source_ledger": "pass" if record else "missing",
                "read_source": "pass" if record and record.get("status") == "read" else "missing",
                "decision_state": "pass" if "**Decision state.**" in text else "missing",
                "technical_coverage": patterns[entry["pattern_id"]]["coverage"]["technical"],
                "decision_coverage": patterns[entry["pattern_id"]]["coverage"]["decision"],
            }
            pattern_coverage = patterns[entry["pattern_id"]]["coverage"]
            gaps = ["technical-" + pattern_coverage["technical"],
                    "decision-" + pattern_coverage["decision"],
                    "independent-review-missing"]
            if dimensions["backlink"] != "pass":
                gaps.append("backlink-missing")
            card_entries.append({"pattern_id": entry["pattern_id"],
                                 "atlas_section": entry["atlas_section"],
                                 "dimensions": dimensions, "gaps": gaps,
                                 "question": field(text, "Decision question")})
    audited = {item["pattern_id"] for item in card_entries}
    for pattern in patterns.values():
        if pattern["id"] in audited:
            continue
        dimensions = {name: "blocked" for name in DIMENSIONS}
        dimensions["technical_coverage"] = pattern["coverage"]["technical"]
        dimensions["decision_coverage"] = pattern["coverage"]["decision"]
        card_entries.append({"pattern_id": pattern["id"], "atlas_section": pattern["atlas_section"],
                             "dimensions": dimensions,
                             "gaps": ["blocked-source", "no-card"], "question": ""})
    card_entries.sort(key=lambda item: item["pattern_id"])
    routes = set()
    related_dispositions = []
    for item in card_entries:
        text = ""
        pattern = patterns[item["pattern_id"]]
        # Re-read the card only for related labels.
        for batch in batches["batches"]:
            chapter = chapters[batch["chapter"]]
            card_entry = next((entry for entry in batch["entries"]
                               if entry["pattern_id"] == pattern["id"]), None)
            if card_entry:
                source = card_entry.get("card_path", chapter["path"])
                _, body = split((root / source).read_text(encoding="utf-8"))
                text = section(body, pattern["atlas_section"])
                break
        related = field(text, "Related entries")
        for label in [part.strip() for part in related.split(";") if part.strip()]:
            target = aliases.get(norm(label))
            if target and target != pattern["id"]:
                routes.add((pattern["id"], target))
            elif not target:
                related_dispositions.append({
                    "from": pattern["id"],
                    "label": label,
                    "disposition": "non-route",
                    "target": None,
                    "reason": "label names a technical concept or owner section "
                              "outside the 145-entry catalog; no alias is invented",
                })
    route_rows = [{"from": source, "to": target, "basis": "card-related-entry"}
                  for source, target in sorted(routes)]
    related_dispositions.sort(key=lambda item: (item["from"], item["label"]))
    questions = [{"pattern_id": item["pattern_id"], "atlas_section": item["atlas_section"],
                  "question": item["question"]} for item in card_entries if item["question"]]
    gap_matrix = []
    for item in card_entries:
        pattern = patterns[item["pattern_id"]]
        gap_matrix.append({
            "pattern_id": pattern["id"],
            "technical": pattern["coverage"]["technical"],
            "decision": pattern["coverage"]["decision"],
            "overall": pattern["coverage"]["overall"],
            "card": bool(item["question"]),
            "owner_state": pattern["technical_owner"]["state"],
            "gaps": item["gaps"],
        })
    return {
        "schema_version": 1,
        "generated_from": {
            "registry_sha256": sha(root / REGISTRY),
            "ledger_sha256": sha(root / LEDGER),
            "card_batches_sha256": sha(root / BATCHES),
            "route_index_sha256": sha(root / ROUTE),
            "coverage_sha256": sha(root / COVERAGE),
        },
        "dimensions": DIMENSIONS,
        "summary": {
            "pages": len(dispositions),
            "entries": len(card_entries),
            "cards": len(questions),
            "routes": len(route_rows),
            "related_labels": len(related_dispositions),
            "non_routes": sum(1 for item in related_dispositions
                              if item["disposition"] == "non-route"),
            "unresolved_related": 0,
            "retrieval_questions": len(questions),
            "blocked_entries": sum(1 for item in card_entries if "blocked-source" in item["gaps"]),
        },
        "page_dispositions": dispositions,
        "entry_audit": card_entries,
        "gap_matrix": gap_matrix,
        "routes": route_rows,
        "related_dispositions": related_dispositions,
        "retrieval_questions": questions,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build(args.root)
    path = args.root / ARTIFACT
    if args.check:
        if not path.is_file():
            print("FAIL: phase4-artifact-missing", file=sys.stderr)
            return 1
        if load(args.root, ARTIFACT) != data:
            print("FAIL: phase4-artifact-stale", file=sys.stderr)
            return 1
        print("PASS: phase4", data["summary"]["pages"], "pages,", data["summary"]["entries"], "entries")
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(data["summary"], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
