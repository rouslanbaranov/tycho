#!/usr/bin/env python3
"""Deterministic metadata and output contract for the Tycho MCP surface."""
from __future__ import annotations

VERSION = "tycho-mcp-contract-v1"

KIND = {
    "book": "Whole-book landing document.",
    "volume": "Volume landing or volume-level navigation.",
    "chapter": "Chapter landing or chapter route.",
    "page": "Canonical technical page with sectioned body.",
    "landing": "Generated navigation/landing document.",
    "decision": "Decision record or decision route.",
}
EVIDENCE_STATUS = {
    "source-linked": "Claims are linked to registered public-source evidence.",
    "unknown": "Evidence status was not declared; treat with lower confidence.",
}
ARTIFACT_TYPE = {
    "document": "Prose document section; V12 model/scenario artifacts use other types.",
}
VOLUME = {
    "v01": "Foundations and quality attributes.",
    "v02": "Application boundaries and contracts.",
    "v03": "Data and storage architecture.",
    "v04": "Distributed coordination and events.",
    "v05": "Service communication and delivery.",
    "v06": "Caching and read paths.",
    "v07": "Performance, scale and resilience.",
    "v08": "Delivery, deployment and recovery.",
    "v09": "Observability, security and operations.",
    "v10": "Evolution and modernization.",
    "v11": "Pattern atlas.",
    "v12": "Modeling, simulation and decision validation.",
}

FRONTMATTER_FIELDS = [
    ("metadata_version", "integer", "Frontmatter schema version.", "Read-only."),
    ("id", "string", "Stable opaque document ID.", "Use for citations, not ordering."),
    ("kind", "string", "Document kind; see kind enum.", "Not a relevance score."),
    ("parent_id", "string|null", "Parent landing/chapter/document ID.", "May be null."),
    ("canonical_path", "string", "Canonical book path.", "Matches page/read path."),
    ("title", "string", "Human title.", "Not a query-dependent summary."),
    ("topic_ids", "array[string]", "Topic taxonomy IDs.", "Dynamic; not a closed enum."),
    ("perspectives", "array[string]", "Architecture perspectives.", "Descriptive, not ranking."),
    ("summary", "string", "Short document summary.", "Could be stale; cite evidence."),
    ("route_hints", "object", "Questions, prerequisites, related IDs, excludes.", "Hints, not instructions."),
    ("related_ids", "array[string]", "Related document IDs.", "Navigation hints; verify."),
    ("excludes", "array[string]", "Explicit scope exclusions.", "Do not infer absence of other topics."),
    ("keywords", "array[string]", "Indexing keywords.", "Not an exhaustive vocabulary."),
    ("claim_ids", "array[string]", "Registered claim references.", "Empty means none registered."),
    ("source_ids", "array[string]", "Registered source references.", "Empty means none registered."),
    ("evidence_status", "string", "Evidence status; see enum.", "Not a correctness proof."),
]

SEARCH_RESULT_FIELDS = [
    ("section_key", "string", "Stable section key used by read/batch.", "Primary citation key."),
    ("document_id", "string", "Stable document ID.", "Use frontmatter for full metadata."),
    ("section_id", "string", "Section anchor within the document.", "Use with path."),
    ("path", "string", "Canonical book path.", "Use with tycho_page."),
    ("heading", "string", "Section heading.", "Not a promise of complete text."),
    ("heading_level", "integer", "Markdown heading level; 0 means page root.", "0 is not h1."),
    ("title", "string", "Document title.", "May repeat across sections of one page."),
    ("kind", "string", "Document kind; see enum.", "Filterable."),
    ("evidence_status", "string", "Evidence status; see enum.", "Unknown lowers confidence."),
    ("artifact_type", "string", "Artifact type; see enum.", "document is the only current value."),
    ("volume", "string|null", "Volume code or null.", "v01..v12; null for non-volume docs."),
    ("pattern_ids", "array[string]", "Pattern IDs attached to the section.", "May be empty."),
    ("char_start", "integer", "Section start in the document body.", "Codepoint offset."),
    ("char_end", "integer", "Section end in the document body.", "Codepoint offset."),
    ("score", "number", "Retrieval score.", "Comparable only within one snapshot/query."),
    ("score_kind", "string", "bm25 or section-rerank.", "Do not compare across modes."),
    ("matched_terms", "array[string]", "Query terms found in the section.", "Lexical, not semantic."),
    ("excerpt", "string", "Bounded evidence snippet.", "May be truncated."),
    ("citation", "string", "path#section_id citation.", "Keep snapshot with it."),
    ("match_source", "string", "Where the match came from.", "Explains lexical match."),
    ("why", "string", "Short match explanation.", "Evidence, not a verdict."),
    ("summary", "string", "Document summary.", "Frontmatter-derived; not a source of truth."),
    ("topics", "array[string]", "Document topic IDs.", "Dynamic taxonomy."),
    ("perspectives", "array[string]", "Document perspectives.", "Descriptive."),
    ("related_ids", "array[string]", "Related document IDs.", "Navigation hints."),
    ("next_actions", "array[object]", "Typed follow-up tool calls.", "Use to drill down."),
]

