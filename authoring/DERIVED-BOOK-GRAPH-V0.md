# Derived structural graph v0

> **Status: implemented and locally checked, 2026-10-26.** Issue #538. This is
> self-checked engineering evidence, not independent review, retrieval evaluation
> or product acceptance.

## Scope

The v0 graph is a deterministic, read-only index over links that already exist in
canonical frontmatter, book prose and the pattern registry. It is not a curated
concept graph, a graph database or a retrieval feature. Canonical Markdown and
metadata remain authoritative.

The decision and edge semantics are in
[the ADR addendum](ADR-DERIVED-BOOK-GRAPH.md). The implementation is
`scripts/book_graph.py` with two CLI entry points:

- `scripts/build_book_graph.py` builds or checks the artifact.
- `scripts/query_book_graph.py` runs offline queries.

## Commands

Building validates the complete corpus through
`route_index.canonical_scan`, so it needs the documented schema dependencies:

~~~sh
python3 -m pip install -r requirements-validation.txt -r scripts/requirements-routing.txt
python3 scripts/build_book_graph.py build
python3 scripts/build_book_graph.py check
~~~

Querying and auditing read only the graph artifact and need the standard library:

~~~sh
python3 scripts/query_book_graph.py backlinks --id tycho.page.ace968ab1de8409383c6a9b22a00d006
python3 scripts/query_book_graph.py path \
  --from tycho.page.ace968ab1de8409383c6a9b22a00d006 \
  --to tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0 \
  --max-hops 4
python3 scripts/query_book_graph.py audit
python3 scripts/query_book_graph.py --json audit
~~~

`path` follows directed edges by default. Use `--undirected` only when a
reverse route is explicitly wanted; the output marks reverse steps.

## Artifact

The generated file is `generated/book-graph.v1.json`. It is a build output and
is ignored by Git because the v0 copy is large; run `build` before querying and
use `check` as the freshness gate. The file carries:

- `schema` and `graph_version`;
- `source_snapshot_sha256` from the validated route scan;
- `counts`, `nodes`, `edges` and a `content_sha256` over nodes and edges;
- `body_link_issues` and `unresolved_pattern_owners`.

Nodes are `document`, `pattern`, `source` and `topic` records with stable IDs
and minimal labels. Edges are `parent`, `related`, `prerequisite`,
`body-link`, `cites`, `owns-pattern` and `has-topic`. Each edge records its
origin, canonical path, field or line locator, optional anchor and the hash of the
file that supplied it.

## Current audit

On the snapshot used for this v0:

| Measure | Value |
|---|---:|
| Documents | 423 |
| Pattern entries | 145 |
| Cited sources | 133 |
| Topic nodes | 17 |
| Graph nodes | 718 |
| Graph edges | 6,711 |
| `related` edges | 1,746 |
| Asymmetric non-hierarchical `related` edges | 605 |
| Body-link occurrences | 3,229 |
| Body-link pairs absent from `related` | 1,118 |
| `prerequisite` edges | 318 |
| Longest prerequisite chain | 34 |
| Sequential chapter transitions | 59 |
| Patterns without owner | 0 |
| Documents without navigation incoming | 1 |
| Documents without navigation outgoing | 7 |
| Unresolved canonical body links | 0 |

The counts are observations, not repair instructions. The 34-hop chain reflects
authored reading order, not a demonstrated conceptual dependency. Asymmetric
`related` edges and body-only routes are candidates for editorial review, not
automatic fixes. "Navigation" counts use `related`, `prerequisite`,
`body-link` and `owns-pattern`; parent links are hierarchy and are excluded.

## Limits

- The body-link parser is lexical, not a complete CommonMark implementation. It
  skips fenced and inline code, images, external URLs, anchors and local links
  outside `book/`; it does not resolve reference-style links or validate anchors.
- `prerequisite` is preserved as authored. The graph does not relabel it as a
  dependency or infer transitive prerequisites.
- The graph is a snapshot. A changed page requires a deliberate rebuild; `check`
  fails when the artifact differs.
- No MCP tool, search ranker, web UI, graph database or Graphify builder is part
  of v0. A pinned Graphify viewer experiment remains a separate decision.
- No independent review, retrieval benefit or source truth is claimed.
