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

Every query validates the persisted index and binds it to the current book.
A process-local snapshot cache reuses a canonical scan only after hashing every
book Markdown document and the metadata schema; any content change forces a full
canonical rescan. The deep structural verifier remains section_fts_index.py
check; search performs a quick integrity/count check and the route-snapshot
comparison.
"""
import argparse
import copy
from collections import OrderedDict
import functools
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import threading

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
    "char_end", "content", "artifact_type", "volume",
)
TOKEN = section_fts_index.TOKEN
_QUERY_CACHE = OrderedDict()
_QUERY_CACHE_LOCK = threading.Lock()
_INDEX_VALIDATION_CACHE = OrderedDict()
_INDEX_VALIDATION_LOCK = threading.Lock()
_INDEX_VALIDATION_MAX = 4
_SEARCH_CONCURRENCY = threading.BoundedSemaphore(2)
_ARTIFACT_STOPWORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "by", "does", "do",
    "for", "from", "how", "in", "is", "it", "of", "on", "or", "that",
    "the", "to", "what", "when", "where", "which", "why", "with",
})
_QUERY_CACHE_MAX = 128


def _query_cache_key(root, snapshot, query, limit, kind, topic,
                     evidence_status, path_prefix, index_path, all_sections,
                     abstain, include_weak, detail, max_chars, artifact_type,
                     volume, pattern_ids, section_rerank,
                     section_rerank_margin):
    return (str(Path(root).resolve()), snapshot, query, limit, kind, topic,
            evidence_status, path_prefix, str(index_path), all_sections,
            abstain, include_weak, detail, max_chars, artifact_type, volume,
            tuple(pattern_ids or ()), section_rerank, section_rerank_margin)


def _cache_get(key):
    with _QUERY_CACHE_LOCK:
        value = _QUERY_CACHE.pop(key, None)
        if value is None:
            return None
        _QUERY_CACHE[key] = value
        return copy.deepcopy(value)


def _cache_put(key, value):
    with _QUERY_CACHE_LOCK:
        _QUERY_CACHE[key] = value
        _QUERY_CACHE.move_to_end(key)
        while len(_QUERY_CACHE) > _QUERY_CACHE_MAX:
            _QUERY_CACHE.popitem(last=False)


def bm25_weights():
    raw = os.environ.get("TYCHO_BM25_WEIGHTS", "5,2,0.5")
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


# Process-local validation cache: exact book/schema bytes -> canonical route
# snapshot. It never spans processes and never replaces the index checks; it only
# avoids reparsing every document when the complete input state is unchanged.
_SNAPSHOT_SCAN_CACHE = {}
_SNAPSHOT_SCAN_CACHE_LIMIT = 4
_SNAPSHOT_SCAN_CACHE_LOCK = threading.Lock()


def _book_state_key(root):
    """Hash every canonical input of route_index.canonical_scan.

    Content hashes, not timestamps, decide reuse. Any changed, added, removed,
    renamed or symlinked Markdown page yields a different key, and so does a
    changed metadata schema. Unsafe paths are left to canonical_scan's stricter
    checks and are not cached.
    """
    root = Path(root).resolve()
    book = root / "book"
    if not book.is_dir() or book.is_symlink():
        raise ValueError("book directory missing or symlink")
    resolved_book = book.resolve()
    digest = hashlib.sha256(b"tycho.snapshot-cache.v1\0")
    for file in sorted(book.rglob("*.md")):
        if file.is_symlink() or not file.resolve().is_relative_to(resolved_book):
            raise ValueError("unsafe book file/symlink")
        text = file.read_text(encoding="utf-8")
        relative = file.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8") + b"\0")
        digest.update(hashlib.sha256(text.encode("utf-8")).digest())
    schema = root / "schemas/document-metadata.v1.schema.json"
    try:
        schema_text = schema.read_text(encoding="utf-8")
    except FileNotFoundError:
        schema_digest = hashlib.sha256(b"missing").digest()
    else:
        schema_digest = hashlib.sha256(schema_text.encode("utf-8")).digest()
    digest.update(b"\0schema\0")
    digest.update(schema_digest)
    return str(root), digest.hexdigest()


def _remember_snapshot_scan(root, key, snapshot_sha256):
    """Replace stale entries for this root and keep the cache bounded."""
    root_key = str(root)
    for existing in [item for item in _SNAPSHOT_SCAN_CACHE
                     if item[0] == root_key]:
        _SNAPSHOT_SCAN_CACHE.pop(existing, None)
    _SNAPSHOT_SCAN_CACHE[key] = snapshot_sha256
    while len(_SNAPSHOT_SCAN_CACHE) > _SNAPSHOT_SCAN_CACHE_LIMIT:
        _SNAPSHOT_SCAN_CACHE.pop(next(iter(_SNAPSHOT_SCAN_CACHE)))


def _current_route_snapshot(root):
    """Return the canonical route snapshot for the current book, cached by bytes.

    A cache hit reuses only a scan produced from the identical book and schema
    bytes. On a miss, canonical_scan runs under a lock so concurrent callers share
    one scan. The post-scan key is checked before caching so a concurrent book
    change cannot bind an old key to a newer scan.
    """
    root = Path(root).resolve()
    try:
        key = _book_state_key(root)
    except (OSError, ValueError):
        key = None
    with _SNAPSHOT_SCAN_CACHE_LOCK:
        if key is not None:
            cached = _SNAPSHOT_SCAN_CACHE.get(key)
            if cached is not None:
                return cached
        scan = route_index.canonical_scan(root, allow_partial=True)
        snapshot = scan["snapshot_sha256"]
        if key is not None:
            try:
                unchanged = _book_state_key(root) == key
            except (OSError, ValueError):
                unchanged = False
            if unchanged:
                _remember_snapshot_scan(root, key, snapshot)
        return snapshot


def open_snapshot(root, index_path=None):
    """Open a published index and refuse it unless it matches the current book."""
    root = Path(root).resolve()
    target = section_fts_index.output_path(root, index_path)
    if not target.is_file() or target.is_symlink():
        raise SearchError(
            "No published section index; run section_fts_index.py build first",
            "not-available")
    stat = target.stat()
    cache_key = (str(target), stat.st_mtime_ns, stat.st_size,
                 getattr(stat, "st_ino", 0))
    with _INDEX_VALIDATION_LOCK:
        cached = _INDEX_VALIDATION_CACHE.get(cache_key)
    try:
        db = sqlite3.connect("file:" + target.as_posix() + "?mode=ro", uri=True)
    except sqlite3.DatabaseError as exc:
        raise SearchError("Section index cannot be opened", "not-available") from exc
    db.row_factory = sqlite3.Row
    if cached is not None:
        try:
            manifest = cached
            current = _current_route_snapshot(root)
            if current != manifest["route_snapshot_sha256"]:
                raise SnapshotMismatch(
                    "Section index snapshot does not match the current book; rebuild it")
            facet_current = section_fts_index.facet_input_sha256(root)
            if facet_current != manifest.get("facet_input_sha256"):
                raise SnapshotMismatch(
                    "Section index V12 facets do not match the current indexes; rebuild it")
        except (sqlite3.DatabaseError, ValueError, TypeError, KeyError) as exc:
            db.close()
            if isinstance(exc, SearchError):
                raise
            raise SearchError("Section index is unreadable or malformed",
                              "not-available") from exc
        return db, manifest
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
        current = _current_route_snapshot(root)
        if current != manifest["route_snapshot_sha256"]:
            raise SnapshotMismatch(
                "Section index snapshot does not match the current book; rebuild it")
        facet_current = section_fts_index.facet_input_sha256(root)
        if facet_current != manifest.get("facet_input_sha256"):
            raise SnapshotMismatch(
                "Section index V12 facets do not match the current indexes; rebuild it")
        with _INDEX_VALIDATION_LOCK:
            _INDEX_VALIDATION_CACHE[cache_key] = manifest
            while len(_INDEX_VALIDATION_CACHE) > _INDEX_VALIDATION_MAX:
                _INDEX_VALIDATION_CACHE.popitem(last=False)
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


_METADATA_CACHE = {}


def load_document_metadata(root):
    path = Path(root) / "generated/route-index.v1.json"
    try:
        stat = path.stat()
    except OSError:
        return {}
    key = (str(path), stat.st_mtime_ns, stat.st_size)
    if key in _METADATA_CACHE:
        return _METADATA_CACHE[key]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    documents = payload.get("documents")
    if not isinstance(documents, list):
        return {}
    metadata = {
        document["path"]: document
        for document in documents
        if isinstance(document, dict) and isinstance(document.get("path"), str)
    }
    if len(_METADATA_CACHE) >= 4:
        _METADATA_CACHE.clear()
    _METADATA_CACHE[key] = metadata
    return metadata


def load_v12_artifacts(root):
    """Load V12 model/scenario/run/decision facets from derived indexes.

    The FTS index covers book pages; V12 artifacts are JSON contracts. This
    lookup keeps them discoverable without pretending they are book sections.
    """
    root = Path(root).resolve()
    index_path = root / "generated/v12-index.v1.json"
    reverse_path = root / "edition/v12/reverse-index.v1.json"
    if not index_path.is_file() or index_path.is_symlink():
        return []
    try:
        payload = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    reverse_patterns = {}
    if reverse_path.is_file() and not reverse_path.is_symlink():
        try:
            reverse = json.loads(reverse_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            reverse = {}
        for pattern_id, entries in (reverse.get("patterns") or {}).items():
            if not isinstance(pattern_id, str):
                continue
            for entry in entries or []:
                path = entry.get("path") if isinstance(entry, dict) else None
                if isinstance(path, str):
                    reverse_patterns.setdefault(path, set()).add(pattern_id)
    artifacts = []
    for document in payload.get("documents", []):
        if not isinstance(document, dict):
            continue
        artifact_type = document.get("artifact_type") or "document"
        if artifact_type == "document":
            continue
        path = document.get("path")
        if not isinstance(path, str):
            continue
        patterns = set(document.get("pattern_ids") or [])
        patterns.update(reverse_patterns.get(path, set()))
        artifacts.append({
            "id": document.get("id"),
            "path": path,
            "title": document.get("title"),
            "artifact_type": artifact_type,
            "volume": document.get("volume") or "v12",
            "evidence_status": document.get("evidence_status") or "unknown",
            "pattern_ids": sorted(patterns),
            "summary": document.get("summary") or "",
            "questions": list(document.get("questions") or []),
            "keywords": list(document.get("keywords") or []),
            "topics": list(document.get("topics") or []),
        })
    artifacts.sort(key=lambda item: (str(item["artifact_type"]), str(item["id"])))
    return artifacts


def v12_artifacts(root, pattern_ids=None, artifact_type=None, volume="v12",
                  limit=50, terms=None):
    """Return V12 artifacts filtered and optionally ranked by query terms."""
    pattern_ids = pattern_ids or []
    _require(isinstance(pattern_ids, (list, tuple)),
             "pattern_ids must be a list")
    for name, value in (("artifact_type", artifact_type), ("volume", volume)):
        _require(value is None or (isinstance(value, str) and value),
                 name + " filter must be a non-empty string")
    for pattern_id in pattern_ids:
        _require(isinstance(pattern_id, str) and pattern_id,
                 "pattern_id filter must be a non-empty string")
    _require(isinstance(limit, int) and 1 <= limit <= 200,
             "artifact limit must be an integer in 1..200")
    artifacts = []
    for item in load_v12_artifacts(root):
        if artifact_type is not None and item["artifact_type"] != artifact_type:
            continue
        if volume is not None and item["volume"] != volume:
            continue
        if pattern_ids and not set(pattern_ids).issubset(set(item["pattern_ids"])):
            continue
        artifacts.append(item)
    if terms:
        artifact_terms = [term for term in set(terms)
                          if term not in _ARTIFACT_STOPWORDS and len(term) > 2]
        scored = []
        for item in artifacts:
            text = " ".join(
                [str(item.get("title") or ""),
                 str(item.get("summary") or ""),
                 " ".join(item.get("questions") or []),
                 " ".join(item.get("keywords") or []),
                 " ".join(item.get("topics") or []),
                 " ".join(item.get("pattern_ids") or [])]).casefold()
            hits = [term for term in artifact_terms if term in text]
            if hits and len(hits) >= min(2, len(artifact_terms)):
                scored.append((len(hits),
                               sum(text.count(term) for term in hits),
                               item))
        scored.sort(key=lambda row: (-row[0], -row[1], str(row[2]["id"])))
        artifacts = [row[2] for row in scored]
    return {
        "status": "ok" if artifacts else "no-results",
        "filters": {
            "pattern_ids": list(pattern_ids),
            "artifact_type": artifact_type,
            "volume": volume,
        },
        "returned": len(artifacts[:limit]),
        "total": len(artifacts),
        "artifacts": artifacts[:limit],
        "scope": (
            "Derived V12 model, scenario, run and decision lookup. "
            "Not a semantic graph and not a source of claim truth."
        ),
    }


def metadata_fallback(db, metadata, query, terms, limit):
    if not metadata:
        return []
    route = route_index.route(
        {"documents": list(metadata.values()),
         "snapshot_sha256": "", "coverage": "metadata-only",
         "unannotated_paths": []},
        query,
        limit=limit,
    )
    results = []
    for candidate in route.get("results", []):
        row = db.execute(
            "SELECT " + sections_select() +
            " FROM sections s WHERE s.path = ?"
            " ORDER BY s.heading_level, s.char_start LIMIT 1",
            (candidate["path"],),
        ).fetchone()
        if row is None:
            continue
        meta = metadata.get(row["path"], {})
        content = row["content"]
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
            "artifact_type": row["artifact_type"],
            "volume": row["volume"],
            "pattern_ids": [],
            "char_start": row["char_start"],
            "char_end": row["char_end"],
            "score": 0.0,
            "score_kind": "route-metadata",
            "matched_terms": [
                term for term in terms if term in content.casefold()],
            "excerpt": excerpt(content, terms) or meta.get("summary", ""),
            "metadata_snippet": meta.get("summary"),
            "route_questions": (meta.get("questions") or [])[:3],
            "route_keywords": (meta.get("keywords") or [])[:8],
            "citation": row["path"] + "#" + row["section_id"],
            "match_source": "route-metadata",
            "why": "metadata route matched the question; no FTS section matched",
            "next_actions": [
                {"tool": "tycho_read",
                 "arguments": {"section_key": row["section_key"]}},
                {"tool": "tycho_page",
                 "arguments": {"path": row["path"]}},
            ],
        })
    return results


def section_rerank_candidates(db, terms, selected, limit, filters, params,
                              weight_sql):
    paths = []
    for _, _, _, candidate in selected:
        path = candidate["row"]["path"]
        if path not in paths:
            paths.append(path)
    if not paths:
        return selected
    placeholders = ",".join("?" * len(paths))
    sql = ("SELECT " + sections_select() + ",bm25(fts,0.0," + weight_sql
           + ") AS rank FROM fts JOIN sections s"
           " ON s.section_key = fts.section_key WHERE fts MATCH ?"
           " AND s.path IN (" + placeholders + ")")
    if filters:
        sql += " AND " + " AND ".join(filters)
    sql += " ORDER BY rank ASC LIMIT ?"
    rows = db.execute(
        sql, [match_expression(terms)] + paths + params
        + [max(limit * 20, 100)]).fetchall()
    scored = []
    for row in rows:
        text = (row["heading"] + " " + row["content"]).casefold()
        hits = sum(1 for term in set(terms) if term in text)
        heading_hits = sum(1 for term in set(terms)
                           if term in row["heading"].casefold())
        score = float(hits * 1000 + heading_hits * 10 - row["rank"])
        candidate = {"section_key": row["section_key"], "row": row,
                     "h2_score": None, "passage": None}
        scored.append((score, "section-rerank", None, candidate))
    scored.sort(key=lambda item: (-item[0], item[3]["row"]["section_key"]))
    return scored[:limit] or selected


def _bounded_search(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        with _SEARCH_CONCURRENCY:
            return function(*args, **kwargs)
    return wrapper


@_bounded_search
def search(root, query, limit=5, kind=None, topic=None, evidence_status=None,
           path_prefix=None, index_path=None, all_sections=False, abstain=True,
           include_weak=False, detail="snippets", max_chars=None,
           artifact_type=None, volume=None, pattern_ids=None,
           include_artifacts=False, section_rerank=False,
           section_rerank_margin=None):
    terms = normalize_terms(query)
    _require(isinstance(limit, int) and 1 <= limit <= 20,
             "limit must be an integer in 1..20")
    _require(isinstance(all_sections, bool), "all_sections must be boolean")
    _require(isinstance(abstain, bool), "abstain must be boolean")
    _require(isinstance(section_rerank, bool),
             "section_rerank must be boolean")
    _require(not (all_sections and section_rerank),
             "section_rerank cannot be combined with all_sections")
    _require(not (section_rerank and volume == "v12"),
             "section_rerank is disabled for volume v12")
    _require(section_rerank_margin is None or (
        isinstance(section_rerank_margin, (int, float))
        and not isinstance(section_rerank_margin, bool)
        and 0 <= section_rerank_margin <= 1),
        "section_rerank_margin must be null or a number in 0..1")
    _require(isinstance(include_weak, bool), "include_weak must be boolean")
    _require(isinstance(include_artifacts, bool), "include_artifacts must be boolean")
    pattern_ids = pattern_ids or []
    _require(isinstance(pattern_ids, (list, tuple)),
             "pattern_ids must be a list")
    for pattern_id in pattern_ids:
        _require(isinstance(pattern_id, str) and pattern_id,
                 "pattern_id filter must be a non-empty string")
    _require(detail in ("ids", "snippets"), "detail must be ids or snippets")
    _require(max_chars is None or (
        isinstance(max_chars, int) and not isinstance(max_chars, bool)
        and max_chars >= 256), "max_chars must be null or an integer >= 256")
    for name, value in (("kind", kind), ("topic", topic),
                        ("evidence_status", evidence_status),
                        ("artifact_type", artifact_type),
                        ("volume", volume)):
        _require(value is None or (isinstance(value, str) and value),
                 name + " filter must be a non-empty string")
    prefix = None if path_prefix is None else path_prefix_pattern(path_prefix)
    db, manifest = open_snapshot(root, index_path)
    cache_key = _query_cache_key(
        root, manifest["snapshot_id"], query, limit, kind, topic,
        evidence_status, path_prefix, index_path, all_sections, abstain,
        include_weak, detail, max_chars, artifact_type, volume, pattern_ids,
        section_rerank, section_rerank_margin)
    cached = _cache_get(cache_key)
    if cached is not None:
        db.close()
        return cached
    metadata = load_document_metadata(root)
    try:
        filters, params = [], []
        if kind is not None:
            filters.append("s.kind = ?")
            params.append(kind)
        if evidence_status is not None:
            filters.append("s.evidence_status = ?")
            params.append(evidence_status)
        if artifact_type is not None:
            filters.append("s.artifact_type = ?")
            params.append(artifact_type)
        if volume is not None:
            filters.append("s.volume = ?")
            params.append(volume)
        for pattern_id in pattern_ids:
            filters.append("EXISTS (SELECT 1 FROM section_patterns sp"
                           " WHERE sp.section_key = s.section_key"
                           " AND sp.pattern_id = ?)")
            params.append(pattern_id)
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
        section_rerank_applied = False
        if section_rerank:
            if ("v12" in query.casefold()
                    or (selected
                        and selected[0][3]["row"]["volume"] == "v12")):
                raise SearchError(
                    "section_rerank is disabled for V12 results",
                    "invalid-request")
            apply_rerank = section_rerank_margin is None
            if not apply_rerank:
                scores = sorted((item[0] for item in selected), reverse=True)
                margin = ((scores[0] - scores[1]) / scores[0]
                          if len(scores) > 1 and scores[0] else 1.0)
                apply_rerank = margin < section_rerank_margin
            if apply_rerank:
                selected = section_rerank_candidates(
                    db, terms, selected, limit, filters, params, weight_sql)
                section_rerank_applied = True
        pattern_map = {}
        selected_keys = [candidate["row"]["section_key"]
                         for _, _, _, candidate in selected]
        if selected_keys:
            rows = db.execute(
                "SELECT section_key,pattern_id FROM section_patterns"
                " WHERE section_key IN (" + ",".join("?" * len(selected_keys))
                + ") ORDER BY section_key,pattern_id", selected_keys).fetchall()
            for pattern_row in rows:
                pattern_map.setdefault(
                    pattern_row["section_key"], []).append(
                        pattern_row["pattern_id"])
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
                "artifact_type": row["artifact_type"],
                "volume": row["volume"],
                "pattern_ids": pattern_map.get(row["section_key"], []),
                "char_start": row["char_start"],
                "char_end": row["char_end"],
                "score": round(score, 6),
                "score_kind": ("section-rerank" if section_rerank_applied
                               else "bm25"),
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
            document_meta = metadata.get(row["path"], {})
            if document_meta and not any(
                    term in item["excerpt"].casefold() for term in terms):
                item["metadata_snippet"] = document_meta.get("summary")
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
        weak_results = []
        if not results and include_weak:
            weak_results = metadata_fallback(
                db, metadata, query, terms, limit)
        if weak_results:
            status = "no-confident-answer"
            assessment = dict(assessment)
            assessment["no_confident_answer"] = True
            assessment["confident"] = False
            assessment["state"] = "metadata-expansion"
            assessment["basis"] = "route-metadata-fallback"
        elif not results:
            status = "no-results"
            assessment = dict(assessment)
            assessment["no_confident_answer"] = True
            assessment["confident"] = False
            assessment["state"] = "no-results"
            assessment["basis"] = "zero-results"
        elif abstain and assessment["no_confident_answer"]:
            status = "no-confident-answer"
            if include_weak:
                weak_results = results
            results = []
            truncated = False
        else:
            status = "ok"
        artifact_payload = {
            "artifacts": [], "total": 0, "filters": {
                "pattern_ids": list(pattern_ids),
                "artifact_type": artifact_type,
                "volume": volume,
            },
        }
        if include_artifacts or pattern_ids or artifact_type or volume:
            artifact_terms = (terms if include_artifacts and not pattern_ids
                              and artifact_type is None else None)
            artifact_payload = v12_artifacts(
                root, pattern_ids=pattern_ids, artifact_type=artifact_type,
                volume=volume, limit=min(max(limit * 5, 50), 200),
                terms=artifact_terms)
        if not results and artifact_payload["artifacts"]:
            status = "ok"
            assessment = dict(assessment)
            assessment["no_confident_answer"] = False
            assessment["confident"] = False
            assessment["state"] = "artifact-lookup"
            assessment["basis"] = "v12-derived-artifacts"
        facets = {"kind": {}, "evidence_status": {},
                  "artifact_type": {}, "volume": {}, "pattern_id": {}}
        for item in results + weak_results:
            kind_value = item.get("kind") or "unknown"
            evidence_value = item.get("evidence_status") or "unknown"
            artifact_value = item.get("artifact_type") or "unknown"
            volume_value = item.get("volume") or "unknown"
            facets["kind"][kind_value] = facets["kind"].get(kind_value, 0) + 1
            facets["evidence_status"][evidence_value] = (
                facets["evidence_status"].get(evidence_value, 0) + 1)
            facets["artifact_type"][artifact_value] = (
                facets["artifact_type"].get(artifact_value, 0) + 1)
            facets["volume"][volume_value] = (
                facets["volume"].get(volume_value, 0) + 1)
            for pattern_id in item.get("pattern_ids") or []:
                facets["pattern_id"][pattern_id] = (
                    facets["pattern_id"].get(pattern_id, 0) + 1)
        if detail == "ids":
            keep = (
                "section_key", "document_id", "section_id", "path", "heading",
                "heading_level", "title", "kind", "evidence_status", "score",
                "score_kind", "matched_terms", "citation", "anchor", "why",
                "artifact_type", "volume", "pattern_ids", "next_actions",
            )
            results = [
                {key: item[key] for key in keep if key in item}
                for item in results
            ]
            weak_results = [
                {key: item[key] for key in keep if key in item}
                for item in weak_results
            ]
        next_actions = []
        for item in results + weak_results:
            next_actions = item.get("next_actions") or []
            if next_actions:
                break
        response = {
            "status": status,
            "snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"],
            "unannotated": len(manifest["unannotated_paths"]),
            "query": query,
            "match_mode": mode,
            "ranker_version": RANKER_VERSION,
            "citation_scheme": CITATION_SCHEME,
            "result_scope": ("all-sections" if all_sections else
                             "section-rerank" if section_rerank_applied else
                             "best-section-per-document"),
            "filters": {"kind": kind, "topic": topic,
                        "evidence_status": evidence_status,
                        "path_prefix": path_prefix,
                        "artifact_type": artifact_type,
                        "volume": volume,
                        "pattern_ids": list(pattern_ids)},
            "detail": detail,
            "max_chars": max_chars,
            "returned": len(results),
            "weak_returned": len(weak_results),
            "metadata_expanded": bool(weak_results),
            "truncated": truncated,
            "facets": facets,
            "artifacts": artifact_payload["artifacts"],
            "artifact_total": artifact_payload["total"],
            "artifact_filters": artifact_payload["filters"],
            "next_actions": next_actions,
            "answerability": assessment,
            "results": results,
            "weak_results": weak_results,
        }
        if max_chars is not None:
            def encoded_size():
                return len(json.dumps(
                    response, ensure_ascii=False,
                    separators=(",", ":")).encode("utf-8"))
            while encoded_size() > max_chars:
                if response["weak_results"]:
                    response["weak_results"].pop()
                    response["weak_returned"] = len(response["weak_results"])
                elif response["results"]:
                    response["results"].pop()
                    response["returned"] = len(response["results"])
                elif response.get("facets"):
                    response.pop("facets", None)
                elif response.get("next_actions"):
                    response.pop("next_actions", None)
                elif isinstance(response.get("answerability"), dict) and (
                        "features" in response["answerability"]):
                    response["answerability"].pop("features", None)
                else:
                    break
                response["truncated"] = True
        response["returned_chars"] = len(json.dumps(
            response, ensure_ascii=False,
            separators=(",", ":")).encode("utf-8"))
        _cache_put(cache_key, copy.deepcopy(response))
        return response
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
    ap.add_argument("action", choices=("search", "read", "evidence", "v12"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--index", type=Path)
    ap.add_argument("--query")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--all-sections", action="store_true",
                    help="Return every matching section instead of the best per page")
    ap.add_argument("--section-rerank", action="store_true",
                    help="Rank sections across the top pages by coverage")
    ap.add_argument("--section-rerank-margin", type=float,
                    help="Apply rerank only below this top1/top2 margin")
    ap.add_argument("--kind")
    ap.add_argument("--topic")
    ap.add_argument("--evidence-status")
    ap.add_argument("--artifact-type")
    ap.add_argument("--volume")
    ap.add_argument("--pattern-id", action="append", default=[])
    ap.add_argument("--include-artifacts", action="store_true")
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
                all_sections=args.all_sections,
                section_rerank=args.section_rerank,
                section_rerank_margin=args.section_rerank_margin,
                artifact_type=args.artifact_type, volume=args.volume,
                pattern_ids=args.pattern_id,
                include_artifacts=args.include_artifacts)
        elif args.action == "v12":
            payload = v12_artifacts(
                args.root, pattern_ids=args.pattern_id,
                artifact_type=args.artifact_type,
                volume=args.volume or "v12", limit=args.limit)
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
