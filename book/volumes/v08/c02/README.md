---
metadata_version: 1
id: "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08/c02/README.md"
title: "V08/C02 — Supply chain and release verification"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How are reproducibility, signatures and promotion controls established?"
route_hints:
  questions:
    - "How are reproducibility, signatures and promotion controls established?"
  prerequisites:
    - "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.slsa"
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

# V08/C02 — Supply chain and release verification

## Purpose and mission

How are reproducibility, signatures and promotion controls established? This chapter owns that question within delivery, deployment and disaster recovery. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Verify artifact identity and provenance against an authorization policy; distinguish signatures, attestations and component inventories.

A valid signature from an unapproved identity, or an SBOM for another digest, must not authorize promotion. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Software supply-chain evidence: SBOM, build attestations and release verification](sbom-attestation-and-release-verification.md) | How are reproducibility, signatures and promotion controls established? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Distinguish evidence objects and subjects](sbom-attestation-and-release-verification.md#1-distinguish-evidence-objects-and-subjects).
- [2. SLSA 1.2: levels and provenance have explicit scopes](sbom-attestation-and-release-verification.md#2-slsa-12-levels-and-provenance-have-explicit-scopes).
- [8. Public source-to-claim ledger and unperformed verification](sbom-attestation-and-release-verification.md#8-public-source-to-claim-ledger-and-unperformed-verification).
- [Engineering walkthrough — Authentic artifact, incomplete evidence and denied promotion](sbom-attestation-and-release-verification.md#engineering-walkthrough-authentic-artifact-incomplete-evidence-and-denied-promotion).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C01 — CI/CD architecture and artifact provenance](../c01/README.md) |
| Next | [V08/C03 — VMs, containers, orchestration and serverless](../c03/README.md) |
| Prerequisite | [V08/C01 — CI/CD architecture and artifact provenance](../c01/README.md) |
| Source reading | [Page-local evidence and versions](sbom-attestation-and-release-verification.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
