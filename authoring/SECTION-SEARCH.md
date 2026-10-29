# Snapshot-bound section search and bounded reads (E07-04, E17-70)

> Issue [#50](https://github.com/rouslanbaranov/tycho/issues/50), M4; H3 parent-H2
> retrieval added for E17-70. **Status 2026-10-24:** local implementation over the #49
> section snapshot; not merged, not independently reviewed, not an MCP or production
> service. No held-out human relevance evaluation exists; the measurements below are
> diagnostics.

## Scope and authority

[section_search.py](../scripts/section_search.py) is a read-only consumer of the
deterministic [section index](SECTION-FTS-INDEX.md) and of the canonical book bytes that
index pins. It performs two operations:

- **search** returns ranked parent-H2 section candidates with a bounded excerpt, an
  optional internal H3 passage diagnostic, and a citation;
- **read** returns an exact codepoint range from one selected parent-H2 section;
- **v12** returns the derived V12 model/scenario/run/decision lookup for a pattern.

The canonical Markdown and its frontmatter remain authoritative. The tool never edits the
book, rebuilds the index implicitly, fetches sources, runs embeddings or writes evidence.
It is lexical retrieval only: semantic/hybrid retrieval (#52–#55), evidence resolution
(#51) and MCP transport (#57–#60) are separate.

## Snapshot discipline

Every search and read call:

1. opens `generated/sections-fts-v5.sqlite` in read-only mode;
2. runs `PRAGMA quick_check`, validates the manifest and compares stored section, FTS,
   passage and passage-FTS row counts with the manifest;
3. binds the book to the index: a process-local cache, keyed by SHA-256 of every
   `book/**/*.md` document and the metadata schema, reuses a canonical scan only
   for byte-identical inputs; a changed book or schema forces a full
   `route_index.canonical_scan`, whose snapshot SHA is compared with the
   manifest's pinned route snapshot;
4. refuses the call when the book or metadata changed after the index was published.

The search layer also accepts V12 `artifact_type`, `volume` and `pattern_ids` filters. Book
sections carry the first two; the derived V12 artifact lookup returns model, scenario, run and
decision contracts for a pattern even though those JSON contracts are not book sections.

The deep structural verifier remains `section_fts_index.py check`, which reparses every
section and H3 passage and compares parent mappings, offsets, content, topics and both
FTS payloads. Search deliberately does not reparse all sections per query; the route
snapshot covers every page byte and every metadata value, so a stale index cannot
silently answer. The cache is process-local and never bypasses the index checks: every
call still opens the SQLite file, runs `quick_check`, validates the manifest and row
counts, and compares the pinned route snapshot. A changed, added, removed, renamed or
symlinked page, a changed schema, a stale route snapshot and a corrupt or missing index
all still fail closed. The first validation after process start pays one full scan;
later queries reuse it only while the complete input state is byte-identical.

Failure is explicit: a stale snapshot raises `snapshot-mismatch`; a missing, corrupted or
incompatible index raises `not-available`; unknown section IDs raise `not-found`.

## Search

~~~sh
python3 scripts/section_fts_index.py build
python3 scripts/section_search.py search --query "idempotent consumer duplicate" --limit 5
python3 scripts/section_search.py search --query "retry" --all-sections
python3 scripts/section_search.py search --query "retry budget" --kind page
python3 scripts/section_search.py search --query "rollback" --topic deployment
python3 scripts/section_search.py search --query "retry" --path-prefix book/volumes/v04
~~~

Inputs are tokenized to Unicode words and every token is quoted before it reaches FTS5, so
query operators such as `OR`, `*` and `-` are treated as text, not syntax. A multi-term query
is an any-term OR query: BM25 decides which section explains the most terms, and
`match_mode` is always `any-terms`. This is recall-oriented; it does not prove that every
term was relevant.

H2 sections and internal H3 passages are matched in separate FTS tables. An H3 match is
mapped to its parent H2 before any public result is built. Within one document, the
best parent selected by parent-H2 or passage score becomes the single candidate; across
documents, order remains anchored to the parent-H2 score so the H2 baseline is not
silently reranked. By default the adapter returns that best section per document so the
first page lists distinct candidate pages. `all_sections=true`, or `--all-sections` on the
CLI, returns unique matching parent sections instead; `result_scope` reports which mode
produced the page.

Ranking uses FTS5 BM25 with field weights title 5, heading 2 and body 0.25. The reported
`score` is the negated BM25 value, so a higher score means a better match. When an H3
passage supplies the selected parent, `score` is the passage BM25 value and
`match_source` is `h3-passage`; otherwise the parent-H2 score is used. Ties break by
`section_key`. The ranker version is `tycho-section-fts5-bm25-v5`; scores from other
rankers or snapshots are not comparable.

Supported filters are `kind`, `topic`, `evidence_status` and `path_prefix`. A path prefix
must be a relative path under `book/`; absolute paths, backslashes and `..` segments are
rejected. Filters are applied before the result limit, so a filtered zero-hit result means
"no section in this filter", not "no such knowledge".

Each result carries the parent document and section IDs, canonical path, heading and
level, title, kind, evidence status, parent section offsets, matched terms, a
whitespace-normalized excerpt of at most 240 characters, the score and the ranker version.
An H3 match adds `matched_passage_id`, `matched_passage_key`,
`matched_passage_heading`, `matched_passage_score`, parent-relative passage offsets and a
passage excerpt. These diagnostics never change `section_key`, `section_id`, `content`,
offsets or the citation. `truncated` says whether more matches exist beyond `limit`; the
initial limit is a routing heuristic, not an evidence ceiling.

Citations use `path#section_id` and `citation_scheme: tycho.section-key.v2`. This is a
stable snapshot-scoped identifier, not a guarantee that the same string is a valid GitHub
URL anchor. Consumers must keep the snapshot ID with the citation.

## Read

~~~sh
python3 scripts/section_search.py read \
  --id "tycho.page.0123456789abcdef0123456789abcdef#overview" \
  --offset 0 --budget-chars 2000 --include-evidence
python3 scripts/section_search.py evidence --claim claim.same-intent-retry
python3 scripts/section_search.py evidence --document <document_id>
~~~

A read validates the parent section key, offset and budget, rechecks the snapshot and
the document SHA, and returns the requested codepoint range from the unchanged H2
section, including any H3 headings inside it. Internal passage keys are diagnostics, not
read identifiers. `offset` and `next_offset` are relative to the section;
`document_char_start` and `document_char_end` are relative to the whole page.
`truncated` and `next_offset` expose bounded continuation. A document that changed after
publication is refused as `snapshot-mismatch`; the adapter never slices a newer file with
an older offset.

Limits: `limit` 1–20, `budget_chars` 1–5,000, excerpt at most 240 characters, and no full
document is returned by search. Offsets are Unicode codepoint offsets, not UTF-8 bytes.

## Evidence

`evidence` accepts exactly one of `--document`, `--claim` or `--source`, rechecks the
section index, resolves the record through [section_evidence.py](../scripts/section_evidence.py)
and adds `search_snapshot` and `search_route_snapshot` to the evidence result. The separate
evidence snapshot still guards the claim ledger, register and lock; pass
`--expected-evidence-snapshot` to refuse a changed record. `read --include-evidence` embeds
the document-level evidence block in a read response.

The resolver returns registered metadata, relations, contradictions and unavailable-source
outcomes only. It does not return source text, permitted excerpts or an answer verdict.

## Response statuses

| Status | Meaning |
|---|---|
| `ok` | At least one parent section matched and every consistency check passed. |
| `no-results` | The query is valid but no section matched under the filters. |
| `invalid-request` | Bad query, limit, offset, budget, filter or path prefix. |
| `not-found` | The requested section or evidence ID is absent from this snapshot. |
| `not-available` | The index or evidence components are missing, unreadable or incompatible. |
| `snapshot-mismatch` | The book or metadata changed after the index was published. |

A `no-results` answer is not proof that the corpus lacks the concept; it only reports this
snapshot, index and filter scope.

## Retrieval-contract coverage and gaps

The implementation currently provides the contract's search identifier, path, heading,
bounded excerpt, score kind, ranker version, filters, truncation and snapshot identity,
optional H3 passage diagnostics, and the read offsets, hash check, truncation and next
offset. Not implemented yet: opaque cursors, estimated totals, permitted excerpts,
lexical-plus-evidence quality measurement, vector or hybrid ranking, per-result semantic
confidence and MCP envelopes (#57–#60). The bounded evidence operation exists; these
remaining gaps are not implied to be complete.

## Measured local evidence — 2026-10-24

| Observation | Value |
|---|---|
| Indexed documents, sections and H3 passages | 423, 2,753 and 504 |
| Index snapshot | `8c797c532e473f079aa32da5986e85b27ba311c1bbb259af27fd0ee25d548182` |
| Unit tests | 20 offline search/read tests |
| Runtime | Python 3.9.6, SQLite 3.54.0 |

The timings and retrieval measurements are single-machine diagnostics, not a benchmark,
latency SLO or capacity forecast.

### Snapshot-validation latency diagnostic — 2026-10-29

| Observation | Before | After |
|---|---:|---:|
| p50, 20 answerable qrels items, 3 repeats | 593.2 ms | 102.9 ms |
| p95, same run | 619.1 ms | 143.3 ms |

Both runs used `scripts/search_perf.py` with warmup 3 on the same published snapshot
and the first 20 answerable items of qrels v2. Before recomputed
`route_index.canonical_scan` on every query; after reuses the process-local
byte-keyed scan cache. All 155 answerable qrels items produced identical serialized
search results before and after the change. Runtime for this diagnostic was Python
3.15.0 and SQLite 3.54.1. The cache is process-local: a fresh process pays one full
canonical scan before reuse, and each process validates independently. `quick_check`
still runs on every call. These are single-machine diagnostics, not a benchmark,
latency SLO or capacity forecast.

### H3 parent-H2 retrieval diagnostic

The H3 layer was compared with the same H2-only baseline on qrels v2 (155 answerable
items of 220) and the phase-3 filtered answerable set (19 items), at limit 10 and 5
respectively, with abstention disabled to isolate retrieval:

| Measurement | H2 baseline | H3 parent mapping |
|---|---:|---:|
| qrels v2 section hit@1 | 0.4000 | 0.4000 |
| qrels v2 section hit@5 | 0.7806 | 0.7806 |
| qrels v2 section MRR | 0.5516 | 0.5516 |
| qrels v2 page hit@5 | 0.8129 | 0.8129 |
| qrels v2 nDCG@10 | 0.6091 | 0.6091 |
| phase-3 section hit@5 | 10/19 (0.5263) | 11/19 (0.5789) |
| phase-3 dev section hit@5 | 7/13 (0.5385) | 8/13 (0.6154) |
| phase-3 page hit@5 | 15/19 (0.7895) | 15/19 (0.7895) |

Phase-3 labels are agent-authored and agent-adjudicated; the 19-item answerable set is a
small challenge set, not training data or human review. The gain is concentrated in
selecting a more specific parent H2 within an already retrieved document. The refusal gate
was not retrained. Because a passage can supply the selected parent score, gate features
can shift; no claim is made that retention or false-answer counts are unchanged.

## Verification boundary

The tests use synthetic two-page snapshots and mocked route scans. They cover ranking,
any-term matching, H3 parent mapping and diagnostics, parent read behavior, per-document
dedupe, filters, validation, stale refusal, tampered section and passage row counts,
bounded reads and offset continuation. Cache tests cover reuse for unchanged input,
book-change invalidation, route-snapshot mismatch after a warm cache, missing or corrupt
indexes, and concurrent single-flight validation. They do not prove relevance on the
423-page corpus, answer quality, citation correctness, process-level cache behavior or
performance under production load. The 25-question smoke is in-sample against
author-created labels, not a held-out benchmark or qrels set. No independent review,
gold relevance set or CI result is claimed.

Next gates: build a corpus-level qrels set and ranking baseline before claiming search
quality; add evidence resolution (#51); then MCP envelopes (#57–#60).
