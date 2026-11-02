#!/usr/bin/env python3
"""Deterministic, read-only-input section FTS5 snapshot over validated Tycho pages.

Uses the existing route_index.canonical_scan as the authority on document IDs,
metadata, source SHA and coverage. Never edits book/frontmatter, checks remote
sources, enriches text, modifies another index or triggers workflows.

Section model: one page overview plus every level-2 heading. Level-3 headings
inside an H2 section are also stored as internal passages with a parent-H2
mapping. Passages are rankable and diagnostic only; they never become public
citable sections. Level-4 and deeper headings stay inside the owning passage or
section text.

The v5 schema also stores nullable artifact_type and volume columns plus a
section_patterns table derived from the V12 index and reverse index. V12 JSON
artifacts are exposed by the search-layer lookup, not by rewriting the book.

Incremental mode reuses unchanged section *parsing* from an older valid index,
then atomically publishes a fresh complete SQLite file; it does NOT claim
in-place incremental SQLite B-tree updates or stable heading IDs across rename.
"""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import tempfile
from contextlib import contextmanager

import route_index

ROOT = Path(__file__).resolve().parents[1]
INDEX_NAME = "sections-fts-v5.sqlite"
VERSION = 5
SECTION_MODEL = "overview+h2; porter unicode61; bm25 title=5 heading=2 body=0.25"
FACET_MODEL = "v12-artifact-type+volume+pattern-ids; document defaults"
PASSAGE_MODEL = ("h3-under-h2; parent-h2 mapping; porter unicode61; "
                 "bm25 title=5 heading=2 body=0.25")
