"""MCP bounded section and page read handlers."""
from mcp_runtime import *  # noqa: F401,F403


class ReadToolsMixin:
    def _tool_read(self, args):
        reject_unknown(args, {
            "section_key", "offset", "budget_chars", "include_evidence",
            "snapshot_id",
        })
        section_key = arg_string(
            args, "section_key", required=True, maximum=500)
        offset = arg_int(args, "offset", 0, 0, 10 ** 9)
        budget = arg_int(
            args, "budget_chars", DEFAULT_BUDGET, 1, MAX_BUDGET)
        include_evidence = arg_bool(args, "include_evidence", False)
        requested = arg_snapshot(args)
        try:
            payload = section_search.read(
                self.root,
                section_key,
                offset=offset,
                budget_chars=budget,
                index_path=self.index_path,
                include_evidence=include_evidence,
            )
        except section_search.SearchError as exc:
            return self.search_error(exc, "tycho_read")
        except (OSError, sqlite3.Error, ValueError):
            return self.tool_error(
                "not-available", "Read is not available", tool="tycho_read")
        mismatch = self.check_snapshot(requested, payload.get("snapshot"))
        if mismatch is not None:
            mismatch["tool"] = "tycho_read"
            return mismatch
        payload["anchor"] = payload.get("section_id")
        payload["frontmatter"] = read_frontmatter(self.root, payload.get("path"))
        payload["related"] = resolve_related(
            self.root, related_ids(payload["frontmatter"]))
        payload["content_trust"] = CONTENT_TRUST
        payload["tool"] = "tycho_read"
        return payload

    def _tool_page(self, args):
        reject_unknown(args, {
            "path", "offset", "budget_chars", "include_evidence",
            "snapshot_id",
        })
        path = arg_string(args, "path", required=True, maximum=500)
        offset = arg_int(args, "offset", 0, 0, 10 ** 9)
        budget = arg_int(
            args, "budget_chars", DEFAULT_BUDGET, 1, MAX_BUDGET)
        include_evidence = arg_bool(args, "include_evidence", False)
        requested = arg_snapshot(args)
        self.validate_page_path(path)
        try:
            db, manifest = self.open_snapshot()
        except section_search.SearchError as exc:
            return self.search_error(exc, "tycho_page")
        try:
            mismatch = self.check_snapshot(requested, manifest["snapshot_id"])
            if mismatch is not None:
                mismatch["tool"] = "tycho_page"
                return mismatch
            rows = db.execute(
                "SELECT section_key,document_id,section_id,path,heading,"
                "heading_level,title,kind,evidence_status,content,char_start,"
                "char_end,document_sha256 FROM sections WHERE path = ? "
                "ORDER BY char_start", (path,)).fetchall()
            if not rows:
                return self.tool_error(
                    "not-found",
                    "No indexed page at " + path,
                    path=path,
                    tool="tycho_page",
                )
            return self.page_payload(
                rows, manifest, path, offset, budget, include_evidence)
        finally:
            db.close()

    def page_payload(self, rows, manifest, path, offset, budget,
                     include_evidence):
        document_id = rows[0]["document_id"]
        if any(row["document_id"] != document_id for row in rows):
            return self.tool_error(
                "not-available",
                "Page sections do not share one document identity",
                path=path,
                tool="tycho_page",
            )
        digest = rows[0]["document_sha256"]
        if any(row["document_sha256"] != digest for row in rows):
            return self.tool_error(
                "not-available",
                "Page sections do not share one document hash",
                path=path,
                tool="tycho_page",
            )
        source = self.root / path
        try:
            book_root = (self.root / "book").resolve()
            resolved = source.resolve()
            if (source.is_symlink() or not source.is_file()
                    or not resolved.is_relative_to(book_root)):
                return self.tool_error(
                    "not-available",
                    "Indexed page is missing or unsafe",
                    path=path,
                    tool="tycho_page",
                )
            text = source.read_text(encoding="utf-8")
        except (OSError, RuntimeError, ValueError):
            return self.tool_error(
                "not-available", "Indexed page is unreadable",
                path=path, tool="tycho_page")
        actual = hashlib.sha256(text.encode("utf-8")).hexdigest()
        expected = manifest["document_sha256"].get(document_id)
        if actual != digest or actual != expected:
            return self.tool_error(
                "snapshot-mismatch",
                "Document changed after the snapshot was published",
                path=path,
                tool="tycho_page",
            )
        for previous, current in zip(rows, rows[1:]):
            if previous["char_end"] != current["char_start"]:
                return self.tool_error(
                    "not-available",
                    "Page sections are not contiguous",
                    path=path,
                    tool="tycho_page",
                )
        page_start = rows[0]["char_start"]
        page_end = rows[-1]["char_end"]
        page_text = "".join(row["content"] for row in rows)
        if text[page_start:page_end] != page_text:
            return self.tool_error(
                "not-available",
                "Page sections do not reconstruct the canonical bytes",
                path=path,
                tool="tycho_page",
            )
        total = len(page_text)
        try:
            slice_info = section_search.paginate_text(
                page_text, offset, budget)
        except section_search.SearchError as exc:
            if getattr(exc, "status", "") == "offset-out-of-range":
                raise ProtocolFailure(-32602, str(exc))
            return self.tool_error(
                getattr(exc, "status", "invalid-request"), str(exc),
                tool="tycho_page", offset=offset, total_chars=total)
        end = slice_info["end"]
        sections = []
        for row in rows:
            sections.append({
                "section_key": row["section_key"],
                "section_id": row["section_id"],
                "heading": row["heading"],
                "heading_level": row["heading_level"],
                "title": row["title"],
                "body_offset_start": row["char_start"] - page_start,
                "body_offset_end": row["char_end"] - page_start,
                "citation": row["path"] + "#" + row["section_id"],
            })
        payload = {
            "status": "ok",
            "snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"],
            "document_id": document_id,
            "path": path,
            "title": rows[0]["title"],
            "kind": rows[0]["kind"],
            "evidence_status": rows[0]["evidence_status"],
            "citation": path,
            "citation_scheme": section_search.CITATION_SCHEME,
            "document_sha256": digest,
            "page_char_start": page_start,
            "page_char_end": page_end,
            "offset": offset,
            "returned_chars": end - offset,
            "budget_requested_chars": budget,
            "budget_overrun_chars": slice_info["overrun"],
            "diagram_completed": slice_info["diagram_completed"],
            "total_chars": total,
            "next_offset": end if end < total else None,
            "truncated": end < total,
            "content": page_text[offset:end],
            "sections": sections,
            "frontmatter": read_frontmatter(self.root, path),
            "related": resolve_related(
                self.root, related_ids(read_frontmatter(self.root, path))),
            "content_trust": CONTENT_TRUST,
            "tool": "tycho_page",
        }
        if include_evidence:
            try:
                import section_evidence
                payload["evidence"] = section_evidence.resolve_document(
                    section_evidence.build_store(), document_id)
            except (ImportError, OSError, ValueError, RuntimeError):
                payload["evidence"] = {
                    "status": "not-available",
                    "error": "Evidence is not available",
                }
        return payload

    @staticmethod
    def validate_page_path(path):
        if path.startswith("/") or "\\" in path:
            raise ProtocolFailure(
                -32602, "path must be a relative book path")
        parts = path.split("/")
        if ".." in parts or "." in parts or "" in parts:
            raise ProtocolFailure(
                -32602, "path must not contain traversal or empty segments")
        if not path.startswith("book/") or not path.endswith(".md"):
            raise ProtocolFailure(
                -32602, "path must be a canonical Markdown path under book/")
