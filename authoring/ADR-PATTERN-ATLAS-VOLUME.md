# ADR — Add an eleventh pattern-atlas volume as a decision layer

> **Decision accepted by the owner on 2026-10-21 for issue #228.** The owner
> selected a navigation and decision layer, not a replacement for the technical
> chapters. This record authorizes a bounded structural change. It does not
> assert that source reading, page authoring or independent review is complete.

## Context

Issue #228 requires a 145-entry System Design pattern catalog, exact ownership
and a page-level coverage audit. The default plan was owner-first: preserve the
ten-volume structure, use existing technical owners, and add a page only when
ownership cannot fit.

The owner reviewed that plan and chose an eleventh volume, the **Pattern Atlas**,
as a navigation and decision layer. The atlas is a reference that pages from
other chapters can link to. Its pages also cite exact public sources.

The issue permits a structural decision only when a genuinely distinct research
question justifies it. The atlas owns a distinct question: **which pattern fits
this problem, under which conditions, and what observation would reverse the
choice?** That is not the same as explaining the mechanism, its guarantees and
its failure behavior, which remains with the existing technical owners.

## Decision

Add one volume, `book/volumes/v11-pattern-atlas/`, with eleven chapters by
catalog family and one section for each of the 145 catalog entries. Chapter and
page counts are content-dependent; [the atlas contract](PATTERN-ATLAS-CONTRACT.md)
defines the editorial boundary.

The atlas is a **decision layer**, not a second technical manuscript:

- each entry states the decision question, good-fit conditions, hard
  contraindications, one competing alternative, a short failure/recovery
  summary and the decision state;
- each entry links to the canonical technical owner at an exact section, or
  records an explicit `technical-owner-missing` finding;
- each entry cites exact public sources, versions and inspected sections;
- primary technical owners link back to the atlas entry.

## Scope boundary

| Concern | Canonical owner |
|---|---|
| Catalog membership, aliases and coverage | `edition/patterns/registry.v1.json` |
| Decision summary and contraindications | V11 atlas section |
| Mechanism, invariants and failure behavior | Existing technical page |
| Source identity and admission | `sources/register.json` |
| Reading scope and claim support | Reading ledger and page source tables |
| Page identity, navigation and frontmatter | `book/` frontmatter and route index |

## Page-count policy

Page count in a chapter is content-dependent. A chapter may need one page or
many. The split follows coherent questions, subfamilies and ownership, never a
fixed two- or three-page quota. Page count is inventory, not acceptance. An
empty page is forbidden even when the chapter map reserves a slot.

## Alternatives considered

- **No new volume; owner-first only** — rejected by the owner. It keeps ten
  volumes but leaves no unified decision layer.
- **Deep-reference volume** — rejected. It would duplicate technical owners and
  create two competing mechanism explanations.
- **One chapter per pattern** — rejected. It would manufacture 145 chapters and
  conflict with the content-driven page policy.
- **Atlas as navigation and decision layer** — accepted. It adds selection
  guidance and source routing without replacing mechanism owners.

## Consequences

- The current corpus grows beyond the historical ten-volume, 407-document
  baseline. Historical statements remain dated; current statements must be
  reconciled explicitly.
- The registry has separate `technical` and `decision` coverage. The overall
  state is the weaker layer, so an atlas entry cannot mask a missing technical
  explanation.
- Edition manifests, validators and tests need an explicit post-migration
  overlay. Historical migration, decomposition and enrichment records are not
  rewritten to hide the addition.
- Primary technical pages need a backlink to their atlas entry. The backlink
  change is recorded in the content-revision overlay.
- Source reading, authoring and independent review remain separate gates.
- No release, deployment, hosted retrieval or automatic CI claim follows from
  this decision.

## Revisit criteria

Stop and reassess through a new ADR if any of these conditions holds:

1. Independent review finds that the atlas duplicates technical explanations
   or becomes a second source of truth.
2. After the coverage map, a material share of entries has no credible
   technical owner and the atlas would be used to hide that gap.
3. Maintaining 145 sections and backlinks is not sustainable without a
   dedicated owner.
4. A material share of required sources cannot be admitted or read lawfully.

A reversal keeps the registry and audit evidence, removes the volume only
through an explicit migration, and restores owner-first routing.

## Evidence and limits

Owner authorization is recorded in issue #228 and this ADR. No source reading,
page authoring, benchmark, independent review or coverage completion is claimed
by this record. The 145 catalog entries are a research and authoring backlog,
not a measured popularity ranking.
