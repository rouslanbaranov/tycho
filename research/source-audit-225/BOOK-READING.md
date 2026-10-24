# Foundational book reading

Issue [#225](https://github.com/rouslanbaranov/tycho/issues/225). Updated 2026-10-24.
**SRE whole-book reading complete; OSTEP CPU and scheduling batch read;**
**wider reading and comparison in progress.** The owner prioritized foundational
books over further technology-reference auditing. Earlier reference readings remain
recorded; one whole book is now complete. The wider source-reading and Tycho
comparison obligations remain open.

## Current reading position

| Book | Actual progress | Next action |
| --- | --- | --- |
| Site Reliability Engineering | All 48 public book units read: 34 chapters, foreword, preface, five part introductions, six appendices and bibliography, with footnotes, tables, examples and embedded figures/formulas | Whole scoped book complete; compare exact passages with the frozen Tycho baseline and separately read linked publications; see `SRE-COMPLETION.md` |
| Operating Systems: Three Easy Pieces | Chapters 1, 3 and 4-11 read completely (10 new units; chapter 2 earlier): CPU virtualization, process API, limited direct execution and scheduling. 11 numbered units total; raster figures not visually inspected | Continue chapter 12 and the memory/VM chapters; then concurrency and persistence |
| Designing Data-Intensive Applications, 2nd edition | Publisher contents and short chapter 1 preview only | Full text requires lawful access; do not count the preview as chapter reading or silently substitute the first edition |
| Distributed Systems, 4th edition | Author's access instructions examined; no book text obtained | Personalized download requires an email and human-verification step; no request submitted |
| Other registered books | Not started in this audit | Continue `book-queue.json`; distinguish available complete texts from commercial previews |

## Reading notes for later comparison

These are short original notes, not Tycho corrections or completed chapter audits. Exact reading coverage and limitations are in `book-readings.json` and its linked continuation ledgers. Reported historical practices remain attributed to the source's setting and date.

- **SRE preface:** operational responsibility spans a system's lifecycle. General principles require translation from the source's environment; reliability goals and safety constraints cannot be transplanted without context. Keep bibliography follow-up distinct from reading the preface.
- **SRE chapter 1:** operational staffing, automation, incentives and ownership interact with technical architecture. The described engineering-time allocation and incident practices are organizational policies, not universal measured laws. Later comparison should examine whether Tycho connects operational costs to architectural decisions clearly enough.
- **SRE chapter 2:** distinguish a process/task, physical machine, cluster and geographical location. The sample deployment illustrates capacity while updating and failing, not a universal redundancy formula. Its explicit assumption about simultaneous task failures matters when correlated failure domains are present. The described infrastructure is a historical context, not a prescription for reproducing a particular stack.
- **SRE chapter 3:** choose reliability against user impact and cost. Request-weighted availability differs from elapsed uptime; aggregate success can hide unequal consequences. Separate service classes may justify different resource allocations. Error-budget policy needs authority and a feedback mechanism, not just an arithmetic remainder. The figures' two availability definitions were visually inspected.
- **SRE chapter 4:** an indicator requires a measurement boundary and population; a target requires product judgment. Aggregation can hide bursts and tail behavior. A published dependency promise and its observed behavior can diverge. Future comparison should assess definition templates, heterogeneous workload classes and expectation management separately from monitoring tooling.
- **SRE chapter 5:** repetitive operational work, administrative overhead and durable engineering improvements are different categories. Automation invocation can retain human cost. Averages can hide overloaded individuals. Compare future architectural recommendations with the actual recurring effort they remove, rather than treating every difficult task as waste.
- **SRE chapter 6:** monitoring for diagnosis and alerts requiring immediate human action serve different purposes. Latencies of successful and failed requests need separate interpretation. Error status alone can miss incorrect successful responses. Collection resolution, aggregation and sampling must fit the question being asked; simpler alert paths are easier to operate reliably.
- **SRE chapter 7:** repetitive execution and autonomous system design have different ownership and maintenance costs. The public historical examples expose incomplete rollout states, fragile assumptions in destructive selection and the need for bounded, observable recovery. Idempotence of a step does not automatically establish safety of a larger workflow. Benefits and percentages in the examples remain publisher self-reports.
- **SRE chapter 8:** source revision alone does not identify a release environment. Tools, dependencies, configuration, packaged artifacts and approval records also matter. Tests on main do not automatically cover a release with additional cherry picks. A movable package label and an immutable package identity serve different purposes. Different configuration distribution models trade independent updates against compatibility and reproducibility.
- **SRE chapter 9:** remove accidental complexity and unused behavior, preserve clear module/API boundaries, and keep releases understandable. Minimal interfaces and independent changes can reduce operational uncertainty. These are design principles, not a claim that splitting every component into a remote service improves reliability.
- **SRE chapter 10:** monitoring has its own storage, query, aggregation and failure-domain architecture. The examples compute per-instance rates before aggregation, explicitly addressing resets and missing samples in footnotes. Alert conditions combine population, threshold and persistence; a ratio alone need not trigger an alert. White-box collection cannot observe every request that fails before reaching the service. The historical rule language is not a verified current Prometheus specification.
- **SRE chapter 11:** staffing, response expectations, incident frequency, escalation and protected engineering time constrain an operational design. The chapter's numerical staffing examples depend on its rotation assumptions. Low alert activity does not alone establish readiness: familiarity and practice can decay. Avoid transferring the source's organizational targets as universal requirements.
- **SRE chapter 12:** mitigate impact while preserving evidence; separate a plausible hypothesis from a demonstrated cause. Diagnostic intervention can itself change timing or resource use. Rejected explanations and negative experiments retain value. The historical case distinguishes external-call tracing from local computation, showing why unchanged request volume does not imply unchanged work per request.
- **SRE chapter 13:** recovery depends on accessible administrative tools, communications, sufficient surviving capacity and functioning rebuild infrastructure. A rollback plan needs exercise, not just documentation. The cases distinguish restoring service from rebuilding lost capacity, and show how a nominally scoped test can expose hidden dependencies. The chapter extends an incident already discussed in chapter 7; do not double-count that as independent corroboration.
- **SRE chapter 14:** incident coordination separates technical modification, command, communications and planning. Explicit acknowledged handoff and a live state record help prevent uncoordinated changes. The response channel and state document need to remain available when the affected service is broken. The narrative is an illustrative scenario, not a measured experiment.
- **SRE chapter 15:** define review triggers before incidents; record contributing conditions, impact and preventive actions without assigning personal blame. Review and sharing are part of the learning process. The source's aspirations for automated prediction are future work in that text, not demonstrated capabilities.
- **SRE chapter 16:** an alert, an incident and a postmortem are different records. Aggregation can reveal repeated small problems that individual large-incident reviews miss. Tags support comparison but require interpretation: incident counts can reflect sensitive monitoring or client behavior and do not establish severity or causal contribution by themselves.
- **SRE chapter 17:** distinguish offline checks, live configuration checks, stress testing and exposure to production traffic. A clean test result covers a particular composition; mixed deployed versions can create additional combinations. Repair tools need restart, checkpoint and validation contracts. Reusing a random seed does not necessarily reproduce interleavings. Emergency release paths can preserve testing feedback even when deployment proceeds early. The numerical illustrations and formula images were read, not validated as general probabilistic guarantees.
- **SRE chapter 18:** capacity requests should retain their motivating constraints, dependency demands, priorities and performance assumptions. More resources in an unsuitable location may not solve a shortage. An optimization model can report unmet requirements, but its output still depends on input accuracy and modeling scope. The product-development case separates an initial heuristic from a later solver and discusses adoption and maintainable interfaces.
- **OSTEP chapter 2:** virtualization, concurrency and persistence are separate foundational questions. Resource mechanisms and selection policies differ. Shared-state examples expose non-atomic updates; persistence involves storage ordering and recovery beyond a convenient file API. Simulated outcomes depend on model assumptions. This introductory chapter does not establish a particular JVM memory model, storage durability contract or implementation benchmark.

## Scope limits

No whole-book understanding is inferred from chapter summaries, contents or previous model knowledge. Exercises were read, not executed. Published references at chapter ends were read bibliographically, not automatically treated as fully read papers. No private companion corpus was consulted. No canonical book content, source registry or release metadata changed.

Detailed source-to-book comparison follows reading and stays in this research directory. The current notes are hypotheses for that comparison, not claims that Tycho omits every mentioned topic.

## Completion continuation — SRE chapters 19–34 and remaining units

The prior chapter-19 continuation instruction is superseded by this completed reading. All 48 units in `sre-units.json` are now read. `sre-completion-readings.json` adds 29 exact records (B023–B051), including inspection of 44 embedded images in this continuation. References in earlier records describe what remained at those earlier checkpoints.

- **Chapter 19:** global routing must combine proximity, capacity and health. Resolver caching limits DNS control; stable connection mapping and packet encapsulation add different failure and size constraints. Protocol-status statements belong to the source's historical date.
- **Chapter 20:** connection count, request count and resource use are distinct. Subset selection affects balance and churn; fast errors can attract traffic under naive least-loaded selection. Graceful draining requires explicit client-visible state.
- **Chapter 21:** rejecting traffic consumes resources too. Client throttling, priority propagation, task protection and bounded retries address different layers. Sparse clients see less history; identical retry policy is unsuitable for local imbalance and broad overload.
- **Chapter 22:** remedial mechanisms can create positive feedback. Test beyond saturation and through recovery, including cold caches and slow dependencies. Distinguish process health from ability to serve, and propagate deadlines and cancellation.
- **Chapter 23:** consensus safety, eventual progress and operational availability have different prerequisites. Placement changes quorum latency, durability costs and correlated-failure exposure. The protocol overview is not a complete correctness specification.
- **Chapter 24:** scheduling agreement does not settle an uncertain external side effect. Recovery needs operation identity plus idempotency or authoritative outcome lookup. Persisting launch state, leadership boundaries and staggered execution solve different problems.
- **Chapter 25:** shortening periodic intervals can reduce progress when runs overlap. Exactly-once published results depend on current leases, immutable task/configuration identity, unique outputs and coordinator validation; they do not imply arbitrary effects execute once.
- **Chapter 26:** recovery must return usable data within its objective. Retention, early corruption detection, schema compatibility, media diversity and restore capacity all matter. Slow corruption can require selective recovery from different historical points.
- **Chapter 27:** launch review should scale with risk and remain concrete. Staged deployment and client controls reduce exposure; peak launch traffic may differ from steady-state traffic. Review cannot remove ongoing architectural growth constraints.
- **Chapter 28:** combine foundational reasoning, real tools, bounded failure practice and progressive ownership. A training checklist measures comprehension rather than mere document access; learning continues after joining the rotation.
- **Chapter 29:** protect sustained engineering time by making interrupt responsibility explicit. Queue assignment, handoffs and recurring-cause analysis are organizational design choices with reliability consequences.
- **Chapter 30:** temporary assistance should improve the team's ability to reason and prevent recurring work. Establish service objectives, reveal latent risks, demonstrate useful analysis and explain the reasons behind changes.
- **Chapter 31:** production review connects observed service behavior with architecture and action ownership. Shared tooling needs maintained components and explicit decisions. Migration equivalence requires actual output validation, not interface similarity alone.
- **Chapter 32:** late readiness review, early engagement and a common platform distribute responsibility differently. Standard control surfaces reduce repeated integration work, while application correctness still needs explicit ownership.
- **Chapter 33:** transfer preparedness, learning and decision principles with their assumptions. Failure consequences and acceptable change rates govern applicability; interview reports are not universal empirical proof.
- **Chapter 34:** operating experience should feed engineering improvements and usable controls. Increased system scale does not justify a proportional increase in manual work.
- **Foreword and five part introductions:** the book presents contextual accounts and a coherent reliability progression, not a universally applicable implementation recipe. The practices hierarchy links observation, response, learning, testing, capacity and design.
- **Appendix A:** time-based downtime tables assume a chosen window; operation-weighted success is often preferable under partial availability and varying traffic.
- **Appendix B:** connect configuration validation, staged change, user-visible objectives, incident learning, overload controls and sustainable ownership. Numeric staffing and redundancy guidance is contextual.
- **Appendix C:** an incident record separates current state, roles, exit conditions, tasks and timeline; the example is illustrative rather than a production observation.
- **Appendix D:** impact, contributing causes, trigger, response and follow-up actions have different roles. Action ownership and context matter; the example and its placeholders are not evidence of a real incident.
- **Appendix E:** the published checklist is explicitly historical and abridged. Its categories prompt dependency, capacity, failure, security, growth and rollout questions; it is not a current exhaustive standard.
- **Appendix F:** the sample meeting turns service metrics and incidents into tracked operational changes. It is an example, not an independently observed team practice.
- **Bibliography:** all entries read. Their publication texts, videos and code remain separate reading units; bibliography completion does not complete those dependencies.

## OSTEP continuation - CPU virtualization and scheduling

Ten records B052-B061 add chapters 1, 3 and 4-11; chapter 2 was read at the
earlier checkpoint. The records use the official publisher PDF URLs and a
plain-text reader representation retrieved on 2026-10-24. Raster figures were
not visually inspected; linked papers, simulator code and exercises were not
executed. Chapter 9's PDF footer says version 1.20 while the site table of
contents still says 1.10; the record keeps the chapter's printed version.

- **Chapter 1:** the book frames operating systems around virtualization,
  concurrency and persistence; this is scope framing, not an architecture
  taxonomy or technical evidence.
- **Chapter 3:** virtualization gives each consumer an illusion of a private
  resource over a shared physical resource; the sharing policy is deferred,
  and the metaphor does not establish isolation or capacity.
- **Chapter 4:** a process is a running program whose machine state includes
  address space, registers and I/O state; running/ready/blocked states are
  policy-visible abstractions, and xv6 adds lifecycle states including zombie.
- **Chapter 5:** fork() returns asymmetrically, wait() orders child completion,
  and exec() replaces the current program; the fork-exec gap enables shell
  redirection and pipes, while signals and ownership complete the control
  surface.
- **Chapter 6:** limited direct execution combines two privilege modes, a trap
  gate and a timer; protection depends on kernel-owned trap-table indirection,
  not on trapping alone. A context switch is two save/restore pairs plus a
  kernel-stack swap; syscall argument validation and interrupt masking remain
  explicit risks.
- **Chapter 7:** scheduling policy is derived by relaxing workload assumptions.
  Turnaround and response time are antagonistic metrics; FIFO, SJF, STCF and
  RR expose the trade-off, and slice length must amortize switch cost.
- **Chapter 8:** MLFQ infers job class from observed CPU use, combining strict
  priority with intra-queue round robin, demotion on cumulative use and a
  periodic boost. Starvation and gaming remain policy costs; the boost interval
  is a tuned constant, not a derived guarantee.
- **Chapter 9:** lottery scheduling gives probabilistic expected shares, stride
  scheduling is exact per cycle but needs global pass state, and CFS uses
  nice-derived weights, vruntime and a red-black tree. Linux 6.6 moved to
  EEVDF; ticket assignment remains an unresolved policy choice.
- **Chapter 10:** cache coherence does not make compound shared updates atomic.
  SQMS is simple but lock-contended and affinity-hostile; MQMS scales but needs
  migration or work stealing, with a tuned overhead/imbalance trade-off.
- **Chapter 11:** the summary separates mechanism (traps, timer, context switch)
  from policy (priority, quantum, feedback) and treats metric conflict as a
  design trade-off rather than a solvable constant.

The batch advances reading, not source-to-book completeness. Candidate
comparisons are recorded in [comparisons.json](comparisons.json); they are
questions, not defects or proposed book edits.
