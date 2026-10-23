#!/usr/bin/env python3
"""Deterministic, read-only-input section FTS5 snapshot over validated Tycho pages.

Uses the existing route_index.canonical_scan as the authority on document IDs,
metadata, source SHA and coverage. Never edits book/frontmatter, checks remote
sources, enriches text, modifies another index or triggers workflows.

Section model: one page overview plus every level-2 heading. Level-3 and
deeper headings stay inside the owning level-2 section and remain searchable
text, but are not separate citable sections in this format.

Incremental mode reuses unchanged section *parsing* from an older valid index,
then atomically publishes a fresh complete SQLite file; it does NOT claim
in-place incremental SQLite B-tree updates or stable heading IDs across rename.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import tempfile

import route_index

ROOT = Path(__file__).resolve().parents[1]
INDEX_NAME = "sections-fts-v3.sqlite"
VERSION = 3
SECTION_MODEL = "overview+h2; porter unicode61; bm25 title=5 heading=2 body=0.25"
HEAD = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
ANCHOR = re.compile(r"\s*\{#([a-z][a-z0-9_-]*)\}\s*$")
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})")
TOKEN = re.compile(r"[^\W_]+", re.UNICODE)
HEX = re.compile(r"^[0-9a-f]{64}$")
SECTION_COLUMNS = (
    "section_key", "document_id", "section_id", "path", "heading",
    "heading_level", "title", "kind", "evidence_status", "content",
    "char_start", "char_end", "document_sha256",
)
MANIFEST_KEYS = {
    "format_version", "route_snapshot_sha256", "coverage", "unannotated_paths",
    "document_count", "section_count", "document_sha256", "section_model",
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


def body_of(section):
    """Return indexable body text; drop the heading line of an H2 section."""
    if section["heading_level"] == 2:
        _, sep, rest = section["content"].partition("\n")
        return rest if sep else ""
    return section["content"]


def parse_sections(doc, text):
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
        })
    require(segments, "No indexable content in " + doc["path"])
    return segments


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
        records = [dict(zip(SECTION_COLUMNS, r)) for r in rows]
        for section in records:
            require(HEX.match(section["document_sha256"]) is not None,
                    "Malformed document digest")
            require(section["char_start"] < section["char_end"],
                    "Invalid section offsets")
        parts = [{"section_key": r["section_key"],
                  "char_start": r["char_start"], "char_end": r["char_end"],
                  "document_sha256": r["document_sha256"]} for r in records]
        parts.sort(key=lambda r: (r["section_key"].split("#")[0],
                                  r["char_start"],
                                  r["section_key"].split("#")[-1]))
        stable = {k: v for k, v in manifest.items() if k != "snapshot_id"}
        require(digest(canonical_json(stable) + "\n" + canonical_json(parts))
                == manifest["snapshot_id"],
                "Snapshot ID does not match indexed sections")
        grouped = {}
        for section in records:
            grouped.setdefault(section["document_id"], []).append(section)
        topics_by_key = {}
        for key, topic in topics:
            topics_by_key.setdefault(key, []).append(topic)
        return {"sections": grouped, "topics": topics_by_key}, manifest
    except (sqlite3.DatabaseError, ValueError, TypeError, KeyError) as exc:
        if isinstance(exc, ValueError) and str(exc).startswith(
                "Existing section index"):
            raise
        raise ValueError(
            "Existing section index is corrupt/incompatible; refuse unverified reuse")


def safe_reuse(doc, text, header_end, cached):
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
        if safe_reuse(doc, text, header.end(), cached):
            segments = cached
            reused += 1
        else:
            segments = parse_sections(doc, text)
        result.extend(segments)
        for section in segments:
            topics[section["section_key"]] = sorted(set(doc["topics"]))
    result.sort(key=lambda s: (s["document_id"], s["char_start"], s["section_id"]))
    names = [r["section_key"] for r in result]
    require(len(names) == len(set(names)),
            "Ambiguous section ID; add explicit unique anchors")
    stable = {
        "format_version": VERSION,
        "route_snapshot_sha256": scan["snapshot_sha256"],
        "coverage": scan["coverage"],
        "unannotated_paths": scan["unannotated_paths"],
        "document_count": len(scan["documents"]),
        "section_count": len(result),
        "document_sha256": {d["id"]: d["sha256"] for d in scan["documents"]},
        "section_model": SECTION_MODEL,
    }
    parts = [{k: r[k] for k in ("section_key", "char_start", "char_end",
                                "document_sha256")} for r in result]
    stable["snapshot_id"] = digest(canonical_json(stable) + "\n" +
                                   canonical_json(parts))
    return stable, result, topics, reused


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


def write_index(target, manifest, sections, topics):
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
                "char_end INTEGER NOT NULL,document_sha256 TEXT NOT NULL)")
            db.execute("CREATE TABLE section_topics(section_key TEXT NOT NULL,"
                       "topic TEXT NOT NULL,PRIMARY KEY(section_key,topic))")
            try:
                db.execute(
                    "CREATE VIRTUAL TABLE fts USING fts5(section_key UNINDEXED,"
                    "title,heading,body,tokenize='porter unicode61')")
            except sqlite3.OperationalError as exc:
                raise ValueError("SQLite build lacks FTS5 support") from exc
            rows = [tuple(section[k] for k in SECTION_COLUMNS)
                    for section in sections]
            db.executemany(
                "INSERT INTO sections VALUES(" + ",".join("?" * len(SECTION_COLUMNS)) + ")",
                rows)
            db.executemany(
                "INSERT INTO section_topics(section_key,topic) VALUES(?,?)",
                sorted((key, topic) for key, values in topics.items()
                       for topic in values))
            db.executemany(
                "INSERT INTO fts(section_key,title,heading,body) VALUES(?,?,?,?)",
                [(s["section_key"], s["title"], s["heading"], body_of(s))
                 for s in sections])
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
    manifest, sections, topics, reused = compose(
        root, previous, allow_partial=allow_partial)
    if previous[1] is not None and previous[1] == manifest and not full:
        verify(root, target)
        return {"outcome": "unchanged", "snapshot": manifest["snapshot_id"],
                "documents": manifest["document_count"],
                "sections": len(sections), "reused_documents": reused}
    write_index(target, manifest, sections, topics)
    return {"outcome": "published", "snapshot": manifest["snapshot_id"],
            "documents": manifest["document_count"], "sections": len(sections),
            "reused_documents": reused}


def verify(root, supplied=None):
    require_fts5()
    target = output_path(root, supplied)
    cached, manifest = old_sections(target)
    require(manifest is not None, "No published section index")
    fresh, fresh_sections, fresh_topics, _ = compose(
        root, ({}, None), allow_partial=True)
    require(fresh == manifest,
            "Section index stale: canonical source/route snapshot changed")
    cached_rows = [x for rows in cached["sections"].values() for x in rows]
    cached_rows.sort(key=lambda x: (x["document_id"], x["char_start"],
                                    x["section_id"]))
    require(cached_rows == fresh_sections,
            "Section metadata, offsets or content diverge from book")
    require(cached["topics"] == fresh_topics,
            "Section topic filters diverge from book metadata")
    return {"outcome": "verified", "snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"],
            "unannotated_count": len(manifest["unannotated_paths"]),
            "documents": manifest["document_count"],
            "sections": manifest["section_count"]}


def stats(root, supplied=None):
    target = output_path(root, supplied)
    _, manifest = old_sections(target)
    require(manifest is not None, "No published section index")
    return {"snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"],
            "documents": manifest["document_count"],
            "sections": manifest["section_count"],
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
