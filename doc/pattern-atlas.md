# Pattern atlas

The pattern atlas is Tycho's decision-oriented catalogue of system-design
patterns. It is not a glossary and not a second book: each entry has a canonical
owner section, a decision card and a promotion state.

The atlas lives under
[`book/volumes/v11-pattern-atlas/`](../book/volumes/v11-pattern-atlas/README.md).
The machine-readable owners are in
[owner-units.v1.json](../edition/patterns/owner-units.v1.json).

## At a glance

| Measure | Value |
|---|---:|
| Pattern entries | 145 |
| Families | 11 |
| Atlas chapters | 11 |
| Atlas Markdown documents | 157 |
| Decision cards | 145 |
| Owner units | 145 |
| Shared owner pages | 30 |
| Sufficient entries | 104 |
| Remaining entries | 41 |

Every entry is currently self-checked. None is described as independently
reviewed merely because it appears in the atlas.

## Families

| Family | Entries |
|---|---:|
| Messaging and event-driven integration | 20 |
| Resilience and fault tolerance | 16 |
| Data consistency, transactions and event sourcing | 14 |
| Caching and retrieval | 14 |
| Database and storage architecture | 13 |
| Security, isolation and operational architecture | 13 |
| Application architecture and boundaries | 12 |
| API and service communication | 12 |
| Deployment and legacy modernization | 12 |
| Scalability and load distribution | 10 |
| Distributed coordination | 9 |

Families are navigation aids, not claims that every entry in a family has the
same evidence depth.

## The three artifacts per entry

### Owner unit

The owner unit is the section-level home. It carries:

- stable `pattern_id`;
- canonical owner page and heading anchor;
- family;
- technical and decision coverage;
- source and decision evidence;
- review state.

An owner unit can be a dedicated page or a section on a shared page. Shared pages
are allowed, but a promotion-bound card must not remain on a page where ownership
is ambiguous.

### Decision card

The card is the compact decision surface. It should answer:

- When does this pattern fit?
- When is it contraindicated?
- What is the competing alternative?
- What fails, and how is recovery checked?
- Which evidence supports the card?
- Which related entries or sources should be read next?

The card is not a complete explanation. It routes the reader to the owner
section and evidence.

### Promotion record

The promotion record binds the owner page and card hashes to a reviewed commit.
See [Evidence layer](evidence-layer.md) for the record fields and workflow.

## Coverage states

| State | Meaning |
|---|---|
| `name-only` | A name and pointer, without a reviewable card or owner |
| `partial` | Some dimensions or decision fields are missing |
| `partial-bounded` | Bounded evidence exists, but a gate remains open |
| `sufficient` | Technical and decision gates passed, with a valid record |

Current distribution:

- 104 `sufficient`;
- 37 `partial`;
- 4 `partial-bounded`;
- 0 `name-only`.

The 41 non-sufficient entries are not failures of the atlas. They are the
remaining promotion queue, and their gaps are recorded rather than hidden.

## How the atlas is structured

The atlas has 11 chapters. Each chapter is a family-level landing page with:

- a scope and decision question;
- links to the relevant entries;
- cross-links to canonical book owners;
- a list of open evidence or review gaps.

The entries themselves are Markdown pages with frontmatter, an owner section,
the decision card, applicability and contraindication material, failure and
recovery, alternatives and source notes.

## How to use an entry

1. Start with the decision question, not the pattern name.
2. Read the card's fit and contraindication fields.
3. Check the competing alternative.
4. Read the owner section for mechanism and failure behavior.
5. Follow the evidence and source IDs.
6. Treat `partial` entries as research leads, not recommendations.

A decision question can also be answered without a pattern. "Retain the current
design", "measure first" and "insufficient evidence" are valid outcomes.

## Relationship to the book

The atlas is a routing layer. Canonical explanations remain in their book owner
pages. An atlas card should not duplicate a full technical explanation; it should
state the decision and link to the owner.

The book has 12 volumes and 89 chapters. The atlas is one volume (V11) and does
not replace the other 11 volumes.

## Validation

The atlas is checked by:

- `scripts/validate_sufficient_promotions.py`;
- `scripts/validate_pattern_sources.py`;
- `scripts/validate_pattern_owner_units.py`;
- `scripts/check_atlas_integrity.py`;
- the route index and book navigation validators.

Validators check structure, IDs, hashes, owner links and coverage declarations.
They do not prove that a pattern is correct or that the prose is complete.

## Promotion queue

The 41 remaining entries are the queue for future promotion. A promotion must
follow the one-entry-at-a-time workflow in
[ENTRY-PROMOTION.md](../governance/ENTRY-PROMOTION.md). The owner acceptance
record currently covers 94 of the 104 sufficient entries.

## Limits

- The atlas is a catalogue, not a proof of uniform evidence quality.
- Shared owner pages can make ownership harder to inspect; the owner-unit file
  is the authority.
- A card can be decision-sufficient while the broader chapter remains partial.
- Promotion counts change; the JSON files are authoritative over this summary.
- No independent human review of the full atlas is claimed.
