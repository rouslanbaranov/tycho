"""MCP pattern registry and evidence handlers."""
from mcp_runtime import *  # noqa: F401,F403


class PatternToolsMixin:
    def _tool_patterns(self, args):
        reject_unknown(args, {
            "family", "query", "limit", "offset", "registry_snapshot_id",
        })
        family = arg_string(args, "family", maximum=200)
        text = arg_string(args, "query", maximum=500)
        limit = arg_int(
            args, "limit", DEFAULT_PATTERNS_LIMIT, 1, MAX_PATTERNS_LIMIT)
        offset = arg_int(
            args, "offset", 0, 0, MAX_PATTERN_OFFSET)
        requested = arg_hash(args, "registry_snapshot_id")
        data, snapshot, error = self.load_patterns()
        if error is not None:
            return self.tool_error(
                "not-available", error, tool="tycho_patterns")
        mismatch = registry_mismatch(requested, snapshot)
        if mismatch is not None:
            mismatch["tool"] = "tycho_patterns"
            return mismatch
        families = {
            item.get("id"): item
            for item in data["families"]
            if isinstance(item, dict) and item.get("id")
        }
        all_patterns = [
            item for item in data["patterns"] if isinstance(item, dict)
        ]
        selected = []
        needle = text.casefold() if text is not None else None
        for pattern in all_patterns:
            if family is not None and pattern.get("family") != family:
                continue
            if needle is not None:
                aliases = pattern.get("aliases") or []
                haystack = " ".join([
                    str(pattern.get("id", "")),
                    str(pattern.get("catalog_name", "")),
                    str(pattern.get("catalog_problem", "")),
                    " ".join(str(item) for item in aliases
                             if isinstance(item, str)),
                ]).casefold()
                if needle not in haystack:
                    continue
            selected.append(pattern)
        selected.sort(key=lambda item: (
            item.get("catalog_order")
            if is_int(item.get("catalog_order")) else 10 ** 9,
            str(item.get("id", "")),
        ))
        total = len(selected)
        page = selected[offset:offset + limit]
        patterns = [
            self.pattern_summary(item, families) for item in page
        ]
        coverage = coverage_summary(all_patterns)
        sufficient = coverage.get("sufficient", 0)
        status = "ok" if total else "no-results"
        truncated = offset + len(patterns) < total
        return {
            "status": status,
            "registry_snapshot": snapshot,
            "registry_version": data.get("registry_version"),
            "registry_status": data.get("status"),
            "registry_updated_at": data.get("updated_at"),
            "registry_entries": len(all_patterns),
            "coverage_summary": coverage,
            "sufficiency": {
                "sufficient_entries": sufficient,
                "registry_status": data.get("status") or "unknown",
                "caveat": (
                    "Sufficient entries and registry status are read from "
                    "the registry, not inferred here."
                ),
            },
            "citation_scheme": PATTERN_CITATION_SCHEME,
            "family": family,
            "query": text,
            "offset": offset,
            "limit": limit,
            "total": total,
            "returned": len(patterns),
            "truncated": truncated,
            "next_offset": (offset + len(patterns)) if truncated else None,
            "patterns": patterns,
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_patterns",
        }

    def _tool_pattern(self, args):
        reject_unknown(args, {
            "pattern_id", "registry_snapshot_id",
        })
        pattern_id = arg_string(
            args, "pattern_id", required=True, maximum=200)
        requested = arg_hash(args, "registry_snapshot_id")
        data, snapshot, error = self.load_patterns()
        if error is not None:
            return self.tool_error(
                "not-available", error, tool="tycho_pattern")
        mismatch = registry_mismatch(requested, snapshot)
        if mismatch is not None:
            mismatch["tool"] = "tycho_pattern"
            return mismatch
        families = {
            item.get("id"): item
            for item in data["families"]
            if isinstance(item, dict) and item.get("id")
        }
        pattern = next((
            item for item in data["patterns"]
            if isinstance(item, dict) and item.get("id") == pattern_id
        ), None)
        if pattern is None:
            return self.tool_error(
                "not-found",
                "No pattern at " + pattern_id,
                pattern_id=pattern_id,
                tool="tycho_pattern",
            )
        cards, cards_error = self.load_pattern_cards()
        card = None if cards is None else cards.get(pattern_id)
        owner = pattern.get("technical_owner") or {}
        path = owner.get("path")
        anchor = owner.get("anchor")
        coverage = pattern.get("coverage") or {}
        try:
            v12_artifacts = section_search.v12_artifacts(
                self.root, pattern_ids=[pattern_id], limit=50)
        except (OSError, ValueError, section_search.SearchError):
            v12_artifacts = {
                "status": "not-available", "returned": 0, "total": 0,
                "artifacts": [], "filters": {"pattern_ids": [pattern_id]},
            }
        return {
            "status": "ok",
            "registry_snapshot": snapshot,
            "registry_version": data.get("registry_version"),
            "registry_status": data.get("status"),
            "registry_updated_at": data.get("updated_at"),
            "pattern": pattern,
            "family": families.get(pattern.get("family")),
            "card": card,
            "cards_status": "ok" if cards_error is None else "not-available",
            "citation": (path + "#" + anchor) if path and anchor else path,
            "citation_scheme": PATTERN_CITATION_SCHEME,
            "owner_read": (
                {"tool": "tycho_page", "arguments": {"path": path}}
                if path else None
            ),
            "coverage": coverage,
            "v12_artifacts": v12_artifacts,
            "sufficiency": {
                "sufficient": coverage.get("overall") == "sufficient",
                "coverage_state": coverage.get("overall", "unknown"),
                "caveat": (
                    "Pattern coverage is a registry state, not independent "
                    "technical or decision sufficiency."
                ),
            },
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_pattern",
        }

    def _tool_evidence(self, args):
        reject_unknown(args, {
            "document_id", "claim_id", "source_id",
            "expected_evidence_snapshot", "snapshot_id",
        })
        values = [
            arg_string(args, name, maximum=500)
            for name in ("document_id", "claim_id", "source_id")
        ]
        provided = [value for value in values if value is not None]
        if len(provided) != 1:
            raise ProtocolFailure(
                -32602,
                "Provide exactly one of document_id, claim_id or source_id",
            )
        expected = args.get("expected_evidence_snapshot")
        if expected is not None:
            if not isinstance(expected, str) or not SNAPSHOT_RE.fullmatch(expected):
                raise ProtocolFailure(
                    -32602,
                    "expected_evidence_snapshot must be 64 lowercase "
                    "hexadecimal characters",
                )
        requested = arg_snapshot(args)
        try:
            payload = section_search.evidence(
                self.root,
                document_id=values[0],
                claim_id=values[1],
                source_id=values[2],
                index_path=self.index_path,
                expected_evidence_snapshot=expected,
            )
        except section_search.SearchError as exc:
            return self.search_error(exc, "tycho_evidence")
        except OSError:
            return self.tool_error(
                "not-available", "Evidence store is not available",
                tool="tycho_evidence")
        except (sqlite3.Error, ValueError, RuntimeError) as exc:
            return self.tool_error(
                getattr(exc, "status", "not-available"),
                str(exc),
                tool="tycho_evidence",
            )
        mismatch = self.check_snapshot(
            requested, payload.get("search_snapshot"))
        if mismatch is not None:
            mismatch["tool"] = "tycho_evidence"
            return mismatch
        payload["content_trust"] = CONTENT_TRUST
        payload["tool"] = "tycho_evidence"
        return payload
