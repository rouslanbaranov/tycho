# B46 Idempotency Key split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no Idempotency Key promotion, owner acceptance or independent
AI review is claimed.

## Commit chain

- Parent: `0604f3db50f0d9e09dbe9c1ded6acfe24d481175` (`0604f3db`).
- B46 book-binding cherry-pick: `ed4ff869`, source `f08f379d`.
- This integration: dedicated card page, shared metadata, counters and tests.

The cherry-pick applied cleanly. It contains the B46 lane note, the V04/C04
owner edits and the updated inline V11/C04 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c04-consistency-events/idempotency-key.md`.
- Page identity: `tycho.page.d9c13bc73d3060017a13776ac9dec4b9`.
- Page raw SHA-256:
  `d5cb23fa9854bd70c5bfe24242041768f92738f88d3103bfe811f7ac9899b352`;
  historical-view SHA-256:
  `7e4378969686ee8f036c0080c1abbac17495ee5fcd7226805053ebc33c9316e1`;
  body SHA-256:
  `5f7bad055798e23cf4b15f1e6ff81f4e1a1c63c31b8883f97858341eab3ab413`.
- README raw SHA-256:
  `ef3f51dbe8be3570a2763b7c396783a7d2292f893e4e8b666ea5001c23d7382a`;
  historical-view SHA-256:
  `f4dacf4fd13e115622a79160acb48d85a6ff76ed2efa4c6e9e73ca3960bd5e27`.
- Owner page raw SHA-256:
  `bc89d1f358d6ba470d4b5e9654f19c334c362365ad13da700b655a6f3d7f58e3`;
  historical-view SHA-256:
  `962a429644bcda0a57c3f25ecd1a648b61ac4f74d77adbbb48b002c9275f1c6f`.
- The README keeps the `### Idempotency Key` anchor and points to the
  dedicated card. The card keeps the owner backlink, the identity, all explicit
  card markers and the Tycho-labelled four-part contract. The owner page line
  remains `104`.

## Applied metadata

- `sources/register.json`: 305 sources; IETF moves to draft-08; AWS, Stripe
  and Microsoft gain their 2026-10-31 revisions, scopes and titles. The source
  catalogue is regenerated.
- `edition/patterns/reading-ledger.v1.json`: 214 -> 218 records. The retained
  draft-07 and Microsoft 2026-10-30 records stay historical.
- `edition/patterns/source-plan.v1.json`: 260/259/214 ->
  263/262/218 required/read/ledger; blocked stays 1. Every new record is bound
  to a read unit.
- `edition/patterns/registry.v1.json`: source units 260 -> 263; technical
  owner and technical/overall coverage move to `partial-bounded`; decision
  coverage stays `partial-bounded`.
- `edition/patterns/owner-units.v1.json`: all four dimensions set to
  `supported` with primary and supporting bindings. Counters: mechanism
  112 -> 113, invariant 77 -> 78, failure/recovery 71 -> 72, alternative
  76 -> 77, technical partial-bounded 15 -> 16, technical partial 71 -> 70.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and the draft-08 ledger record.
- `edition/content-revisions.json`: one issue-540 revision with the immutable
  directory baselines for the README and owner page. The new page baseline is
  its historical-view hash, so it needs no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the new page and its
  identity, keep the README anchor and record the migration addition.
- The route index, section index, page census, coverage/reverse maps, phase 4,
  delivery evidence, semantic summary, qrels and edition inventory were
  refreshed. Test guards and schema caps move to 501 pages, 78 V11 documents,
  263 source units and 218 ledger records.

## Deviations from the B46 note

- The note kept the card inline and said not to convert it. The task directed a
  dedicated page under C04, so the README keeps only the anchor and pointer.
- The note requested the Stripe unit type `api-reference`, which the reading
  ledger and source-plan schemas do not admit. The record uses
  `documentation-page`, the closest admitted type.
- Replacing the single IETF unit removed the only plan reference to the
  historical draft-07 record. It is retained in `foundation_records` and marked
  `intentionally-unused`, so the record stays unchanged while every ledger
  record remains referenced.
- The lane-view previous hashes differ from the immutable directory baselines.
  The content revision records the baselines, not the lane-worktree hashes.
- The phase-2 qrels quote for the owner section was split into two contiguous
  passages because the lane expanded the mechanism and invariant paragraphs.
  The claim and question are unchanged.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.idempotency-key`: PASS,
  1/1.
- Full suite: 681 tests pass, run once at batch end.
- PASS: sources, registry, cards, owner units, atlas, directory migration,
  decomposition, enrichment, book metadata, coverage, phase 4, delivery
  evidence, semantic audit, edition, source catalogue, census, sufficient
  pilot and AI-review index.
- PASS: line length (145 exact owner-link exceptions) and boundary checks.

## Limits

- Partial-bounded coverage only; no Idempotency Key promotion or owner
  acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding.
- The integrator applied the lane's recorded revisions and did not re-fetch
  the public units. No benchmark, production observation or runtime experiment
  is claimed.
- No new source id or source-page images were read; linked pages remain outside
  the records.
