# Directed architecture knowledge graph — vocabulary, provenance and ownership v1

> **ARCHIVED PROPOSAL — NOT PART OF TYCHO DELIVERY.** Superseded on 2026-10-19 by [ADR: Retire Tycho's curated knowledge graph](../ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md). The graph structures, shards, graph-query tasks and graph-related acceptance gates below are **historical**, not requirements or implemented capabilities. Graph-oriented topics remain valid as educational book material.

> E06-01 [issue #42](https://github.com/rouslanbaranov/tycho/issues/42), M4, 2026-10-19. This is a **contract**, not a populated static graph, graph extraction benchmark, inferred knowledge source, validated graph assembly or deployed query API. Tycho remains self-contained and uses independently public inputs.

## Why two relationship planes must stay separate

1. **Extracted code facts**: an extraction tool at an exact locked public Git revision may report `declares`, `imports`, `calls`, `reads`, `writes`. These edges are scoped by language/parser/tool version and file/line/symbol boundaries and are **not** automatically architectural dependencies. `calls` is directed caller→callee only if supported by the extractor's verified direction.
2. **Curated reasoning relationships**: original Tycho analysis connects a user `requirement`, `constraint`, `pattern`, `concept`, `mechanism`, `decision` or `evidence`. `candidate_for`, `contraindicated_by`, `depends_on`, `supports`, `qualifies`, `contradicts` require named applicability, rationale and exact evidence. A source or neighboring chapter mentioning two names does **not** create such an edge.
3. **Book navigation**: `contains`, `next_read` and `canonical_owner` link stable document identities to reading routes and source claims. These links cannot claim runtime causation, transitivity or unmeasured implementation.

These planes are distinct graph namespaces, not interchangeable projections. Graph semantics never override the canonical prose, [metadata ID contract](document-metadata-identity.md), [claim provenance](../../sources/CLAIM-PROVENANCE.md), [source register](../../sources/register.json), or exact-commit [repository lock](../../sources/public-repositories.lock.json).

## Directed multigraph model

A graph is `G=(V,E)`, with stable node IDs and **multiple distinct directed edge records** permitted between identical endpoints where relation, condition, witness or revision differs. Every edge has its own unique `id`; a tuple of endpoints alone is not an edge identifier. Reversal of `from` and `to` is a different statement; inverse expansion is allowed only if explicitly defined for a relation. No `depends_on` transitive closure, call-graph inference, pattern recommendation or cross-source equivalence without an explicit separately evidenced rule.

| Node `kind` | Prefix and authoritative meaning |
|---|---|
| `document` | `doc:` + existing stable Tycho metadata ID, canonical Markdown page |
| `claim` | `claim:` + existing `claim.*` record ID (not a cloned proof object) |
| `source` | `src:` + existing `src.*` source-register ID |
| `concept` | `concept:` + curated stable slug; general engineering construct |
| `pattern` | `pattern:` + curated stable slug, applicability not universal |
| `requirement` | `req:` + original requirement ID with declared synthetic/real scope |
| `constraint` | `constraint:` + original invariant/hard gate with scope |
| `decision` | `adr:` + stable ADR ID and version |
| `implementation` | `impl:` + source ID and Git revision and relative path/symbol, within a locked public source |
| `symbol` | `symbol:` + source ID + revision + language-qualified path/symbol, derived from inspected code |

Prefix spelling is **owned by this contract**, but external claim/source/doc IDs continue to be owned by their canonical registers. For implementation references, a revision must equal the versioned Git lock; a source's `main`/branch name never qualifies as an immutable code fact.

| Plane | Edge `kind` | Direction | Evidence and constraints |
|---|---|---|---|
| navigation | `contains` | parent document → child document | Canonical metadata parent identity; no multiple authoritative parents |
| navigation | `next_read` | current doc → candidate doc | Editorial nonbinding route; not dependency or proof |
| navigation | `canonical_owner` | concept/pattern → owning doc | One authoritative explanation; versioned ownership |
| curated | `supports`, `qualifies`, `contradicts` | source/claim → bounded claim/decision | Exact source/claim ledger and authored rationale; contradiction may target an inference, not a different source |
| curated | `candidate_for` | pattern → requirement | Conditional, requires workload/operational envelope, alternatives and falsifiable test |
| curated | `contraindicated_by` | pattern → constraint | Hard disqualifier with evidence, else hypothesis/unknown |
| curated | `depends_on` | concept/decision → named prerequisite | Does not imply transitive proof or universal deployment order |
| curated | `implemented_by` | concept/pattern → implementation | Requires actual code inspection at pinned version; not a general endorsement |
| code | `declares`, `imports`, `calls`, `reads`, `writes` | extracted file/symbol actor → target | Tool name/version, exact source revision, path and extraction limitations; never inferred curated recommendation |

An edge is **evidence-backed** only when its `evidence_claim_ids` resolve to existing checked claim records and its `conditions`, `limitations`, `rationale` are explicit. Source IDs alone or an accessible URL do not establish technical support. For extracted code, `extractor`, locked revision and observed scope are required; a graph parser may provide syntactic observations but not automatically prove runtime behavior. Proposed/hypothetical edges carry `status=proposed`; only a separate documented review may promote `status=reviewed`. A generated timestamp is never a review event.

## Shards, ownership and manifests

- **One canonical owner per ID prefix**: `graph/curated/` owns conceptual/decision/requirement/constraint nodes and curated edges; `graph/code/<source-id>/<full-revision>/` owns extracted implementation/symbol nodes and code edges; `graph/navigation/` is **derived** from canonical metadata/index and should not be manually edited. External source/claim document nodes are **references** to registers, not competing source-of-truth copies.
- Every shard has `graph_schema_version=1`, `shard_id`, `owner_prefixes`, `origin`, `snapshot`, sorted `nodes`/`edges` and `evidence_scope`. `origin` is `curated`, `extracted` or `derived`. The extracted shard additionally fixes source ID, full revision and extractor version. Shard paths and ownership are recorded in `graph/manifest.v1.json`; path traversal, duplicate ownership and opaque unversioned graphs are forbidden.
- Cross-shard relationships may point to **existing stable external node IDs**, but every endpoint must resolve at assembly time. Curated edges do not rewrite extracted shards; extracted graph data cannot assert a curated applicability edge.
- The assembly is **derived, deterministic and replaceable**, not another committed authoritative graph: sort shards by ID, nodes by ID and edges by (kind, from, to, id); validate uniqueness and exact endpoint resolution, output content hash, source revision manifest and per-plane coverage. A build must fail on ambiguous shard ownership, stale pinned Git revision, type/direction violation, missing supporting claim, or contradictory graph schema version.
- Prefix governance requires a deliberate migration map for renaming IDs/shards, an exact reference diff and backwards-compatible aliases where necessary. New semantics use an explicit schema version; don't silently reinterpret existing edges.

## Worked original **hypothetical** edge (not verified)

~~~json
{
  "id": "edge:curated:admission:1",
  "kind": "candidate_for",
  "from": "pattern:bounded-admission",
  "to": "req:synthetic-burst-deadline",
  "plane": "curated",
  "status": "proposed",
  "conditions": ["Offered load measured separately from admitted throughput", "Business SLA permits explicit rejection"],
  "limitations": ["No load test on a deployed system"],
  "rationale": "A bounded early-admission mechanism may protect an expensive downstream capacity limit; measure end-to-end user outcomes first.",
  "evidence_claim_ids": []
}
~~~

**Validation consequence:** in a strict reviewed graph this record cannot be called `reviewed` with an empty evidence list; the synthetic requirement needs a declared owner; the example is an illustrative incomplete draft, *not* an assembled shard. A future implementation should reject it as a publishable evidence-backed decision until claims/conditions/review resolve.

## Completion and future issue boundaries

- #43 proves version-pinned static code extraction on permitted public source snapshots and records tool/parser scope. This contract alone does not claim Graphify output.
- #44 curates actual pilot reasoning nodes/edges with inspectable evidence and independent review state.
- #45 supplies strict graph schema, shard/manifest/endpoint/integrity validation and deterministic assembly; sample format is specified by this contract but not yet fully enforced by code.
- #46 provides bounded direction-aware queries with explicit limits, snapshot identity, continuation and no invented transitive semantics.

**Review state:** original proposed ontology and sample, no independent technical review, code extraction, graph serialization or live graph queries executed.