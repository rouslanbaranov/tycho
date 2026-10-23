#!/usr/bin/env python3
"""Evidence-aware refusal gate trained on the phase-2 agent qrels.

The model uses retrieval confidence, lexical evidence coverage, query scope
signals and a small bag of query tokens. It is an agent-adjudicated diagnostic,
not human review, answer correctness or a sufficiency claim.
"""
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "edition/patterns/evidence-gate.v1.json"
VERSION = "tycho-evidence-gate-v1"
TOKEN = re.compile(r"[a-z0-9]+")
SCOPE = {
    "vendor": re.compile(
        r"\b(vendor|provider|product|managed|named|specific|particular)\b",
        re.I),
    "current": re.compile(
        r"\b(current|today|price|cost|charge|latest|retire|version)\b", re.I),
    "production": re.compile(
        r"\b(our\s+(production|cluster|company|tenant)|last\s+(month|week)|"
        r"auditor|payroll)\b", re.I),
    "exact": re.compile(
        r"\b(exact|p99|how\s+many\s+nodes|throughput|capacity)\b", re.I),
    "org": re.compile(
        r"\b(team\s+size|data\s+residency|slo\s+target|should\s+our)\b",
        re.I),
}
FEATURES = [
    "score", "score_per_term", "coverage", "heading", "margin",
    "margin_ratio", "returned", "unknown", "q_len", "phrase",
    "scope_count", "vendor", "current", "production", "exact", "org",
]


def tokens(text):
    return [item for item in TOKEN.findall(text.casefold())]


def unique_terms(query):
    out = []
    for term in tokens(query):
        if term not in out:
            out.append(term)
    return out


def phrase_ratio(query, text):
    query_terms = tokens(query)
    body = tokens(text)
    best = 0
    for start in range(len(query_terms)):
        for end in range(start + 1, len(query_terms) + 1):
            seq = query_terms[start:end]
            for pos in range(len(body) - len(seq) + 1):
                if body[pos:pos + len(seq)] == seq:
                    best = max(best, len(seq))
                    break
    return best / len(query_terms) if query_terms else 0.0


def extract_features(query, results, unknown_rate):
    terms = unique_terms(query)
    top = results[0] if results else None
    heading = " ".join([top.get("title", ""), top.get("heading", "")]).casefold() if top else ""
    text = " ".join((top.get("excerpt", "") if top else "").split())
    scores = [item.get("score", 0.0) for item in results]
    mean = sum(scores) / len(scores) if scores else 0.0
    variance = sum((score - mean) ** 2 for score in scores) / len(scores) if scores else 0.0
    return {
        "score": top.get("score", 0.0) if top else 0.0,
        "score_per_term": (top.get("score", 0.0) / len(terms)) if top and terms else 0.0,
        "coverage": (len(top.get("matched_terms", [])) / len(terms)) if top and terms else 0.0,
        "heading": (sum(1 for term in terms if term in heading) / len(terms)) if terms else 0.0,
        "margin": (scores[0] - scores[1]) if len(scores) > 1 else (scores[0] if scores else 0.0),
        "margin_ratio": ((scores[0] - scores[1]) / (scores[0] + 1e-6)) if len(scores) > 1 else 0.0,
        "returned": len(results),
        "unknown": unknown_rate,
        "q_len": len(terms),
        "phrase": phrase_ratio(query, text),
        "scope_count": 0,
        "vendor": 0,
        "current": 0,
        "production": 0,
        "exact": 0,
        "org": 0,
    } | {
        name: 1.0 if pattern.search(query) else 0.0
        for name, pattern in SCOPE.items()
    } | {"scope_count": sum(
        1.0 for pattern in SCOPE.values() if pattern.search(query))}


def load_model(path=MODEL_PATH):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def probability(model, query, features):
    total = model["weights"].get("bias", 0.0)
    for name, mean, std in zip(
            model["numeric_features"], model["means"], model["stds"]):
        value = (features[name] - mean) / (std or 1.0)
        total += model["weights"].get("n:" + name, 0.0) * value
    for token in set(tokens(query)):
        total += model["weights"].get("t:" + token, 0.0)
    return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, total))))


def assess(query, results, unknown_rate, model=None):
    model = model or load_model()
    if not model:
        return None
    features = extract_features(query, results, unknown_rate)
    score = probability(model, query, features)
    abstain = score >= model["threshold"]
    return {
        "version": VERSION,
        "model": model["version"],
        "answerable": None,
        "no_confident_answer": abstain,
        "confident": False,
        "state": "abstained" if abstain else "not-calibrated-answer",
        "basis": "evidence-score-threshold" if abstain else "below-threshold",
        "probability_unanswerable": round(score, 6),
        "threshold": model["threshold"],
        "features": {key: round(value, 6) for key, value in features.items()},
        "caveat": (
            "Trained on agent-adjudicated phase-2 dev data; not human review, "
            "not answer correctness and not sufficient coverage."
        ),
    }
