---
metadata_version: 1
id: "tycho.page.4e0e4db7547b45469f36915886473750"
kind: "page"
parent_id: "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-independence.md"
title: "Independent deployment and its costs"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Which coordination costs justify introducing a remote boundary?"
route_hints:
  questions:
    - "Which coordination costs justify introducing a remote boundary?"
  prerequisites:
    - "tycho.page.acb452608a8b42898aae7482c27f5f04"
  related_ids:
    - "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
    - "tycho.page.acb452608a8b42898aae7482c27f5f04"
    - "tycho.page.cdb86c0b91a6489f979689ab08efad35"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "service"
    - "independence"
evidence_scope:
  source_ids:
    - "src.soa-model"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.acb452608a8b42898aae7482c27f5f04; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-29"
source_inspection_date: null
content_verified_at: null
---
# Independent deployment and its costs

**Owning question:** Which coordination costs justify introducing a remote boundary?

This page belongs to [V02/C04 — SOA, microservices and distributed boundaries](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.acb452608a8b42898aae7482c27f5f04:1 -->
## 1. Separate concept, deployment and ownership

| Dimension | Service-oriented view | Microservice-style tendency | Design caution |
|---|---|---|---|
| Capability | Exposes work/results to a consumer under a described contract | Decomposes around cohesive business capabilities | An endpoint does not establish ownership |
| Visibility and policy | Consumer can discover/reach/use described capability | Direct service or mediated routing/discovery | Discovery is not authentication or authorization |
| Deployability | Depends on concrete SOA implementation | Separate services are intended to deploy independently | Coordinated DB/schema deployment can defeat independence |
| Information model | Public messages and effects specified | Local representation often private to each service | One global canonical model may hide contextual differences |
| Data authority | Must be explicitly declared | Decentralized state ownership is common | Two writers for one invariant remain unsafe |
| Operations | Versions, policy, monitoring and governance | Per-service pipelines, telemetry, resilience and automation | More moving parts are not free |
| Transaction | Contracts define business effect and failure semantics | Remote calls/events cross resource boundaries | Local ACID cannot cover arbitrary remote effects |

Some service-oriented systems use large-grained capabilities and centrally governed contracts; others use narrower services with distributed ownership. Neither label tells you whether a product has acceptable latency, isolation or release economics.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Self-Contained Service](../../v11-pattern-atlas/c01-application-boundaries/self-contained-service.md#self-contained-service)
> — decision conditions and contraindications.
<!-- tycho-question-source:tycho.page.acb452608a8b42898aae7482c27f5f04:2 -->
## 2. Independence is not proved by a separate container

A separately deployed component can still require lockstep releases if it:
- writes tables owned by other components;
- directly imports their internal data structure;
- changes events/enum meanings without consumer compatibility;
- relies on a shared deployment gate or one synchronous downstream critical path;
- lacks its own operational owner, rollback/forward-repair path or documented support window.

Conversely, distinct modules inside one executable may remain the safer target when transactions must remain local and independent release cadence brings little benefit. [Layered/hexagonal design](../c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md) owns source dependency direction, [domain/data authority](../c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md) owns semantic boundaries, and [modular monolith](../c03-modular-monolith-and-internal-events/modular-monolith-and-internal-events.md) owns internal lifecycle.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.acb452608a8b42898aae7482c27f5f04:4 -->
## 4. The costs created by a remote boundary

Moving a call across processes introduces issues that in-process invocation does not have in the same way:

- a request can be delivered and committed while the reply is lost;
- transport reachability changes independently of the callee's data state;
- latency and deadline budgets now include network, service discovery, queue/pool wait and TLS/authentication;
- retries can amplify load and duplicate non-idempotent business effects;
- deployment/schema/event versions overlap during rollouts;
- per-service observability and security identities grow;
- independent scaling may shift pressure to a shared datastore or hot key.

**Synthetic failure:** the reservation service commits an exclusive booking, but a gateway times out. If the caller retries with a new logical identity, two notifications or other effects may be created. A correctly designed application reconciles stable operation identity; it cannot infer “nothing happened” from the missing reply. See [retries/idempotency](../../v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/retries-idempotency-and-ambiguous-effects.md) and [HTTP/RPC contracts](../c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md).

These costs must be measured against concrete promised benefits; they cannot be hand-waved away by a circuit breaker.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](service-orientation-microservices-and-distribution.md) |
| Next | [Continue the reasoning](service-contracts.md) |
| Integrated question | [Original scenario and limits](service-orientation-microservices-and-distribution.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Self-Contained Service

The pattern rule is to design a service so that it can respond to a synchronous
request without waiting for the response from any other service. A
self-contained service uses the Saga pattern to asynchronously maintain data
consistency. It uses the CQRS pattern to maintain a replica of data owned by other
services.

The baseline problem is that a synchronous call to an unavailable collaborator
cannot complete and must return an error. A service can retry a request to a
failed collaborator but this increases response time. Synchronous
request/response reduces availability. The pattern's recovery design is a local
read model plus asynchronous reconciliation, which lets the service respond
while a collaborator is unavailable. The trade-off is duplication, reconciliation
and staleness.

A self-contained service still exposes a synchronous contract to its caller. It
reduces runtime coupling, not the service boundary. The pattern is about response
independence and availability.
