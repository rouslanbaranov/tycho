# Search snapshot and reindex protocol

Status: pre-enrichment freeze. Quality tuning is suspended until the book
content stabilizes and qrels are re-adjudicated.

## Purpose

The book and its qrels can change during enrichment. This harness freezes the
current search/content state, detects stale derived artifacts, and rebuilds the
index without rewriting labels.

It never edits `book/`, rewrites qrels or claims that the frozen labels remain
valid after content changes.

## Commands

```sh
python3 scripts/search_reindex.py snapshot
python3 scripts/search_reindex.py check
python3 scripts/search_reindex.py rebuild
```

- `snapshot` rebuilds the route index and section index, then writes
  `edition/patterns/search-pre-enrichment.v1.json`.
- `check` compares content, route, section index and qrels hashes. Exit code 0
  only when the snapshot is fully current; stale qrels produce
  `current-with-stale-qrels` and exit 1.
- `rebuild` rebuilds route/section indexes and writes
  `generated/search-reindex-report.json`. It does not change qrels.

## Frozen pre-enrichment state

The manifest records:

- 423 book files and their content digest;
- route snapshot `06b80bd6…` (current at freeze time);
- 2,751 H2 sections and 504 H3 passages;
- qrels hashes, item counts and route bindings;
- `qrels_stale: [corpus-qrels.v2.json]` because the current route no longer
  matches that older qrels snapshot;
- `quality_claims: suspended-until-post-enrichment-revalidation`.

This is intentional: the harness exposes the mismatch instead of silently
rebinding labels.

## After enrichment

1. Run `rebuild`.
2. Re-adjudicate accepted answers and the excluded phase-3 items.
3. Rebuild the human sample.
4. Only then recalibrate BM25/gate/ranking metrics.
5. Preserve this manifest as pre-enrichment evidence; do not overwrite it.

## Limits

- The freeze is a derived snapshot, not human review or sufficient coverage.
- Stale qrels are reported, not repaired.
- No CI, owner acceptance or quality claim.
