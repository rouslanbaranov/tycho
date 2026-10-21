---
metadata_version: 1
id: "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
kind: "page"
parent_id: "tycho.chapter.5b8edae85f83413997cac0c873919b57"
canonical_path: "book/volumes/v09-observability-security-and-operations/c07-safety-isolation-and-privacy-in-agent-accessible-services/safe-agent-access-and-knowledge-isolation.md"
title: "Safe agent-accessible knowledge: trust boundaries, privacy and bounded authority"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Integrated question, original scenario and transfer limits for Safety, isolation and privacy in agent-accessible services. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What can remote readers infer or retrieve under bounded permissions?"
  prerequisites: []
  related_ids:
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.3870e6370654489c949e098b9acd1840"
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.page.6315cc62b4384a64b31f8694d77d1c35"
    - "tycho.page.7987026eace9417a8c3a1d4dbc6c7da0"
    - "tycho.page.b38397b1d9fe456dbdb30e5b2ec2f3c8"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Safe"
    - "agent-accessible"
    - "knowledge"
    - "trust"
    - "boundaries"
    - "privacy"
    - "and"
    - "bounded"
    - "authority"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.0ae1aabac3b64c2f924cc427684bdbab:-1 -->

# Safe agent-accessible knowledge: trust boundaries, privacy and bounded authority

> **Tycho book draft V09/C07**, 2026-10-19. This is **System Design education**, not a deployed agent, authentication service, retrieval API, MCP adapter or security validation. Examples and policies are original and fictional; source-bound recommendations draw on public OWASP guidance.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ae1aabac3b64c2f924cc427684bdbab:0 -->
## Purpose and mission

A knowledge service becomes agent-accessible when software can retrieve snippets and, potentially, request actions based on their contents. The architectural problem is not whether the language model is "trusted" as a person. It is how the system **enforces identity, resource authorization, data provenance and the permitted effects of tool calls regardless of the model's interpretation**.

Retrieved documents can contain inaccurate claims, stale revisions or text explicitly designed to change an assistant's behavior. An external paragraph must never acquire the authority of application instructions merely because it appeared in a tool result. [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) explains direct and indirect instruction-manipulation risk, and that retrieval augmentation does not remove it. [OWASP LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) identifies excessive tool functionality, permissions and autonomy as independent amplification factors.

This chapter discusses the *general* architecture of an agent-facing service. Tycho's actual ranked search, transport adapter and shared specialist are separate future product deliverables, not claimed implemented here.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Enforce caller permissions, collection boundaries and bounded tool effects independently of retrieved text.

Relevant source text may contain instructions; retrieval must not grant it authority to execute actions or cross data boundaries.

The detailed pages separate the mechanisms that make this decision conditional:

- [Principals, retrieval and bounded tool effects](principal-tools.md) — Which boundary prevents retrieved instructions from acquiring execution authority?
- [Collection identity, privacy and retention](collection-privacy.md) — Which content and metadata may each caller observe across snapshots?
- [Negative access tests and architecture limits](agent-negative-tests.md) — Which denial or unavailable-evidence outcome must an agent-accessible service preserve?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
