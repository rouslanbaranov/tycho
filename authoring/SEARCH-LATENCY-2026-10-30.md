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

## Validation cache

Added a validated-manifest cache keyed by index path, mtime, size and inode.
The book/route and facet snapshots are still checked on every query; corrupt or
rebuilt files get a new key.

| Mode | Before p50/p95 | After p50/p95 |
|---|---|---|
| BM25 warm | 133.3/178.5 ms | **66.7/79.7 ms** |
| Margin .05 | 142.6/206.4 ms | **60.2/70.5 ms** |
| Best (20) | 361.7/842.2 ms | **216.5/420.4 ms** |

BM25 cold-cache p50 also falls from 173.7 ms to 53.7 ms because repeated index
validation was the dominant cost. Max outliers remain from process/model warmup.

## Limits

- Local machine, warm process; no production hardware/client.
- AI qrels; no human review, CI, owner acceptance or sufficient coverage.
