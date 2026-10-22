# Independent agent review — sufficient candidates — 2026-10-22

Status: independent non-human agent reviews of selected sufficient-candidate sections.
This is not human review, owner acceptance, per-page review of the corpus or a
sufficient-coverage claim.

- Reviewer: independent review agent (separate from the authoring pass)
- Mode: read-only
- Scope: the sections named below and their atlas cards
- Verdicts: API Gateway pass; Event Sourcing pass; Negative Caching pass; Health
  Endpoint Monitoring pass; Cache-Aside pass-with-findings.

## API Gateway — pass

Original findings:

1. **Mechanism.** No enforcement mechanism for identity forwarding, central-decision
   binding, authentication/quota/authorization order or fail-closed behavior.
2. **Limits.** No bound on quota/rate-limit state or routing-policy staleness.

Remediation: added enforcement order, trusted-context forwarding, fail-closed/break-glass,
quota-state ownership, per-tenant fairness and stale-route limits.

Re-review: **pass**, no findings.

## Event Sourcing — pass

Original findings:

1. **Failure.** The card named replay duplication and schema drift without a recovery
   action; the owner link anchored at §2 did not discuss either.
2. **Invariant.** §2 did not state the expected-version conditional append, racing-command
   rejection or retry double-append risk.

Remediation: §2 states conditional append, re-read/reject and operation identity; the card
names stale-version rejection, idempotent projectors and versioned handlers/rebuild plan.

Re-review: **pass**, no findings.

## Negative Caching — pass

Original findings:

1. **Source.** Status/TTL and error-caching statements lacked a citation, claim ID or ledger
   row.
2. **Mechanism.** No tenant/principal key scoping, revocation invalidation or
   no-entry/tombstone/cached-negative distinction.

Remediation: added the Google CDN citation, page source scope and chapter ledger row;
tenant/principal/operation keying, delete-or-version on change, tombstone distinction and
revocation tests.

Re-review: **pass**, no findings.

## Health Endpoint Monitoring — pass

Original findings:

1. No rule for absent/unknown probe data or probe-path independence.
2. No endpoint exposure, authorization or disclosure limit.

Remediation: fail-open/fail-closed per dependency, independent probe path, missing-data
alerting, caller authorization and disclosure/load limits.

Re-review: **pass**, no findings.

## Cache-Aside — pass-with-findings

Original findings:

1. **Mechanism.** No stale-fill race or definition of the version gate.
2. **Failure/recovery.** The card deferred to an owner section that did not sequence stale
   fills, concurrent misses or failed invalidation.

First remediation: added read-V1/commit-V2/refill-V1, version gate, failed-invalidation
retry/alert and single-flight recovery.

First re-review findings:

1. The "race always remains" claim was too strong; atomic compare-and-set must be
   distinguished from non-atomic check-then-write.
2. Invalidation intent was recorded only after a failed delete; it must be durable at
   commit time, and a missing TTL makes a lost invalidation unbounded.

Second remediation: added atomic/non-atomic distinction and the outbox-in-the-same-
transaction requirement, plus the no-TTL case.

Second re-review finding: the CAS sentence still overstates the guarantee. A cache-key CAS
cannot atomically compare a source revision, and a naive SET NX after DEL can resurrect V1.
The section must say the CAS compares a cached revision/tombstone, with absence treated as
a failed compare.

This latest finding is now remediated: the section compares the cached revision/tombstone
under the shared key and treats absence as a failed compare. It is **not re-reviewed**.
Verdict remains **pass-with-findings**.

## Cache Invalidation — pass-with-findings

Reviewer verdict: **pass-with-findings**. Two findings:

1. **Mechanism.** No read-V1/commit-V2/fill-V1 sequence, fill-version source or mismatch
   action.
2. **Limits.** No invalidation fan-out/coupling, multi-cache/region coherence or TTL/
   versioned-key trade-off.

Remediation: added the stale-fill sequence, source-revision-on-fill with discard/retry, and
fan-out/multi-cache limits with TTL-only and versioned-key alternatives.

Not re-reviewed. Verdict remains **pass-with-findings**.

## Leader Election — pass-with-findings

Reviewer verdict: **pass-with-findings**. Two findings:

1. The card did not separate stale follower reads from linearizable reads requiring
   read-index/lease confirmation.
2. Committed-entry durability was conditional on stable storage and membership behavior,
   but the card mentioned only divergent uncommitted logs and linked only §4.

Remediation: card now requires read-index/lease confirmation for linearizable reads,
states the storage/membership durability contingency and links §5 reconfiguration.

Not re-reviewed. Verdict remains **pass-with-findings**.

## Limits

- Seven sections, not 145 entries or 423 pages.
- Non-human review; no independent human sign-off.
- No `sufficient` promotion; validators still require a complete review record and policy
  change.
