# Sufficient coverage queue — 2026-10-28

Status: working queue, not acceptance. `sufficient` requires a saved external pass
and a promotion record; owner acceptance is separate.

Current: **15 sufficient / 145**, **14 owner-accepted**, **1 pending owner decision**.
Pilot six: **all six sufficient**.
Owner accepted 14 entries on 2026-10-28; Federated Identity awaits a new owner decision.

## Sufficient and accepted

| Entry | External report | Owner accepted |
|---|---|---|
| Static Content Hosting | `2026-10-27-static-content-hosting-review6-codex.md` | yes |
| Transactional Outbox | `2026-10-27-transactional-outbox-review4-codex.md` | yes |
| Cache Invalidation | `2026-10-27-cache-invalidation-review-codex.md` | yes |

## Sufficient, pending owner acceptance

| Entry | External report | Owner accepted |
|---|---|---|
| Valet Key | `2026-10-27-valet-key-split-review6-codex.md` | no |
| Anti-Corruption Layer | `2026-10-27-anti-corruption-layer-split-review4-codex.md` | no |
| Parallel Run | `2026-10-27-parallel-run-split-review2-codex.md` | no |
| Workload Identity / mTLS | `2026-10-27-workload-identity-review5-codex.md` | no |
| Sidecar | `2026-10-27-sidecar-review5-codex.md` | no |
| Dark Launching / Shadow Traffic | `2026-10-27-dark-launching-review2-codex.md` | no |
| Async Request-Reply | `2026-10-27-async-request-reply-review3-codex.md` | no |
| RBAC / ABAC | `2026-10-28-rbac-abac-review-codex.md` | no |
| Service Discovery | `2026-10-28-service-discovery-review-codex.md` | no |
| Controlled Cutover | `2026-10-28-controlled-cutover-review-codex.md` | no |
| Request-Reply Messaging | `2026-10-28-request-reply-messaging-review-codex.md` | no |
| Federated Identity | `2026-10-28-federated-identity-review2-codex.md` | no |

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
- c04 README — Transactional Outbox promotion.

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
