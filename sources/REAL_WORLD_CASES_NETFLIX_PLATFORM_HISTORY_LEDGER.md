# M9 / E16-01 — Source Admission Wave 06: Netflix Historical Platform Evidence

**Source inspection:** 2026-10-19. **Nine candidate IDs:** src.m9-n03/src.m9-n04/src.m9-n08/src.m9-n13/src.m9-n15/src.m9-n16/src.m9-n17/src.m9-n19/src.m9-n20. **Evidence:** original public conference description, live Netflix Java team pages, public Netflix GitHub wiki, and attributed Netflix-authored historical technology blog publications. These document historical, version-scoped systems, NOT contemporary proof of all deployment details. Hyperlinking and independent summary do not grant permission to copy original diagrams/code.

| ID | Original author/publisher/date or snapshot | Primary original | Admission boundary |
|---|---|---|---|
| src.m9-n03 | Paul Bakker; JavaOne 2026 **2026-03-17** session | [JavaOne: How Netflix Uses Java, 2026 Edition](https://dev.java/community/javaone-2026/sessions/lrn1058/) | **Abstract only:** talk scope and >3,000 Java services as *organizer description*, no full talk result inferred |
| src.m9-n04 | Netflix Java Integration Framework (JIF) team; living page viewed **2026-10-19** | [Netflix JIF team](https://sites.google.com/netflix.com/javaplatformnetflix/jif) | Public platform/team charter only; no immutable publication date or deployment percentages |
| src.m9-n08 | Netflix/zuul public GitHub wiki, edited **2026-07-08** at inspection; **12 wiki revisions** visible | [Zuul 2.0 How It Works](https://github.com/Netflix/zuul/wiki/How-It-Works-2.0) | Public architectural mechanism; **no pinned Git wiki commit** yet; never treat mutable wiki as fixed source-code evidence |
| src.m9-n13 | Ketan Duvedi, Jinhua Li, Dhruv Garg, Philip Fisher-Ogden; Netflix TechBlog **2018-01-23** | [Scaling Time Series Data Storage — Part I](https://medium.com/netflix-techblog/scaling-time-series-data-storage-part-i-ec2b6d44ba39) | Historical viewing-data Cassandra/cache layout and published results |
| src.m9-n15 | Netflix Chaos Team: Ali Basiri, Lorin Hochstein, Abhijit Thosar, Casey Rosenthal; Netflix TechBlog **2015-09-25** | [Chaos Engineering Upgraded](https://medium.com/netflix-techblog/chaos-engineering-upgraded-878d341f15fa) | Historical **simulated regional outage**, not actual AWS Region shutdown or independently proven availability |
| src.m9-n16 | Netflix Real-Time Data Infrastructure Team, Netflix TechBlog **2016-02-15** | [Evolution of the Netflix Data Pipeline](https://medium.com/netflix-techblog/evolution-of-the-netflix-data-pipeline-da246ca36905) | Keystone was live Dec 2015; old period-only throughput figures |
| src.m9-n17 | Amer Hesson, Marcelo Mayworm, James Mulcahy, Brittany Truong; Netflix TechBlog **2026-05-11** | [Data Projects: Managing Data Assets at Netflix Scale](https://netflixtechblog.medium.com/data-projects-managing-data-assets-at-netflix-scale-7ca25888591e) | Public data-governance/identity design, not access-control proof beyond reported deployments |
| src.m9-n19 | Ed Bukoski, Brian Moyles and Mike McGarr; Netflix TechBlog **2016-03-09** | [How We Build Code at Netflix](https://medium.com/netflix-techblog/how-we-build-code-at-netflix-c5d9bd727f15) | Nebula/Jenkins/Aminator/Spinnaker paved road **in 2016**, not current JVM CI/CD |
| src.m9-n20 | Netflix JVM Ecosystem team charter; living page viewed **2026-10-19** | [Netflix JVM Ecosystem](https://sites.google.com/netflix.com/javaplatformnetflix/jvm) | Undated support remit and illustrative self-reported repository/artifact counts; revision not pinned |

## Bounded claim-to-source locations and counterclaims

| Claim | Exact publisher source section | What we can say | What we cannot say |
|---|---|---|---|
| evidence.m9-n03.001 | JavaOne session 'Summary', 'Profile' | 2026 organizers describe maintaining **>3,000 Java services** and topics Spring Boot, DGS, gRPC, generational ZGC, virtual threads and AOT | An abstract is **not** evidence any specific deployment gain or Java version adoption percentage |
| evidence.m9-n04.001 | 'OUR work' | JIF's **Spring Boot composable starters** cover service integrations including security, observability, REST, gRPC and GraphQL | No claim every Netflix team uses identical starter combination |
| evidence.m9-n08.001 | 'Architectural Overview' / 'Filters' | Zuul 2 is built on **Netty server/client** with inbound, endpoint and outbound filters; sync filters must **never block event loops** | It is **false** that all async code is automatically safe or that mutable wiki pins an implementation version |
| evidence.m9-n13.001 | 'Start Simple' | Viewing history started with Cassandra member-based partitions under a reported ~**9:1 write/read ratio** | An early Cassandra decision doesn't prove it stays optimal for 2026-scale data |
| evidence.m9-n13.002 | 'Results' | Historical reported **~6× less data**, **~13× less Cassandra maintenance time**, **~5× lower average read latency**, **~1.5× lower average write latency** after data model, parallelism and compression changes | Company-scoped 2018 measurements; not a direct recommendation for unrelated workload/cache compression |
| evidence.m9-n15.001 | 'Chaos Kong' and footnote | Chaos Kong **simulated** an AWS Region outage, unlike Chaos Monkey's server termination; the company says this helped prepare for a real 2015 US-EAST-1 DynamoDB incident | It did **not** actually power off AWS infrastructure and doesn't guarantee future global resiliency |
| evidence.m9-n15.002 | 'Chaos Kong' | Netflix reported a brief availability blip yet avoided significant impact during the **2015-09-20** regional service disruption | One historical outage and publisher attribution, not measured 99.9999% uptime |
| evidence.m9-n16.001 | Intro and 'data pipeline' | Keystone pipeline entered production **2015-12**; 2016 publication reported **~500B events/~1.3PB daily**, **~8M events/~24GB per second** at peak | Historical publisher-reported event traffic; never the entire Netflix 2026 pipeline |
| evidence.m9-n17.001 | 'The Problem: Managing Assets at Netflix Scale' | Per-table ACLs and author-bound workflow identity broke under reorgs and staff changes; project-level identity/asset ownership was introduced | Not proof of comprehensive audit/security success on every dataset |
| evidence.m9-n19.001 | Article's build/integrate/bake/deploy stages | Netflix described **Nebula/Gradle → Git/Jenkins → AMI baking → Spinnaker** as 2016 company paved road | Do not claim all current teams still use Jenkins masters and AMIs in 2026 |
| evidence.m9-n19.002 | 'The Road Ahead' | A specific Janitor Monkey cross-region deployment reportedly took **16 min**, including roughly **7 min** baking | One example, not fleet p99 release lead time; the authors themselves flagged bake latency as an issue |
| evidence.m9-n20.001 | 'Our work' / 'On the horizon' | Team manages JVM dependency/build/package/JDK-upgrade tooling, and an **undated** charter claims about **3,000 repos** producing **~9,000 JAR artifacts/day** | Treat these as **as-seen 2026-10-19 website claims with unknown measurement time**, not the 2023 or 2026 service-fleet count |

## Important correction to source triage

**src.m9-n15 is not inaccessible anymore:** this audit obtained and read the original Netflix-branded 2015 publication, including its crucial footnote differentiating a *simulated* region failure from a real AWS action. A retriever's earlier timeout was not proof the article was unusable. src.m9-n14 (Oct 2026 Netflix Conductor internal fork) still has an attributed syndication but **no directly verified original article body** in the reader; that source's status remains unresolved for primary-claim admission.

**src.m9-n08 remains revision-unpinned.** GitHub displays a dated wiki edit and number of revisions, but this is not the immutable wiki Git commit. Do not attach code-line provenance or claim reproducible source version until Git revision ownership and checkout are explicit.

**src.m9-n03 remains abstract-only.** The 2026 conference session scope does not prove present-day Netflix OpenJDK leadership, adoption of features in every service or performance results. The 2023 Netflix QCon talk src.m9-n02 is independent time-scoped evidence.

**Licensing:** no external diagram, source text or code material has been copied into the book. Code licenses for Netflix/zuul and potential cloned revisions are handled separately by existing public-source snapshot governance (K08/K09), not implicitly granted by viewing GitHub wiki.

## Source coverage checkpoint

With these nine historically bounded admissions, **32/43** original candidates have at least one reviewed source-specific claim and original location. **11** sources still need claim-level verification or transparent deferral. No standalone benchmark reproduction, publisher-permitted figure mirroring, independent review, whole-book re-enrichment or production index/graph/MCP run is claimed. #114 remains open.
