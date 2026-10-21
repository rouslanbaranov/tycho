#!/usr/bin/env python3
"""Tiny in-sample lexical smoke test for three historical pilot reading routes.

No external services, model or search index. This is NOT a retrieval benchmark or
an evaluation of technical answer quality. It only verifies a query-to-chapter
route on a small authored fixture set using a deterministic term overlap model.
"""
import json
import math
import re
from collections import Counter
from pathlib import Path
from directory_paths import HistoricalView

ROOT = Path(__file__).resolve().parents[1]
STOP = set(("the a an of to at in what how when does can is are with without and "
            "or by for on no only give which this it that from then where who why "
            "into under above between about exact if new old be do our same have "
            "should must some after before example how does").split())


def terms(text):
    return [t for t in re.findall(r"[a-z0-9]{3,}", text.lower()) if t not in STOP]


def evaluate():
    data = json.loads((ROOT / "evaluation/pilot-questions.json").read_text())
    cases = data["items"]
    paths = sorted({x["canonical_page"] for x in cases})
    # Keep this historical three-route fixture across the explicit split.
    # This is not a new section-search or answer-quality benchmark.
    manifest_path = ROOT / 'edition/decomposition-manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else None
    view = HistoricalView(ROOT)
    def route_text(path):
        record = next((r for r in manifest['source_bodies'] if r['source_path'] == view.original(path)), None) if manifest else None
        if record is None:
            return (ROOT / path).read_text()
        from decompose_chapters import extract_blocks
        blocks = {}
        for target in {s['target'] for s in record['sections']}:
            blocks.update(extract_blocks(view.path(target).read_text()))
        return ''.join(blocks[(record['source_id'], s['index'])]
                       for s in sorted(record['sections'], key=lambda s: s['index']))
    docs = {path: Counter(terms(route_text(path))) for path in paths}
    lengths = {path: sum(counts.values()) for path, counts in docs.items()}
    df = Counter()
    for counts in docs.values():
        df.update(set(counts))

    def score(query, path):
        tokens = set(terms(query))
        total = 0.0
        for token in tokens:
            tf, found = docs[path][token], df[token]
            if not found:
                continue
            idf = math.log(1 + (len(paths) - found + .5) / (found + .5))
            total += idf * (tf * 2.2) / (
                tf + 1.2 * (0.25 + 0.75 * lengths[path] / 5500))
        return total

    observations = []
    for case in cases:
        ranked = sorted(paths, key=lambda path: (-score(case["question"], path), path))
        predicted = ranked[0]
        observations.append({"id": case["id"], "expected": case["canonical_page"],
                             "top1": predicted, "correct": predicted == case["canonical_page"]})
    return observations


if __name__ == "__main__":
    rows = evaluate()
    correct = sum(r["correct"] for r in rows)
    print(json.dumps({"scope": "pilot-only, in-sample, 3 historical reading routes; no LLM/answer evaluation",
                      "top1_correct": correct, "total": len(rows),
                      "observations": rows}, indent=2))
