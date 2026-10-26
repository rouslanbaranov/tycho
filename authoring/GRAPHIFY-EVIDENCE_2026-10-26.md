# Graphify necessity evidence — 2026-10-26

> **Status: bounded evaluation, no adoption.** Issue #544. Graphify
> `0.9.96` was pinned, installed and exercised for code-only and deterministic
> Markdown paths. The semantic documentation path was blocked: no model backend
> or API key is configured. No Tycho dependency, generated artifact or MCP tool
> is added by this evaluation. No independent review is claimed.

## Question and test

Is Graphify necessary for any Tycho domain? A domain passes only when a
representative Tycho task is materially worse without Graphify after comparing
quality, provenance, cost and existing capabilities. A feature list, a vendor
benchmark or a graph that merely looks useful does not pass.

The verdict uses three labels:

- **necessary** — an existing task cannot be met acceptably without Graphify;
- **optional** — useful for exploration, but existing capabilities meet the task;
- **not necessary** — existing capabilities match or exceed Graphify for the task.

## Verdict

No examined Tycho domain makes Graphify necessary. The code graph is an optional
exploration/visualization aid, not an authoritative impact tool. The semantic
documentation path is blocked without a model backend and is misaligned with
canonical IDs and explicit provenance. No dependency is added.

## Pinned environment

| Item | Value |
|---|---|
| Graphify package | `graphifyy==0.9.96` from PyPI |
| CLI | `graphify 0.9.96` |
| Python | 3.15.0 |
| Declared runtime dependencies | 107 |
| Isolated environment size | 154 MB |
| Wheel size | 1.8 MB |
| Tycho snapshot | `0f3ece31` |
| Book corpus | 423 Markdown pages, about 463k words, 4.5 MB |

