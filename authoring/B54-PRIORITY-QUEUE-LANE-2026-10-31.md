# B54 — Priority Queue four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 0/4 at the parent HEAD: mechanism, invariant, failure/recovery and
alternative were all partial. This lane binds all four to five public units
read on 2026-10-31, labels the max-wait/aging rule, per-level capacity and
tenant cap as Tycho, and keeps the card inline in V11/C07. The lane commit
edits only the two book files and this note.

## Lane coordinates

- Parent HEAD: 65918d896c1dfdc4db39699c617fa6c29a1e0292 (65918d89).
- Branch: b54-priority-queue; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b54-priority-queue.
- Scope: the owner section "### Priority Queue" in V07/C05 and the inline
  V11/C07 card "### Priority Queue".
- Owner path (concatenate):

      book/volumes/v07-performance-scale-and-resilience/
      c05-overload-protection-and-graceful-degradation/
      admission-resource.md

- Card path: book/volumes/v11-pattern-atlas/c07-resilience/README.md.
- Exactly three files change: the owner page, the inline card and this note.
- No shared JSON file is edited.
- Existing source ids used: src.rabbitmq, src.microsoft-cloud-patterns and
  src.aws-sqs.
- New source id proposed: src.azure-service-bus-amqp, used only by the owner
  and card frontmatter until the integrator registers it.
- New ledger records proposed: five, listed below.
- Retained record: read.batch4-rabbit-priority.2026-10-21 remains historical;
  its content_sha256 does not match the 2026-10-31 RabbitMQ representation.
- Baseline and final line-length and boundary checks pass.

## Baseline and gap

edition/patterns/owner-units.v1.json records all four dimensions as partial.
Every reason is: "Local representation is a Cloudflare challenge page; the
RabbitMQ unit text is absent." The owner section already stated the mechanism,
invariant, failure/recovery and alternative as Tycho guidance, but no exact
public quote, section and representation hash were bound to the four
dimensions. The four owner-unit quote sentences are preserved verbatim:

- mechanism: "A priority queue is a broker-side ordering policy"
- invariant: "The queue must define class levels, per-level capacity and the
  broker's actual priority support."
- failure_recovery: "Add aging or a maximum-wait rule so low classes make
  progress"
- alternative: "An admission-controlled FIFO or separate lanes per class
  avoids starvation when priority is unverifiable."

The base owner page SHA-256 is
68181cf76bed23f7a9d17d9c2a52d2a9b9bb75c8fbd50e0d1c7f9ec5e18700d8. It
matches the page_sha256 in the sufficient-candidates re-review record. The
base card SHA-256 is
b6e000bc832668169a0e5a16bc5771d872757b2e6858d381da6f090f81f213b9.

The gap was evidential, not a missing mechanism. The local RabbitMQ snapshot
was a Cloudflare challenge page, so the recorded unit could not support the
owner section. The 2026-10-31 live public page is readable and quotable. The
selected Azure units are the official Architecture Center Priority Queue
pattern and the Service Bus AMQP protocol guide. The pattern documents
priority as an application property routed by SQL filters; the AMQP guide
maps no `priority` header to a Service Bus API. The selected AWS units
document queue-type ordering and fair-queue behavior; neither defines a
native message-priority field. Shared metadata still shows 0/4 until the
integrator applies the proposals below.

## Candidate evaluation

- RabbitMQ, "Priority Support in Queues" (selected). It defines classic and
  quorum priority support, publisher-assigned integer priorities, the
  `x-max-priority` declaration range, quorum 0-31 behavior, starvation,
  strict-priority delay, prefetch inversion, max-length drop behavior and
  multiple-queue alternatives. Primary source for mechanism and
  failure/recovery.
- Microsoft Learn, "Priority Queue pattern" (selected). It defines the
  application-assigned priority value, single-queue and multiple-queue
  approaches, consumer-pool designs, starvation risk and age-based priority
  promotion. Its worked example uses Azure Service Bus topics, a custom
  `Priority` application property and SQL filters. Primary source for the
  application-level invariant and the aging technique.
- Microsoft Learn, "AMQP 1.0 in Azure Service Bus and Event Hubs" (selected).
  Its "Messages" section maps standard AMQP header fields to Service Bus API
  names. The `priority` row has no usage and no API name, and application
  properties are directed to the AMQP application-properties map. Primary
  source for the native Service Bus priority boundary.
- AWS, "Amazon SQS queue types" (selected). It defines standard and FIFO
  queues, best-effort ordering and ordered delivery within a message group.
  Primary source for the FIFO side of the alternative.
- AWS, "Amazon SQS fair queues" (selected). It defines dwell time, noisy-neighbor
  rebalancing, tenant-level prioritization without a per-tenant consumption
  cap, and age monitoring. Primary source for the fair-queue side of the
  alternative and a supporting failure/recovery age signal.
