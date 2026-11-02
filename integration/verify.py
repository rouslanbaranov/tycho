#!/usr/bin/env python3
"""Verify a local Tycho integration without a harness."""
import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_TOOLS = 11


def emit(ok, name, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (": " + detail if detail else ""))
    return ok


def run(cmd, cwd):
    return subprocess.run(
        [str(part) for part in cmd], cwd=str(cwd), capture_output=True,
        text=True, timeout=600)


def check_python():
    version = sys.version_info
    text = "%d.%d.%d" % (version[0], version[1], version[2])
    return emit(version >= (3, 15), "python", text)


def check_dependencies():
    try:
        import jsonschema  # noqa: F401
        import yaml  # noqa: F401
    except Exception as exc:
        return emit(False, "dependencies", str(exc))
    return emit(True, "dependencies", "yaml, jsonschema")


def check_book(root):
    pages = sorted((root / "book").rglob("*.md"))
    return emit(bool(pages), "book", "%d pages" % len(pages))


def check_index(root):
    database = root / "generated" / "sections-fts-v5.sqlite"
    if not database.is_file():
        return emit(False, "index", "missing generated/sections-fts-v5.sqlite")
    script = root / "scripts" / "section_fts_index.py"
    proc = run([sys.executable, script, "check", "--root", root], root)
    if proc.returncode != 0:
        return emit(False, "index", (proc.stdout + proc.stderr).strip()[-300:])
    try:
        data = json.loads(proc.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return emit(False, "index", "unreadable check output")
    ok = data.get("outcome") == "verified"
    detail = "documents=%s sections=%s snapshot=%s" % (
        data.get("documents"), data.get("sections"), data.get("snapshot"))
    return emit(ok, "index", detail)


def stdio_surface(root):
    server = root / "mcp" / "mcp_server.py"
    proc = subprocess.Popen(
        [sys.executable, str(server), "--root", str(root)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True)
    try:
        def rpc(message):
            proc.stdin.write(json.dumps(message) + "\n")
            proc.stdin.flush()
            return json.loads(proc.stdout.readline())

        rpc({"jsonrpc": "2.0", "id": 1, "method": "initialize",
             "params": {"protocolVersion": "2025-11-25", "capabilities": {},
                        "clientInfo": {"name": "verify", "version": "0"}}})
        listing = rpc({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        return listing["result"]["tools"]
    finally:
        try:
            proc.stdin.close()
            proc.wait(timeout=10)
        except Exception:
            proc.kill()


def check_stdio(root):
    try:
        tools = stdio_surface(root)
    except Exception as exc:
        return emit(False, "stdio", str(exc)[:200])
    names = [tool.get("name") for tool in tools]
    ok = len(names) == EXPECTED_TOOLS and all(
        name and name.startswith("tycho_") for name in names)
    return emit(ok, "stdio", "%d tools" % len(names))


def http_get(base, path, token=None, timeout=5):
    request = urllib.request.Request(base.rstrip("/") + path)
    if token:
        request.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def check_http(base):
    try:
        health = http_get(base, "/health")
        ready = http_get(base, "/ready")
    except (urllib.error.URLError, OSError, ValueError) as exc:
        return emit(False, "http", str(exc)[:200])
    ok = health.get("status") == "ok" and ready.get("status") == "ok"
    detail = "snapshot=%s documents=%s" % (
        ready.get("snapshot"), ready.get("documents"))
    return emit(ok, "http", detail)


def check_project(project):
    results = []
    config = project / ".mcp.json"
    if config.is_file():
        try:
            data = json.loads(config.read_text(encoding="utf-8"))
        except ValueError as exc:
            results.append(emit(False, "project", ".mcp.json: " + str(exc)))
        else:
            has = "tycho" in (data.get("mcpServers") or {})
            results.append(emit(has, "project", ".mcp.json tycho entry"))
    else:
        results.append(emit(False, "project", ".mcp.json missing"))
    vscode = project / ".vscode" / "mcp.json"
    if vscode.is_file():
        try:
            data = json.loads(vscode.read_text(encoding="utf-8"))
        except ValueError as exc:
            results.append(emit(False, "project", ".vscode/mcp.json: " + str(exc)))
        else:
            has = "tycho" in (data.get("servers") or {})
            results.append(emit(has, "project", ".vscode/mcp.json tycho entry"))
    else:
        results.append(emit(False, "project", ".vscode/mcp.json missing"))
    agents = sorted((project / ".github" / "agents").glob("*.agent.md"))
    results.append(emit(bool(agents), "project", "%d agent files" % len(agents)))
    return all(results)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT,
                        help="Tycho checkout, default: the parent directory")
    parser.add_argument("--http-base", default=None,
                        help="Base URL of a running HTTP server")
    parser.add_argument("--token-env", default="TYCHO_MCP_TOKEN",
                        help="Environment variable with the bearer token")
    parser.add_argument("--project", type=Path, default=None,
                        help="Target project to check for MCP configuration")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    results = [check_python(), check_dependencies(), check_book(root),
               check_index(root), check_stdio(root)]
    if args.http_base:
        results.append(check_http(args.http_base))
    if args.project:
        results.append(check_project(args.project.resolve()))
    passed = sum(1 for item in results if item)
    print("SUMMARY %d/%d checks passed" % (passed, len(results)))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

