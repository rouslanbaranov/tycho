---
metadata_version: 1
id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09/c05/README.md"
title: "V09/C05 — Identity, authorization and threat modeling"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Where do trust boundaries and permission checks have to sit?"
route_hints:
  questions:
    - "Where do trust boundaries and permission checks have to sit?"
  prerequisites:
    - "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
  related_ids:
    - "tycho.chapter.5426707ddf264b758016aafe71f342b7"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.oauth-security"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V09/C05 — Identity, authorization and threat modeling

## Purpose and mission

Where do trust boundaries and permission checks have to sit? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Place identity and resource authorization at the actual effect boundary, including object, tenant and credential scope.

Network reachability or a valid token does not grant permission to every object; test denied operations through indirect paths. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Threat boundaries, identity, authorization and service isolation](identity-authorization-and-isolation.md) | Where do trust boundaries and permission checks have to sit? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Start with protected outcomes and an explicit threat model](identity-authorization-and-isolation.md#1-start-with-protected-outcomes-and-an-explicit-threat-model).
- [2. Authentication is not authorization](identity-authorization-and-isolation.md#2-authentication-is-not-authorization).
- [7. Verification and decision gates](identity-authorization-and-isolation.md#7-verification-and-decision-gates).
- [8. Exact public source evidence](identity-authorization-and-isolation.md#8-exact-public-source-evidence).

## Boundaries and further reading

- [V02/C07 — Authorization boundaries and multitenancy](../../v02/c07/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C04 — Logging, audit and lineage](../c04/README.md) |
| Next | [V09/C06 — Incident response and operational change](../c06/README.md) |
| Prerequisite | [V09/C04 — Logging, audit and lineage](../c04/README.md) |
| Source reading | [Page-local evidence and versions](identity-authorization-and-isolation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
