> **Dated inventory — 2026-10-29.** The “17 owner-accepted” reference is
> historical; the owner-accepted file currently lists **7** entries. Current
> promotion state is in [the 2026-10-31 hand-off](HANDOFF-2026-10-31.md).

# Frozen split inventory — 2026-10-29

Status: planning only. Read-only inventory at HEAD
`3951a862515f8f7b3f8a88caef916319cfb0cc3a`. No book or edition artifact, promotion,
acceptance record or test was changed. Hashes are SHA-256 prefixes of the files at that
HEAD; each prefix matched the bound value in
`edition/patterns/sufficient-promotions.v1.json`.

## Scope and mapping assumption

The request names `c04 application boundaries`, `c05 delivery/deployment` and
`c09 security/operations`. At this HEAD those labels do not match the V11 codes:
C04 is data consistency and events, C05 is caching and retrieval, and C09 is
scalability and load distribution. Application boundaries is C01, delivery/deployment
is C10, and security/operations is C11.

To avoid missing a promotion-bound file, this inventory covers both readings:

- literal C04, C05 and C09 shared card pages;
- the C01, C10 and C11 domain clusters;
- a residual list of the other promotion-bound shared files.

Path shorthand: `vNN/cMM/file.md` means the single `cMM-*` directory under
`book/volumes/vNN-*/`; `v11/cNN/file.md` means the V11 chapter directory.
Card hashes bind the whole card file. Owner hashes bind the whole technical page, not
only the named section. Full 64-character values and review report paths remain in
`edition/patterns/sufficient-promotions.v1.json`; the prefixes below match that record.

## Binding rules used here

1. A promotion binds `owner_page_sha256` and `card_sha256`; changing either file
   suspends the promotion until a fresh external review passes.
2. Splitting a card also edits its reciprocal owner backlink, so both hashes change
   even when the owner section itself does not move.
3. Moving a promoted owner section off a shared page changes that page for every other
   promotion on it; all affected entries must be re-reviewed in the same batch.
4. Suspend a promotion, never delete its report. Restore only with a new review at the
   new HEAD and the new pair of hashes.
5. Prefer moving the promoted section. Move a candidate section only when that is
   strictly smaller and the affected promotions are re-reviewed anyway.

## Inventory summary

| Group | Promotions | Shared card page | Shared owner pages | Candidates |
|---|---:|---|---|---:|
| C04 literal | 1 | C04 README | 1 | 14 |
| C05 literal | 1 | C05 README | 1 (solitary) | 13 |
| C09 literal | 1 | C09 README | 1 | 10 |
| C01 boundaries | 4 | C01 README | 2 (1 solitary) | 9 |
| C10 deployment | 3 | C10 README | 3 (1 solitary) | 13 |
| C11 security | 4 | none | 4 (2 solitary) | 2 |

The six groups cover 14 of 21 current promotions. They touch 55 distinct candidate
entries after cross-group de-duplication. Candidate statuses below are from
`sufficient-ready-plan.v1.json`; almost all are `rejected-technical-support`, so a
split removes a file lock but does not make an entry review-ready.

## C04 — consistency and events (literal c04)

Promoted:
- **Transactional Outbox** — card `v11/c04/README.md` (`01bc33fe…`);
  owner `v04/c05/outbox-inbox-sagas-and-durable-workflows.md`
  (`02ae83f4…`).

Remaining candidates on the card page (13): CQRS, Event Sourcing, Domain Events,
Saga, Saga Choreography, Saga Orchestration, Compensating Transaction,
Transactional Inbox, Idempotency Key, CDC, Materialized View, Command-Side Replica,
2PC. Owner-page candidate (1): Distributed Workflow Orchestration.

Smallest batch (2 moves): move card lines 314–347 to
`v11/c04/transactional-outbox.md`; move owner lines 129–143 to
`v04/c05/transactional-outbox.md`; update both backlinks. Suspends one promotion;
frees 13 card candidates and Distributed Workflow Orchestration. Moving 13 cards or
the single candidate section would be larger or equal and would still invalidate the
same owner hash.

## C05 — caching and retrieval (literal c05)

Promoted:
- **Cache Invalidation** — card `v11/c05/README.md` (`ac95570b…`);
  owner `v06/c02/cache-invalidation-stampede-and-hot-keys.md`
  (`ba797acd…`). The owner page has no other pattern section.

Remaining candidates on the card page (13): Distributed Cache, Cache-Aside,
Read-Through, Write-Through, Write-Behind, Write-Around, TTL-Based Expiration,
Negative Caching, Cache Stampede Protection, Single Flight, Stale-While-Revalidate,
Multi-Level Caching, CDN / Edge Caching. TTL is in `remediation`; the rest are
`rejected-technical-support`.

Smallest batch (1 move): move card lines 272–304 to
`v11/c05/cache-invalidation.md`; update the owner backlink only. Suspends one
promotion; frees 13 cards. CDN / Edge Caching remains owner-blocked by C09 (below),
not by this page.

