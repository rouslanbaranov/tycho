---
metadata_version: 1
id: "tycho.page.de9c5bc478ba44718fcb731e69109dce"
kind: "page"
parent_id: "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
canonical_path: "book/volumes/v02/c05/version-compatibility.md"
title: "Behavioral compatibility and interface choice"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Which old/new caller and server combinations must remain valid?"
route_hints:
  questions:
    - "Which old/new caller and server combinations must remain valid?"
  prerequisites:
    - "tycho.page.43414664520b4866929f7f006f27f59b"
  related_ids:
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "version"
    - "compatibility"
evidence_scope:
  source_ids:
    - "src.http-semantics"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.cccbd188936543a2aaf904f4002236d8; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Behavioral compatibility and interface choice

**Owning question:** Which old/new caller and server combinations must remain valid?

This page belongs to [V02/C05 — Public APIs, HTTP/RPC and compatibility](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:4 -->
## 4. Version compatibility is behavioral and asymmetric

A versioned schema is necessary for safe evolution, but not sufficient. A new server reading an old client may behave differently from an old server reading a new client; adding a field can be wire-safe while becoming a required business value that an old caller cannot supply.

| Mixed-version pairing | Representative change | Required experiment |
|---|---|---|
| Old client → new server | New optional response field | Check old decoder and old business interpretation |
| New client → old server | Newly sent request field | Check whether field is ignored, rejected or changes semantics |
| Old client → new server | New mandatory authorization or consistency rule | Confirm whether old requests retain authorized meaning |
| New client → old server | New enum value or error type | Test explicit unknown-value fallback |
| Canary client/server mix | New stream/message ordering or timeout | Exercise mixed-version failure and recovery |
| Rollback after a data change | New persistent schema and job state | Confirm old code can read/write or perform planned forward repair |

Protocol Buffers represent fields on the wire by numbered tags. The [official Protocol Buffers editions guide](https://protobuf.dev/programming-guides/editions/) and [schema best practices](https://protobuf.dev/best-practices/dos-donts/) document why a removed field number should not be reused and why preserving wire parsing can still involve semantic or lossy behavior. Reserve retired numbers, and assess field presence, defaults, enums and JSON mapping in the actual configured language/runtime. Do not call an entire protobuf change compatible solely because it parses.

For HTTP JSON consumers, explicitly test required/unknown fields, removed enum values, null versus absent, changed units, pagination ordering, date interpretation and error-contract evolution. For either protocol, distinguish **wire-parse compatibility**, **semantic compatibility**, and **operational coexistence** over the real deployment and rollback window.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:5 -->
## 5. Which interface approach fits the decision?

| Option | Often justified by | Additional questions / contraindications |
|---|---|---|
| HTTP resource API | Broad client ecosystem, caching or resource-oriented semantics, independently documented HTTP contracts | Does a command have durable identity? Are cache/auth/status semantics correct? |
| gRPC unary RPC | Strongly typed service contracts, generated clients and explicit RPC deadline/cancellation/retry tools | Are all clients/platforms supported? What happens under reconnect or changing proto fields? |
| gRPC streaming | Long-lived ordered message exchanges and flow-control semantics needed by the application | What are cancellation, backpressure, reconnect and replay requirements? |
| Async command + status query | Work exceeds request deadline or needs durable acceptance and recovery | Who owns durable state, deduplication, user status and cleanup? |
| In-process call | Same deployable failure boundary and no justified remote contract | Would network transport add failure modes without useful independent ownership? |

These are **conditions**, not a global ranking. A synchronous RPC is not a replacement for a durable job workflow when work outlives the caller. A document schema does not fix a missing retry invariant. Local module calls remain viable when separate deployment has no measured benefit.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:6 -->
## 6. Testable acceptance and negative evidence

For each interface revision, document a concrete version/behavior matrix and exercise at least:

1. Old/new client against old/new server for intended versions and rollback skew.
2. Acknowledgment loss after effect commit, duplicates with identical and conflicting keys, restart across the deduplication boundary.
3. Deadline expiration before and after durable commit; cancellation propagation and cleanup of spawned work.
4. Retry storm/overload bounds, persistent failure and server pushback; retries must not cause unchecked multiplicative load.
5. Unknown fields/enum values, missing optional fields and newly strict validation.
6. Distinct authorization identities and scoped deduplication keys; never leak another principal's operation outcome.
7. Forward recovery after data/schema evolution, including an irreversible-effect boundary.

A passing OpenAPI checker, protobuf compilation or isolated happy-path unit test **cannot** establish all seven. Use contract-test fixtures, pairwise version tests and deliberately injected failures. Where untested, state the unresolved guarantee.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](deadlines-retries.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](http-rpc-contracts-and-compatibility.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
