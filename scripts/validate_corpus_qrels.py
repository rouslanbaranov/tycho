#!/usr/bin/env python3
"""Validate corpus-level relevance judgments against schema and route metadata.

Structural validation only. It does not prove that a label is correct, that the
questions are independent, or that an evaluation result generalizes.
"""
import argparse
import json
from pathlib import Path
import sys
from route_index import legacy_scope

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QRELS = ROOT / "evaluation/corpus-qrels.v2.json"
DEFAULT_ROUTE = ROOT / "generated/route-index.v1.json"
DEFAULT_SCHEMA = ROOT / "schemas/corpus-qrels.v1.schema.json"
KINDS = {"book", "volume", "chapter", "page", "landing", "decision"}


def require(value, message):
    if not value:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate(qrels, route, schema, require_snapshot=True):
    if "unannotated_paths" in route and "coverage" in route:
        route = legacy_scope(route)
    from jsonschema import Draft202012Validator, FormatChecker

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(qrels), key=lambda item: list(item.path))
    if errors:
        first = errors[0]
        where = "/".join(str(part) for part in first.path) or "<root>"
        raise ValueError("schema violation at " + where + ": " + first.message)

    snapshot = qrels["snapshot"]
    if require_snapshot:
        require(snapshot["route_index_snapshot"] == route["snapshot_sha256"],
                "qrels snapshot does not match the routed book; revalidate labels")
    require(snapshot["document_count"] == len(route["documents"]),
            "qrels document_count does not match the route index")

    docs = {doc["id"]: doc for doc in route["documents"]}
    paths = {doc["path"]: doc for doc in route["documents"]}
    seen_ids = set()
    accepted_count = 0
    for item in qrels["items"]:
        require(item["id"] not in seen_ids, "duplicate item id " + item["id"])
        seen_ids.add(item["id"])
        if item["category"] != "unanswerable":
            require(item["accepted"], item["id"] + ": answerable item has no accepted page")
        else:
            require(not item["accepted"], item["id"] + ": unanswerable item has accepted pages")
        seen_answers = set()
        for answer in item["accepted"]:
            doc = docs.get(answer["document_id"])
            require(doc is not None, item["id"] + ": unknown document id")
            require(doc["kind"] in KINDS, item["id"] + ": unsupported document kind")
            require(doc["path"] == answer["path"],
                    item["id"] + ": document id and path disagree")
            require(paths[answer["path"]]["id"] == answer["document_id"],
                    item["id"] + ": path is not the documented page")
            key = (answer["document_id"], answer["section_id"])
            require(key not in seen_answers, item["id"] + ": duplicate accepted answer")
            seen_answers.add(key)
            accepted_count += 1

    if qrels["status"] != "bootstrap-author-labelled":
        require(len(qrels["items"]) >= qrels["target_item_count"],
                "non-bootstrap qrels must reach target_item_count")

    dev = sum(1 for item in qrels["items"] if item["split"] == "dev")
    heldout = len(qrels["items"]) - dev
    categories = {}
    for item in qrels["items"]:
        categories[item["category"]] = categories.get(item["category"], 0) + 1
    return {
        "status": "ok",
        "items": len(qrels["items"]),
        "dev": dev,
        "heldout": heldout,
        "accepted_answers": accepted_count,
        "target_item_count": qrels["target_item_count"],
        "bootstrap": qrels["status"].startswith("bootstrap"),
        "categories": dict(sorted(categories.items())),
        "snapshot": snapshot["route_index_snapshot"],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--qrels", type=Path, default=DEFAULT_QRELS)
    ap.add_argument("--route-index", type=Path, default=DEFAULT_ROUTE)
    ap.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = ap.parse_args()
    try:
        result = validate(load(args.qrels), load(args.route_index), load(args.schema))
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
