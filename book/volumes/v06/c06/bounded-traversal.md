---
metadata_version: 1
id: "tycho.page.6d8377d616c548ef9c3b213d8a2df934"
kind: "page"
parent_id: "tycho.chapter.1f0c8323023f4adfaa1affc7bf2993d4"
canonical_path: "book/volumes/v06/c06/bounded-traversal.md"
title: "Bounded graph traversal and relational alternatives"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "What direction, cycle and result limits make the traversal question precise?"
route_hints:
  questions:
    - "What direction, cycle and result limits make the traversal question precise?"
  prerequisites:
    - "tycho.page.ae4febbe43f941f78d825613e126419b"
  related_ids:
    - "tycho.chapter.1f0c8323023f4adfaa1affc7bf2993d4"
    - "tycho.page.d34afc7f27b54431b779f7f75f11e2c3"
    - "tycho.page.64f398c0535345258b1fdf5eebbf4438"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "bounded"
    - "traversal"
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
# Bounded graph traversal and relational alternatives

**Owning question:** What direction, cycle and result limits make the traversal question precise?

This page belongs to [V06/C06 — Graph relationships and traversal](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:3 -->
## 3. Graph traversal and relational joins can express similar answers

| Requirement | Relational option | Graph-model option |
|---|---|---|
| One-hop fixed relationship | Indexed join on foreign keys/link table | Match one typed edge |
| Small known-depth chain | Several joins or recursive CTE | Bounded path pattern |
| Arbitrary-depth reachability | Recursive CTE with cycle detection and limits | Variable-length traversal with path/cycle constraints |
| Frequent evolving relationship types | Schema/model discipline and relation tables | Explicit typed edges/property graph |
| Complex OLTP transaction | Relational integrity and transactions may be strong fit | Graph engine needs its own ACID/consistency verification |
| Search by terms/meaning | Full-text/vector index may be simpler | Traversal only helps when reliable relations change result |

Traversal can generate many possible paths in dense/cyclic graphs. Limit max depth, result cardinality, type/direction, visited-state and request resources. A high-degree hub can make a path search expensive even if the graph holds few total nodes. The [Neo4j variable-length pattern guide](https://neo4j.com/docs/cypher-manual/current/patterns/variable-length-paths/) explicitly discusses path explosion, path quantifiers and pruning predicates.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:4 -->
## 4. Query specification must include semantics and bounds

A graph question needs more than a starting node:
1. Edge types and direction allowed.
2. Maximum number of hops and maximum returned results.
3. Whether paths may repeat nodes/relationships.
4. Snapshot/time validity.
5. Required filters on nodes/edges, including permission checks.
6. Whether output expects *all paths*, *any path*, *shortest path*, or just reachable node IDs.
7. What to do when traversal exceeds budget or a node/edge has missing provenance.

A graph's linked structure can expose sensitive information through edge labels or relationship counts even if hidden node contents are not returned. Enforce authorized scope at query execution and result construction, not solely at UI display.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](edge-semantics.md) |
| Next | [Continue the reasoning](graph-provenance.md) |
| Integrated question | [Original scenario and limits](graph-data-models-and-traversal.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
