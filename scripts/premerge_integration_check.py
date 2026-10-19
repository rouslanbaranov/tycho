#!/usr/bin/env python3
"""Opt-in pinned local validation of the combined Tycho M1–M9 draft branch.

This runner does not alter the per-issue feature-branch convention or CI
trigger policy. It reuses existing repository validators at a fixed, clean Git
checkout. Passing the checks validates structures and known fixtures, NEVER
independent technical claims, source rights, complete publication acceptance,
or a live MCP 60-scenario evaluation.

Example:
  python3 scripts/premerge_integration_check.py \
    --branch integration/tycho-m1-m9-unified-manuscript-20261019 \
    --expected-head <the-current-40-character-commit-sha>
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
INTEGRATION_BRANCH = "integration/tycho-m1-m9-unified-manuscript-20261019"
SHA40 = re.compile(r"[0-9a-f]{40}\Z")


def validate_identity(branch: str, expected_head: str, actual_head: str) -> None:
    """Explicit integration allow-list, never a broad bypass of issue branches."""
    if branch != INTEGRATION_BRANCH:
        raise ValueError("Only the explicitly approved Tycho M1–M9 integration branch is valid")
    if not SHA40.fullmatch(expected_head):
        raise ValueError("Expected full lowercase 40-character Git commit SHA")
    if actual_head != expected_head:
        raise ValueError("Git checkout HEAD disagrees with pinned expected commit SHA")


def checked_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def commands(python: str = sys.executable) -> list[list[str]]:
    """Reuse existing validators, do not create new weaker versions."""
    return [
        [python, "scripts/check_boundary.py"],
        [python, "scripts/validate_sources.py"],
        [python, "scripts/source_catalog.py", "--check"],
        [python, "scripts/validate_claim_references.py"],
        [python, "scripts/validate_metadata_schemas.py", "examples"],
        [python, "scripts/validate_book_metadata.py"],
        [python, "scripts/validate_knowledge.py", "--mode", "strict", "--json"],
        [python, "scripts/validate_book_navigation.py"],
        [python, "scripts/validate_m9_cases.py"],
        [python, "scripts/validate_m9_cases.py", "--self-test"],
        [python, "-m", "unittest", "discover", "-s", "tests",
         "-p", "test_tycho*.py", "-v"],
        [python, "-m", "unittest", "discover", "-s", "tests",
         "-p", "test_m9*.py", "-v"],
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", required=True,
                        help="Exact approved M1–M9 integration branch name")
    parser.add_argument("--expected-head", required=True,
                        help="40-character pinned SHA; never use a moving branch ref")
    args = parser.parse_args()

    repo_root = checked_git("rev-parse", "--show-toplevel")
    if Path(repo_root).resolve() != ROOT:
        raise ValueError("Run in the Tycho checkout, not another repository")

    head = checked_git("rev-parse", "HEAD")
    validate_identity(args.branch, args.expected_head, head)

    # Detached pinned checkouts are permitted. For an attached checkout, verify
    # it is exactly the approved branch; never infer identity from a flag alone.
    status = subprocess.run(
        ["git", "symbolic-ref", "--quiet", "--short", "HEAD"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if status.returncode == 0 and status.stdout.strip() != args.branch:
        raise ValueError("Attached checkout is not on the declared integration branch")
    if status.returncode not in (0, 1):
        raise ValueError("Unable to inspect checkout branch safely")

    if checked_git("status", "--porcelain", "--untracked-files=all"):
        raise ValueError("Integration checkout must be clean before validation")

    print("PINNED:", head, "BRANCH:", args.branch, flush=True)
    print("SCOPE: structural validators and local tests; not source or MCP acceptance",
          flush=True)
    for command in commands():
        print("RUN:", " ".join(command), flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
    print("PASS: pinned M1–M9 local validation commands completed.")
    print("LIMIT: human review, source rights and live MCP scenarios remain separate.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, subprocess.CalledProcessError, OSError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
