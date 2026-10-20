---
metadata_version: 1
id: "tycho.chapter.5b8edae85f83413997cac0c873919b57"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09/c07/README.md"
title: "V09/C07 — Safety, isolation and privacy in agent-accessible services"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What can remote readers infer or retrieve under bounded permissions?"
route_hints:
  questions:
    - "What can remote readers infer or retrieve under bounded permissions?"
  prerequisites:
    - "tycho.chapter.691463ecbf6f44af84274ab3ff798b3d"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
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

# V09/C07 — Safety, isolation and privacy in agent-accessible services

## Purpose and mission

What can remote readers infer or retrieve under bounded permissions? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Enforce caller permissions, collection boundaries and bounded tool effects independently of retrieved text.

Relevant source text may contain instructions; retrieval must not grant it authority to execute actions or cross data boundaries. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Safe agent-accessible knowledge: trust boundaries, privacy and bounded authority](safe-agent-access-and-knowledge-isolation.md) | What can remote readers infer or retrieve under bounded permissions? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Define distinct security principals](safe-agent-access-and-knowledge-isolation.md#1-define-distinct-security-principals).
- [2. Treat retrieval as a data pipeline, not a command channel](safe-agent-access-and-knowledge-isolation.md#2-treat-retrieval-as-a-data-pipeline-not-a-command-channel).
- [7. Architecture decision and limits](safe-agent-access-and-knowledge-isolation.md#7-architecture-decision-and-limits).
- [8. Public evidence ledger and navigation](safe-agent-access-and-knowledge-isolation.md#8-public-evidence-ledger-and-navigation).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C06 — Incident response and operational change](../c06/README.md) |
| Next | [V10/C01 — Architecture requirement and workload profiles](../../v10/c01/README.md) |
| Prerequisite | [V09/C06 — Incident response and operational change](../c06/README.md) |
| Source reading | [Page-local evidence and versions](safe-agent-access-and-knowledge-isolation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
