# Deterministic section-level lexical indexing (E07-03)

> Issue [#49](https://github.com/rouslanbaranov/tycho/issues/49), M4. **Status 2026-10-22:**
> local implementation exercised on the current 423-page corpus; not merged, not
> independently reviewed, not a search or MCP service. Python 3.9.6 and SQLite 3.54.0
> were used locally; the repository validation requirements are unchanged.

## Scope and authority

[section_fts_index.py](../scripts/section_fts_index.py) builds a read-only SQLite FTS5
snapshot from canonical Markdown and its validated YAML frontmatter. It calls the existing
[route-index scanner](../scripts/route_index.py) for document IDs, kinds, topics, evidence
status, paths, source hashes and coverage. It does not create frontmatter, fetch sources,
enrich prose, run embeddings, build a graph or expose MCP.

The canonical book remains authoritative. The index is a disposable generated artifact at
`generated/sections-fts-v2.sqlite`; it is excluded by [.gitignore](../.gitignore) and can
always be rebuilt from the pinned book tree. Rebuilding never rewrites the book.

## Section model v2

- Every page has one `overview` section: everything after the frontmatter and before the
  first level-2 heading, including the level-1 title and page introduction.
- Every `##` heading starts one section. Level-3 and deeper headings stay inside their
  owning level-2 section; they are searchable text but not separate citable sections.
- Headings inside fenced code blocks are never treated as sections.
- A heading may carry an explicit `{#stable-anchor}`; otherwise the index derives a
  lowercase slug. Duplicate slugs receive `-2`, `-3` suffixes within one document.
- Section key: `document_id#section_id`. Offsets are Unicode codepoint offsets, not UTF-8
  byte offsets. Each section stores the exact original content for bounded reads.

Known limits: implicit heading slugs are not stable across heading edits; renaming a
heading changes its `section_id` and therefore its citation. Level-3 anchors are not
separately addressable in v2. A future version may add explicit anchors or redirects; the
snapshot identifier prevents silently reusing stale references.

## Published tables

- `meta.manifest`: format version, route snapshot SHA, coverage and unannotated paths,
  document and section counts, per-document content hashes, section model and snapshot ID.
- `sections`: IDs, path, heading and level, title, kind, evidence status, exact content,
  codepoint offsets and document SHA.
- `section_topics`: one row per section and topic, used for exact topic filters.
- `fts`: `section_key` unindexed, plus `title`, `heading` and `body` with `unicode61`.
  BM25 field weights are title 4, heading 3, body 1. For a level-2 section the body
  excludes the heading line, so heading terms are not counted twice.

The snapshot ID hashes the deterministic manifest and every section key, offset and
document hash. Equality means the same logical snapshot; it is not a byte-identical
SQLite-file promise.

## Build, check and failure behavior

~~~sh
mkdir -p generated
python3 scripts/section_fts_index.py build
python3 scripts/section_fts_index.py check
python3 scripts/section_fts_index.py stats
python3 scripts/section_fts_index.py build --full
python3 scripts/section_fts_index.py build --allow-partial
~~~

`build` refuses unannotated pages unless `--allow-partial` explicitly records partial
coverage. `check` reparses every section from the book, compares the route snapshot,
metadata, offsets, content, topics and FTS payload, and fails on any divergence. An
unchanged build returns `unchanged` without rewriting. An incremental build reuses
verified unchanged parsing, then stages and atomically publishes a new whole SQLite file
through `os.replace`; it does not claim in-place B-tree updates.

The target must be an ordinary direct `.sqlite` file inside `generated/`; symlinks and
other destinations are refused. The builder requires SQLite 3.26+ with FTS5 and the exact
weighted-BM25 feature probe, and fails closed if that profile is missing.

## Measured local evidence — 2026-10-22

| Observation | Value |
|---|---|
| Canonical documents | 423, coverage complete, 0 unannotated |
| Sections | 2,753 (423 overviews plus 2,330 level-2 sections) |
| Snapshot ID | `ebd7cae56659889b81d387b36d9337c0620710ef1a78fdc20cc567e6f8e91739` |
| Index file size | 12,922,880 bytes |
| Full build | 1.2 s |
| Deep check | 1.2 s |
| Unchanged incremental build | 2.2 s, 423 documents reused |
| Runtime | Python 3.9.6, SQLite 3.54.0, local checkout |

These are single-machine observations on a warm checkout, not a benchmark, capacity
forecast or performance claim. No independent review or CI run is asserted.

## Verification boundary and next gates

[Ten unit tests](../tests/test_tycho_section_fts_index.py) cover the overview/level-2
model, fence exclusion, offsets, explicit anchors, deterministic full and incremental
builds, partial coverage, stale detection, FTS tampering, corrupt identity, unsafe targets
and the SQLite/FTS5 profile. Tests mock the validated route scan; they do not prove that
every real page is correctly annotated.

Not implemented here: query ranking, snippets, filters over the index, bounded reads and
snapshot refusal at query time (#50); evidence resolution (#51); semantic/hybrid retrieval;
MCP. Any consumer must check the route snapshot before using a published index.
