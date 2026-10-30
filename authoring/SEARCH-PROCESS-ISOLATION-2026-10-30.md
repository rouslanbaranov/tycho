# Process isolation benchmark — 2026-10-30

Status: local bounded benchmark. Not a production-client measurement; no human
review, CI, owner acceptance or sufficient coverage.

## Results

150 qrels v4 queries; one process per worker; 0 mismatches.

| Processes | Elapsed | Mismatches |
|---:|---:|---:|
| 2 | 14.2 s | 0 |
| 4 | **9.3 s** | 0 |
| 8 | **8.6 s** | 0 |

For comparison, the bounded thread path (2 workers) was 13.1 s and the
16-thread capped run was 20.0 s.

## Interpretation

- Process isolation removes the GIL/SQLite thread contention.
- 4 processes give most of the gain; 8 is only modestly faster.
- Each process opens its own read-only index and validation cache; memory grows
  with process count.
- A production MCP pool should start at 4 processes and be bounded by memory.

## Decision

No server change in this experiment. Keep the in-process semaphore for now;
process isolation is the preferred next step for concurrent clients.

## Limits

- Local hardware; warm filesystem; AI qrels.
- No production-client load, no long-running soak.
- No human review, CI, owner acceptance or sufficient coverage.
