#!/usr/bin/env python3
"""Validate saved external AI review reports against the index."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = Path("authoring/ai-reviews")
INDEX = ARCHIVE / "README.md"
CODE = re.compile(r"`([^`]+)`")
HEX = re.compile(r"^[0-9a-f]{64}$")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def parse_index(root):
    rows = []
    for line in (root / INDEX).read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] == "Date":
            continue
        report = CODE.search(cells[4])
        digest = CODE.search(cells[5])
        if report is None or digest is None:
            continue
        rows.append((report.group(1), digest.group(1), cells[3]))
    return rows


def validate(root=ROOT):
    root = Path(root).resolve()
    archive = root / ARCHIVE
    rows = parse_index(root)
    require(rows, "ai-reviews-index-empty")
    seen = set()
    for name, digest, verdict in rows:
        require(name not in seen, "ai-reviews-duplicate: " + name)
        seen.add(name)
        require(HEX.fullmatch(digest) is not None,
                "ai-reviews-hash-format: " + name)
        path = archive / name
        require(path.is_file() and not path.is_symlink(),
                "ai-reviews-report-missing: " + name)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "ai-reviews-hash-mismatch: " + name)
        require(verdict in ("pass", "reject", "pass-with-findings"),
                "ai-reviews-verdict: " + name)
    reports = {path.name for path in archive.iterdir()
               if path.is_file() and path.suffix in (".md", ".json")
               and path.name not in ("README.md", "REGRESSIONS.md")}
    require(reports == seen, "ai-reviews-unindexed")
    return {"reports": len(rows)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        return 1
    print("PASS: AI review index", result["reports"], "reports")
    return 0


if __name__ == "__main__":
    sys.exit(main())
