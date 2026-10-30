# MCP multi-process throughput — 2026-10-30

Status: local stdio benchmark; no default change, no production-client or human
review.

## Results

150 qrels v4 queries; one MCP server process per worker; 0 errors.

| Processes | Elapsed | Responses |
|---:|---:|---:|
| 1 | 7.8 s | 151 |
| 2 | 4.6 s | 152 |
| 4 | **3.1 s** | 154 |

Responses include initialize/tools metadata; all query calls returned without
MCP errors.

## Interpretation

- Multi-process MCP scales: 4 processes are 2.5x faster than one.
- The in-process thread semaphore is still correct for one server; process
  isolation is the preferred deployment for concurrent clients.
- Start at 4 processes and bound by memory; each process has its own index
  connection/validation cache.

## Decision

No server code change. Deploy multiple MCP server processes rather than
increasing threads. Keep the semaphore as a per-process guard.

## Limits

- Local machine, warm filesystem; no production client/load generator.
- AI qrels; no human review, CI, owner acceptance or sufficient coverage.
