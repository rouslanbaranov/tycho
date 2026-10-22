# Independent agent review — sufficient candidates — 2026-10-22

Status: one section reviewed and re-reviewed by an independent non-human agent. This is
not human review, owner acceptance, per-page review of the corpus or a sufficient-coverage
claim.

- Reviewer: independent review agent (separate from the authoring pass)
- Scope: the **API Gateway** owner section and its atlas card only
- Mode: read-only
- Verdict: **pass-with-findings**

## Findings

1. **Mechanism.** The section asserted that a gateway is trusted only for the functions
   it enforces, but did not explain enforcement: identity establishment/forwarding,
   binding a central decision to the request, the order of authentication, quota and
   resource authorization, or fail-closed behavior when the policy plane is unavailable.
2. **Limits.** Quota/rate-limit state and routing-policy staleness were not bounded:
   shared counters, per-tenant fairness, counter-store outage and stale-route behavior
   were missing.

## Remediation applied after the review

- Added an **Enforcement** paragraph: authenticate, forward integrity-protected context,
  bind decision to audience/action/resource/tenant, then authorize at the resource-owned
  boundary; fail closed without a bounded audited break-glass path.
- Extended **Limits**: quota-state ownership, per-tenant fairness, counter-store outage,
  and stale route as a routing failure rather than a quota decision.

## Re-review

A second read-only independent-agent review examined the remediation and returned
**pass** with no findings. It confirmed the enforcement order, trusted-context binding,
fail-closed/break-glass behavior and the quota/routing limits.

The original verdict was **pass-with-findings**; the current verdict is **pass**.


## Limits

- One section, not 145 entries or 423 pages.
- Non-human review; no independent human sign-off.
- No `sufficient` promotion; validators still require a review record and policy change.
## Event Sourcing — pass-with-findings

Reviewer verdict: **pass-with-findings**. Two findings:

1. **Failure.** The card named replay duplication and schema drift but gave no recovery
action; the owner link anchored at §2 did not discuss either.
2. **Invariant.** §2 did not state the write-side conditional-append invariant, the
racing-command rejection path or retry double-append risk.

Remediation applied after the review:

- §2 now states the expected-version conditional append, re-read/reject on conflict and
  operation identity for retries.
- The Event Sourcing card now names the stale-version rejection, idempotent projectors and
  versioned handlers/rebuild plan.

## Event Sourcing re-review

Second read-only review returned **pass** with no findings. It verified the conditional
append, re-read/reject path, operation identity, card recovery actions, anchors and hashes.
The current verdict is **pass**.

Not re-reviewed again.
## Cache-Aside — pass-with-findings

Reviewer verdict: **pass-with-findings**. Two findings:

1. **Mechanism.** The section promised the read/write interleaving that breaks a naive
freshness promise but did not show the stale-fill race or define the version gate.
2. **Failure/recovery.** The card deferred to the owner section, which did not sequence
stale fills, concurrent misses or a failed/partial invalidation.

Remediation applied after the review:

- Added the stale-fill race (read V1, commit V2, refill V1), the version gate and its
  remaining check/write window.
- Added failed-invalidation retry/alert, TTL bound and single-flight recovery.
- Replaced the card's deferral with concrete gate/retry/single-flight actions.

Not re-reviewed. Verdict remains **pass-with-findings**.
## Negative Caching — pass-with-findings

Reviewer verdict: **pass-with-findings**. Two findings:

1. **Source.** The section made status/TTL and error-caching statements without a citation,
claim ID or ledger row; the card cited the Google CDN source.
2. **Mechanism.** The heading promised "evicted authorization" but did not define key scoping,
revocation invalidation or no-entry versus tombstone versus cached-negative.

Remediation applied after the review:

- Added tenant/principal/operation key scoping, delete-or-version on create/grant, tombstone
  distinction and a global-visibility restriction.
- Added the Google Cloud CDN negative-caching citation to the section, page source scope and
  chapter source ledger.
- Replaced the card's status/TTL deferral with scope, delete/version, TTL and revocation tests.

Not re-reviewed. Verdict remains **pass-with-findings**.
## Cache-Aside re-review — pass-with-findings

Second read-only review confirmed the stale-fill and recovery text is present, but found:

1. The claim that a race always remains is too strong; an atomic compare-and-set closes
   the check/write gap, as the sibling stale-fill owner states.
2. Recording invalidation only after a failed delete can lose the intent; the intent must
   be durable at commit time, and a missing TTL makes a lost invalidation unbounded.

Remediation: the section now distinguishes atomic and non-atomic fill, requires an outbox
intent in the same local transaction as the write, and states the no-TTL unbounded case.

Not re-reviewed again. Verdict remains **pass-with-findings**.
## Health Endpoint Monitoring — pass-with-findings

Reviewer verdict: **pass-with-findings**. Two findings:

1. No rule for absent/unknown probe data or probe-path independence; a monitoring outage
could look like health.
2. No statement of endpoint exposure, authorization or what the response discloses.

Remediation: added fail-open/fail-closed per dependency, independent probe path and missing-
data alerting; added caller authorization, disclosure and load-amplification limits. The card
now names missing health and bounded exposure.

Not re-reviewed. Verdict remains **pass-with-findings**.
## Negative Caching re-review

Second read-only review returned **pass** with no findings. It verified the Google CDN
citation and ledger row, tenant/principal/operation keying, delete-or-version on change,
tombstone distinction and the card recovery actions. The current verdict is **pass**.
