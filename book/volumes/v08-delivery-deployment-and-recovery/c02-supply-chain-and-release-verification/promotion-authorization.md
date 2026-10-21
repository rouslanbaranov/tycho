---
metadata_version: 1
id: "tycho.page.46fdc865ee574e828bb2e50436587b6b"
kind: "page"
parent_id: "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c02-supply-chain-and-release-verification/promotion-authorization.md"
title: "Authorized promotion and missing evidence"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Why is authentic evidence insufficient to authorize an artifact in every environment?"
route_hints:
  questions:
    - "Why is authentic evidence insufficient to authorize an artifact in every environment?"
  prerequisites:
    - "tycho.page.56bd7133980b4b1992816a98308be676"
  related_ids:
    - "tycho.chapter.92bd770bf87d4d6c9ab6e71cfa291132"
    - "tycho.page.38bb8a14ebb54866a7004080318b47e1"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "promotion"
    - "authorization"
evidence_scope:
  source_ids:
    - "src.slsa"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.38bb8a14ebb54866a7004080318b47e1; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Authorized promotion and missing evidence

**Owning question:** Why is authentic evidence insufficient to authorize an artifact in every environment?

This page belongs to [V08/C02 — Supply chain and release verification](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:4 -->
## 4. Authenticity is not authorization

[Sigstore Cosign verification guidance](https://docs.sigstore.dev/cosign/verifying/verify/) covers signature verification using explicit keys or OIDC-issued certificate identity and issuer constraints. [Sigstore in-toto attestation guidance](https://docs.sigstore.dev/cosign/verifying/attestation/) explains verification of signed predicates and policy checking. Real deployments must pin compatible tool, format, issuer/trust-root and verification policies; examples in live documentation may change.

**Hypothetical authorization failure:** a CI account from an unapproved fork signs an artifact correctly. Cryptographic verification succeeds, but the signing identity, builder/source revision or environment target is not on the release allowlist. The proper outcome is **reject**, not “valid signature means approved”.

A verification gate should bind:
1. Exact subject digest of the artifact being promoted.
2. Signature authenticity and supported algorithm/trust-root/certificate chain.
3. Allowed issuer, signing workflow/builder and expected identity claims; expiry/revocation where applicable.
4. Approved source repository and immutable source revision (or explicit policy-matched provenance materials).
5. Expected build parameters and dependency/source policy, with known optional fields documented.
6. SBOM identity/format and integrity; vulnerability/license gates according to an explicit policy.
7. Named target/environment eligibility and mixed-version runtime/data safety *before exposure*.
8. Recorded evidence IDs, timestamp, decision and a failure/exception process that does not silently weaken the gate.

A public transparency log provides a different property from an authorization policy. An entry's existence can support accountability or inclusion verification; it does not approve the publisher's authority, nor ensure that every missing attestation was ever submitted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:5 -->
## 5. Missing evidence must fail the gate appropriately

| Failure scenario | Superficial green signal | Required policy behavior |
|---|---|---|
| Signed artifact with wrong digest | Signature verification on unrelated object | Refuse digest mismatch; bind subject to actual bytes |
| Valid signature by unauthorized identity | Cryptographic check passed | Reject issuer/identity/source or target policy mismatch |
| Provenance references mutable branch only | Branch exists and CI is green | Require immutable source identity appropriate to the policy |
| SBOM generated for source, not released image | Scanner says no finding | Record coverage gap; verify final built object |
| Attestation omitted or deleted | Other checks happened to pass | Required proof absent → reject or explicit controlled exception |
| Signature service unavailable | Build and unit tests passed | Do not auto-disable verification; hold candidate |
| Old critical scan database | Last scan green | Record freshness window and re-evaluate under policy |
| New image incompatible with persisted state | Build integrity is good | Block rollout until schema/data coexistence and recovery gates pass |

SLSA Build L2 or L3 should not be inferred from a custom script merely writing a JSON file. Provenance authenticity and isolation controls matter; implementation requires evaluating the *actual* build platform against the published track requirements.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:6 -->
## 6. Original worked decision: controlled artifact promotion

**Fictional project:** a small open-source photo-gallery server releases a versioned container image and a command-line package. Both are built from the same source revision but with distinct toolchains and artifact bytes. The team wants to promote a digest to a new environment.

Candidate A trusts the image tag, an unscoped signature and a successful unit-test job. Candidate B records the container digest, source revision, builder provenance, relevant SBOM coverage, policy decision and target-runtime compatibility before approval.

B provides a stronger **potential verification design**, conditional on actual enforcement and absence of bypasses. A is unsuitable if the release policy requires traceable bytes and limited promotion authority. B is not necessarily equivalent to SLSA Build L3; its implementation, builder isolation, provenance producer and policy enforcement still need an independently reviewed assessment.

**Falsifiable experiment (not executed):** retag an image to a different digest; present a genuine signature from an unauthorized CI identity; delete a required provenance attachment; use an SBOM whose subject digest is the previous release. The verifier should reject each mismatch, without permitting deployment through an alternate unguarded entry point. Positive tests should accept only artifacts satisfying the explicitly recorded policy.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.38bb8a14ebb54866a7004080318b47e1:7 -->
## 7. A release gate belongs outside the artifact itself

The party that built the artifact should not be the sole authority deciding that its own output is trustworthy. Independent policy evaluation can be applied at promotion, registry ingestion or target runtime admission, with multiple gates for high-impact changes. Any gate needs reliable identity, time/scoped evidence and audit of exceptions. If deployment tools can bypass it directly, the mechanism is advisory rather than enforced.

The final release decision additionally checks runtime and data outcomes. A fully traceable container that drops committed events, serves unauthorized records or corrupts stored data is not a safe release. The [safe rollout/recovery](../../../delivery/safe-rollout-and-recovery.md) page owns these post-build validity gates.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](provenance-subjects.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](sbom-attestation-and-release-verification.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
