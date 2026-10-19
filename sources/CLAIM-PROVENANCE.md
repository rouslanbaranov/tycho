# Typed claim-to-source provenance and evidence relations

> E03-03 [issue #29](https://github.com/rouslanbaranov/tycho/issues/29); 2026-10-19. This describes the **implemented local JSON validation contract**, not semantic proof, a deployed knowledge graph, a search index, legal clearance, or an automated citation renderer.

## Artifacts and scopes

- [claim-references.json](claim-references.json): three deliberately bounded example records: an idempotency claim, a disputed inference about HTTP idempotence, and unavailable JEP 491 content. Each references exactly one existing owner page.
- [validate_claim_references.py](../scripts/validate_claim_references.py): offline check of claim IDs, canonical owner paths, source catalogue IDs and admission states, evidence relationships and bounded locations. For code evidence it requires a matching full commit SHA in [public-repositories.lock.json](public-repositories.lock.json) and a safe relative path/optional symbol; it **does not** clone or read the target code.
- [test_tycho_claim_references.py](../tests/test_tycho_claim_references.py): structural validation tests for valid records, unavailable and unadmitted sources, spurious certainty, contradictions, unsafe URLs, revision/path mismatch and owner paths.

~~~sh
python3 scripts/validate_claim_references.py
python3 -m unittest discover -s tests -p 'test_tycho_claim_references.py' -v
~~~

The script reads the existing canonical public inventory and two issue-specific JSON manifests without network calls or writes. Owner-page existence is checked by the CLI against the local checkout. It does not automatically update metadata, enrich chapters, mirror sources or run GitHub Actions.

## Claim, evidence and location semantics

| Field | Operational meaning |
|---|---|
| Claim `id / statement / owner_page` | Original bounded assertion with one canonical existing page, not an untracked fragment |
| Claim `applicability.conditions / exclusions` | Conditions under which the assertion can be reasoned about; explicit counterconditions |
| Claim `status` | `proposed`, `evidence-linked`, `contested`, `insufficient-evidence`. Not synonymous with independently reviewed or production-tested |
| Evidence `source_id` | Must resolve to the existing registered public source ID; registration alone is NOT a read event |
| Evidence `relation` | `supports`: narrow scope; `qualifies`: narrows premises; `contradicts`: conflicts with the stated claim/inference, **not necessarily with another source**; `unavailable`: cannot establish a factual passage |
| Evidence `reasoning / observed_at` | Human/agent rationale and actual inspection or access observation date |
| Evidence `verification` | `section-inspected`, `identifier-only`, `not-accessible`. These are manually supplied declarations; a structural validator **cannot verify their honesty** |
| `document-section` location | Exact HTTPS URL hosted by the registered public source owner plus explicit section; unlike a general website search result |
| `source-code` location | Exact pinned Git revision, relative repository path and optional symbol. Exact reference identity is mechanically checked against lock, **not** content truth |

An `evidence-linked` claim requires a support relation and no unresolved contradiction. Any `contradicts` relation forces status `contested`. A `pending-content-access` or `bibliography-only` source cannot be offered as inspected technical evidence: only `unavailable` is allowed. A status is not a peer-review or factual-certainty certificate.

## Demonstration and non-overclaim

The example `claim.same-intent-retry` links an original *proposed service design contract* to inspected sections of [AWS Builders' Library, Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) and a scope qualification from [RFC 9110, §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html). Both pages were inspected on 2026-10-19. AWS documents the use of client request identity, atomic association and semantically equivalent retry outcomes; RFC 9110 addresses method semantics. Neither proves that any Tycho example was implemented or that its external notification is globally exactly once.

`claim.http-idempotence-is-not-global-exactly-once` stores an intentionally **disputed inference** and the counter-reasoning that narrows it. It does *not* falsely claim that the two primary publications contradict one another. `claim.jep491-full-text-unavailable` captures an HTTP 403 observation and has no invented document location or technical citation. Its historical official-companion scope is recorded separately in [ACCESS-LICENSING-RESOLUTION.md](ACCESS-LICENSING-RESOLUTION.md).

### Why precise references are not sufficient evidence by themselves

A code reference with SHA/path/symbol is **identifiable**, but a different version, runtime configuration or additional state boundary may invalidate a general architectural inference. A passage can be real but a cited claim may overstate it. This validator does not check URL reachability, compare book prose to a cited section, confirm a symbol exists in a remote code revision, implement a knowledge graph or determine legal rights. These are separate acquisition, semantic review and graph/provenance gates; always preserve the source's inspected revision and the claim's applicability and uncertainty.

## Future integration boundary

Claims are stored as human-readable **JSON examples, not generated YAML frontmatter**. Future semantic graph and metadata milestones may ingest these typed relationships after schema evolution/migration and ownership review, without replacing their existing canonical source catalogue. No chapter is automatically re-enriched; no M9 source material is edited.
