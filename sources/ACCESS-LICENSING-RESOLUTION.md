# Public-source access and reuse decisions — bounded resolution wave 01

> Issue [#27](https://github.com/rouslanbaranov/tycho/issues/27), E03-01 / M2. Research record, 2026-10-19. No legal advice or permission grant. An accessible web page is **not** a redistribution licence. This document resolves how to proceed when a source cannot lawfully or technically be read, but it does not assert that every registered source was content-verified.

## Purpose, corpus boundary and reproducibility

The authoritative discovery corpus is [register.json](register.json) (169 entries, inspected for these admission states 2026-10-19). The existing [source gaps](GAPS.md) and [reading plan](READING-PLAN.md) already identify source families and access caveats; this wave does **not** repeat discovery or change register admission statuses without new primary-content evidence.

Exactly **12 entries** currently have explicit access restrictions: ten \`bibliography-only\` commercial books and two \`pending-content-access\` OpenJDK JEPs. The other register entries remain subject to their individual edition, terms, section and code-revision checks: absence from this restricted subset does **not** imply unrestricted mirroring or verified content.

## Two canonical-page retrieval gaps — status preserved

| Register ID / expected primary text | Direct URL and retrieval observation, 2026-10-19 | Accessible official companion and directly inspected boundary | Allowed evidentiary inference / remaining gap |
|---|---|---|---|
| \`src.jep444\`: JEP 444, Virtual Threads (Java 21) | [openjdk.org/jeps/444](https://openjdk.org/jeps/444) returned HTTP **403** to automated retrieval; exact JEP text **not inspected** | [Oracle Java SE 25, *Virtual Threads*](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html), sections *What Is a Virtual Thread?*, *Why Use Virtual Threads?*, *Scheduling Virtual Threads and Pinned Virtual Threads*, *Use Semaphores to Limit Concurrency*. Living vendor documentation, inspected on 2026-10-19 | Cite these **Oracle** sections for virtual-thread behavior, bounded carrier/IO descriptions and resource-concurrency guidance. Do **not** cite unseen JEP 444 paragraphs or assume Java 25 text is the Java 21 specification. |
| \`src.jep491\`: JEP 491, Synchronize Virtual Threads without Pinning (Java 24) | [openjdk.org/jeps/491](https://openjdk.org/jeps/491) returned HTTP **403** to automated retrieval; exact JEP text **not inspected** | [Oracle JDK 24 release notes](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html), section *Synchronize Virtual Threads without Pinning*, and [Oracle significant changes in JDK 24](https://docs.oracle.com/en/java/javase/25/migrate/significant-changes-jdk-24.html), corresponding heading; inspected 2026-10-19 | These companions describe how blocking under \`synchronized\` changes in JDK 24. They do **not** establish all JEP motivation, alternative designs, exact implementation proof or compatibility with every runtime. Avoid repeating obsolete Java 21 pinning advice for Java 24+. |

The OpenJDK URLs remain canonical identification links and stay \`pending-content-access\`. Accessible official companions may support **narrow new claims under their own source IDs/URLs**; they do not retroactively verify the unavailable canonical JEPs. A future authorized manual retrieval, linked official source revision, or exact publishable JEP text may resolve this gap only after a new documented inspection. Never bypass access restrictions or invent downloaded contents.

## Commercial full-text boundary: ten bibliography-only entries

| Register IDs | Permitted use in this wave | Explicitly prohibited inference |
|---|---|---|
| \`src.ddia\`, \`src.database-internals\`, \`src.fundamentals-architecture\`, \`src.architecture-hard-parts\`, \`src.building-microservices\` | Existing bibliographic title, author, edition/publisher, and links; locate separately public author/official materials for **new** inspections | No content-level claims from unread chapters, no wholesale text capture, figures, tables, exercise answer reproduction or "fully read" status |
| \`src.monolith-to-microservices\`, \`src.microservices-patterns-book\`, \`src.enterprise-application\`, \`src.release-it\`, \`src.performance-modeling\` | Same bibliography-only treatment; original commentary may separately cite inspected lawful public materials | An author's website, sample, preview or purchase page does not grant the book's full text or independent reuse rights |

No commercial book was purchased or supplied in this wave. An openly visible publisher preview does not authorize full-text ingestion, transformation into a mirrored chapter, or public redistribution. A chapter may name a bibliography item as **further reading** but must cite actually inspected sources for substantive technical claims. If paid material later becomes lawfully accessible, document the access basis and permitted use; read access alone still does not settle republication.

## Reuse and mirroring decision matrix

The following are conservative **operational rules for this project**, not an assertion that a legal exception never applies. Check source-specific terms, underlying copyright, assets, jurisdiction and distribution context at the moment of reuse.

| Intended action | Default project decision | Required evidence before widening |
|---|---|---|
| Store bibliographic metadata, IDs, canonical URL, title and edition | **Allow** as discovery metadata with provenance | Preserve factual accuracy, site terms and observation date; do not confuse metadata with complete-content verification |
| Link to official documentation/standards | **Allow** ordinary reference links and short original descriptions | Version/section/source owner and retrieval status; no implied endorsement |
| Write original, independently composed technical explanation | **Allow** with claim-level primary evidence and original diagrams | Verify public content actually read; avoid reconstructing protected expression |
| Quote third-party prose | **Case-by-case limited**; do not use a blanket length or "fair use" entitlement | Actual applicable permission/licence or defensible exception, attribution and editorial review; keep quotations minimal |
| Copy external figures, substantial tables, full articles or paid book chapters | **Block by default** | Explicit applicable reuse permission and fulfilment of all terms; otherwise redraw an original illustration with distinct expression |
| Mirror third-party documentation or code into the Tycho corpus / index | **Block by default**, including public GitHub and public web pages | Source-specific licence and redistribution/notice obligations, access/robots/service conditions, version pin and approval; prefer link + claim ledger |
| Redistribute licensed software code | **Conditional** | Identify licence in that exact repository/revision, obligations for notices/source/attribution and whether dependencies/assets have different licences |
| Process CC BY 4.0 text or images | **Conditional**, not automatic for arbitrary pages | Verify work is truly under CC BY 4.0, satisfy credit/licence link/change notice; other rights may still restrict use |
| Use material under CC BY-NC 4.0 | **Do not presume commercial reuse allowed** | Verify actual licence, intended context and scope; escalate uncertainty for rights review |

### Primary rights documents inspected (scope and limitations)

- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service), section **D.5, License Grant to Other Users** and **D.8, Public Repositories and Lawful Access**, inspected 2026-10-19. Visibility and repository forking are not a blanket grant to redistribute hosted files in a new public book. Consult the actual file/repository licence; a GitHub link alone is not a licence.
- [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), deed sections **You are free to**, **Under the following terms**, **Notices**, inspected 2026-10-19. The deed is a summary, not legal code; permission depends on the material actually carrying this licence and complying with attribution and change indication.
- [Creative Commons Attribution-NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en), deed sections **Under the following terms** and **Notices**, inspected 2026-10-19. No generalized commercial right follows.
- [Apache Software Foundation, Applying the Apache License, Version 2.0](https://www.apache.org/legal/apply-license), *Applying the license to new software*, inspected 2026-10-19. Software distributions may require a LICENSE and correct NOTICE; this is an example of licence-specific obligations, not permission to copy material from an unrelated site.

## Executable authoring guardrails

1. Before quoting or incorporating an asset, bind the exact source URL, publisher, version/revision, retrieval date and section to the proposed claim or object.
2. Record separate fields for \`access_state\`, \`content_verified\`, \`source_license\`, \`reuse_scope\` and \`rights_review\`. **Do not** derive any one automatically from the others.
3. For \`pending-content-access\`, allow a canonical identifier and an **independently inspected companion**, with the latter cited directly; never fill a missing JEP section from a model's memory.
4. For \`bibliography-only\`, do not promote a paid book to research evidence until actual lawful access and section verification are documented.
5. Keep excerpt and artwork ingestion disabled in the automated harness by default. If later introduced, track original notice, permission and version per asset; do not confuse link indexing with corpus mirroring.
6. Record "blocked / available companion / permissions unresolved" explicitly rather than manufacturing a verification result. Escalate ambiguous terms to a competent rights owner before republication.

## Verification and acceptance status

Completed here: inventory review for all twelve explicitly restricted entries; direct current retrieval attempts for the two JEPs; official-companion inspection with scope boundaries; primary rights-document inspection; project operational decision table. **Not completed:** legal assessment for every one of the other 157 entries, retrospective rights certification, automatic enforcement, complete catalogue regeneration, local full premerge checks, independent rights/domain review. Therefore this file is a **substantial bounded issue deliverable**, not blanket approval to close #27 or the M2 milestone without further acceptance checks.

No repository automation or external mirroring has been run in this wave. Updates to specific \`register.json\` entries must await a genuine source status change; merely documenting access gaps is not a reason to flip \`content_verified\` from \`null\`.
