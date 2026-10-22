# Independent-agent review batch — 2026-10-22

Read-only independent-agent reviews of dedicated sufficient-coverage candidates.
These are non-human reviews; they are not human per-page review and do not establish
owner acceptance or sufficient coverage.

### Layered Architecture

Verdict: **pass-with-findings**. Findings: 2.

- Card names transaction boundaries across layers and anemic models as failures, but the anchored 123-word section covers only dependency bypass, cycles and pass-through.
- Card's claim that the linked owner section states the remaining limits is not met.

### Modular Monolith

Verdict: **pass-with-findings**. Findings: 2.

- The 120-word unit repeats the dependency-test sentence verbatim and leaves local-transaction value and event durability outside the anchored unit.
- Card good-fit and recovery conditions point outside the unit.

### Microservices Architecture

Verdict: **pass-with-findings**. Findings: 2.

- Card requires timeouts, idempotency and observability for recovery, but the anchored unit names only contract, failure budget and local transaction boundary.
- The cited source does not support the card's idempotency recovery claim.

### Service-Oriented Architecture (SOA)

Verdict: **reject**. Findings: 2.

- SOA unit duplicates three of seven sentences in the adjacent Microservices unit and applies independent-deployment language to SOA.
- Card's distinctive mediation, governance-overhead, bus-bottleneck and observability claims are absent; the linked section does not support them.

### Hexagonal Architecture / Ports and Adapters

Verdict: **pass-with-findings**. Findings: 2.

- Dedicated section states a reservation-consistency invariant, not the defining dependency invariant that domain code must not depend on adapter/technology types.
- Card's mapping-layer latency claim is not covered.

### Domain-Driven Design / Bounded Context

Verdict: **pass-with-findings**. Findings: 2.

- No limit on translation or boundary-maintenance cost, although the card's reversal depends on it.
- Card's domain-expert validation condition and hard contraindication are absent.

### Database per Service

Verdict: **pass-with-findings**. Findings: 2.

- Card's one-team-owns-all-services contraindication overgeneralizes the owner's shared-database condition.
- Card's dual-write, stale-replica and outbox/idempotency recovery material is not covered.

### Self-Contained Service

Verdict: **pass-with-findings**. Findings: 2.

- Card's data duplication, staleness and reconciliation conditions are absent from the dedicated section.
- Card annotation says the section owns local-transaction alternatives, but it does not discuss local transactions.

### Sidecar

Verdict: **pass-with-findings**. Findings: 2.

- Card owner label says Service mesh and traffic intermediaries while targeting #sidecar.
- Card says independent lifecycle is useful, while owner section requires lifecycle coupled to the instance; contradiction needs stating.

### Ambassador

Verdict: **pass-with-findings**. Findings: 2.

- Owner section names a shared ingress gateway as alternative while card lists a sidecar for per-client egress; mechanisms are not coherent.
- Owner text is ungrammatical and the card owner label misnames #ambassador.

### Anti-Corruption Layer

Verdict: **pass-with-findings**. Findings: 2.

- Owner section reuses R7 without definition and repeats the ACTIVE/AVAILABLE scenario without its synthetic label.
- Section duplicates the walkthrough, adds no contract tests/versioned mappings, and one line exceeds 100 characters.

### Gateway Routing

Verdict: **pass-with-findings**. Findings: 2.

- Bounded section is near-verbatim duplication of the earlier routing-contract paragraph.
- Card failure/recovery cites wrong-version selection, no-match, route versioning and precedence tests that the linked section does not cover.

### Service Discovery

Verdict: **pass-with-findings**. Findings: 2.

- Card claims the owner covers discovery outage, last-known-good recovery and fast-error attraction; the section does not.
- Section duplicates sibling client/server text and leaves distinct discovery recovery underdeveloped.

### Client-Side Discovery

Verdict: **pass-with-findings**. Findings: 2.

- Card still says client-specific policy is not a dedicated section, although one exists.
- Card names registry outage, divergent policies and retry storms; owner section gives no last-known set, retry bound or divergence control.

### Server-Side Discovery

Verdict: **pass-with-findings**. Findings: 2.

- Card still says server-side specifics are not a dedicated section, although one exists.
- Card names proxy outage, retry amplification and bottleneck; owner section specifies no recovery, health-check or backoff.

### Asynchronous Request-Reply

Verdict: **pass-with-findings**. Findings: 2.

- Card hard contraindication when the operation is not idempotent is overbroad; the durable handle/reconcile rule targets non-idempotent work.
- Card names duplicate submissions and orphaned jobs; owner section covers only lost/expired replies.

### Event-Driven Consumer

Verdict: **pass-with-findings**. Findings: 2.

- Card requires backpressure and acknowledgement; owner section gives no prefetch/in-flight bound, flow-control rule or overload action.
- Owner polling rationale does not match the card's polling/scheduled-batch alternative and volume reversal.

### Request-Reply Messaging

Verdict: **pass-with-findings**. Findings: 2.

- Card requires a durable reply path; owner mentions reply address and cost but not reply-queue durability, ownership or cleanup.
- Invariant is one reply per request, but duplicate/late replies after deadline have no detection or disposition.

### Correlation Identifier

Verdict: **pass-with-findings**. Findings: 2.

- Card rejects identifiers reused across operations, but owner states only generation rule and collision check, not operation-scoped uniqueness.
- No recovery for ambiguous matching or identifier expiry.

### Content-Based Router

Verdict: **pass-with-findings**. Findings: 2.

- Card rejects routing on untrusted fields; owner section never requires validating or trusting predicate fields.
- Card's workflow/orchestrator alternative and hidden-process-engine warning are omitted.

### Message Filter

Verdict: **pass-with-findings**. Findings: 2.

- Rejected-message disposition is unresolved: discard, fallback, dead-letter or audit and retention ownership are not specified.
- Card owner link is labelled Requirement-driven comparison, not a ranking, while targeting #message-filter.

