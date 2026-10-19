#!/usr/bin/env python3
"""Non-enriching Tycho knowledge-validation orchestration (E04-06).

Explicit local runner; never invokes source acquisition, clone, reindex,
frontmatter apply, external services or GitHub Actions.
All commands are read-only and their results must be reported honestly.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "sources/register.json": ("schema_version", 2),
    "sources/public-repositories.lock.json": ("schema_version", 1),
    "sources/claim-references.json": ("schema_version", 1),
    "sources/document-observations.json": ("schema_version", 1),
    "sources/research-events.json": ("schema_version", 1),
}
SCHEMAS = (
    "schemas/document-metadata.v1.schema.json",
    "schemas/source-reference.v1.schema.json",
)
CORE = (
    ("source-register", ["scripts/validate_sources.py"]),
    ("source-catalogue", ["scripts/source_catalog.py", "--check"]),
    ("public-repo-lock", ["scripts/public_repo_snapshots.py", "check"]),
    ("claim-provenance", ["scripts/validate_claim_references.py"]),
    ("document-observations", ["scripts/document_observations.py", "validate"]),
    ("research-checkpoints", ["scripts/research_checkpoints.py", "check"]),
    ("strict-json-schemas", ["scripts/validate_metadata_schemas.py", "examples"]),
    ("book-metadata", ["scripts/validate_book_metadata.py"]),
    ("book-navigation", ["scripts/validate_book_navigation.py"]),
)


def contract_versions(root):
    seen = {}
    for rel, (field, expected) in EXPECTED.items():
        data = json.loads((root / rel).read_text(encoding="utf-8"))
        value = data.get(field)
        if type(value) is not int or value != expected:
            raise ValueError(f"{rel}: incompatible {field}: expected {expected}")
        seen[rel] = value
    for rel in SCHEMAS:
        data = json.loads((root / rel).read_text(encoding="utf-8"))
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise ValueError(rel + ": unsupported JSON Schema dialect")
    return seen


def ordered_checks(root, mode):
    if mode not in {"available", "strict"}:
        raise ValueError("mode must be available or strict")
    checks = list(CORE)
    missing = []
    index = root / "generated/route-index.v1.json"
    if index.is_file():
        checks.append(("routing-index", ["scripts/route_index.py", "check"]))
    else:
        missing.append("routing-index-not-built")
    if mode == "strict" and missing:
        raise ValueError("strict knowledge validation unavailable: " + ", ".join(missing))
    return checks, missing


def run(root, mode):
    versions = contract_versions(root)
    checks, missing = ordered_checks(root, mode)
    statuses = []
    for label, argv in checks:
        executable = root / argv[0]
        if not executable.is_file():
            raise ValueError("required checker missing: " + argv[0])
        command = [sys.executable, str(executable), *argv[1:]]
        print("RUN", label, argv[0], *argv[1:], flush=True)
        result = subprocess.run(command, cwd=root, check=False)
        statuses.append({"name": label, "exit_code": result.returncode,
                         "status": "passed" if result.returncode == 0 else "failed"})
        if result.returncode != 0:
            break
    if any(x["status"] == "failed" for x in statuses):
        outcome = "failed"
    elif missing:
        outcome = "incomplete"
    else:
        outcome = "passed"
    return {"outcome": outcome, "mode": mode, "contract_versions": versions,
            "checks": statuses, "missing_gates": missing,
            "warning": "Structural validation is NOT independent semantic/source review."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=ROOT)
    p.add_argument("--mode", choices=("available", "strict"), default="available")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    root = args.root.resolve()
    result = run(root, args.mode)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("Knowledge validation outcome:", result["outcome"])
        for label in result["missing_gates"]:
            print("NOT IMPLEMENTED:", label)
    if result["outcome"] != "passed":
        # Strict pre-merge and milestone closure must not silently skip gates.
        # Available-mode 'incomplete' also exits nonzero to prevent false CI green.
        sys.exit(2 if result["outcome"] == "incomplete" else 1)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
