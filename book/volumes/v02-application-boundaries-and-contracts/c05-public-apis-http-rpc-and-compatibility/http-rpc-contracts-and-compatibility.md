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
updated_at: "2026-10-21"
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
> [Backend for Frontend](../../v11-pattern-atlas/c02-api-communication/README.md#backend-for-frontend-bff) — decision conditions and contraindications.
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

A backend for frontend composes the API surface for one client experience. It needs a
client owner, a composition contract, a policy for duplicated domain logic and a boundary
that prevents the BFF from becoming a second domain authority. Use it when clients need
materially different payloads, latency budgets or release cadences. Do not use it when one
API contract serves all clients or when the BFF would own core business rules.

The failure path is drift between the BFF and the domain API; version the composition and
test the client contract. A shared API with client-side selection is the alternative when
the differences are small and can be expressed without a new authority.

**Limits.** A BFF duplicates client-specific policy and adds a deployable; its contract and
client matrix need an owner, and a BFF that caches or authorizes objects becomes another
authority.

### API Composition

An API composition layer calls several owner APIs for one request and assembles their responses into
a single caller-visible result. The composed response must declare per-source freshness and what
partial failure means, rather than presenting one aggregate result as uniformly current.

One slow or failed participant must not silently disappear from the result; apply per-call
deadlines, mark missing parts or fail the composition explicitly. Build a maintained read model or a
client-specific backend for frontend; prefer composition when the sources are authoritative and the
caller needs a live view.

**Limits.** Fan-out latency is the max of participants; per-source authorization, versioning
and partial-failure schema are costs, and a maintained read model may be cheaper for repeated
composition. A composition endpoint is not a transaction.
