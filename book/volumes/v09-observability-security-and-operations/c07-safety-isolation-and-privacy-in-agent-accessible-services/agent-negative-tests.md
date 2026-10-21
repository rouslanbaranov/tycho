---
metadata_version: 1
id: "tycho.page.b38397b1d9fe456dbdb30e5b2ec2f3c8"
kind: "page"
parent_id: "tycho.chapter.5b8edae85f83413997cac0c873919b57"
canonical_path: "book/volumes/v09-observability-security-and-operations/c07-safety-isolation-and-privacy-in-agent-accessible-services/agent-negative-tests.md"
title: "Negative access tests and architecture limits"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Which denial or unavailable-evidence outcome must an agent-accessible service preserve?"
route_hints:
  questions:
    - "Which denial or unavailable-evidence outcome must an agent-accessible service preserve?"
  prerequisites:
    - "tycho.page.7987026eace9417a8c3a1d4dbc6c7da0"
  related_ids:
    - "tycho.chapter.5b8edae85f83413997cac0c873919b57"
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "agent"
    - "negative"
    - "tests"
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
# Negative access tests and architecture limits

**Owning question:** Which denial or unavailable-evidence outcome must an agent-accessible service preserve?

This page belongs to [V09/C07 — Safety, isolation and privacy in agent-accessible services](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.0ae1aabac3b64c2f924cc427684bdbab:6 -->
## 6. A synthetic negative test matrix

| Attack or failure scenario | Correct server behavior | What does not prove it |
|---|---|---|
| Unauthorized document ID obtained from a citation | Deny reading/metadata for that subject | Hiding it from ranking only |
| A note contains adversarial instructions | Treat as untrusted document content; no change in tool privilege | Simple instruction "do not obey" without access gates |
| Model requests write through a search tool | Refuse unsupported operation; side-effect API not present | Assuming "read-only" because UI shows only a search box |
| Cached snippet from a different scope | Do not serve data outside entitled scope | Cache hit ratio or successful authentication |
| Outdated source reference | Mark snapshot/verification status and request fresh evidence | Date string without source revision |
| Arbitrary file path passed as document ID | Restrict to approved stable IDs and root; reject escape or symlink traversal | String suffix check without canonical path resolution |
| Model-generated malformed action arguments | Reject by deterministic schema and access-policy checks | Model's promise to send correct JSON |
| Excessive requests or output sizes | Enforce size, time, rate and result bounds; degrade predictably | Generic cloud resource limits alone |
| Incident logs contain secrets | Redact/deny, limit retention and audit access | Encrypting storage without data minimization |

An executable service should test denial cases end-to-end, with independent authorization configurations and synthetic restricted fixtures. Passing a boundary checker is evidence only for the tested patterns, not universal proof of safety.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ae1aabac3b64c2f924cc427684bdbab:7 -->
## 7. Architecture decision and limits

**Default recommendation for an external documentation service:** scoped, read-only retrieval with server-side document authorization, bounded section results, immutable source IDs, versioned citations and no arbitrary tools. When a user asks for a consequential architecture decision, supply relevant source evidence, uncertainty and alternatives. Do not grant automatic deployment/change authority to the same agent merely because it could find the correct chapter.

A full MCP implementation, client interoperability, OAuth/transport design, host protection, and response-size benchmarks are **separate software engineering and security validation tasks**. The book only documents the reasoning contract. No production mechanism, security evaluation, malicious-input exercise or human approval was executed as part of this page.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](collection-privacy.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](safe-agent-access-and-knowledge-isolation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
