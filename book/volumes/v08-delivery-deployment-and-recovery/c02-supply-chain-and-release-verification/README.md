---
metadata_version: 1
id: "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c02-supply-chain-and-release-verification/README.md"
title: "V08/C02 — Supply chain and release verification"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How are reproducibility, signatures and promotion controls established? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How are reproducibility, signatures and promotion controls established?"
  prerequisites:
    - "tycho.chapter.8a2d2a79846d4567bb3d33957e19977f"
  related_ids:
    - "tycho.page.38bb8a14ebb54866a7004080318b47e1"
    - "tycho.page.56bd7133980b4b1992816a98308be676"
    - "tycho.page.46fdc865ee574e828bb2e50436587b6b"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](sbom-attestation-and-release-verification.md) | How are reproducibility, signatures and promotion controls established? |
| [Artifact subjects, provenance and component inventories](provenance-subjects.md) | What does each evidence object describe and what does it omit? |
| [Authorized promotion and missing evidence](promotion-authorization.md) | Why is authentic evidence insufficient to authorize an artifact in every environment? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C01 — CI/CD architecture and artifact provenance](../c01-ci-cd-architecture-and-artifact-provenance/README.md) |
| Next | [V08/C03 — VMs, containers, orchestration and serverless](../c03-vms-containers-orchestration-and-serverless/README.md) |
| Prerequisite | [V08/C01 — CI/CD architecture and artifact provenance](../c01-ci-cd-architecture-and-artifact-provenance/README.md) |
| Source reading | [Page-local evidence and versions](sbom-attestation-and-release-verification.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:8 -->
## 8. Public source-to-claim ledger and unperformed verification

| Inspected source (accessed 2026-10-19) | Narrow supported point | Not established |
|---|---|---|
| [SLSA 1.2 specification](https://slsa.dev/spec/v1.2/) and [Build Track Basics](https://slsa.dev/spec/v1.2/build-track-basics) | Distinct Build/Source tracks, provenance and layered build levels | A demonstrated Tycho or fictional project SLSA level |
| [SLSA 1.2 artifact verification](https://slsa.dev/spec/v1.2/verifying-artifacts) | Expected provenance/builder/signature/parameter comparisons | Existence of a deployed verifier or actual policies |
| [SPDX specifications](https://spdx.dev/use/specifications/) | SPDX 3.0 published model and formats | Every SBOM has complete runtime components |
| [CycloneDX specification overview](https://cyclonedx.org/specification/overview/) | BOM format/object identity and versioned serialization | Quality of any generator's output |
| [Sigstore Cosign signature verification](https://docs.sigstore.dev/cosign/verifying/verify/) and [attestation verification](https://docs.sigstore.dev/cosign/verifying/attestation/) | Cryptographic verification plus predicate policy checks | Correct trust-root deployment, authorized release or automatic runtime safety |

The diagrams, failures, candidate designs and validation experiments are original **hypothetical** teaching content. No artifact was built or signed, no tool was executed and no private system was consulted. Compatibility/semantic review and full Tycho editorial acceptance remain open.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:9 -->
## Engineering walkthrough — Authentic artifact, incomplete evidence and denied promotion

**Synthetic release case:** an artifact digest D is accompanied by build provenance referring to D, an SBOM generated from its dependency closure and a signature. Verification succeeds cryptographically but the SBOM omits a dynamically downloaded dependency, while the signer identity is outside the organization's approved builder policy. **No release authorization follows solely from cryptographic validity.**

| Verification question | Required check | Unsafe inference |
|---|---|---|
| Subject | Every attestation identifies the exact immutable digest D | Matching filename is equivalent to matching bytes |
| Builder | SLSA version/track and actual builder identity meet policy | A provenance JSON document proves trusted build execution |
| Dependencies | SBOM format, subject and completeness limits are declared | SPDX/CycloneDX presence proves vulnerability-free code |
| Signing | Certificate/key identity, verification chain and allowed issuer match policy | "Signature valid" means "deployment approved" |
| Deployment | Environment, change authorization and old/new compatibility pass | Artifact integrity guarantees business correctness |

The SLSA 1.2, SPDX, CycloneDX and Sigstore documents cited in this chapter describe distinct evidence classes; they should be used under exact version/verification scope. A missing SBOM can be a hard failure for a regulated release or a documented exception under a more permissive policy—**exception authority must be explicit**, not a silent validator bypass.

**Proposed, not executed:** swap an artifact digest while keeping the original attestation, present an SBOM for another build, sign with an unknown identity and attempt a deployment to a forbidden environment. Assert that authorization fails even where signature parsing succeeds. A reproducible rejection record should state *which gate* failed and what evidence would permit reconsideration, without revealing credentials or granting broad bypass rights.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:10 -->
## Navigation

- Proposed owner V08/C02 in [planned contents](../../../PROPOSED-STRUCTURE.md); current [delivery landing](../../../delivery/README.md).
- Prerequisite: [CI/CD provenance and GitOps](../c01-ci-cd-architecture-and-artifact-provenance/ci-cd-provenance-and-gitops.md).
- Follow-on: [Progressive deployment and schema evolution](../../../delivery/progressive-delivery-and-schema-evolution.md), [safe rollback/recovery](../../../delivery/safe-rollout-and-recovery.md), [security authority and isolation](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md).
<!-- /tycho-question-source -->
