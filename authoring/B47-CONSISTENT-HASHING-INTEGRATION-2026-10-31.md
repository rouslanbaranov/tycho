# B47 Consistent Hashing split and promotion

Status: integrated and promoted on 2026-10-31. The entry is technical and decision
`sufficient`; owner acceptance remains open. A different-vendor review and a
supplementary same-vendor review both returned `pass-with-findings` with no blocking
or major finding.

## Commit chain

- Baseline: `46b66671` (merge of the 2026-10-31 hand-off into the B47 WIP branch).
- B47 content: `19739a73` (dedicated card, owner section, shared metadata, refresh).
- Review HEAD: `409c8ed6` (review packet, historical review pin, count guards).
- Promotion: `d71b145b` (promotion record, owner units, registry, delivery evidence,
  review reports and guards).
- Timing and state: this commit.

## Card split

- Dedicated card:
  `book/volumes/v11-pattern-atlas/c06-database-storage/consistent-hashing.md`.
- Page identity: `tycho.page.ba4ee752a40342cfb6d6be5ac81c4bd3`.
- Owner page SHA-256:

      3ebcff9969062507cb594e4344c0ec143cf7e6fb5940983942e7028f61362453

- Card SHA-256:

      ea2ce0bc8e2c70f7930f8d6806ba39697ce0df0e1a80e2d785be52cd4efca8de

- Chapter landing SHA-256:

      74a283fc42fe468cada73d4ce1ad4c82d4cfa4a973849d7baf1da1e0c090378b

- Owner section: `### Consistent Hashing`, level 3, line 132, 844 words.
- The chapter landing keeps the anchor and card pointer; the card keeps the owner
  backlink, identity and four-part contract.

## Applied metadata

- `sources/register.json`: 305 to 306 sources with `src.karger`; the Dynamo,
  Cassandra and Riak read scopes now record the 2026-10-31 B47 units.
- `edition/patterns/reading-ledger.v1.json`: 218 to 224 records.
- `edition/patterns/source-plan.v1.json`: 263/262/218 to 269/268/224
  required/read/ledger; blocked stays 1.
- `edition/patterns/registry.v1.json`: source units 263 to 269; technical and
  atlas owner states and coverage are `sufficient`.
- `edition/patterns/owner-units.v1.json`: all four dimensions `supported`;
  technical and decision coverage `sufficient`. Counters: mechanism 114,
  invariant 79, failure/recovery 73, alternative 78; partial-bounded technical
  16 to 15 and decision 85 to 84; sufficient technical and decision 60 to 61.
- `edition/patterns/delivery-evidence.v1.json`: the same coverage counters;
  145 entries, 145 cards.
- `edition/patterns/sufficient-promotions.v1.json`: 60 to 61 promotions.
- Card batches, atlas manifest, directory migration, document identities, semantic
  audit, content revisions, route and section indexes, page census, coverage and
  reverse maps, phase 4, qrels and inventory were refreshed.
- `sources/CATALOG.md` and the test guards move to 306 sources, 224 ledger records,
  502 pages and 79 V11 documents.

## Reviews

Qualifying different-vendor review:

- Reviewer: Codex / OpenAI, model `gpt-5.6-sol`, CLI 0.166.0.
- Session: `01a19206-effa-7242-9576-bfad67fc85ed`.
- Review HEAD: `409c8ed6`; content commit: `19739a73`.
- Verdict: `pass-with-findings`; one minor finding, no blocking or major.
- Report: `authoring/ai-reviews/2026-10-31-consistent-hashing-codex.md`.
- Report SHA-256:

      f50fc94a02638fa7bd60d2da9851a1d37bd0ad252d90972013c686c643514974

Supplementary same-vendor review:

- Reviewer: DeepSeek Reviewer, fresh read-only separate agent, not a fork.
- Session: `cc6ca316-8d0b-4b19-9a1e-df599ad70a5a`; the report records the
  delegating session id `ce241624-57b4-4f9a-84d7-da8f93fedd03`.
- Review HEAD: `409c8ed6`; content commit: `19739a73`.
- Verdict: `pass-with-findings`; nine minor findings, no blocking or major.
- Report: `authoring/ai-reviews/2026-10-31-consistent-hashing-deepseek.md`.
- Report SHA-256:

      3e5289deb8fb5cff4e8830f764a73a4eeb8a73b675ac86c7b9975384c6bd20a9

The Codex report is the promotion gate. The same-vendor review is supplementary and
does not replace a different-vendor review where one is available. Promotion follows
the hand-off rule to promote on a pass with no blocking or major finding and the
accelerated-pipeline allowance for recorded minor findings.

## Findings and disposition

- Codex B47-M1: the `K/N` movement formula does not separate the leaving denominator
  from the joining `N+1` denominator. The surrounding text calls the figure an
  expectation, not a guarantee. Recorded; the owner page is not edited because that
  would change the promoted hash and require a new review.
- DeepSeek minor 1: one Dynamo supporting binding named section 4.3 while the quote
  is in 4.2. Fixed before promotion; the guard test pins 4.2.
- DeepSeek minor 2: a Karger excerpt ends with a period where the source has a comma.
- DeepSeek minor 3: a Riak quote reproduces rendered text rather than the pinned
  Markdown emphasis. Both touch the promoted owner page; recorded for a future edit
  and fresh review.
- DeepSeek minor 4: the card and owner state the Tycho failure rule differently
  ("verify ownership" versus "record the ownership epoch", and the card omits hot
  keys). A card edit would change the promoted hash; recorded.
- DeepSeek minor 5: the 2026-10-26 `sufficient-ready-plan.v1.json` pilot snapshot
  still says rejected. It is a dated historical plan, not a current status source;
  left unchanged.
- DeepSeek minors 6 and 7: historical re-review scope and reconciliation artifacts
  keep older provenance and a `current_verdict` field derived from the 2026-10-23
  record. Recorded; these files are historical evidence, not promotions.
- DeepSeek minor 8: the register under-described the B47 source scopes. Fixed before
  promotion; the guard test pins the 4.2 label and the 2026-10-31 scopes.
- DeepSeek minor 9: the owner page-level review dates predate the new section. A
  frontmatter edit would change the promoted hash; recorded for a future edit.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.consistent-hashing`: PASS, 1/1.
- Full suite at `d71b145b`: 688 tests OK in 73.9 s.
- `validate_ai_reviews.py`: PASS, 123 reports.
- `validate_sufficient_promotions.py`: PASS, 61 promotions.
- `validate_delivery_evidence.py`: PASS, 145 entries, 145 cards.
- Pattern atlas, registry, owner units, source plan, semantic audit, census and
  re-review packet validators pass at the same HEAD.
- `check_boundary.py`: PASS; independent-origin review still required.
- `check_markdown_line_length.py`: PASS; 145 exact owner-link exceptions.
- Not run: `premerge_check.py` on this lane branch; GitHub Actions is milestone-only.

## Limits

- Owner acceptance remains open; no acceptance record is added.
- No benchmark, production observation, cluster experiment or CI is claimed.
- Codex could not fetch the recorded Princeton Karger PDF or the exact Riak
  adding/removing URL; it recorded those retrieval limits. The supplementary review
  reproduced the recorded hashes from public URLs.
- The content-level minor findings that touch promoted bytes remain recorded, not
  silently closed. A later edit requires a new review and promotion hash.
- The promotion binds the exact owner and card SHA-256 values above.
