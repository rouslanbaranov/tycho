# Accelerated batch pilot — B2–B6

Status: pilot completed; pipeline adopted with coordination guardrails.

## Result

- 8 entries reviewed and restored: Transactional Outbox, Static Content Hosting,
  Self-Contained Service, Sidecar, Ambassador, Controlled Cutover, Dark Launching,
  RBAC/ABAC.
- Final state: 21 sufficient promotions, 9 owner-accepted (final acceptance deferred).
- Full suite: 606 tests OK at batch end.
- One pre-split batch, parallel packet reviews, delta fixes for two anchors.
- Elapsed pilot window: roughly 1h45 for 8 entries, versus the earlier serial
  per-entry cadence.

## What worked

- pre-splitting all promotion-bound pages once;
- parallel bounded reviews instead of one giant review;
- auto packet generation and delta fixes for link-only changes;
- one full suite at batch end.

## What caused churn

- two agents edited shared `owner-units` concurrently;
- stale pass/promoted labels in review artifacts;
- hardcoded regression guards expecting partial-bounded;
- stale hashes in batch records after remediation.

## Adopted guardrails

1. One writer for shared metadata/owner-units per batch.
2. Freeze batch hashes only after the final remediation commit.
3. Update guards and derived counters at batch end, not per entry.
4. Review in parallel packet groups; no reviewer tests.
5. Promotion allowed on pass with recorded minor findings.
6. No content-addressed promotion migration without a separate L3 issue.
