#!/usr/bin/env python3
"""Section-aware semantic chunks for Tycho H2 sections.

Chunks target 200 words with a 40-word (20%) overlap. Ends prefer sentence,
paragraph and heading boundaries. Every chunk retains its parent H2 section.
"""
import argparse
import json
from pathlib import Path
import re
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "generated/sections-fts-v5.sqlite"
WORD = re.compile(r"\S+")
TARGET = 200
MIN_WORDS = 180
MAX_WORDS = 250
OVERLAP = 40


def word_spans(text):
    return list(WORD.finditer(text))


def boundary(text, spans, index):
    word = spans[index].group()
    if word.endswith((".", "!", "?", ":", ";")):
        return True
    if index + 1 >= len(spans):
        return True
    gap = text[spans[index].end():spans[index + 1].start()]
    return "\n\n" in gap or "\n#" in gap or "#" in gap


def split_section(content, target=TARGET, min_words=MIN_WORDS,
                  max_words=MAX_WORDS, overlap=OVERLAP):
    """Return [(char_start, char_end, word_count)] for one H2 body."""
    spans = word_spans(content)
    n = len(spans)
    if n == 0:
        return []
    if n <= max_words:
        return [(spans[0].start(), spans[-1].end(), n)]
    chunks = []
    start = 0
    while start < n:
        if n - start <= max_words:
            end = n
        else:
            low = min(n, start + min_words)
            high = min(n, start + max_words)
            candidates = [i + 1 for i in range(low - 1, high)
                          if boundary(content, spans, i)]
            hint = start + target
            end = (min(candidates, key=lambda value: abs(value - hint))
                   if candidates else min(n, hint))
        char_start = spans[start].start()
        char_end = spans[end - 1].end()
        chunks.append((char_start, char_end, end - start))
        if end >= n:
            break
        start = max(start + 1, end - overlap)
    return chunks


def h2_sections(root, index_path=None):
    target = Path(index_path) if index_path else Path(root) / "generated/sections-fts-v5.sqlite"
    with sqlite3.connect("file:" + target.resolve().as_posix() + "?mode=ro",
                         uri=True) as db:
        db.row_factory = sqlite3.Row
        rows = db.execute(
            "select section_key, section_id, path, heading, title, content"
            " from sections where heading_level=2").fetchall()
    return [dict(row) for row in rows]


def build_chunks(root, index_path=None):
    chunks = []
    for section in h2_sections(root, index_path):
        content = section.get("content") or ""
        for number, (start, end, words) in enumerate(split_section(content)):
            body = content[start:end].strip()
            chunks.append({
                "chunk_id": section["section_key"] + "#chunk-" + str(number),
                "parent_section_key": section["section_key"],
                "section_id": section["section_id"],
                "path": section["path"],
                "heading": section["heading"],
                "title": section["title"],
                "text": body,
                "char_start": start,
                "char_end": end,
                "word_count": words,
            })
    return chunks


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--index", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    chunks = build_chunks(args.root, args.index)
    result = {"sections": len({c["parent_section_key"] for c in chunks}),
              "chunks": len(chunks),
              "min_words": min(c["word_count"] for c in chunks),
              "max_words": max(c["word_count"] for c in chunks)}
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
