# Foundational book reading

Issue [#225](https://github.com/rouslanbaranov/tycho/issues/225). Updated 2026-10-21. **Reading in progress; no whole book completed.** The owner prioritized foundational books over further technology-reference auditing. Earlier reference readings remain recorded; the next substantive work is book reading.

## Current reading position

| Book | Actual progress | Next action |
| --- | --- | --- |
| Site Reliability Engineering | Preface and chapters 1–5 read completely, including footnotes and chapter 2–4 technical figures | Read chapter 6, then continue through all remaining chapters, frontmatter/part introductions, six appendices and bibliography; see `sre-units.json` |
| Operating Systems: Three Easy Pieces | Chapter 2 read completely, all 19 pages, examples, footnotes, references and homework text | Continue introductory dialogue and CPU/process chapters before deeper concurrency and persistence sections |
| Designing Data-Intensive Applications, 2nd edition | Publisher contents and short chapter 1 preview only | Full text requires lawful access; do not count the preview as chapter reading or silently substitute the first edition |
| Distributed Systems, 4th edition | Author's access instructions examined; no book text obtained | Personalized download requires an email and human-verification step; no request submitted |
| Other registered books | Not started in this audit | Continue `book-queue.json`; distinguish available complete texts from commercial previews |

## Reading notes for later comparison

These are short original notes, not Tycho corrections or completed chapter audits. Exact reading coverage and limitations are in `book-readings.json`. Reported historical practices remain attributed to the source's setting and date.

- **SRE preface:** operational responsibility spans a system's lifecycle. General principles require translation from the source's environment; reliability goals and safety constraints cannot be transplanted without context. Keep bibliography follow-up distinct from reading the preface.
- **SRE chapter 1:** operational staffing, automation, incentives and ownership interact with technical architecture. The described engineering-time allocation and incident practices are organizational policies, not universal measured laws. Later comparison should examine whether Tycho connects operational costs to architectural decisions clearly enough.
- **SRE chapter 2:** distinguish a process/task, physical machine, cluster and geographical location. The sample deployment illustrates capacity while updating and failing, not a universal redundancy formula. Its explicit assumption about simultaneous task failures matters when correlated failure domains are present. The described infrastructure is a historical context, not a prescription for reproducing a particular stack.
- **SRE chapter 3:** choose reliability against user impact and cost. Request-weighted availability differs from elapsed uptime; aggregate success can hide unequal consequences. Separate service classes may justify different resource allocations. Error-budget policy needs authority and a feedback mechanism, not just an arithmetic remainder. The figures' two availability definitions were visually inspected.
- **SRE chapter 4:** an indicator requires a measurement boundary and population; a target requires product judgment. Aggregation can hide bursts and tail behavior. A published dependency promise and its observed behavior can diverge. Future comparison should assess definition templates, heterogeneous workload classes and expectation management separately from monitoring tooling.
- **SRE chapter 5:** repetitive operational work, administrative overhead and durable engineering improvements are different categories. Automation invocation can retain human cost. Averages can hide overloaded individuals. Compare future architectural recommendations with the actual recurring effort they remove, rather than treating every difficult task as waste.
- **OSTEP chapter 2:** virtualization, concurrency and persistence are separate foundational questions. Resource mechanisms and selection policies differ. Shared-state examples expose non-atomic updates; persistence involves storage ordering and recovery beyond a convenient file API. Simulated outcomes depend on model assumptions. This introductory chapter does not establish a particular JVM memory model, storage durability contract or implementation benchmark.

## Scope limits

No whole-book understanding is inferred from chapter summaries, contents or previous model knowledge. Exercises were read, not executed. Published references at chapter ends were read bibliographically, not automatically treated as fully read papers. No private companion corpus was consulted. No canonical book content, source registry or release metadata changed.

Detailed source-to-book comparison follows reading and stays in this research directory. The current notes are hypotheses for that comparison, not claims that Tycho omits every mentioned topic.
