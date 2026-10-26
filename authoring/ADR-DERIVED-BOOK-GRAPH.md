# ADR addendum — Derived structural graph v0

> **Status: owner-authorized bounded v0 spike, 2026-10-26.** Issue #538.
> The owner authorized implementation; this is not independent review or
> acceptance of the v0 results. This addendum does not reverse the
> [retirement decision](ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md) and does not
> restore graph operations in the retrieval contract.

## Context

Tycho commits canonical document metadata, a deterministic route index, section
FTS and pattern registries. Those artifacts answer lookup and reading questions.
They do not expose reverse links, edge provenance, bounded traversal or a
structural audit of relationships that are already written down.

The current snapshot has 423 documents, 422 parent links, 1,746 directed
`related_ids`, 318 `prerequisites` and about 2,500 unique internal body links.
The pattern registry has 145 entries and 69 technical-owner pages, with zero
typed `relations`.

Two observations motivate the spike but are not errors by themselves:

- 59 chapter transitions use the previous chapter as a prerequisite; the longest
  chain is 34 hops. The field mixes reading order with conceptual dependency.
- 605 of 1,153 non-hierarchical `related_ids` edges have no reverse edge.
  Direction may be intentional, but the asymmetry is invisible without an audit.

## Relationship to the 2026-10-19 decision

The [retirement ADR](ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md) rejected a
**curated** concept/decision graph because its benefit and maintenance cost were
unproven. It also removed graph operations from the retrieval contract. That
decision remains in force for curated edges, graph shards, graph-aware MCP tools
and graph-dependent ranking.

This addendum proposes a narrower artifact: a deterministic index of links that
already exist in canonical frontmatter and prose. It adds no conceptual edge and
claims no retrieval benefit. The offline audit commands are not part of the
retrieval contract, MCP surface or search ranker.

For the bounded spike, this addendum authorizes only that offline structural
tool. It does not reopen #44-#46, restore graph neighbors in search or permit a
graph database. The absolute wording in [the retrieval
contract](models/retrieval-contracts.md) is narrowed only for these offline audit
commands; the retrieval contract itself remains graph-free.

## Decision for the bounded spike

The owner authorized a bounded v0 spike to build a deterministic, read-only
**derived structural graph**:

- Input: canonical frontmatter, canonical Markdown body links and the pattern
  registry.
- Output: a disposable JSON graph with typed edges and exact provenance.
- Authority: canonical Markdown and metadata remain authoritative; the graph
  cannot override them or create an edge that is not written down.
- Scope: `backlinks`, bounded `path` and `audit` only, as offline commands.
- Integration: no search, MCP or web UI in v0.

The graph is an index, like the route index and section FTS. It is not a new
knowledge base.

## Node and edge model

Nodes are minimal: `document` (canonical ID, kind, path, title), `pattern`
(registry ID and catalog name), `source` (source-register ID and title) and
`topic` (taxonomy ID). No summaries, claims or inferred concepts are copied.

Edges in v0:

- `parent` from `parent_id`: edition hierarchy only.
- `related` from `route_hints.related_ids`: discovery, not proof or dependency.
- `prerequisite` from `route_hints.prerequisites`: as authored; the audit
  reports reading-order shape, but the query must not call it a dependency.
- `body-link` from a Markdown link resolving to another canonical book page:
  navigation only, with line and optional anchor.
- `cites` from `evidence_scope.source_ids`: declared source reference, not
  evidence that the source supports the page.
- `owns-pattern` from the registry `technical_owner`: pattern to page and
  anchor.
- `has-topic` from `topic_ids`: taxonomy membership.

Every edge records `kind`, `from`, `to`, `origin`, `path`, a `field` or
`line` locator and the source snapshot hash. No edge may be inferred from
co-occurrence, similarity, an LLM or an undocumented heuristic.

## Queries and audit

`backlinks <id>` returns incoming edges grouped by kind and provenance. It does
not expand transitively by default.

`path <from> <to>` returns the shortest structural path within an explicit hop
limit and reports every edge kind used. It is a navigation path, not a
dependency proof.

`audit` reports, without auto-fixing:

- dangling endpoints and duplicate edges;
- asymmetric peer `related` edges;
- body links absent from `related_ids`, and the reverse;
- parent, prerequisite and reading-order shape;
- pattern-owner concentration and unresolved ownership;
- pages with no incoming or outgoing structural links.

## Non-goals

- No curated graph, graph shards, Neo4j or graph database.
- No LLM extraction and no Graphify dependency in v0.
- No typed pattern relations derived from prose.
- No source-to-claim change-impact implementation; that remains issue #91.
- No automatic symmetrization or repair of metadata.
- No MCP tool, search ranker or visual UI.

## Graphify boundary

Graphify is not selected as the builder. Its documentation path uses a semantic
model and `INFERRED` edges, while Tycho needs explicit, provenance-bound edges.
A later, separately pinned spike may render or query the v0 graph with
Graphify's viewer, without its documentation pass and without treating its
output as canonical. That spike is outside this decision.

## Validation and stop conditions

The spike is complete only when the builder is deterministic, `--check` fails
on stale output, every endpoint resolves, no edge lacks provenance and focused
tests pass. The audit result must distinguish observed facts from proposed
repairs.

Stop or narrow the spike if:

- the body-link parser cannot resolve canonical targets reliably;
- `prerequisite` cannot be presented without implying conceptual dependency;
- the graph cannot be rebuilt from canonical inputs without drift;
- the audit produces no actionable finding beyond existing validators.

The v0 does not establish retrieval or agent benefit. Any MCP/search integration
requires a separate decision and an evaluation against existing qrels.

## Evidence and limits

Counts in this addendum are observed from the route snapshot at commit
`19d37017`, not an independent audit. No builder, query result, Graphify run,
benchmark or independent review exists yet. This is a proposed scope, not
delivery. Implementation is tracked in issue #538 and recorded in
[DERIVED-BOOK-GRAPH-V0.md](DERIVED-BOOK-GRAPH-V0.md).
