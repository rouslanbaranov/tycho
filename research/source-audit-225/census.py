#!/usr/bin/env python3
"""Reproduce the frozen input census; never fetch sources or edit book files."""
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE = "6754bac6e26faa57d65a301a60be10b3da93f65b"
URL = re.compile(r'https?://[^\s<>"\x27`]+')


def normalized(url):
    p = urlsplit(html.unescape(url))
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path, p.query, ""))


def urls(line):
    # Conservative lexical superset: includes prose, code examples and metadata.
    # Balance parentheses so legal URLs retain internal parenthesized paths.
    for match in URL.finditer(line):
        value = match.group().rstrip(".,;:]}\\")
        while value.endswith(")") and value.count(")") > value.count("("):
            value = value[:-1]
        yield value


def write(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main():
    tracked = subprocess.check_output(
        ["git", "ls-tree", "-rz", "--full-tree", BASE], cwd=ROOT
    ).split(b"\0")
    manifest = []
    for item in tracked:
        if not item:
            continue
        header, rawpath = item.split(b"\t", 1)
        path = rawpath.decode()
        mode, kind, oid = header.decode().split()
        assert kind == "blob", path
        payload = (ROOT / path).read_bytes()
        git_oid = hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\0" + payload).hexdigest()
        assert git_oid == oid, "Frozen input changed: " + path
        manifest.append({"path": path, "git_blob": oid, "sha256": hashlib.sha256(payload).hexdigest()})
    sources = json.loads((ROOT / "sources/register.json").read_text())["sources"]
    identities = json.loads((ROOT / "sources/document-identities.json").read_text())["documents"]
    by_url = {}
    for source in sources:
        for key in ("url", "resolved_url"):
            by_url.setdefault(normalized(source[key]), set()).add(source["id"])
    occurrences, pages, candidates = [], [], {}
    for document in sorted(identities, key=lambda d: d["canonical_path"]):
        path = document["canonical_path"]
        text = (ROOT / path).read_text()
        source_ids = sorted(set(re.findall(r"\bsrc\.[a-z0-9]+(?:-[a-z0-9]+)*", text)))
        page_urls = set()
        for number, line in enumerate(text.splitlines(), 1):
            for url in urls(line):
                unit = normalized(url)
                ids = sorted(by_url.get(unit, set()))
                page_urls.add(unit)
                occurrence = {"path": path, "line": number, "url": url, "unit_url": unit, "registered_ids": ids}
                occurrences.append(occurrence)
                project_link = unit.startswith("https://github.com/rouslanbaranov/tycho/")
                classification = "project-tracking-link" if project_link else ("registered-url" if ids else "pending-editorial-classification")
                candidate = candidates.setdefault(unit, {"url": unit, "registered_ids": ids, "pages": [], "classification": classification})
                if path not in candidate["pages"]:
                    candidate["pages"].append(path)
        pages.append({"id": document["id"], "kind": document["kind"], "path": path,
                      "source_ids": source_ids, "external_unit_urls": sorted(page_urls),
                      "review_status": "not-yet-assessed"})
    queue = []
    for source in sources:
        unit = normalized(source["url"])
        queue.append({"source_id": source["id"], "title": source["title"], "url": source["url"],
                      "resolved_url": source["resolved_url"], "baseline_version": source["version"],
                      "kind": source["kind"], "admission": source["admission"],
                      "reading_unit": "pending-scope-definition",
                      "reading_status": "not-started-in-this-audit",
                      "pages_by_source_id": [p["path"] for p in pages if source["id"] in p["source_ids"]],
                      "pages_by_exact_url": candidates.get(unit, {}).get("pages", [])})
    supplemental = [{**c, "reading_unit": "pending-scope-definition", "reading_status": "not-started-in-this-audit"}
                    for c in sorted(candidates.values(), key=lambda c: c["url"])
                    if not c["registered_ids"] and c["classification"] != "project-tracking-link"]
    summary = {"baseline_commit": BASE, "registered_sources": len(sources),
               "canonical_documents": len(pages), "tracked_input_files": len(manifest),
               "external_url_occurrences": len(occurrences), "distinct_fragmentless_urls": len(candidates),
               "urls_without_exact_register_match": sum(not c["registered_ids"] for c in candidates.values()),
               "project_tracking_urls": sum(c["classification"] == "project-tracking-link" for c in candidates.values()),
               "supplemental_source_url_candidates": len(supplemental),
               "scope": "All canonical Markdown bytes scanned, including frontmatter and code. URL candidates are not all evidence citations. Fragment removal only; no inferred redirect or publication equivalence. Inventory is not reading or claim verification."}
    assert len(pages) == 406 and len(sources) == 247
    assert {p["path"] for p in pages} == {p.relative_to(ROOT).as_posix() for p in (ROOT / "book").rglob("*.md")}
    write("baseline-files.json", manifest)
    write("source-queue.json", queue)
    write("supplemental-queue.json", supplemental)
    write("page-census.json", pages)
    write("url-occurrences.json", occurrences)
    write("url-candidates.json", sorted(candidates.values(), key=lambda c: c["url"]))
    write("census-summary.json", summary)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
