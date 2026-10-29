# Sufficient coverage queue — 2026-10-28

Status: working queue, not acceptance. `sufficient` requires a saved external pass
and a promotion record; owner acceptance is separate.

Current: **18 sufficient / 145**, **16 owner-accepted**, **2 suspended promotions**
(Request-Reply Messaging, Message Filter). Claim Check is review-ready but not promoted.
Pilot six: **all six sufficient**. Owner accepted 16 of the 18 current promotions on
2026-10-28; Splitter and Pipes and Filters await final acceptance.

## Sufficient and accepted

| Entry | External report | Owner accepted |
|---|---|---|
| Static Content Hosting | `2026-10-27-static-content-hosting-review6-codex.md` | yes |
| Transactional Outbox | `2026-10-27-transactional-outbox-review4-codex.md` | yes |
| Cache Invalidation | `2026-10-27-cache-invalidation-review-codex.md` | yes |

## Sufficient and owner-accepted (batch rows)

| Entry | External report | Owner accepted |
|---|---|---|
| Valet Key | `2026-10-27-valet-key-split-review6-codex.md` | yes |
| Anti-Corruption Layer | `2026-10-27-anti-corruption-layer-split-review4-codex.md` | yes |
| Parallel Run | `2026-10-27-parallel-run-split-review2-codex.md` | yes |
| Workload Identity / mTLS | `2026-10-27-workload-identity-review5-codex.md` | yes |
| Sidecar | `2026-10-27-sidecar-review5-codex.md` | yes |
| Dark Launching / Shadow Traffic | `2026-10-27-dark-launching-review2-codex.md` | yes |
| Async Request-Reply | `2026-10-27-async-request-reply-review3-codex.md` | yes |
| RBAC / ABAC | `2026-10-28-rbac-abac-review-codex.md` | yes |
| Service Discovery | `2026-10-28-service-discovery-review-codex.md` | yes |
| Controlled Cutover | `2026-10-28-controlled-cutover-review-codex.md` | yes |
| Federated Identity | `2026-10-28-federated-identity-review2-codex.md` | yes |
| Ambassador | `2026-10-28-ambassador-review-codex.md` | yes |

## Suspended promotions

The c03 cards moved to dedicated pages on 2026-10-28. Request-Reply Messaging was
suspended again on 2026-10-29 when the shared `workflow-failure.md` owner page changed
for Claim Check review remediation. Coverage is `partial-bounded`; neither entry is
promoted or counted as sufficient.

| Entry | Prior report | State |
|---|---|---|
| Request-Reply Messaging | `2026-10-28-request-reply-review4-codex.md` | suspended |
| Message Filter | `2026-10-28-message-filter-review-codex.md` | suspended |

Claim Check is not a suspended promotion: no promotion record exists. Its dedicated card
and owner section are review-ready with four source-bound dimensions and `partial-bounded`
coverage; a fresh external review is required before any promotion decision.

## Pilot six

| Entry | Status | Blocker |
|---|---|---|
| Parallel Run | sufficient | owner acceptance pending |
| Workload Identity | sufficient | owner acceptance pending |
| Dark Launching | sufficient | owner acceptance pending |
| RBAC/ABAC | sufficient | owner acceptance pending |
| Federated Identity | sufficient | owner acceptance pending |
| Controlled Cutover | sufficient | owner acceptance pending |

## Frozen by page-bound promotion

- c01 README — Sidecar promotion;
- c02 README — Async card moved to its own page, promotion restored;
- c05 README — Cache Invalidation promotion;
- c09 README — Static Content Hosting promotion;
- c10 README — Dark card moved to its own page, promotion restored;
- c04 README — Transactional Outbox promotion;
- c03 README — no active card-page promotion; Claim Check card is on its own page;
  Request-Reply Messaging and Message Filter suspensions are tracked above.

Editing these pages requires a split and fresh review before promotion can remain valid.

## Shared-page blockers

- **Federated Identity** — owner page `identity-authorization-and-isolation.md`
  also carries the Workload Identity promotion. Editing it invalidates Workload;
  split the page and re-review both before Federated work.
- **Controlled Cutover** — atlas card is on the c10 page with the Dark Launching
  promotion. Split c10 before editing the card.
- **Service Discovery / Load Balancing** — cards are on c02/c09 pages with Async
  and Static Content Hosting promotions.
- **TTL-based Expiration** — card is on the c05 page with Cache Invalidation.
