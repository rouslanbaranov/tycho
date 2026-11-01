"""MCP describe handler."""
from mcp_runtime import *  # noqa: F401,F403


class DescribeToolsMixin:
    def _tool_describe(self, args):
        reject_unknown(args, {"snapshot_id", "registry_snapshot_id"})
        requested = arg_snapshot(args)
        registry_requested = arg_hash(args, "registry_snapshot_id")
        try:
            db, manifest = self.open_snapshot()
        except section_search.SearchError as exc:
            return self.search_error(exc, "tycho_describe")
        db.close()
        mismatch = self.check_snapshot(requested, manifest["snapshot_id"])
        if mismatch is not None:
            mismatch["tool"] = "tycho_describe"
            return mismatch
        logging = "disabled"
        if self.query_log is not None:
            logging = (
                "enabled" if self.query_log_is_safe() else "not-available")
        patterns, pattern_snapshot, pattern_error = self.load_patterns()
        if pattern_error is None:
            mismatch = registry_mismatch(
                registry_requested, pattern_snapshot)
            if mismatch is not None:
                mismatch["tool"] = "tycho_describe"
                return mismatch
            registry = {
                "status": "ok",
                "snapshot": pattern_snapshot,
                "version": patterns.get("registry_version"),
                "registry_status": patterns.get("status"),
                "entries": len(patterns["patterns"]),
                "coverage_summary": coverage_summary(patterns["patterns"]),
                "citation_scheme": PATTERN_CITATION_SCHEME,
            }
        else:
            if registry_requested is not None:
                return self.tool_error(
                    "not-available",
                    pattern_error,
                    tool="tycho_describe",
                )
            registry = {
                "status": "not-available",
                "error": pattern_error,
            }
        return {
            "status": "ok",
            "collection": {
                "id": "tycho",
                "title": "Tycho - System Design",
                "kind": "book",
                "units": "volumes, chapters, pages and a pattern atlas",
            },
            "snapshot": manifest["snapshot_id"],
            "route_snapshot": manifest["route_snapshot_sha256"],
            "coverage": manifest["coverage"],
            "unannotated": len(manifest["unannotated_paths"]),
            "counts": {
                "documents": manifest["document_count"],
                "sections": manifest["section_count"],
            },
            "pattern_registry": registry,
            "ranker_version": section_search.RANKER_VERSION,
            "citation_scheme": section_search.CITATION_SCHEME,
            "protocol_versions": list(SUPPORTED_VERSIONS),
            "tools": list(TOOL_ORDER),
            "query_logging": logging,
            "limits": {
                "search_limit": [1, MAX_LIMIT],
                "read_budget_chars": [1, MAX_BUDGET],
                "page_budget_chars": [1, MAX_BUDGET],
                "patterns_limit": [1, MAX_PATTERNS_LIMIT],
                "patterns_offset": [0, MAX_PATTERN_OFFSET],
                "message_chars": MAX_MESSAGE_CHARS,
            },
            "metadata": mcp_contract.catalog(),
            "operations": {
                "search": ("lexical BM25 by default; retrieval_mode=best "
                           "selects adaptive hybrid plus V12-gated reranker"),
                "batch": "bounded multi-read and evidence resolution",
                "outline": "canonical planning outline without full text",
                "compare": "extractive cited option matrix without a winner",
                "context": "bounded extractive analysis bundle",
                "read": "bounded codepoint range from one section",
                "page": "bounded page body plus section map",
                "patterns": "draft pattern-registry summaries and lookup",
                "evidence": "registered evidence metadata only",
            },
            "answerability": {
                "gate": "tycho-evidence-gate-v1",
                "strict_basis": "evidence-score-floor",
                "score_floor": 15.618061,
                "agent_default": "abstain=false; return candidates with metadata",
                "caveat": ("AI-calibrated floor, not answer correctness or human "
                           "review."),
            },
            "not_implemented": [
                "answer generation or verdicts",
                "OAuth, per-client authorization or rate limiting",
                "decision-method lookup",
            ],
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_describe",
        }
