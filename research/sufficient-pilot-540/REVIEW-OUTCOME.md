# Sufficient pilot review outcome

Report: `authoring/ai-reviews/2026-10-26-sufficient-pilot-codex.md`.
SHA-256: `b755e412cf6de44e58d111448dd2595a228dbd4a133d20087f65ffccd13faaa9`.
Reviewed HEAD: `cf9e02f2`.

Verdict: **reject**. No entry is promoted. `sufficient: 0`.

## Findings

- **P540-01, blocking:** the six owner-unit technical evidence records mark all four
  dimensions supported although several quoted clauses are synthetic or not bound to the
  source. All six technical assessments reject.
- **P540-02, blocking:** five ledger records have contradictory reading scopes
  (sections read vs sections not read vs `read_scope`).
- **P540-03, blocking:** RFC 9700 and Spanner fresh bytes do not reproduce the recorded
  hashes, and the ASVS record pins an overview representation while claiming the full
  PDF.
- **P540-04, non-blocking:** two card source notes describe stale or duplicated scopes.

## Disposition

No promotion record was added. The six entries remain `partial-bounded` for now; the
required correction may lower individual dimensions to `partial` where the bound source
does not support the full clause.

Remediation must precede a focused re-review. A pass on the earlier hand-off is not
reused, and the original reject remains historical for its snapshot.

## Remediation applied

- **P540-01:** unsupported pilot dimensions were downgraded from `supported` to
  `partial` with explicit reasons. Technical coverage is now four `partial` and two
  `partial-bounded` entries; no entry is sufficient.
- **P540-02:** NIST, OpenID Federation, Spanner Cutover, MinimumCD and ASVS ledger
  scopes were reconciled with their section lists and source-plan bindings.
- **P540-03:** ASVS now pins the 120-page 5.0.0 PDF (`a2fa1bbe...`); RFC 9700 and
  Spanner hashes were refreshed to the served representations and documented.
- **P540-04:** RBAC/ABAC and Workload Identity source notes were rewritten; duplicate
  prose was removed.

Artifact counts after remediation: 141 `partial-bounded` technical, 4 `partial`,
0 sufficient. Six pilot entries remain unpromoted and blocked.

A focused re-review of the changed evidence is required. The prior reject remains
historical for `cf9e02f2`.
