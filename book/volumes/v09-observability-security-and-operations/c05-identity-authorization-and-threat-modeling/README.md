---
metadata_version: 1
id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/README.md"
title: "V09/C05 — Identity, authorization and threat modeling"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Where do trust boundaries and permission checks have to sit? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Where do trust boundaries and permission checks have to sit?"
  prerequisites:
    - "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
  related_ids:
    - "tycho.chapter.5426707ddf264b758016aafe71f342b7"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.e9524931fbcc4b4e833f6b0465a27698"
    - "tycho.page.43bf5d29ec5b4327b0c4cf57391679da"
    - "tycho.page.96c78f4525504257baf5861e2397dab8"
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
updated_at: "2026-10-22"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision](identity-authorization-and-isolation.md) | Where do trust boundaries and permission checks have to sit? |
| [Threat models and authenticated identity](threat-identity.md) | Which asset and principal are protected and what does authentication establish? |
| [Object permission, credentials and isolation](object-credentials.md) | Where must resource authorization be enforced across direct and indirect paths? |
| [Synthetic attacks and decision gates](security-tests.md) | Which denied or confused-deputy outcome would invalidate the design? |

## Boundaries and further reading

- [V02/C07 — Authorization boundaries and multitenancy](../../v02-application-boundaries-and-contracts/c07-authorization-boundaries-and-multitenancy/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C04 — Logging, audit and lineage](../c04-logging-audit-and-lineage/README.md) |
| Next | [V09/C06 — Incident response and operational change](../c06-incident-response-and-operational-change/README.md) |
| Prerequisite | [V09/C04 — Logging, audit and lineage](../c04-logging-audit-and-lineage/README.md) |
| Source reading | [Page-local evidence and versions](identity-authorization-and-isolation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

The 2026-10-19 date in the source table is the chapter baseline inspection date. The landing itself
does not claim a new page-level source inspection, and `source_inspection_date` remains null.


## Further mechanism and recovery questions

- [Key rotation, revocation and unavailable authorities](object-credentials.md#key-rotation-revocation-and-unavailable-authorities) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:8 -->
## 8. Exact public source evidence

| Ref | Primary source and inspected section, 2026-10-19 | Validity boundary |
|---|---|---|
| E01 | [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/), published revision and [authentication assurance](https://pages.nist.gov/800-63-4/sp800-63b/aal/) | Relevant digital identity/auth assurance concepts, not an achieved compliance claim |
| E02 | [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), *Deny by Default* and *Validate Permissions on Every Request* | Preventive design guidance, not proof every route is enforced |
| E03 | [OWASP Authorization Patterns](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Patterns_Cheat_Sheet.html), PEP/PDP/service-level authorization | Enforcement/decision separation, not an installed reference policy engine |
| E04 | [OWASP API Security Top 10, 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/), API1/API3 categories | Risk classification, not a discovered vulnerability in Tycho |
| E05 | [RFC 9700 OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html), token privileges, sender constraint and refresh-token handling | OAuth-specific recommendations, not generic correctness guarantees for every identity protocol |

No operating security policy, cryptographic key, production attack test, formal threat assessment, independent auditor or penetration test has been implemented or carried out. This is a conceptual engineering chapter with falsifiable checks, not a certified deployment.
<!-- /tycho-question-source -->
