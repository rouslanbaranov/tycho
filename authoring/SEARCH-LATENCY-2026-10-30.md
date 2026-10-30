# Search latency baseline — 2026-10-30

Status: local warm benchmark; not production-client, CI or sufficient coverage.

## Results

150 qrels v4 queries; index 17,170,432 bytes:

| Mode | Mean | p50 | p95 | Max |
|---|---:|---:|---:|---:|
| BM25 cold cache | 186.6 ms | 173.7 ms | 263.7 ms | 947.2 ms |
| BM25 warm cache | 139.3 ms | 133.3 ms | 178.5 ms | 315.1 ms |
| margin .05 | 150.8 ms | 142.6 ms | 206.4 ms | 316.9 ms |
| best (20 queries) | 723.5 ms | 361.7 ms | 842.2 ms | 6873.3 ms |

open_snapshot alone: p50 **117.5 ms**, dominated by PRAGMA quick_check and
manifest/row-count validation on every query.

## Implication

BM25 is ~20 ms of actual query work; most warm latency is repeated index
validation. Best mode has a cold model-load spike and remains opt-in.

## Next

Cache index validation by file identity (mtime/size) while still checking the
book/route snapshot. Re-measure after the change.

## Limits

- Local machine, warm process; no production hardware/client.
- AI qrels; no human review, CI, owner acceptance or sufficient coverage.
