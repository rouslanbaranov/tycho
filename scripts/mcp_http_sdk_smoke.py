#!/usr/bin/env python3
"""Optional official MCP SDK client smoke over the local HTTP container.

Requires Python 3.11+ and the official mcp SDK (tested with mcp==2.3.0). The
standard-library client smoke remains the default; this script verifies that
an official SDK client can negotiate modern 2026-07-28 over authenticated
Streamable HTTP.
"""
import argparse
import asyncio
import contextlib
import json
import os
import sys


DEFAULT_HOST = "127.0.0.1"
DEFAULT_URL = "http://" + DEFAULT_HOST + ":8000"


def authed_transport(url, token):
    import httpx2
    from mcp.client.streamable_http import streamable_http_client

    @contextlib.asynccontextmanager
    async def transport():
        headers = {"Authorization": "Bearer " + token}
        async with httpx2.AsyncClient(headers=headers) as http_client:
            async with streamable_http_client(
                    url, http_client=http_client) as streams:
                yield streams

    return transport()


async def run(args):
    from mcp import Client

    token = args.token or os.environ.get(args.token_env)
    if not token:
        raise SystemExit("Missing token: set " + args.token_env)
    url = args.url.rstrip("/") + "/mcp"
    async with Client(authed_transport(url, token)) as client:
        tools = await client.list_tools()
        result = await client.call_tool(
            "tycho_search", {"query": args.query, "limit": 2})
        structured = result.structured_content or {}
        return {
            "protocol_version": client.protocol_version,
            "server": {
                "name": client.server_info.name,
                "version": client.server_info.version,
            },
            "tools": [tool.name for tool in tools.tools],
            "search": {
                "is_error": result.is_error,
                "status": structured.get("status"),
                "returned": structured.get("returned"),
                "citation": (
                    structured.get("results") or [{}]
                )[0].get("citation"),
            },
        }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--token-env", default="TYCHO_MCP_TOKEN")
    parser.add_argument("--token")
    parser.add_argument("--query", default="retry budget")
    args = parser.parse_args(argv)
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
