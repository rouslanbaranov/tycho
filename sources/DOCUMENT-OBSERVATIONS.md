# Admitted public document observations and change candidates

> E03-04 [issue #30](https://github.com/rouslanbaranov/tycho/issues/30). This workflow separates **public document observation** from verification of technical claims, from repository source locks, from index builds, and from AI chapter generation. Current implementation is metadata-only and on-demand, not a background crawler.

## Delivery and trust boundary

- Canonical, append-preserving [observation ledger](document-observations.json) starts with **zero recorded remote fetches**; no fabricated publisher content hashes.
- [Offline-first observation tool](../scripts/document_observations.py) validates registered source IDs and `admitted-for-research` status, rejects nonpublic/non-HTTPS URLs and unresolved access categories, checks response host against canonical/resolved registered origins (including redirects), limits fetched bytes to 2 MiB and accepts named text/JSON/XML formats only.
- **Only an explicit operator command** `acquire --source src.ID --allow-network` performs one HTTPS GET. It records observation time, requested/resolved URL, registered source version, HTTP status, response type/size, ETag/Last-Modified, SHA-256 digest or bounded unavailability status. It does NOT store the fetched raw document, excerpts, figures or paid books, infer reuse rights, run untrusted scripts or follow off-register redirects.
- Nonpublic, commercial, registration-restricted or `pending-content-access` sources are not automatically acquired. Existing [licensing/access decisions](ACCESS-LICENSING-RESOLUTION.md) still apply.
- A metadata hash difference is a **candidate for expert claim re-review**. It may reflect a timestamp, navigation/template change or reorganization; it does **not** establish a semantic change.
- The observation file is distinct from [register.json](register.json), the [public repository lock](public-repositories.lock.json), book chapters, search indexes and knowledge graphs. No automatic source catalogue refresh, git reset, reindex, graph build, chapter re-enrichment or CI invocation is permitted by this tool.

## Local invocation

~~~sh
# Offline validation and deterministic structural tests:
python3 scripts/document_observations.py validate
python3 -m unittest discover -s tests -p 'test_tycho_document_observations.py' -v

# Compare two deliberate observation snapshots; read-only:
python3 scripts/document_observations.py compare \
    --before sources/document-observations-before.json \
    --after sources/document-observations-after.json

# One expressly approved network operation (do NOT run as routine CI):
python3 scripts/document_observations.py acquire \
    --source src.http-semantics \
    --allow-network
~~~

The before/after filenames illustrate independently saved snapshots, **not** files shipped in the repository. A reviewer decides whether a new observation snapshot can replace or extend the checked-in ledger; no network fetch runs merely because an agent loads a book page.

## Change detection and evidence re-review

| Observation change | Tool output | Human/agent next action |
|---|---|---|
| First admitted observation for source ID | `new-observation` | Record exact section(s) actually read before linking a technical claim |
| Content hash, publication/version scope, response status or resolved URL changed | `candidate-re-review` with exact changed fields | Investigate source relocation and affected claim ledger; inspect relevant sections; do not automatically invalidate all claims |
| No compared metadata changed | No change event | Preserve existing evidence state; age may still demand a separate freshness review |
| Earlier source absent from new snapshot | `missing-new-observation` | Do not treat a missing fetch as source deletion |
| HTTP 401/403/404/410/429 | `unavailable` metadata only | Preserve source ID as inaccessible; seek permitted official companion rather than invent content |
| Unsupported type, oversized body, dangerous redirect, fetch failure | Raise a bounded error; **do not commit altered content** | Fix the admission/rights/transport issue separately |

A re-review candidate should list affected `claim.*` IDs from [claim-references.json](claim-references.json), source revision, new versus old response, impacted sections, whether the evidence **still** supports the original claim, and who performed the review. This join/report is planned for E03-05; this E03-04 tool does not invent that analysis.

## Source and rights limits

A digest is **not** a licence, a right to publish, a verified technical statement, a commit revision, or a preserved content copy. HTTP header dates can be incomplete/inaccurate; a rolling public page has no guaranteed immutable revision unless the publisher supplies one. Store all observations with explicit access scope `metadata-only` and `rights_status=not-assessed`.

The command deliberately does not update a checked-out Git repository. That job belongs exclusively to the explicit pinned [read-only snapshot tool](../scripts/public_repo_snapshots.py) under issue #28; never silently update its revision. There are **no collected production results or public remote fetches in the checked-in ledger**. The Python unit tests use synthetic HTTP responses; network availability and independent source/rights review are separate checks.

## Validation boundary

The [test suite](../tests/test_tycho_document_observations.py) exercises metadata-only hashing, denied sources, HTTP 403, size/type/redirect checks, diffs, unchanged content, append preservation and forged licence/duplicate timestamp rejection using synthetic fixtures. These tests must be executed in a checkout to claim passing status; creating them alone does not prove execution or correctness. No M9 data, deployment, backend or source rights are altered.