- RabbitMQ, "Consumer Priorities" (considered, not selected). It describes
  consumer allocation while a consumer is active or blocked, not message
  priority, queue declaration or aging. It is not bound to a dimension.
- RabbitMQ, "Reliability Guide" (retained, not selected). It is a delivery and
  acknowledgement citation, not priority support. The card no longer uses the
  old reliability record as the priority source.
- AWS, "What is Amazon Simple Queue Service?" (retained, not selected). It
  covers durability, lifecycle and retention, not queue-type ordering or
  priority handling.
- No broker, queue, consumer, filter or fair-queue feature was created or
  executed. No benchmark or production observation is used.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Two fetches per URL were
byte-identical. Canonical text was extracted with
scripts/source_content_hash.py. None of the five pages exposes the script's
article-body markers, so each canonical digest covers visible page text
including navigation chrome. Raw HTML SHA-256 is over the decoded response
body. Quotes were checked as whitespace-normalized substrings; link-extraction
spaces before punctuation are not reproduced.

### R1 — RabbitMQ, Priority Support in Queues

- Record: read.rabbitmq-priority-queues.2026-10-31 (proposed).
- Source: src.rabbitmq (existing).
- URL: https://www.rabbitmq.com/docs/priority
- Label/type: "Priority Support in Queues — RabbitMQ documentation";
  documentation-page; documentation version 4.4.
- Representation: HTTP/2 200 on 2026-10-31T17:01:09Z; 57,138-byte decoded
  text/html; no Last-Modified; ETag
  W/"156c44d42d25101b08d798ed7bff7c9c"; raw HTML SHA-256
  33dbbae94a1c62a8c4fc84cadc5ebe6fbd351fe3b519c5b2af4f89027bc9021f;
  canonical text 13,684 characters / 2,189 words, SHA-256
  4ca982ad871d4c03eabc5545059ce945bade5ee5da444132361401119438dc45.
- Sections read: "What is a Priority Queue"; "Before Adopting Priority
  Queues: Consider the Alternatives"; "Declaration and Supported Priority
  Ranges" including "Classic Queues", "Configuring the Maximum Number of
  Priorities", "Using Client-provided Optional Arguments", "Quorum Queues" and
  "Priorities Are Always Enabled"; "Priority Queue Behaviour" including
  "Quorum Queue Specifics", "Per-Priority Message Counts", "Redelivery of
  Returned Messages" and "Priority-Aware Message Expiration"; "Low Message
  Priority and the Resource Starvation Problem"; "Maximum Number of Priorities
  and Resource Usage"; "How Priority Queues Work with Consumers" including
  "Example" and "Now Add Priorities"; "Interaction with Other Features"; "Why
  Policy Definition is not Supported for Priority Queues".
- Sections not read: linked RabbitMQ tutorials, client API pages and examples
  as separate units; navigation chrome as a unit. Example code was read as
  text, not executed.
- Claims supported: classic and quorum queues support priorities; ready
  messages are dispatched by priority; publishers set a positive integer;
  larger numbers indicate higher priority; classic queues take
  `x-max-priority` in [1, 255]; quorum queues expose 0-31 and ignore
  `x-max-priority`; declaration fixes the priority count; missing priority
  defaults to 4 for quorum and 0 for classic; starvation, strict-priority
  delay, prefetch inversion, max-length drop and TTL-head behavior are
  documented.
- Limits: one living documentation page, not a benchmark or release-tagged
  specification. The page version was 4.4 at retrieval; the digest pins the
  2026-10-31 representation, not every RabbitMQ release. No broker was run.

### R2 — Microsoft Learn, Priority Queue pattern

- Record: read.microsoft-priority-queue-pattern.2026-10-31 (proposed).
- Source: src.microsoft-cloud-patterns (existing).
- URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/priority-queue
- Label/type: "Priority Queue pattern — Azure Architecture Center";
  pattern-page.
- Representation: HTTP/2 200 on 2026-10-31T17:01:11Z; 63,858-byte text/html;
  Last-Modified 2026-09-17T05:03:54Z; ETag
  "DH7Jopyv59XUz+WCrc5vDmL+kqY="; ms.date 2026-08-11T00:00:00Z;
  updated_at 2026-09-17T05:02:00Z; git_commit_id
  96c2e16cbf46d319d4e9b15e285f462de05e29e2; document_version_independent_id
  0a9e98f2-e2a1-3570-ff72-aa2e39bc29a9; raw HTML SHA-256
  b979c68fe300b12e250067e69409e989bea6e482c1b08628c29fbd436519d534;
  canonical text 12,954 characters / 1,872 words, SHA-256
  da8e65b90263acd29305315fdba36da3e6b4127e688532f1132ed681eb4c1fde.
