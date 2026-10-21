#!/usr/bin/env python3
"""Check V11 prose line length, allowing only exact owner-link exceptions."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "**Technical owner.**"


def check_text(text, origin="<text>"):
    violations = []
    exceptions = 0
    for number, line in enumerate(text.splitlines(), 1):
        if len(line) <= 100:
            continue
        if line.startswith(MARKER) and line.count("](") == 1:
            exceptions += 1
            continue
        violations.append((origin, number, len(line)))
    return violations, exceptions


def check_tree(root=ROOT):
    root = Path(root).resolve()
    directory = root / "book/volumes/v11-pattern-atlas"
    violations = []
    exceptions = 0
    for path in sorted(directory.rglob("*.md")):
        found, count = check_text(path.read_text(encoding="utf-8"), str(path.relative_to(root)))
        violations.extend(found)
        exceptions += count
    return violations, exceptions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    violations, exceptions = check_tree(args.root)
    if violations:
        for origin, number, length in violations[:20]:
            print(f"FAIL: markdown-line-length: {origin}:{number}: {length}", file=sys.stderr)
        return 1
    print(f"PASS: V11 prose <=100; {exceptions} exact owner-link exceptions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
