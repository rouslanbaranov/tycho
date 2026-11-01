#!/usr/bin/env python3
"""Small read-only MCP-like CLI for a drill-down agent session."""
import argparse, json, os, time
from pathlib import Path
import mcp_server

ROOT = Path(__file__).resolve().parents[1]

def log(path, record):
    if not path:
        return
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=("search", "read", "page", "outline", "describe"))
    ap.add_argument("value", nargs="?")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--max-chars", type=int, default=4500)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--log", default=os.environ.get("TYCHO_SESSION_LOG"))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if args.command != "describe" and not args.value:
        ap.error(args.command + " requires a value")
    if not 1 <= args.max_chars <= 6000:
        ap.error("--max-chars must be in 1..6000")
    if args.command == "outline" and not 1 <= args.limit <= 5:
        ap.error("outline --limit must be in 1..5")
    server = mcp_server.TychoMcpServer(root=ROOT)
    t0 = time.perf_counter()
    try:
        if args.command == "search":
            payload = server._tool_search({
                "query": args.value, "limit": args.limit, "abstain": False,
                "detail": "snippets", "max_chars": args.max_chars})
        elif args.command == "read":
            payload = server._tool_read({"section_key": args.value,
                                         "budget_chars": args.max_chars,
                                         "offset": args.offset})
        elif args.command == "page":
            payload = server._tool_page({"path": args.value,
                                         "budget_chars": args.max_chars,
                                         "offset": args.offset})
        elif args.command == "describe":
            payload = server._tool_describe({})
        else:
            payload = server._tool_outline({"topic": args.value,
                                            "limit": args.limit})
    except Exception as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}))
        log(args.log, {"command": args.command, "value": args.value,
                       "ok": False, "error": str(exc),
                       "latency_ms": round((time.perf_counter()-t0)*1000, 2)})
        return 1
    text = payload.get("structuredContent", payload)
    log(args.log, {"command": args.command, "value": args.value,
                   "ok": True, "returned": len(text.get("results", [])),
                   "status": text.get("status"),
                   "latency_ms": round((time.perf_counter()-t0)*1000, 2)})
    if args.json or True:
        limit = 200000 if args.command == "describe" else 20000
        print(json.dumps(text, indent=1)[:limit])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