### Pipes and Filters

Verdict: **pass-with-findings**. Findings: 2.

- Stage contract is under-specified: ordering scope, intermediate observability and stage-level effect identity/dedup are missing.
- Card owner link is mislabeled as Requirement-driven comparison.

### Splitter

Verdict: **pass-with-findings**. Findings: 2.

- Invariant conflates part identity with stable partition identity and omits parent correlation, expected part set and completion condition.
- Card ordering contraindication requires a coordinator, but owner section assigns no coordinator, sequence or reconstruction rule.

### Aggregator

Verdict: **pass-with-findings**. Findings: 2.

- No completion rule: expected set, declared count, quorum or timeout-as-final is not defined.
- Aggregation-state durability, restart recovery, eviction and timeout cleanup are missing.

### Gatekeeper

Verdict: **pass-with-findings**. Findings: 2.

- Owner note/card omit limited-privilege/no-credential isolation, so the trust separation that justifies the extra hop is missing.
- Card says gatekeeper mechanics are not a dedicated section, while owner-units records a dedicated unit; clarify bounded note vs deep section.

### Publish/Subscribe

Verdict: **pass-with-findings**. Findings: 2.

- Card hard contraindication when broker cannot express retention rejects ephemeral pub/sub, which the owner explicitly allows when signal loss is acceptable.
- Competing-alternative reversal is ambiguous; restate one work item/one consumer rather than every subscriber needing the work.

### Point-to-Point Queue

Verdict: **pass**. Findings: 0.


### Competing Consumers

Verdict: **pass**. Findings: 0.


### Gateway Aggregation

Verdict: **pass-with-findings**. Findings: 2.

- Card alternative includes API Composition, but owner section names only client-side composition or a BFF and does not draw the boundary.
- Section covers read-style partial failure only; omits read-mostly fit, hidden domain workflow contraindication and retry amplification.

### Gateway Offloading

Verdict: **pass-with-findings**. Findings: 2.

- No inclusion boundary that the function is shared/cross-cutting and edge-enforceable; no contraindication for domain-state functions or edge outage blocking every backend.
- L127 is 141 characters, over the 100-character limit.

### Backend for Frontend (BFF)

Verdict: **pass-with-findings**. Findings: 2.

- Section does not cover multi-BFF shape: duplicated logic, cross-BFF drift, shared domain contracts and per-BFF observability.
- Card says BFF tailoring is not a dedicated section, but a dedicated section exists; clarify the owner description.

### Reverse Proxy

Verdict: **pass-with-findings**. Findings: 2.

- Card's connection management, health checks, draining and stale-connection requirements are absent from the owner section.
- Recovery test covers outage/stale route/header stripping, not connection lifecycle and draining policy.

### Scatter-Gather

Verdict: **pass-with-findings**. Findings: 2.

- No correlation key or one-reply-per-recipient matching; late, duplicate or misrouted replies have no attribution or exclusion rule.
- Card's per-recipient deadlines and caller-exhaustion contraindication are unsupported; no concurrency or caller-capacity bound.

### Dead Letter Channel / DLQ

Verdict: **pass-with-findings**. Findings: 2.

- Replay procedure does not require effect-identity preservation, reauthorization or an already-committed-effect check.
- No quarantine retention horizon, capacity limit, access policy or cleanup.

### Durable Subscriber

Verdict: **pass-with-findings**. Findings: 2.

- At-least-once redelivery is stated without an effect key or dedup rule; a resumed subscription can double-apply local effects.
- Card's late-replay deadline contraindication is absent; no stale-replay detection or deadline test.

### Idempotent Receiver

Verdict: **pass-with-findings**. Findings: 2.

- Key derivation/validation and collision disposition are unspecified.
- No marker lifetime, cleanup owner or post-expiry reject/reconcile behavior.

### Resequencer

Verdict: **pass-with-findings**. Findings: 2.

- Late-message disposition after release and action at buffer capacity are undefined.
- Card owner label still says Requirement-driven comparison; alternative/reversal differ from the note.

### Claim Check

Verdict: **pass-with-findings**. Findings: 2.

- Token-to-payload binding/stability and retrieval-latency bound are not defined.
- Card owner link is mislabeled as a durable workflow/request-reply contract.

### Message Broker / Messaging Bridge

Verdict: **pass-with-findings**. Findings: 2.

- Note reuses earlier prose including a dangling sentence; no broker outage failure; invariant concerns publisher confirms, not broker behavior.
- Card owner description still says consumer ownership and omits single-point, semantic-loss and observability limits.

### Canonical Data Model

Verdict: **pass-with-findings**. Findings: 1.

- Card owner label still says Requirement-driven comparison and calls the comparison section bounded, while #canonical-data-model is a dedicated note.

### Process Manager / Routing Slip

Verdict: **pass-with-findings**. Findings: 2.

- Card narrows a two-variant entry to a durable coordinator and routes slip gets one sentence without failure/recovery; owner link also mislabeled.
- Invariant overclaims crash safety; recorded dispatch intent is the missing condition.

### Command Query Responsibility Segregation (CQRS)

Verdict: **pass-with-findings**. Findings: 2.

- Anchored note largely restates earlier CQRS/Materialized View text; little distinct ownership.
- Card read-after-write hard contraindication over-rejects; atomic view/cursor recovery absent.

### Domain Events

Verdict: **pass-with-findings**. Findings: 2.

- Dedicated note repeats earlier domain-event/failure/alternative paragraphs nearly verbatim; three sentences match.
- Card alternative (synchronous call/command) and owner alternative (state transfer/polling/CDC) describe different choices.

### Saga

Verdict: **pass-with-findings**. Findings: 2.