- Sections read: "Context and problem"; "Solution"; "Single queue"; "Multiple
  queues"; "Single consumer pool"; "Multiple consumer pools"; "Problems and
  considerations"; "General recommendations"; "Multiple queue
  recommendations"; "When to use this pattern"; "Workload design"; "Example".
- Sections not read as separate units: "Next steps", "Related resources",
  feedback and site chrome; linked pages, images and the GitHub sample
  deployment. No deployment was run.
- Claims supported: priority is assigned by the application or producer;
  single-queue and multiple-queue approaches; consumer-pool designs; a single
  pool can delay lower priorities indefinitely; low-priority items may need
  age-based priority promotion; the Service Bus example uses a custom
  `Priority` application property, SQL filters and high/low subscriptions;
  strict FIFO or cross-priority ordering dependencies are contraindications.
- Limits: one living pattern page with no semantic version. It documents a
  pattern and a Service Bus example, not a native Service Bus priority field.
  The canonical digest covers page chrome. No Service Bus namespace, topic,
  filter or subscription was created.

### R5 — Microsoft Learn, AMQP 1.0 in Azure Service Bus and Event Hubs

- Record: read.azure-service-bus-amqp-message-mapping.2026-10-31 (proposed).
- Source: src.azure-service-bus-amqp (proposed; new source id).
- URL:
  https://learn.microsoft.com/en-us/azure/service-bus-messaging/
  service-bus-amqp-protocol-guide
  (concatenate the two lines).
- Label/type: "AMQP 1.0 in Azure Service Bus and Event Hubs protocol guide —
  Azure Service Bus"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T17:06:10Z; 102,686-byte
  text/html; Last-Modified 2026-10-24T22:16:01Z; ETag
  "RK1ukalJWzu5YPxlYuPYhgDOWtk="; ms.date 2024-11-18T00:00:00Z; updated_at
  2026-10-13T22:18:00Z; git_commit_id
  bb63da0dc31787d3949b8217dfd538f641e78c00; document_version_independent_id
  9c6be489-f9d8-9b66-09f8-18be4ec77f3b; raw HTML SHA-256
  7048def99d18f4c4bad3784fe92a8456051631574bc633c13ee0fec75823e883;
  canonical text 40,179 characters / 6,042 words, SHA-256
  a1d6a361f205a21ff53f6323a87ad27dd9dd5efc15f136c8d829f896e16cbaab.
- Sections read: "Messages", including "Header" and "Properties".
- Sections not read as separate units: "Goals", "What is AMQP?", "Basic AMQP
  scenarios" (connections, sessions, links, transfers, flow control), "Transaction
  capability", "Advanced Service Bus capabilities", related content, linked
  pages, code samples and images. The whole served text was extracted, but
  only the message-mapping section is bound.
- Claims supported: the guide maps standard AMQP message properties to the
  Service Bus API set; the `priority` header row has no usage and no Service
  Bus API name; application-defined properties belong in the AMQP
  application-properties map; `ttl` maps to TimeToLive and `delivery-count`
  maps to DeliveryCount.
- Limits: one section of a long protocol guide; it documents the mapping, not
  a Service Bus priority feature or a broker experiment. The canonical digest
  covers the whole page including chrome. No Service Bus message was sent and
  no priority header was exercised.

### R3 — AWS, Amazon SQS queue types

- Record: read.aws-sqs-queue-types.2026-10-31 (proposed).
- Source: src.aws-sqs (existing).
- URL:
  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/
  sqs-queue-types.html
  (concatenate the two lines).
- Label/type: "Amazon SQS queue types — Amazon SQS Developer Guide";
  documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T17:01:13Z; 23,591-byte text/html;
  Last-Modified 2026-10-31T03:34:37Z; ETag
  "DEYh/DqMmoxHOA+bd2gt3VNjdMU="; raw HTML SHA-256
  c6210c4d6ba382b7801c5576a22d9338028b96cd1fe4beff707b4d0c05f3dd3d;
  canonical text 5,786 characters / 905 words, SHA-256
  c9ccf72844c5180d80502042f9abf7766b8af7e194f217065ddf50a43f540609.
- Sections read: "Amazon SQS queue types" (the whole page, including the
  standard/FIFO comparison table and usage examples).
- Sections not read: linked FIFO, high-throughput, batching and quota pages,
  navigation chrome and images.
- Claims supported: SQS has standard and FIFO queues; standard queues provide
  best-effort ordering; FIFO queues preserve order within each message group;
  multiple groups can be processed in parallel while preserving order within
  a group; FIFO provides exactly-once processing within its documented scope.
  The page does not define a message-priority field or priority queue.
