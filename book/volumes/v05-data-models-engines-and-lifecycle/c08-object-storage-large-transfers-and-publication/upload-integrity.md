---
{
  "metadata_version": 1,
  "id": "tycho.page.60ae29b6b2a422214c18be04cf012b6e",
  "kind": "page",
  "parent_id": "tycho.chapter.0bf6cdc27afdb2f2494b82013d92eb73",
  "canonical_path": "book/volumes/v05-data-models-engines-and-lifecycle/c08-object-storage-large-transfers-and-publication/upload-integrity.md",
  "title": "Resumable large uploads and byte integrity",
  "topic_ids": [
    "object-storage"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "Which transfer identities allow interruption recovery without confusing uploaded parts with a verified object?",
  "route_hints": {
    "questions": [
      "Which transfer identities allow interruption recovery without confusing uploaded parts with a verified object?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.0bf6cdc27afdb2f2494b82013d92eb73"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "which",
      "transfer",
      "identities",
      "allow",
      "interruption",
      "recovery",
      "without",
      "confusing",
      "uploaded",
      "parts",
      "with",
      "verified"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.s3-multipart-enrichment"
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

# Resumable large uploads and byte integrity

**Owning question:** Which transfer identities allow interruption recovery without confusing uploaded parts with a verified object?

## Separate the identities

Name the logical upload request, object key/version, multipart session, part position and expected content digest. A client reconnecting after an interruption must know which of those identities remains authoritative. Retrying with a new random object key every time can create orphan copies; reusing a key without concurrency control can overwrite another upload.

The S3 multipart overview describes initiation, part upload and completion; individual parts can be retried. Its documentation explicitly cautions that a completed multipart object's ETag is not necessarily the MD5 of its bytes. Select a documented checksum algorithm and compare the declared byte content, rather than treating an opaque validator as a portable checksum.

## Original worked transfer budget

Assume a fictional workshop records a 4 GiB payload, divided into 64 parts of 64 MiB, with four concurrent part transfers. These are invented values, not a recommended universal part size. Client buffering one complete part per transfer would require at least 256 MiB just for those buffers; actual memory includes protocol and application overhead. Streaming can reduce that amount but changes retry/re-read requirements.

Persist an upload manifest containing an authorized owner, logical operation ID, expected object identity, session ID, size/checksum contract and completed part receipts. Use bounded concurrency and backpressure so a fast reader does not allocate the whole payload. The storage API's actual part-size/count constraints must be checked for the selected service and bucket type.

~~~mermaid
stateDiagram-v2
    [*] --> Initiated
    Initiated --> Uploading: Persist session identity
    Uploading --> Uploading: Retry missing or failed part
    Uploading --> Completing: Required part receipts available
    Completing --> Verifying: Completion confirmed or resolved
    Completing --> Unknown: Response lost
    Unknown --> Verifying: Resolve exact object and session
    Verifying --> Ready: Expected bytes and policy checks pass
    Verifying --> Quarantined: Mismatch or unsafe content
    Uploading --> Aborting: Cancel or expire ownership
~~~

Text alternative: transferred parts become a completed candidate, then a verified object. A lost response introduces an explicit unknown state; it does not prove that completion failed. This is an original application state model, not an S3 internal state diagram.

## Resolve ambiguity before starting again

After a completion timeout, query the exact intended object/version and verify the expected metadata and checksum under the chosen API contract. A matching key alone is insufficient if another writer may have replaced it. If no unambiguous resolution is possible, quarantine the logical upload for repair; do not publish guessed bytes.

A part retry also needs stable content. If the local file changes between reading part 1 and retrying part 2, a transfer can succeed while combining unintended data. Pin the source version or detect changes. A checksum verifies bytes against a trusted expected value; it does not establish permission, safe content or the authenticity of a maliciously supplied manifest.

## Cancellation, cost and alternatives

Incomplete uploads consume storage and need an explicit cleanup policy. Coordinate abort with in-flight transfers; an abort acknowledgement should not be interpreted as proof that every concurrently sent part has already disappeared. Track the selected service's cleanup semantics.

For small content with a reliable request budget, a single bounded upload may be simpler. For an unseekable producer, durable local staging or restartable generation may be needed. Avoid calling a design resumable unless its client can recover the required manifest and source bytes.

## Evidence and navigation

[Multipart upload overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) supports the named S3 lifecycle/checksum caveats; selected passages inspected 2026-10-20. The manifest, state model, memory arithmetic and recovery rule are original unexecuted proposals. Test interruption during a part, changed source bytes, duplicate completion and lost completion responses.

Parent: [object chapter](README.md). Next: [publication](publication-consistency.md). Related: [network connection fate](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/connections-draining.md).