- Dedicated note is near-verbatim duplicate of earlier Saga paragraphs; three sentences match and cost-based reversal is dropped.
- Alternative bundles 2PC and orchestration; orchestration is a coordination style, not an alternative, and reversal condition is muddled.

### Saga Choreography

Verdict: **pass-with-findings**. Findings: 2.

- Card requires stable event contracts and timeout policy; owner unit omits timeout, contract-stability and central-ordering rules; four of seven sentences repeat §4.
- Card owner annotation misdescribes event-driven choreography as compensation/branching.

### Saga Orchestration

Verdict: **pass-with-findings**. Findings: 2.

- Card includes compensation, participant autonomy and bottleneck/SPOF reversal; anchored unit does not discuss them.
- Unit repeats §5 mechanism/failure/alternative nearly verbatim; cited Temporal record does not support the prevalence claims.

### Compensating Transaction

Verdict: **pass-with-findings**. Findings: 2.

- Card requires compensation ordering and cost/risk reversal; unit states neither.
- Unit repeats §4 mechanism/examples/alternative; does not explain ordering or how counter-effect is proven.

### Transactional Outbox

Verdict: **pass-with-findings**. Findings: 2.

- Reversal condition is inverted: reverse to direct publish when relay complexity exceeds risk, not when risk exceeds complexity.
- Card recovery requires bounded attempts/age and retained repair evidence; unit omits them and repeats §0 sentences.

### Distributed Cache

Verdict: **pass-with-findings**. Findings: 2.

- Note condenses earlier walkthrough; five sentences repeat lines 91-101, adding no distinct mechanism.
- Card requires partitioning/replication and stale-replica behavior; section only calls it a shared dependency and omits topology.

### Read-Through Cache

Verdict: **pass-with-findings**. Findings: 2.

- No version/invalidation rule for a fill that reads old data and races a concurrent write.
- Underspecified authentication versus caller-specific authorization, so the card's per-read authorization contraindication lacks owner support.

### Write-Through Cache

Verdict: **pass-with-findings**. Findings: 2.

- No ordering rule between cache and authoritative store, and no statement of what a read sees between the two updates.
- Card failure/recovery says to verify ordering in the owner section, which is order-agnostic.

### Write-Behind / Write-Back

Verdict: **pass-with-findings**. Findings: 2.

- Durability contract is self-contradictory: pending buffer must survive, yet cache loss may discard acknowledged writes and a loss window is acceptable.
- Conflates losing the cache with losing the pending buffer; card contraindication and owner loss-window recommendation conflict.

### Idempotency Key

Verdict: **pass-with-findings**. Findings: 2.

- Page evidence scope lists only RFC 9110 (HTTP semantics), not the card's application-level key source.
- Unit repeats integrated-decision sentences; card's atomic outcome record and server-generated identity alternative are absent.

### Change Data Capture (CDC)

Verdict: **reject**. Findings: 2.

- Unit is a near-verbatim condensation of section 1 and adds little distinct explanation of CDC replay.
- Card's per-key/cross-table ordering and downstream-apply idempotency are absent; source plan records general CDC as unread.

### Materialized View

Verdict: **reject**. Findings: 2.

- Unit is a near-verbatim extract of CQRS text and describes projector/cursor recovery rather than stored-query/refresh mechanism; refresh ownership, locking and blocking absent.
- Card's PostgreSQL current page is unpinned and only heading-level; ledger claims command sections that were not read.

### Two-Phase Commit (2PC)

Verdict: **pass-with-findings**. Findings: 2.

- Card owner link label targets a different heading on the same page.
- Generic coordinator/recovery claims are not tied to the card's PostgreSQL source; source ledger has no 2PC row.

### Write-Around

Verdict: **pass-with-findings**. Findings: 2.

- Card rejects unreliable invalidation/read-after-write, but section allows invalidation or bounded TTL and permits a TTL-only deployment the card rejects.
- Fit condition 'write volume is high' omits the card's 'large or infrequent' qualifier; gate is ambiguous.

### TTL-Based Expiration

Verdict: **pass-with-findings**. Findings: 2.

- Trade-off compares a TTL duration with source change rate; no condition that TTL be shorter than business freshness.
- Jitter advice does not state that jitter cannot protect a single hot key.

### Cache Stampede Protection

Verdict: **pass-with-findings**. Findings: 2.

- No source-admission mechanism, coordination-failure fallback, wait bound or ownership rule despite card fit/contraindications.
- Coalescing is gated on stale acceptability, which belongs to stale-while-revalidate; coalescing can share a fresh load.

### Single Flight / Request Coalescing

Verdict: **pass-with-findings**. Findings: 2.

- Card's read-mostly/key-stability fit and authorization/parameter contraindication are absent; cancellation absent.
- Only in-process vs distributed-lease scope; card's independent-calls alternative and shared-latency/failure reversal are missing.

### Stale-While-Revalidate

Verdict: **pass-with-findings**. Findings: 2.

- Refresh lease is not treated as a correctness lock; background refresh can read an older version and publish after invalidation.
- Card lists TTL-only expiry as alternative; unit compares only blocking refresh.

### Multi-Level Caching

Verdict: **pass-with-findings**. Findings: 2.

- No promotion path (local miss -> shared -> local fill) or placement ownership.
- Card's local-only alternative is not compared in the anchored unit.

### CDN / Edge Caching

Verdict: **pass-with-findings**. Findings: 2.

- Both owner bindings use #cdn-edge-caching, but GitHub renders ### CDN / Edge Caching as #cdn--edge-caching; anchors do not resolve.
- Unit repeats cacheability/authorization sentences and omits origin-protection condition.

### Sharding

Verdict: **pass-with-findings**. Findings: 2.

- Unit repeats Purpose/Invariant/Failure paragraphs and sits under a second Bounded pattern ownership notes heading without preamble.
- Cross-shard join/transaction and hot-tenant conditions are not covered.

