#!/usr/bin/env python3
"""Offline Markdown navigation and bounded structural validation for Tycho.

No source fetching, formatting or enrichment. Reports only relative file paths,
line numbers and rule codes, not restricted prose. Anchor normalization is a
conservative GitHub-style approximation, not a full Markdown renderer.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"^\s*(`{3,}|~{3,})[^\r\n]*$")
HEAD = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
LINK = re.compile(r"(?<!!)\[[^\]\n]{1,1500}\]\(([^)\n]+)\)")
INLINE = re.compile(r"`[^`\n]*`")


def slug_heading(label):
    """Best-effort conservative rendering of a common Markdown heading ID."""
    text = re.sub(r"<[^>]*>", "", label)
    text = INLINE.sub(lambda m: m.group(0).strip("`"), text)
    text = text.strip().rstrip("#").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)


def parse_document(content):
    headings, links, warnings, fenced = set(), [], [], None
    seen = Counter()
    heading_count = 0
    for number,line in enumerate(content.splitlines(),1):
        m = FENCE.match(line)
        if m:
            marker = m.group(1)
            if fenced is None:
                fenced=(marker[0],len(marker),number)
            elif marker[0]==fenced[0] and len(marker)>=fenced[1]:
                fenced=None
            continue
        if fenced is not None:
            continue
        h = HEAD.match(line)
        if h:
            key=slug_heading(h.group(2))
            if key:
                n=seen[key]
                headings.add(key if n==0 else key+"-"+str(n))
                seen[key]+=1
                heading_count+=1
        # Do not interpret inline backtick literals as links. This is a
        # conservative lexical check, not a full CommonMark parser.
        visible=INLINE.sub("",line)
        for link in LINK.finditer(visible):
            links.append((number,link.group(1).strip()))
    if fenced is not None:
        warnings.append((fenced[2],"unclosed-fence"))
    if heading_count==0:
        warnings.append((1,"missing-heading"))
    return headings,links,warnings


def resolve_target(repo_root,source,raw):
    # Markdown links to external sources are citation responsibilities of
    # provenance review; this checker only validates internal targets.
    value=raw.strip().split(" ",1)[0].strip("<>")
    if value.startswith(("http://","https://","mailto:","data:")):
        return None
    parts=urlsplit(value)
    if parts.scheme or parts.netloc:
        return None
    target=unquote(parts.path)
    fragment=unquote(parts.fragment)
    if target.startswith("/") or "\\" in target or ".git" in target.split("/"):
        raise ValueError("unsafe-local-path")
    source_relative=source.relative_to(repo_root).as_posix()
    combined=posixpath.normpath(posixpath.join(posixpath.dirname(source_relative),target)) if target else source_relative
    if combined==".." or combined.startswith("../") or combined.startswith("/"):
        raise ValueError("escapes-repository")
    dest=repo_root/combined
    if dest.is_dir():
        dest=dest/"README.md"
    if dest.is_symlink() or not dest.is_file() or not dest.resolve().is_relative_to(repo_root.resolve()):
        raise ValueError("missing-local-target")
    return dest,fragment


def validate_tree(root=ROOT,max_page_chars=120000):
    root=Path(root).resolve()
    book=root/"book"
    if not book.is_dir() or book.is_symlink():
        raise ValueError("Missing non-symlink book directory")
    if not 1000 <= max_page_chars <= 500000:
        raise ValueError("max_page_chars must be 1000..500000")
    files=sorted(book.rglob("*.md"))
    issues=[]
    parsed={}
    for file in files:
        relative=file.relative_to(root).as_posix()
        if file.is_symlink():
            issues.append({"path":relative,"line":1,"rule":"symlink-forbidden"})
            continue
        try:
            content=file.read_text(encoding="utf-8")
        except (UnicodeError,OSError):
            issues.append({"path":relative,"line":1,"rule":"unreadable-utf8"})
            continue
        headings,links,warnings=parse_document(content)
        parsed[file]=(headings,links)
        for line,rule in warnings:
            issues.append({"path":relative,"line":line,"rule":rule})
        if len(content)>max_page_chars:
            issues.append({"path":relative,"line":1,"rule":"page-size-safety-cap"})
        if file.name=="README.md":
            lower=content.lower()
            if "purpose" not in lower or "mission" not in lower:
                issues.append({"path":relative,"line":1,"rule":"landing-missing-purpose-mission"})
            if len(files)>1 and not links:
                issues.append({"path":relative,"line":1,"rule":"landing-missing-internal-navigation"})
    for file,(_,links) in parsed.items():
        relative=file.relative_to(root).as_posix()
        for line,value in links:
            try:
                target=resolve_target(root,file,value)
            except ValueError as exc:
                issues.append({"path":relative,"line":line,"rule":str(exc)})
                continue
            if target is None:
                continue
            dest,frag=target
            if frag and dest.suffix.lower()==".md":
                if dest not in parsed:
                    # A target outside /book can be existing and valid; this
                    # check scans its headings individually without private prose.
                    try:
                        anchors=parse_document(dest.read_text(encoding="utf-8"))[0]
                    except (UnicodeError,OSError):
                        issues.append({"path":relative,"line":line,"rule":"unreadable-anchor-target"})
                        continue
                else:
                    anchors=parsed[dest][0]
                if frag.lower() not in anchors:
                    issues.append({"path":relative,"line":line,"rule":"missing-local-anchor"})
    issues.sort(key=lambda x:(x["path"],x["line"],x["rule"]))
    return {"pages_checked":len(files),"issue_count":len(issues),"issues":issues,
            "scope":"structural-only; links and approximate anchors, not claim truth or review"}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,default=ROOT)
    p.add_argument("--max-page-chars",type=int,default=120000)
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    result=validate_tree(args.root,args.max_page_chars)
    if args.json:
        print(json.dumps(result,indent=2))
    else:
        print("Checked",result["pages_checked"],"book pages; issues",result["issue_count"])
        for issue in result["issues"]:
            print(issue["path"]+":"+str(issue["line"])+": "+issue["rule"])
    if result["issue_count"]:
        sys.exit(1)


if __name__=="__main__":
    main()
