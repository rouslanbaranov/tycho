# Search concurrency audit — 2026-10-30

Status: local audit on the validation-cached BM25 path. No default change.
Not a production-client benchmark; no human review, CI, owner acceptance or
sufficient coverage.

## Results

150 qrels v4 queries; one round per worker count; 0 result mismatches at every
level.

| Workers | Elapsed | Mismatches |
|---:|---:|---:|
| 1 | 15.6 s | 0 |
| 2 | **13.1 s** | 0 |
| 4 | 24.0 s | 0 |
| 8 | 35.9 s | 0 |
| 16 | 43.0 s | 0 |

Three 16-worker rounds: 34.6/35.3/40.4 s, 0 mismatches.

## Interpretation

- Cached validation is thread-safe: no fingerprint divergence.
- Throughput peaks at ~2 workers; 4+ degrade from SQLite/GIL contention.
- 16-thread concurrency is ~3x slower than 2 workers.
- A single process should cap concurrent searches near 2, or use separate
  processes for parallel clients.
- Do not raise thread concurrency based on this result.

## Follow-up

- Consider a bounded search semaphore or process pool for MCP concurrency.
- Keep BM25 latency default and validation cache.
- Verify with a production client before selecting a concurrency limit.

## Limits

- Local machine; warm process; AI qrels.
- No production-client, CI, human review or sufficient coverage.
