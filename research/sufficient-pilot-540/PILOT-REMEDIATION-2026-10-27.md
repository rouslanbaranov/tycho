# Pilot six remediation

Status: six pilot entries are reviewed but not sufficient. Four other entries are already
sufficient through the batch path; this file tracks the original six.

- **Workload Identity-mTLS** (partial-bounded): failure and alternative bindings are synthetic;
  add an admitted representation for rotation failure and permissive mode.
- **Dark Launching / Shadow Traffic** (partial): invariant and failure are synthetic; find a
  primary source for shadow-copy isolation and comparison.
- **RBAC / ABAC** (partial): invariant, failure and alternative are synthetic; bind policy
  decision and denial behavior to an admitted source.
- **Federated Identity** (partial-bounded): failure and alternative are synthetic; bind
  federation metadata and trust failure to OpenID Federation text.
- **Controlled Cutover** (partial): all four dimensions are synthetic; define the mechanism from
  a primary cutover source.
- **Parallel Run** (partial): invariant and alternative are synthetic; bind comparison key,
  side-effect boundary and the shadow/canary alternative.

## Order

1. Workload Identity-mTLS: add the Istio source-markdown representation and bind rotation and
   permissive-mode passages.
2. Federated Identity: use the OpenID Federation full-unit record for metadata and trust failure.
3. Parallel Run: locate the MinimumCD source text for comparison and side-effect boundaries.
4. Dark Launching, RBAC/ABAC, Controlled Cutover: source-first; rewrite only after a quote exists.

## Gate

Each entry needs four supported dimensions, a saved external report, and a promotion record.
A pass is not owner acceptance. The four existing sufficient entries still await the owner
decision in `authoring/OWNER-ACCEPTANCE-PACKAGE-2026-10-27.md`.
