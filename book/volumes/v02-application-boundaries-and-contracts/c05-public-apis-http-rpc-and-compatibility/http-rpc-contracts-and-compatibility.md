---
metadata_version: 1
id: "tycho.page.cccbd188936543a2aaf904f4002236d8"
kind: "page"
parent_id: "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md"
title: "HTTP and RPC contracts: compatibility, deadlines and retry safety"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Public APIs, HTTP/RPC and compatibility. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do deadlines, versioning, retries and API contracts evolve?"
  prerequisites: []
  related_ids:
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
    - "tycho.page.e7e65b602c5a41fb80fa4a1e88a33298"
    - "tycho.page.43414664520b4866929f7f006f27f59b"
    - "tycho.page.de9c5bc478ba44718fcb731e69109dce"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "HTTP"
    - "and"
    - "RPC"
    - "contracts"
    - "compatibility"
    - "deadlines"
    - "retry"
    - "safety"
evidence_scope:
  source_ids:
    - "src.http-semantics"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-30"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:-1 -->

# HTTP and RPC contracts: compatibility, deadlines and retry safety

> **Research status:** independent, source-grounded book draft, 2026-10-19. **Proposed owner:** V02/C05 (public APIs, HTTP/RPC and compatibility). No runtime tests, empirical benchmark, client interoperability test or independent technical acceptance is claimed.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Backend for Frontend](../../v11-pattern-atlas/c02-api-communication/backend-for-frontend.md#backend-for-frontend-bff) — decision conditions and contraindications.
> [API Composition](../../v11-pattern-atlas/c02-api-communication/README.md#api-composition) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:0 -->
## Purpose and mission

An API is not merely a URL, an interface description or an encoded message. It is a promise about which effects a caller can request, when the caller may assume the effect occurred, how errors are interpreted, and what remains usable when old and new versions coexist. The architectural decision is therefore not initially “HTTP or RPC?” It is “which observable contract can the caller and provider preserve under delay, retries, partial failure and version skew?”

This chapter distinguishes **transport/method semantics**, **domain-effect identity**, **time budgets**, **wire and behavior compatibility**, and **contract evidence**. It uses original synthetic examples and independently published specifications. Service boundaries and transaction coordination are explained further in [module and service boundaries](../../../application/architecture-styles-and-module-boundaries.md), [outbox and idempotent effects](../../../distributed/transactional-outbox-and-idempotency.md) and [safe versioned rollout](../../../delivery/progressive-delivery-and-schema-evolution.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:9 -->
## Engineering walkthrough — Mixed clients and an unacknowledged committed POST

**Original compatibility matrix:** legacy client N sends a booking `POST` with no stable key; new N+1 sends `operationId` and accepts a `PENDING` response. Server S1 only understands immediate success/failure; S2 persists operation identities and can report UNKNOWN while reconciliation runs. A rollout that updates S2 first must not fabricate keys on N's behalf as if independent retries were uniquely identifiable.

| Interaction | Valid contract | Unsafe shortcut |
|---|---|---|
| N → S2 | Preserve legacy semantics or explicitly gate incompatible features | Return `PENDING` when old client interprets any 2xx as final confirmation |
| N+1 → S1 | Keep supported old wire format or reject unsupported version | Assume a new field is understood merely because payload parses |
| N+1 → S2 | Stable intent ID, bounded deadline and queryable result | Treat cancellation as authoritative transaction abort |
| Response lost after S2 commit | Resolve from durable operation identity | Blindly retry as a fresh write |

HTTP [RFC 9110 idempotent-method semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) apply at the method-intent level, not automatically to a custom booking POST. gRPC deadline/cancellation guidance distinguishes no-longer-waiting from undoing a side effect. Record independent transport timeout, domain status and ledger lookup outcomes.

**Proposed test:** introduce N/N+1 clients, two server versions, wrong-version events, lost acknowledgments and one concurrent duplicate intent. The same logical reservation must never be confirmed twice; errors must remain machine distinguishable and within the client's retry budget. If old clients cannot represent pending outcomes, retaining an immediate final result or an explicit incompatible-version refusal may be safer than a subtle protocol upgrade. No client/server interoperation was executed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:10 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — DGS and Spring GraphQL](../../../cases/netflix-dgs-spring-graphql-convergence.md)**. **Relevant mechanism or architectural contrast:** Compatibility wrappers and measured overhead can support framework convergence without a big-bang rewrite. **Not established by this report/playbook:** A staged 2024 DGS/Spring journey does not guarantee API parity for arbitrary GraphQL implementations or later release versions.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Define behavioral compatibility, operation identity, end-to-end budgets and caller-visible unknown outcomes alongside the wire format.

A lost response after commit is compatible with transport failure; blindly replaying a state-changing request may create another effect.

The detailed pages separate the mechanisms that make this decision conditional:

- [API contracts and effect identity](effect-identity.md) — Which promises belong to transport semantics and which require application deduplication?
- [Deadlines, cancellation and retry budgets](deadlines-retries.md) — How should one end-to-end time budget bound nested calls and retries?
- [Behavioral compatibility and interface choice](version-compatibility.md) — Which old/new caller and server combinations must remain valid?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Backend for Frontend (BFF)

**Mechanism and ownership.** A BFF is a separate backend for one client experience,
owned by the frontend team: it customizes the client API and may compose several
service calls, code duplication is a probable outcome, and cross-cutting and domain
logic remain outside the BFF. AWS defines the pattern as "having one backend per user
experience, instead of having only one general-purpose API backend". Microsoft says to
"Create a separate backend service for each frontend interface, instead of using a
single general-purpose backend for all of them" and that the pattern "customizes the
client experience for a specific interface without affecting other interfaces". AWS
summarizes Sam Newman's account: "the BFF is tightly coupled to a specific user
experience, and will typically be maintained by the same team as the user interface".
Microsoft states that "Frontend teams independently manage their own BFF service" and
that "Code duplication is a probable outcome of this pattern. Evaluate the trade-off
between code duplication and a better-tailored experience for each client." It also
says "The BFF service should only handle client-specific logic related to a specific
user experience. Cross-cutting features, such as monitoring and authorization, should
be abstracted to maintain efficiency." Its desktop-BFF example says the service
"aggregates multiple requests by using underlying microservices calls before responding
to the client with a multiple page response". The microservices.io variation "defines a
separate API gateway for each kind of client". These statements support the separate
client-specific backend, team ownership, composition, code-duplication trade-off and
client-specific scope. Tycho guidance, not a source claim: the composition contract is
the explicit list of downstream calls, versions and partial-failure behavior the BFF
exposes to its client, the duplication policy decides where repeated client-specific
logic is acceptable, and domain authority stays with the service that owns the business
rule, so the BFF does not become a second domain authority. Do not use it when one API
contract serves all clients or when the BFF would own core business rules.

**Failure and recovery.** A BFF is tightly coupled to one client experience and released
with it, while the services it composes have independent lifecycles; Tycho guidance,
not a source claim: treat divergence between the BFF composition and the domain API as
drift, version the composition and test the client contract on every release. Microsoft
notes that "Each individual service has its own life cycle, deployment and maintenance
requirements, and security needs." AWS says the BFF's tight coupling is what simplifies
"lining up releases of both the client and server components". Microsoft's reliability
note adds that "When you isolate services to a specific frontend interface, you contain
malfunctions. The availability of one client doesn't affect the availability of another
client's access." Those statements support independent lifecycles, release alignment and
per-client failure containment; they do not document a drift incident, a versioning
scheme or a client-contract test. Tycho guidance, not a source claim: keep the domain
contract as the shared authority rather than copying business rules into the BFF. With
several BFFs, each composition needs its own version, observability and client matrix.

**Alternative.** A shared API with client-side selection is the alternative when the
differences are small and can be expressed without a new authority.

**Limits.** Tycho guidance, not a source claim: a BFF duplicates client-specific policy
and adds a deployable; its contract and client matrix need an owner, and a BFF that
caches or authorizes objects becomes another authority. With several BFFs, each
composition needs a shared domain contract and its own observability; otherwise the
BFFs drift independently.

**Source boundary.** Public pattern pages and a vendor blog, accessed 2026-10-30;
living pages, not a benchmark or an executed drift test.

- Microsoft, "Backends for Frontends pattern", sections "Solution", "Problems and
  considerations", "Workload design" and "Example": canonical text revision
  `0210c2a7732bf3e43621e28c82c284f78fe7f9e02ef2a50328b9d44bcebd353f`, raw HTML
  revision `d391b18b665844a88784473345c8ae88384d46c86e15fdb3557bb92997d6a70f`.
- microservices.io, "API Gateway / Backends for Frontends", section "Variation:
  Backends for frontends": record `read.microservices-api-gateway.2026-10-21`, raw
  revision `e94bf7ae68567226222138dc2836247873d5908b63bf07ca05207377a9999d4d`.
- AWS Front-End Web & Mobile, "Backends for Frontends Pattern", sections "The BFF
  pattern" and "Conclusion": canonical text revision
  `bfab5e7c99406c982f8bddbe077d4e2d5fc3494c6e7ef6762d82d0f3a746280c`, raw HTML
  revision `9290394588cc569f6a8182c5199f39a5ca51fc1ac5d5709a95e9007b491e2f5d`.

### API Composition

An API composition layer calls several owner APIs for one request and assembles their responses into
a single caller-visible result.

microservices.io says to "Implement a query by defining an API Composer, which invokes the
services that own the data and performs an in-memory join of the results." It also notes that
"Some queries would result in inefficient, in-memory joins of large datasets." The pattern page
does not define a freshness format. The composed response must make the partial-or-failed
response policy explicit when a source times out. Azure supports that partial-failure decision.
Tycho synthesis, not a source claim: the per-source freshness format remains Tycho guidance.

One slow or failed participant must not silently disappear from the result; apply per-call
deadlines, mark missing parts or fail the composition explicitly. Azure's Gateway Aggregation
pattern says: "If one or more service calls take too long, it might be acceptable to time out and
return a partial set of data. Consider how your application will handle this scenario." It also
says the aggregation layer "becomes responsible for handling unresponsive back-end services
gracefully and preventing failures from cascading across the aggregated response." For a timeout
or error, Azure says the gateway can "return a partial response when missing data is acceptable,
or it might fail the entire request when complete and consistent order data is required" and that
the team should "Make this decision explicit in the policy design so that clients experience
predictable behavior." Tycho synthesis, not a source claim: the per-call deadline and the
partial-result schema remain Tycho's contract; the Azure page gives policy choices, not an
executed composition test.

**No snapshot.** Tycho synthesis, not a source claim: per-owner reads happen at different times,
so the aggregate can mix owner revisions; it is not a cross-source snapshot, and a caller's
just-committed write may be absent. Read-your-writes needs per-source version/as-of markers or a
read model.

**Query shape.** Tycho synthesis, not a source claim: filtering, sorting and pagination cannot
generally be delegated to owners; the composer over-fetches, joins in memory and must bound
payload, memory and merged-page stability. A maintained read model is often cheaper for repeated
shaped queries.

**Contract boundary.** Microsoft's API design guidance says "A web API that implements versioning
can indicate the features and resources that it exposes, and a client application can submit
requests that are directed to a specific version of a feature or resource." It also says "APIs
that support the inclusion of trace and context information enhance their observability level and
debugging capabilities." Tycho synthesis, not a source claim: the composition endpoint and each
owner adapter need an explicit version and a propagated trace context, because a composed failure
spans several calls.

**Alternative (CQRS; selection rule Tycho synthesis).** Build a maintained read model;
prefer composition when the
sources are authoritative and the caller needs a live view. Tycho synthesis,
not a source claim: reverse the choice when fan-out latency and partial-failure complexity
outweigh the cost of duplicating the data.

**Limits.** Fan-out latency is the max of participants; per-source authorization, versioning and
partial-failure schema are costs, and a maintained read model may be cheaper for repeated
composition. Azure also warns that the gateway "shouldn't introduce service coupling across the
back-end services" and "might introduce a single point of failure (SPoF)." Tycho synthesis, not a
source claim: a composition endpoint is not a transaction.

**Source boundary.** Public pattern and API-design pages, inspected 2026-10-21 and 2026-11-01;
living pages, not a benchmark or an executed composition test. Azure calls the related pattern
Gateway Aggregation; it supports the fan-out/partial-failure policy, not API Composition's
query-join scope.

- microservices.io, "API Composition", sections "Solution", "Resulting context" and "Related
  patterns": record `read.microservices-api-composition.2026-10-21`, raw HTML revision
  `7ec014c171b2421f216c3a82ddb60af0104a2f38e6bb3af93e93c8065f04750b`.
- Microsoft, "Gateway Aggregation pattern", sections "Solution", "Problems and considerations"
  and "Example": canonical text revision
  `b29c820c64a8ea1394113b5afe2152e4ff5e16551ca83fd4498d6c52f14a5f49`, raw HTML revision
  `3dff76ba664fc8089dd7974e55123810bdeaf8e2994acf29ec2dc14c55f17d0a`.
- Microsoft, "Web API design best practices", sections "Implement versioning" and "Enable
  distributed tracing and trace context in APIs": canonical text revision
  `2891e38400bb5898d6905fed7c324f903ef76c5774da5439646fb7e0fa6face0`, raw HTML revision
  `9825b790a5306510791741e08be0e4ade313a173464141cd2103311163d83b27`.
