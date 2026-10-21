# Deep-source expansion plan — 2026-10-22

Program: #228. Scope: 145 pattern entries, 11 families. This plan tracks the
deep-source pass; it does not claim sufficient coverage or independent review.

## Method

- One family per batch; read or reread one exact public unit per entry.
- Add mechanism, applicability, contraindications, alternative, failure/recovery
  and trade-off detail to the owner section and card.
- Update owner-unit evidence with verbatim quotes and the reading ledger with
  exact sections; keep coverage `partial-bounded` until independent review.
- Rebuild registry, phase 4, semantic audit and delivery evidence; run all
  validators, tests and premerge.

## Family gap matrix

Codes: M mechanism, I invariant, F failure/recovery, A alternative.

- api-and-service-communication: 12 entries, 5 partial, 7 bounded; gaps M5 I0 F4 A7.
- application-architecture-and-boundaries: 12 entries, 4 partial, 8 bounded; gaps M4 I4 F5 A6.
- caching-and-retrieval: 14 entries, 2 partial, 12 bounded; gaps M1 I1 F6 A4.
- data-consistency-transactions-and-event-sourcing: 14 entries,
  7 partial, 7 bounded; gaps M6 I5 F7 A11.
- database-and-storage-architecture: 13 entries, 4 partial, 9 bounded; gaps M4 I3 F6 A7.
- deployment-and-legacy-modernization: 12 entries, 5 partial, 7 bounded; gaps M4 I4 F5 A6.
- distributed-coordination: 9 entries, 2 partial, 7 bounded; gaps M1 I2 F3 A5.
- messaging-and-event-driven-integration: 20 entries, 6 partial, 14 bounded; gaps M6 I1 F3 A5.
- resilience-and-fault-tolerance: 16 entries, 10 partial, 6 bounded; gaps M10 I7 F8 A15.
- scalability-and-load-distribution: 10 entries, 1 partial, 9 bounded; gaps M1 I0 F6 A7.
- security-isolation-and-operational-architecture: 13 entries,
  1 partial, 12 bounded; gaps M1 I0 F4 A3.

## Batch order

1. distributed-coordination (9 entries, 3 partial).
2. resilience-and-fault-tolerance (16, 10 partial).
3. data-consistency-transactions-and-event-sourcing (14, 7 partial).
4. api-and-service-communication (12, 5 partial).
5. deployment-and-legacy-modernization (12, 5 partial).
6. application-architecture-and-boundaries (12, 4 partial).
7. database-and-storage-architecture (13, 4 partial).
8. messaging-and-event-driven-integration (20, 6 partial).
9. caching-and-retrieval (14, 2 partial).
10. scalability-and-load-distribution (10, 1 partial).
11. security-isolation-and-operational-architecture (13, 1 partial).

## Per-entry acceptance for this pass

- [ ] One exact public source section read and recorded.
- [ ] Owner section explains mechanism, applicability, contraindications, alternative
      and failure/recovery with exact scope.
- [ ] Card fields expanded beyond the minimal template.
- [ ] Owner-unit evidence quotes are verbatim and coverage stays honest.
- [ ] Registry, phase 4, semantic audit and delivery evidence rebuilt.
- [ ] Validators, tests and premerge pass.

## Pilot batch — distributed coordination

- Leader Election: `partial-bounded`; gaps failure_recovery, alternative.
  Source: `read.batch4-raft.2026-10-21`.
- Consensus: `partial-bounded`; gaps none.
  Source: `read.batch4-raft.2026-10-21`.
- Distributed Lock: `partial-bounded`; gaps none.
  Source: `read.batch4-k8s-leases.2026-10-21`.
- Lease-Based Ownership: `partial-bounded`; gaps alternative.
  Source: `read.batch4-k8s-leases.2026-10-21`.
- Fencing Tokens: `partial-bounded`; gaps none.
  Source: `read.batch4-fencing.2026-10-21`.
- Quorum Coordination: `partial-bounded`; gaps alternative.
  Source: `read.batch4-raft.2026-10-21`.
- Causal Ordering: `partial`; gaps invariant, failure_recovery.
  Source: `read.batch4-causal.2026-10-21`.
- Session Consistency: `partial-bounded`; gaps alternative.
  Source: `read.batch4-jepsen.2026-10-21`.
- Distributed Workflow Orchestration: `partial`; gaps mechanism,
  invariant, failure_recovery, alternative.
  Source: `read.batch2-temporal-workflows.2026-10-21`.

## Batch 1 progress — 2026-10-22

- Distributed Lock: owner section expanded with lock semantics, failure classes
  and alternatives; owner unit is `partial-bounded` with all four evidence
  dimensions supported.
- Causal Ordering: owner section expanded with the causal invariant, partition/
  server-switching failures and alternatives; evidence is `partial-bounded`.
- Distributed Workflow Orchestration: owner section expanded with durable state,
  replay/repair failure modes and alternatives; evidence is `partial-bounded`.
- Leader Election, Lease-Based Ownership, Quorum Coordination and Session Consistency
  now have all four evidence dimensions supported.
- **Batch 1 complete:** all nine distributed-coordination entries are
  `partial-bounded` with no evidence-dimension gaps. Next: resilience-and-fault-tolerance.
## Resilience progress — 2026-10-22

- Fallback, Graceful Degradation and Load Shedding: owner vocabulary and cards
  expanded; each is `partial-bounded` with all four evidence dimensions supported.
- Retry with Exponential Backoff, Timeout, Deadline Propagation, Throttling and Rate
  Limiting are also `partial-bounded` with all four dimensions supported.
- Queue-Based Load Leveling, Health Endpoint Monitoring and Failover/Failback are also
  `partial-bounded`.
- Remaining resilience gaps: alternative/failure evidence for Circuit Breaker, Bulkhead
  and Hedged Requests.
