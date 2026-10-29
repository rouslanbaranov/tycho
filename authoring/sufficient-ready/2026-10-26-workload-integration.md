# Workload Identity / mTLS — source integration

Date: 2026-10-26. Refs #532. Status: integrated; not sufficient.

## Source

The full Istio Security page was read on 2026-10-26 (SHA-256
`0291fb8211b0215a91fe1c2bf389db7b3cdb6fffd57605f13fb4e6b402eb66e4`). The existing ledger
record `read.batch6-istio.2026-10-21` was extended in place so downstream references keep
their identity. The source is an unversioned `latest` page; the hash pins this retrieval.

## Metadata correction

`sources/register.json` bound `src.istio` to the architecture page while the ledger used the
security page. The register now points to the security page with title, access date and
verification scope corrected. The source inventory date moved to 2026-10-26.

## Content changes

- Card: the Sources block now lists the full read sections and states that identity binding,
certificate rotation, mTLS and authorization are supported.
- Owner note: the preamble now allows a section to cite a dedicated source. A source
boundary states that revocation, trust-root bootstrap, key storage and lifetime policy are
outside the read scope and remain synthetic.

## Verification

PASS: source plan; pattern cards; owner units; semantic audit; atlas; directory migration;
edition inventory.

Full suite: 583 tests, one pre-existing failure in the Phase 2 qrels quote for
`queue-recovery.md`; that page is outside this change.

## Residual

Two packets are now `page-changed-since-review` (Workload Identity and Federated Identity,
which shares the owner page). Both need a fresh external AI review before rebinding; this
is tracked in #540. No sufficient coverage is claimed.
