# Deterministic section and H3 passage lexical indexing (E07-03, E17-70)

> Issue [#49](https://github.com/rouslanbaranov/tycho/issues/49), M4; H3 parent-H2
> passages added for E17-70. **Status 2026-10-24:** local implementation exercised on
> the current 423-page corpus; not merged, not independently reviewed, not a search or
> MCP service. Python 3.9.6 and SQLite 3.54.0 were used locally; the repository
> validation requirements are unchanged.

## Scope and authority

[section_fts_index.py](../scripts/section_fts_index.py) builds a read-only SQLite FTS5
snapshot from canonical Markdown and its validated YAML frontmatter. It calls the existing
[route-index scanner](../scripts/route_index.py) for document IDs, kinds, topics, evidence
status, paths, source hashes and coverage. It does not create frontmatter, fetch sources,
enrich prose, run embeddings, build a graph or expose MCP.

The canonical book remains authoritative. The index is a disposable generated artifact at
`generated/sections-fts-v5.sqlite`; it is excluded by [.gitignore](../.gitignore) and can
always be rebuilt from the pinned book tree. Rebuilding never rewrites the book.

The v5 schema adds nullable `artifact_type` and `volume` columns plus the
`section_patterns` table. They are populated from the derived V12 index and reverse index;
V12 artifacts themselves stay JSON contracts and are exposed by the search-layer lookup.

## Section model

- Every page has one `overview` section: everything after the frontmatter and before the
  first level-2 heading, including the level-1 title and page introduction.
- Every `##` heading starts one section. The section content still contains its level-3
  and deeper headings, so parent-H2 offsets and bounded reads are unchanged.
- Every `###` heading inside an H2 section also starts an internal passage. The passage
  ends at the next level-3 heading or at the parent H2 boundary. Level-4 and deeper
  headings stay inside the owning passage text.
- Headings inside fenced code blocks are never treated as sections or passages.
- A heading may carry an explicit `{#stable-anchor}`; otherwise the index derives a
  lowercase slug. Duplicate slugs receive `-2`, `-3` suffixes within one parent.
- Section key: `document_id#section_id`; passage key: `section_key~passage_id`. Offsets
  are Unicode codepoint offsets, not UTF-8 byte offsets. Each section and passage stores
  the exact original content for bounded reads and verification.

Known limits: implicit heading slugs are not stable across heading edits; renaming a
heading changes its `section_id` or passage `passage_id`. Passages are internal
diagnostics, not public citations, and their keys are not accepted by section reads. A
future version may add explicit anchors or redirects; the snapshot identifier prevents
silently reusing stale references.

## Published tables

- `meta.manifest`: format version, route snapshot SHA, coverage and unannotated paths,
  document, section and passage counts, per-document content hashes, section and passage
  models, and the snapshot ID.
- `sections`: IDs, path, heading and level, title, kind, evidence status, exact content,
  codepoint offsets and document SHA.
- `passages`: internal H3 key and ID, parent section key and ID, document and path,
  heading, title, exact content and body, codepoint offsets and document SHA.
- `section_topics`: one row per section and topic, used for exact topic filters.
- `fts`: `section_key` unindexed, plus `title`, `heading` and `body` with `porter unicode61`.
- `passage_fts`: `passage_key` unindexed, plus the same three indexed fields.
  BM25 field weights are title 5, heading 2, body 0.25. For an H2 section or H3 passage
  the body excludes the heading line, so heading terms are not counted twice.

The snapshot ID hashes the deterministic manifest and every section and passage key,
parent, offset and document hash. Equality means the same logical snapshot; it is not a
byte-identical SQLite-file promise.

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
coverage. `check` reparses every section and H3 passage from the book, compares the route
snapshot, metadata, parent mapping, offsets, content, topics and both FTS payloads, and
fails on any divergence. An unchanged build returns `unchanged` without rewriting. An
incremental build reuses verified unchanged H2 parsing, redelivers deterministic
passages, then stages and atomically publishes a new whole SQLite file through
`os.replace`; it does not claim in-place B-tree updates.

The target must be an ordinary direct `.sqlite` file inside `generated/`; symlinks and
other destinations are refused. The builder requires SQLite 3.26+ with FTS5 and the exact
weighted-BM25 feature probe, and fails closed if that profile is missing.

## Measured local evidence — 2026-10-24

| Observation | Value |
|---|---|
| Canonical documents | 423, coverage complete, 0 unannotated |
| Sections | 2,753 (423 overviews plus 2,330 level-2 sections) |
| H3 passages | 504 passages under 229 level-2 sections |
| Snapshot ID | `8c797c532e473f079aa32da5986e85b27ba311c1bbb259af27fd0ee25d548182` |
| Index file size | 16,338,944 bytes |
| Full build / deep check / unchanged build | 3.7 s / 2.3 s / 3.5 s, 423 documents reused |
| Runtime | Python 3.9.6, SQLite 3.54.0, local checkout |

These are single-machine observations on a warm checkout, not a benchmark, capacity
forecast or performance claim. No independent review or CI run is asserted.

## Verification boundary and next gates

[Fourteen unit tests](../tests/test_tycho_section_fts_index.py) cover the overview/level-2
model, H3 parent binding and keys, fence exclusion, offsets, explicit anchors,
deterministic full and incremental builds, partial coverage, stale detection, FTS and
passage tampering, format-version refusal, corrupt identity, unsafe targets and the
SQLite/FTS5 profile. Tests mock the validated route scan; they do not prove that every
real page is correctly annotated.

Not implemented here: query ranking, snippets, filters over the index, bounded reads and
snapshot refusal at query time (#50); evidence resolution (#51); semantic/hybrid retrieval;
MCP. Any consumer must check the route snapshot before using a published index.
