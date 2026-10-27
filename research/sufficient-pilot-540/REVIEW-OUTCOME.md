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

## R2 review — 2026-10-27

Report: `authoring/ai-reviews/2026-10-27-sufficient-r2-codex.md`.
SHA-256: `3997c55722125ca28477b4a0e07feb57437710ed334708595187effb1ded5278`.
Reviewed HEAD: `55649c3a`.

Verdict: **pass-with-findings** for the bounded remediation. The six technical
promotion verdicts remain **reject**; no entry qualifies for promotion. `sufficient: 0`.

Residual findings:

- **R2-01:** ASVS source unit still mixed the overview URL/label with the full PDF, and
  one ledger claim still described the page as an overview. Corrected: manifest now
  points to the PDF/versioned label; stale claim removed.
- **R2-02:** Spanner raw HTML hash was not reproducible. Replaced with a reproducible
  canonical article-text hash (`aa3be889...`) computed by `scripts/source_content_hash.py`;
  raw HTML chrome remains mutable and is not the hash domain.
- **R2-03:** four manifest `current_coverage` fields were stale. Synchronized with
  owner units and registry.
- **R2-04:** the mTLS card cited an unexplained eight-heading subset. The eight named
  headings are now listed.

R2 accepts retaining the rejected/blocked pilot; it does not authorize promotion. Any
future promotion requires new evidence and its own review. The R2 revision gap is now
addressed by a documented canonical-text hash, not a sufficient claim.

## R3 review — 2026-10-27

Report: `authoring/ai-reviews/2026-10-27-sufficient-r3-codex.md`.
SHA-256: `0b1ca9965cc40f8522a8f6994a3bb27ea76c5eb99af1dc56d0957c975d4a718d`.
Reviewed HEAD: `7482e650`.

Verdict: **pass-with-findings** for the focused R2-01..R2-04 remediation. The six
technical promotion verdicts remain **reject**; decision verdicts are pass. No entry is
promoted; `sufficient: 0`.

R3-01, non-blocking: three other cards on the shared C11 page still described the ASVS
overview and fourteen headings while citing the full PDF record. Corrected: the three
notes now name the full 120-page ASVS 5.0.0 PDF, V1-V17 and appendices A-E.

The R2 residuals are closed for the six-entry scope. Future promotion still needs
positive technical evidence, not only decision passes.
