#!/usr/bin/env python3
"""Read-only HTTP MCP service for local container and client-agent tests.

The existing stdio adapter remains the canonical protocol implementation.
This module adds a modern 2026-07-28 stateless HTTP wrapper, bearer auth,
health/readiness, a bounded search API and raw book file delivery. It does not
implement OAuth, TLS termination, sessions, SSE subscriptions or production
rate limiting; those remain deployment-provider work.

Every MCP and book request requires a bearer token from the environment.
The process never writes the book, index or query log.
"""
import argparse
import hmac
import html
import json
import os
from pathlib import Path
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, unquote, urlsplit

from mcp_server import (
    META_VERSION,
    MODERN_VERSION,
    ProtocolFailure,
    TychoMcpServer,
    error_response,
)

ROOT = Path(__file__).resolve().parents[1]
MAX_BODY_BYTES = 1_000_000
SERVICE_NAME = "tycho-mcp-http"
SERVICE_VERSION = "0.1.0"


class HttpRequestError(Exception):
    def __init__(self, status, message, code=-32600):
        super().__init__(message)
        self.status = status
        self.message = message
        self.code = code


def json_rpc_error(code, message, data=None):
    return error_response(None, code, message, data)


def decode_body(raw):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise HttpRequestError(400, "Body must be UTF-8 JSON") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise HttpRequestError(400, "Invalid JSON body", -32700) from exc


def response_error(code, message, data=None):
    return json_rpc_error(code, message, data)


