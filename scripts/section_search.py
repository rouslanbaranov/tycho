#!/usr/bin/env python3
"""Snapshot-bound ranked search and bounded reads over the section FTS5 index.

The canonical book and its metadata remain authoritative. This module only reads
a published section index and the book bytes it pins. It never writes the book,
the index, source evidence or another provider's data.

Every query first recomputes the route snapshot and refuses a stale index. The
deep structural verifier remains section_fts_index.py check; search performs a
quick integrity/count check and the route-snapshot comparison.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys

import route_index
import section_fts_index

ROOT = Path(__file__).resolve().parents[1]
RANKER_VERSION = "tycho-section-fts5-bm25-v3"
CITATION_SCHEME = "tycho.section-key.v2"
TOKEN = section_fts_index.TOKEN


class SearchError(ValueError):
    """A bounded, machine-readable retrieval failure."""

    def __init__(self, message, status="invalid-request"):
        super().__init__(message)
        self.status = status


class SnapshotMismatch(SearchError):
    def __init__(self, message):
        super().__init__(message, "snapshot-mismatch")


def _require(value, message, status="invalid-request"):
    if not value:
        raise SearchError(message, status)


def normalize_terms(query):
    _require(isinstance(query, str) and query.strip(), "query must be a non-empty string")
    terms = []
    for token in TOKEN.findall(query.casefold()):
        if token not in terms:
            terms.append(token)
    _require(terms, "query has no searchable terms")
    return terms


def match_expression(terms):
    return " OR ".join('"' + term + '"' for term in terms)


def open_snapshot(root, index_path=None):
    """Open a published index and refuse it unless it matches the current book."""
    root = Path(root).resolve()
    target = section_fts_index.output_path(root, index_path)
    if not target.is_file() or target.is_symlink():
        raise SearchError(
            "No published section index; run section_fts_index.py build first",
            "not-available")
    try:
        db = sqlite3.connect("file:" + target.as_posix() + "?mode=ro", uri=True)
    except sqlite3.DatabaseError as exc:
        raise SearchError("Section index cannot be opened", "not-available") from exc
    db.row_factory = sqlite3.Row
    try:
        _require(db.execute("PRAGMA quick_check").fetchone()[0] == "ok",
                 "Section index failed quick integrity check", "not-available")
        row = db.execute(
            "SELECT value FROM meta WHERE key='manifest'").fetchone()
        _require(row is not None, "Section index has no manifest", "not-available")
        manifest = json.loads(row[0])
        _require(manifest.get("format_version") == section_fts_index.VERSION,
                 "Section index format is incompatible", "not-available")
        _require(set(manifest) == section_fts_index.MANIFEST_KEYS,
                 "Section index manifest is malformed", "not-available")
        sections = db.execute("SELECT count(*) FROM sections").fetchone()[0]
        fts = db.execute("SELECT count(*) FROM fts").fetchone()[0]
        _require(sections == fts == manifest["section_count"],
                 "Section index row counts diverge", "not-available")
        scan = route_index.canonical_scan(root, allow_partial=True)
        if scan["snapshot_sha256"] != manifest["route_snapshot_sha256"]:
            raise SnapshotMismatch(
                "Section index snapshot does not match the current book; rebuild it")
    except (sqlite3.DatabaseError, ValueError, TypeError, KeyError) as exc:
        db.close()
        if isinstance(exc, SearchError):
            raise
        raise SearchError("Section index is unreadable or malformed",
                          "not-available") from exc
    return db, manifest


def path_prefix_pattern(value):
    _require(isinstance(value, str) and value,
             "path_prefix must be a non-empty string")
    _require(not value.startswith("/") and "\\" not in value
             and ".." not in value.split("/"),
             "path_prefix must be a relative book path")
    _require(value == "book" or value.startswith("book/"),
             "path_prefix must stay under book/")
    escaped = value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    return escaped + "%"


def excerpt(content, terms, budget=240):
    folded = content.casefold()
    positions = [pos for pos in (folded.find(term) for term in terms) if pos >= 0]
    if positions:
        start = max(0, min(positions) - budget // 3)
        end = min(len(content), start + budget)
        if end - start < budget:
            start = max(0, end - budget)
    else:
        start, end = 0, min(len(content), budget)
    text = " ".join(content[start:end].split())
    if start > 0:
        text = "…" + text
    if end < len(content):
        text = text + "…"
    return text


def search(root, query, limit=5, kind=None, topic=None, evidence_status=None,
           path_prefix=None, index_path=None, all_sections=False):
    terms = normalize_terms(query)
    _require(isinstance(limit, int) and 1 <= limit <= 20,
             "limit must be an integer in 1..20")
    _require(isinstance(all_sections, bool), "all_sections must be boolean")
    for name, value in (("kind", kind), ("topic", topic),
                        ("evidence_status", evidence_status)):
        _require(value is None or (isinstance(value, str) and value),
                 name + " filter must be a non-empty string")
    prefix = None if path_prefix is None else path_prefix_pattern(path_prefix)
    db, manifest = open_snapshot(root, index_path)
    try:
        filters, params = [], []
        if kind is not None:
            filters.append("s.kind = ?")
            params.append(kind)
        if evidence_status is not None:
            filters.append("s.evidence_status = ?")
            params.append(evidence_status)
        if prefix is not None:
            filters.append("s.path LIKE ? ESCAPE '\\'")
            params.append(prefix)
        if topic is not None:
            filters.append("EXISTS (SELECT 1 FROM section_topics t"
                           " WHERE t.section_key = s.section_key AND t.topic = ?)")
            params.append(topic)
        sql = ("SELECT s.section_key,s.document_id,s.section_id,s.path,s.heading,"
               "s.heading_level,s.title,s.kind,s.evidence_status,s.char_start,"
               "s.char_end,s.content,bm25(fts,0.0,4.0,3.0,1.0) AS rank"
               " FROM fts JOIN sections s ON s.section_key = fts.section_key"
               " WHERE fts MATCH ?")
        if filters:
            sql += " AND " + " AND ".join(filters)
        sql += " ORDER BY rank ASC, s.section_key ASC LIMIT ?"
        mode = "any-terms"
        fetch = limit + 1 if all_sections else min(max(limit * 10, 50), 200)
        rows = db.execute(
            sql, [match_expression(terms)] + params + [fetch]).fetchall()
        if all_sections:
            selected = rows[:limit]
            truncated = len(rows) > limit
        else:
            selected = []
            seen = set()
            for row in rows:
                if row["document_id"] in seen:
                    continue
                seen.add(row["document_id"])
                selected.append(row)
                if len(selected) == limit + 1:
                    break
            truncated = len(selected) > limit
            selected = selected[:limit]
        results = []
        for row in selected:
            content = row["content"]
            folded = content.casefold()
            body = content
            if row["heading_level"] == 2:
                body = content.partition("\n")[2] or content
                if not any(term in body.casefold() for term in terms):
                    body = content
            results.append({
                "section_key": row["section_key"],
                "document_id": row["document_id"],
                "section_id": row["section_id"],
                "path": row["path"],
                "heading": row["heading"],
                "heading_level": row["heading_level"],
                "title": row["title"],
                "kind": row["kind"],
                "evidence_status": row["evidence_status"],
                "char_start": row["char_start"],
                "char_end": row["char_end"],
                "score": round(-row["rank"], 6),
                "score_kind": "bm25",
                "matched_terms": [term for term in terms if term in folded],
                "excerpt": excerpt(body, terms),
                "citation": row["path"] + "#" + row["section_id"],
            })
        status = "ok" if results else "no-results"
        return {
            "status": status,
            "snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"],
            "unannotated": len(manifest["unannotated_paths"]),
            "query": query,
            "match_mode": mode,
            "ranker_version": RANKER_VERSION,
            "citation_scheme": CITATION_SCHEME,
            "result_scope": ("all-sections" if all_sections
                             else "best-section-per-document"),
            "filters": {"kind": kind, "topic": topic,
                        "evidence_status": evidence_status,
                        "path_prefix": path_prefix},
            "returned": len(results),
            "truncated": truncated,
            "results": results,
        }
    finally:
        db.close()


def read(root, section_key, offset=0, budget_chars=2000, index_path=None):
    _require(isinstance(section_key, str) and section_key.strip(),
             "section_key must be a non-empty string")
    _require(isinstance(offset, int) and offset >= 0,
             "offset must be a non-negative integer")
    _require(isinstance(budget_chars, int) and 1 <= budget_chars <= 5000,
             "budget_chars must be an integer in 1..5000")
    root = Path(root).resolve()
    db, manifest = open_snapshot(root, index_path)
    try:
        row = db.execute(
            "SELECT section_key,document_id,section_id,path,heading,heading_level,"
            "title,kind,evidence_status,content,char_start,char_end,document_sha256"
            " FROM sections WHERE section_key = ?", (section_key,)).fetchone()
        _require(row is not None, "Unknown section: " + section_key, "not-found")
        relative = row["path"]
        _require(relative.startswith("book/") and ".." not in relative.split("/"),
                 "Indexed path is outside book/", "not-available")
        path = root / relative
        _require(not path.is_symlink() and path.is_file()
                 and path.resolve().is_relative_to((root / "book").resolve()),
                 "Indexed page is missing or unsafe", "not-available")
        text = path.read_text(encoding="utf-8")
        actual = hashlib.sha256(text.encode("utf-8")).hexdigest()
        _require(actual == row["document_sha256"]
                 and actual == manifest["document_sha256"].get(row["document_id"]),
                 "Document changed after the snapshot was published",
                 "snapshot-mismatch")
        content = row["content"]
        _require(offset <= len(content), "offset is beyond the section length")
        end = min(len(content), offset + budget_chars)
        return {
            "status": "ok",
            "snapshot": manifest["snapshot_id"],
            "section_key": row["section_key"],
            "document_id": row["document_id"],
            "section_id": row["section_id"],
            "path": row["path"],
            "heading": row["heading"],
            "heading_level": row["heading_level"],
            "title": row["title"],
            "kind": row["kind"],
            "evidence_status": row["evidence_status"],
            "offset": offset,
            "returned_chars": end - offset,
            "total_chars": len(content),
            "next_offset": end if end < len(content) else None,
            "truncated": end < len(content),
            "document_char_start": row["char_start"] + offset,
            "document_char_end": row["char_start"] + end,
            "document_sha256": row["document_sha256"],
            "citation": row["path"] + "#" + row["section_id"],
            "citation_scheme": CITATION_SCHEME,
            "content": content[offset:end],
        }
    finally:
        db.close()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("search", "read"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--index", type=Path)
    ap.add_argument("--query")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--all-sections", action="store_true",
                    help="Return every matching section instead of the best per page")
    ap.add_argument("--kind")
    ap.add_argument("--topic")
    ap.add_argument("--evidence-status")
    ap.add_argument("--path-prefix")
    ap.add_argument("--id")
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--budget-chars", type=int, default=2000)
    args = ap.parse_args(argv)
    try:
        if args.action == "search":
            payload = search(
                args.root, args.query or "", limit=args.limit, kind=args.kind,
                topic=args.topic, evidence_status=args.evidence_status,
                path_prefix=args.path_prefix, index_path=args.index,
                all_sections=args.all_sections)
        else:
            payload = read(
                args.root, args.id or "", offset=args.offset,
                budget_chars=args.budget_chars, index_path=args.index)
    except SearchError as exc:
        print(json.dumps({"status": exc.status, "error": str(exc)},
                         sort_keys=True))
        return 1
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
