#!/usr/bin/env python3
"""Read-only MCP stdio adapter for Tycho's snapshot-bound retrieval core.

The adapter exposes bounded search, section read, page read and evidence lookup
over the published section index. It implements a dual-era MCP surface:

* modern 2026-07-28 per-request metadata, server/discover and stateless calls;
* bounded legacy 2025-11-25 initialize/tools behavior over stdio.

BM25 is the default. An optional best mode combines adaptive hybrid ranking
with a frozen top-1 reranker when its dependencies and cache are available. It
is not a pinned-SDK conformance run, a hosted HTTP service, an answer generator
or a writer.
Returned book text is evidence, never permission or instructions.

See authoring/MCP-READ-ONLY-MVP.md for the bounded contract and limits.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import stat
import sys
import time

try:
    import yaml
except ImportError:  # frontmatter stays omitted if PyYAML is unavailable
    yaml = None

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "scripts"))

import best_search
import mcp_contract
import route_index
import section_fts_index
import section_search

ROOT = Path(__file__).resolve().parents[1]
from mcp_runtime import *

def search_schema():
    return mcp_contract.input_schema("tycho_search")


def batch_schema():
    return mcp_contract.input_schema("tycho_batch")


def outline_schema():
    return mcp_contract.input_schema("tycho_outline")


def compare_schema():
    return mcp_contract.input_schema("tycho_compare")


def context_schema():
    return mcp_contract.input_schema("tycho_context")


def read_schema():
    return mcp_contract.input_schema("tycho_read")


def page_schema():
    return mcp_contract.input_schema("tycho_page")


def evidence_schema():
    return mcp_contract.input_schema("tycho_evidence")


def describe_schema():
    return mcp_contract.input_schema("tycho_describe")


def patterns_schema():
    return mcp_contract.input_schema("tycho_patterns")


def pattern_schema():
    return mcp_contract.input_schema("tycho_pattern")


def tool_definitions():
    definitions = []
    for name in TOOL_ORDER:
        item = {key: value for key, value in TOOL_SPECS[name].items()
                if key != "handler"}
        item["outputSchema"] = mcp_contract.OUTPUT_SCHEMAS[name]
        definitions.append(item)
    return definitions


from mcp_context_tools import ContextToolsMixin
from mcp_describe_tools import DescribeToolsMixin
from mcp_pattern_tools import PatternToolsMixin
from mcp_read_tools import ReadToolsMixin
from mcp_search_tools import SearchToolsMixin


class TychoMcpServer(
        SearchToolsMixin, ContextToolsMixin, ReadToolsMixin,
        PatternToolsMixin, DescribeToolsMixin):
    """A bounded dual-era MCP adapter over one Tycho checkout."""

    def __init__(self, root=ROOT, index_path=None, pattern_registry=None,
                 pattern_cards=None, query_log=None, query_log_raw=False):
        self.root = Path(root).resolve()
        self.index_path = None if index_path is None else Path(index_path)
        self.pattern_registry = self.root / (
            pattern_registry or DEFAULT_PATTERN_REGISTRY)
        self.pattern_cards = self.root / (
            pattern_cards or DEFAULT_PATTERN_CARDS)
        self.query_log = None if query_log is None else Path(query_log)
        self.query_log_raw = query_log_raw
        self.legacy_initialized = False
        self.legacy_version = None
        self._last_refresh = 0.0
        self.index_refresh = self.refresh_index(force=True)

    def refresh_index(self, force=False):
        """Verify or rebuild the derived index before serving a request."""
        now = time.monotonic()
        if not force and now - self._last_refresh < 0.5:
            return self.index_refresh
        self._last_refresh = now
        self.index_refresh = section_fts_index.ensure_fresh(
            self.root, self.index_path)
        return self.index_refresh

    def load_patterns(self):
        try:
            raw = self.pattern_registry.read_bytes()
        except OSError:
            return None, None, "Pattern registry is not available"
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None, None, "Pattern registry is malformed"
        if (not isinstance(data, dict)
                or not isinstance(data.get("patterns"), list)
                or not isinstance(data.get("families"), list)):
            return None, None, "Pattern registry has an unexpected shape"
        return data, hashlib.sha256(raw).hexdigest(), None

    def load_pattern_cards(self):
        try:
            raw = self.pattern_cards.read_bytes()
        except OSError:
            return None, "Pattern cards are not available"
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None, "Pattern cards are malformed"
        if not isinstance(data, dict) or not isinstance(data.get("batches"), list):
            return None, "Pattern cards have an unexpected shape"
        cards = {}
        for batch in data["batches"]:
            if not isinstance(batch, dict):
                continue
            for entry in batch.get("entries", []):
                if (isinstance(entry, dict)
                        and isinstance(entry.get("pattern_id"), str)):
                    cards.setdefault(entry["pattern_id"], entry)
        return cards, None

    @staticmethod
    def pattern_summary(pattern, families):
        family = families.get(pattern.get("family")) or {}
        owner = pattern.get("technical_owner") or {}
        path = owner.get("path")
        anchor = owner.get("anchor")
        return {
            "pattern_id": pattern.get("id"),
            "catalog_name": pattern.get("catalog_name"),
            "family": pattern.get("family"),
            "family_title": family.get("title"),
            "kind": pattern.get("kind"),
            "priority": pattern.get("priority"),
            "catalog_order": pattern.get("catalog_order"),
            "catalog_problem": pattern.get("catalog_problem"),
            "technical_owner": owner,
            "citation": (path + "#" + anchor) if path and anchor else path,
            "citation_scheme": PATTERN_CITATION_SCHEME,
            "coverage": pattern.get("coverage"),
            "confidence": pattern.get("confidence"),
            "review_status": pattern.get("review_status"),
            "source_units": pattern.get("source_units") or [],
        }

    def query_log_is_safe(self):
        target = self.query_log
        if target is None:
            return False
        try:
            if target.is_symlink():
                return False
            resolved = target.resolve(strict=False)
            if resolved == self.root or resolved.is_relative_to(self.root):
                return False
            if not resolved.parent.is_dir():
                return False
            if target.exists():
                info = target.stat()
                if (not stat.S_ISREG(info.st_mode)
                        or info.st_nlink != 1):
                    return False
        except (OSError, RuntimeError, ValueError):
            return False
        return True

    def log_query(self, payload, args, query, limit):
        if self.query_log is None:
            return
        if not self.query_log_is_safe():
            payload["query_log"] = "not-available"
            return
        record = {
            "schema_version": 1,
            "logged_at": datetime.now(timezone.utc).isoformat(
                timespec="seconds").replace("+00:00", "Z"),
            "tool": "tycho_search",
            ("query" if self.query_log_raw else "query_sha256"):
                (query if self.query_log_raw
                 else hashlib.sha256(query.encode("utf-8")).hexdigest()),
            "filters": {
                "kind": args.get("kind"),
                "topic": args.get("topic"),
                "evidence_status": args.get("evidence_status"),
                "path_prefix": args.get("path_prefix"),
                "all_sections": args.get("all_sections", False),
            },
            "limit": limit,
            "snapshot": payload.get("snapshot"),
            "status": payload.get("status"),
            "returned": payload.get("returned"),
            "top": [
                item.get("citation")
                for item in payload.get("results", [])
            ][:20],
        }
        flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
        flags |= getattr(os, "O_NOFOLLOW", 0)
        descriptor = None
        try:
            descriptor = os.open(str(self.query_log), flags, 0o600)
            info = os.fstat(descriptor)
            if (not stat.S_ISREG(info.st_mode)
                    or info.st_nlink != 1):
                raise OSError("query log must be a regular file")
            with os.fdopen(descriptor, "a", encoding="utf-8") as handle:
                descriptor = None
                handle.write(json.dumps(
                    record, ensure_ascii=False, sort_keys=True) + "\n")
        except (OSError, ValueError):
            payload["query_log"] = "not-available"
        else:
            payload["query_log"] = "recorded"
        finally:
            if descriptor is not None:
                os.close(descriptor)

    def handle(self, message):
        self.refresh_index()
        if not isinstance(message, dict):
            raise ProtocolFailure(-32600, "JSON-RPC message must be an object")
        if message.get("jsonrpc") != "2.0":
            raise ProtocolFailure(-32600, "jsonrpc must be '2.0'")
        method = message.get("method")
        if not isinstance(method, str) or not method:
            raise ProtocolFailure(-32600, "method must be a non-empty string")
        request_id = message.get("id")
        has_id = "id" in message
        if has_id and (
                request_id is None or isinstance(request_id, bool)
                or not isinstance(request_id, (str, int))):
            raise ProtocolFailure(-32600, "id must be a string or integer")
        params = message.get("params", {})
        if params is None:
            params = {}
        if not has_id:
            return None
        if not isinstance(params, dict):
            raise ProtocolFailure(-32602, "params must be an object")
        meta = params.get("_meta")
        if meta is not None and not isinstance(meta, dict):
            raise ProtocolFailure(-32602, "_meta must be an object")
        has_modern_meta = (
            isinstance(meta, dict) and META_VERSION in meta)

        if method == "server/discover":
            reject_unknown(params, {"_meta"})
            if meta is None:
                raise ProtocolFailure(
                    -32602, "Missing required _meta for server/discover")
            version = self.metadata_version(meta)
            if version != MODERN_VERSION:
                raise self.unsupported(version)
            self.require_capabilities(meta)
            return self.modern_response(request_id, self.discover())

        if method == "initialize":
            if has_modern_meta:
                raise ProtocolFailure(
                    -32601, "initialize is not part of protocol 2026-07-28")
            return self.legacy_initialize(request_id, params)

        modern = has_modern_meta
        if modern:
            version = self.metadata_version(meta)
            if version != MODERN_VERSION:
                raise self.unsupported(version)
            self.require_capabilities(meta)
        elif not self.legacy_initialized:
            if meta is not None:
                raise ProtocolFailure(
                    -32602,
                    "Missing required _meta field " + META_VERSION,
                )
            raise ProtocolFailure(
                -32600,
                "Missing per-request _meta; call server/discover or initialize",
            )
        result = self.dispatch(method, params, modern)
        if modern:
            return self.modern_response(request_id, result)
        return self.legacy_response(request_id, result)

    @staticmethod
    def metadata_version(meta):
        version = meta.get(META_VERSION)
        if not isinstance(version, str) or not version:
            raise ProtocolFailure(
                -32602, "Missing required _meta field " + META_VERSION)
        return version

    @staticmethod
    def require_capabilities(meta):
        capabilities = meta.get(META_CAPABILITIES)
        if not isinstance(capabilities, dict):
            raise ProtocolFailure(
                -32602, "Missing required _meta field " + META_CAPABILITIES)

    @staticmethod
    def unsupported(version):
        return ProtocolFailure(
            -32022,
            "Unsupported protocol version",
            {"supported": list(SUPPORTED_VERSIONS), "requested": version},
        )

    def legacy_initialize(self, request_id, params):
        protocol = params.get("protocolVersion")
        if not isinstance(protocol, str) or not protocol:
            raise ProtocolFailure(-32602, "protocolVersion is required")
        if protocol != LEGACY_VERSION:
            raise ProtocolFailure(
                -32602,
                "Unsupported legacy protocol version",
                {"supported": [LEGACY_VERSION], "requested": protocol},
            )
        capabilities = params.get("capabilities", {})
        if capabilities is not None and not isinstance(capabilities, dict):
            raise ProtocolFailure(-32602, "capabilities must be an object")
        client = params.get("clientInfo")
        if client is not None and not isinstance(client, dict):
            raise ProtocolFailure(-32602, "clientInfo must be an object")
        self.legacy_initialized = True
        self.legacy_version = protocol
        return self.legacy_response(request_id, {
            "protocolVersion": LEGACY_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": dict(SERVER_INFO),
            "instructions": INSTRUCTIONS,
        })

    def discover(self):
        return {
            "supportedVersions": list(SUPPORTED_VERSIONS),
            "capabilities": {"tools": {}},
            "instructions": INSTRUCTIONS,
            "ttlMs": CACHE_TTL_MS,
            "cacheScope": CACHE_SCOPE,
        }

    def dispatch(self, method, params, modern):
        if method == "ping":
            if modern:
                raise ProtocolFailure(
                    -32601, "ping is not part of protocol 2026-07-28")
            return {}
        if method == "tools/list":
            return self.tools_list(params, modern)
        if method == "tools/call":
            return self.tools_call(params)
        raise ProtocolFailure(-32601, "Method not found: " + method)

    def tools_list(self, params, modern):
        reject_unknown(params, {"cursor", "_meta"})
        if params.get("cursor") is not None:
            raise ProtocolFailure(-32602, "Pagination is not supported")
        result = {"tools": tool_definitions()}
        if modern:
            result["ttlMs"] = CACHE_TTL_MS
            result["cacheScope"] = CACHE_SCOPE
        return result

    def tools_call(self, params):
        reject_unknown(params, {"name", "arguments", "_meta"})
        name = params.get("name")
        if not isinstance(name, str) or not name:
            raise ProtocolFailure(-32602, "name is required")
        arguments = params.get("arguments", {})
        if arguments is None:
            arguments = {}
        require_object(arguments, "arguments")
        spec = TOOL_SPECS.get(name)
        if spec is None:
            raise ProtocolFailure(
                -32602, "Unknown tool: " + name, {"tool": name})
        payload = getattr(self, spec["handler"])(arguments)
        return self.tool_result(payload)

    def tool_result(self, payload):
        payload = dict(payload)
        if payload.get("status") == "offset-inside-diagram":
            return {
                "content": [{"type": "text",
                             "text": str(payload.get("error", ""))}],
                "isError": True,
            }
        payload.setdefault("content_trust", CONTENT_TRUST)
        text = json.dumps(
            payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        return {
            "content": [{"type": "text", "text": text}],
            "structuredContent": payload,
            "isError": payload.get("status") not in (
                "ok", "no-results", "no-confident-answer"),
        }

    @staticmethod
    def modern_response(request_id, result):
        result = dict(result)
        result["resultType"] = "complete"
        meta = dict(result.get("_meta") or {})
        meta[META_SERVER] = dict(SERVER_INFO)
        result["_meta"] = meta
        return {"jsonrpc": "2.0", "id": request_id, "result": result}

    @staticmethod
    def legacy_response(request_id, result):
        return {"jsonrpc": "2.0", "id": request_id, "result": result}

    def open_snapshot(self):
        self.refresh_index()
        return section_search.open_snapshot(self.root, self.index_path)

    @staticmethod
    def check_snapshot(requested, current):
        return snapshot_mismatch(requested, current)

    @staticmethod
    def tool_error(status, message, **extra):
        payload = dict(extra)
        payload["status"] = status
        payload["error"] = message
        payload["content_trust"] = CONTENT_TRUST
        return payload

    def search_error(self, exc, tool):
        return self.tool_error(
            getattr(exc, "status", "invalid-request"),
            str(exc),
            tool=tool,
        )

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--index", type=Path)
    parser.add_argument("--pattern-registry", type=Path)
    parser.add_argument("--pattern-cards", type=Path)
    parser.add_argument(
        "--query-log", type=Path,
        help="Opt-in JSONL search-query log; disabled by default")
    parser.add_argument(
        "--query-log-raw", action="store_true",
        help="Store raw query text in the opt-in log (hash is default)")
    args = parser.parse_args(argv)
    server = TychoMcpServer(
        args.root, args.index, pattern_registry=args.pattern_registry,
        pattern_cards=args.pattern_cards, query_log=args.query_log,
        query_log_raw=args.query_log_raw)
    try:
        serve(server)
    except BrokenPipeError:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
