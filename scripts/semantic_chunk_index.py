#!/usr/bin/env python3
"""Snapshot-bound semantic index over section-aware chunks."""
import argparse
import json
from pathlib import Path
import sys
import threading

import semantic_chunks

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_fts_index

DEFAULT_MODEL = "minishlab/potion-base-8M"
DEFAULT_EMBEDDINGS = (Path.home() / ".cache/tycho/"
                      "semantic-chunks-v2.npz")
_CACHE = {}
_LOCK = threading.Lock()


def load_model(model_name=DEFAULT_MODEL, backend="model2vec",
               max_seq_length=None):
    key = (model_name, backend, max_seq_length)
    with _LOCK:
        cached = _CACHE.get(key)
    if cached is not None:
        return cached
    if backend == "sentence-transformers":
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(model_name)
        if max_seq_length:
            model.max_seq_length = int(max_seq_length)
    else:
        from model2vec import StaticModel
        model = StaticModel.from_pretrained(model_name)
    with _LOCK:
        _CACHE[key] = model
    return model


def build(root, model_name=DEFAULT_MODEL, output=None,
          backend="model2vec", max_seq_length=None):
    import numpy as np
    output = Path(output or DEFAULT_EMBEDDINGS)
    chunks = semantic_chunks.build_chunks(root)
    model = load_model(model_name, backend, max_seq_length)
    texts = [c["heading"] + "\n" + c["text"] for c in chunks]
    matrix = np.asarray(model.encode(texts, show_progress_bar=False),
                        dtype="float32")
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True).clip(min=1e-9)
    output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        output, matrix=matrix,
        chunk_id=np.asarray([c["chunk_id"] for c in chunks]),
        parent_section_key=np.asarray([c["parent_section_key"] for c in chunks]),
        section_id=np.asarray([c["section_id"] for c in chunks]),
        path=np.asarray([c["path"] for c in chunks]),
        heading=np.asarray([c["heading"] for c in chunks]),
        title=np.asarray([c["title"] for c in chunks]),
        text=np.asarray([c["text"] for c in chunks]),
        char_start=np.asarray([c["char_start"] for c in chunks]),
        char_end=np.asarray([c["char_end"] for c in chunks]),
        word_count=np.asarray([c["word_count"] for c in chunks]))
    meta = {
        "schema_version": 2,
        "model": model_name,
        "backend": backend,
        "max_seq_length": max_seq_length,
        "snapshot": section_fts_index.stats(root)["snapshot"],
        "sections": len({c["parent_section_key"] for c in chunks}),
        "chunks": len(chunks),
        "target_words": semantic_chunks.TARGET,
        "overlap_words": semantic_chunks.OVERLAP,
        "max_words": max(c["word_count"] for c in chunks),
    }
    Path(str(output) + ".json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return meta


def load(root, model_name=DEFAULT_MODEL, path=None,
         backend="model2vec"):
    import numpy as np
    path = Path(path or DEFAULT_EMBEDDINGS)
    meta_path = Path(str(path) + ".json")
    if not path.is_file() or not meta_path.is_file():
        raise RuntimeError("semantic chunk index missing; build it")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    current = section_fts_index.stats(root)["snapshot"]
    if meta.get("snapshot") != current:
        raise RuntimeError("semantic chunk index is stale; rebuild it")
    if meta.get("model") != model_name or meta.get("backend") != backend:
        raise RuntimeError("semantic chunk index model/backend mismatch")
    key = (str(Path(root).resolve()), str(path.resolve()),
           path.stat().st_mtime_ns, model_name, backend)
    with _LOCK:
        cached = _CACHE.get(key)
    if cached is not None:
        return cached
    data = np.load(path)
    result = (data, meta)
    with _LOCK:
        _CACHE[key] = result
    return result


def score_sections(root, query, section_keys, model_name=DEFAULT_MODEL,
                   path=None, backend="model2vec"):
    """Return the best chunk score for selected parent sections only."""
    import numpy as np
    data, meta = load(root, model_name, path, backend)
    model = load_model(model_name, backend, meta.get("max_seq_length"))
    vector = np.asarray(model.encode([query], show_progress_bar=False)[0],
                        dtype="float32")
    vector /= max(float(np.linalg.norm(vector)), 1e-9)
    scores = data["matrix"] @ vector
    wanted = set(section_keys)
    best = {}
    for index, score in enumerate(scores):
        parent = str(data["parent_section_key"][index])
        if parent not in wanted:
            continue
        if score > best.get(parent, -1.0):
            best[parent] = float(score)
    return best


def search(root, query, limit=20, model_name=DEFAULT_MODEL,
           path=None, backend="model2vec"):
    import numpy as np
    data, meta = load(root, model_name, path, backend)
    model = load_model(model_name, backend, meta.get("max_seq_length"))
    vector = np.asarray(model.encode([query], show_progress_bar=False)[0],
                        dtype="float32")
    vector /= max(float(np.linalg.norm(vector)), 1e-9)
    scores = data["matrix"] @ vector
    order = np.argsort(-scores)
    best = {}
    for index in order:
        parent = str(data["parent_section_key"][index])
        if parent in best:
            continue
        best[parent] = {
            "section_key": parent,
            "section_id": str(data["section_id"][index]),
            "path": str(data["path"][index]),
            "heading": str(data["heading"][index]),
            "chunk_id": str(data["chunk_id"][index]),
            "chunk_text": str(data["text"][index]),
            "score": float(scores[index]),
            "word_count": int(data["word_count"][index]),
        }
        if len(best) >= limit:
            break
    return list(best.values()), meta


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("build", "search", "info"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--query")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--backend", choices=("model2vec", "sentence-transformers"),
                        default="model2vec")
    parser.add_argument("--max-seq-length", type=int)
    parser.add_argument("--embeddings", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.action == "build":
        print(json.dumps(build(args.root, args.model, args.embeddings,
                               args.backend, args.max_seq_length),
                         indent=2, sort_keys=True))
    elif args.action == "info":
        _, meta = load(args.root, args.model, args.embeddings, args.backend)
        print(json.dumps(meta, indent=2, sort_keys=True))
    else:
        if not args.query:
            raise SystemExit("--query is required")
        rows, meta = search(args.root, args.query, args.limit, args.model,
                            args.embeddings, args.backend)
        print(json.dumps({"query": args.query, "snapshot": meta["snapshot"],
                          "results": rows}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
