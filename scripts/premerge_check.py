#!/usr/bin/env python3
"""Run Tycho pre-merge validation locally without invoking GitHub Actions.

All commands run from the repository root and exit on first failure.
Supply exact issue branch and GitHub issue title. Does not claim source
truth, independent review, deployed-service behavior or milestone acceptance.
"""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", required=True, help="Issue-specific feature branch")
    parser.add_argument("--issue-title", required=True, help="Exact GitHub issue title")
    args = parser.parse_args()
    commands = [
        [sys.executable, "scripts/check_feature_branch.py",
         "--branch", args.branch, "--issue-title", args.issue_title],
        [sys.executable, "scripts/check_boundary.py"],
        [sys.executable, "scripts/validate_sources.py"],
        [sys.executable, "scripts/source_catalog.py", "--check"],
        [sys.executable, "scripts/validate_pattern_registry.py"],
        [sys.executable, "scripts/validate_pattern_atlas.py"],
        [sys.executable, "scripts/validate_pattern_coverage.py"],
        [sys.executable, "scripts/pattern_census.py", "--check"],
        [sys.executable, "-m", "unittest", "discover", "-s", "tests",
         "-p", "test_tycho*.py", "-v"],
    ]
    if (ROOT / 'edition/directory-migration.json').is_file():
        commands.insert(-1, [sys.executable, 'scripts/validate_directory_migration.py'])
    for command in commands:
        print("RUN:", " ".join(command), flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
    print("Local pre-merge checks passed; milestone acceptance remains separate.")


if __name__ == "__main__":
    main()