### Expand-and-Contract Schema

Verdict: **pass-with-findings**. Findings: 2.

- 122-word unit largely verbatim from earlier text; two lines exceed 100 characters.
- Card's rollback-impossible contraindication and versioned API boundary alternative are unsupported.

### Online Data Migration

Verdict: **pass-with-findings**. Findings: 2.

- Unit reuses earlier text and adds little depth; owner record wrongly says it is nested.
- Card says priority advanced while registry/source-plan record core.

### Backup, PITR and Restore

Verdict: **pass-with-findings**. Findings: 2.

- Card rejects PITR for missing restore evidence rather than mechanism mismatch; owner requires drills.
- Replica failover is not a competing alternative under the same assumptions.

### Circuit Breaker

Verdict: **pass-with-findings**. Findings: 2.

- Unit restates earlier table/alternative and two lines exceed 100 chars; little distinct depth.
- Card's retry/bulkhead alternative and fallback/state conditions lack owner support.

### Partitioning

Verdict: **pass-with-findings**. Findings: 2.

- Card failure/recovery names skew/maintenance; section covers query fan-out and plan inspection, not recovery.
- Section is table-only and range/list-only; card covers stream and PostgreSQL hash partitioning.

### Consistent Hashing

Verdict: **pass-with-findings**. Findings: 2.

- Card names hotspots/uneven rebalancing; section covers wrong-owner/incomplete-copy routing and epoch.
- Card requires virtual nodes/replication precondition; section treats vnodes as optional and omits replication.

### Leader-Follower Replication

Verdict: **pass-with-findings**. Findings: 2.

- Section repeats walkthrough and Consensus stale-leader text, carrying undefined A; no limits or promotion procedure.
- Card rejects untested failover and points recovery verification here; the unit does not explain quorum/term.

### Multi-Leader Replication

Verdict: **pass-with-findings**. Findings: 2.

- Invariant's LWW claim conflicts with cited Cassandra Dynamo record; gap is acknowledged-effect preservation/conflict metadata.
- Card rejects mandatory monotonic writes and names quorum; section never mentions either.

### Rate Limiting

Verdict: **pass-with-findings**. Findings: 2.

- Card citation says read.sre-overload covers Rate limiting, but ledger lists Per-Customer Limits/Client-Side Throttling; public SRE chapter has no rate-limiting section.
- Unit repeats three sentences from earlier paragraph; new material is identity, local/global quota and clock skew.

### Queue-Based Load Leveling

Verdict: **pass-with-findings**. Findings: 2.

- Unit near-verbatim restates earlier queue/failure paragraphs; only additions are monitoring and fit condition.
- Card names poison messages; unit has no poison-message disposition.

### Priority Queue

Verdict: **reject**. Findings: 2.

- Unit is near-verbatim extract of section 3 and never explains priority ordering, levels or non-preemption.
- Card requires broker priority support; unit covers only class authentication and fairness.

### Hedged Requests

Verdict: **pass-with-findings**. Findings: 1.

- Mitigation table is broken: failure/alternative paragraphs split rows, so last three mitigations render as literal text outside the table.

### Read Replicas

Verdict: **pass-with-findings**. Findings: 1.

- Card owner annotation is copied from adjacent multi-leader cards and ends 'not a complete multi-leader protocol', misstating the read-replica limit; linked section itself reads soundly.

### Quorum-Based Reads/Writes

Verdict: **pass-with-findings**. Findings: 2.

- Dedicated note repeats three sentences from section 2; adds no distinct owner content.
- R + W > N 'latest committed value' wording lacks version comparison/read repair; intersecting replica can still return older value.

### Index Table

Verdict: **reject**. Findings: 2.

- Linked unit explains a native secondary index, which the card lists as the alternative, not the separately maintained lookup table.
- Note repeats section-5 text and never covers dual-write consistency, separate-table maintenance or stale-row repair.

### CQRS Read Projections

Verdict: **pass-with-findings**. Findings: 2.

- Note repeats earlier CQRS sentences verbatim; little distinct ownership.
- Card's projection ownership, per-aggregate ordering and rebuild conditions, and unbounded-rebuild contraindication, are absent.

### Bulkhead

Verdict: **pass-with-findings**. Findings: 1.

- Card's technical-owner annotation is copied from Circuit Breaker and does not describe the Bulkhead limits.

### Retry with Exponential Backoff

Verdict: **pass-with-findings**. Findings: 2.

- Unit never defines exponential growth: no base, multiplier, cap or attempt sequence.
- Unit restates earlier paragraph and omits card's retry-budget condition; source record claims a Jitter section not present.

### Timeout

Verdict: **pass-with-findings**. Findings: 2.

- Card hard contraindication 'cancellation leaves irreversible effects' contradicts its failure/recovery and the unit's ambiguity rule; narrow to outcome cannot be observed/reconciled.
- Unit largely restates earlier timeout text; source record claims 'Cancel running futures' heading not present.

### Deadline Propagation

Verdict: **pass-with-findings**. Findings: 2.

- Card hard contraindications are overbroad or inverted: async work can still use a deadline; relative timeout avoids clock comparison; every-hop timeout is a reason to adopt propagation.
- Source record citation labels do not match the SRE chapter; unit repeats earlier deadline text and three lines exceed 100 chars.

### Failover / Failback

Verdict: **pass-with-findings**. Findings: 2.

- Unit largely verbatim from earlier failback paragraphs; first two sentences repeat that failback is not inverse.
- No citation/synthetic label; card's standby-promotion source does not support authority-epoch/rollback-gate claims.

### Consensus

Verdict: **pass-with-findings**. Findings: 2.

- Three sentences verbatim from elsewhere on the page; recycles scenario and alternative rather than adding distinct mechanism/limit.
- Card requires safety/progress verification and quorum-loss treatment; unit defines neither safety nor progress and has no citation.

