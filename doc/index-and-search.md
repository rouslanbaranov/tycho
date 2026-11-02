# Index and search

Tycho separates canonical content from generated retrieval artifacts. The book
and metadata are canonical; the route index and section index are derived and
must be rebuildable.

This document describes the route layer, the section index and the search
quality evidence. The MCP transport is described separately in
[MCP layer](mcp-layer.md).

## What is indexed

| Layer | Scope | Artifact |
|---|---|---|
| Route index | Book metadata, paths, topics, routes | `generated/route-index.v1.json` |
| Section index | Page overviews, H2 sections, H3 passages | `generated/sections-fts-v5.sqlite` |
| V12 index | Models, scenarios, runs, decisions | `generated/v12-index.v1.json` |

The current route index covers 612 documents with no unannotated paths. The
section model produces:

- 612 page overviews;
- 2,578 citable H2 sections;
- 504 internal H3 passages.

An H3 passage is rankable and diagnostic. It is not a public citable section;
citations resolve to the owning H2 section.

## Route index

The route index is the deterministic map of the book. Each document record
contains:

- stable document ID and path;
- kind, parent and summary;
- topics, perspectives, questions and keywords;
- related IDs and prerequisites;
- source and claim IDs;
- evidence status;
- content SHA-256.

It is used by the outline, page, search and context tools, and by the generated
navigation and validation checks.

## Section index

The section index is a SQLite FTS5 snapshot. Its schema includes:

- document and section identity;
- canonical path and heading anchor;
- section text and offsets;
- source and claim IDs;
- artifact type and volume;
- pattern links derived from the V12 and reverse indexes.

The index is deterministic over validated pages. It never edits book
frontmatter, fetches remote sources or enriches text.

## Build and inspect

```sh
python3 scripts/section_fts_index.py build --full
python3 scripts/section_fts_index.py check --root .
python3 scripts/section_fts_index.py stats --root .
```

`build` publishes a complete snapshot atomically. `check` verifies that the
current snapshot matches the canonical scan. `stats` reports coverage, sections
and passages.

Incremental mode reuses parsed sections from a valid older index, but it still
publishes a fresh complete SQLite file. It does not claim in-place B-tree
updates or stable heading IDs across a rename.

## Search behavior

The default search layer is lexical. Its contract is:

- return ranked stable IDs and section anchors;
- include bounded excerpts, scores and citation fields;
- enforce query, result and character limits;
- bind results to one snapshot;
- fail closed on a snapshot mismatch;
- disclose partial coverage and unbuilt areas;
- never treat a zero-hit result as proof of absence.

The MCP search tool adds modes and filters. Semantic and hybrid retrieval remain
experiments unless a measured benefit is documented.

## Evaluation

The repository contains several evaluation families:

| Evaluation | Scope | Key count |
|---|---|---:|
| Qrels v4 | Page and section relevance | 150 queries |
| Qrels v5-dense | Dense candidate pool | 4,500 judgments |
| Search quality v5 | Ranking profiles and metrics | Multiple profiles |
| Agent retrieval v5 | Hit-at-k and recall | 150 questions |
| V12 artifact qrels | V12 artifact retrieval | 30 questions |

Qrels v4 has 610 candidate pages/sections, 447 accepted and 188 direct answers.
The v5-dense pool has 4,500 page and 4,500 section judgments, with 997 accepted
pages and 996 accepted sections.

Selected search-quality results for the `3,2,1` profile:

| Level | P@5 | R@5 | MRR | nDCG@5 |
|---|---:|---:|---:|---:|
| Page | 0.4387 | 0.3489 | 0.8360 | 0.6160 |
| Section | 0.2867 | 0.2363 | 0.7138 | 0.4698 |

Agent retrieval hit rates:

| Level | hit@1 | hit@3 | hit@5 |
|---|---:|---:|---:|
| Page | 0.9333 | 0.9933 | 0.9933 |
| Section | 0.8933 | 0.9867 | 0.9933 |

These are AI-adjudicated, pool-relative results. They are not human review,
coverage proof or production latency measurements.

## Snapshot discipline

Every search or read result carries a snapshot ID. If the caller follows a stale
cursor or requests a new snapshot, the service fails closed rather than silently
mixing content. Citation format is `path#section_id`, with the snapshot ID kept
alongside it.

## Why lexical first

The project does not assume that semantic retrieval is better. A lexical
baseline is inspectable, reproducible and cheap to validate. A vector or hybrid
experiment must show a measurable improvement while preserving exact citations,
snapshot consistency and bounded output.

## Limits

- The index is derived; regenerating it is not research.
- 612 route documents do not imply 612 equally reviewed pages.
- Search quality is measured on a finite, AI-labelled pool.
- Section recall is not answer correctness.
- No production latency, availability or concurrency claim is made.
- The SQLite snapshot must be rebuilt after route-index changes.
