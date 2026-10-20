---
{
  "metadata_version": 1,
  "id": "tycho.page.df45fc7c08edd5544234864073ea5cc0",
  "kind": "page",
  "parent_id": "tycho.chapter.0bf6cdc27afdb2f2494b82013d92eb73",
  "canonical_path": "book/volumes/v05/c08/access-lifecycle.md",
  "title": "Object capabilities, versions and lifecycle cleanup",
  "topic_ids": [
    "object-storage"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "How are object access, retained versions and cleanup governed after publication?",
  "route_hints": {
    "questions": [
      "How are object access, retained versions and cleanup governed after publication?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.0bf6cdc27afdb2f2494b82013d92eb73"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "object",
      "access",
      "retained",
      "versions",
      "cleanup",
      "governed",
      "after",
      "publication"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.s3-multipart-enrichment",
      "src.gcp-deletion-enrichment"
    ],
    "claim_ids": [],
    "status": "source-linked",
    "notes": "Exact selected passages and source limitations are recorded in the page ledger and dated enrichment inspection record. Synthetic protocols are original design reasoning."
  },
  "content_review": {
    "status": "self-checked",
    "reviewed_at": "2026-10-20",
    "reviewer": "Codex enrichment author; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-20",
  "updated_at": "2026-10-20",
  "source_inspection_date": "2026-10-20",
  "content_verified_at": null
}
---

# Object capabilities, versions and lifecycle cleanup

**Owning question:** How are object access, retained versions and cleanup governed after publication?

## Address, access and retention are different properties

An object key names a storage location. An unguessable key is not a complete authorization design. A temporary download capability may permit use until its expiry under the service's validation rules; revoking a catalogue permission does not automatically invalidate every issued capability. State whether immediate revocation, bounded exposure or public distribution is required.

**Original fictional requirement:** workshop attendees can download a recording for seven days, while the owner can retire it immediately from the catalogue. A temporary bearer link valid for the whole seven days cannot satisfy immediate retirement unless another enforcement point rechecks current permission. Options include short-lived capabilities, an authorizing proxy or a documented revocation mechanism with an acceptable propagation bound. Shorter validity increases renewal traffic and dependence on the issuer.

## Publication-to-retirement protocol

Store the object version, authorized owner, publication status and lifecycle policy in authoritative metadata. Resolve the current caller before minting a capability; restrict its object/action scope and lifetime. Do not place tokens in general telemetry. Downstream caches must follow the same exposure contract.

~~~mermaid
stateDiagram-v2
    [*] --> Published
    Published --> Hidden: Revoke new catalogue access
    Hidden --> Retained: Existing retention obligation
    Hidden --> Deleting: Removal authorized
    Retained --> Deleting: Policy permits removal
    Deleting --> Removed: Required copies and versions accounted for
    Deleting --> RepairRequired: Copy or key evidence missing
~~~

Text alternative: hiding a catalogue entry is immediate application behavior; removal may require separate decisions about versions, derived objects and retained copies. This original policy model is not a universal provider lifecycle guarantee.

## What a deletion inventory must contain

Account for current and noncurrent versions, previews, transcodes, temporary parts, replication targets, edge caches, search references and backups. A current-name delete may have different semantics from removal of all retained versions. Provider-specific versioning, object-lock, expiry and capability rules require exact additional documentation before an implementation recipe is selected.

A reference collector should distinguish an abandoned candidate from a published version that is temporarily absent from one index snapshot. Use metadata-owned retirement and a bounded grace process; do not delete on an eventually consistent secondary index's absence alone. See [cross-store publication](publication-consistency.md).

## Original cost and failure comparison

Assume 1,000 GiB of authoritative recordings and three equally large derived renditions. The initial stored footprint is 4,000 GiB before replication, versions, incomplete parts or backups. This illustrative multiplication says nothing about an actual bill. Add request, retrieval, egress, transform and recovery costs, especially when an archival class delays restores.

A leaked capability is a security event, not a cache miss. A missing key can make encrypted data unavailable even when every byte replica is healthy. A failed cleanup can accumulate cost while the UI reports success. Define separate metrics for retired references, pending physical deletion, orphan candidates and inaccessible-but-retained payloads.

## Evidence and acceptance

The inspected [Multipart upload overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) supports multipart storage cleanup obligations. General lifecycle/version/capability behavior above is original requirements analysis; no universal S3-compatible behavior or immediate provider erasure is claimed. Read [cross-store deletion](../c06/migration-retirement.md#deletion-across-derived-state-and-restored-backups) and [key recovery](../../v09/c05/object-credentials.md#key-rotation-revocation-and-unavailable-authorities).

Proposed tests: retirement while a capability remains valid, cleanup concurrent with publication, an older retained version, delayed rendition deletion and restoration from a pre-retirement backup. Require the declared visible/access contract before asserting deletion complete.

## Navigation

Parent: [object chapter](README.md). Previous: [publication](publication-consistency.md). Continue to [edge cache](../../v08/c08/edge-cache-origin.md) and [backup/restore](../c07/README.md).