- Limits: one living AWS documentation page with no published version
  identifier. The canonical digest includes served navigation chrome. No
  queue was created and no message was sent or received.

### R4 — AWS, Amazon SQS fair queues

- Record: read.aws-sqs-fair-queues.2026-10-31 (proposed).
- Source: src.aws-sqs (existing).
- URL:
  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/
  sqs-fair-queues.html
  (concatenate the two lines).
- Label/type: "Amazon SQS fair queues — Amazon SQS Developer Guide";
  documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T17:01:15Z; 22,622-byte
  text/html; Last-Modified 2026-10-31T03:34:35Z; ETag
  "oVl95SiV/oQcNWFINihy+1sWm9w="; raw HTML SHA-256
  ab0a62a5e64d732cba5d3b072469183ea01305f01ef797bc700cf43e1a1fdfc7;
  canonical text 6,351 characters / 1,000 words, SHA-256
  9d0821490fbdd48ed28c195c3b5bdc466d800d34383b1caf36dd802ec0e7ca5f.
- Sections read: "Amazon SQS fair queues"; "Steady state"; "Noisy neighbor
  impact"; "Mitigation with fair queues"; "How to use fair queues"; "When to
  use fair queues"; "Fair queues CloudWatch metrics".
- Sections not read: linked "How Amazon SQS fair queues work" detail page,
  CloudWatch metrics reference, images and navigation chrome.
- Claims supported: fair queues mitigate noisy-neighbor impact in multi-tenant
  queues; dwell time measures arrival-to-processing time; SQS prioritizes
  message delivery for other tenants when one tenant has disproportionate
  in-flight messages; fair queues do not limit consumption per tenant;
  `MessageGroupId` is a tenant identifier on standard queues and does not
  enforce order; older message ages can appear in queue-level metrics.
- Limits: one living AWS documentation page with no published version
  identifier. Fair queues are tenant fairness, not a business priority-level
  field, aging knob or per-tenant quota. No queue was created or exercised.

## Selected exact quotes

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. Every quote below passed the whitespace-normalized substring check
against the named canonical representation. Two quotes omit a terminal period
because the extraction inserts a space before it (R1 "resource starvation ."
and R2 "Low ."); the words are unchanged. Tycho-labelled sentences in the book
are not source quotes.

### Mechanism

- Q1, RabbitMQ, section "What is a Priority Queue":

      Classic and quorum queues in RabbitMQ support priorities.

- Q2, RabbitMQ, section "What is a Priority Queue":

      Priority queues deliver messages in the order of message priorities.

- Q3, RabbitMQ, section "What is a Priority Queue":

      A message priority is a positive integer value set by publishers at
      publishing time.

- Q4, RabbitMQ, section "Using Client-provided Optional Arguments":

      To declare a priority queue, use the x-max-priority optional queue
      argument.

- Q5, RabbitMQ, section "Using Client-provided Optional Arguments":

      Larger numbers indicate higher priority.

### Invariant

- Q6, RabbitMQ, section "Why Policy Definition is not Supported for Priority
  Queues":

      Priority queues can never change the number of priorities they support
      after queue declaration

- Q7, RabbitMQ, section "Priorities Are Always Enabled":

      Quorum queues always provide the full 0-31 priority range.

- Q8, RabbitMQ, section "Quorum Queues":

      Messages without a priority property are treated as priority 4 (classic
      queues default to 0).

- Q9, Azure, section "Solution":

      The application or producer that sends a request assigns a priority value
      to the message, and consumers process the messages by priority.

- Q10, Azure, section "Example":

      The PriorityQueueSender application creates messages, assigns a custom
      application property called Priority to each message, and sets the
      Priority value to High or Low

- Q11, Azure, section "Example":

      Service Bus uses SQL filters to route each message to the high-priority or
      low-priority subscription, based on its Priority value.

- Q31, Service Bus AMQP guide, section "Messages":

      The following sections explain which properties from the standard AMQP
      message sections are used by Service Bus and how they map to the Service
      Bus API set.

- Q32, Service Bus AMQP guide, section "Messages":

      Any property that application needs to define should be mapped to AMQP's
      application-properties map.

Table-row evidence, Service Bus AMQP guide, section "Messages": the served
mapping table contains the row `priority - -`, with no usage entry and no
Service Bus API name. The adjacent table rows map `ttl` to TimeToLive and
`delivery-count` to DeliveryCount.

### Failure and recovery

- Q12, RabbitMQ, section "Low Message Priority and the Resource Starvation
  Problem":

      A common issue with priority-based message delivery is resource starvation

- Q13, RabbitMQ, section "Low Message Priority and the Resource Starvation
  Problem":

      In the context of priority queues, this means that only messages with
      higher priorities are delivered, and lower-priority messages are never
      delivered.

