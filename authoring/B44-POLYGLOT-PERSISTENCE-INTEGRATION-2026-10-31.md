# B44 Polyglot Persistence split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no Polyglot Persistence promotion, owner acceptance or
independent AI review is claimed.

## Commit chain

- Parent: `24e8edf7392efa6fde870579983cffb7f66e0159` (`24e8edf7`).
- B44 book-binding cherry-pick: `dd315292`, source `0e9ec96e`.
- This commit: Polyglot Persistence card split, metadata integration, counters
  and tests.

The cherry-pick applied cleanly. `dd315292` contains the B44 lane note, the
V05/C04 owner edits and the updated inline V11/C06 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c06-database-storage/polyglot-persistence.md`.
- Page identity: `tycho.page.6a386512b280490da745f1ae2c416c58`.
- Page raw SHA-256:
  `5d83838b61ad8e2e9ab031d2922ec4076d2876b3279772b7e829faba502d25c6`;
  historical-view SHA-256:
  `5663589cfa334602cb66381944fb532d9124456a8a3d90caa75e8fb7e4e552ea`;
  body SHA-256:
  `48da8110d9373bc243ee5de0325d2146631ee9213650b09db1ad4d1469ea9a59`.
- README raw SHA-256:
  `9b16a71467f6dae31b6d506583f3fa38c985b55864bd0fe551151cd8f65fbe36`;
  historical-view SHA-256:
  `60bbdba25a758a3fe04d4aee2b546dfc40cb776631d7af021784d45fe804c78d`.
- Owner page raw SHA-256:
  `8c0b6ad3059770d2b5e06e6a57feeedad4e0c09e3f9fd629597e1a68c393af9f`;
  historical-view SHA-256:
  `60934b5c7fe9f7e0108a2036fb31246e53fc6dfb924f1246f9709ffa88b36fd8`.
- The README keeps the `### Polyglot Persistence` anchor and now points to
  the dedicated card. The card keeps the owner backlink, the identity, all
  nine explicit card markers, the Tycho-labelled four-part invariant and the
  failure/recovery sequence. The owner page line remains `110`.
- The new page uses a 2026-10-31 self-check date because the preflight requires
  `content_review.reviewed_at` not to predate `source_inspection_date`. This
  is an integration self-check, not a new external review.

## Applied metadata

- `sources/register.json`: 304 sources; `updated` stays 2026-10-31. The
  Debezium outbox page moves to `full-public-page-inspected` with its
  2026-10-31 canonical and raw revisions. PostgreSQL keeps its entry and
  appends the 2026-10-31 logical-replication, conflicts and restrictions
  revisions. No new source id.
- `edition/patterns/reading-ledger.v1.json`: 208 -> 212 records; add
  `read.debezium-outbox.2026-10-31`,
  `read.postgresql-logical-replication.2026-10-31`,
  `read.postgresql-logical-replication-conflicts.2026-10-31` and
  `read.postgresql-logical-replication-restrictions.2026-10-31`. The retained
  Debezium 2026-10-21 record stays historical.
- `edition/patterns/source-plan.v1.json`: 251/250 -> 257/256 required/read;
  blocked stays 1; ledger records 212. Add the AWS and Microsoft retained
  records and the four new records in source-plan order after the Fowler unit.
- `edition/patterns/registry.v1.json`: 251 -> 257 source units; the technical
  owner and technical/overall coverage move to `partial-bounded`; decision
  coverage stays `partial-bounded`; no promotion.
- `edition/patterns/owner-units.v1.json`: invariant and failure/recovery set
  to `supported` with primary and supporting bindings; the retained Fowler
  record stays primary and six auxiliary records are added. Coverage remains
  `partial-bounded`. Counters: invariant 75 -> 76, failure/recovery 69 -> 70,
  technical partial-bounded 15 -> 16, technical partial 73 -> 72.
- `edition/patterns/card-batches.v1.json`: the Polyglot Persistence entry
  gains the dedicated `card_path`.
- `edition/content-revisions.json`: one issue-540 revision with the immutable
  directory baselines for the README and owner page. The new page baseline is
  its historical-view hash, so it needs no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the new page and its
  identity, keep the README anchor and record the migration addition.
- The route index, section index, page census, coverage/reverse maps, phase 4,
  delivery evidence, semantic summary, qrels and edition inventory were
  refreshed from the changed inputs. The candidate, review-reconciliation and
  rereview-packet artifacts were reconciled from the changed card hash.
- `schemas/pattern-delivery-evidence.v1.schema.json` and the affected test
  guards move to 212 ledger records; the atlas and census guards move to 76 V11
  documents and the registry guard to 257 source units.

## Deviations from the B44 note

- The B44 note kept the card inline and said not to convert it. The task
  directed a dedicated page under C06, so the README keeps only the anchor and
  pointer. The metadata therefore records the split README hash.
- The lane note supplied lane-view previous hashes (`0123387e...` for the
  owner page and `72fa5464...` for the README). The content-revision validator
  authorizes against the immutable directory baselines, so the recorded
  previous hashes are `2788d062...` and `81235b0c...`. The current
  historical-view hashes are `60934b5c...` and `60bbdba2...`.
- The cherry-picked card and owner page still called the four new ledger
  records "proposed". Because the metadata integration creates those records,
  the stale qualifier was removed; no claim or revision changed.
- The optional Microsoft register version note for the byte-identical CQRS
  refetch was not added. The retained 2026-10-30 register record and ledger
  record remain accurate and are the ones bound by the owner unit.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.polyglot-persistence`:
  PASS, 1/1.
- Full suite: 681 tests pass.
- PASS: sources, registry, cards, owner units, atlas, directory migration,
  decomposition, enrichment, book metadata, coverage, phase 4, delivery
  evidence, semantic audit, edition, source catalogue, census, sufficient
  pilot and AI-review index.
- PASS: line length (145 exact owner-link exceptions) and boundary checks.

## Limits

- Partial-bounded coverage only; no Polyglot Persistence promotion or owner
  acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding.
- The integrator applied the lane's recorded revisions and did not re-fetch
  the public units. No benchmark, production observation or runtime experiment
  is claimed.
- No new source id or source-page images were read; linked pages remain outside
  the records.
