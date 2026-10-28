# c03 split batch — execution record

Status: started. Goal is autonomous; no owner confirmations are requested.

## Order

1. Move Request-Reply Messaging to `c03-messaging-integration/request-reply-messaging.md`.
2. Move Message Filter to `c03-messaging-integration/message-filter.md`.
3. Keep c03 anchor link sections.
4. Suspend both promotions and acceptance.
5. Run two fresh reviews against the new page/card hashes.
6. Restore promotions/acceptance after pass.
7. Continue Aggregator / Scatter-Gather / Splitter / Pipes and Filters /
   Claim Check / Resequencer.

## Constraints

- Every c03 edit invalidates both promotion-bound cards until split.
- No promotion without a saved external pass.
- Owner acceptance is recorded only after the batch is complete.
