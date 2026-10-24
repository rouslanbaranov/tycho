# Source-to-book audit - interim synthesis

**Status: interim, not final.** Issue #225 remains open. This document synthesizes
the evidence read so far and records the gaps explicitly; it does not claim
source-to-book completeness, independent review or acceptance.

Baseline: main `6754bac6e26faa57d65a301a60be10b3da93f65b`; 247 registered
sources, 406 canonical documents, 681 tracked files. No book, source-register,
index or edition file was changed.

## 1. Evidence base

- **Two books text-complete.** SRE: 48/48 public book units, including embedded
  images. OSTEP: chapters 1-57, appendices A-H and the preface, in 65
  continuation records (20,189 lines, 323,810 words, 803 pages plus the earlier
  chapter 2 record). OSTEP raster figures were not visually inspected.
- **96 reference records** in `readings.json`: 76 full reads, 1 partial, 17 blocked-full-text
  and 2 excluded-from-scope. All 45 baseline fetch-incomplete sources have a
  disposition: 29 read, 14 blocked, 2 excluded; none unaccounted.
- **44 assessed comparisons** in `comparisons.json` against 34 canonical pages:
  24 supported, 18 qualified, 2 not-addressed, 0 contradicted.
- **Page matrix:** all 406 pages have a recorded review status; 34 are
  comparison-assessed and 372 carry an explicit evidence gap
  (`page-review-summary.json`). A recorded gap is not a pass.

## 2. What the evidence supports

### Java execution, scheduling and release boundaries

- The virtual-thread page is correct that a carrier scheduler is not a
  backpressure mechanism (C001, supported). OSTEP's cache-affinity and queue
  discussion shows why runnable tasks do not create downstream capacity.
