---
metadata_version: 1
id: "tycho.page.38bb8a14ebb54866a7004080318b47e1"
kind: "page"
parent_id: "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c02-supply-chain-and-release-verification/sbom-attestation-and-release-verification.md"
title: "Software supply-chain evidence: SBOM, build attestations and release verification"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated decision and bounded source limits for Supply chain and release verification. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How are reproducibility, signatures and promotion controls established?"
  prerequisites: []
  related_ids:
    - "tycho.page.7921e82a71b9446790f185c818326911"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.56bd7133980b4b1992816a98308be676"
    - "tycho.page.46fdc865ee574e828bb2e50436587b6b"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Software"
    - "supply-chain"
    - "evidence"
    - "SBOM"
    - "build"
    - "attestations"
    - "and"
    - "release"
    - "verification"
evidence_scope:
  source_ids:
    - "src.slsa"
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
<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:-1 -->

# Software supply-chain evidence: SBOM, build attestations and release verification

> **Tycho book manuscript draft V08/C02 (2026-10-19).** Based on independently public SLSA 1.2, SPDX, CycloneDX and Sigstore material. Original synthetic failure examples. No build, signing, scanning, provenance verifier, release policy, or security assessment has been executed for this book. The content_review field retains the decomposition-era draft state; no independent acceptance is asserted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:0 -->
## Purpose and mission

A release is not trustworthy simply because a pipeline succeeded or an artifact carries a signature. A signature can demonstrate a claim was made by a cryptographic identity; a Software Bill of Materials (SBOM) can enumerate components according to its declared scope; an attestation can describe how a particular artifact was built. None of these alone proves the artifact contains no vulnerability, that its dependencies are complete, that the signing identity is allowed to publish it, or that it is safe to deploy against existing state.

This chapter owns the **independent verification chain from actual artifact digest to authorized release decision**. The [CI/CD and GitOps architecture](../c01-ci-cd-architecture-and-artifact-provenance/ci-cd-provenance-and-gitops.md) chapter owns runner topology, promotion flow and reconciliation. [Progressive delivery](../../../delivery/progressive-delivery-and-schema-evolution.md) owns safe exposure and mixed-version data contracts.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Verify artifact identity and provenance against an authorization policy; distinguish signatures, attestations and component inventories.

A valid signature from an unapproved identity, or an SBOM for another digest, must not authorize promotion.

The detailed pages separate the mechanisms that make this decision conditional:

- [Artifact subjects, provenance and component inventories](provenance-subjects.md) — What does each evidence object describe and what does it omit?
- [Authorized promotion and missing evidence](promotion-authorization.md) — Why is authentic evidence insufficient to authorize an artifact in every environment?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
