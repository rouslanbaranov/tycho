# Snapshot-bound section search and bounded reads (E07-04)

> Issue [#50](https://github.com/rouslanbaranov/tycho/issues/50), M4. **Status 2026-10-22:**
> local implementation over the #49 section snapshot; not merged, not independently
> reviewed, not an MCP or production service. Search quality on the full corpus is not
> evaluated here.

## Scope and authority

[section_search.py](../scripts/section_search.py) is a read-only consumer of the
deterministic [section index](SECTION-FTS-INDEX.md) and of the canonical book bytes that
index pins. It performs two operations:

- **search** returns ranked section candidates with a bounded excerpt and a citation;
- **read** returns an exact codepoint range from one selected section.

The canonical Markdown and its frontmatter remain authoritative. The tool never edits the
book, rebuilds the index implicitly, fetches sources, runs embeddings or writes evidence.
It is lexical retrieval only: semantic/hybrid retrieval (#52–#55), evidence resolution
(#51) and MCP transport (#57–#60) are separate.

## Snapshot discipline

Every search and read call:

1. opens `generated/sections-fts-v2.sqlite` in read-only mode;
2. runs `PRAGMA quick_check`, validates the manifest and compares stored section and FTS
   row counts with the manifest;
3. recomputes `route_index.canonical_scan` and compares its snapshot SHA with the
   manifest's pinned route snapshot;
4. refuses the call when the book or metadata changed after the index was published.

The deep structural verifier remains `section_fts_index.py check`, which reparses every
section and compares offsets, content, topics and the FTS payload. Search deliberately
does not reparse all sections per query; the route snapshot covers every page byte and
every metadata value, so a stale index cannot silently answer.

Failure is explicit: a stale snapshot raises `snapshot-mismatch`; a missing, corrupted or
incompatible index raises `not-available`; unknown section IDs raise `not-found`.

## Search

~~~sh
python3 scripts/section_fts_index.py build
python3 scripts/section_search.py search --query "idempotent consumer duplicate" --limit 5
python3 scripts/section_search.py search --query "retry budget" --kind page
python3 scripts/section_search.py search --query "rollback" --topic deployment
python3 scripts/section_search.py search --query "retry" --path-prefix book/volumes/v04
~~~

Inputs are tokenized to Unicode words and every token is quoted before it reaches FTS5, so
query operators such as `OR`, `*` and `-` are treated as text, not syntax. Search first
requires all terms in one section. If that returns nothing for a multi-term query, it
retries any term and reports `match_mode: any-terms` with `broadened: true`. A broadened
result is a recall fallback, not evidence that every term was relevant.

Ranking uses FTS5 BM25 with field weights title 4, heading 3 and body 1. The reported
`score` is the negated BM25 value, so a higher score means a better match. Ties break by
`section_key`. The ranker version is `tycho-section-fts5-bm25-v2`; scores from other
rankers or snapshots are not comparable.

Supported filters are `kind`, `topic`, `evidence_status` and `path_prefix`. A path prefix
must be a relative path under `book/`; absolute paths, backslashes and `..` segments are
rejected. Filters are applied before the result limit, so a filtered zero-hit result means
"no section in this filter", not "no such knowledge".

Each result carries the document and section IDs, canonical path, heading and level, title,
kind, evidence status, section offsets, matched terms, a whitespace-normalized excerpt of at
most 240 characters, the score and the ranker version. `truncated` says whether more
matches exist beyond `limit`; the initial limit is a routing heuristic, not an evidence
ceiling.

Citations use `path#section_id` and `citation_scheme: tycho.section-key.v2`. This is a
stable snapshot-scoped identifier, not a guarantee that the same string is a valid GitHub
URL anchor. Consumers must keep the snapshot ID with the citation.

## Read

~~~sh
python3 scripts/section_search.py read \
  --id "tycho.page.0123456789abcdef0123456789abcdef#overview" \
  --offset 0 --budget-chars 2000
~~~

A read validates the section key, offset and budget, rechecks the snapshot and the
document SHA, and returns the requested codepoint range. `offset` and `next_offset` are
relative to the section; `document_char_start` and `document_char_end` are relative to the
whole page. `truncated` and `next_offset` expose bounded continuation. A document that
changed after publication is refused as `snapshot-mismatch`; the adapter never slices a
newer file with an older offset.

Limits: `limit` 1–20, `budget_chars` 1–5,000, excerpt at most 240 characters, and no full
document is returned by search. Offsets are Unicode codepoint offsets, not UTF-8 bytes.

## Response statuses

| Status | Meaning |
|---|---|
| `ok` | At least one section matched and every consistency check passed. |
| `no-results` | The query is valid but no section matched under the filters. |
| `invalid-request` | Bad query, limit, offset, budget, filter or path prefix. |
| `not-found` | The requested section key is absent from this snapshot. |
| `not-available` | The index is missing, unreadable, corrupt or format-incompatible. |
| `snapshot-mismatch` | The book or metadata changed after the index was published. |

A `no-results` answer is not proof that the corpus lacks the concept; it only reports this
snapshot, index and filter scope.

## Retrieval-contract coverage and gaps

The implementation currently provides the contract's search identifier, path, heading,
bounded excerpt, score kind, ranker version, filters, truncation and snapshot identity, and
the read offsets, hash check, truncation and next offset. Not implemented yet: opaque
cursors, estimated totals, the evidence operation (#51), vector or hybrid ranking,
per-result semantic confidence and MCP envelopes (#57–#60). These gaps are not implied to be
complete by this document.

## Measured local evidence — 2026-10-22

| Observation | Value |
|---|---|
| Indexed documents and sections | 423 and 2,753 |
| Index snapshot | `ebd7cae56659889b81d387b36d9337c0620710ef1a78fdc20cc567e6f8e91739` |
| CLI search, warm local run | about 1.16 s end to end |
| CLI read, warm local run | about 1.06 s end to end |
| Dominant cost | route-snapshot revalidation, not FTS5 matching |
| Unit tests | 10 offline search/read tests |
| Runtime | Python 3.9.6, SQLite 3.54.0 |

The timings are single-machine observations including interpreter startup and metadata
validation. They are not a benchmark, a latency SLO or a capacity forecast.

## Verification boundary

The tests use synthetic two-page snapshots and mocked route scans. They cover ranking,
filters, broadening, validation, stale refusal, tampered row counts, bounded reads and
offset continuation. They do not prove relevance on the 423-page corpus, answer quality,
citation correctness, concurrency behavior or performance under load. No independent
review, gold relevance set or CI result is claimed.

Next gates: build a corpus-level qrels set and ranking baseline before claiming search
quality; add evidence resolution (#51); then MCP envelopes (#57–#60).
