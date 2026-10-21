---
{
  "metadata_version": 1,
  "id": "tycho.page.55e76c3f0ab496d04873ae3a1e52bf3f",
  "kind": "page",
  "parent_id": "tycho.chapter.0bf6cdc27afdb2f2494b82013d92eb73",
  "canonical_path": "book/volumes/v05-data-models-engines-and-lifecycle/c08-object-storage-large-transfers-and-publication/publication-consistency.md",
  "title": "Object publication and cross-store reconciliation",
  "topic_ids": [
    "object-storage"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "When may an application expose uploaded bytes if object storage and metadata do not share a transaction?",
  "route_hints": {
    "questions": [
      "When may an application expose uploaded bytes if object storage and metadata do not share a transaction?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.0bf6cdc27afdb2f2494b82013d92eb73"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "when",
      "application",
      "expose",
      "uploaded",
      "bytes",
      "object",
      "storage",
      "metadata",
      "share",
      "transaction"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.s3-conditional-enrichment"
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

# Object publication and cross-store reconciliation

**Owning question:** When may an application expose uploaded bytes if object storage and metadata do not share a transaction?

## The visible-state invariant

**Original fictional contract:** a catalogue entry is visible only when it references an immutable, validated object version that belongs to the permitted owner. The metadata database owns publication state. Object existence alone does not authorize exposure, and committing a metadata row does not atomically commit a remote object write.

Begin with a pending record using a stable operation ID. Upload into a nonpublic candidate identity, verify the object, then atomically change the metadata state to published with the exact object version and any required outbox event. Readers only follow the published reference and enforce current permission.

~~~mermaid
sequenceDiagram
    participant C as Client
    participant M as Metadata service
    participant O as Object store
    participant R as Repair worker
    C->>M: Create pending operation K
    M-->>C: Authorized candidate identity
    C->>O: Upload candidate bytes
    C->>M: Complete K with exact object reference
    M->>O: Verify object identity and integrity
    M->>M: Publish K and record event atomically
    R->>M: Inspect aged pending operations
    R->>O: Resolve or retire exact candidates
~~~

Text alternative: upload and publication are separate steps. A repair worker resolves aged pending records without inventing a cross-store transaction. This synthetic protocol assumes a durable metadata transaction and appropriately restricted object access.

## Crash windows

| Crash point | Persisted evidence | Recovery |
|---|---|---|
| Before upload starts | Pending K, no verified object | Resume or expire pending intent |
| After upload, before completion call | Candidate object and pending K | Verify exact candidate and resume |
| During validation | Pending K and validation attempt | Repeat safe validation under the same identity |
| After publish commit, before response | Published K and its object reference | Return existing result for K |
| After publication, before event delivery | Published row and durable outbox entry | Relay event without recreating publication |

An object-created notification is a useful wake-up signal, not the authority for a business publication decision. It may arrive before validation or more than once. The worker must consult current metadata and handle duplicate notices idempotently.

## Prevent replacement, not only duplication

S3 conditional writes support create-if-absent and ETag-based preconditions for particular write APIs. They protect the scoped object operation; they do not commit a separate database row. Other stores may differ.

Prefer an immutable version-bound reference where the required store supports it. If the application reads by a mutable name, another writer can change the bytes between verification and later use. Restrict who can overwrite/delete verified candidates, or enforce a version/precondition protocol spanning the check and publication assumptions. Revalidate policy when a pending record changes ownership.

## Garbage collection races

A collector must not delete every unreferenced object it observed at time T: publication could establish a reference after that observation. Use a metadata-owned retirement decision, a grace/state protocol and immutable object identities. One proposal is to atomically move expired pending K to retiring; publication may succeed only from pending/verified, so it loses that race cleanly. Then delete only the candidate belonging to that retired record. An independently resurrected object needs a new identity.

For a small workload, storing content and metadata in one database may eliminate this class of cross-store protocol. Compare actual size, backup, access and cost requirements before distributing state.

## Evidence and navigation

[Conditional writes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html) supports the specific S3 precondition mechanism. The publication protocol and crash matrix are original synthetic reasoning, not a reproduced service implementation. Test the check/publish overwrite race, collector/publisher race and response loss after commit.

Parent: [object chapter](README.md). Previous: [upload](upload-integrity.md). Next: [access and cleanup](access-lifecycle.md). Read [outbox/inbox](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/README.md) for transaction-local effect boundaries.