- Q14, RabbitMQ, section "Low Message Priority and the Resource Starvation
  Problem":

      Starting with RabbitMQ 4.3, quorum queues implement strict priority with
      no such interleaving: a sustained stream of higher-priority messages will
      delay lower-priority ones indefinitely.

- Q15, RabbitMQ, section "Low Message Priority and the Resource Starvation
  Problem":

      Workloads that need a guaranteed share of attention for lower-priority
      traffic should use separate queues per priority class

- Q16, RabbitMQ, section "How Priority Queues Work with Consumers":

      higher prioritised messages may in practice need to wait for lower
      priority messages to be processed first.

- Q17, RabbitMQ, section "Interaction with Other Features":

      This means that higher priority messages might be dropped to make way for
      lower priority ones

- Q18, Azure, section "Single consumer pool":

      This setup can lead to lower-priority messages being continually delayed
      and potentially never processed.

- Q19, Azure, section "General recommendations":

      Consider low-priority processing. Decide whether all high-priority items
      must be processed before any lower-priority items. If possible,
      dynamically increase the priority of old messages to ensure that
      low-priority messages eventually get processed.

- Q20, AWS SQS fair queues, section "Fair queues CloudWatch metrics":

      the general queue-level metrics might reveal increasing backlogs or older
      message ages.

- Q21, AWS SQS fair queues, section "Mitigation with fair queues":

      Amazon SQS does not limit the consumption rate per tenant.

### Alternative

- Q22, AWS, section "Amazon SQS queue types":

      Amazon SQS supports two types of queues: standard queues and FIFO queues.

- Q23, AWS, section "Amazon SQS queue types":

      Best-effort ordering – Provides best-effort ordering, meaning that while
      Amazon SQS attempts to deliver messages in the order they were sent, it
      does not guarantee this.

- Q24, AWS, section "Amazon SQS queue types":

      FIFO queues ensure that you receive messages in the order they are sent
      within each message group.

- Q25, AWS, section "Amazon SQS queue types":

      By distributing messages across multiple groups, you can process them in
      parallel while still maintaining the order within each group.

- Q26, AWS SQS fair queues, section "Amazon SQS fair queues":

      Amazon SQS fair queues automatically mitigates the noisy-neighbor impact
      in multi-tenant queues that contain messages from multiple logical
      entities, such as customers, client applications, or message types.

- Q27, AWS SQS fair queues, section "Mitigation with fair queues":

      When a tenant has a disproportionately large number of in-flight messages
      compared to others, Amazon SQS identifies that tenant as a noisy neighbor
      and prioritizes message delivery for other tenants.

- Q28, AWS SQS fair queues, section "How to use fair queues":

      On standard queues, MessageGroupId is used only as a tenant identifier
      for fair queues and does not enforce message ordering.

- Q29, RabbitMQ, section "Before Adopting Priority Queues: Consider the
  Alternatives":

      Use multiple queues instead of one.

- Q30, Azure, section "Multiple queues":

      Multiple queues separate messages by priority.

## Dimension mapping

- Mechanism. Primary: Q1-Q5, record
  read.rabbitmq-priority-queues.2026-10-31, sections "What is a Priority
  Queue" and "Using Client-provided Optional Arguments", revision
  4ca982ad871d4c03eabc5545059ce945bade5ee5da444132361401119438dc45.
  Supporting: Q9-Q11 for the application-assigned form. Owner quote: "A
  priority queue is a broker-side ordering policy". Tycho reading: the broker
  orders ready messages by class; it does not preempt a running handler, and
  it does not admit or authenticate the class by itself.
- Invariant. Primary: Q31-Q32 and the `priority - -` mapping row, record
  read.azure-service-bus-amqp-message-mapping.2026-10-31, section "Messages",
  revision
  a1d6a361f205a21ff53f6323a87ad27dd9dd5efc15f136c8d829f896e16cbaab.
  Supporting: Q9-Q11 (application property plus SQL filters), Q6-Q8
  (declaration fixes the priority count and default class) and Q1 (broker
  support is version/queue-type specific). Owner quote: "The queue must define
  class levels, per-level capacity and the broker's actual priority support."
  Tycho rule: treat the class as authenticated application metadata; declare
  the full class set, default and routing before admission; map each class to
  a bounded lane or subscription; cap each tenant's share. The AMQP guide maps
  no Service Bus priority header; the official pattern uses an application
  property and SQL filters instead.
