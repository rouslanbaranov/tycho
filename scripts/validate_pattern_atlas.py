#!/usr/bin/env python3
"""Validate the V11 pattern-atlas scaffold against its manifest and registry.

Structural checks only: hashes, identities, parent links, anchors and the
catalog partition. This does not prove technical truth, source reading or review.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assemble_edition import split
from validate_pattern_registry import heading_slugs

TICK = chr(96)
MANIFEST = Path("edition/atlas-manifest.json")
SCHEMA = Path("schemas/pattern-atlas.v1.schema.json")
REGISTRY = Path("edition/patterns/registry.v1.json")
OUTLINE = Path("edition/outline.json")
BOOK_ID = "tycho.book.37c50125355948f1b52ec66229ef59bd"
FAMILY_SECTIONS = ("## Purpose and mission", "## Pages and reasoning route",
                   "## Entry inventory", "## Navigation and prerequisites",
                   "## Evidence and known limits")
VOLUME_SECTIONS = ("## Purpose and mission", "## A worked cross-chapter synthesis",
                   "## Questions and chapters", "## Counterexample and handoff",
                   "## Evidence and known limits")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def engine():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError("Install validation dependencies from requirements-validation.txt") from exc
    return Draft202012Validator, FormatChecker


def validate_data(data, root=ROOT):
    root = Path(root).resolve()
    Draft, Format = engine()
    schema = load(root / SCHEMA)
    Draft.check_schema(schema)
    validator = Draft(schema, format_checker=Format())
    errors = sorted(validator.iter_errors(data),
                    key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError("atlas-schema: " + str(len(errors)) + " error(s), first at "
                         + path + ": " + first.message)

    registry = load(root / REGISTRY)
    outline = load(root / OUTLINE)
    require(data["version"] == outline["version"], "atlas-edition-version")
    require(data["parent_issue"] == 228, "atlas-parent-issue")
    require(data["epic_issue"] == 233, "atlas-epic-issue")
    require(data["task_issue"] == 234, "atlas-task-issue")
    require(data["registry_sha256"] == hashlib.sha256(
        (root / REGISTRY).read_bytes()).hexdigest(), "atlas-registry-hash")
    require(data["status"] in ("scaffolded", "authoring", "reviewed"),
            "atlas-status")

    documents = data["documents"]
    require(len(documents) >= 12, "atlas-document-count")
    by_id = {}
    by_path = {}
    for doc in documents:
        require(doc["id"] not in by_id, "atlas-duplicate-document-id")
        require(doc["path"] not in by_path, "atlas-duplicate-document-path")
        path = root / doc["path"]
        require(path.is_file() and not path.is_symlink(), "atlas-document-missing")
        text = path.read_text(encoding="utf-8")
        meta, body = split(text)
        require(meta["id"] == doc["id"], "atlas-document-id")
        require(meta["kind"] == doc["kind"], "atlas-document-kind")
        require(meta["canonical_path"] == doc["path"], "atlas-document-path")
        require(meta["title"] == doc["title"], "atlas-document-title")
        require(hashlib.sha256(text.encode("utf-8")).hexdigest() == doc["sha256"],
                "atlas-document-sha")
        by_id[doc["id"]] = doc
        by_path[doc["path"]] = doc

    volume = data["volume"]
    require(volume["id"] in by_id and by_id[volume["id"]]["kind"] == "volume",
            "atlas-volume-document")
    require(volume["path"] == by_id[volume["id"]]["path"], "atlas-volume-path")
    require(by_id[volume["id"]]["parent_id"] == BOOK_ID, "atlas-volume-parent")
    volume_text = (root / volume["path"]).read_text(encoding="utf-8")
    _, volume_body = split(volume_text)
    for section in VOLUME_SECTIONS:
        require(section in volume_body, "atlas-volume-section: " + section)
    require(TICK * 3 + "mermaid" in volume_body, "atlas-volume-diagram")

    chapters = data["chapters"]
    require(len(chapters) == 11, "atlas-chapter-count")
    codes = [item["code"] for item in chapters]
    require(codes == ["V11/C%02d" % number for number in range(1, 12)],
            "atlas-chapter-codes")
    family_by_id = {item["id"]: item for item in registry["families"]}
    pattern_ids = {item["id"] for item in registry["patterns"]}
    seen = set()
    for chapter in chapters:
        require(chapter["id"] in by_id and by_id[chapter["id"]]["kind"] == "chapter",
                "atlas-chapter-document")
        require(chapter["path"] == by_id[chapter["id"]]["path"], "atlas-chapter-path")
        require(by_id[chapter["id"]]["parent_id"] == volume["id"], "atlas-chapter-parent")
        require(chapter["family"] in family_by_id, "atlas-chapter-family")
        family = family_by_id[chapter["family"]]
        require(set(chapter["pattern_ids"]) == set(family["pattern_ids"]),
                "atlas-pattern-partition")
        require(not (seen & set(chapter["pattern_ids"])), "atlas-pattern-duplicate")
        seen.update(chapter["pattern_ids"])
        chapter_text = (root / chapter["path"]).read_text(encoding="utf-8")
        _, body = split(chapter_text)
        for section in FAMILY_SECTIONS:
            require(section in body, "atlas-chapter-section: " + section)
        anchors = heading_slugs(root / chapter["path"])
        for pattern_id in chapter["pattern_ids"]:
            pattern = next(p for p in registry["patterns"] if p["id"] == pattern_id)
            require(pattern["atlas_section"] in anchors,
                    "atlas-missing-anchor: " + pattern_id)
    require(seen == pattern_ids, "atlas-catalog-partition")
    require(len(by_id) == 12, "atlas-document-kind-count")

    return {
        "version": data["version"],
        "volume": volume["code"],
        "chapters": len(chapters),
        "documents": len(documents),
        "patterns": len(seen),
        "scope": "structural manifest, hashes and anchors; not source or technical truth",
    }


def validate(root=ROOT):
    root = Path(root).resolve()
    data = load(root / MANIFEST)
    return validate_data(data, root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("PASS: atlas", result["volume"], result["chapters"], "chapters,",
              result["documents"], "documents,", result["patterns"], "patterns")
    return 0


if __name__ == "__main__":
    sys.exit(main())