## C09 — scalability and load distribution (literal c09)

Promoted:
- **Static Content Hosting** — card `v11/c09/README.md` (`4bcf5ea4…`);
  owner `v08/c08/edge-cache-origin.md` (`70762b2e…`).

Remaining candidates on the card page (9): Load Balancing, Horizontal Scaling,
Vertical Scaling, Autoscaling, Cell-Based Architecture, Shuffle Sharding,
Deployment Stamps, Geode, Tenant-Based Resource Isolation. Owner-page candidate (1):
CDN / Edge Caching. Load Balancing is separately owner-blocked by Service Discovery
(C02 residual); CDN is freed by this batch.

Smallest batch (2 moves): move card lines 334–365 to
`v11/c09/static-content-hosting.md`; move owner lines 147–165 to
`v08/c08/static-content-hosting.md`; update both backlinks. Suspends one promotion;
frees 9 cards and CDN / Edge Caching.

## C01 — application boundaries

Promoted:
- **Self-Contained Service** — card `v11/c01/README.md` (`3eeeee79…`);
  owner `v02/c04/service-independence.md` (`f343e82b…`); owner section is solitary.
- **Sidecar** — card `v11/c01/sidecar.md` (`d2169cf7…`);
  owner `v08/c03/static-stability.md` (`d16d4de3…`).
- **Ambassador** — card `v11/c01/ambassador.md` (`e424421b…`);
  same owner page and hash as Sidecar.
- **Anti-Corruption Layer** — card `v11/c01/anti-corruption-layer.md`
  (`3d717950…`); owner `v02/c06/anti-corruption-adapters-and-coexistence.md`
  (`cc614532…`); both files are already isolated, so no move is needed.

Remaining candidates on the C01 card page (8): Modular Monolith, Hexagonal
Architecture, DDD Bounded Context, Layered Architecture, Microservices, SOA,
Clean / Onion Architecture, Database per Service. Owner-page candidate (1):
Immutable Infrastructure on `static-stability.md`.

Smallest batch (2 moves): move the Self-Contained Service card lines 384–412 to
`v11/c01/self-contained-service.md`; move Immutable Infrastructure lines 175–190
from `v08/c03/static-stability.md` to
`v08/c03/immutable-infrastructure.md`. Suspends three promotions: Self-Contained
Service (card), Sidecar and Ambassador (owner page changed). Frees 8 cards and
Immutable Infrastructure. Moving the one candidate section is smaller than moving
both promoted owner sections (two moves), and those two promotions need a fresh
review either way.

## C10 — delivery and deployment modernization

Promoted:
- **Controlled Cutover** — card `v11/c10/README.md` (`ab44d301…`);
  owner `v10/c05/cutover-gates.md` (`6342da62…`).
- **Dark Launching / Shadow Traffic** — card `v11/c10/dark-launching.md`
  (`c6fe7809…`); owner `v08/c04/gitops-canary-and-progressive-rollout.md`
  (`e8600ac3…`).
- **Parallel Run** — card `v11/c10/parallel-run.md` (`f1e0a750…`);
  owner `v10/c05/authority-states.md` (`36cef2f3…`); both files are already
  isolated, so no move is needed.

Remaining candidates on the C10 card page (9): Rolling Deployment, Blue/Green,
Canary Release, Feature Flags, GitOps, Immutable Infrastructure, Strangler Fig,
Branch by Abstraction, Expand-and-Contract. Owner-page candidates (4): Branch by
Abstraction on `cutover-gates.md`; Rolling, Blue/Green and Canary on
`gitops-canary-and-progressive-rollout.md`.

Smallest batch (3 moves): move Controlled Cutover card lines 374–404 to
`v11/c10/controlled-cutover.md`; move Controlled Cutover owner lines 131–140 to
`v10/c05/controlled-cutover.md`; move Dark Launching owner lines 111–135 to
`v08/c04/dark-launching-shadow-traffic.md`. Suspends two promotions: Controlled
Cutover (card and owner) and Dark Launching (owner only); Parallel Run is untouched.
Frees 9 cards and four owner candidates. Requires C01 first only for the Immutable
Infrastructure candidate; the other moves are independent.

## C11 — security, isolation and operations

Promoted:
- **Valet Key** — card `v11/c11/valet-key.md` (`08079939…`);
  owner `v09/c05/object-credentials.md` (`ced47a04…`); solitary owner section.
- **RBAC / ABAC** — card `v11/c11/rbac-abac.md` (`d61f241d…`);
  owner `v09/c05/authorization-policy-and-least-privilege.md` (`4e506116…`).
- **Workload Identity / mTLS** — card `v11/c11/workload-identity-mtls.md`
  (`41a07159…`); owner `v09/c05/identity-authorization-and-isolation.md`
  (`88c86973…`).
- **Federated Identity** — card `v11/c11/federated-identity.md`
  (`641c819f…`); same owner page and hash as Workload Identity.