HEAD = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
ANCHOR = re.compile(r"\s*\{#([a-z][a-z0-9_-]*)\}\s*$")
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})")
TOKEN = re.compile(r"[^\W_]+", re.UNICODE)
HEX = re.compile(r"^[0-9a-f]{64}$")
SECTION_COLUMNS = (
    "section_key", "document_id", "section_id", "path", "heading",
    "heading_level", "title", "kind", "evidence_status", "content",
    "char_start", "char_end", "document_sha256", "artifact_type", "volume",
)
PASSAGE_COLUMNS = (
    "passage_key", "passage_id", "parent_section_key", "parent_section_id",
    "document_id", "path", "heading", "heading_level", "title", "content",
    "body", "char_start", "char_end", "document_sha256",
)
MANIFEST_KEYS = {
    "format_version", "route_snapshot_sha256", "coverage", "unannotated_paths",
    "document_count", "section_count", "passage_count", "document_sha256",
    "section_model", "passage_model", "facet_model", "facet_input_sha256",
    "snapshot_id",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def canonical_json(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def slug(value):
    bits = TOKEN.findall(value.casefold())
    return "-".join(bits)[:120] or "section"


def volume_of(path):
    """Return the readable volume ID for a book path, or None."""
    parts = Path(path).parts
    if len(parts) >= 3 and parts[0] == "book" and parts[1] == "volumes":
        return parts[2].split("-", 1)[0]
    return None


def facet_input_sha256(root):
    """Hash the derived V12 files that supply search facets."""
    root = Path(root).resolve()
    digest = hashlib.sha256(b"tycho.v12-search-facets.v1\0")
    for relative in ("generated/v12-index.v1.json",
                     "edition/v12/reverse-index.v1.json"):
        path = root / relative
        digest.update(relative.encode("utf-8") + b"\0")
        if path.is_file() and not path.is_symlink():
            digest.update(path.read_bytes())
        else:
            digest.update(b"missing")
        digest.update(b"\0")
    return digest.hexdigest()


def load_facets(root):
    """Load V12 artifact facets from the derived index and reverse index.

    The canonical book and route metadata remain authoritative. Missing files
    produce document defaults, so a non-V12 tree builds unchanged.
    """
    root = Path(root).resolve()
    facets = {}
    index_path = root / "generated/v12-index.v1.json"
    if index_path.is_file() and not index_path.is_symlink():
        try:
            payload = json.loads(index_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            payload = {}
        for document in payload.get("documents", []):
            if not isinstance(document, dict) or not isinstance(
                    document.get("path"), str):
                continue
            facets[document["path"]] = {
                "artifact_type": document.get("artifact_type") or "document",
                "volume": document.get("volume") or volume_of(document["path"]),
                "pattern_ids": sorted(set(document.get("pattern_ids") or [])),
            }
    reverse_path = root / "edition/v12/reverse-index.v1.json"
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
                if not isinstance(path, str):
                    continue
                facets.setdefault(path, {
                    "artifact_type": "document",
                    "volume": volume_of(path),
                    "pattern_ids": [],
                })["pattern_ids"] = sorted(set(
                    facets[path]["pattern_ids"] + [pattern_id]))
    return facets


def body_of(section):
    """Return indexable body text; drop the heading line of an H2 section."""
    if section["heading_level"] == 2:
        _, sep, rest = section["content"].partition("\n")
        return rest if sep else ""
    return section["content"]


def body_of_passage(passage):
    """Return passage text without its H3 heading line."""
    _, sep, rest = passage["content"].partition("\n")
    return rest if sep else ""


def parse_sections(doc, text, facets=None):
    facets = facets or {}
    require(digest(text) == doc["sha256"],
            "document digest changed since metadata scan")
    header = route_index.FENCE.match(text)
    require(header is not None,
            "route-index document lacks expected YAML frontmatter")
    start = header.end()
    headings = []
    at = 0
    fenced = None
    for line in text.splitlines(keepends=True):
        line_start = at
        at += len(line)
        if line_start < start:
            continue
        stripped = line.rstrip("\r\n")
        fence = FENCE.match(stripped)
        if fence:
            char = fence.group(1)[0]
            if fenced is None:
                fenced = (char, len(fence.group(1)))
            elif fenced[0] == char and len(fence.group(1)) >= fenced[1]:
                fenced = None
            continue
        if fenced is not None:
            continue
        match = HEAD.match(stripped)
        if match and len(match.group(1)) == 2:
            raw = match.group(2).strip()
            explicit = ANCHOR.search(raw)
            heading = ANCHOR.sub("", raw).strip()
            require(heading, "empty heading in " + doc["path"])
            headings.append(
                (line_start, heading, explicit.group(1) if explicit else None))
    boundaries = [(start, doc["title"], "overview", 0)]
    boundaries.extend((pos, heading, anchor, 2) for pos, heading, anchor in headings)
    segments = []
    seen = {}
    for i, (offset, heading, explicit, level) in enumerate(boundaries):
        end = boundaries[i + 1][0] if i + 1 < len(boundaries) else len(text)
        chunk = text[offset:end]
        if level == 2 and not chunk.strip():
            continue
        proposed = explicit or (slug(heading) if level == 2 else "overview")
        seen[proposed] = seen.get(proposed, 0) + 1
        section_id = proposed if seen[proposed] == 1 else f"{proposed}-{seen[proposed]}"
        segments.append({
            "section_key": doc["id"] + "#" + section_id,
            "document_id": doc["id"],
            "section_id": section_id,
            "path": doc["path"],
            "heading": heading,
            "heading_level": level,
            "title": doc["title"],
            "kind": doc["kind"],
            "evidence_status": doc["evidence_status"],
            "content": chunk,
            "char_start": offset,
            "char_end": end,
            "document_sha256": doc["sha256"],
            "artifact_type": facets.get("artifact_type") or "document",
            "volume": facets.get("volume") or volume_of(doc["path"]),
            "pattern_ids": sorted(set(facets.get("pattern_ids") or [])),
        })
    require(segments, "No indexable content in " + doc["path"])
    return segments


def parse_passages(section):
    """Derive internal H3 passages from one canonical parent H2 section.

    Passage offsets stay absolute document codepoint offsets. The parent H2
    section row remains authoritative and unchanged; passages are an additional
    retrieval view used only to select and expose the internal match.
    """
    require(section["heading_level"] == 2,
            "Passages require a level-2 parent section")
    content = section["content"]
    base = section["char_start"]
    headings = []
    at = 0
    fenced = None
    for line in content.splitlines(keepends=True):
        line_start = at
        at += len(line)
        stripped = line.rstrip("\r\n")
        fence = FENCE.match(stripped)
        if fence:
            char = fence.group(1)[0]
            if fenced is None:
                fenced = (char, len(fence.group(1)))
            elif fenced[0] == char and len(fence.group(1)) >= fenced[1]:
                fenced = None
            continue
        if fenced is not None:
            continue
        match = HEAD.match(stripped)
        if match and len(match.group(1)) == 3:
            raw = match.group(2).strip()
            explicit = ANCHOR.search(raw)
            heading = ANCHOR.sub("", raw).strip()
            require(heading, "empty H3 heading in " + section["path"])
            headings.append(
                (line_start, heading, explicit.group(1) if explicit else None))
    passages = []
    seen = {}
    for i, (offset, heading, explicit) in enumerate(headings):
        end = headings[i + 1][0] if i + 1 < len(headings) else len(content)
        chunk = content[offset:end]
        if not chunk.strip():
            continue
        proposed = explicit or slug(heading)
        seen[proposed] = seen.get(proposed, 0) + 1
        passage_id = proposed if seen[proposed] == 1 else f"{proposed}-{seen[proposed]}"
        passages.append({
            "passage_key": section["section_key"] + "~" + passage_id,
            "passage_id": passage_id,
            "parent_section_key": section["section_key"],
            "parent_section_id": section["section_id"],
            "document_id": section["document_id"],
            "path": section["path"],
            "heading": heading,
            "heading_level": 3,
            "title": section["title"],
            "content": chunk,
            "body": (chunk.partition("\n")[2] if "\n" in chunk else ""),
            "char_start": base + offset,
            "char_end": base + end,
            "document_sha256": section["document_sha256"],
        })
    return passages


def old_sections(index_path):
    """Load and structurally validate an existing index for parse reuse."""
    if not index_path.is_file() or index_path.is_symlink():
        return {}, None
    try:
        with sqlite3.connect(
                "file:" + index_path.as_posix() + "?mode=ro", uri=True) as db:
            row = db.execute(
                "SELECT value FROM meta WHERE key='manifest'").fetchone()
            require(row is not None, "Section index has no manifest")
            manifest = json.loads(row[0])
            require(manifest.get("format_version") == VERSION,
                    "Incompatible section index format")
            require(set(manifest) == MANIFEST_KEYS,
                    "Unexpected snapshot manifest fields")
            rows = db.execute(
                "SELECT " + ",".join(SECTION_COLUMNS) + " FROM sections"
                " ORDER BY document_id,char_start,section_id").fetchall()
            require(db.execute("PRAGMA integrity_check").fetchone()[0] == "ok",
                    "Corrupt SQLite index")
            fts_rows = db.execute(
                "SELECT section_key,title,heading,body FROM fts"
                " ORDER BY section_key").fetchall()
            require(sorted(
                (r[0], r[6], r[4], body_of(dict(zip(SECTION_COLUMNS, r))))
                for r in rows) == fts_rows,
                "FTS records diverge from canonical section rows")
            topics = db.execute(
                "SELECT section_key,topic FROM section_topics"
                " ORDER BY section_key,topic").fetchall()
            pattern_rows = db.execute(
                "SELECT section_key,pattern_id FROM section_patterns"
                " ORDER BY section_key,pattern_id").fetchall()
            passage_rows = db.execute(
                "SELECT " + ",".join(PASSAGE_COLUMNS) + " FROM passages"
                " ORDER BY document_id,char_start,passage_id").fetchall()
            passage_fts_rows = db.execute(
                "SELECT passage_key,title,heading,body FROM passage_fts"
                " ORDER BY passage_key").fetchall()
        records = [dict(zip(SECTION_COLUMNS, r)) for r in rows]
        patterns_by_key = {}
        for key, pattern_id in pattern_rows:
            patterns_by_key.setdefault(key, []).append(pattern_id)
        for section in records:
            section["pattern_ids"] = sorted(patterns_by_key.get(
                section["section_key"], []))
        for section in records:
            require(HEX.match(section["document_sha256"]) is not None,
                    "Malformed document digest")
            require(section["char_start"] < section["char_end"],
                    "Invalid section offsets")
        sections_by_key = {section["section_key"]: section
                           for section in records}
        passages = [dict(zip(PASSAGE_COLUMNS, r)) for r in passage_rows]
        for passage in passages:
            parent = sections_by_key.get(passage["parent_section_key"])
            require(parent is not None, "Passage parent section is missing")
            require(parent["heading_level"] == 2
                    and passage["heading_level"] == 3,
                    "Passage level is not H3 under H2")
            require(passage["passage_key"]
                    == parent["section_key"] + "~" + passage["passage_id"],
                    "Passage key does not match its stable identity")
            require(passage["parent_section_id"] == parent["section_id"]
                    and passage["document_id"] == parent["document_id"]
                    and passage["path"] == parent["path"]
                    and passage["title"] == parent["title"]
                    and passage["document_sha256"] == parent["document_sha256"],
                    "Passage metadata diverges from its parent section")
            require(type(passage["char_start"]) is int
                    and type(passage["char_end"]) is int
                    and parent["char_start"] <= passage["char_start"]
                    < passage["char_end"] <= parent["char_end"],
                    "Passage offsets are outside the parent section")
            start = passage["char_start"] - parent["char_start"]
            end = passage["char_end"] - parent["char_start"]
            require(parent["content"][start:end] == passage["content"],
                    "Passage content diverges from its parent section")
            require(HEX.match(passage["document_sha256"]) is not None,
                    "Malformed passage document digest")
            require(passage["body"] == body_of_passage(passage),
                    "Passage body diverges from its content")
        require(sorted((p["passage_key"], p["title"], p["heading"], p["body"])
                       for p in passages) == passage_fts_rows,
                "Passage FTS records diverge from canonical passage rows")
        parts = [{"section_key": r["section_key"],
                  "char_start": r["char_start"], "char_end": r["char_end"],
                  "document_sha256": r["document_sha256"]} for r in records]
        parts.sort(key=lambda r: (r["section_key"].split("#")[0],
                                  r["char_start"],
                                  r["section_key"].split("#")[-1]))
        passage_parts = [{"passage_key": r["passage_key"],
                          "parent_section_key": r["parent_section_key"],
                          "char_start": r["char_start"],
                          "char_end": r["char_end"],
                          "document_sha256": r["document_sha256"]}
                         for r in passages]
        stable = {k: v for k, v in manifest.items() if k != "snapshot_id"}
        require(digest(canonical_json(stable) + "\n" + canonical_json(
            {"sections": parts, "passages": passage_parts}))
                == manifest["snapshot_id"],
                "Snapshot ID does not match indexed sections and passages")
        grouped = {}
        for section in records:
            grouped.setdefault(section["document_id"], []).append(section)
        grouped_passages = {}
        for passage in passages:
            grouped_passages.setdefault(passage["document_id"], []).append(passage)
        topics_by_key = {}
        for key, topic in topics:
            topics_by_key.setdefault(key, []).append(topic)
        return {"sections": grouped, "topics": topics_by_key,
                "passages": grouped_passages}, manifest
    except (sqlite3.DatabaseError, ValueError, TypeError, KeyError) as exc:
        if isinstance(exc, ValueError) and str(exc).startswith(
                "Existing section index"):
            raise
        raise ValueError(
            "Existing section index is corrupt/incompatible; refuse unverified reuse")


def safe_reuse(doc, text, header_end, cached, facets=None):
    facets = facets or {}
    if not cached:
        return False
    cached = sorted(cached, key=lambda r: r["char_start"])
    if cached[0]["char_start"] < header_end or cached[-1]["char_end"] != len(text):
        return False
    if text[header_end:cached[0]["char_start"]].strip():
        return False
    if any(a["char_end"] != b["char_start"] for a, b in zip(cached, cached[1:])):
        return False
    for section in cached:
        expected_key = section["document_id"] + "#" + section["section_id"]
        if (section["section_key"] != expected_key
                or section["path"] != doc["path"]
                or section["document_sha256"] != doc["sha256"]
                or section["title"] != doc["title"]
                or section["kind"] != doc["kind"]
                or section["evidence_status"] != doc["evidence_status"]
                or section["artifact_type"] != (facets.get("artifact_type") or "document")
                or section["volume"] != (facets.get("volume") or volume_of(doc["path"]))
                or sorted(section.get("pattern_ids") or []) != sorted(
                    set(facets.get("pattern_ids") or []))
                or type(section["char_start"]) is not int
                or type(section["char_end"]) is not int
                or section["char_start"] >= section["char_end"]
                or section["content"] != text[section["char_start"]:section["char_end"]]):
            return False
    return True


def compose(root, previous=None, allow_partial=False):
    root = Path(root).resolve()
    scan = route_index.canonical_scan(root, allow_partial=allow_partial)
    require(scan["documents"], "No validated metadata documents for indexing")
    old, previous_manifest = previous if previous is not None else ({}, None)
    result = []
    reused = 0
    topics = {}
    facets = load_facets(root)
    for doc in sorted(scan["documents"], key=lambda item: item["id"]):
        path = root / doc["path"]
        require(not path.is_symlink() and path.is_file()
                and path.resolve().is_relative_to((root / "book").resolve()),
                "Invalid canonical page path " + doc["path"])
        text = path.read_text(encoding="utf-8")
        require(digest(text) == doc["sha256"],
                "Source file changed during index build")
        header = route_index.FENCE.match(text)
        require(header is not None, "Missing frontmatter during index build")
        cached = old.get("sections", {}).get(doc["id"], [])
        facet = facets.get(doc["path"])
        if safe_reuse(doc, text, header.end(), cached, facet):
            segments = cached
            reused += 1
        else:
            segments = parse_sections(doc, text, facet)
        result.extend(segments)
        for section in segments:
            topics[section["section_key"]] = sorted(set(doc["topics"]))
    result.sort(key=lambda s: (s["document_id"], s["char_start"], s["section_id"]))
    names = [r["section_key"] for r in result]
    require(len(names) == len(set(names)),
            "Ambiguous section ID; add explicit unique anchors")
    passages = []
    for section in result:
        if section["heading_level"] == 2:
            passages.extend(parse_passages(section))
    passages.sort(key=lambda p: (p["document_id"], p["char_start"],
                                 p["passage_id"]))
    passage_names = [p["passage_key"] for p in passages]
    require(len(passage_names) == len(set(passage_names)),
            "Ambiguous H3 passage ID; add explicit unique anchors")
    stable = {
        "format_version": VERSION,
        "route_snapshot_sha256": scan["snapshot_sha256"],
        "coverage": scan["coverage"],
        "unannotated_paths": scan["unannotated_paths"],
        "document_count": len(scan["documents"]),
        "section_count": len(result),
        "passage_count": len(passages),
        "document_sha256": {d["id"]: d["sha256"] for d in scan["documents"]},
        "section_model": SECTION_MODEL,
        "passage_model": PASSAGE_MODEL,
        "facet_model": FACET_MODEL,
        "facet_input_sha256": facet_input_sha256(root),
    }
    parts = [{k: r[k] for k in ("section_key", "char_start", "char_end",
                                "document_sha256")} for r in result]
    passage_parts = [{k: p[k] for k in ("passage_key", "parent_section_key",
                                       "char_start", "char_end",
                                       "document_sha256")}
                     for p in passages]
    stable["snapshot_id"] = digest(canonical_json(stable) + "\n" +
                                   canonical_json({"sections": parts,
                                                   "passages": passage_parts}))
    return stable, result, topics, passages, reused


def require_fts5():
    """Fail explicitly when the supported SQLite/FTS5 BM25 profile is absent."""
    require(sqlite3.sqlite_version_info >= (3, 26, 0),
            "SQLite 3.26.0 or newer is required")
    try:
        with sqlite3.connect(":memory:") as db:
            db.execute("CREATE VIRTUAL TABLE probe USING fts5("
                       "key UNINDEXED,title,heading,body,"
                       "tokenize='porter unicode61')")
            db.execute("INSERT INTO probe VALUES(?,?,?,?)",
                       ("probe", "Architecture", "Retrieval", "bounded latency"))
            hit = db.execute(
                "SELECT key,bm25(probe,0.0,4.0,3.0,1.0) FROM probe"
                " WHERE probe MATCH ?", ("retrieval",)).fetchone()
            require(hit is not None and hit[0] == "probe"
                    and isinstance(hit[1], (int, float)),
                    "Required SQLite FTS5 weighted BM25 features are unavailable")
    except sqlite3.DatabaseError as exc:
        raise ValueError("Required SQLite FTS5 features are unavailable") from exc


def output_path(root, supplied=None):
    root = Path(root).resolve()
    folder = root / "generated"
    require(folder.is_dir() and not folder.is_symlink(),
            "Create ordinary generated/ directory explicitly")
    target = Path(supplied) if supplied is not None else folder / INDEX_NAME
    require(target.parent.resolve() == folder.resolve()
            and not target.is_symlink() and target.name.endswith(".sqlite"),
            "Index must be a normal direct file under generated/")
    return target


def write_index(target, manifest, sections, topics, passages):
    temp = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".tycho-fts-", suffix=".sqlite",
                                         dir=target.parent, delete=False) as tmp:
            temp = Path(tmp.name)
        with sqlite3.connect(temp) as db:
            db.execute("PRAGMA page_size=4096")
            db.execute("CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT NOT NULL)")
            db.execute(
                "CREATE TABLE sections(section_key TEXT PRIMARY KEY,"
                "document_id TEXT NOT NULL,section_id TEXT NOT NULL,"
                "path TEXT NOT NULL,heading TEXT NOT NULL,"
                "heading_level INTEGER NOT NULL,title TEXT NOT NULL,"
                "kind TEXT NOT NULL,evidence_status TEXT NOT NULL,"
                "content TEXT NOT NULL,char_start INTEGER NOT NULL,"
                "char_end INTEGER NOT NULL,document_sha256 TEXT NOT NULL,"
                "artifact_type TEXT NOT NULL,volume TEXT)")
            db.execute(
                "CREATE TABLE passages(passage_key TEXT PRIMARY KEY,"
                "passage_id TEXT NOT NULL,parent_section_key TEXT NOT NULL,"
                "parent_section_id TEXT NOT NULL,document_id TEXT NOT NULL,"
                "path TEXT NOT NULL,heading TEXT NOT NULL,"
                "heading_level INTEGER NOT NULL,title TEXT NOT NULL,"
                "content TEXT NOT NULL,body TEXT NOT NULL,"
                "char_start INTEGER NOT NULL,char_end INTEGER NOT NULL,"
                "document_sha256 TEXT NOT NULL)")
            db.execute("CREATE INDEX passages_parent ON passages("
                       "parent_section_key)")
            db.execute("CREATE TABLE section_topics(section_key TEXT NOT NULL,"
                       "topic TEXT NOT NULL,PRIMARY KEY(section_key,topic))")
            db.execute("CREATE TABLE section_patterns(section_key TEXT NOT NULL,"
                       "pattern_id TEXT NOT NULL,"
                       "PRIMARY KEY(section_key,pattern_id))")
            try:
                db.execute(
                    "CREATE VIRTUAL TABLE fts USING fts5(section_key UNINDEXED,"
                    "title,heading,body,tokenize='porter unicode61')")
                db.execute(
                    "CREATE VIRTUAL TABLE passage_fts USING fts5("
                    "passage_key UNINDEXED,title,heading,body,"
                    "tokenize='porter unicode61')")
            except sqlite3.OperationalError as exc:
                raise ValueError("SQLite build lacks FTS5 support") from exc
            rows = [tuple(section[k] for k in SECTION_COLUMNS)
                    for section in sections]
            db.executemany(
                "INSERT INTO sections VALUES(" + ",".join("?" * len(SECTION_COLUMNS)) + ")",
                rows)
            db.executemany(
                "INSERT INTO passages VALUES(" + ",".join("?" * len(PASSAGE_COLUMNS)) + ")",
                [tuple(passage[k] for k in PASSAGE_COLUMNS)
                 for passage in passages])
            db.executemany(
                "INSERT INTO section_topics(section_key,topic) VALUES(?,?)",
                sorted((key, topic) for key, values in topics.items()
                       for topic in values))
            db.executemany(
                "INSERT INTO section_patterns(section_key,pattern_id)"
                " VALUES(?,?)",
                sorted((section["section_key"], pattern_id)
                       for section in sections
                       for pattern_id in section.get("pattern_ids", [])))
            db.executemany(
                "INSERT INTO fts(section_key,title,heading,body) VALUES(?,?,?,?)",
                [(s["section_key"], s["title"], s["heading"], body_of(s))
                 for s in sections])
            db.executemany(
                "INSERT INTO passage_fts(passage_key,title,heading,body)"
                " VALUES(?,?,?,?)",
                [(p["passage_key"], p["title"], p["heading"], p["body"])
                 for p in passages])
            db.execute("INSERT INTO meta(key,value) VALUES('manifest',?)",
                       (canonical_json(manifest),))
            require(db.execute("PRAGMA integrity_check").fetchone()[0] == "ok",
                    "SQLite integrity failure")
            db.commit()
        with sqlite3.connect("file:" + temp.as_posix() + "?mode=ro", uri=True) as db:
            stored = db.execute(
                "SELECT value FROM meta WHERE key='manifest'").fetchone()
            require(stored is not None and json.loads(stored[0]) == manifest,
                    "Metadata readback failed")
        os.replace(temp, target)
        temp = None
    finally:
        if temp is not None and temp.exists():
            temp.unlink()


def publish(root, supplied=None, *, full=False, allow_partial=False):
    require_fts5()
    target = output_path(root, supplied)
    previous = ({}, None) if full else old_sections(target)
    manifest, sections, topics, passages, reused = compose(
        root, previous, allow_partial=allow_partial)
    if previous[1] is not None and previous[1] == manifest and not full:
        verify(root, target)
        return {"outcome": "unchanged", "snapshot": manifest["snapshot_id"],
                "documents": manifest["document_count"],
                "sections": len(sections), "passages": len(passages),
                "reused_documents": reused}
    write_index(target, manifest, sections, topics, passages)
    return {"outcome": "published", "snapshot": manifest["snapshot_id"],
            "documents": manifest["document_count"], "sections": len(sections),
            "passages": len(passages), "reused_documents": reused}


FRESH_SUFFIX = ".fresh.json"


def _source_fingerprint(root):
    """Cheap stat fingerprint of canonical inputs and the route index."""
    root = Path(root)
    digest = hashlib.sha256()
    paths = sorted((root / "book").rglob("*"))
    route = root / "generated" / "route-index.v1.json"
    if route.is_file():
        paths.append(route)
    for path in paths:
        if not path.is_file():
            continue
        stat = path.stat()
        rel = path.relative_to(root).as_posix()
        digest.update(rel.encode("utf-8") + b"\0")
        digest.update(str(stat.st_size).encode("ascii") + b"\0")
        digest.update(str(stat.st_mtime_ns).encode("ascii") + b"\n")
    return digest.hexdigest()


def _marker_path(index):
    return Path(index).with_name(Path(index).name + FRESH_SUFFIX)


def _marker_matches(root, index):
    try:
        marker = json.loads(_marker_path(index).read_text(encoding="utf-8"))
        stat = Path(index).stat()
    except (OSError, ValueError, json.JSONDecodeError):
        return None
    if marker.get("index_mtime_ns") != stat.st_mtime_ns:
        return None
    if marker.get("index_size") != stat.st_size:
        return None
    if marker.get("source_fingerprint") != _source_fingerprint(root):
        return None
    return marker


def _write_marker(root, index, result):
    marker = {
        "snapshot": result.get("snapshot"),
        "documents": result.get("documents"),
        "sections": result.get("sections"),
        "coverage": result.get("coverage"),
        "index_mtime_ns": Path(index).stat().st_mtime_ns,
        "index_size": Path(index).stat().st_size,
        "source_fingerprint": _source_fingerprint(root),
    }
    target = _marker_path(index)
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(target.suffix + ".tmp")
    temp.write_text(json.dumps(marker, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temp, target)


@contextmanager
def build_lock(index):
    """Serialize index verification/build across CLI and HTTP processes."""
    lock = Path(index).with_name(Path(index).name + ".lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open("a") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def ensure_fresh(root, supplied=None):
    """Verify the index and rebuild it when stale or missing.

    The rebuild is incremental and atomic. Errors are returned rather than
    raised so a server can keep its normal not-available response behavior.
    """
    index = Path(supplied) if supplied is not None else Path(root) / "generated" / INDEX_NAME
    cached = _marker_matches(root, index)
    if cached is not None:
        return {"status": "fresh", "cached": True,
                "snapshot": cached.get("snapshot"),
                "documents": cached.get("documents"),
                "sections": cached.get("sections")}
    with build_lock(index):
        cached = _marker_matches(root, index)
        if cached is not None:
            return {"status": "fresh", "cached": True,
                    "snapshot": cached.get("snapshot"),
                    "documents": cached.get("documents"),
                    "sections": cached.get("sections")}
        try:
            current = verify(root, index)
            _write_marker(root, index, current)
            return {"status": "fresh", **current}
        except (ValueError, RuntimeError, OSError, sqlite3.Error):
            pass
        try:
            publish(root, index, full=False)
            current = verify(root, index)
            _write_marker(root, index, current)
            return {"status": "rebuilt", **current}
        except (ValueError, RuntimeError, OSError, sqlite3.Error) as exc:
            return {"status": "unavailable", "error": str(exc)}


def verify(root, supplied=None):
    require_fts5()
    target = output_path(root, supplied)
    cached, manifest = old_sections(target)
    require(manifest is not None, "No published section index")
    fresh, fresh_sections, fresh_topics, fresh_passages, _ = compose(
        root, ({}, None), allow_partial=True)
    require(fresh == manifest,
            "Section index stale: canonical source/route snapshot changed")
    cached_rows = [x for rows in cached["sections"].values() for x in rows]
    cached_rows.sort(key=lambda x: (x["document_id"], x["char_start"],
                                    x["section_id"]))
    require(cached_rows == fresh_sections,
            "Section metadata, offsets or content diverge from book")
    cached_passages = [x for rows in cached["passages"].values() for x in rows]
    cached_passages.sort(key=lambda x: (x["document_id"], x["char_start"],
                                        x["passage_id"]))
    require(cached_passages == fresh_passages,
            "H3 passage metadata, offsets or content diverge from book")
    require(cached["topics"] == fresh_topics,
            "Section topic filters diverge from book metadata")
    return {"outcome": "verified", "snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"],
            "unannotated_count": len(manifest["unannotated_paths"]),
            "documents": manifest["document_count"],
            "sections": manifest["section_count"],
            "passages": manifest["passage_count"]}


def stats(root, supplied=None):
    target = output_path(root, supplied)
    _, manifest = old_sections(target)
    require(manifest is not None, "No published section index")
    return {"snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"],
            "documents": manifest["document_count"],
            "sections": manifest["section_count"],
            "passages": manifest["passage_count"],
            "bytes": target.stat().st_size}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("build", "check", "stats"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--index", type=Path)
    ap.add_argument("--full", action="store_true",
                    help="Reparse all documents before atomic publish")
    ap.add_argument("--allow-partial", action="store_true",
                    help="Index annotated pages and disclose unannotated coverage")
    args = ap.parse_args()
    try:
        if args.action == "build":
            result = publish(args.root, args.index, full=args.full,
                             allow_partial=args.allow_partial)
        elif args.action == "check":
            result = verify(args.root, args.index)
        else:
            result = stats(args.root, args.index)
    except (ValueError, RuntimeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)},
                         sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
