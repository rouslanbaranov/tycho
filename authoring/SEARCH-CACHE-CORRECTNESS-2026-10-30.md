# Search cache correctness — 2026-10-30

Status: production audit fix. No ranking/default change.

## Defect

The query cache key omitted:

- `include_artifacts`;
- BM25 field weights.

A query first cached without artifacts could return the cached payload after
`include_artifacts=True`; changing `TYCHO_BM25_WEIGHTS` could return the old
ranking.

## Fix

Both values are now part of `_query_cache_key`. Regression test constructs keys
with/without artifacts and with different weights and asserts they differ.

## Verification

- targeted 33 tests PASS;
- full suite 728 PASS;
- premerge PASS;
- book/atlas/index unchanged.

## Limits

- No production-client cache exercise.
- AI qrels; no human review, CI, owner acceptance or sufficient coverage.
