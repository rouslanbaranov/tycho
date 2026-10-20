---
metadata_version: 1
id: "tycho.page.64f398c0535345258b1fdf5eebbf4438"
kind: "page"
parent_id: "tycho.chapter.1f0c8323023f4adfaa1affc7bf2993d4"
canonical_path: "book/volumes/v06/c06/graph-provenance.md"
title: "Derived relationships and falsification"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Which source and update contract makes a derived edge usable?"
route_hints:
  questions:
    - "Which source and update contract makes a derived edge usable?"
  prerequisites:
    - "tycho.page.6d8377d616c548ef9c3b213d8a2df934"
  related_ids:
    - "tycho.chapter.1f0c8323023f4adfaa1affc7bf2993d4"
    - "tycho.page.d34afc7f27b54431b779f7f75f11e2c3"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "graph"
    - "provenance"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.d34afc7f27b54431b779f7f75f11e2c3; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Derived relationships and falsification

**Owning question:** Which source and update contract makes a derived edge usable?

This page belongs to [V06/C06 — Graph relationships and traversal](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:5 -->
## 5. Derived graphs and provenance

A dependency edge extracted from a software build has different authority from a human-reviewed architectural statement. A graph constructed from source references should record:
- source file/version or admitted document;
- inference/extraction method and date;
- confidence or evidence status;
- edge freshness and deprecation/removal rule;
- ownership of conflict resolution.

An edge is not fact merely because a visualization draws it. Source revision drift can invalidate it. For a system design reference book, **there is no requirement to materialize a graph service**: ordinary cross-references and precise source/claim links may be enough to explain the architecture.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:6 -->
## 6. Architecture decision and falsifiable benchmark

**Original synthetic decision:** keep the equipment dependency model in normalized relational tables at first. A graph engine becomes a conditional candidate if representative deep reachability/path questions dominate, static join/CTE approaches cannot meet the required latency/complexity, and operational/recovery/security constraints favor it.

A fair experiment would compare:
- identical entity/edge snapshot, degree distribution and mutation volume;
- equivalent permission/time filters and path semantics;
- query mix across one-hop, deep reachability and negative cases;
- p95/p99, CPU, memory, index/build cost and data freshness;
- update and deletion correctness, cycles and duplicate edges;
- recovery cost and total operations.

Reject any claimed advantage caused by returning fewer paths, omitting authorization or changing the query semantics. **No such test was performed.**

<!-- /tycho-question-source -->

## Original stale-edge counterexample

Imagine an illustrative edge stating that component A depends on B in snapshot S1. A later source revision S2 removes the call, but an independently rebuilt relationship store still serves the S1 edge. A query can traverse a syntactically valid path and nevertheless answer the wrong temporal question. The existence of an edge and successful query execution do not establish current source support.

Carry the inspected source identity, relation meaning and snapshot membership into any derived relationship. An update can mark a relationship stale or unknown instead of asserting that the absence of a new inspection proves removal. Conversely, deleting the stale edge must not silently erase the historical reason it once existed.

A useful negative experiment asks the same dependency question against S1, S2 and a mixed snapshot. Accept the historical answer only with S1 attribution; reject the mixed-snapshot conclusion or disclose the unresolved evidence. This is original conceptual reasoning. It introduces no curated Tycho graph implementation, empirical graph benchmark or inferred causal relationship.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](bounded-traversal.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](graph-data-models-and-traversal.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
