#!/usr/bin/env python3
"""End-to-end stdio smoke for the MCP server."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def line(payload):
    return json.dumps(payload, separators=(",", ":")) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    requests = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2025-11-25", "capabilities": {},
                    "clientInfo": {"name": "smoke", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
         "params": {"name": "tycho_search", "arguments": {
             "query": "nested text"}}},
        {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
         "params": {"name": "tycho_search", "arguments": {
             "query": "nested text", "section_rerank": True,
             "section_rerank_margin": 0.05}}},
        {"jsonrpc": "2.0", "id": 5, "method": "tools/call",
         "params": {"name": "tycho_search", "arguments": {
             "query": "V12 replay", "volume": "v12"}}},
        {"jsonrpc": "2.0", "id": 6, "method": "tools/call",
         "params": {"name": "tycho_search", "arguments": {
             "query": "nested text", "section_rerank": True,
             "section_rerank_margin": 1.0}}},
        {"jsonrpc": "2.0", "id": 7, "method": "tools/call",
         "params": {"name": "tycho_search", "arguments": {
             "query": "service discovery", "volume": "v11"}}},
        {"jsonrpc": "2.0", "id": 8, "method": "tools/call",
         "params": {"name": "tycho_search", "arguments": {
             "query": "stock-flow offered work",
             "include_artifacts": True}}},
    ]
    proc = subprocess.Popen(
        [sys.executable, "scripts/mcp_server.py"], cwd=args.root,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True)
    payload = "".join(line(request) for request in requests)
    stdout, stderr = proc.communicate(payload, timeout=60)
    responses = {}
    for raw in stdout.splitlines():
        message = json.loads(raw)
        if "id" in message:
            responses[message["id"]] = message
    tools = responses.get(2, {}).get("result", {}).get("tools", [])
    output = {"tools": len(tools), "calls": {}}
    for request_id in (3, 4, 5, 6, 7, 8):
        message = responses.get(request_id, {})
        result = message.get("result", {})
        content = result.get("structuredContent", {})
        output["calls"][str(request_id)] = {
            "isError": result.get("isError"),
            "result_scope": content.get("result_scope"),
            "score_kind": (content.get("results") or [{}])[0].get("score_kind"),
            "status": content.get("status"),
            "artifacts": len(content.get("artifacts") or []),
        }
    output["stderr_tail"] = stderr.strip().splitlines()[-2:]
    print(json.dumps(output, indent=2))
    return 1 if proc.returncode else 0


if __name__ == "__main__":
    raise SystemExit(main())
