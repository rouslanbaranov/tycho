#!/usr/bin/env python3
"""HTTP client smoke for the local Tycho MCP container.

The client uses only the standard library so it can run from the host without
installing the MCP SDK. It exercises modern discovery, tools/list, tools/call,
the search API and a raw book page over one bearer-authenticated HTTP session.
It is a transport smoke, not an agent-quality evaluation or an SDK conformance
test.
"""
import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

MODERN = "2026-07-28"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_URL = "http://" + DEFAULT_HOST + ":8000"
META = {
    "io.modelcontextprotocol/protocolVersion": MODERN,
    "io.modelcontextprotocol/clientCapabilities": {},
}


def call(url, token, method, payload=None, headers=None, expect_json=True):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request_headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    if headers:
        request_headers.update(headers)
    request = Request(url, data=data, headers=request_headers, method=method)
    try:
        with urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
            if not expect_json:
                return response.status, body
            return response.status, json.loads(body) if body else None
    except HTTPError as exc:
        body = exc.read().decode("utf-8")
        if not expect_json:
            return exc.code, body
        return exc.code, json.loads(body) if body else None
    except URLError as exc:
        raise SystemExit("Cannot reach " + url + ": " + str(exc)) from exc


def mcp(url, token, request_id, method, params):
    payload = {"jsonrpc": "2.0", "id": request_id, "method": method,
               "params": params}
    headers = {
        "MCP-Protocol-Version": MODERN,
        "Mcp-Method": method,
    }
    if method == "tools/call":
        headers["Mcp-Name"] = params["name"]
    status, response = call(url, token, "POST", payload, headers)
    if status != 200 or not isinstance(response, dict):
        raise SystemExit(
            "MCP " + method + " failed with HTTP " + str(status) +
            ": " + json.dumps(response)[:500])
    if "error" in response:
        raise SystemExit(
            "MCP " + method + " returned " + json.dumps(response["error"]))
    return response["result"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--token-env", default="TYCHO_MCP_TOKEN")
    parser.add_argument("--token")
    parser.add_argument("--query", default="idempotent consumer duplicate")
    parser.add_argument("--book-path", default="README.md")
    args = parser.parse_args(argv)
    token = args.token or os.environ.get(args.token_env)
    if not token:
        print("Missing token: set " + args.token_env, file=sys.stderr)
        return 2
    base = args.url.rstrip("/")
    mcp_url = base + "/mcp"
    summary = {}
    discovered = mcp(mcp_url, token, 1, "server/discover", {"_meta": META})
    summary["protocol"] = discovered.get("supportedVersions")
    tools = mcp(mcp_url, token, 2, "tools/list", {"_meta": META})
    summary["tools"] = [item["name"] for item in tools.get("tools", [])]
    search = mcp(mcp_url, token, 3, "tools/call", {
        "_meta": META,
        "name": "tycho_search",
        "arguments": {"query": args.query, "limit": 2},
    })
    structured = search.get("structuredContent") or {}
    summary["tool_search"] = {
        "is_error": search.get("isError"),
        "status": structured.get("status"),
        "returned": structured.get("returned"),
        "snapshot": structured.get("snapshot"),
    }
    status, payload = call(
        base + "/search?q=" + quote(args.query) + "&limit=2", token, "GET")
    summary["search_api"] = {
        "http": status,
        "status": payload.get("status") if isinstance(payload, dict) else None,
        "returned": payload.get("returned") if isinstance(payload, dict) else None,
    }
    book_url = base + "/book/" + quote(args.book_path)
    status, text = call(book_url, token, "GET", expect_json=False)
    summary["book"] = {
        "http": status,
        "bytes": len(text) if isinstance(text, str) else None,
    }
    status, health = call(base + "/health", token, "GET")
    summary["health"] = {"http": status, "status": health.get("status")}
    if summary["tool_search"]["is_error"]:
        print("MCP search returned isError=true", file=sys.stderr)
        return 1
    if summary["tool_search"]["status"] not in (
            "ok", "no-results", "no-confident-answer"):
        print("Unexpected search status", file=sys.stderr)
        return 1
    if summary["search_api"]["http"] != 200:
        print("Search API failed", file=sys.stderr)
        return 1
    if summary["book"]["http"] != 200:
        print("Book read failed", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
