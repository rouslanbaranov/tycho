#!/usr/bin/env python3
"""Optional official MCP SDK client smoke for the local Tycho stdio server.

This file is not part of the stdlib-only test suite. It requires Python 3.11+
and the official SDK, tested here with mcp==2.3.0. It starts the local server
over stdio, runs a bounded modern or legacy roundtrip and prints a JSON summary.

Example (SDK environment separate from the server environment):
  python3.15 mcp/tests/smoke/mcp_sdk_smoke.py --server-python .venv/bin/python
"""
import argparse
import asyncio
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--server-python", default=str(ROOT / ".venv/bin/python"))
    parser.add_argument(
        "--mode", choices=("auto", "legacy"), default="auto",
        help="SDK connection mode; auto negotiates the current revision")
    return parser.parse_args(argv)


async def run(args):
    from mcp import Client, StdioServerParameters

    root = args.root.resolve()
    params = StdioServerParameters(
        command=args.server_python,
        args=[str(root / "mcp/mcp_server.py"), "--root", str(root)],
        cwd=str(root),
    )
    async with Client(params, mode=args.mode) as client:
        tools = await client.list_tools()
        search = await client.call_tool(
            "tycho_search",
            {"query": "idempotent consumer duplicate", "limit": 2},
        )
        page = await client.call_tool(
            "tycho_page", {"path": "book/README.md", "budget_chars": 80})
        patterns = await client.call_tool(
            "tycho_patterns", {"limit": 2})
        pattern = None
        pattern_list = patterns.structured_content.get("patterns") or []
        if pattern_list:
            result = await client.call_tool(
                "tycho_pattern",
                {"pattern_id": pattern_list[0]["pattern_id"]},
            )
            pattern = {
                "pattern_id": result.structured_content["pattern"]["id"],
                "catalog_name": result.structured_content["pattern"][
                    "catalog_name"],
                "citation": result.structured_content["citation"],
            }
        search_result = search.structured_content
        return {
            "mode": args.mode,
            "protocol_version": client.protocol_version,
            "server": {
                "name": client.server_info.name,
                "version": client.server_info.version,
            },
            "tools": [tool.name for tool in tools.tools],
            "search": {
                "is_error": search.is_error,
                "status": search_result.get("status"),
                "returned": search_result.get("returned"),
                "citation": (
                    search_result.get("results") or [{}]
                )[0].get("citation"),
            },
            "page": {
                "is_error": page.is_error,
                "status": page.structured_content.get("status"),
                "returned_chars": page.structured_content.get(
                    "returned_chars"),
            },
            "patterns": {
                "is_error": patterns.is_error,
                "status": patterns.structured_content.get("status"),
                "total": patterns.structured_content.get("total"),
                "returned": patterns.structured_content.get("returned"),
            },
            "pattern": pattern,
        }


def main(argv=None):
    args = parse_args(argv)
    try:
        summary = asyncio.run(run(args))
    except ImportError as exc:
        print(
            "Official MCP SDK is not installed in this interpreter: " + str(exc),
            file=sys.stderr,
        )
        return 2
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
