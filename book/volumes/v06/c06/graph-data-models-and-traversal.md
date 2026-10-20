---
metadata_version: 1
id: "tycho.page.d34afc7f27b54431b779f7f75f11e2c3"
kind: "page"
parent_id: "tycho.chapter.1f0c8323023f4adfaa1affc7bf2993d4"
canonical_path: "book/volumes/v06/c06/graph-data-models-and-traversal.md"
title: "Graph data models and traversal: when relationships are the query"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Graph relationships and traversal. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "When is explicit typed connectivity preferable to lexical or vector similarity?"
  prerequisites: []
  related_ids:
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.4348c76938fc4d41b239721b94338436"
    - "tycho.page.c75a11f9786442a5b5456f11c2412df4"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.ae4febbe43f941f78d825613e126419b"
    - "tycho.page.6d8377d616c548ef9c3b213d8a2df934"
    - "tycho.page.64f398c0535345258b1fdf5eebbf4438"
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
<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:-1 -->

# Graph data models and traversal: when relationships are the query

> **Tycho educational System Design manuscript V06/C06 (2026-10-19).** Graph models are a general architectural topic; **a manually curated knowledge graph for Tycho itself is explicitly excluded** from the product/infrastructure roadmap. This page is original explanatory prose and synthetic scenarios with public Neo4j Cypher references. No graph database was installed, queried or benchmarked.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:0 -->
## Purpose and mission

Some questions start from an entity and follow relationships: “Which components depend on this library?”, “What sequence of connections leads from station A to station B?” or “Which permissions allow this user to reach that resource?” A graph model represents **vertices, edges and their identities/attributes**, and graph traversal is useful when relationship paths are central to the workload.

The decision is not simply “use a graph database”. Many bounded relationship queries can be answered by relational joins, adjacency lists or document links. A graph engine becomes plausible only when traversal shape, depth, mutation frequency, transactional requirements and operating cost justify the additional model.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:8 -->
## Engineering walkthrough — A bounded dependency path is not proof of causation

**Original fictional equipment graph:** nodes are physical `Unit`, `Module` and `Supplier`; edges `DEPENDS_ON` have direction, effective date and source identity. Query: "Which currently operational units depend on a part supplied by vendor X within at most three transitions?" A graph path of unlimited depth risks cycles, irrelevant historical dependencies and unbounded query cost.

Graph design must define whether dependencies are direct or inferred, what "current" means, and which edge source/version supports it. A Cypher-style bounded expansion such as `(unit)-[:DEPENDS_ON*1..3]->(part)` is meaningful only under a declared schema and direction policy; it is *not* a test of a deployed query or an authorization contract. A relational schema with `dependency(source_id,target_id,valid_from,valid_to)` plus a recursive CTE can answer a similar bounded reachability question; the appropriate storage choice depends on actual traversal frequency and update costs, not the visual elegance of graph arrows.

| Contradiction | Required handling |
|---|---|
| A→B and B→A cycle | Enforce visited/depth budget; repeated traversal is not extra evidence |
| Historical edge expired | Time-filter before interpreting path as current |
| Supplier changed identity | Reconcile stable owner and evidence revision |
| Tenant A path crosses forbidden tenant B | Authorization must apply to intermediate vertices/edges, not just final result |

**Proposed, not run:** compare bounded Cypher and recursive relational queries on the same versioned synthetic topology with skew/cycles, measuring completeness, latency, updates and access control. A graph could be unnecessary for shallow stable joins, and useful for variable-depth relationship-rich questions. **This chapter teaches graph data architecture only; it does not introduce a manually curated Tycho knowledge graph or platform implementation.**

### Paired graph and relational traversal with the same answer (unexecuted synthetic fixture)

**Question:** which *Tenant t1* physical units depend, within **one to three current directed `DEPENDS_ON` edges**, on `Part C`? Fix evaluation date `2026-10-20`. Fixture nodes are `U1` (Unit, t1), `U2` (Unit, t1), `U3` (Unit, t2), `A` (Part, t1), `B` (Part, t1), `C` (Part, t1); all node IDs are globally unique here. Active edges: `U1→A`, `A→C`, `U2→B`, `B→C`, plus an *unauthorized cross-tenant* `U3→C`; each edge carries `tenant`, `valid_from`, `valid_until`. A separate `C→A` cycle is included to test path safety. Expected authorized distinct unit IDs: **`U1, U2`**, never U3. Tenant authorization is an explicit *assumed query scope*, not proven by these queries.

**Illustrative Neo4j Cypher variable-length relationship syntax** (Neo4j Cypher 5/25 manuals; label and property schema defined above):

```cypher
MATCH p = (u:Unit {tenant: 't1'})-[:DEPENDS_ON*1..3]->
          (target:Part {id: 'C', tenant: 't1'})
WHERE ALL(n IN nodes(p) WHERE n.tenant = 't1')
  AND ALL(r IN relationships(p)
          WHERE r.tenant = 't1'
            AND r.valid_from <= date('2026-10-20')
            AND (r.valid_until IS NULL OR r.valid_until > date('2026-10-20')))
RETURN DISTINCT u.id AS unit_id ORDER BY unit_id;
```

