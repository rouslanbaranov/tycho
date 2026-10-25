#!/usr/bin/env python3
"""Snapshot-bound ranked search and bounded reads over the section FTS5 index.

The canonical book and its metadata remain authoritative. This module only reads
a published section index and the book bytes it pins. It never writes the book,
the index, source evidence or another provider's data.

H2 sections remain the public result and citation unit. Internal H3 passages are
matched in a separate FTS table and mapped to their parent H2. A passage can
select a better parent section within the same document, while cross-document
order stays anchored to parent-H2 scores. Passage diagnostics never replace the
parent section key, content or citation.

Every query first recomputes the route snapshot and refuses a stale index. The
deep structural verifier remains section_fts_index.py check; search performs a
quick integrity/count check and the route-snapshot comparison.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import sys

import answerability as answerability_policy
import evidence_gate
import route_index
import section_fts_index

ROOT = Path(__file__).resolve().parents[1]
RANKER_VERSION = "tycho-section-fts5-bm25-v5"
CITATION_SCHEME = "tycho.section-key.v2"
PASSAGE_SCORE_WEIGHT = 1.0
SECTION_SEARCH_COLUMNS = (
    "section_key", "document_id", "section_id", "path", "heading",
    "heading_level", "title", "kind", "evidence_status", "char_start",
    "char_end", "content",
)
TOKEN = section_fts_index.TOKEN


def bm25_weights():
    raw = os.environ.get("TYCHO_BM25_WEIGHTS", "5,2,0.25")
    try:
        values = tuple(float(part) for part in raw.split(","))
    except ValueError as exc:
        raise SearchError("TYCHO_BM25_WEIGHTS must be three numbers") from exc
    if len(values) != 3 or any(value <= 0 for value in values):
        raise SearchError("TYCHO_BM25_WEIGHTS must be three positive numbers")
    return values


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
        passages = db.execute("SELECT count(*) FROM passages").fetchone()[0]
        passage_fts = db.execute(
            "SELECT count(*) FROM passage_fts").fetchone()[0]
        _require(sections == fts == manifest["section_count"],
                 "Section index row counts diverge", "not-available")
        _require(passages == passage_fts == manifest["passage_count"],
                 "H3 passage index row counts diverge", "not-available")
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


def unknown_term_rate(db, terms):
    """Fraction of normalized terms absent from the published FTS vocabulary."""
    try:
        db.execute("CREATE VIRTUAL TABLE temp.vocabulary USING "
                   "fts5vocab(main, fts, 'row')")
        vocabulary = {row[0] for row in
                      db.execute("SELECT term FROM vocabulary")}
    except sqlite3.DatabaseError:
        return 0.0
    return sum(1 for term in terms if term not in vocabulary) / len(terms)


def sections_select(alias="s"):
    return ",".join(alias + "." + column for column in SECTION_SEARCH_COLUMNS)


def load_sections(db, keys):
    """Load public parent rows for keys that an H3 candidate introduced."""
    rows = {}
    ordered = sorted(set(keys))
    for start in range(0, len(ordered), 500):
        chunk = ordered[start:start + 500]
        sql = ("SELECT " + sections_select() + " FROM sections s"
               " WHERE s.section_key IN (" + ",".join("?" * len(chunk)) + ")")
        for row in db.execute(sql, chunk):
            rows[row["section_key"]] = row
    return rows


def candidate_priority(candidate):
    """Choose the public parent score and whether an H3 passage supplied it."""
    h2_score = candidate["h2_score"]
    passage = candidate["passage"]
    if passage is None:
        return h2_score, "parent-h2", None
    passage_score = -passage["rank"]
    if h2_score is None or passage_score * PASSAGE_SCORE_WEIGHT > h2_score:
        return passage_score * PASSAGE_SCORE_WEIGHT, "h3-passage", passage_score
    return h2_score, "parent-h2", passage_score


def search(root, query, limit=5, kind=None, topic=None, evidence_status=None,
           path_prefix=None, index_path=None, all_sections=False, abstain=True,
           include_weak=False, detail="snippets", max_chars=None):
    terms = normalize_terms(query)
    _require(isinstance(limit, int) and 1 <= limit <= 20,
             "limit must be an integer in 1..20")
    _require(isinstance(all_sections, bool), "all_sections must be boolean")
    _require(isinstance(abstain, bool), "abstain must be boolean")
    _require(isinstance(include_weak, bool), "include_weak must be boolean")
    _require(detail in ("ids", "snippets"), "detail must be ids or snippets")
    _require(max_chars is None or (
        isinstance(max_chars, int) and not isinstance(max_chars, bool)
        and max_chars >= 256), "max_chars must be null or an integer >= 256")
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
        weight_sql = ",".join(f"{value:g}" for value in bm25_weights())
        sql = ("SELECT " + sections_select() + ",bm25(fts,0.0," + weight_sql
               + ") AS rank"
               " FROM fts JOIN sections s ON s.section_key = fts.section_key"
               " WHERE fts MATCH ?")
        if filters:
            sql += " AND " + " AND ".join(filters)
        sql += " ORDER BY rank ASC, s.section_key ASC LIMIT ?"
        mode = "any-terms"
        fetch = min(max(limit * 10, 50), 200)
        rows = db.execute(
            sql, [match_expression(terms)] + params + [fetch]).fetchall()
        candidates = {}
        for row in rows:
            candidates[row["section_key"]] = {
                "section_key": row["section_key"],
                "row": row,
                "h2_score": -row["rank"],
                "passage": None,
            }
        passage_sql = (
            "SELECT p.passage_key,p.passage_id,p.parent_section_key,"
            "p.parent_section_id,p.document_id,p.path,p.heading,"
            "p.heading_level,p.title,p.content,p.body,p.char_start,p.char_end,"
            "bm25(passage_fts,0.0," + weight_sql + ") AS rank"
            " FROM passage_fts JOIN passages p"
            " ON p.passage_key = passage_fts.passage_key"
            " JOIN sections s ON s.section_key = p.parent_section_key"
            " WHERE passage_fts MATCH ?")
        if filters:
            passage_sql += " AND " + " AND ".join(filters)
        passage_sql += " ORDER BY rank ASC, p.passage_key ASC LIMIT ?"
        passage_fetch = min(max(limit * 20, 100), 500)
        passage_rows = db.execute(
            passage_sql,
            [match_expression(terms)] + params + [passage_fetch]).fetchall()
        best_passages = {}
        for passage in passage_rows:
            key = passage["parent_section_key"]
            current = best_passages.get(key)
            if current is None or passage["rank"] < current["rank"]:
                best_passages[key] = passage
        missing = [key for key in best_passages if key not in candidates]
        for key, row in load_sections(db, missing).items():
            candidates[key] = {
                "section_key": key,
                "row": row,
                "h2_score": None,
                "passage": None,
            }
        for key, passage in best_passages.items():
            if key in candidates:
                candidates[key]["passage"] = passage
        ordered = []
        for candidate in candidates.values():
            score, source, passage_score = candidate_priority(candidate)
            ordered.append((score, source, passage_score, candidate))
        ordered.sort(key=lambda item: (
            -item[0], item[3]["row"]["section_key"]))
        if all_sections:
            selected = ordered[:limit]
            truncated = len(ordered) > limit
        else:
            h2_candidates = [candidate for candidate in candidates.values()
                             if candidate["h2_score"] is not None]
            h2_candidates.sort(key=lambda candidate: (
                -candidate["h2_score"],
                candidate["row"]["section_key"]))
            grouped = {}
            for candidate in h2_candidates:
                grouped.setdefault(
                    candidate["row"]["document_id"], []).append(candidate)
            extra = [candidate for candidate in candidates.values()
                     if candidate["row"]["document_id"] not in grouped]
            extra.sort(key=lambda candidate:
                       -candidate_priority(candidate)[0])
            for candidate in extra:
                grouped.setdefault(
                    candidate["row"]["document_id"], []).append(candidate)
            selected = []
            for group in grouped.values():
                best = max(group, key=lambda candidate:
                           candidate_priority(candidate)[0])
                score, source, passage_score = candidate_priority(best)
                selected.append((score, source, passage_score, best))
                if len(selected) == limit + 1:
                    break
            truncated = len(selected) > limit
            selected = selected[:limit]
        results = []
        for score, source, passage_score, candidate in selected:
            row = candidate["row"]
            content = row["content"]
            folded = content.casefold()
            body = content
            if row["heading_level"] == 2:
                body = content.partition("\n")[2] or content
                if not any(term in body.casefold() for term in terms):
                    body = content
            item = {
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
                "score": round(score, 6),
                "score_kind": "bm25",
                "matched_terms": [term for term in terms if term in folded],
                "excerpt": excerpt(body, terms),
                "citation": row["path"] + "#" + row["section_id"],
                "match_source": source,
                "why": (
                    "matched in " + source +
                    " for terms: " + ", ".join(
                        term for term in terms if term in folded)),
                "next_actions": [
                    {"tool": "tycho_read",
                     "arguments": {"section_key": row["section_key"]}},
                    {"tool": "tycho_page",
                     "arguments": {"path": row["path"]}},
                ],
            }
            passage = candidate["passage"]
            if passage is not None:
                item.update({
                    "matched_passage_id": passage["passage_id"],
                    "matched_passage_key": passage["passage_key"],
                    "matched_passage_heading": passage["heading"],
                    "matched_passage_score": round(passage_score, 6),
                    "matched_passage_char_start": passage["char_start"],
                    "matched_passage_char_end": passage["char_end"],
                    "matched_passage_excerpt": excerpt(
                        passage["body"] or passage["content"], terms),
                })
            results.append(item)
        unknown = unknown_term_rate(db, terms)
        assessment = evidence_gate.assess(query, results, unknown)
        if assessment is None:
            assessment = answerability_policy.assess(
                query, results[0]["score"] if results else 0, unknown)
        if not results:
            status = "no-results"
            assessment = dict(assessment)
            assessment["no_confident_answer"] = True
            assessment["confident"] = False
            assessment["state"] = "no-results"
            assessment["basis"] = "zero-results"
        elif abstain and assessment["no_confident_answer"]:
            status = "no-confident-answer"
            results = []
            truncated = False
        else:
            status = "ok"
        returned = len(results)
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
            "returned": returned,
            "truncated": truncated,
            "answerability": assessment,
            "results": results,
        }
    finally:
        db.close()


def read(root, section_key, offset=0, budget_chars=2000, index_path=None,
         include_evidence=False):
    _require(isinstance(section_key, str) and section_key.strip(),
             "section_key must be a non-empty string")
    _require(isinstance(include_evidence, bool),
             "include_evidence must be boolean")
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
        payload = {
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
        if include_evidence:
            import section_evidence
            payload["evidence"] = section_evidence.resolve_document(
                section_evidence.build_store(), row["document_id"])
        return payload
    finally:
        db.close()


def evidence(root, document_id=None, claim_id=None, source_id=None,
             index_path=None, expected_evidence_snapshot=None):
    """Resolve evidence for a section-search result through the current index."""
    provided = [value for value in (document_id, claim_id, source_id)
                if value is not None]
    _require(len(provided) == 1,
             "provide exactly one of document_id, claim_id or source_id")
    db, manifest = open_snapshot(root, index_path)
    db.close()
    import section_evidence
    store = section_evidence.build_store()
    if document_id is not None:
        payload = section_evidence.resolve_document(
            store, document_id, expected_evidence_snapshot)
    elif claim_id is not None:
        payload = section_evidence.resolve_claim(
            store, claim_id, expected_evidence_snapshot)
    else:
        payload = section_evidence.resolve_source(
            store, source_id, expected_evidence_snapshot)
    payload["search_snapshot"] = manifest["snapshot_id"]
    payload["search_route_snapshot"] = manifest["route_snapshot_sha256"]
    return payload


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("search", "read", "evidence"))
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
    ap.add_argument("--include-evidence", action="store_true")
    ap.add_argument("--document")
    ap.add_argument("--claim")
    ap.add_argument("--source")
    ap.add_argument("--expected-evidence-snapshot")
    args = ap.parse_args(argv)
    try:
        if args.action == "search":
            payload = search(
                args.root, args.query or "", limit=args.limit, kind=args.kind,
                topic=args.topic, evidence_status=args.evidence_status,
                path_prefix=args.path_prefix, index_path=args.index,
                all_sections=args.all_sections)
        elif args.action == "read":
            payload = read(
                args.root, args.id or "", offset=args.offset,
                budget_chars=args.budget_chars, index_path=args.index,
                include_evidence=args.include_evidence)
        else:
            payload = evidence(
                args.root, document_id=args.document, claim_id=args.claim,
                source_id=args.source, index_path=args.index,
                expected_evidence_snapshot=args.expected_evidence_snapshot)
    except ValueError as exc:
        print(json.dumps({"status": getattr(exc, "status", "invalid-request"),
                          "error": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
