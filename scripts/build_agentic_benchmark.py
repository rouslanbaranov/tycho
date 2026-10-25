#!/usr/bin/env python3
"""Build the frozen agentic benchmark from the author-labelled corpus qrels.

The benchmark reuses existing questions and accepted paths; it does not edit
the book or generate new labels. Selection is deterministic and stratified by
the existing corpus categories.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evaluation/corpus-qrels.v2.json"
OUTPUT = ROOT / "evaluation/agentic-qrels.v1.json"

COUNTS = {
    "fact": 10,
    "failure": 5,
    "tradeoff": 5,
    "synthesis": 5,
    "change_impact": 4,
    "contradiction": 3,
    "unanswerable": 8,
}


def select(source):
    selected = []
    for category, count in COUNTS.items():
        items = [
            item for item in source["items"]
            if item.get("category") == category
        ]
        items.sort(key=lambda item: item["id"])
        if category == "unanswerable":
            items = [item for item in items if not item.get("accepted")]
        else:
            items = [item for item in items if item.get("accepted")]
        if len(items) < count:
            raise SystemExit(
                "Not enough items for " + category + ": " + str(len(items)))
        for item in items[:count]:
            selected.append({
                "id": "A" + item["id"],
                "source_id": item["id"],
                "category": category,
                "split": item.get("split"),
                "question": item["question"],
                "accepted": [
                    {
                        "path": entry["path"],
                        "section_id": entry.get("section_id"),
                        "document_id": entry.get("document_id"),
                    }
                    for entry in item.get("accepted", [])
                ],
            })
    return selected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    raw = args.source.read_bytes()
    source = json.loads(raw)
    items = select(source)
    payload = {
        "schema_version": 1,
        "dataset": "agentic-retrieval-v1",
        "created": "2026-10-25",
        "label_status": source.get("status", "unknown"),
        "source": {
            "path": str(args.source.relative_to(ROOT)),
            "sha256": hashlib.sha256(raw).hexdigest(),
        },
        "selection": {
            "method": "first N per existing category, sorted by source ID",
            "counts": COUNTS,
            "total": len(items),
        },
        "items": items,
    }
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(args.output),
        "total": len(items),
        "counts": COUNTS,
        "source_sha256": payload["source"]["sha256"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
