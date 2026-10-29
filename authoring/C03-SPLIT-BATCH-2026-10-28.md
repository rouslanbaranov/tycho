# c03 split batch — execution record

Status: split complete on 2026-10-28. Request-Reply Messaging and Message Filter
were the first pair. The Pipes and Filters update below records the later split and
the re-suspended Message Filter promotion. No external review was run for Pipes and
Filters and it is not promoted or sufficient.

## Order

1. Move Request-Reply Messaging to `c03-messaging-integration/request-reply-messaging.md` — done.
2. Move Message Filter to `c03-messaging-integration/message-filter.md` — done.
3. Keep c03 anchor link sections — done.
4. Suspend both promotions and acceptance — done.
5. Run two fresh reviews against the new page/card hashes — pending.
6. Restore promotions/acceptance after pass — pending; requires a pass.
7. Continue Aggregator / Scatter-Gather / Splitter / Pipes and Filters /
   Claim Check / Resequencer — later batch.

## Execution state

- New pages registered in atlas, directory, identity and semantic metadata.
- `card_path` set in card batches; reciprocal owner backlinks rebound.
- Both promotions and the Request-Reply owner-acceptance entry suspended.
- Registry and owner-unit coverage set to `partial-bounded`.
- Fresh external reviews and any restoration remain pending.

## Constraints

- Every c03 edit invalidates both promotion-bound cards until split.
- No promotion without a saved external pass.
- Owner acceptance is recorded only after the batch is complete.

## Update - Pipes and Filters, 2026-10-28

Pipes and Filters moved to `c03-messaging-integration/pipes-and-filters.md` while
preparing the entry for sufficient review. The c03 landing keeps an index link only.
The owner section in `message-selection.md` was rewritten decision-first, so the
Message Filter promotion is suspended: its owner-page hash changed even though its
card page did not. Message Filter remains `partial-bounded` and review-ready; its
four dimensions are still supported and a fresh external review is required before
restoration.

Pipes and Filters remains `partial-bounded` with four source-bound dimensions and no
promotion. No external review was run in this batch.

## Update - Claim Check, 2026-10-29

Claim Check was split to a dedicated c03 page on 2026-10-28. On 2026-10-29 the owner section
and card were remediated against review findings: decision wording now uses payload
lifecycle, the owner-unit notes attribute all four bindings to the Microsoft page and limit
the EIP page to the stored-payload/claim-token description, and failure cases are explicitly
source-attributed. Editing the shared owner page suspended Request-Reply Messaging again;
Request-Reply remains `partial-bounded` and review-ready with its four dimensions supported.
Claim Check remains `partial-bounded` with no promotion and no sufficient claim. Fresh
external reviews are required for both.

## Update - Resequencer, 2026-10-29

Resequencer moved to `c03-messaging-integration/resequencer.md` and its owner note was
rewritten decision-first. Both edits are source-bound: the mechanism binds to the Enterprise
Integration Patterns Resequencer page, the bounded backlog and timeout recovery bind to the
Apache Camel 4.22.x LTS Resequence page, and the partitioned-ordering alternative binds to the
Microsoft Learn Sequential Convoy page. The two new public units were read, recorded in the
ledger, planned in the source plan and registered.

The shared `message-selection.md` owner page changed, so the Pipes and Filters promotion was
suspended. Pipes and Filters remains `partial-bounded` with four supported dimensions and is
review-ready; its dedicated card is unchanged. Resequencer remains `partial-bounded` with no
promotion and no sufficient claim. No external review was run in this batch.
