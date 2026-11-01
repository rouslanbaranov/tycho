"""MCP context, compare, outline and batch handlers."""
from mcp_runtime import *  # noqa: F401,F403


class ContextToolsMixin:
    def _tool_batch(self, args):
        reject_unknown(args, {
            "section_keys", "document_ids", "claim_ids", "source_ids",
            "budget_chars", "max_chars",
        })
        groups = {}
        for name in ("section_keys", "document_ids", "claim_ids", "source_ids"):
            value = args.get(name, [])
            if not isinstance(value, list):
                raise ProtocolFailure(-32602, name + " must be an array")
            if len(value) > 8:
                raise ProtocolFailure(-32602, name + " exceeds 8 items")
            if any(not isinstance(item, str) or not item.strip()
                   or len(item) > 500 for item in value):
                raise ProtocolFailure(
                    -32602, name + " must contain non-empty strings")
            groups[name] = value
        total = sum(len(value) for value in groups.values())
        if total == 0:
            raise ProtocolFailure(-32602, "At least one batch item is required")
        if total > 8:
            raise ProtocolFailure(-32602, "The combined batch exceeds 8 items")
        budget = arg_int(args, "budget_chars", 800, 100, 2000)
        max_chars = arg_int(args, "max_chars", 8000, 2048, 20000)
        items = []
        errors = 0
        for section_key in groups["section_keys"]:
            try:
                payload = section_search.read(
                    self.root,
                    section_key,
                    offset=0,
                    budget_chars=budget,
                    index_path=self.index_path,
                )
                items.append({
                    "kind": "section",
                    "status": payload.get("status"),
                    "section_key": section_key,
                    "result": payload,
                })
            except section_search.SearchError as exc:
                errors += 1
                items.append({
                    "kind": "section",
                    "status": getattr(exc, "status", "invalid-request"),
                    "section_key": section_key,
                    "error": str(exc),
                })
            except (OSError, sqlite3.Error, ValueError):
                errors += 1
                items.append({
                    "kind": "section",
                    "status": "not-available",
                    "section_key": section_key,
                    "error": "Read unavailable",
                })
        for name, kind in (
                ("document_ids", "document"),
                ("claim_ids", "claim"),
                ("source_ids", "source")):
            for identity in groups[name]:
                try:
                    payload = section_search.evidence(
                        self.root,
                        **{name[:-1]: identity},
                        index_path=self.index_path,
                    )
                    items.append({
                        "kind": kind,
                        "status": payload.get("status"),
                        "id": identity,
                        "result": payload,
                    })
                except section_search.SearchError as exc:
                    errors += 1
                    items.append({
                        "kind": kind,
                        "status": getattr(exc, "status", "invalid-request"),
                        "id": identity,
                        "error": str(exc),
                    })
                except (OSError, sqlite3.Error, ValueError, RuntimeError):
                    errors += 1
                    items.append({
                        "kind": kind,
                        "status": "not-available",
                        "id": identity,
                        "error": "Evidence unavailable",
                    })
        response = {
            "status": "partial" if errors else "ok",
            "items": items,
            "returned": len(items),
            "errors": errors,
            "budget_chars": budget,
            "max_chars": max_chars,
            "returned_chars": 0,
            "truncated": False,
            "notice": (
                "Bounded batch output; failed items are isolated. Evidence "
                "metadata is not source text and is not a final answer."),
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_batch",
        }
        def encoded_size():
            return len(json.dumps(
                response, ensure_ascii=False,
                separators=(",", ":")).encode("utf-8"))
        while encoded_size() > max_chars and response["items"]:
            response["items"].pop()
            response["returned"] = len(response["items"])
            response["truncated"] = True
        response["returned_chars"] = encoded_size()
        return response

    def _tool_outline(self, args):
        reject_unknown(args, {
            "topic", "path_prefix", "kind", "limit", "max_chars",
        })
        topic = arg_string(args, "topic", maximum=200)
        path_prefix = arg_string(args, "path_prefix", maximum=500)
        kind = arg_string(args, "kind", maximum=100)
        limit = arg_int(args, "limit", 8, 1, 20)
        max_chars = arg_int(args, "max_chars", 6000, 2048, 20000)
        if not topic and not path_prefix:
            raise ProtocolFailure(
                -32602, "topic or path_prefix is required")
        try:
            route_payload = json.loads(
                (self.root / "generated/route-index.v1.json").read_text(
                    encoding="utf-8"))
            db, manifest = self.open_snapshot()
            db.close()
        except (OSError, json.JSONDecodeError, section_search.SearchError):
            return self.tool_error(
                "not-available", "Outline is not available",
                tool="tycho_outline")
        if route_payload.get("snapshot_sha256") != (
                manifest.get("route_snapshot_sha256")):
            return self.tool_error(
                "snapshot-mismatch", "Route metadata and index differ",
                tool="tycho_outline")
        documents = route_payload.get("documents") or []
        if topic:
            routed = route_index.route(
                route_payload, topic, kind=kind, limit=limit * 4)
            paths = [item["path"] for item in routed.get("results", [])]
            by_path = {
                document["path"]: document
                for document in documents
                if isinstance(document, dict) and "path" in document
            }
            selected = [by_path[path] for path in paths if path in by_path]
        else:
            selected = [
                document for document in documents
                if isinstance(document, dict)
                and (kind is None or document.get("kind") == kind)
                and document.get("path", "").startswith(path_prefix)
            ]
            selected.sort(key=lambda item: item["path"])
        selected = selected[:limit]
        entries = []
        for order, document in enumerate(selected, start=1):
            entries.append({
                "order": order,
                "citation": document["path"],
                "path": document["path"],
                "title": document.get("title"),
                "kind": document.get("kind"),
                "summary": document.get("summary"),
                "questions": (document.get("questions") or [])[:3],
                "evidence_status": document.get("evidence_status"),
            })
        response = {
            "status": "ok" if entries else "no-results",
            "snapshot": manifest.get("snapshot_id"),
            "route_snapshot": route_payload.get("snapshot_sha256"),
            "topic": topic,
            "path_prefix": path_prefix,
            "kind": kind,
            "entries": entries,
            "returned": len(entries),
            "max_chars": max_chars,
            "returned_chars": 0,
            "truncated": False,
            "gaps": [] if entries else [
                "No canonical documents matched the outline request."],
            "notice": (
                "Outline only. It is not a completeness claim; read each "
                "cited page before drawing conclusions."),
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_outline",
        }
        def encoded_size():
            return len(json.dumps(
                response, ensure_ascii=False,
                separators=(",", ":")).encode("utf-8"))
        while encoded_size() > max_chars and response["entries"]:
            response["entries"].pop()
            response["returned"] = len(response["entries"])
            response["truncated"] = True
        response["returned_chars"] = encoded_size()
        return response

    def _tool_compare(self, args):
        reject_unknown(args, {
            "options", "limit", "max_chars", "snapshot_id",
        })
        options = args.get("options")
        if (not isinstance(options, list) or not 2 <= len(options) <= 5):
            raise ProtocolFailure(
                -32602, "options must be an array of 2..5 strings")
        if any(not isinstance(value, str) or not value.strip()
               or len(value) > 300 for value in options):
            raise ProtocolFailure(
                -32602, "options must be non-empty strings <=300 characters")
        if len(set(options)) != len(options):
            raise ProtocolFailure(-32602, "options must be unique")
        limit = arg_int(args, "limit", 3, 1, 5)
        max_chars = arg_int(args, "max_chars", 6000, 2048, 12000)
        requested = arg_snapshot(args)
        cells = []
        uncertainties = []
        snapshot = None
        for option in options:
            try:
                found = section_search.search(
                    self.root,
                    option,
                    limit=limit,
                    index_path=self.index_path,
                    abstain=False,
                    detail="snippets",
                )
            except section_search.SearchError as exc:
                return self.search_error(exc, "tycho_compare")
            except (OSError, sqlite3.Error, ValueError):
                return self.tool_error(
                    "not-available", "Comparison is not available",
                    tool="tycho_compare")
            if snapshot is None:
                snapshot = found.get("snapshot")
            mismatch = self.check_snapshot(requested, found.get("snapshot"))
            if mismatch is not None:
                mismatch["tool"] = "tycho_compare"
                return mismatch
            assessment = found.get("answerability") or {}
            confident = assessment.get("confident") is True
            results = found.get("results") or []
            if not results:
                uncertainties.append(
                    "No section matched the option: " + option)
            elif not confident:
                uncertainties.append(
                    "Policy not confident for option: " + option +
                    "; cells are exploratory.")
            for item in results:
                text = " ".join(str(item.get(key, "")) for key in (
                    "heading", "title", "excerpt")).casefold()
                if any(token in text for token in (
                        "trade-off", "tradeoff", "cost ")):
                    dimension = "tradeoff"
                elif any(token in text for token in (
                        "failure", "fail", "retry", "timeout", "error")):
                    dimension = "failure"
                elif any(token in text for token in (
                        "decision", "choose", "selection")):
                    dimension = "decision"
                elif any(token in text for token in (
                        "example", "walkthrough", "case study")):
                    dimension = "example"
                elif item.get("heading_level") == 1:
                    dimension = "overview"
                else:
                    dimension = "evidence"
                cells.append({
                    "option": option,
                    "dimension": dimension,
                    "citation": item.get("citation"),
                    "section_key": item.get("section_key"),
                    "path": item.get("path"),
                    "heading": item.get("heading"),
                    "excerpt": item.get("excerpt"),
                    "evidence_status": item.get("evidence_status"),
                    "weak": not confident,
                })
        response = {
            "status": "ok" if cells else "no-results",
            "snapshot": snapshot,
            "options": options,
            "dimensions": sorted({cell["dimension"] for cell in cells}),
            "cells": cells,
            "uncertainties": uncertainties,
            "notice": (
                "Extractive comparison only. No winner, recommendation or "
                "final verdict is produced; verify every cited cell."),
            "max_chars": max_chars,
            "returned_chars": 0,
            "returned_cells": len(cells),
            "truncated": False,
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_compare",
        }
        def encoded_size():
            return len(json.dumps(
                response, ensure_ascii=False,
                separators=(",", ":")).encode("utf-8"))
        while encoded_size() > max_chars and response["cells"]:
            response["cells"].pop()
            response["returned_cells"] = len(response["cells"])
            response["truncated"] = True
        response["returned_chars"] = encoded_size()
        return response

    def _tool_context(self, args):
        reject_unknown(args, {
            "question", "limit", "max_chars", "kind", "topic",
            "evidence_status", "path_prefix", "include_evidence",
            "snapshot_id",
        })
        question = arg_string(
            args, "question", required=True, maximum=2000)
        limit = arg_int(args, "limit", 5, 1, 8)
        max_chars = arg_int(args, "max_chars", 6000, 2048, 20000)
        kind = arg_string(args, "kind", maximum=300)
        topic = arg_string(args, "topic", maximum=300)
        evidence_status = arg_string(
            args, "evidence_status", maximum=300)
        path_prefix = arg_string(args, "path_prefix", maximum=500)
        include_evidence = arg_bool(args, "include_evidence", False)
        requested = arg_snapshot(args)
        try:
            found = section_search.search(
                self.root,
                question,
                limit=limit,
                kind=kind,
                topic=topic,
                evidence_status=evidence_status,
                path_prefix=path_prefix,
                index_path=self.index_path,
                abstain=True,
                include_weak=True,
                detail="snippets",
            )
        except section_search.SearchError as exc:
            return self.search_error(exc, "tycho_context")
        except (OSError, sqlite3.Error, ValueError):
            return self.tool_error(
                "not-available", "Context is not available",
                tool="tycho_context")
        mismatch = self.check_snapshot(requested, found.get("snapshot"))
        if mismatch is not None:
            mismatch["tool"] = "tycho_context"
            return mismatch
        items = found.get("results") or found.get("weak_results") or []
        exploratory = found.get("status") == "no-confident-answer"
        sections = []
        gaps = []
        for item in items:
            text = " ".join(str(item.get(key, "")) for key in (
                "heading", "title", "excerpt")).casefold()
            if any(token in text for token in (
                    "trade-off", "tradeoff", "trade off", "cost ")):
                role = "tradeoff"
            elif any(token in text for token in (
                    "failure", "fail", "retry", "timeout", "error")):
                role = "failure"
            elif any(token in text for token in (
                    "decision", "choose", "selection", "select ")):
                role = "decision"
            elif any(token in text for token in (
                    "example", "walkthrough", "case study")):
                role = "example"
            elif (item.get("heading_level") == 1
                  or "overview" in text):
                role = "overview"
            else:
                role = "evidence"
            section = {
                "role": role,
                "citation": item.get("citation"),
                "section_key": item.get("section_key"),
                "path": item.get("path"),
                "heading": item.get("heading"),
                "title": item.get("title"),
                "evidence_status": item.get("evidence_status"),
                "excerpt": item.get("excerpt"),
                "why": item.get("why"),
                "weak": bool(exploratory),
                "next_actions": item.get("next_actions") or [],
            }
            if include_evidence and item.get("document_id"):
                try:
                    metadata = section_search.evidence(
                        self.root,
                        document_id=item["document_id"],
                        index_path=self.index_path,
                    )
                except (section_search.SearchError, OSError,
                        sqlite3.Error, ValueError, RuntimeError):
                    gaps.append(
                        "Registered evidence metadata was unavailable for " +
                        str(item.get("citation")))
                else:
                    section["evidence"] = {
                        key: metadata[key]
                        for key in (
                            "status", "claims", "sources",
                            "contradictions")
                        if key in metadata
                    }
            sections.append(section)
        assessment = found.get("answerability") or {}
        if not sections:
            gaps.append("No candidate sections were found for this question.")
        if exploratory:
            gaps.append(
                "The calibrated policy found no confident answer; sections "
                "are exploratory evidence, not an answer.")
        features = assessment.get("features") or {}
        unknown = features.get("unknown")
        if isinstance(unknown, (int, float)) and unknown > 0:
            gaps.append(
                "Some query terms are absent from the indexed vocabulary; "
                "treat coverage as incomplete.")
        next_actions = []
        for section in sections:
            next_actions = section.get("next_actions") or []
            if next_actions:
                break
        response = {
            "status": found.get("status"),
            "snapshot": found.get("snapshot"),
            "coverage": found.get("coverage"),
            "question": question,
            "limit": limit,
            "max_chars": max_chars,
            "answerability": assessment,
            "sections": sections,
            "gaps": gaps,
            "next_actions": next_actions,
            "notice": (
                "Extractive context only. No final answer, recommendation "
                "or verdict is produced; verify citations before use."),
            "returned_chars": 0,
            "truncated": False,
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_context",
        }
        def encoded_size():
            return len(json.dumps(
                response, ensure_ascii=False,
                separators=(",", ":")).encode("utf-8"))
        while encoded_size() > max_chars and response["sections"]:
            response["sections"].pop()
            response["truncated"] = True
        response["returned_chars"] = encoded_size()
        response["returned_sections"] = len(response["sections"])
        return response