### Distributed Lock

Verdict: **pass-with-findings**. Findings: 2.

- Card names quorum loss and release races; unit covers only pauses/delayed writes, and lease-first definition blurs boundary with Lease-Based Ownership.
- No citation; Kubernetes lease source does not support the bounded-pause exclusion claim.

### Lease-Based Ownership

Verdict: **pass-with-findings**. Findings: 2.

- Card's unbounded clock-skew contraindication is not addressed; stop-write deadline derivation and pause bound are undefined.
- Three sentences repeat earlier page text; line 207 exceeds 100 chars; no lease-duration/renewal-cost limit.

### Fallback

Verdict: **pass-with-findings**. Findings: 2.

- Card cites a Fallback section that does not exist; source heading is Load Shedding and Graceful Degradation, so the fallback-specific contract is unsourced.
- Unit omits card's same-failed-resource contraindication and cheaper/independently-safe fit; opening repeats page summary.

### Graceful Degradation

Verdict: **pass-with-findings**. Findings: 2.

- Card requires recovery hysteresis; unit has entry/recovery conditions but no hysteresis or normal-service resumption.
- Closing paragraph repeats visible-status requirement, has dangling 'now', and line 187 exceeds 100 chars.

### Load Shedding

Verdict: **pass-with-findings**. Findings: 2.

- Card's equally-critical and hard-obligation contraindications and essential-outcome requirement are absent.
- Card cites a load-shedding section that is not in the source record; opening repeats summary.

### Throttling

Verdict: **pass-with-findings**. Findings: 2.

- Unit states no invariant; its precondition list is marked invariant supported.
- Unit blurs throttling with load shedding and omits card's clients-cannot-react contraindication.

### Autoscaling

Verdict: **pass-with-findings**. Findings: 2.

- Unit repeats opening feedback-control sentences and does not address card's metric-can-be-gamed contraindication.
- Card's churn/cold-start reversal is only implicit, not stated as a decision condition.

### Cell-Based Architecture

Verdict: **reject**. Findings: 2.

- Unit is a near-verbatim condensation of the earlier cell-boundary section and omits cell-outage, control-plane, reassignment and restore recovery that card points to.
- Card cites Microsoft Deployment Stamps, not a cell source; source plan says not a dedicated cell source.

### Shuffle Sharding

Verdict: **reject**. Findings: 2.

- Opening guarantee that one unhealthy worker affects fewer tenants is not generally true; a failed worker affects every tenant whose subset includes it.
- Unit repeats earlier paragraph and gives tests, not recovery; too-few-shards and unstable-assignment contraindications absent.

### Deployment Stamps

Verdict: **pass-with-findings**. Findings: 1.

- Card technical-owner label is 'A cell is a boundary...' although anchor is #deployment-stamps; gloss conflates stamps with cells.

### Geode

Verdict: **pass-with-findings**. Findings: 2.

- Card's global-routing single-point contraindication is not covered.
- Replication lag and regional failover failure are not addressed beyond stale/isolation routing and fencing.

### Static Content Hosting

Verdict: **reject**. Findings: 2.

- Unit repeats earlier static-content mechanism/failure/alternative verbatim and states no cost/tradeoff; retained-version/GC limit sits outside unit.
- Card's origin-protection precondition, explicit-TTL alternative and prewarm/versioned-rollback recovery are absent.

### Tenant-Based Resource Isolation

Verdict: **pass-with-findings**. Findings: 2.

- Card requires compute/data/network quotas; section omits networking quota or network-isolation path.
- Card's shared-pool rate-limit alternative and stranded-capacity/unenforceable-quota contraindications are absent.

### Rolling Deployment

Verdict: **pass-with-findings**. Findings: 2.

- Card requires drain/rollback definition and rejects rollback needing simultaneous replacement; section mentions drain as cost only.
- Card alternative includes recreate and incremental-compatibility reversal; section compares only blue/green on spare capacity.

### Dark Launching / Shadow Traffic

Verdict: **pass-with-findings**. Findings: 2.

- Card cites only Fowler Strangler, which supports Strangler Fig, not dark launch/shadow traffic; owner note is synthetic with no exact source.
- Owner link #dark-launching-shadow-traffic does not match GitHub slug #dark-launching--shadow-traffic.

### Expand-and-Contract

Verdict: **pass-with-findings**. Findings: 2.

- Card's sole Flyway source covers ordered migrations and explicitly not full expand/contract; owner support is Fowler Parallel Change.
- Card rejects when rollback impossible, but owner keeps pattern applicable via forward repair.

### Controlled Cutover

Verdict: **pass-with-findings**. Findings: 2.

- Card cites only Fowler Strangler, which has no no-return/cutover-gate content; owner note cites no exact unit.
- Card makes partial-cutover detection a hard condition; owner gives no detection/limit for partial switch.

### Federated Identity

Verdict: **pass-with-findings**. Findings: 2.

- Card's RFC 9700 supports OAuth token hardening, not federation trust metadata, discovery, key rotation or revocation claims.
- Card requires revocation/key rotation fit conditions; owner explains neither revocation nor replay.

### Distributed Workflow Orchestration

Verdict: **pass-with-findings**. Findings: 2.

- Unit restates earlier workflow paragraphs and never states coordinator-vs-choreography distinction or cross-service coupling.
- Lines 148 and 154 exceed 100 characters.

### Load Balancing

Verdict: **pass-with-findings**. Findings: 2.

- Card's cited frontend chapter does not cover backend-selection signals or fast-error failure; datacenter ledger row absent.
- Unit largely restates L118-L142, omits health/ejection/retry safety/stale recovery; line 262 over 100 chars.

### Horizontal Scaling

Verdict: **pass-with-findings**. Findings: 2.