Remaining candidates on the C11 card page: none; every card is already dedicated.
Owner-page candidates (2): Zero Trust Architecture and Least Privilege on the
authorization page. The identity page has two promotions but no other candidate.

Smallest batch (1 move): move RBAC/ABAC owner lines 107–128 to
`v09/c05/rbac-abac.md`; card unchanged. Suspends one promotion; frees Zero Trust
and Least Privilege. Separately, if independent work on Federated Identity or
Workload Identity is needed, split both owner sections (lines 93–102 and 103–125)
in a later decoupling batch; that batch frees no remaining candidate.

## Per-batch procedure

1. Record the pre-split hashes and suspend only the promotions the move invalidates;
   keep the reports.
2. Move the section verbatim, add the standard frontmatter to the new page, and update
   the reciprocal card and owner links.
3. Update `card_path` or the owner path in the metadata, then run
   `python3 scripts/refresh_atlas_artifacts.py --authorize \"...\"` for the mechanical
   revisions.
4. Run the structural validators for atlas, cards, owner units, coverage and promotions;
   record the exact post-split HEAD.
5. Obtain one fresh external review per suspended entry at that HEAD.
6. On a pass, rebind the new owner and card hashes and restore coverage; on a failure,
   keep the entry `partial-bounded` and record the finding.

## Ordered batches

| Batch | Group | Moves | Promotions suspended | Depends on |
|---|---|---|---:|---|
| B1 | C05 card | 1 card | Cache Invalidation | none |
| B2 | C04 card + owner | 1 card, 1 owner | Transactional Outbox | none |
| B3 | C09 card + owner | 1 card, 1 owner | Static Content Hosting | none |
| B4 | C01 card + owner | 1 card, 1 owner | Self-Contained, Sidecar, Ambassador | none |
| B5 | C10 card + owner | 1 card, 2 owners | Controlled Cutover, Dark Launching | B4 for Immutable |
| B6 | C11 owner | 1 owner | RBAC/ABAC | none |

B1 is first because it is one card move, one promotion and no owner-section move.
B3 also releases the CDN owner candidate that B1's card split cannot free. B4 must
precede work on Immutable Infrastructure, which is also a C10 card candidate.

## Review and acceptance needs

- Every suspended promotion needs a fresh external AI review at the exact post-split
  HEAD, with the new owner and card hashes, a byte-level check that the moved section
  is unchanged, and a pass on all four dimensions. Do not reuse a report.
- Use a different vendor/harness, or a fresh read-only DeepSeek Reviewer when none is
  available; one bounded batch per run; no tests for the reviewer. Save each report
  under `authoring/ai-reviews/`, add its SHA-256 to the index, and update the
  promotion record only after the pass.
- B4 reviews three entries (Self-Contained Service, Sidecar, Ambassador); B5 reviews
  two (Controlled Cutover, Dark Launching); B1, B2, B3 and B6 review one each.
  Parallel Run, Valet Key, Workload Identity, Federated Identity and Anti-Corruption
  Layer are not suspended by these batches.
- All in-scope promotions are among the 17 owner-accepted entries. A page change
  invalidates the accepted hashes; record one owner re-decision after B1–B6, not one
  per batch. Do not treat the old acceptance as covering the new hashes.
- Run targeted validators during a split and the full suite once at the end of the
  batch, per AGENTS.md. No test was run for this inventory.

## Inventory corrections and residual debt

The older frozen-page plan is stale in three places: C01 now binds Self-Contained
Service (not Sidecar), C02 still binds Service Discovery on its README, and C10 still
binds Controlled Cutover on its README. The C02 and C03 owner pages below remain
promotion-bound and are not covered by B1–B6:

- **C02 Service Discovery** — card `v11/c02/README.md` (`3af8fa5f…`), 10 other
  cards; owner `v08/c08/discovery-balancing.md` (`fb1051c3…`) with Client-Side,
  Server-Side Discovery and Load Balancing. Smallest batch: 1 card + 1 owner.
- **C03 messaging owners** — cards are dedicated, but three owner pages bind five
  promotions: `message-selection.md` (Resequencer, Pipes and Filters; 9 candidates),
  `workflow-failure.md` (Claim Check, Request-Reply Messaging; 2 candidates), and
  `messaging-families-and-durable-workflows.md` (Splitter; 2 candidates).
- **Solitary promotion-bound owner pages** — Async Request-Reply, Anti-Corruption
  Layer, Parallel Run, Valet Key, Self-Contained Service and Cache Invalidation have
  no other pattern section; no split is needed to free a candidate there.
- **Promotion-coupling only** — the identity page holds Workload Identity and
  Federated Identity with no candidate section. It blocks independent edits to those
  two promotions, not a remaining candidate.

## Limits

This inventory derives counts and hashes from committed artifacts; it does not prove
the moved sections are correct or that any review will pass. It does not change the
book, edition, registry, promotions or acceptance records, and it does not authorize
a promotion. Recompute all hashes if HEAD moves before a batch starts.
