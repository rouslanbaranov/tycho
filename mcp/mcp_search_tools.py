"""MCP search tool handlers."""
from mcp_runtime import *  # noqa: F401,F403


class SearchToolsMixin:
    def _tool_search(self, args):
        reject_unknown(args, {
            "query", "limit", "kind", "topic", "evidence_status",
            "path_prefix", "artifact_type", "volume", "pattern_ids",
            "include_artifacts", "all_sections", "abstain", "snapshot_id",
            "mode", "detail", "max_chars", "retrieval_mode",
            "section_rerank", "section_rerank_margin",
        })
        query = arg_string(args, "query", required=True)
        limit = arg_int(args, "limit", DEFAULT_LIMIT, 1, MAX_LIMIT)
        retrieval_mode = arg_string(args, "retrieval_mode", maximum=20) or "bm25"
        if retrieval_mode not in ("bm25", "best"):
            raise ProtocolFailure(-32602, "retrieval_mode must be bm25 or best")
        kind = arg_string(args, "kind", maximum=300)
        topic = arg_string(args, "topic", maximum=300)
        evidence_status = arg_string(
            args, "evidence_status", maximum=300)
        path_prefix = arg_string(args, "path_prefix", maximum=500)
        artifact_type = arg_string(args, "artifact_type", maximum=300)
        volume = arg_string(args, "volume", maximum=100)
        pattern_ids = args.get("pattern_ids", [])
        if pattern_ids is None:
            pattern_ids = []
        if not isinstance(pattern_ids, list) or any(
                not isinstance(item, str) or not item or len(item) > 200
                for item in pattern_ids):
            raise ProtocolFailure(-32602, "pattern_ids must be string IDs")
        include_artifacts = arg_bool(args, "include_artifacts", False)
        all_sections = arg_bool(args, "all_sections", False)
        section_rerank = arg_bool(args, "section_rerank", False)
        section_rerank_margin = args.get("section_rerank_margin", 0.05)
        if section_rerank_margin is not None and (
                not isinstance(section_rerank_margin, (int, float))
                or isinstance(section_rerank_margin, bool)
                or not 0 <= section_rerank_margin <= 1):
            raise ProtocolFailure(
                -32602, "section_rerank_margin must be in 0..1 or null")
        if retrieval_mode == "best":
            section_rerank = False
        if all_sections:
            section_rerank = False
        if section_rerank and (volume == "v12"
                               or "v12" in query.casefold()):
            section_rerank = False
        abstain = arg_bool(args, "abstain", False)
        mode = arg_string(args, "mode", maximum=20) or "strict"
        if mode not in ("strict", "exploratory"):
            raise ProtocolFailure(-32602, "mode must be strict or exploratory")
        detail = arg_string(args, "detail", maximum=20) or "snippets"
        if detail not in ("ids", "snippets"):
            raise ProtocolFailure(-32602, "detail must be ids or snippets")
        max_chars = args.get("max_chars")
        if max_chars is not None and not is_int(max_chars):
            raise ProtocolFailure(-32602, "max_chars must be an integer")
        if max_chars is not None and not 256 <= max_chars <= 50000:
            raise ProtocolFailure(
                -32602, "max_chars must be in 256..50000")
        requested = arg_snapshot(args)
        if retrieval_mode == "best" and any((
                kind, topic, evidence_status, path_prefix, artifact_type,
                volume, pattern_ids, include_artifacts, all_sections,
                detail != "snippets", max_chars is not None)):
            raise ProtocolFailure(
                -32602, "best mode does not support filters or detail overrides")
        try:
            if retrieval_mode == "best":
                best = best_search.best_search(
                    self.root, query, limit=limit)
                payload = {
                    "status": best["status"],
                    "query": query,
                    "snapshot": best["snapshot"],
                    "returned": len(best["results"]),
                    "results": best["results"],
                    "retrieval_mode": best["retrieval_mode"],
                    "rerank": best["rerank"],
                }
            else:
                payload = section_search.search(
                    self.root,
                    query,
                    limit=limit,
                    kind=kind,
                    topic=topic,
                    evidence_status=evidence_status,
                    path_prefix=path_prefix,
                    artifact_type=artifact_type,
                    volume=volume,
                    pattern_ids=pattern_ids,
                    include_artifacts=include_artifacts,
                    index_path=self.index_path,
                    all_sections=all_sections,
                    section_rerank=section_rerank,
                    section_rerank_margin=section_rerank_margin,
                    abstain=abstain,
                    include_weak=(mode == "exploratory"),
                    detail=detail,
                    max_chars=max_chars,
                )
        except section_search.SearchError as exc:
            if section_rerank and "disabled for V12" in str(exc):
                payload = section_search.search(
                    self.root, query, limit=limit, kind=kind, topic=topic,
                    evidence_status=evidence_status,
                    path_prefix=path_prefix, artifact_type=artifact_type,
                    volume=volume, pattern_ids=pattern_ids,
                    include_artifacts=include_artifacts,
                    index_path=self.index_path,
                    all_sections=all_sections, section_rerank=False,
                    abstain=abstain,
                    include_weak=(mode == "exploratory"),
                    detail=detail, max_chars=max_chars)
            else:
                return self.search_error(exc, "tycho_search")
        except (OSError, sqlite3.Error, ValueError, RuntimeError):
            return self.tool_error(
                "not-available", "Search is not available",
                tool="tycho_search")
        mismatch = self.check_snapshot(requested, payload.get("snapshot"))
        if mismatch is not None:
            mismatch["tool"] = "tycho_search"
            return mismatch
        for key in ("results", "weak_results"):
            for item in payload.get(key, []):
                item.setdefault("anchor", item.get("section_id"))
                if "excerpt" in item:
                    item.setdefault("snippet", item.get("excerpt"))
        payload["mode"] = mode
        payload["answerability"] = answerability(payload)
        payload["content_trust"] = CONTENT_TRUST
        payload["tool"] = "tycho_search"
        self.log_query(payload, args, query, limit)
        return payload