- HPA record does not cover partitionability, statelessness, cold start or coordination cost.
- Card's larger-partition alternative and stateless contraindication absent; failure path names coordination lag without recovery.

### Vertical Scaling

Verdict: **pass-with-findings**. Findings: 2.

- Kubernetes resource record does not cover provider size, restart/downtime or superlinear cost.
- Card's superlinear-cost contraindication and larger-size fit absent; 'Neither can increase...' has no antecedent.

### Immutable Infrastructure

Verdict: **pass-with-findings**. Findings: 2.

- Card technical-owner label is 'Infrastructure as code and drift' while link targets #immutable-infrastructure; label points to the wrong section.
- Section does not state automated replacement/rollback fit condition; orphaned-state failure only implicit.

### Strangler Fig

Verdict: **pass-with-findings**. Findings: 2.

- No limit for coexistence funding or team-cannot-own-two-paths contraindication; no-return/rollback condition absent.
- Alternative grouping does not match card's branch-by-abstraction/bounded rewrite.

### Branch by Abstraction

Verdict: **pass-with-findings**. Findings: 2.

- Section repeats opening mechanism and omits removal date/owner and permanent-seams failure.
- Card alternatives (Strangler/big-bang) conflict with section's facade/parallel run; abstraction-cost reversal absent.

### Parallel Run

Verdict: **pass-with-findings**. Findings: 2.

- Only cited Fowler Strangler source never mentions parallel run; ledger claims do not support comparison keys/side-effect/commit authority.
- Card owner label is 'A versioned sequence of safe intermediate states', not Parallel Run; 'shadow index' alternative conflicts with card's shadow traffic.

### Blue/Green Deployment

Verdict: **pass-with-findings**. Findings: 2.

- Card's externalized-state fit and in-flight-work contraindication are absent from anchored note.
- Owner backlink uses #blue-green-deployment, but GitHub renders ### Blue / Green Deployment as #blue--green-deployment; backlink fails.

### Canary Release

Verdict: **pass-with-findings**. Findings: 2.

- 75 of 120 words repeat the page Purpose; section sits under a second Bounded pattern ownership notes H2, limiting distinct depth.
- Representative-cohort fit and metric-leakage failure absent; lines 162 and 167 exceed 100 chars.

### Feature Flags / Feature Toggles

Verdict: **pass-with-findings**. Findings: 2.

- 65 of 124 words repeat earlier feature-flag text; fail-safe default, observable evaluation, snapshot-age recovery and dark-code alternative absent.
- Owner/backlink use #feature-flags-feature-toggles, but GitHub renders ### Feature Flags / Feature Toggles as #feature-flags--feature-toggles; atlas link targets nonexistent V11/C12.

### GitOps

Verdict: **pass-with-findings**. Findings: 2.

- 76 of 126 words repeat earlier GitOps paragraph; little distinct depth.
- Rollback-as-revert-commit and secret-handling conditions absent; manual-release alternative not covered.

### Fencing Tokens

Verdict: **pass-with-findings**. Findings: 2.

- Card reversal is inverted: cheaper destination enforcement favors fencing; no reversal condition in note.
- Note is not self-contained: A/B undefined, repeats earlier text, token/epoch reuse failure absent.

### Quorum Coordination

Verdict: **pass-with-findings**. Findings: 2.

- Note does not own card decision: no intersection/minority-refusal invariant; leader alternative still needs quorum; static assignment, failure-domain and joint membership absent.
- Cited Raft overview has no Safety section and does not support terms/votes/log matching/joint consensus claims.

### Causal Ordering

Verdict: **pass-with-findings**. Findings: 2.

- Note repeats four sentences from section 1 and omits caveat that Lamport clocks cannot distinguish concurrency; vector-clock fit absent.
- Card hard contraindications and partition/server-switch failure path absent.

### Session Consistency

Verdict: **pass-with-findings**. Findings: 2.

- Note repeats seven body sentences and drops original-sketch caveat; 'If none can' lacks antecedent.
- Card eventual-consistency alternative and routing/failover reversal absent; cited Session guarantees section not in current index.

### Zero Trust Architecture

Verdict: **pass**. Findings: 0.


### Least Privilege

Verdict: **pass**. Findings: 0.


### RBAC / ABAC

Verdict: **pass-with-findings**. Findings: 2.

- Owner anchor #rbac-abac does not resolve on GitHub; ### RBAC / ABAC renders as #rbac--abac, and backlink uses single-hyphen form.
- Line 114 grammar: compound subject requires 'grant'.

### Workload Identity / mTLS

Verdict: **pass-with-findings**. Findings: 2.

- Card cites read.batch6-istio sections but fetch ends before Istio identity/MTLS/authorization; Workload Identity is not a heading, so claimed scope and rotation support are not established.
- Card says priority advanced while registry/source-plan record core; owner anchor #workload-identity-mtls does not resolve (#workload-identity--mtls).

### Valet Key

Verdict: **pass-with-findings**. Findings: 2.

- Card fit condition says resource can issue scoped tokens, but section says resource enforces and revocation sits at authority; can wrongly exclude an enforcing-only resource.
- Card owner label 'Token and credential boundaries' targets #valet-key, not the named heading.

### Multitenant Isolation

Verdict: **pass-with-findings**. Findings: 2.

- Card duplicates Tenant-Based Resource Isolation framing and failure line; compute/quota/noisy-neighbor conditions belong to sibling section.
- Decision layer is inverted: card's shared-pool alternative is this anchor's mechanism, while anchor's tenant-per-deployment is the isolation side.

### Distributed Tracing

Verdict: **pass-with-findings**. Findings: 2.

- Unit repeats page Purpose definition and missing-span sentence almost verbatim; little new mechanism.
- Card's sensitive-data, retention, one-service and broken-context recovery conditions are absent.

### Audit Trail

Verdict: **pass-with-findings**. Findings: 2.