- JEP 491's canonical body is now read (R016). It supports the page's revised
  bounded claim and lets the historical "body not accessible" caveat be retired
  later, while the implementation-specific LM_LEGACY caveat remains (C017,
  supported; no edit under #225).
- JEP 444 adds a concrete release-boundary detail: interrupting a virtual thread
  blocked on socket I/O closes the socket. The cancellation page correctly says
  interruption is not rollback but does not state this side effect (C018,
  qualified; candidate addition only).
- First-party platform experience (R045) and the Zuul async retrospective (R046)
  both warn that virtual threads and async rewrites are not automatic capacity
  gains. The gRPC worker-pool regression and the CPU-bound API cluster that saw
  no efficiency gain are concrete counterexamples to a blanket "async is faster"
  claim. These are reference-level evidence, not yet separate page comparisons.

### Durability, replication and recovery

- Tycho's WAL page keeps acknowledgment, log commit and data durability as
  separate claims. OSTEP journaling supports that separation: a transaction-end
  commit and ordered data-before-commit are protocol conditions, not
  consequences of writing a log (C011, qualified).
- The Kafka acknowledgment page distinguishes replica and acknowledgment
  conditions. OSTEP reliable messaging explains lost acknowledgments and
  duplicate delivery; exactly-once is conditional, not automatic (C012,
  qualified).
- TAO (R036), Kafka tiers (R035) and memcache (R038) all show that a cache or
  replica tier adds visibility and completeness obligations. Kafka Audit's
  producer/consumer counts and TAO's single-primary eventual consistency are
  concrete mechanisms; they do not establish a general guarantee for Tycho's
  pages.

### Overload, backpressure and fairness

- R032 documents a shift from static quota rate limiting to in-flight
  concurrency, CoDel queues, per-tenant scorecards, write/partition/memory
  regulators and a priority-aware PID controller. Its reported gains are
  first-party operational figures, not a controlled benchmark.
- The strongest transferable claims are qualitative: a local quota cannot see
  remote overload; static timeouts can cause retry storms; concurrency is a
  better signal only when it maps to the constrained resource; and fairness
  needs a separate per-tenant mechanism. C019 finds the queueing page compatible
  with the concurrency signal, but the page correctly does not treat it as
  universal; the source names low-QPS large-write and hot-key exceptions.

- C021 (deadline/hedging vs R060) is supported: the page warns against
  independent retries at multiple layers and requires a bounded, capacity-aware
  retry owner; the source gives the same warning with the 3^5 amplification
  example.
- C022 (static stability vs R061) is supported: the page keeps the AWS account
  as a reported design approach and does not promise that every orchestrator
  shares its guarantees.
- C023 (hedging vs R065) is supported: the page states cancellation, bounded
  speculative work and the shared-bottleneck risk that the tail paper also
  emphasizes.
- C024 (Kafka Streams recovery vs R066) is qualified: the comparison table
  matches changelog restore and task migration, while the source adds standby
  replicas and rack-aware assignment not named in the table.
- C025 (Kafka ISR and acknowledgment vs R068) is supported: the page keeps ISR
  membership, acks and min.insync.replicas separate and bounds durability by a
  live ISR replica, matching the design document.
- C027 (filtering and recall vs R069) is supported: the page states that
  approximate indexes filter after the candidate scan and names iterative
  scans, partial indexes and partitioning as mitigations, matching the README.
- C026 (metric semantics vs R070) is supported: the page keeps point kinds,
  identity attributes, timestamps and temporality as separate conditions,
  matching the OpenTelemetry data model.
- C028 (messaging durability vs R071) is supported: the page separates broker
  acknowledgement from the consumer durable effect and treats dedup as a
  correctness boundary, matching the RabbitMQ reliability guide.
- C029 (token audience and sender constraints vs R072) is supported: the page
  separates token validity from audience and sender constraints and treats
  cross-resource reuse as a security failure, matching RFC 9700.
- C030 (measurement boundary vs R073) is qualified: the page keeps Little's Law
  to a mean identity and rejects tail prediction, while the source adds the
  finite-interval edge-effect bias and the need for a statistical estimator.
- C031 (client request key vs R077) is qualified: the page requires a scoped key,
  immutable parameters, atomic token/effect storage and expiry, matching the
  AWS account; the source does not define a universal API contract.
- C032 (pool fleet equation vs R078) is supported: the page separates client
  leases from server connections and names transaction-pooling state limits,
  matching the PgBouncer configuration reference.
- C033 (small saturated pool vs R079) is supported: the page keeps the pool
  formula as a starting point and refuses to equate configured size with
  throughput, matching the maintainer guidance.
- C034 (edge cache permission/freshness vs R075) is supported: the page keeps
  reuse permission, freshness and authorization separate, matching RFC 9111.
- C035 (GOAWAY boundary vs R076) is supported: the page distinguishes stream,
  attempt and operation identity and does not treat a missing response as
  rollback, matching RFC 9113.
- C036 (WAL durability vs R080) is supported: the page separates commit
  acknowledgment, WAL flush and data-page durability, matching PostgreSQL
  chapter 28's synchronous/asynchronous commit and checkpoint semantics.

### Migration, cutover and architecture evolution

- R037 (CDC ingestion), R028 (data-store migration), R033 (Bazel), R040 (cloud
  migration) and R039 (agent-assisted mobile migration) converge on a common
  shape: small reversible steps, shadow or dual operation, explicit equality
  checks, a rollback path and retirement of the old path only after evidence.
- These are first-party narratives. They support the general pattern but do not
  establish that any specific Tycho cutover gate is sufficient. C020 compares
  the cutover-gate table with the CDC migration and finds it compatible, while
  noting that reverse shadowing and checksum gates are not yet named in the
  table; this is a candidate enrichment, not a defect.
- Domain-oriented services (R024), modular-monolith evolution (R025, R031) and
  generated dependency enforcement show that boundaries are maintained by
  contracts, dependency analysis and ownership, not by directory layout or a
  deployment label.

### Security boundaries

- The security introduction and access-control sources support Tycho's
  separation of protected assets, principals, authentication and authorization
  (C013 and C014, supported). Authentication does not imply authorization, and
  a transport channel does not establish endpoint safety.

## 3. Candidate page actions

Only two candidate actions have direct page evidence:

1. **C017 - provenance update.** If the owner later edits the virtual-thread
   page, cite R016 and retire the "JEP 491 body not accessible" limitation while
   keeping the LM_LEGACY implementation-review caveat. No edit under #225.
2. **C018 - release-boundary addition.** If the owner later edits the
   cancellation page, name the socket-close side effect and its JDK/release
   boundary. No edit under #225.

All other assessments are "supported" or "qualified" with no correction. The two
"not-addressed" entries (scheduler queue topology in C003 and TLB coverage in
C008) are optional additions, not defects.

## 4. Contradictions and uncertainties

- **No contradicted comparison** has been recorded. This is not proof of
  correctness: only 14 pages have a bounded comparison.
- OSTEP version evidence is mixed: chapter 9, chapter 32 and the preface print
  version 1.20 while the site table of contents says 1.10. Records preserve the
  printed version and the discrepancy.
- R024 and R032 duplicate their article bodies in the retrieved representation.
  Unique text was read; duplicate blocks were verified by headings. R041 is a
  wiki page whose navigation chrome was excluded from the architecture claim.
- Fourteen blocked pages remain unread; no summary is inferred from a challenge
  page. Two internal team sites were excluded rather than accessed.
- No independent review was obtained. A Reviewer-preset child returned no report
  before the bounded stop; `human_review` is not-performed and `sufficient` is 0.

## 5. Coverage gaps

- **156 registered sources** are still at landing-or-abstract inspection. They
  are not full reads, even where their titles and URLs are registered.
- **372 of 406 canonical pages** have no page-level comparison. Their matrix
  status is an explicit gap, not an inferred pass.
- Linked publications, xv6 source, simulator code and exercises were not read or
  executed. Embedded raster figures were not visually inspected.
- The full external-link inventory beyond the register has not been reconciled
  to a finite reading unit for every citation.
- No experiments, production measurements or independent peer review were
  performed.

## 6. Acceptance checklist for #225

- [x] Baseline pinned; 681 tracked files match; no book change.
- [x] Two foundational books text-complete; all 45 baseline fetch-incomplete
  sources have an honest disposition.
- [x] Every full reference record has a finite unit, exact revision, access date,
  sections and omissions; blocked/excluded records do not claim content.
- [ ] Every accessible scoped source read completely: 156 landing-only sources
  remain, and 14 pages are blocked.
- [ ] All 406 pages have an applicability/review status beyond an explicit gap:
  19 assessed, 387 gaps.
- [ ] Material explanations have source comparisons across every technical page:
  24 comparisons exist; the applied case layer and most pages are unassessed.
- [ ] Complete external-link inventory and finite units for every citation.
- [x] Findings carry exact book anchors and source records for the 36 assessed
  comparisons; confidence and no-edit actions are recorded.
- [ ] Deep synthesis final: this is an interim synthesis.
- [x] Research artifacts reviewed for lexical boundary and whitespace; no
  independent-origin review beyond that.

## 7. Priorities for the next batch

1. Reconcile the 156 landing-or-abstract sources into finite units and read the
   highest-priority official documentation that Tycho cites repeatedly.
2. Extend page-level comparisons from 14 to the pages with the strongest
   material claims: crash consistency, replication, overload, migration gates,
   modularity and security boundaries.
3. Complete the external-link census and map each citation to a source ID or an
   explicit unresolved gap.
4. Re-run the Reviewer preset with a smaller, bounded batch; do not claim review
   until a report is returned and verified.
5. Write the final synthesis only after the page matrix and source inventory
   support it.

## Limits

This synthesis is based on public sources read through the recorded
representations. It does not reproduce source text, does not claim that a
first-party article is a benchmark, and does not claim that Tycho is complete or
correct. The 156 landing-only sources and 372 unassessed pages are the dominant
remaining uncertainty.