class TychoHttpApplication:
    def __init__(self, root=ROOT, index_path=None, token=None):
        self.root = Path(root).resolve()
        self.server = TychoMcpServer(self.root, index_path)
        self.token = token

    def authorized(self, headers):
        if not self.token:
            return False
        value = headers.get("Authorization", "")
        if not value.startswith("Bearer "):
            return False
        return hmac.compare_digest(value[7:], self.token)

    def health(self):
        return {
            "status": "ok",
            "service": SERVICE_NAME,
            "version": SERVICE_VERSION,
            "protocol": MODERN_VERSION,
        }

    def ready(self):
        db, manifest = self.server.open_snapshot()
        db.close()
        return {
            "status": "ok",
            "snapshot": manifest["snapshot_id"],
            "route_snapshot": manifest["route_snapshot_sha256"],
            "coverage": manifest["coverage"],
            "documents": manifest["document_count"],
            "sections": manifest["section_count"],
        }

    @staticmethod
    def message_meta(message):
        params = message.get("params")
        if not isinstance(params, dict):
            return {}
        meta = params.get("_meta")
        return meta if isinstance(meta, dict) else {}

    def check_headers(self, message, headers):
        method = message.get("method")
        meta = self.message_meta(message)
        version = meta.get(META_VERSION)
        header_version = headers.get("MCP-Protocol-Version")
        if header_version and version and header_version != version:
            raise HttpRequestError(
                400,
                "MCP-Protocol-Version header differs from request metadata",
                -32020,
            )
        header_method = headers.get("Mcp-Method")
        if header_method and header_method != method:
            raise HttpRequestError(
                400, "Mcp-Method header differs from JSON-RPC method", -32020)
        if method == "tools/call":
            params = message.get("params")
            name = params.get("name") if isinstance(params, dict) else None
            header_name = headers.get("Mcp-Name")
            if header_name and header_name != name:
                raise HttpRequestError(
                    400, "Mcp-Name header differs from tool name", -32020)

    def handle_mcp(self, raw, headers):
        message = decode_body(raw)
        if not isinstance(message, dict):
            raise HttpRequestError(400, "JSON-RPC message must be an object")
        self.check_headers(message, headers)
        if message.get("method") == "initialize":
            raise HttpRequestError(
                400,
                "legacy initialize is not supported by stateless HTTP; "
                "use modern 2026-07-28",
                -32601,
            )
        try:
            response = self.server.handle(message)
        except ProtocolFailure as exc:
            return 200, error_response(
                message.get("id"), exc.code, exc.message, exc.data)
        except Exception:
            return 200, error_response(
                message.get("id"), -32603, "Internal server error")
        if response is None:
            return 202, None
        if message.get("method") == "server/discover":
            result = response.get("result")
            if isinstance(result, dict):
                result["supportedVersions"] = [MODERN_VERSION]
        return 200, response

    def search_arguments(self, values):
        args = {}
        query = values.get("query", values.get("q"))
        if not isinstance(query, str) or not query.strip():
            raise HttpRequestError(400, "query is required")
        args["query"] = query
        for name in ("kind", "topic", "evidence_status", "path_prefix"):
            value = values.get(name)
            if value is not None:
                if not isinstance(value, str) or not value:
                    raise HttpRequestError(400, name + " must be a string")
                args[name] = value
        limit = values.get("limit", 5)
        if isinstance(limit, str):
            try:
                limit = int(limit)
            except ValueError as exc:
                raise HttpRequestError(400, "limit must be an integer") from exc
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise HttpRequestError(400, "limit must be an integer")
        args["limit"] = limit
        all_sections = values.get("all_sections", False)
        if isinstance(all_sections, str):
            all_sections = all_sections.lower() in ("1", "true", "yes")
        if not isinstance(all_sections, bool):
            raise HttpRequestError(400, "all_sections must be boolean")
        args["all_sections"] = all_sections
        snapshot = values.get("snapshot_id")
        if snapshot is not None:
            if not isinstance(snapshot, str):
                raise HttpRequestError(400, "snapshot_id must be a string")
            args["snapshot_id"] = snapshot
        return args

    def handle_search(self, values):
        args = self.search_arguments(values)
        try:
            payload = self.server._tool_search(args)
        except ProtocolFailure as exc:
            raise HttpRequestError(400, exc.message, exc.code) from exc
        except Exception:
            raise HttpRequestError(503, "Search is not available")
        return 200, payload

    def book_index(self):
        book_root = self.root / "book"
        files = sorted(
            path.relative_to(book_root).as_posix()
            for path in book_root.rglob("*.md")
            if path.is_file() and not path.is_symlink()
        )
        links = "\n".join(
            '<li><a href="/book/' + quote(name) + '">' +
            html.escape(name) + "</a></li>"
            for name in files
        )
        return (
            "<!doctype html><html><head><meta charset=\"utf-8\">"
            "<title>Tycho book</title></head><body>"
            "<h1>Tycho book</h1><p>Read-only raw Markdown pages.</p>"
            "<ul>" + links + "</ul></body></html>"
        )

    def book_file(self, request_path):
        prefix = "/book/"
        if not request_path.startswith(prefix):
            raise HttpRequestError(404, "Book path not found")
        relative = unquote(request_path[len(prefix):])
        if (not relative or relative.startswith("/") or "\\" in relative
                or ".." in relative.split("/")
                or not relative.endswith(".md")):
            raise HttpRequestError(400, "Invalid book path")
        target = (self.root / "book" / relative).resolve()
        book_root = (self.root / "book").resolve()
        if (target == book_root or not target.is_relative_to(book_root)
                or target.is_symlink() or not target.is_file()):
            raise HttpRequestError(404, "Book path not found")
        text = target.read_text(encoding="utf-8")
        return 200, "text/markdown; charset=utf-8", text