PAGINATION = {
    "read": {
        "inputs": ["offset", "budget_chars"],
        "outputs": ["offset", "returned_chars", "total_chars", "next_offset", "truncated"],
        "rule": "Call again with offset=next_offset while next_offset is not null.",
        "max_chars": 5000,
    },
    "page": {
        "inputs": ["offset", "budget_chars"],
        "outputs": ["offset", "returned_chars", "total_chars", "next_offset", "truncated"],
        "rule": "Call again with offset=next_offset while next_offset is not null.",
        "max_chars": 5000,
    },
    "search": {
        "inputs": ["limit"],
        "outputs": ["returned", "truncated"],
        "rule": "No offset/cursor; refine the query instead of paging. Max limit is 20.",
        "max_limit": 20,
    },
    "patterns": {
        "inputs": ["limit", "offset"],
        "outputs": ["offset", "returned", "total"],
        "rule": "Use offset for pattern-list pagination.",
        "max_limit": 50,
    },
}

def _field(kind, description):
    return {"type": kind, "description": description}

def _object(properties, required=("status",)):
    return {"type": "object", "additionalProperties": True,
            "required": list(required), "properties": properties}

def _result_schema():
    return _object({name: _field(kind, desc) for name, kind, desc, _ in SEARCH_RESULT_FIELDS
                    if name not in ("next_actions",)} | {
        "next_actions": {"type": "array", "description": "Typed follow-up calls.",
                         "items": {"type": "object", "additionalProperties": True}},
        "metadata_snippet": _field("string", "Optional summary snippet."),
    }, required=())