- Unit restates walkthrough without tamper detection, audit-access authority or post-loss reconciliation; card's tamper/missing-event claim unsupported.
- Card's OpenLineage source is lineage metadata, not append-only attributable/tamper-evident audit; audit mechanism lacks exact source.

### SLI/SLO and Error Budgets

Verdict: **pass-with-findings**. Findings: 2.

- Card owner link and backlink use #sli-slo-and-error-budgets, but GitHub renders ### SLI / SLO and Error Budgets as #sli--slo-and-error-budgets; links do not resolve.
- Note repeats walkthrough 99.9%/300% and 2xx/denominator sentences; new content limited to definitions, publish/review and final fit/limit.

### Synthetic Monitoring

Verdict: **pass-with-findings**. Findings: 2.

- Read record lists Synthetic Monitoring and Alerting sections, but hashed SRE Workbook page has neither heading; synthetic appears only under Testing Alerting Logic.
- Card failure/recovery names probe blindness and credential leakage; owner covers failed auth, shallow probes, rotation, noise and journey coverage, not those failures.

### Health, Readiness and Liveness Checks

Verdict: **pass-with-findings**. Findings: 2.

- Read record was truncated at 100,000 chars before probe content; claimed Liveness/Readiness/Startup sections are not in hashed read, so card support unverified.
- Card alternative adds process supervision; owner presents only external journey monitoring and does not discuss process supervision.

### Polyglot Persistence

Verdict: **pass-with-findings**. Findings: 2.

- Card alternative is single store with derived projections/query-time joins; owner names only single store with secondary indexes, so alternatives are not compared.
- Card names dual-write ambiguity and partial migration; owner requires write owner/schema migration but does not describe those failure modes or recovery.

## Re-review after remediation

Three prior rejects were rewritten and re-reviewed. Verdicts are now pass-with-findings, not pass.

### tycho.pattern.priority-queue

Verdict: **pass-with-findings**. Findings: 2.

- Card requires tenant isolation and per-hop class verification; note covers propagation but not tenant isolation.
- Closing alternative is verbatim from section 3; authentication sentence is a near-verbatim paraphrase.

### tycho.pattern.index-table

Verdict: **pass-with-findings**. Findings: 2.

- Fit condition says must be shared across stores, contradicting query-shape/sort-order cases; lines 108 and 113 exceed 100 chars.
- Only cited source is PostgreSQL native indexes, not the application-owned lookup table; dual-write/stale-row claims lack cited public support.

### tycho.pattern.service-oriented-architecture-soa

Verdict: **pass-with-findings**. Findings: 1.

- Alternative groups microservices, API gateway and modular monolith under capabilities are few and adds a component the card does not list; card maps microservices to independent product capabilities and modular monolith to one ownership boundary.


## Second re-review after remediation

Three more prior rejects were rewritten and re-reviewed. All are now pass-with-findings.

### tycho.pattern.change-data-capture-cdc

Verdict: **pass-with-findings**. Findings: 2.

- General CDC replay claims still lack an exact source; source plan records general CDC as unread, card cites only Debezium outbox-router.
- Card cross-table-ordering contraindication remains unowned; section requires per-key grouping but never states cross-table ordering is unavailable.

### tycho.pattern.materialized-view

Verdict: **pass-with-findings**. Findings: 2.

- Card failure/recovery still cites projector crash/cursor gaps, and good-fit requires source version/offset; rewritten section covers refresh, not event projection.
- PostgreSQL source record is unpinned and lists SQL commands as page sections; line 294 exceeds 100 chars.

### tycho.pattern.static-content-hosting

Verdict: **pass-with-findings**. Findings: 2.

- Five of eight sentences still track earlier lines 77-90; distinct addition is limited to manifest alias, host ownership and GC/tombstone.
- Card alternative explicit-TTL cache prong and edge-complexity reversal are absent.


## Third re-review after remediation

The final two prior rejects were rewritten and re-reviewed. All are now pass-with-findings.

### tycho.pattern.cell-based-architecture

Verdict: **pass-with-findings**. Findings: 2.

- Card cites only Deployment Stamps read record, not a dedicated cell source; cell-specific blast-radius/failover/migration claims need src.cell-boundaries or a comparison-only label.
- Concrete outage/restore policy remains outside anchored unit; line 166 exceeds 100 chars.

### tycho.pattern.shuffle-sharding

Verdict: **pass-with-findings**. Findings: 2.

- Unit repeats earlier comparison clause verbatim and gives assignment tests rather than a hot-tenant failure/recovery path.
- Card hard contraindication on operational cost of many assignments is absent.


## Fourth re-review after remediation

### Hedged Requests

Verdict: **pass**. Findings: 0. The split mitigation table is repaired and the card/owner link resolves.


### Service-Oriented Architecture (SOA) — latest re-review

Verdict: **pass**. Findings: 0. The alternative now maps microservices to independent product teams and the modular monolith to one ownership boundary; mediation, registry, bus bottleneck and observability are present.


## Fifth re-review after remediation

### Priority Queue

Verdict: **pass-with-findings**. One remaining finding: near-verbatim reuse of section 3.

### Index Table

Verdict: **pass-with-findings**. Latest review flagged a native-index paragraph mislabeled as the index-table mechanism and a long line; both were scoped/wrapped, re-review pending.


### Priority Queue — latest re-review

Verdict: **pass**. Findings: 0. Broker ordering, non-preemption, per-hop class authentication, tenant caps, aging/max-wait and admission-controlled FIFO align with the card.


### Saga — latest re-review

Verdict: **pass**. Findings: 0. Card and §4 now name only one local transaction or two-phase commit; the #saga owner anchor resolves.


### Process Manager / Routing Slip — latest re-review

Verdict: **pass**. Findings: 0. Both coordinator and routing-slip variants are distinct, and the V04↔V11 anchors match one heading and resolve.


