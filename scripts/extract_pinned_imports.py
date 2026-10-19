#!/usr/bin/env python3
"""Deterministic, read-only *syntactic* import observations at pinned Git SHA.

Not a full call graph, runtime dependency detector, Java parser, Graphify
replacement or validated graph assembly. Requires an already downloaded,
clean, detached, remote-free pinned checkout produced by E03-02.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TOOL_VERSION = "tycho-syntactic-imports/0.1"
MAX_FILES = 1000
MAX_FILE_BYTES = 1024 * 1024
JAVA_IMPORT = re.compile(
    r"^[ \t]*import[ \t]+(static[ \t]+)?([A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*|\.\*)+)[ \t]*;",
    re.MULTILINE,
)
JAVA_COMMENTS = re.compile(r"/\*.*?\*/|//[^\n]*", re.DOTALL)


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def git(path, *args):
    result = subprocess.run(
        ["git", "-C", str(path), *args], capture_output=True,
        check=False, timeout=30,
    )
    if result.returncode:
        raise ValueError("Git inspection failed: " + args[0])
    return result.stdout


def syntactic_imports(path, text):
    """Import identifiers only, never claim resolution/call direction."""
    if path.endswith(".py"):
        try:
            tree = ast.parse(text, filename=path)
        except SyntaxError as exc:
            raise ValueError("Invalid Python syntax: " + path) from exc
        result = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                result.extend(("python", alias.name, node.lineno, "ast.Import") for alias in node.names)
            if isinstance(node, ast.ImportFrom):
                name = "." * node.level + (node.module or "")
                result.extend(("python", name + ("." + alias.name if alias.name else ""),
                               node.lineno, "ast.ImportFrom") for alias in node.names)
        return result
    if path.endswith(".java"):
        without_comments = JAVA_COMMENTS.sub(
            lambda m: "\n" * m.group(0).count("\n"), text
        )
        return [("java", match.group(2), without_comments.count("\n", 0, match.start()) + 1,
                 "java-import-token") for match in JAVA_IMPORT.finditer(without_comments)]
    raise ValueError("unsupported language")


def extract(root, source_id, limit=MAX_FILES):
    from public_repo_snapshots import inspect_checkout, load_manifest
    entries = {e["id"]: e for e in load_manifest()}
    require(source_id in entries, "Unknown or unlocked public Git source ID")
    locked = entries[source_id]
    root = Path(root)
    revision = inspect_checkout(root, locked)
    names = [x.decode("utf-8", "strict") for x in git(root, "ls-files", "-z", "--", "*.java", "*.py").split(b"\0") if x]
    names.sort()
    require(0 < len(names) <= limit <= MAX_FILES,
            "No supported tracked source files or extraction scope exceeds allowed limit")
    evidence = []
    for name in names:
        require(not name.startswith("/") and ".." not in name.split("/")
                and "\\" not in name, "unsafe Git path")
        data = git(root, "show", "HEAD:" + name)
        require(len(data) <= MAX_FILE_BYTES, "source file exceeds per-file budget")
        try:
            src = data.decode("utf-8", "strict")
        except UnicodeDecodeError as exc:
            raise ValueError("Source is not UTF-8: " + name) from exc
        for lang, imported, line, parser in syntactic_imports(name, src):
            edge_id = hashlib.sha256(
                (source_id + "\0" + revision + "\0" + name + "\0" + lang +
                 "\0" + imported + "\0" + str(line)).encode()
            ).hexdigest()[:24]
            evidence.append({
                "id": "import:" + edge_id, "kind": "imports", "plane": "code",
                "from": {"source_id": source_id, "revision": revision, "path": name},
                "to": {"language": lang, "unresolved_import": imported},
                "source_line": line, "extractor": parser,
                "semantic_limit": "syntactic import only; target may not resolve, no runtime call inferred",
            })
    evidence.sort(key=lambda e: (e["from"]["path"], e["source_line"], e["to"]["unresolved_import"], e["id"]))
    return {
        "format": "tycho-import-observations-v1",
        "tool_version": TOOL_VERSION, "source_id": source_id,
        "locked_revision": revision,
        "scope": {"tracked_supported_files": len(names), "max_files": limit,
                  "languages": ["java", "python"], "unsupported": "other languages and dynamic references"},
        "observations": evidence, "checked_out_code_executed": False,
        "claim": "Static import syntax only; not an independently validated dependency graph",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--max-files", type=int, default=MAX_FILES)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(1 <= args.max_files <= MAX_FILES, "Invalid file budget")
    require(not args.out.exists(), "Refuse overwrite of existing report")
    out = extract(args.checkout, args.source_id, args.max_files)
    args.out.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Recorded", len(out["observations"]), "syntactic import observations at", out["locked_revision"])


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