The `*1..3` syntax is the older still-supported variable-length form; the [Neo4j reference](https://neo4j.com/docs/cypher-manual/current/patterns/reference/variable-length-paths/) distinguishes it from modern quantified relationship syntax. The bounded path and per-node/per-edge checks are important: matching only the end node's tenant is **not** sufficient to prevent forbidden intermediate disclosure.

**Equivalent illustrative PostgreSQL 17 recursive CTE** assumes `nodes(id text PRIMARY KEY, kind text, tenant text)` and `edges(src text, dst text, tenant text, valid_from date, valid_until date)`, populated with the same fixture:

```sql
WITH RECURSIVE walk(tenant, origin, node_id, depth, visited) AS (
    SELECT n.tenant, n.id, n.id, 0, ARRAY[n.id]::text[]
      FROM nodes n WHERE n.kind = 'Unit' AND n.tenant = 't1'
    UNION ALL
    SELECT w.tenant, w.origin, e.dst, w.depth + 1, w.visited || e.dst
      FROM walk w
      JOIN edges e ON e.src = w.node_id AND e.tenant = w.tenant
      JOIN nodes n ON n.id = e.dst AND n.tenant = w.tenant
     WHERE w.depth < 3
       AND e.valid_from <= DATE '2026-10-20'
       AND (e.valid_until IS NULL OR e.valid_until > DATE '2026-10-20')
       AND NOT (e.dst = ANY(w.visited))
)
SELECT DISTINCT origin AS unit_id FROM walk
 WHERE node_id = 'C' AND depth BETWEEN 1 AND 3
 ORDER BY unit_id;
```

The [PostgreSQL 17 recursive CTE and cycle-detection documentation, §7.8.2](https://www.postgresql.org/docs/17/queries-with.html) explains recursive evaluation and cycle handling; here `visited` stops revisiting nodes. The Cypher path-match engine and recursive SQL have different physical execution strategies and may have different path-multiplicity semantics, but **the distinct authorized endpoint set** should match for this fixture. The toy queries are **not executed**, not a claim about performance and not a substitute for access control enforced in storage/query authorization. Real tenancy demands graph-wide object/edge permission enforcement, not just a caller-supplied `tenant` literal. No Tycho infrastructure knowledge graph is created or implied.

### Query-language version and cycle semantics (editorial compatibility note)

The preceding `-[:DEPENDS_ON*1..3]->` is the **legacy variable-length relationship** form. The [Neo4j Cypher 25 variable-length-path manual](https://neo4j.com/docs/cypher-manual/25/patterns/variable-length-paths/) says this syntax remains available but is **not GQL conformant**; modern quantified relationships such as `-[:DEPENDS_ON]->{1,3}` express a corresponding depth bound. The [Cypher language-version selection reference](https://neo4j.com/docs/cypher-manual/current/queries/select-version/) explains how to pin `CYPHER 5` or `CYPHER 25`, and the current compatibility manual records that new Neo4j databases have generally defaulted to Cypher 25 since **2026.02**. This edition is not an assertion that both query spellings were executed.

**Further distinction:** the illustrative SQL CTE excludes **revisiting any node** through `visited`, while Cypher's default path uniqueness is relationship-based unless additional node/path restrictions are imposed. Both may return the same `DISTINCT unit_id` for the specified six-node toy fixture, but that is **not general bag-of-path equivalence** when cycles, repeated vertices, multiple evidence edges or path counts matter. Before implementing, define node-simple/relationship-simple path semantics, exact authorization on intermediate nodes and edges, deployed language version, and test both queries for the *same agreed result relation*. Neither syntax is an access-control enforcement mechanism by itself.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d34afc7f27b54431b779f7f75f11e2c3:9 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Meta — TAO graph serving](../../../cases/meta-tao-social-graph-serving.md)**. **Relevant mechanism or architectural contrast:** Graph-shaped access over authoritative relational data and tiered caches is a targeted domain serving architecture. **Not established by this report/playbook:** TAO does not imply every domain needs a graph database, eventual consistency policy or manually curated Tycho graph.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Use explicit edge semantics, direction and bounded traversal when the question depends on relationships.

A path through a graph does not imply causal influence or permission; cycles and fan-out require explicit traversal limits.

The detailed pages separate the mechanisms that make this decision conditional:

- [Edge meaning and relationship questions](edge-semantics.md) — Which explicit relation is being traversed and what can a path not prove?
- [Bounded graph traversal and relational alternatives](bounded-traversal.md) — What direction, cycle and result limits make the traversal question precise?
- [Derived relationships and falsification](graph-provenance.md) — Which source and update contract makes a derived edge usable?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
