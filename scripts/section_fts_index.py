#!/usr/bin/env python3
"""Deterministic, read-only-input section FTS5 snapshot over validated Tycho pages.

Uses the existing route_index.canonical_scan as the authority on document IDs,
metadata, source SHA and partial coverage. Never edits book/frontmatter, checks
remote sources, enriches text, modifies another index or triggers workflows.

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
INDEX_NAME = "sections-fts-v1.sqlite"
VERSION = 1
HEAD = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
ANCHOR = re.compile(r"\s*\{#([a-z][a-z0-9_-]*)\}\s*$")
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})")
TOKEN = re.compile(r"[^\W_]+", re.UNICODE)
HEX = re.compile(r"^[0-9a-f]{64}$")


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


def parse_sections(doc, text):
    require(digest(text) == doc["sha256"], "document digest changed since metadata scan")
    header = route_index.FENCE.match(text)
    require(header is not None, "route-index document lacks expected YAML frontmatter")
    start = header.end()
    positions = []
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
        if match:
            raw_heading = match.group(2).strip()
            explicit = ANCHOR.search(raw_heading)
            heading = ANCHOR.sub("", raw_heading).strip()
            require(heading, "empty heading in " + doc["path"])
            positions.append((line_start, heading, explicit.group(1) if explicit else None))
    segments = []
    boundaries = [(start, "", "intro")] + [(p, h, a) for p, h, a in positions]
    seen = {}
    for i, (offset, heading, explicit) in enumerate(boundaries):
        end = boundaries[i + 1][0] if i + 1 < len(boundaries) else len(text)
        chunk = text[offset:end]
        if not chunk.strip():
            continue
        proposed = explicit or slug(heading)
        if proposed == "intro" and i > 0:
            proposed = "intro-heading"
        seen[proposed] = seen.get(proposed, 0) + 1
        section_id = proposed if seen[proposed] == 1 else f"{proposed}-{seen[proposed]}"
        section_key = doc["id"] + "#" + section_id
        segments.append({
            "section_key": section_key, "document_id": doc["id"],
            "section_id": section_id, "path": doc["path"], "heading": heading,
            "title": doc["title"], "content": chunk,
            "char_start": offset, "char_end": end, "document_sha256": doc["sha256"],
        })
    require(segments, "No indexable content in " + doc["path"])
    return segments


def old_sections(index_path):
    if not index_path.is_file() or index_path.is_symlink():
        return {}, None
    try:
        with sqlite3.connect("file:" + index_path.as_posix() + "?mode=ro", uri=True) as db:
            schema = json.loads(db.execute("SELECT value FROM meta WHERE key='manifest'").fetchone()[0])
            if schema["format_version"] != VERSION:
                return {}, None
            rows = db.execute("""SELECT section_key,document_id,section_id,path,heading,title,content,
                                       char_start,char_end,document_sha256 FROM sections
                                ORDER BY document_id,char_start""").fetchall()
            require(db.execute("PRAGMA integrity_check").fetchone()[0] == "ok",
                    "Corrupt SQLite index")
            fts_rows = db.execute(
                "SELECT section_key,title,body FROM fts ORDER BY section_key").fetchall()
            require(sorted((r[0],r[5],r[6]) for r in rows) == fts_rows,
                    "FTS records diverge from canonical section rows")
        cols = ("section_key","document_id","section_id","path","heading",
                "title","content","char_start","char_end","document_sha256")
        grouped = {}
        for row in rows:
            section = dict(zip(cols, row))
            grouped.setdefault(section["document_id"], []).append(section)
        return grouped, schema
    except (sqlite3.DatabaseError, ValueError, TypeError, KeyError):
        raise ValueError("Existing section index is corrupt/incompatible; refuse unverified reuse")


def compose(root, previous=None):
    root = Path(root).resolve()
    scan = route_index.canonical_scan(root, allow_partial=True)
    require(scan["documents"], "No validated metadata documents for indexing")
    old, previous_manifest = previous if previous is not None else ({}, None)
    result = []
    reused = 0
    for doc in sorted(scan["documents"], key=lambda item: item["id"]):
        path = root / doc["path"]
        require(not path.is_symlink() and path.is_file()
                and path.resolve().is_relative_to((root / "book").resolve()),
                "Invalid canonical page path " + doc["path"])
        text = path.read_text(encoding="utf-8")
        require(digest(text) == doc["sha256"], "Source file changed during index build")
        cached = old.get(doc["id"], [])
        cached = sorted(cached, key=lambda r: r["char_start"])
        header = route_index.FENCE.match(text)
        safe_cached = (
            cached and header is not None
            and cached[0]["char_start"] == header.end()
            and cached[-1]["char_end"] == len(text)
            and all(r["path"] == doc["path"]
                    and r["document_sha256"] == doc["sha256"]
                    and r["title"] == doc["title"]
                    and r["section_key"] == doc["id"] + "#" + r["section_id"]
                    and type(r["char_start"]) is int
                    and type(r["char_end"]) is int
                    and r["char_start"] < r["char_end"]
                    and r["content"] == text[r["char_start"]:r["char_end"]]
                    for r in cached)
            and all(a["char_end"] == b["char_start"]
                    for a,b in zip(cached,cached[1:]))
        )
        if safe_cached:
            segments = cached
            reused += 1
        else:
            segments = parse_sections(doc, text)
        result.extend(segments)
    result.sort(key=lambda s: (s["document_id"], s["char_start"], s["section_id"]))
    names = [r["section_key"] for r in result]
    require(len(names) == len(set(names)), "Ambiguous section ID; add explicit unique anchors")
    stable = {
        "format_version": VERSION, "route_snapshot_sha256": scan["snapshot_sha256"],
        "coverage": scan["coverage"], "unannotated_paths": scan["unannotated_paths"],
        "document_count": len(scan["documents"]), "section_count": len(result),
        "document_sha256": {d["id"]: d["sha256"] for d in scan["documents"]},
        "index_semantics": "canonical-frontmatter-only; heading anchors or slugs, snapshot scoped",
    }
    stable["snapshot_id"] = digest(canonical_json(stable) + "\n" +
        canonical_json([{k:r[k] for k in ("section_key","char_start","char_end",
                                         "document_sha256")} for r in result]))
    return stable, result, reused


def output_path(root, supplied=None):
    root = Path(root).resolve()
    folder = root / "generated"
    require(folder.is_dir() and not folder.is_symlink(), "Create ordinary generated/ directory explicitly")
    target = Path(supplied) if supplied is not None else folder / INDEX_NAME
    require(target.parent.resolve() == folder.resolve()
            and not target.is_symlink() and target.name.endswith(".sqlite"),
            "Index must be a normal direct file under generated/")
    return target


def publish(root, supplied=None, *, full=False):
    target = output_path(root, supplied)
    previous = ({}, None) if full else old_sections(target)
    manifest, sections, reused = compose(root, previous)
    if previous[1] is not None and previous[1] == manifest and not full:
        verify(root, target)
        return {"outcome": "unchanged", "snapshot": manifest["snapshot_id"],
                "sections": len(sections), "reused_documents": reused}
    temp = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".tycho-fts-", suffix=".sqlite",
                                         dir=target.parent, delete=False) as tmp:
            temp = Path(tmp.name)
        with sqlite3.connect(temp) as db:
            db.execute("PRAGMA page_size=4096")
            db.execute("CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT NOT NULL)")
            db.execute("""CREATE TABLE sections(section_key TEXT PRIMARY KEY,
                       document_id TEXT,section_id TEXT,path TEXT,heading TEXT,
                       title TEXT,content TEXT,char_start INTEGER,char_end INTEGER,
                       document_sha256 TEXT)""")
            try:
                db.execute("CREATE VIRTUAL TABLE fts USING fts5(section_key UNINDEXED,title,body,tokenize='unicode61')")
            except sqlite3.OperationalError as exc:
                raise ValueError("SQLite build lacks FTS5 support") from exc
            data = [(row[k] for k in ("section_key","document_id","section_id","path",
                                     "heading","title","content","char_start","char_end",
                                     "document_sha256")) for row in sections]
            db.executemany("INSERT INTO sections VALUES(?,?,?,?,?,?,?,?,?,?)",
                           [tuple(a) for a in data])
            db.executemany("INSERT INTO fts(section_key,title,body) VALUES(?,?,?)",
                           [(r["section_key"], r["title"], r["content"]) for r in sections])
            db.execute("INSERT INTO meta(key,value) VALUES('manifest',?)", (canonical_json(manifest),))
            require(db.execute("PRAGMA integrity_check").fetchone()[0] == "ok",
                    "SQLite integrity failure")
            db.commit()
        require(json.loads(sqlite3.connect(temp).execute(
            "SELECT value FROM meta WHERE key='manifest'").fetchone()[0]) == manifest,
            "Metadata readback failed")
        os.replace(temp, target)
        temp = None
    finally:
        if temp is not None and temp.exists():
            temp.unlink()
    return {"outcome": "published", "snapshot": manifest["snapshot_id"],
            "sections": len(sections), "reused_documents": reused}


def verify(root, supplied=None):
    target = output_path(root, supplied)
    cached, manifest = old_sections(target)
    require(manifest is not None, "No published section index")
    fresh, actual_rows, _ = compose(root, ({}, None))
    require(fresh == manifest, "Section index stale: canonical source/route snapshot changed")
    cached_rows = [x for rows in cached.values() for x in rows]
    cached_rows.sort(key=lambda x: (x["document_id"],x["char_start"],x["section_id"]))
    require(cached_rows == actual_rows, "Section metadata, offsets or content diverge from book")
    return {"outcome": "verified", "snapshot": manifest["snapshot_id"],
            "coverage": manifest["coverage"], "unannotated_count": len(manifest["unannotated_paths"]),
            "sections": manifest["section_count"]}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("build","check"))
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--index", type=Path)
    ap.add_argument("--full", action="store_true", help="Reparse all documents before atomic publish")
    args = ap.parse_args()
    if args.action == "build":
        result = publish(args.root, args.index, full=args.full)
    else:
        result = verify(args.root, args.index)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
