#!/usr/bin/env python3
"""Offline, deterministic Route-Read-Verify over validated book frontmatter.

Reads only already marked-up canonical book pages. Does not infer metadata,
edit prose, fetch public sites, run embeddings or alter source/graph histories.
Explicit --allow-partial marks missing coverage; never reports complete falsely.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/document-metadata.v1.schema.json"
DEFAULT_INDEX = ROOT / "generated/route-index.v1.json"
FENCE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
WORD = re.compile(r"[a-z0-9]+", re.I)
_SCHEMA_CACHE = {}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def engine():
    try:
        import yaml
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as e:
        raise RuntimeError(
            "Install schema and YAML dependencies: python3 -m pip install "
            "-r requirements-validation.txt -r scripts/requirements-routing.txt"
        ) from e
    return yaml, Draft202012Validator, FormatChecker


def canonical_scan(root, allow_partial=False):
    yaml, Draft, Format = engine()
    root = Path(root).resolve()
    book = root / "book"
    require(book.is_dir() and not book.is_symlink(), "book directory missing or symlink")
    schema_path = root / "schemas/document-metadata.v1.schema.json"
    schema_text = schema_path.read_text()
    cache_key = (str(schema_path), schema_text)
    check = _SCHEMA_CACHE.get(cache_key)
    if check is None:
        schema = json.loads(schema_text)
        Draft.check_schema(schema)
        check = Draft(schema, format_checker=Format())
        _SCHEMA_CACHE[cache_key] = check
    docs, skipped, ids, paths = [], [], set(), set()
    for file in sorted(book.rglob("*.md")):
        require(not file.is_symlink(), "unsafe book file/symlink")
        text = file.read_text(encoding="utf-8")
        rel = file.relative_to(root).as_posix()
        header = FENCE.match(text)
        if not header:
            skipped.append(rel)
            continue
        meta = yaml.safe_load(header.group(1))
        require(isinstance(meta, dict), rel + ": YAML root must be a mapping")
        errs = sorted(check.iter_errors(meta), key=lambda x: str(list(x.path)))
        require(not errs, rel + ": invalid strict metadata: " + (errs[0].message if errs else ""))
        require(meta["canonical_path"] == rel, rel + ": metadata path differs from current file")
        require(meta["id"] not in ids and rel not in paths, rel + ": duplicate ID/path")
        ids.add(meta["id"])
        paths.add(rel)
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        docs.append({
            "id": meta["id"], "kind": meta["kind"], "path": rel,
            "parent_id": meta["parent_id"], "related": meta["route_hints"]["related_ids"],
            "prerequisites": meta["route_hints"]["prerequisites"],
            "title": meta["title"], "summary": meta["summary"],
            "questions": meta["route_hints"]["questions"],
            "topics": meta["topic_ids"], "perspectives": meta["perspectives"],
            "keywords": meta["route_hints"]["keywords"],
            "evidence_status": meta["evidence_scope"]["status"],
            "claim_ids": meta["evidence_scope"]["claim_ids"],
            "source_ids": meta["evidence_scope"]["source_ids"],
            "sha256": digest,
        })
    require(docs, "No validated frontmatter pages; refusing empty routing index")
    if skipped and not allow_partial:
        raise ValueError(str(len(skipped)) + " unannotated Markdown pages; use --allow-partial with explicit coverage warning")
    index = {d["id"]: d for d in docs}
    for d in docs:
        parent = d["parent_id"]
        if parent is not None:
            require(parent in index, d["path"] + ": dangling parent " + parent)
        for field in ("related", "prerequisites"):
            for key in d[field]:
                require(key in index, d["path"] + ": dangling " + field + " ID " + key)
    marks = {}
    def visit(key):
        state = marks.get(key, 0)
        require(state != 1, "parent hierarchy cycle involving " + key)
        if state == 2:
            return
        marks[key] = 1
        parent = index[key]["parent_id"]
        if parent is not None:
            visit(parent)
        marks[key] = 2
    for item in index:
        visit(item)
    docs.sort(key=lambda x: x["id"])
    stable = {"schema_version": 1, "metadata_version": 1,
              "coverage": "partial" if skipped else "complete",
              "unannotated_paths": skipped, "documents": docs}
    stable_bytes = json.dumps(stable, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return {**stable, "snapshot_sha256": hashlib.sha256(stable_bytes).hexdigest()}


def load_fresh(root, index_file):
    expected = canonical_scan(root, allow_partial=True)
    actual = json.loads(Path(index_file).read_text(encoding="utf-8"))
    require(actual == expected, "routing index stale or corrupted; rebuild deliberately")
    return actual


def route(index, query, kind=None, limit=5):
    require(isinstance(query, str) and query.strip(), "missing query")
    require(1 <= limit <= 20, "result limit must be 1..20")
    terms = set(WORD.findall(query.lower()))
    scored = []
    for d in index["documents"]:
        if kind and d["kind"] != kind:
            continue
        def hits(value):
            return len(terms.intersection(WORD.findall(value.lower())))
        score = (5*hits(d["title"]) + 4*sum(hits(q) for q in d["questions"])
                 + 3*hits(d["summary"]) + 2*sum(hits(x) for x in d["keywords"]+d["topics"]))
        if score:
            scored.append((score, d))
    scored.sort(key=lambda x: (-x[0], x[1]["id"]))
    return {
        "snapshot_sha256": index["snapshot_sha256"],
        "coverage": index["coverage"],
        "unannotated_pages": len(index["unannotated_paths"]),
        "returned": min(len(scored), limit),
        "truncated": len(scored)>limit,
        "results": [
            {"id": d["id"], "path": d["path"], "title": d["title"],
             "kind": d["kind"], "score": score, "evidence_status": d["evidence_status"]}
            for score,d in scored[:limit]
        ]
    }


def selected(root, index, identity):
    require(isinstance(identity, str), "missing document identity")
    node = next((x for x in index["documents"] if x["id"] == identity), None)
    require(node is not None, "ID not present in validated snapshot")
    path = Path(root) / node["path"]
    require(not path.is_symlink() and path.is_file()
            and path.resolve().is_relative_to((Path(root)/"book").resolve()),
            "book path unsafe or missing")
    text = path.read_text(encoding="utf-8")
    require(hashlib.sha256(text.encode()).hexdigest() == node["sha256"],
            "selected page changed since index snapshot")
    return node, text


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("build", "check", "route", "read", "verify"))
    p.add_argument("--root", type=Path, default=ROOT)
    p.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    p.add_argument("--allow-partial", action="store_true")
    p.add_argument("--query")
    p.add_argument("--kind", choices=("book","volume","chapter","page","landing","decision"))
    p.add_argument("--max-results", type=int, default=5)
    p.add_argument("--id")
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--budget-chars", type=int, default=2000)
    args = p.parse_args()
    if args.action == "build":
        data = canonical_scan(args.root, allow_partial=args.allow_partial)
        args.index.parent.mkdir(parents=True, exist_ok=True)
        args.index.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
        print("Built",len(data["documents"]),"docs; coverage:",data["coverage"])
        return
    current = load_fresh(args.root, args.index)
    require(args.allow_partial or current["coverage"] == "complete",
            "partial routing coverage requires explicit --allow-partial")
    if args.action == "check":
        print("PASS:",current["snapshot_sha256"],current["coverage"])
    elif args.action == "route":
        print(json.dumps(route(current,args.query,kind=args.kind,limit=args.max_results),indent=2))
    else:
        node,text = selected(args.root,current,args.id)
        if args.action == "verify":
            print(json.dumps({"id":node["id"],"snapshot":current["snapshot_sha256"],
                  "page_sha256":node["sha256"],"source_ids":node["source_ids"],
                  "claim_ids":node["claim_ids"],"evidence_status":node["evidence_status"],
                  "notice":"Reference IDs only; technical truth requires separate review."},indent=2))
        else:
            require(0<=args.offset<len(text) and 1<=args.budget_chars<=5000,"invalid bounded read")
            segment = text[args.offset:args.offset+args.budget_chars]
            print(json.dumps({"id":node["id"],"snapshot":current["snapshot_sha256"],
                "offset":args.offset,"next_offset":args.offset+len(segment) if args.offset+len(segment)<len(text) else None,
                "text":segment,"truncated":args.offset+len(segment)<len(text)},ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (ValueError,RuntimeError,OSError) as exc:
        print("FAIL:",exc,file=sys.stderr)
        sys.exit(1)
