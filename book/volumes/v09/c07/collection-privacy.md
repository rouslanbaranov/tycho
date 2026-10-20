---
metadata_version: 1
id: "tycho.page.7987026eace9417a8c3a1d4dbc6c7da0"
kind: "page"
parent_id: "tycho.chapter.5b8edae85f83413997cac0c873919b57"
canonical_path: "book/volumes/v09/c07/collection-privacy.md"
title: "Collection identity, privacy and retention"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Which content and metadata may each caller observe across snapshots?"
route_hints:
  questions:
    - "Which content and metadata may each caller observe across snapshots?"
  prerequisites:
    - "tycho.page.6315cc62b4384a64b31f8694d77d1c35"
  related_ids:
    - "tycho.chapter.5b8edae85f83413997cac0c873919b57"
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
    - "tycho.page.b38397b1d9fe456dbdb30e5b2ec2f3c8"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "collection"
    - "privacy"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.0ae1aabac3b64c2f924cc427684bdbab; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Collection identity, privacy and retention

**Owning question:** Which content and metadata may each caller observe across snapshots?

This page belongs to [V09/C07 — Safety, isolation and privacy in agent-accessible services](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.0ae1aabac3b64c2f924cc427684bdbab:4 -->
## 4. Versioned provenance and cross-collection isolation

A reference result should identify:
- immutable or revision-bound knowledge snapshot and document ID;
- bounded section/range and canonical local/public source reference;
- evidence confidence and verification freshness as separate states;
- authorization scope and whether a linked source was actually inspected;
- relevant contradictions, missing support or version mismatch.

Indexes, caches and citations are alternate **views of the same authorized content**, not independent permissions. A cache key must reflect principal/tenant scopes or serve only deliberately public results. A search index built from multiple collections must never turn a cross-collection link into permission to read the linked target. "Related document" is a navigation hint, not an ACL bypass.

When a source document changes, stale snippets and old citations may no longer support a decision. Snapshot pinning, versioned document IDs and eventual re-indexing reduce accidental mismatch, but a pinned result alone cannot certify semantic truth. The caller still needs the authoritative source when making consequential architectural claims.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ae1aabac3b64c2f924cc427684bdbab:5 -->
## 5. Privacy, audit and retention boundaries

Agent interactions may include user questions, selected snippets, query filters, result IDs, tool traces and tool arguments. These records can reveal interests or sensitive content even if the book prose itself is public. A reference design should:
- minimize retained query/input text and avoid logging credentials, tokens or raw confidential documents;
- define what metadata is necessary for incident diagnosis and abuse detection;
- limit audit access and retention, and allow investigation without exporting private content indiscriminately;
- label and redact any untrusted remote source content appropriately, rather than treating it as safe to publish;
- prevent generated summaries or prompts from mixing restricted collections or leaking source metadata;
- separate operational observability (latency, errors, sizes) from authorization and audit evidence (decision, principal, object and outcome).

[Tycho trace, logs and audit chapter](../../../observability/trace-context-lineage-and-audit.md) explains why sampled tracing is not an authoritative audit trail. [Tycho security boundaries](../c05/identity-authorization-and-isolation.md) describes object-level authorization and isolation independent of agent-specific prompts.


### Worked cross-tenant retrieval failure: a valid citation is not a permission

**Original fictional scenario:** two engineering teams, A and B, share an index. The agent for A is authenticated and may read public pages and A's private notes, but not B's. A public page includes a Markdown link to a B-only incident and a previously cached citation ID. The search result for that public page is allowed; following its link is **not** a grant to access B's target.

| Step | Authority and required check | Failure if omitted |
|---|---|---|
| Query and initial ranking | Validate caller and restrict candidate visibility *before exposing* titles, snippets and counts | A learns the existence or title of B's private incident |
| Follow related citation | Resolve stable target ID, verify target access **again** under caller A | A public source launders a B-only document into authorized content |
| Read cached snippet | Cache key includes effective collection/object entitlement and snapshot, or is demonstrably public | B's previously cached text is returned to A |
| Summarize and cite | Only permitted text, source identity and revision may support the answer | Answer or "supporting evidence" leaks B's restricted assertion |
| Agent asks to perform a write | An independent action authority requires its own ACL and explicit effect contract | Text inside B's note induces a privileged tool invocation |

A deliberately untrusted retrieved note says, in the fictional scenario, that a reviewer should follow a protected URL before answering. **That instruction remains data**; it cannot override access policy. Merely telling the language model to ignore injection is insufficient. Every document/section-level read must pass deterministic authorization, regardless of how the agent reached it. The [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) supports deny-by-default and resource-level enforcement principles; it does not certify this unimplemented design.

**Failure/recovery:** revoke A's access to a document between the initial search and an expansion. The next read must be denied; stale route hints and cached snippets must not bypass the new policy. Record a security event containing minimally necessary principal/object identifiers without copying private content into general telemetry. A correct response can cite *only* allowed sources or state that required evidence is inaccessible—never disclose the forbidden source to justify refusal.

**Proposed negative test, not executed:** use two tenant identities, shared index/cache, a public-to-private cross-link, delayed ACL update, forged citation ID and an injected tool directive. Require zero unauthorized result/metadata exposure and zero unauthorized writes before considering ranked retrieval correct. No hosted Tycho MCP service, model agent, authorization deployment or penetration test exists from this chapter.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](principal-tools.md) |
| Next | [Continue the reasoning](agent-negative-tests.md) |
| Integrated question | [Original scenario and limits](safe-agent-access-and-knowledge-isolation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
