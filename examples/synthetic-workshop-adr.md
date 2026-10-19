# ADR-SYN-001 — Retain the registration boundary pending measured failure evidence

> **Status: proposed / insufficient evidence, synthetic only.** Original demonstration for Tycho [#20](https://github.com/rouslanbaranov/tycho/issues/20), dated 2026-10-19. No real system, measured load, human approval or deployment is represented.

## Context and decision boundary

The fictional workshop-registration application owns a local registration database and communicates with a separate notification component. A user sometimes *hypothetically* retries after a lost response. We do not know whether the transaction committed, whether a duplicate request was made, or whether a notification was independently durable. The scope is the registration command and its state/notification boundary; the workload, SLOs, release tooling and recoverability are **unknown**.

Reference owners: [requirements/workload model](../authoring/models/requirements-workload-profile.md), [legacy modernization baseline](../authoring/models/legacy-modernization-profile.md), [pattern applicability contract](../authoring/models/pattern-applicability-card.md), and [outbox mechanism research](../book/distributed/transactional-outbox-and-idempotency.md). These are Tycho's public synthetic contracts, not production instrumentation.

## Candidate set, including retaining the baseline

| Option | Potential outcome, not a forecast | Risks and prerequisites |
|---|---|---|
| A: retain one deployable application; add command idempotency and tracing | Smallest change if duplicate effects are at the local transaction boundary | Need atomic uniqueness and actual proof of same-intent request outcomes |
| B: retain registration database; add outbox and relay | Could durably express the *intent* to publish after registration commit | Additional relay, lag, dedup and reconciliation; requires an actual external-notification durability requirement |
| C: split registration and notification into separately deployed services | Could enable independent release/operations, **if this is a requirement** | Cross-system transaction semantics, monitoring, mixed-version contracts and incident burden |

A high RPS figure, number of users or preference for microservices has NOT been supplied; it cannot be invented.

## Hard gate assessment and evidence request

| Gate | A | B | C | Resolution |
|---|---|---|---|---|
| No duplicate committed seat allocation | Unknown | Unknown | Unknown | Prove local invariant and race handling under concurrent same-key retries |
| Existing callers remain compatible | Unknown | Unknown | Unknown | Inventory consumers; exercise old/new API variants |
| No silent loss of accepted notification | Unspecified requirement | Conditional benefit; not verified | No automatic guarantee | First obtain business durability obligation; test commit-to-relay failure |
| Downtime and RPO/RTO within approved budget | Unknown | Unknown | Unknown | Agree and execute fault/recovery exercise |
| Operating budget and owner support | Unknown | Unknown | Unknown | Count relay/deployment/monitoring and maintenance, not just cloud spend |

**No option can be accepted** under these unknown hard constraints. Do not give C a preference score to bypass missing correctness evidence.

## Falsifiable investigations, in dependency order

1. Obtain the real command idempotency contract, including payload-identity, key retention, transaction boundary and the current observable result after a dropped HTTP reply. Inject two simultaneous equal-intent commands and replay after an ambiguous timeout. **Reject** A if the local transaction cannot preserve uniqueness without a stronger coordination mechanism.
2. Establish whether notification delivery is a durable user obligation, a best-effort convenience or optional. If durable, examine a controlled crash after local commit before external publication, and verify replay and consumer dedup. **Reject** any option that loses accepted business effects.
3. Measure current end-to-end request and notification delays under the agreed real operation mix and burst. Profile queues, pool waits and storage contention. If all user goals are satisfied, **retain or tune in place** and do not split merely to add topology.
4. Only if independent deployment is an approved capability, test mixed-old/new client compatibility, actual release procedure and data-reconciliation paths. A green unit test of a new service does not prove these boundaries.

## Proposed decision

**Measure first; provisionally retain the current deployment boundary.** This is a deliberately cautious outcome, not approval to deploy a specific implementation. Consider B only after notification durability and operating support are proven. Consider C only after independent deployment need, interface ownership and costs are established. No transition or irreversible migration is authorized.

Consequences: less immediate topology change; more effort spent discovering transaction correctness and operational facts; possible future extraction if the evidence justifies it. Revisit the decision upon the first verified missing-response/concurrency result, confirmed notification delivery requirement, approved target SLO/RPO/RTO, or external API version change.

## Transparent sensitivity illustration

If stakeholders merely change subjective weight between release independence and operations simplicity, a numerical option ranking can reverse without any factual system change (see [the candidate-comparison model](../authoring/models/candidate-comparison-adr.md)). Such a reversal motivates stakeholder clarification, not a new architecture. The hard unknown gates above remain unchanged and binding.

## Source and provenance boundary

- [arc42 §9 Architecture decisions](https://docs.arc42.org/section-9/), *Content*, *Motivation*, *Form*: inspected 2026-10-19 as support for recording rationale, alternatives and consequences, not a technical answer for the fictitious application.
- [Tycho outbox pilot](../book/distributed/transactional-outbox-and-idempotency.md), *Failure and recovery matrix*: a separately sourced public mechanism explanation; not a claim that a broker/database integration has been deployed here.
- Every numbered option, scenario and unknown above is a **newly invented exercise**, with no request traces, experiments, QA sign-off or reviewer approval.

**Review state: self-authored example, no independent approval, no infrastructure or benchmarks executed.**