- Failure and recovery. Primary: Q12-Q17, record
  read.rabbitmq-priority-queues.2026-10-31, sections "Low Message Priority and
  the Resource Starvation Problem", "How Priority Queues Work with Consumers"
  and "Interaction with Other Features", revision
  4ca982ad871d4c03eabc5545059ce945bade5ee5da444132361401119438dc45.
  Supporting: Q18-Q19 (single-pool delay and age-based promotion), Q20-Q21
  (age signal and no per-tenant cap) and Q15 (separate queues). Owner quote:
  "Add aging or a maximum-wait rule so low classes make progress". Tycho
  runbook: define a maximum wait and aging/promotion rule; monitor per-class
  age; reserve lower-class capacity where strict priority is unsafe; test
  strict mode, prefetch, max-length and TTL behavior. The broker does not
  supply a universal max-wait or aging bound; the rule is Tycho synthesis.
- Alternative. Primary: Q22-Q28, records
  read.aws-sqs-queue-types.2026-10-31 and
  read.aws-sqs-fair-queues.2026-10-31, revisions
  c9ccf72844c5180d80502042f9abf7766b8af7e194f217065ddf50a43f540609 and
  9d0821490fbdd48ed28c195c3b5bdc466d800d34383b1caf36dd802ec0e7ca5f.
  Supporting: Q29-Q30 (multiple queues). Owner quote: "An admission-controlled
  FIFO or separate lanes per class avoids starvation when priority is
  unverifiable." Tycho choice rule: admission-controlled FIFO when per-group
  order dominates; tenant-fair queues when fairness dominates; separate
  priority lanes when classes are stable and capacity can be partitioned.
  Reverse when inversion, starvation or queue-management cost exceeds the
  latency benefit.

## Book edits

### Owner page

- Path (concatenate):

      book/volumes/v07-performance-scale-and-resilience/
      c05-overload-protection-and-graceful-degradation/
      admission-resource.md

- Frontmatter adds src.rabbitmq, src.microsoft-cloud-patterns,
  src.azure-service-bus-amqp and src.aws-sqs to evidence_scope.source_ids;
  rewrites the notes as a folded block; sets
  content_review.reviewed_at and reviewer to 2026-10-31 and "Automated
  authoring agent"; sets updated_at and source_inspection_date to 2026-10-31.
- The Priority Queue section keeps all four owner-unit quotes verbatim and
  adds labelled mechanism, invariant, failure/recovery, alternative,
  bound-source and source-unit paragraphs. The heading is line 187; the
  section is 104 lines and 873 words.
- Page 300 lines; 2,680 words; SHA-256
  4441a43732be430e96f598d7064260c3b8d27693aded548c855e54026d840a56.
- Section SHA-256 (heading through the last source-unit bullet):
  7e688a4bd4262e5e821083075628df169eaf0cd4aeae388ee82dcd2325bb1c1c.

### Inline card

- Path: book/volumes/v11-pattern-atlas/c07-resilience/README.md.
- Frontmatter adds src.azure-service-bus-amqp and rewrites
  evidence_scope.notes to name the 2026-10-31 Priority Queue binding. The
  other three source ids were already present. No review date change was
  needed because the card was already at 2026-10-31.
- "Good-fit conditions", "Hard contraindications", "Competing alternative",
  "Failure and recovery" and "Sources" now bind the five records, revisions
  and source limits; the owner link and anchor are unchanged. The heading is
  line 355; the section is 66 lines and 396 words.
- Page 514 lines; 2,623 words; SHA-256
  beaec86670b0c07b0e908e7eb0b9f7c9f8fdd8890cc0b38205fcd498b85ed14d.
- Section SHA-256 (heading through "Related entries"):
  4d1fb001bb0ed5cb313fa8a3c10585580b16bd84f43fd6a3bc431e79bcf71c7e.
- No other book file, edition JSON, promotion or generated file is changed.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
entry can move to 4/4 supported and before review hashes can be rebound.

### Source register sources/register.json

Set updated to 2026-10-31. Keep the three existing source ids and add one new
source, src.azure-service-bus-amqp. Extend each version and
verification_scope with the 2026-10-31 representation.

- src.rabbitmq: append "Priority Support in Queues" docs version 4.4;
  57,138 bytes; no Last-Modified; ETag
  W/"156c44d42d25101b08d798ed7bff7c9c"; raw HTML SHA-256
  33dbbae94a1c62a8c4fc84cadc5ebe6fbd351fe3b519c5b2af4f89027bc9021f;
  canonical text 13,684 characters / SHA-256
  4ca982ad871d4c03eabc5545059ce945bade5ee5da444132361401119438dc45;
  HTTP Date 2026-10-31T17:01:09Z; access and content-verified 2026-10-31.
  Scope: the sections listed in R1, excluding linked pages.
