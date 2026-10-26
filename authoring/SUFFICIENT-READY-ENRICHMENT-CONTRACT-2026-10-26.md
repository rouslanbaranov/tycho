# Sufficient-ready enrichment contract — pilot

Date: 2026-10-26. Refs #532, #233. Status: pilot in progress.

## Purpose

Move six pattern entries from `partial-bounded` toward **sufficient-ready** evidence. This contract does not claim sufficient coverage and does not replace independent human review or owner acceptance.

## Pilot scope

1. Federated Identity
2. RBAC/ABAC
3. Workload Identity / mTLS
4. Dark Launching / Shadow Traffic
5. Controlled Cutover
6. Parallel Run

## Workflow per entry

1. Record the current gap: source, owner section, card, decision evidence.
2. Read a bounded public source unit and record exact sections/hash.
3. Reconcile card, owner section and source; remove synthetic-only claims where evidence exists.
4. Produce an evidence matrix: claim -> source section, mechanism, invariant, failure/recovery, alternative, limits.
5. Request an independent Reviewer decision.
6. Record `sufficient-ready` or `insufficient-evidence`; never record `sufficient` in this issue.

## Acceptance

- Six entries have dedicated source support or an explicit `insufficient-evidence` disposition.
- Card, owner and source metadata agree.
- No entry is marked sufficient.
- Reviewer returns PASS/REVISE per entry.
- Structural validators and focused tests pass.

## Preservation

Accepted manuscripts and historical enrichment manifests remain unchanged. New work is additive and revision-recorded.
