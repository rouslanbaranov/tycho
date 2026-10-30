#!/usr/bin/env python3
"""Production healthcheck for Tycho search."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mcp_server
import section_fts_index
import section_search

EXPECTED_WEIGHTS = (5.0, 2.0, 0.5)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    errors = []
    stats = section_fts_index.stats(args.root)
    snapshot = stats["snapshot"]
    qrels_paths = (
        args.root / "evaluation/corpus-qrels.v4.json",
        args.root / "evaluation/section-qrels.v4.json",
    )
    qrels = {}
    for path in qrels_paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        qrels[path.name] = {
            "status": data.get("status"),
            "count": len(data.get("items", [])),
            "snapshot_match": data.get("snapshot") == snapshot,
        }
        if data.get("status") != "ai-adjudicated-not-human":
            errors.append(path.name + ": unexpected status")
        if len(data.get("items", [])) != 150:
            errors.append(path.name + ": expected 150 queries")
        if data.get("snapshot") != snapshot:
            errors.append(path.name + ": stale snapshot")
    artifact_path = args.root / "evaluation/v12-artifact-qrels.v1.json"
    artifact = {"exists": artifact_path.is_file()}
    if not artifact_path.is_file():
        errors.append("artifact qrels missing")
    else:
        data = json.loads(artifact_path.read_text(encoding="utf-8"))
        artifact.update({
            "status": data.get("status"),
            "count": len(data.get("items", [])),
            "snapshot_match": data.get("snapshot") == snapshot,
        })
        if data.get("status") != "ai-adjudicated-not-human":
            errors.append("artifact qrels: unexpected status")
        if len(data.get("items", [])) != 30:
            errors.append("artifact qrels: expected 30 queries")
        if data.get("snapshot") != snapshot:
            errors.append("artifact qrels: stale snapshot")
    weights = section_search.bm25_weights()
    if weights != EXPECTED_WEIGHTS:
        errors.append("unexpected BM25 weights: " + repr(weights))
    schema = mcp_server.search_schema()["properties"]
    if schema["section_rerank"]["default"] is not False:
        errors.append("MCP section_rerank default is not false")
    if schema["section_rerank_margin"]["default"] != 0.05:
        errors.append("MCP margin default is not .05")
    output = {
        "index_snapshot": snapshot,
        "qrels": qrels,
        "artifact_qrels": artifact,
        "weights": weights,
        "mcp_defaults": {
            "section_rerank": schema["section_rerank"]["default"],
            "margin": schema["section_rerank_margin"]["default"],
        },
        "status": "ok" if not errors else "fail",
        "errors": errors,
    }
    print(json.dumps(output, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
