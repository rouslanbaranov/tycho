---
metadata_version: 1
id: "tycho.page.d34afc7f27b54431b779f7f75f11e2c3"
kind: "page"
parent_id: "tycho.landing.4348c76938fc4d41b239721b94338436"
canonical_path: "book/search/graph-data-models-and-traversal.md"
title: "Graph data models and traversal: when relationships are the query"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Reader entry for Graph data models and traversal: when relationships are the query. Scope includes 1. Clarify the meaning of an edge; 2. Original fictional example: a workshop equipment dependency map; 3. Graph traversal and relational joins can express similar answers."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Graph data models and traversal: when relationships are the query?"
  prerequisites: []
  related_ids:
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.4348c76938fc4d41b239721b94338436"
    - "tycho.page.c75a11f9786442a5b5456f11c2412df4"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Graph"
    - "data"
    - "models"
    - "and"
    - "traversal"
    - "when"
    - "relationships"
    - "are"
    - "the"
    - "query"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Graph data models and traversal: when relationships are the query

> **Tycho educational System Design manuscript V06/C06 (2026-10-19).** Graph models are a general architectural topic; **a manually curated knowledge graph for Tycho itself is explicitly excluded** from the product/infrastructure roadmap. This page is original explanatory prose and synthetic scenarios with public Neo4j Cypher references. No graph database was installed, queried or benchmarked.

## Purpose and mission

Some questions start from an entity and follow relationships: “Which components depend on this library?”, “What sequence of connections leads from station A to station B?” or “Which permissions allow this user to reach that resource?” A graph model represents **vertices, edges and their identities/attributes**, and graph traversal is useful when relationship paths are central to the workload.

The decision is not simply “use a graph database”. Many bounded relationship queries can be answered by relational joins, adjacency lists or document links. A graph engine becomes plausible only when traversal shape, depth, mutation frequency, transactional requirements and operating cost justify the additional model.

## 1. Clarify the meaning of an edge

A useful graph schema identifies:
- node identity and node type;
- relationship type, direction, endpoints and cardinality;
- whether multiple parallel relationships are allowed;
- temporal validity/version of the relation;
- authorization and visibility of nodes **and edges**;
- whether the relationship is authoritative or derived;
- deletion, cycle, duplicate and integrity policies.

The [Neo4j Cypher pattern manual](https://neo4j.com/docs/cypher-manual/current/patterns/) explains declarative patterns over nodes and relationships, including traversals and paths. A path is a specific sequence of matched graph elements, not a guarantee that all reachable nodes or every shortest path were enumerated within a query budget.

## 2. Original fictional example: a workshop equipment dependency map

A community event uses portable devices with replaceable parts. A battery pack is compatible with a charger, a projector uses a specific cable, and a setup checklist requires a functioning power supply. The question is whether an unavailable charger affects a set of planned equipment kits.

```mermaid
flowchart LR
    C["Charger model"] -->|SUPPLIES| B["Battery pack"]
    B -->|POWERS| P["Portable projector"]
    P -->|USED_IN| K["Workshop equipment kit"]
    K -->|BOOKED_FOR| E["Event"]
```

**Text alternative:** the fictional charger supplies a battery, which powers a projector used in a kit booked for an event. Querying the paths could show affected event kits. The arrows express modeled relationships, not measured physical behavior, actual inventory or authoritative compatibility certifications.

A direct question “Which chargers supply battery B?” is one hop. “Which events might depend transitively on charger C?” follows a variable-length typed path. But a path is a potential dependency chain, **not automatically a proof that the event cannot proceed**: spare batteries, alternate chargers and temporal availability matter.

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

## 5. Derived graphs and provenance

A dependency edge extracted from a software build has different authority from a human-reviewed architectural statement. A graph constructed from source references should record:
- source file/version or admitted document;
- inference/extraction method and date;
- confidence or evidence status;
- edge freshness and deprecation/removal rule;
- ownership of conflict resolution.

An edge is not fact merely because a visualization draws it. Source revision drift can invalidate it. For a system design reference book, **there is no requirement to materialize a graph service**: ordinary cross-references and precise source/claim links may be enough to explain the architecture.

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

## 7. Public evidence and explicit product-scope boundary

| Independently inspected public source | Supports | Not established |
|---|---|---|
| [Neo4j Cypher — Patterns](https://neo4j.com/docs/cypher-manual/current/patterns/) | Property-graph query patterns and path semantics | Implementation for fictional equipment model |
| [Neo4j Cypher — Variable-length paths](https://neo4j.com/docs/cypher-manual/current/patterns/variable-length-paths/) | Bounded variable-length traversal and explosion/pruning concerns | Performance of any real graph DB under a target workload |
| [Tycho hybrid retrieval](hybrid-ranking-graph-and-evaluation.md) | Prior theoretical distinctions of retrieval mechanisms | Actual hybrid search or graph infrastructure |

All graph nodes, edges, diagrams, inferred rules and experiments are original invented educational examples. No graph was created, indexed, traversed or independently reviewed. **This chapter does not reintroduce a curated Tycho knowledge graph.** It covers graph *architectures as a subject of System Design*, not a product feature.

**Navigation:** proposed **V06/C06** in [planned book contents](../PROPOSED-STRUCTURE.md), current [search/data information architecture](README.md). Related [Hybrid lexical/vector ranking](hybrid-ranking-graph-and-evaluation.md), [Storage alternatives](../data/storage-model-alternatives-and-workload-fit.md), [Authorization boundaries](../security/identity-authorization-and-isolation.md).

## Applied M9 evidence: what transfers and what does not

The following historical cases are **time-scoped publisher/practitioner reports**, not a Tycho benchmark or proof of a universal architecture choice. Any associated decision playbook is an **original synthetic comparison**, not a decision made by the companies cited. These cases inform the specific mechanism and contraindications above:

- **[Meta — TAO graph serving](../cases/meta-tao-social-graph-serving.md)** illustrates graph-shaped access over authoritative relational data and tiered caches is a targeted domain serving architecture. **It cannot establish:** tAO does not imply every domain needs a graph database, eventual consistency policy or manually curated Tycho graph.

A different system must recheck its workload, source date, version, authority boundary and failure/recovery acceptance criteria before transferring any decision. See the case's own evidence ledger for exact public references and unresolved claims.