class TychoHttpRequestHandler(BaseHTTPRequestHandler):
    application = None
    server_version = "tycho-mcp-http/" + SERVICE_VERSION

    def log_message(self, format, *args):
        path = urlsplit(self.path).path
        sys.stderr.write(
            "%s - - %s %s\n" % (self.address_string(), self.command, path))

    def send_payload(self, status, payload, content_type="application/json"):
        if payload is None:
            body = b""
        elif isinstance(payload, bytes):
            body = payload
        else:
            body = json.dumps(
                payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        if status == 401:
            self.send_header("WWW-Authenticate", "Bearer")
        self.end_headers()
        if body:
            self.wfile.write(body)

    def send_error_payload(self, status, message, code=-32600, data=None):
        self.send_payload(status, error_response(None, code, message, data))

    def require_auth(self):
        if not self.application.authorized(self.headers):
            self.send_error_payload(401, "Bearer token required", -32000)
            return False
        return True

    def read_body(self):
        length = self.headers.get("Content-Length", "0")
        try:
            size = int(length)
        except ValueError:
            raise HttpRequestError(400, "Content-Length must be an integer")
        if size < 0 or size > MAX_BODY_BYTES:
            raise HttpRequestError(413, "Request body is too large")
        return self.rfile.read(size)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Allow", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers",
                         "Authorization, Content-Type, "
                         "MCP-Protocol-Version, Mcp-Method, Mcp-Name")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()

    def do_GET(self):
        parsed = urlsplit(self.path)
        path = parsed.path
        if path == "/health":
            self.send_payload(200, self.application.health())
            return
        if path == "/ready":
            try:
                self.send_payload(200, self.application.ready())
            except Exception:
                self.send_error_payload(503, "Snapshot is not ready")
            return
        if path == "/":
            self.send_payload(200, {
                "service": SERVICE_NAME,
                "version": SERVICE_VERSION,
                "endpoints": ["/mcp", "/search", "/book", "/health", "/ready"],
            })
            return
        if not self.require_auth():
            return
        if path == "/mcp":
            self.send_error_payload(405, "Use POST /mcp", -32600)
            return
        if path == "/search":
            try:
                values = {
                    key: values[-1]
                    for key, values in parse_qs(parsed.query).items()
                    if values
                }
                status, payload = self.application.handle_search(values)
                self.send_payload(status, payload)
            except HttpRequestError as exc:
                self.send_error_payload(
                    exc.status, exc.message, exc.code)
            return
        if path == "/book" or path == "/book/":
            self.send_payload(
                200, self.application.book_index(),
                "text/html; charset=utf-8")
            return
        if path.startswith("/book/"):
            try:
                status, content_type, text = self.application.book_file(path)
                self.send_payload(status, text.encode("utf-8"), content_type)
            except HttpRequestError as exc:
                self.send_error_payload(exc.status, exc.message, exc.code)
            except OSError:
                self.send_error_payload(404, "Book path not found")
            return
        self.send_error_payload(404, "Not found")

    def do_POST(self):
        parsed = urlsplit(self.path)
        path = parsed.path
        if path not in ("/mcp", "/search"):
            self.send_error_payload(404, "Not found")
            return
        if not self.require_auth():
            return
        try:
            raw = self.read_body()
            if path == "/mcp":
                status, payload = self.application.handle_mcp(
                    raw, self.headers)
                self.send_payload(status, payload)
                return
            values = decode_body(raw)
            if not isinstance(values, dict):
                raise HttpRequestError(400, "Search body must be an object")
            status, payload = self.application.handle_search(values)
            self.send_payload(status, payload)
        except HttpRequestError as exc:
            self.send_error_payload(exc.status, exc.message, exc.code)
        except Exception:
            self.send_error_payload(500, "Internal server error", -32603)


def build_server(application, host, port):
    handler = type(
        "BoundTychoHttpRequestHandler",
        (TychoHttpRequestHandler,),
        {"application": application},
    )
    httpd = ThreadingHTTPServer((host, port), handler)
    httpd.daemon_threads = True
    return httpd


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--index", type=Path)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument(
        "--port", type=int, default=int(os.environ.get("PORT", "8000")))
    parser.add_argument("--token-env", default="TYCHO_MCP_TOKEN")
    args = parser.parse_args(argv)
    token = os.environ.get(args.token_env)
    if not token:
        print(
            "Missing bearer token environment variable: " + args.token_env,
            file=sys.stderr,
        )
        return 2
    application = TychoHttpApplication(args.root, args.index, token)
    httpd = build_server(application, args.host, args.port)
    print(
        "Tycho HTTP MCP listening on http://%s:%d/mcp"
        % (args.host, args.port),
        file=sys.stderr,
    )
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