### Index Table — latest re-review

Verdict: **pass**. Findings: 0. Synthetic disclosure present, native-index text scoped as the alternative, line lengths under 100 and the card owner anchor resolves.


### Transactional Outbox — latest re-review

Verdict: **pass**. Findings: 0. Card and section agree on conditions, contraindications, alternative and recovery; the exact technical-owner link qualifies for the repository link exception.


### Domain Events — latest re-review

Verdict: **pass**. Findings: 0. Card contraindications and the synchronous-call/command alternative agree, including the reversal condition.


### Canonical Data Model — card-label re-review

Verdict: **pass**. Findings: 0. The corrected technical-owner label describes the linked owner section.


### Read Replicas — card-label re-review

Verdict: **pass**. Findings: 0. The corrected technical-owner label describes the linked owner section.


### Bulkhead — card-label re-review

Verdict: **pass**. Findings: 0. The corrected technical-owner label describes the linked owner section.


### Deployment Stamps — card-label re-review

Verdict: **pass**. Findings: 0. The label now names independent deployment units, routing keys and upgrade ownership, all supported by the owner section.


### Sidecar — latest re-review

Verdict: **pass**. Findings: 0. Card label, owner anchor and lifecycle/fit conditions agree.


### Immutable Infrastructure — latest re-review

Verdict: **pass**. Findings: 0. Card label, owner anchor and lifecycle/fit conditions agree.


### Valet Key — latest re-review

Verdict: **pass**. Findings: 0. Issuance by resource or separate authority and enforcement by the resource cohere; the exact owner link qualifies for the repository link exception.


### Resequencer — latest re-review

Verdict: **pass**. Findings: 0. Label, per-key alternative, buffer-cap action and late-message disposition agree.


### Content-Based Router — latest re-review

Verdict: **pass**. Findings: 0. Label/anchor, predicate-trust, rejected-disposition or stage-contract text agree.


### Message Filter — latest re-review

Verdict: **pass**. Findings: 0. Label/anchor, predicate-trust, rejected-disposition or stage-contract text agree.


### Pipes and Filters — latest re-review

Verdict: **pass**. Findings: 0. Label/anchor, predicate-trust, rejected-disposition or stage-contract text agree.


### Claim Check — latest re-review

Verdict: **pass**. Findings: 0. Token binding, payload digest, retrieval latency and label/anchor agree.


### Saga Choreography — latest re-review

Verdict: **pass**. Findings: 0. Label, timeout policy, versioned contract and central-ordering alternative agree.


### Gateway Offloading — latest re-review

Verdict: **pass**. Findings: 0. Inclusion boundary/contraindications align; the exact owner link qualifies for the repository link exception.


### Anti-Corruption Layer — latest re-review

Verdict: **pass**. Findings: 0. Undefined R7 removed, synthetic example labelled, contract tests/versioned mappings and line lengths fixed.


### Expand-and-Contract Schema — latest re-review

Verdict: **pass**. Findings: 0. Distinct 127-word note with compatibility gates, reader inventory, expand/contract dates and lines <=100.


### Circuit Breaker — latest re-review

Verdict: **pass**. Findings: 0. Distinct state-machine note with thresholds, bounded half-open probes, separated metrics and lines <=100.


### Lease-Based Ownership — latest re-review

Verdict: **pass**. Findings: 0. Skew/pause bounds, stop-write deadline and lease/renewal cost are stated.


### Deadline Propagation — latest re-review

Verdict: **pass**. Findings: 0. Relative-duration propagation, monotonic clocks, corrected card contraindications and lines <=100.


### Graceful Degradation — latest re-review

Verdict: **pass**. Findings: 0. Recovery hysteresis, normal resumption, essential-path retest and non-duplicated closing text.


### Correlation Identifier — latest re-review

Verdict: **pass**. Findings: 0. Operation-scoped uniqueness, collision check and ambiguous/expired recovery agree.


### Request-Reply Messaging — latest re-review

Verdict: **pass**. Findings: 0. Durable owned reply channel, late/duplicate dispositions and state lifetime beyond deadline.


### Dead Letter Channel / DLQ — latest re-review

Verdict: **pass**. Findings: 0. Quarantine retention/capacity/access/cleanup and replay identity/authorization/commit checks agree.


### Durable Subscriber — latest re-review

Verdict: **pass**. Findings: 0. Stable effect key/dedup and stale-replay deadline are explicit and card-aligned.


### Idempotent Receiver — latest re-review

Verdict: **pass**. Findings: 0. Key derivation/validation/collision and marker lifetime/cleanup/post-expiry agree.


### Event-Driven Consumer — latest re-review

Verdict: **pass**. Findings: 0. Prefetch/in-flight/ack bounds, pause-or-scale overload action and polling/scheduled-batch reversal agree.


### Blue-Green Deployment — latest re-review

Verdict: **pass**. Findings: 0. Heading/anchor normalized; card fit matches externalized-or-dual-readable state and in-flight drain/route.


### Feature Flags / Feature Toggles — latest re-review

Verdict: **pass**. Findings: 0. Normalized heading/anchor, fail-safe default, observable evaluation, snapshot-age recovery and corrected atlas link.


### GitOps — latest re-review

Verdict: **pass**. Findings: 0. Revert-commit rollback, external secret handling, manual-release alternative and distinct depth.


### Fencing Tokens — latest re-review

Verdict: **pass**. Findings: 0. Self-contained, token/epoch reuse failure and corrected reversal condition.


### Causal Ordering — latest re-review

Verdict: **pass**. Findings: 0. Vector-clock fit, Lamport concurrency caveat, partition/server-switch recovery and merge rule.


### Gateway Aggregation — latest re-review

Verdict: **pass**. Findings: 0. Read-mostly fit, hidden-workflow contraindication, retry amplification and API Composition boundary.

