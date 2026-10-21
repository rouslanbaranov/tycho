#!/usr/bin/env python3
"""Build or check the canonical page census.

Counts and hashes are inventory evidence, not page quality or technical review.
"""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assemble_edition import split

TICK = chr(96)
CENSUS = Path("edition/patterns/page-census.v1.json")
ROUTE = Path("generated/route-index.v1.json")
HEAD = re.compile(r"^#{2,4}\s")
MERMAID = re.compile(r"^\s*" + TICK * 3 + r"mermaid\s*$")
URL = re.compile(r"https?://")


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def locate(path):
    parts = path.split("/")
    if "volumes" not in parts:
        return None, None
    index = parts.index("volumes")
    if index + 1 >= len(parts):
        return None, None
    volume = parts[index + 1]
    chapter = parts[index + 2] if len(parts) > index + 2 else None
    return volume, chapter


def build(root=ROOT):
    root = Path(root).resolve()
    route = load(root / ROUTE)
    documents = []
    for doc in route["documents"]:
        text = (root / doc["path"]).read_text(encoding="utf-8")
        _, body = split(text)
        volume, chapter = locate(doc["path"])
        documents.append({
            "id": doc["id"],
            "kind": doc["kind"],
            "path": doc["path"],
            "parent_id": doc["parent_id"],
            "title": doc["title"],
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "word_count": len(body.split()),
            "heading_count": sum(1 for line in body.splitlines() if HEAD.match(line)),
            "mermaid_count": sum(1 for line in body.splitlines() if MERMAID.match(line)),
            "http_link_count": len(URL.findall(body)),
            "volume": volume,
            "chapter": chapter,
        })
    documents.sort(key=lambda item: item["path"])
    return {
        "schema_version": 1,
        "route_index_snapshot": route["snapshot_sha256"],
        "document_count": len(documents),
        "counts": {
            "by_kind": dict(sorted(Counter(item["kind"] for item in documents).items())),
            "by_volume": dict(sorted(Counter(item["volume"] for item in documents
                                            if item["volume"]).items())),
        },
        "documents": documents,
        "scope": "canonical membership, size and hash inventory; not quality or truth",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        result = build(root)
        if not (args.write or args.check):
            args.json = True
        if args.write:
            (root / CENSUS).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if args.check:
            if not (root / CENSUS).is_file():
                raise ValueError("census-missing")
            if load(root / CENSUS) != result:
                raise ValueError("census-stale")
        if args.json:
            print(json.dumps({"documents": result["document_count"], "counts": result["counts"]}, indent=2))
        else:
            print("Census", result["document_count"], "documents")
    except (ValueError, OSError, KeyError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
