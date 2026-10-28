# Owner acceptance record — 15 sufficient entries

Status: **14 accepted; Federated Identity pending owner decision**.
All fifteen have a fresh external `pass` and a promotion record.

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
| 10 | Controlled Cutover | `authoring/ai-reviews/2026-10-28-controlled-cutover-review-codex.md` | yes |
| 11 | Request-Reply Messaging | `authoring/ai-reviews/2026-10-28-request-reply-messaging-review-codex.md` | yes |
| 12 | Federated Identity | `authoring/ai-reviews/2026-10-28-federated-identity-review2-codex.md` | no |

## Evidence limits

- External review pass is not owner acceptance.
- No CI, deployment or human review is claimed.
- Promotion records bind the reviewed HEAD, owner/card hashes and report hash.
- A later page or card change requires a fresh review and a new acceptance record.

## Decision required

Record the accepted subset in `edition/patterns/sufficient-owner-acceptance.v1.json`,
or reject one or more entries with a reason. Until then `accepted_entries` remains
limited to the three entries accepted on 2026-10-27.

## Recorded decision

The owner recorded this payload in
`edition/patterns/sufficient-owner-acceptance.v1.json`:

```json
{
  "status": "accepted",
  "owner": "Ruslan Baranov",
  "accepted_at": "YYYY-MM-DD",
  "accepted_entries": [
    "tycho.pattern.static-content-hosting",
    "tycho.pattern.transactional-outbox",
    "tycho.pattern.cache-invalidation",
    "tycho.pattern.valet-key",
    "tycho.pattern.anti-corruption-layer",
    "tycho.pattern.parallel-run",
    "tycho.pattern.workload-identity-mtls",
    "tycho.pattern.sidecar",
    "tycho.pattern.dark-launching-shadow-traffic",
    "tycho.pattern.asynchronous-request-reply",
    "tycho.pattern.rbac-abac",
    "tycho.pattern.service-discovery",
    "tycho.pattern.controlled-cutover"
  ]
}
```

The recorded decision accepts all fourteen entries.

## Federated Identity decision

Federated Identity passed external review and promotion after the shared-page rewrite.
It is not yet in `accepted_entries`. To accept it, add this ID and report to the
existing acceptance record:

```json
{
  "accepted_entry": "tycho.pattern.federated-identity",
  "review_report": "authoring/ai-reviews/2026-10-28-federated-identity-review2-codex.md"
}
```

Until then the owner acceptance count remains 14 of 15 sufficient entries.
