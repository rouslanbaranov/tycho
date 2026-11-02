#!/usr/bin/env python3
"""Start, stop and inspect the local Tycho HTTP MCP server."""
import argparse
import json
import os
import secrets
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765


def paths(root, token_file=None):
    return {
        "pid": root / ".tycho-mcp-http.pid",
        "log": root / ".tycho-mcp-http.log",
        "token": Path(token_file) if token_file else root / ".tycho-mcp-token",
    }


def read_pid(path):
    try:
        return int(path.read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return None


def running(pid):
    if not pid:
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def read_json(url, timeout=2):
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def base_url(host, port):
    return "http://" + host + ":" + str(port)


def health(host, port):
    try:
        return read_json(base_url(host, port) + "/health")
    except (urllib.error.URLError, OSError, ValueError):
        return None


def ready(host, port):
    try:
        return read_json(base_url(host, port) + "/ready")
    except (urllib.error.URLError, OSError, ValueError):
        return None


def resolve_token(token_file):
    value = os.environ.get("TYCHO_MCP_TOKEN")
    if value:
        return value, "environment"
    if token_file.is_file():
        return token_file.read_text(encoding="utf-8").strip(), "file"
    token = secrets.token_urlsafe(32)
    token_file.write_text(token, encoding="utf-8")
    token_file.chmod(0o600)
    return token, "generated"


def wait_for_health(host, port, timeout):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if health(host, port) is not None:
            return True
        time.sleep(0.25)
    return False


def start(root, host, port, token_file, timeout):
    runtime = paths(root, token_file)
    pid = read_pid(runtime["pid"])
    if running(pid):
        print(json.dumps({"status": "already-running", "pid": pid}, sort_keys=True))
        return 0
    if health(host, port) is not None:
        print(json.dumps({"status": "port-in-use", "port": port}, sort_keys=True))
        return 1
    token, source = resolve_token(runtime["token"])
    environment = dict(os.environ)
    environment["TYCHO_MCP_TOKEN"] = token
    command = [sys.executable, str(root / "mcp" / "mcp_http_server.py"),
               "--root", str(root), "--host", host, "--port", str(port)]
    handle = runtime["log"].open("ab")
    try:
        process = subprocess.Popen(
            command, stdout=handle, stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL, env=environment, start_new_session=True)
    finally:
        handle.close()
    runtime["pid"].write_text(str(process.pid), encoding="utf-8")
    if not wait_for_health(host, port, timeout):
        process.terminate()
        print(json.dumps({"status": "failed", "pid": process.pid,
                          "log": str(runtime["log"])}, sort_keys=True))
        return 1
    snapshot = (ready(host, port) or {}).get("snapshot")
    print(json.dumps({"status": "running", "pid": process.pid, "port": port,
                      "url": base_url(host, port) + "/mcp",
                      "log": str(runtime["log"]),
                      "token_file": str(runtime["token"]),
                      "token_source": source, "snapshot": snapshot},
                     sort_keys=True))
    return 0


def stop(root, token_file):
    runtime = paths(root, token_file)
    pid = read_pid(runtime["pid"])
    if not running(pid):
        runtime["pid"].unlink(missing_ok=True)
        print(json.dumps({"status": "not-running"}, sort_keys=True))
        return 0
    os.kill(pid, 15)
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline and running(pid):
        time.sleep(0.2)
    if running(pid):
        os.kill(pid, 9)
    runtime["pid"].unlink(missing_ok=True)
    print(json.dumps({"status": "stopped", "pid": pid}, sort_keys=True))
    return 0


def status(root, host, port, token_file):
    runtime = paths(root, token_file)
    pid = read_pid(runtime["pid"])
    payload = {"pid": pid if running(pid) else None, "port": port,
               "health": health(host, port), "ready": ready(host, port)}
    print(json.dumps(payload, sort_keys=True))
    return 0 if payload["health"] else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("start", "stop", "restart", "status"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--token-file", default=None)
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args(argv)
    if not 1 <= args.port <= 65535:
        parser.error("--port must be in 1..65535")
    root = args.root.resolve()
    token_file = Path(args.token_file) if args.token_file else None
    if args.command == "start":
        return start(root, args.host, args.port, token_file, args.timeout)
    if args.command == "stop":
        return stop(root, token_file)
    if args.command == "status":
        return status(root, args.host, args.port, token_file)
    stop(root, token_file)
    return start(root, args.host, args.port, token_file, args.timeout)


if __name__ == "__main__":
    raise SystemExit(main())

