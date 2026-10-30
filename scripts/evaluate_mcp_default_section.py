#!/usr/bin/env python3
"""Evaluate the actual MCP default handler on section-qrels v3."""
import argparse
import json
from pathlib import Path

import mcp_server

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    qrels = json.loads((args.root / "evaluation/section-qrels.v3.json")
                       .read_text(encoding="utf-8"))
    server = mcp_server.TychoMcpServer(args.root)
    counts = {"all": {"n": 0, "base": [0, 0, 0], "default": [0, 0, 0]}}
    for item in qrels["items"]:
        accepted = set(item["accepted"])
        base = server._tool_search({
            "query": item["question"], "abstain": False,
            "section_rerank": False,
        })
        default = server._tool_search({
            "query": item["question"], "abstain": False,
        })
        base_keys = [row["section_key"] for row in base.get("results", [])]
        default_keys = [row["section_key"]
                        for row in default.get("results", [])]
        for split in (item["split"], "all"):
            bucket = counts.setdefault(split, {
                "n": 0, "base": [0, 0, 0], "default": [0, 0, 0]})
            bucket["n"] += 1
            for index, k in enumerate((1, 3, 5)):
                bucket["base"][index] += int(
                    bool(set(base_keys[:k]) & accepted))
                bucket["default"][index] += int(
                    bool(set(default_keys[:k]) & accepted))
    output = {"qrels": "evaluation/section-qrels.v3.json", "splits": {}}
    for split, bucket in counts.items():
        n = bucket["n"]
        output["splits"][split] = {
            "n": n,
            "base": [round(v / n, 3) for v in bucket["base"]],
            "default": [round(v / n, 3) for v in bucket["default"]],
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
