#!/usr/bin/env python3
"""Deterministic, deliberately conservative Tycho YAML-frontmatter insertion.

Input is a reviewed versioned JSON metadata instance, never invented by the
tool. Supports render, diff and explicit apply. Never silently modifies an
existing, different frontmatter block or a content body.
"""
import argparse
import difflib
import json
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCHEMA = ROOT / "schemas/document-metadata.v1.schema.json"
FIELDS = (
    "metadata_version", "id", "kind", "parent_id", "canonical_path",
    "title", "topic_ids", "perspectives", "summary", "route_hints",
    "evidence_scope", "content_review", "authored_at", "updated_at",
    "source_inspection_date", "content_verified_at",
)
ID = re.compile(r"^tycho\.(?:book|volume|chapter|page|landing|decision)\.[a-z0-9]{6,32}$")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def scalar(value):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)) and type(value) is not bool:
        return json.dumps(value, allow_nan=False)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    raise ValueError("Unsupported frontmatter scalar type")


def emit_mapping(mapping, indent=0):
    lines = []
    for key, value in mapping.items():
        if not re.fullmatch(r"[a-z_]+", key):
            raise ValueError("Unsafe YAML mapping key")
        prefix = " " * indent + key + ":"
        if isinstance(value, dict):
            lines.append(prefix)
            lines.extend(emit_mapping(value, indent + 2))
        elif isinstance(value, list):
            if not value:
                lines.append(prefix + " []")
            else:
                lines.append(prefix)
                for element in value:
                    if isinstance(element, (dict, list)):
                        raise ValueError("Nested YAML array not supported in v1")
                    lines.append(" " * (indent + 2) + "- " + scalar(element))
        else:
            lines.append(prefix + " " + scalar(value))
    return lines


def render(meta):
    if not isinstance(meta, dict) or set(meta) != set(FIELDS):
        raise ValueError("Metadata instance must match exact v1 keys")
    if not isinstance(meta.get("id"), str) or not ID.fullmatch(meta["id"]):
        raise ValueError("Missing/invalid permanent identity")
    if not isinstance(meta.get("canonical_path"), str):
        raise ValueError("Invalid canonical path")
    ordered = {key: meta[key] for key in FIELDS}
    return "---\n" + "\n".join(emit_mapping(ordered)) + "\n---\n"


def target_path(root, meta):
    path = meta["canonical_path"]
    if (path.startswith("/") or "\\" in path or not path.endswith(".md")
            or any(x in ("", ".", "..", ".git") for x in path.split("/"))
            or not path.startswith("book/")):
        raise ValueError("Only canonical book Markdown paths are writable")
    root = Path(root).resolve()
    target = root / path
    if target.is_symlink() or not target.is_file() or target.resolve().parent != target.parent.resolve():
        raise ValueError("File not found or symbolic link refused")
    if not target.resolve().is_relative_to((root / "book").resolve()):
        raise ValueError("Path escapes book directory")
    return target


def proposed_change(body, expected):
    if body.startswith("---\n") or body.startswith("---\r\n"):
        match = FRONTMATTER.match(body)
        if match is None:
            raise ValueError("Malformed existing frontmatter: refuse to overwrite")
        existing = match.group(0).replace("\r\n", "\n")
        if existing == expected:
            return "unchanged", body
        # Do not parse/overwrite an untrusted existing YAML header. In
        # particular, never replace IDs, claim states or verification dates.
        return "conflict-existing-frontmatter", body
    return "would-insert", expected + "\n" + body


def apply_safe(target, expected, *, allow_write):
    original = target.read_bytes()
    try:
        body = original.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("Only UTF-8 Markdown may be modified") from exc
    status, content = proposed_change(body, expected)
    if status in ("unchanged", "conflict-existing-frontmatter"):
        return status
    if not allow_write:
        return status
    staged = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=target.parent,
                                         prefix=".tycho-frontmatter-", delete=False) as out:
            staged = Path(out.name)
            out.write(content.encode("utf-8"))
        staged.chmod(target.stat().st_mode)
        if target.read_bytes() != original:
            raise ValueError("Markdown changed concurrently; refuse overwrite")
        os.replace(staged, target)
        staged = None
    finally:
        if staged and staged.exists():
            staged.unlink()
    return "inserted"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("render", "diff", "apply"))
    p.add_argument("--metadata", type=Path, required=True,
                   help="Reviewed canonical JSON metadata instance")
    p.add_argument("--root", type=Path, default=ROOT)
    p.add_argument("--allow-write", action="store_true", help="Explicitly permit initial header insertion")
    args = p.parse_args()
    # Dedicated JSON Schema CLI fails closed if the dependency is unavailable.
    from validate_metadata_schemas import validate_document, SCHEMAS
    # The metadata input is validated against strict draft 2020-12 before any I/O.
    # The schema file is selected independently of the metadata payload.
    meta = validate_document("document", args.metadata)
    header = render(meta)
    if args.action == "render":
        print(header, end="")
        return
    target = target_path(args.root, meta)
    content = target.read_text(encoding="utf-8")
    status, proposal = proposed_change(content, header)
    if args.action == "diff":
        if status == "conflict-existing-frontmatter":
            print(status + ": manual review required; no automatic normalization")
        elif status == "unchanged":
            print("unchanged")
        else:
            print("would insert frontmatter into " + str(meta["canonical_path"]))
            print("".join(difflib.unified_diff(
                [], header.splitlines(keepends=True), fromfile="old-header",
                tofile="proposed-header", n=0)), end="")
    else:
        result = apply_safe(target, header, allow_write=args.allow_write)
        print(result + ": " + str(meta["canonical_path"]))


if __name__ == "__main__":
    main()
