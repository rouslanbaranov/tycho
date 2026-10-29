#!/usr/bin/env python3
"""Optional top-1 reranker for BM25 results.

The model is trained on the v2 dev split and is frozen as a JSON artifact.
V12 results and long section-level queries are deliberately not reranked.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "evaluation/top1-reranker.v1.json"
TOKEN = re.compile(r"[^\W_]+")
GENERIC = {
    "purpose-and-mission", "reading-and-navigation", "evidence-and-limits",
    "versioned-public-source-to-claim-ledger",
}
FEATURES = ("bias", "bm25", "rank", "heading_cov", "body_cov", "h3",
            "generic", "query_len")


def tokens(value):
    return set(TOKEN.findall(str(value).casefold()))


def features(query, result, rank):
    terms = tokens(query)
    heading = tokens(result.get("heading", ""))
    body = tokens(result.get("content", ""))
    return [
        1.0,
        float(result.get("score", 0)),
        float(rank),
        len(terms & heading) / max(1, len(terms)),
        len(terms & body) / max(1, len(terms)),
        1.0 if result.get("match_source") == "h3-passage" else 0.0,
        1.0 if result.get("section_id") in GENERIC else 0.0,
        float(len(terms)),
    ]


def skip_reason(query, results):
    if any(result.get("volume") == "v12" for result in results):
        return "skipped-v12"
    if len(tokens(query)) > 16:
        return "skipped-long-query"
    return None


def score(model, vector):
    values = [(value - mean) / (std or 1.0)
              for value, mean, std in zip(vector, model["mean"], model["std"])]
    dot = sum(weight * value for weight, value in zip(model["weights"], values))
    return 1.0 / (1.0 + 2.718281828459045 ** (-dot))


def rerank(query, results, model):
    reason = skip_reason(query, results)
    if reason:
        return list(results), reason
    ordered = sorted(
        enumerate(results, 1),
        key=lambda item: score(model, features(query, item[1], item[0])),
        reverse=True)
    out = []
    for rank, (_, result) in enumerate(ordered, 1):
        item = dict(result)
        item["rerank_score"] = round(
            score(model, features(query, result, rank)), 6)
        item["rerank_mode"] = "top1-logistic"
        out.append(item)
    return out, "reranked"


def load_model(path=MODEL):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if tuple(data.get("feature_order", data.get("features", []))) != FEATURES:
        raise ValueError("reranker feature mismatch")
    return data


def qrels(root):
    rows = []
    for split, relative in (("v2", "evaluation/corpus-qrels.v2.json"),
                            ("p3", "evaluation/agent-qrels.phase3.json"),
                            ("v12", "evaluation/v12-simulation-qrels.v1.json")):
        data = json.loads((Path(root) / relative).read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if split == "p3" and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            rows.append((split, item))
    return rows


def train(root):
    import numpy as np
    import section_search
    train_rows = []
    for split, item in qrels(root):
        if split != "v2":
            continue
        if int(hashlib.sha256(item["id"].encode()).hexdigest()[-1], 16) % 2:
            continue
        results = section_search.search(
            root, item["question"], limit=5, abstain=False).get("results", [])
        accepted = {(a["path"], a.get("section_id"))
                    for a in item.get("accepted", [])}
        for rank, result in enumerate(results, 1):
            label = 1 if ((result["path"], result["section_id"]) in accepted
                          or (result["path"], None) in accepted) else 0
            train_rows.append((features(item["question"], result, rank), label))
    matrix = np.asarray([row[0] for row in train_rows])
    labels = np.asarray([row[1] for row in train_rows])
    mean = matrix.mean(axis=0)
    std = matrix.std(axis=0)
    std[std == 0] = 1.0
    normal = (matrix - mean) / std
    weights = np.zeros(normal.shape[1])
    for _ in range(2000):
        probability = 1.0 / (1.0 + np.exp(-(normal @ weights)))
        gradient = normal.T @ (probability - labels) / len(labels)
        weights -= 0.1 * (gradient + 0.01 * weights)
    model = {
        "schema_version": 1,
        "status": "diagnostic",
        "trained_on": "qrels-v2-dev",
        "feature_order": list(FEATURES),
        "mean": [round(float(value), 8) for value in mean],
        "std": [round(float(value), 8) for value in std],
        "weights": [round(float(value), 8) for value in weights],
        "limits": "Author-labelled dev split; no independent review.",
    }
    MODEL.write_text(json.dumps(model, indent=2, sort_keys=True) + "\n",
                     encoding="utf-8")
    return model


def evaluate(root, model):
    import section_search
    values = []
    for split, item in qrels(root):
        results = section_search.search(
            root, item["question"], limit=5, abstain=False).get("results", [])
        out, _ = rerank(item["question"], results, model)
        accepted = {(a["path"], a.get("section_id"))
                    for a in item.get("accepted", [])}
        rank = None
        for number, result in enumerate(out, 1):
            if ((result["path"], result["section_id"]) in accepted
                    or (result["path"], None) in accepted):
                rank = number
                break
        values.append((split, rank))
    def summary(rows):
        n = len(rows)
        return {k: round(sum(1 for _, rank in rows if rank and rank <= k) / n, 3)
                for k in (1, 3, 5)}
    return {"status": "diagnostic",
            "all": summary(values),
            "v2": summary([v for v in values if v[0] == "v2"]),
            "p3": summary([v for v in values if v[0] == "p3"]),
            "v12": summary([v for v in values if v[0] == "v12"]),
            "limits": "Stale qrels; no quality claim."}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("train", "evaluate"))
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    if args.action == "train":
        print(json.dumps(train(args.root), indent=2, sort_keys=True))
    else:
        print(json.dumps(evaluate(args.root, load_model()), indent=2,
                         sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
