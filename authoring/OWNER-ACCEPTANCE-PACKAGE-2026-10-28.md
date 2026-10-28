# Owner acceptance package — nine additional sufficient entries

Status: **pending owner decision**. Three entries were accepted on 2026-10-27.
These nine have a fresh external `pass` and a promotion record, but are **not**
owner-accepted until the owner records a decision.

## Already accepted

1. Static Content Hosting
2. Transactional Outbox
3. Cache Invalidation

## Pending decision

| # | Entry | External report | Promotion |
|---|---|---|---|
| 1 | Valet Key | `authoring/ai-reviews/2026-10-27-valet-key-split-review6-codex.md` | yes |
| 2 | Anti-Corruption Layer | `authoring/ai-reviews/2026-10-27-anti-corruption-layer-split-review4-codex.md` | yes |
| 3 | Parallel Run | `authoring/ai-reviews/2026-10-27-parallel-run-split-review2-codex.md` | yes |
| 4 | Workload Identity / mTLS | `authoring/ai-reviews/2026-10-27-workload-identity-review5-codex.md` | yes |
| 5 | Sidecar | `authoring/ai-reviews/2026-10-27-sidecar-review5-codex.md` | yes |
| 6 | Dark Launching / Shadow Traffic | `authoring/ai-reviews/2026-10-27-dark-launching-review2-codex.md` | yes |
| 7 | Async Request-Reply | `authoring/ai-reviews/2026-10-27-async-request-reply-review3-codex.md` | yes |
| 8 | RBAC / ABAC | `authoring/ai-reviews/2026-10-28-rbac-abac-review-codex.md` | yes |
| 9 | Service Discovery | `authoring/ai-reviews/2026-10-28-service-discovery-review-codex.md` | yes |

## Evidence limits

- External review pass is not owner acceptance.
- No CI, deployment or human review is claimed.
- Promotion records bind the reviewed HEAD, owner/card hashes and report hash.
- A later page or card change requires a fresh review and a new acceptance record.

## Decision required

Record the accepted subset in `edition/patterns/sufficient-owner-acceptance.v1.json`,
or reject one or more entries with a reason. Until then `accepted_entries` remains
limited to the three entries accepted on 2026-10-27.
