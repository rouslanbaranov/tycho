# Sufficient-ready pilot — source review

Date: 2026-10-26. Refs #532. Status: source extraction complete; no entry promoted.

## Delegation

Seven read-only reader children extracted seven public units for six entries. Child IDs,
URLs and hashes are in `2026-10-26-pilot-manifest.json`. Delegated reading is not
independent review, human review, CI or sufficient coverage.

## Parent checks

- Recomputed hashes: OWASP, Istio security, Parallel Change and Istio Mirroring matched.
- The Spanner full-body hash is fetch-specific; the reader's stable scoped hashes are used.
- One quoted passage per source was found in the served text.
- All candidate paths exist.
- No reader wrote to the repository.

## Per-entry result

### Federated Identity — evidence-partial

OpenID Federation 1.0 sections 1, 3, 4 and 5 support trust anchors, signed Entity
Statements, trust chains and metadata. Section 11 (revocation and key rollover) was not
read, and OIDC discovery/token validation is outside the scoped sections. The owner can
now state trust-chain mechanics; revocation remains unsupported.

Next: read section 11 and an OIDC discovery unit, then reconcile the owner section.

### RBAC/ABAC — evidence-partial

OWASP supports RBAC, ABAC and ReBAC definitions, least privilege, deny-by-default,
per-request checks and logging. It does not define PDP/PEP, attribute staleness, policy
administration or revocation mechanics; its RBAC/ABAC comparison is argued, not measured.

Next: add a source for policy decision/enforcement and revocation, or narrow the owner
claims to what OWASP supports.

### Workload Identity / mTLS — evidence-partial

Istio Security supports workload identity binding, certificate issuance and rotation,
mTLS, secure naming, peer authentication and authorization policy. It does not support
certificate revocation, trust-root bootstrap, key storage, lifetime policy or SPIFFE.

Blocking metadata issue: `src.istio` in `sources/register.json` points to the architecture
page, while the ledger and this unit use the security page. Resolve before integration.

Next: fix the register/ledger URL mismatch, then reconcile the owner section.

### Dark Launching / Shadow Traffic — evidence-partial

Fowler supports hidden invocation from real user flows, load assessment, feature-flag
rollback and old/new comparison. Istio supports traffic mirroring, fire-and-forget responses and fractional mirroring. Neither source supplies a measurement
method, side-effect suppression or a capacity bound; those remain synthetic.

Next: integrate both sources into the card and owner note, retaining the synthetic label for
measurement and side-effect controls.

### Controlled Cutover — evidence-partial

The Spanner cutover page supports a bounded drain-and-switch sequence: pre-cutover checks,
pausing writes, draining CDC, zero-lag checks, DLQ checks and application switch. It is
product-specific and does not establish a general no-return gate, fallback execution, RTO or
zero-loss guarantee.

Next: decide whether the card is a general mechanism or a bounded example; add a general
source if the former.

### Parallel Run — insufficient-evidence

Fowler's `Parallel Change` supports expand-and-contract only. It does not name or define
Parallel Run, and it has no same-work concurrent processing, output comparison, side-effect
suppression, divergence owner or runtime commit rule. The pilot candidate was wrong for this
entry.

Next: find a dedicated Parallel Run source or re-scope the card. Do not use this unit as
support.

## Decision

No entry is sufficient-ready yet. Five are evidence-partial with explicit next sources; one
is insufficient-evidence. Source extraction alone does not change registry coverage.

## Limits

- Reader claims were spot-checked, not independently re-read in full by the parent.
- No structural validator was run for the new plan/report artifacts.
- No owner section or card was edited in this batch.