- src.microsoft-cloud-patterns: append "Priority Queue pattern";
  63,858 bytes; Last-Modified 2026-09-17T05:03:54Z; ETag
  "DH7Jopyv59XUz+WCrc5vDmL+kqY="; ms.date 2026-08-11; updated_at
  2026-09-17T05:02:00Z; git_commit_id
  96c2e16cbf46d319d4e9b15e285f462de05e29e2; raw HTML SHA-256
  b979c68fe300b12e250067e69409e989bea6e482c1b08628c29fbd436519d534;
  canonical text 12,954 characters / SHA-256
  da8e65b90263acd29305315fdba36da3e6b4127e688532f1132ed681eb4c1fde;
  HTTP Date 2026-10-31T17:01:11Z; access and content-verified 2026-10-31.
  Scope: the sections listed in R2, excluding linked pages and sample code.
- src.azure-service-bus-amqp (new): title "AMQP 1.0 in Azure Service Bus and
  Event Hubs"; category messaging; publisher "Microsoft Learn"; kind
  official-docs; URL
  https://learn.microsoft.com/en-us/azure/service-bus-messaging/
  service-bus-amqp-protocol-guide; topics service-bus, amqp,
  message-properties and priority; priority core; admission
  admitted-for-research; reading status full-public-page-inspected; the
  bound scope is the "Messages" section only; version with the 2026-10-31
  representation: 102,686 bytes; Last-Modified 2026-10-24T22:16:01Z; ETag
  "RK1ukalJWzu5YPxlYuPYhgDOWtk="; ms.date 2024-11-18; updated_at
  2026-10-13; git_commit_id
  bb63da0dc31787d3949b8217dfd538f641e78c00; raw HTML SHA-256
  7048def99d18f4c4bad3784fe92a8456051631574bc633c13ee0fec75823e883;
  canonical text 40,179 characters / SHA-256
  a1d6a361f205a21ff53f6323a87ad27dd9dd5efc15f136c8d829f896e16cbaab;
  HTTP Date 2026-10-31T17:06:10Z; access and content-verified 2026-10-31;
  license note "Public Microsoft Learn documentation; cite short excerpts and
  paraphrase; do not mirror."; verification scope names "Messages",
  "Header" and "Properties" and excludes linked pages and executed code.
- src.aws-sqs: append "Amazon SQS queue types" and "Amazon SQS fair queues".
  Queue types: 23,591 bytes; Last-Modified 2026-10-31T03:34:37Z; ETag
  "DEYh/DqMmoxHOA+bd2gt3VNjdMU="; raw HTML SHA-256
  c6210c4d6ba382b7801c5576a22d9338028b96cd1fe4beff707b4d0c05f3dd3d;
  canonical text 5,786 characters / SHA-256
  c9ccf72844c5180d80502042f9abf7766b8af7e194f217065ddf50a43f540609;
  HTTP Date 2026-10-31T17:01:13Z. Fair queues: 22,622 bytes; Last-Modified
  2026-10-31T03:34:35Z; ETag "oVl95SiV/oQcNWFINihy+1sWm9w="; raw HTML
  SHA-256 ab0a62a5e64d732cba5d3b072469183ea01305f01ef797bc700cf43e1a1fdfc7;
  canonical text 6,351 characters / SHA-256
  9d0821490fbdd48ed28c195c3b5bdc466d800d34383b1caf36dd802ec0e7ca5f;
  HTTP Date 2026-10-31T17:01:15Z. Access and content-verified 2026-10-31.
  Scope: the sections listed in R3 and R4, excluding linked pages and images.

### Reading ledger edition/patterns/reading-ledger.v1.json

Add five records. Common fields: access_date 2026-10-31; access_method "public
HTTP fetch on 2026-10-31; two fetches byte-identical; ..." with the raw and
canonical digests, HTTP Date and cache headers from R1-R5; license_notes "Public
<vendor> documentation; cite short excerpts and paraphrase; do not mirror.";
tables_figures "tables and figures in the inspected sections were read in text
form; not reproduced"; reviewer "Automated authoring agent"; status "read".
Each content_sha256 is the canonical-text SHA-256 named below.

- read.rabbitmq-priority-queues.2026-10-31 — source src.rabbitmq; unit
  "Priority Support in Queues — RabbitMQ documentation"; unit_type
  documentation-page; content_sha256
  4ca982ad871d4c03eabc5545059ce945bade5ee5da444132361401119438dc45;
  sections_read and limits as R1.
- read.microsoft-priority-queue-pattern.2026-10-31 — source
  src.microsoft-cloud-patterns; unit "Priority Queue pattern — Azure
  Architecture Center"; unit_type pattern-page; content_sha256
  da8e65b90263acd29305315fdba36da3e6b4127e688532f1132ed681eb4c1fde;
  sections_read and limits as R2.