Public source: [Graphify](https://github.com/Graphify-Labs/graphify).

No model API key, Ollama endpoint, Claude CLI or other semantic backend was
available. The semantic documentation path could therefore not be run. The
blocked command is recorded below.

## Baselines

- Route index: 423 canonical documents with stable IDs and typed frontmatter.
- FTS5 section search and the existing MCP search/read/verify surface.
- Derived graph v0: 718 nodes and 6,711 explicit edges, including typed
  `parent`, `related`, `prerequisite`, `body-link`, `cites`,
  `owns-pattern` and `has-topic` edges with provenance.
- Existing code tools: text search, Python imports, tests and a small number of
  explicit import helpers. Tycho has no pre-existing code graph.

## Result 1 — code graph

Command:

~~~sh
graphify extract /Users/rbaranov/Projects/tycho --code-only \
  --out /tmp/graphify-tycho-code
~~~

Observed:

- 305 code files scanned; 37 unsupported files skipped;
- 1,813 nodes, 4,434 edges and 98 communities;
- 1.7 MB `graph.json`;
- 2.59 s wall-clock build after installation;
- 4,298 `EXTRACTED` and 136 `INFERRED` edges.

The edge mix was 1,807 `calls`, 762 `method`, 712 `imports`, 661
`contains`, 282 `imports_from`, 171 `rationale_for` and smaller counts.

The most-connected nodes were test classes rather than architectural modules:
`McpServerTests` (48 edges), `TychoMcpServer` (41) and `E18SurfaceTests`
(35). That is a property of the corpus, but it makes the default "god nodes"
view weak as an architecture summary.

### Impact-analysis check

For the function `canonical_scan`, a text search found 14 files in
`scripts/` and `tests/`. Graphify `affected` at depth 3 covered 9 of those
14 files. It missed:

- `tests/test_tycho_route_index.py`
- `tests/test_tycho_section_fts_index.py`
- `tests/test_tycho_section_search.py`
- `tests/test_tycho_mcp_http.py`
- `tests/test_tycho_mcp_server.py`

The missing calls were qualified or aliased forms such as
`route.canonical_scan(...)` and patched module attributes. The graph did add
indirect callers that a naive text search does not classify, so it was not
purely worse; its **direct-call recall was incomplete**. It cannot be the sole
impact-analysis tool for this repository.

`graphify explain canonical_scan` gave useful callers and imports with source
lines. `graphify query "canonical_scan"` returned 168 nodes and showed 46 at a
1,200-token budget; that is exploratory output, not a precise reference list.
The existing text search was complete for the direct references and cheaper to
interpret.

**Code-domain verdict: optional.** A code visualizer and exploratory graph are
plausible maintenance aids, but no task requires Graphify. The measured recall
gap prevents claiming it as the authoritative impact tool.

## Result 2 — deterministic Markdown structure

The full documentation path requires an LLM. To isolate the structural part, the
public deterministic Markdown extractor was invoked directly over all 423 book
pages with the repository as scan root. This is not the supported full pipeline,
and it is labelled accordingly.

Observed:

- 3,678 nodes: 423 page nodes and 3,255 heading nodes;
- 5,850 edges: 3,255 `contains` and 2,595 `references`;
- all 423 page nodes carried parsed frontmatter, including 423 unique
  `tycho.*` IDs;
- none of those IDs became node identities;
- no edges were generated from `parent_id`, `related_ids`,
  `prerequisites` or `source_ids`;
- all 3,678 emitted source paths were absolute in this direct invocation.

The structural extractor is good at headings and ordinary Markdown links. It
does not use Tycho's typed metadata relationships as graph edges. It would need
an adapter to canonical IDs, stable paths and typed edges to approach graph v0.
At that point the adapter, not Graphify, owns the Tycho semantics.

**Book-structure verdict: not necessary.** Graph v0 already produces fewer nodes
(718), more typed relationships (6,711) and portable canonical IDs. Graphify
adds heading granularity, which is not the current gap.

## Result 3 — semantic documentation path

Command attempted on one page:

~~~sh
graphify extract /tmp/graphify-docs-sample --out /tmp/graphify-docs-out \
  --backend openai --max-workers 1
~~~

Result:

~~~text
error: backend 'openai' requires OPENAI_API_KEY to be set.
~~~

The full path also requires a configured model and can emit `INFERRED` and
`AMBIGUOUS` semantic edges. The semantic prompt describes relations such as
`conceptually_related_to` and `semantically_similar_to`; it is not designed to
reproduce Tycho's `related`, `prerequisite`, `cites` or `parent` semantics
from frontmatter.

Cost was not measured. The corpus is about 463k words; a semantic pass would
send content to an external model and add nondeterminism, external dependency
and a new provenance question. The documentation path is therefore **blocked,
not demonstrated**, and a positive necessity claim cannot be made from it.

**Semantic-documentation verdict: not demonstrated; not necessary on current
evidence.**

## Result 4 — viewer over graph v0

Graph v0 was converted to Graphify's node-link shape for an isolated viewer
test. No Graphify extraction was involved.

Observed:

- `explain` rendered 64 connections for a page with degree 80;
- `path` found a three-hop route but displayed combined labels such as
  `body-link/related` and omitted the edge's field or line locator;
- `query "outbox idempotency"` returned 198 nodes and showed 21 at a
  1,200-token budget;
- `export html` produced a 1.9 MB page;
- the HTML loaded `vis-network` from `unpkg.com`, so it was not fully
  self-contained or offline.

Graphify's HTML is a real interactive explorer. That is optional convenience,
not a Tycho task that the CLI, route index or MCP surface cannot perform. The
viewer also loses the per-edge provenance that graph v0 preserves.

**Viewer verdict: optional only.** No task-level improvement was measured.

## Domain verdicts

| Domain | Baseline | Graphify evidence | Verdict |
|---|---|---|---|
| Code comprehension | Search, imports, tests | Useful graph; misses qualified calls | Optional |
| Code impact | Search, imports | 9/14 direct reference files | Not necessary |
| Book structure | Graph v0, metadata | Heading graph; no typed metadata edges | Not necessary |
| Book semantics | Metadata, source ledger | LLM path blocked; inferred edges | Not demonstrated |
| Pattern atlas | Registry and cards | No registry relation mapping | Not necessary |
| Retrieval/MCP | FTS5, route index | BFS label query; no ranking benchmark | Not demonstrated |
| Source/provenance | Register, claims | No canonical source edges | Not suitable |
| Visualization | CLI, Mermaid, static pages | Interactive HTML, CDN dependency | Optional |

## What would change the verdict

A positive case needs all of these:

1. A named Tycho task whose current baseline is materially worse.
2. A pinned Graphify run on the same snapshot with an approved model backend.
3. Human-checked edge precision and recall, including qualified calls and
   contradictory cases.
4. A measured task improvement in correctness, citation precision, time or
   token cost, not just a nicer graph.
5. Stable canonical IDs and preserved provenance; no inferred edge becomes
   technical truth.
6. Acceptable install, network, privacy and maintenance costs.

Until then, "Graphify is available" is not evidence that Tycho needs it.

## Conclusion

**No examined Tycho domain makes Graphify necessary.** The strongest case is an
optional code-exploration and visualization aid. It has a measurable
impact-analysis recall gap, a 107-dependency/154 MB installation footprint, and
a viewer with an external CDN dependency. Its documentation path is blocked
without a model backend and is structurally misaligned with Tycho's canonical
IDs and explicit provenance.

Do not add Graphify as a project dependency, a canonical graph source or an MCP
dependency on this evidence. The existing graph v0, route index, FTS5 and MCP
surface remain the supported baseline.

## Limits

- No independent review, owner acceptance or benchmark adjudication.
- No semantic Graphify run; the backend was unavailable.
- The deterministic Markdown test used a public extractor directly, not the full
  LLM pipeline.
- The code-impact sample is one function, `canonical_scan`; it is reproducible
  but not a repository-wide precision study.
- Graphify's own public benchmarks were not reproduced and are not Tycho tasks.
- Temporary outputs and installations live outside the repository; no Graphify
  artifact is committed.
