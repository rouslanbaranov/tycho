# Batch remaining plan — 2026-10-28

Status: planning only. `sufficient` requires a saved external pass and promotion;
owner acceptance is separate. Current: 16 sufficient, 16 accepted; two c03 entries
are suspended pending fresh review of their split cards.

## Remaining by volume

| Volume | Entries | Sufficient | Remaining |
|---|---:|---:|---:|
| other | 6 | 0 | 6 |
| v02-application-boundaries-and-contracts | 17 | 1 | 16 |
| v03-execution-concurrency-and-flow-control | 1 | 1 | 0 |
| v04-distributed-coordination-and-events | 42 | 2 | 40 |
| v05-data-models-engines-and-lifecycle | 8 | 0 | 8 |
| v06-caching-indexing-and-retrieval | 13 | 1 | 12 |
| v07-performance-scale-and-resilience | 13 | 0 | 13 |
| v08-delivery-deployment-and-recovery | 27 | 4 | 23 |
| v09-observability-security-and-operations | 14 | 4 | 10 |
| v10-decision-support-and-modernization | 4 | 2 | 2 |

## Frozen pages

- c01 README — Sidecar promotion;
- c04 README — Transactional Outbox;
- c05 README — Cache Invalidation;
- c09 README — Static Content Hosting.

Shared owner pages with promotions also block edits; split or re-review before changing
the owner section.

## Candidate order

1. Message Filter — failure/recovery only; source supports discard, recovery needs rewrite.
2. Aggregator — alternative only; source names Scatter-Gather as a related pattern.
3. Scatter-Gather — alternative only; verify a direct alternative passage first.
4. Throttling — full client-side rewrite; regenerate packet, scope and B15-RESULT.
5. Ambassador — failure/recovery; card is on frozen c01.
6. Vertical Scaling — alternative; card is on frozen c09.

## Procedure per entry

1. Rewrite the four claims to admitted passages, not just bindings.
2. Align owner section and card.
3. Refresh derived artifacts; verify candidate threshold.
4. Run an exact-HEAD external review.
5. Promote only after pass; request owner acceptance separately.

## Limits

No entry is promised to pass. A source may support only a narrower claim than the
current card, requiring a page rewrite or a decision to keep it partial.

## c01 Ambassador blocker

c01 README now carries the Ambassador promotion. Self-Contained Service edits on
c01 invalidate that promotion until the Ambassador card is split onto its own page
and re-reviewed.

## Source gaps found

- **Message Filter** — the Filter page supports predicate routing, discard and a
  single output channel, but not the Content-Based Router alternative. A separate
  admitted Content-Based Router record is required before the alternative can be
  marked supported.
- **Aggregator / Scatter-Gather** — the pages list each other as related patterns,
  not as mutually exclusive alternatives; a new bounded source is required.
- **Throttling** — the client-side rewrite passed technical/decision checks, but
  packet, scope and B15-RESULT provenance must be regenerated in one commit before
  a fresh review.

## c03 split completed

Request-Reply Messaging and Message Filter now live on dedicated pages under c03.
Both promotions and the Request-Reply owner-acceptance entry are suspended, and both
entries are `partial-bounded`. Fresh reviews of the two new page/card hashes remain
pending. Remaining c03 cards can be edited without invalidating a promotion until a
new pass restores one.