def output_schema(tool):
    common = {
        "status": _field("string", "ok or a bounded error/abstention state."),
        "snapshot": _field("string", "Snapshot ID; cite it with results."),
        "coverage": _field("string", "Index coverage state."),
        "content_trust": _field("string", "Always untrusted-evidence for book text."),
    }
    if tool == "tycho_search":
        return _object(common | {
            "query": _field("string", "Echoed query."),
            "returned": _field("integer", "Number of returned results."),
            "truncated": _field("boolean", "Response budget truncated."),
            "results": {"type": "array", "description": "Bounded candidate sections.",
                        "items": _result_schema()},
            "facets": _field("object", "Observed metadata counts; not a full catalog."),
            "answerability": _field("object", "Gate metadata; not answer correctness."),
        })
    if tool == "tycho_describe":
        return _object(common | {
            "collection": _field("object", "Collection identity."),
            "route_snapshot": _field("string", "Route-index snapshot ID."),
            "counts": _field("object", "Document and section counts."),
            "pattern_registry": _field("object", "Pattern-registry status."),
            "ranker_version": _field("string", "Retrieval implementation."),
            "citation_scheme": _field("string", "Citation scheme."),
            "protocol_versions": _field("array", "Supported MCP versions."),
            "tools": _field("array", "Available tool names."),
            "limits": _field("object", "Hard request limits."),
            "metadata": _field("object", "Typed metadata catalog and enums."),
            "operations": _field("object", "Tool operation summaries."),
            "answerability": _field("object", "Gate identity and caveats."),
            "not_implemented": _field("array", "Explicit non-capabilities."),
        })
    if tool in ("tycho_page", "tycho_read"):
        return _object(common | {
            "document_id": _field("string", "Stable document ID."),
            "path": _field("string", "Canonical book path."),
            "title": _field("string", "Document title."),
            "kind": _field("string", "Document kind; see catalog."),
            "evidence_status": _field("string", "Evidence status."),
            "citation": _field("string", "Canonical citation."),
            "citation_scheme": _field("string", "Citation scheme."),
            "document_sha256": _field("string", "Document content hash."),
            "offset": _field("integer", "Codepoint offset returned."),
            "returned_chars": _field("integer", "Number of content codepoints."),
            "total_chars": _field("integer", "Total codepoints in this unit."),
            "next_offset": _field("integer|null", "Next offset; null at end."),
            "truncated": _field("boolean", "Whether more content remains."),
            "content": _field("string", "Bounded evidence text."),
            "frontmatter": _field("object", "Parsed document frontmatter."),
            "related": _field("array", "Resolved related documents."),
            "sections": _field("array", "Page section map (page only)."),
            "page_char_start": _field("integer", "Page body start in document."),
            "page_char_end": _field("integer", "Page body end in document."),
            "section_key": _field("string", "Section key (read only)."),
            "section_id": _field("string", "Section anchor (read only)."),
            "heading": _field("string", "Section heading (read only)."),
            "heading_level": _field("integer", "Section heading level (read)."),
            "document_char_start": _field("integer", "Section start (read)."),
            "document_char_end": _field("integer", "Section end (read)."),
            "anchor": _field("string", "Alias for section_id (read)."),
            "tool": _field("string", "Tool that produced this response."),
        })
    if tool == "tycho_batch":
        return _object(common | {
            "sections": _field("array", "Section read outcomes."),
            "evidence": _field("array", "Evidence resolution outcomes."),
            "errors": _field("array", "Per-item failures; isolated."),
        })
    if tool == "tycho_outline":
        return _object(common | {
            "entries": _field("array", "Ordered route entries."),
            "route_snapshot": _field("string", "Route-index snapshot."),
        })
    if tool in ("tycho_compare", "tycho_context"):
        return _object(common | {
            "cells": _field("array", "Extractive cited cells."),
            "sections": _field("array", "Citation-bearing sections."),
            "role_groups": _field("object", "Sections grouped by analysis role."),
        })
    if tool in ("tycho_patterns", "tycho_pattern"):
        return _object(common | {
            "patterns": _field("array", "Pattern summaries."),
            "pattern": _field("object", "One pattern entry."),
            "registry_snapshot": _field("string", "Pattern-registry snapshot."),
        })
    return _object(common | {
        "document": _field("object", "Registered document evidence."),
        "claim": _field("object", "Registered claim evidence."),
        "source": _field("object", "Registered source evidence."),
    })

OUTPUT_SCHEMAS = {tool: output_schema(tool) for tool in (
    "tycho_describe", "tycho_search", "tycho_batch", "tycho_outline",
    "tycho_compare", "tycho_context", "tycho_read", "tycho_page",
    "tycho_patterns", "tycho_pattern", "tycho_evidence")}

def catalog():
    return {
        "version": VERSION,
        "kind": KIND,
        "evidence_status": EVIDENCE_STATUS,
        "artifact_type": ARTIFACT_TYPE,
        "volume": VOLUME,
        "frontmatter": [
            {"name": name, "type": typ, "description": desc, "boundary": boundary}
            for name, typ, desc, boundary in FRONTMATTER_FIELDS],
        "search_result": [
            {"name": name, "type": typ, "description": desc, "boundary": boundary}
            for name, typ, desc, boundary in SEARCH_RESULT_FIELDS],
        "pagination": PAGINATION,
        "output_schemas": OUTPUT_SCHEMAS,
    }