- read.azure-service-bus-amqp-message-mapping.2026-10-31 — source
  src.azure-service-bus-amqp; unit "AMQP 1.0 in Azure Service Bus and Event
  Hubs protocol guide — Azure Service Bus"; unit_type documentation-page;
  content_sha256
  a1d6a361f205a21ff53f6323a87ad27dd9dd5efc15f136c8d829f896e16cbaab;
  sections_read and limits as R5.
- read.aws-sqs-queue-types.2026-10-31 — source src.aws-sqs; unit "Amazon SQS
  queue types — Amazon SQS Developer Guide"; unit_type documentation-page;
  content_sha256
  c9ccf72844c5180d80502042f9abf7766b8af7e194f217065ddf50a43f540609;
  sections_read and limits as R3.
- read.aws-sqs-fair-queues.2026-10-31 — source src.aws-sqs; unit "Amazon SQS
  fair queues — Amazon SQS Developer Guide"; unit_type documentation-page;
  content_sha256
  9d0821490fbdd48ed28c195c3b5bdc466d800d34383b1caf36dd802ec0e7ca5f;
  sections_read and limits as R4.

### owner-units.v1.json

For tycho.pattern.priority-queue set technical_evidence.mechanism,
invariant, failure_recovery and alternative state to "supported" and replace
each partial reason with the R1-R5 binding note. Keep the four quote strings
unchanged. Set technical_coverage to "supported"; keep decision_coverage
"partial-bounded" unless a separate decision review changes it. Set
source_support.ledger_record to read.rabbitmq-priority-queues.2026-10-31 and
record the four supporting records in notes. Update the card path/hash and
owner line/anchor if the integrator's schema stores them; the card remains
inline at
book/volumes/v11-pattern-atlas/c07-resilience/README.md#priority-queue.

### source-plan.v1.json and review metadata

Extend required_units for tycho.pattern.priority-queue with R2-R5 and replace
the R1 record/read status with read.rabbitmq-priority-queues.2026-10-31. Keep
the existing RabbitMQ unit URL and section list, adding the 2026-10-31
revision. The sufficient-candidates, sufficient-rereview-packets and any
owner/card hash rows that still carry 68181cf... or the old RabbitMQ record
are stale for this edit; they must be rebound by the integrator, not by this
lane. The owner page is now 4441a437... and the card beaec866...; the
sufficient-review records must not treat the old page hash as current. No
promotion, owner acceptance or independent review is claimed.

## Limits

- The five units are living public documentation pages, not benchmarks,
  standards or production observations. The digests pin the 2026-10-31
  representations, not every future revision.
- The canonical extraction falls back to whole-page text because none of the
  five pages exposes the script's article-body marker. Digests therefore
  include page chrome. Quotes were checked against that canonical text.
- The selected Azure units are a Priority Queue pattern page and a Service Bus
  AMQP protocol guide, not a native message-priority API page. The AMQP guide
  maps no priority header; the pattern implements priority with a custom
  application property and SQL filters. No native Service Bus priority field
  is claimed. The AMQP guide was bound only through its "Messages" section.
- The selected AWS units document FIFO ordering and fair-queue tenant
  fairness, not a native SQS priority-level field, aging knob or per-tenant
  quota. No native SQS priority feature is claimed.
- "Broker max-wait/aging" is a Tycho policy for this page. RabbitMQ documents
  strict delay, prefetch inversion and starvation but no aging setting;
  Azure recommends dynamically increasing the priority of old messages; SQS
  fair queues expose age and dwell-time signals without a per-tenant cap. No
  universal threshold is inferred.
- No RabbitMQ broker, Service Bus namespace, SQS queue, filter, subscription,
  consumer or load generator was created or run. No latency, starvation,
  throughput or recovery measurement was made.
- The owner page is in V07, so the repository's V11 line-length checker does
  not cover it; its touched range was checked directly and has no line over
  100 characters.
- The card remains inline in V11/C07, matching the task brief and the
  registered atlas_section priority-queue. Promotion still requires the
  independent AI review gate and owner acceptance.
- The page's claim_ids stay empty; no claim registry is introduced.

## Checks

- python3 scripts/check_markdown_line_length.py — PASS: V11 prose <=100;
  145 exact owner-link exceptions.
- python3 scripts/check_boundary.py — PASS: configured lexical boundary
  checks; independent-origin review still required.
- Direct owner-page touched-range check — 0 lines over 100 characters.
- All selected quotes — PASS as whitespace-normalized substrings of the named
  canonical text. Owner-unit quote preservation — PASS for all four quotes.
- Frontmatter YAML parse — PASS for owner and card; source ids 7 and 12
  respectively.

## Commit scope

The lane commit contains this note and the two book files only:

- the V07/C05 owner page admission-resource.md;
- the V11/C07 inline card README.md;
- authoring/B54-PRIORITY-QUEUE-LANE-2026-10-31.md.

No shared JSON, promotion or generated file is in the lane commit.
