"""Shared MCP result and metadata helpers."""
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

import section_search
from mcp_contract import CONTENT_TRUST


def answerability(payload):
    if payload.get("answerability"):
        return dict(payload["answerability"])
    if payload.get("status") == "no-results":
        state = "no-results"
        zero = True
        basis = "zero-results"
    else:
        state = "not-assessed"
        zero = None
        basis = "uncalibrated"
    return {
        "answerable": None,
        "no_confident_answer": zero,
        "state": state,
        "confident": False,
        "basis": basis,
        "caveat": (
            "Lexical retrieval has no calibrated abstention or answer "
            "correctness metric; zero results are not proof of absence."
        ),
    }


def snapshot_mismatch(requested, current):
    if requested is None or requested == current:
        return None
    return {
        "status": "snapshot-mismatch",
        "error": "Requested snapshot does not match the published index",
        "requested_snapshot": requested,
        "current_snapshot": current,
        "content_trust": CONTENT_TRUST,
    }


def registry_mismatch(requested, current):
    if requested is None or requested == current:
        return None
    return {
        "status": "snapshot-mismatch",
        "error": "Requested pattern-registry snapshot does not match",
        "requested_registry_snapshot": requested,
        "current_registry_snapshot": current,
        "content_trust": CONTENT_TRUST,
    }


def coverage_summary(patterns):
    counts = {}
    for pattern in patterns:
        state = (pattern.get("coverage") or {}).get("overall", "unknown")
        counts[state] = counts.get(state, 0) + 1
    return counts


def read_frontmatter(root, path):
    try:
        text = (Path(root) / path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}
    if yaml is None or not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    try:
        value = yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        return {}
    return value if isinstance(value, dict) else {}


def related_ids(frontmatter):
    if not isinstance(frontmatter, dict):
        return []
    return list(frontmatter.get("related_ids")
                or frontmatter.get("route_hints", {}).get("related_ids", []))


def resolve_related(root, ids):
    metadata = section_search.load_document_metadata(root)
    by_id = {doc.get("id"): doc for doc in metadata.values() if doc.get("id")}
    out = []
    for doc_id in ids or []:
        doc = by_id.get(doc_id)
        if doc:
            out.append({"id": doc_id, "path": doc.get("path"),
                        "title": doc.get("title"), "kind": doc.get("kind")})
    return out
