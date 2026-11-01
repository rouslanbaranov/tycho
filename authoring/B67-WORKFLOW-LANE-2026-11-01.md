# B67 — Distributed Workflow Orchestration failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-11-01. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both partial
dimensions to Temporal, AWS Step Functions and Cadence public documentation,
and labels the unknown-effect repair rule, the completed-flag caution and the
selection rule as Tycho guidance. The card remains inline in V11/C08. Label
Tycho.

## Lane coordinates

- Parent HEAD: 64570da3.
- Lane label: Tycho.
- Branch: b67-workflow; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b67-workflow.
- Scope: the owner section "Distributed Workflow Orchestration" in V04/C05,
  the inline "Distributed Workflow Orchestration" card in V11/C08, and this
  note. Single-entry lane; no other entry, shared JSON, promotion or generated
  file is changed.
- Owner path (concatenate):

      book/volumes/v04-distributed-coordination-and-events/
      c05-outbox-inbox-sagas-and-durable-workflows/
      outbox-inbox-sagas-and-durable-workflows.md

- Inline card path:
  book/volumes/v11-pattern-atlas/c08-coordination/README.md.
- Exactly three files change: the owner page, the inline card host and this
  note.
- Existing source id: src.temporal.
- New source ids proposed: src.aws-step-functions and src.cadence.
- New ledger records proposed: twelve, listed below.
- Retained historical record: read.batch2-temporal-workflows.2026-10-21.
- Baseline and final line-length and boundary checks pass.

## Card location

The registry records atlas_owner.chapter = V11/C08 and section
distributed-workflow-orchestration for this pattern, and card-batches.v1.json
records no card_path. The C08 chapter landing already contains the card body,
so this lane edits that inline block rather than creating a dedicated page.
The chapter frontmatter notes and review dates are updated because they
describe the cards hosted by that page; the registry, card batches and atlas
manifest are left for the integrator. Precedent: B38, B53, B59-B66 edited
inline card hosts the same way.

The task coordinates named "inline card V11/C04". That does not match the
registry: the registry entry records technical_owner.anchor =
distributed-workflow-orchestration and atlas_owner.chapter = V11/C08, and the
atlas manifest lists the pattern under V11/C08. V11/C04 hosts the separate
Saga, Saga Choreography and Saga Orchestration cards. Editing V11/C04 would
cross entries and change a second pattern's card. This lane therefore edits
V11/C08 and records the discrepancy; if the integrator intended V11/C04,
redirect the card edit before applying the proposed metadata.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism as supported, invariant
as supported, failure_recovery as partial and alternative as partial. The
recorded reasons are:

- failure_recovery: "Temporal text has no unknown external-effect repair
  state." Its quote is "Keep a repair state for an unknown external effect; a
  completed flag is not proof that the effect committed."
- alternative: "Text does not compare choreography, job table or simple
  queue." Its quote is "Use choreography, a job table or a simple queue when
  steps are few, timers are short, or no engine can be operated."

The existing primary binding for the supported dimensions is src.temporal,
record read.batch2-temporal-workflows.2026-10-21, revision
bf9ad7b23161652c799b0ccba76ed36f68efb0c9593b1c7a314f816d5e2403c2. The entry
records technical_coverage partial-bounded, decision_coverage partial-bounded
and review_state self-checked. The summary records failure_recovery_supported
92 and alternative_supported 96; this entry contributes to neither. The
registry records technical_owner.state partial-bounded, atlas_owner.state
partial-bounded, coverage technical and decision partial-bounded, one source
unit and review_status self-checked.

The base owner page is 145 lines, 905 words, 8,011 bytes, SHA-256
10c1342b0b96059095e067d77ff9e72b0ae78e51233a67359c14cd80da0709b2. The base
owner section (lines 133-145) is 13 lines, 124 words, 807 bytes, SHA-256
156f461ce2a3cf9df1322fdc2fed7b61e6d6a01894eb94d3cf404abaa994d518. The base
chapter landing is 321 lines, 1,550 words, 14,458 bytes, SHA-256
b7f4b4e8a04a7d7b42242647374b362128697f4d0c8588f6a6d96ef1072e4c69. The base
card block (lines 261-295) is 35 lines, 207 words, 1,957 bytes, SHA-256
847ba0736e53e955d070d4c6b0f482dedfcb96c224b8ad41c976f18ff2164fa9.

The final owner page is 191 lines, 1,266 words, 11,648 bytes, SHA-256
8f34ba35aae092dd35f7740b7475581066264d6adf60fbe45affc8b4ef9722e2. The final
owner section (lines 133-191) is 59 lines, 485 words, 4,436 bytes, SHA-256
1944793a00838d0751d2280ed56ebb7be8248964a081a8a9bc7154bb616fbe8a. The final
chapter landing is 339 lines, 1,718 words, 15,929 bytes, SHA-256
e8739a592cc7534d3937e44849374cfe8b6d317b7204ed613483e23847d8c47c. The final
card block (lines 261-313) is 53 lines, 371 words, 3,395 bytes, SHA-256
f46535e1434cce0fe851a1f2995a6ef6e675dbe61680c685471ba17972293f7d.

The gap was evidential. The owner page and card already stated the unknown
external-effect repair state, the completed-flag caution, choreography, job
table and simple queue alternatives, and the reverse condition as Tycho
guidance, but no exact public quote, section and representation hash bound
those claims. Shared metadata still shows 2/4 and partial-bounded until the
integrator applies the proposals below.

## Candidate evaluation

- Temporal, Workflows (selected): Event History, replay, and the activity
  boundary for external work. Canonical page https://docs.temporal.io/workflows;
  read representation https://docs.temporal.io/workflows.md.
- Temporal, Activities (selected): idempotency recommendation, retry policy,
  and retry from the initial state unless a heartbeat payload checkpoints.
- Temporal, Activity Execution (selected): an Activity Task can be lost after
  the Activity Function is called and the Worker crashed; the Start-To-Close
  timeout triggers the retry. This is the strongest unknown-effect statement.
- Temporal, Saga Pattern (selected): a charge may commit before success;
  compensations must be idempotent and must tolerate a forward Activity that
  never executed; the comparison table lists choreography.
- Temporal, Job queues (selected): one Activity versus several, or state
  between steps.
- AWS Step Functions, Choosing workflow type (selected): Standard exactly-once
  with its explicit Retry exception, and Express at-least-once.
- AWS Step Functions, Activities (selected): ExecutionTimedOut when no
  success, failure or heartbeat arrives; the task token is invalidated.
- AWS Step Functions, Redrive (selected): a failed Task is rescheduled and
  rerun, while successful steps are preserved.
- AWS Step Functions, Best practices (selected): without an explicit timeout
  an execution can be stuck waiting for a response that will never come.
- Cadence, Activities (selected): activity state is not recovered, failures
  are expected, and regular activities can execute multiple times.
- Cadence, FAQ (selected): queue pain points and the simple fanout boundary.
- Cadence, Workflow Engine (selected): the queue-plus-database alternative,
  the simple-flow limit, and replay from event history.
- AWS, What is Step Functions (examined, not selected): duplicates Choosing
  workflow type with less scoping detail.
- AWS, Handling errors (examined, not selected): retry/catch mechanics
  duplicate redrive and timeout evidence.
- Temporal, Workflow Execution overview (examined, not selected): replay is
  already defined on Workflows.
- Cadence, Workflows (examined, not selected): overlaps Workflow Engine.
- Cadence, /docs/concepts/retries (requested, returned 404): no
  representation exists at that path on 2026-11-01.
- Vendor tutorials and third-party summaries (examined, not selected): not
  primary documentation.

No engine, worker, activity, timer, retry, outage, redrive or repair state was
exercised.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-11-01 (UTC), twice per
representation; the two hashes matched for every selected unit. Raw bytes were
hashed from the served body (no compression was requested). For Markdown, the
served .md representation is the read representation; the canonical page URL
is recorded separately. For HTML, raw bytes are the served page and canonical
text is extracted as described below. Word counts split on whitespace.
Character counts for Markdown are byte counts; for HTML they are canonical
text characters.

Canonical extraction for HTML: select the main element and its article, drop
script, style, nav, footer, header, aside, table-of-contents, pagination,
breadcrumb and page-footer subtrees, convert block tags to newlines, strip
remaining tags, decode entities, normalize non-breaking spaces, typographic
quotes and dashes to ASCII, remove heading pilcrows, collapse space runs and
blank lines, and strip. Markdown was normalized only for whitespace before
quote comparison; its raw bytes are hashed. Quoted fragments were checked
against the normalized text; line breaks inside quotes in this note are
editorial wrapping and are not part of the source text.

### R1 — Temporal, Workflows

- Record: read.temporal-workflows.2026-11-01 (proposed).
- Source: src.temporal (existing).
- URL: https://docs.temporal.io/workflows; representation
  https://docs.temporal.io/workflows.md.
- Label/type: "Temporal Workflow"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:40:26Z and again at
  2026-11-01T01:08:30Z; 5,116-byte Markdown; ETag
  "dc4862817529016eecc25a7b94144ca2"; Last-Modified
  Fri, 30 Oct 2026 22:53:16 GMT; raw Markdown SHA-256
  df74cfb4c9a2ea94427afeb8d3912baeece244ab0b09226d31c61045229a184a on both
  fetches. 780 words.
- Sections read: "Intro to Workflows", "How Workflow replay works",
  "Resuming a Workflow".
- Sections not read: linked child pages, examples and SDK guides.
- Claims supported: Q1-Q3.
- Limits: defines the workflow execution model and replay; does not state that
  an external effect is atomic with the workflow record. Live page; the hash
  pins the 2026-11-01 representation.

### R2 — Temporal, Activities

- Record: read.temporal-activities.2026-11-01 (proposed).
- Source: src.temporal (existing).
- URL: https://docs.temporal.io/activities; representation
  https://docs.temporal.io/activities.md.
- Label/type: "What is a Temporal Activity?"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:40:26Z and again at
  2026-11-01T01:08:32Z; 3,506-byte Markdown; ETag
  "c29d3e53e7c341a044c02001bd040980"; Last-Modified
  Sat, 31 Oct 2026 01:51:18 GMT; raw Markdown SHA-256
  63073f0e815ebf134c6cf165591aca9d66f1ce8ada22cfec0af635bedcc546b6 on both
  fetches. 476 words.
- Sections read: the full page, including the retry paragraph and the
  idempotency recommendation.
- Sections not read: linked Activity Definition, Task Queue and SDK pages.
- Claims supported: Q4-Q5.
- Limits: recommends idempotency and states retries; no repair state or
  completed-flag rule.

### R3 — Temporal, Activity Execution

- Record: read.temporal-activity-execution.2026-11-01 (proposed).
- Source: src.temporal (existing).
- URL: https://docs.temporal.io/activity-execution; representation
  https://docs.temporal.io/activity-execution.md.
- Label/type: "Activity Execution"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:41:18Z and again at
  2026-11-01T01:23Z; 13,988-byte Markdown; ETag
  "ee87872922880445b854fc57380587ea"; Last-Modified
  Fri, 30 Oct 2026 23:49:11 GMT; raw Markdown SHA-256
  710e839d78f8c05445f1d56ee5a6d747c2a46fd6a379185cbadec66f924f9a62 on both
  fetches. 1,775 words.
- Sections read: the full page, including "Activity Execution lifecycle",
  "Cancellation", "What is Asynchronous Activity Completion?".
- Sections not read: linked SDK timeout and async-completion guides.
- Claims supported: Q6-Q7.
- Limits: task loss and retry mechanics, not a general rule that an external
  system's flag is unreliable; the inference is Tycho guidance.

### R4 — Temporal, Saga Pattern

- Record: read.temporal-saga-pattern.2026-11-01 (proposed).
- Source: src.temporal (existing).
- URL: https://docs.temporal.io/design-patterns/saga-pattern; representation
  https://docs.temporal.io/design-patterns/saga-pattern.md.
- Label/type: "Saga Pattern"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:41:19Z and again at
  2026-11-01T01:23Z; 19,152-byte Markdown; ETag
  "72de226891ce7b13006a7bcaefb16458"; Last-Modified
  Sun, 01 Nov 2026 00:41:19 GMT (equal to the fetch time, not a revision pin);
  raw Markdown SHA-256
  987aec66a21037418c7f9930c139aaeb2a20b76690ef140769d6886c5e11e5c9 on both
  fetches. 2,197 words.
- Sections read: "Overview", "Problem", "Solution", "When to register
  compensations", "When to use", "Benefits and trade-offs", "Comparison with
  alternatives", "Best practices", "Common pitfalls".
- Sections not read: SDK sample code and linked patterns.
- Claims supported: Q8-Q10.
- Limits: design-pattern page; states partial completion and the choreography
  comparison, not a production incident or measurement.

### R5 — Temporal, Job queues

- Record: read.temporal-job-queue.2026-11-01 (proposed).
- Source: src.temporal (existing).
- URL: https://docs.temporal.io/evaluate/features/job-queue; representation
  https://docs.temporal.io/evaluate/features/job-queue.md.
- Label/type: "Job queues"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:41:19Z and again at
  2026-11-01T01:23Z; 5,694-byte Markdown; ETag
  "1814cbbc38aa0220de539e346ba7229e"; Last-Modified
  Sun, 01 Nov 2026 00:41:19 GMT (equal to the fetch time, not a revision pin);
  raw Markdown SHA-256
  ab82e99d3c34b54e6e08e07c850c6f29f60f637b0a40a17e502cd6d76b2feff6 on both
  fetches. 752 words.
- Sections read: "What you get that a queue library doesn't give you" and
  "When to use a Standalone Activity instead of a Workflow".
- Sections not read: "What you still operate", release stages, SDK
  quickstarts.
- Claims supported: Q11.
- Limits: product documentation for one engine; "one Activity" versus
  "several" is a selection boundary, not a universal rule.

### R6 — AWS Step Functions, Choosing workflow type

- Record: read.aws-step-functions-workflow-types.2026-11-01 (proposed).
- Source: src.aws-step-functions (proposed).
- URL: https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html
  (canonical); representation with .md appended.
- Label/type: "Choosing workflow type in Step Functions"; official AWS
  documentation.
- Representation: HTTP/1.1 200 on 2026-11-01T00:40:27Z and again at
  2026-11-01T01:23Z; 9,099-byte Markdown; ETag
  "aFwRuWiHJiRVThexE0umDt4HWHQ="; Last-Modified
  Sat, 31 Oct 2026 03:32:30 GMT; raw Markdown SHA-256
  50c0618a8ebf3971d83f90998e12cad480b2550277ccd948e2500cdb33d79646 on both
  fetches. 1,179 words.
- Sections read: "Standard Workflows", "Express Workflows", "Execution
  guarantees in Step Functions workflows".
- Sections not read: linked quotas, pricing and workshop pages.
- Claims supported: Q12-Q13.
- Limits: exactly-once is scoped to "tasks and states" and excludes declared
  Retry behavior; no external-effect ambiguity measurement.

### R7 — AWS Step Functions, Activities

- Record: read.aws-step-functions-activities.2026-11-01 (proposed).
- Source: src.aws-step-functions (proposed).
- URL: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html
  (canonical); representation with .md appended.
- Label/type: "Learn about Activities in Step Functions"; official AWS
  documentation.
- Representation: HTTP/1.1 200 on 2026-11-01T00:41:20Z and again at
  2026-11-01T01:23Z; 8,763-byte Markdown; ETag
  "+IprksvvSKS7tDS0r+NfFc4smI0="; Last-Modified
  Sat, 31 Oct 2026 03:33:14 GMT; raw Markdown SHA-256
  60a969cb473ef6a31578dea9e425739608e08120dda8321e0765e81ea70d5595 on both
  fetches. 1,011 words.
- Sections read: "Overview", "Waiting for an Activity Task to Complete", API
  list.
- Sections not read: linked API references and the Ruby worker example.
- Claims supported: Q14-Q15.
- Limits: timeout and token invalidation, not a repair workflow; no worker or
  activity was run.

### R8 — AWS Step Functions, Redrive

- Record: read.aws-step-functions-redrive.2026-11-01 (proposed).
- Source: src.aws-step-functions (proposed).
- URL: https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html
  (canonical); representation with .md appended.
- Label/type: "Restarting state machine executions with redrive in Step
  Functions"; official AWS documentation.
- Representation: HTTP/1.1 200 on 2026-11-01T00:41:19Z and again at
  2026-11-01T01:23Z; 12,876-byte Markdown; ETag
  "0kFEHnVd+k5zdg5tqMqQyDoiPgc="; Last-Modified
  Sat, 31 Oct 2026 03:32:49 GMT; raw Markdown SHA-256
  89d736fbb430bdab823b6ebd749efa183a52d97552e909b1690fb1a813f64ab3 on both
  fetches. 1,660 words.
- Sections read: "Redrive behavior of individual states", "Retry behavior of
  redriven executions".
- Sections not read: IAM policy example and console screenshots.
- Claims supported: Q16-Q17.
- Limits: redrive for Standard workflows, not a general implication that every
  redrive is safe for an external effect.

### R9 — AWS Step Functions, Best practices

- Record: read.aws-step-functions-best-practices.2026-11-01 (proposed).
- Source: src.aws-step-functions (proposed).
- URL: https://docs.aws.amazon.com/step-functions/latest/dg/sfn-best-practices.html
  (canonical); representation with .md appended.
- Label/type: "Best practices for Step Functions"; official AWS
  documentation.
- Representation: HTTP/1.1 200 on 2026-11-01T00:40:27Z and again at
  2026-11-01T01:23Z; 21,847-byte Markdown; ETag
  "/xGcp3B4I83ROEDnZNDRaYImlN0="; Last-Modified
  Sat, 31 Oct 2026 03:33:10 GMT; raw Markdown SHA-256
  afc807f45a75bfcdb1956796397076526c21f54f4b8c05e377b821bc7843dc9d on both
  fetches. 2,750 words.
- Sections read: "Using timeouts to avoid stuck Step Functions workflow
  executions" and the surrounding best-practice list.
- Sections not read: cost, tagging and CloudWatch sections not used here.
- Claims supported: Q18-Q19.
- Limits: prescribes timeouts and heartbeats; no repair state or operator
  procedure.

### R10 — Cadence, Activities

- Record: read.cadence-activities.2026-11-01 (proposed).
- Source: src.cadence (proposed).
- URL: https://cadenceworkflow.io/docs/concepts/activities/.
- Label/type: "Activities | Cadence"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:40:50Z and again at
  2026-11-01T01:24Z; 48,173-byte HTML; ETag "6ae60412-bc2d"; Last-Modified
  Sat, 31 Oct 2026 15:06:58 GMT; raw HTML SHA-256
  af4e7c940c7464fa61c4dea4c14e8dfc6f1b6101b5ef985fa1a001d5ecb0b0e3 on both
  fetches. Canonical text 11,667 characters / 1,814 words, SHA-256
  d8ea17ad8cf60aa8c27bc11e2ac844322af7b2b73ea5ae1de0c1b89cbcf29a2c. The page
  carries "Last updated on Sep 18, 2026".
- Sections read: "Retries", "Long Running Activities", "Local Activities",
  timeout list.
- Sections not read: linked Stack Overflow questions and SDK samples.
- Claims supported: Q20-Q22.
- Limits: one engine's documentation; states activity-state loss and
  duplicate-execution chance, not a measured rate.

### R11 — Cadence, FAQ

- Record: read.cadence-faq.2026-11-01 (proposed).
- Source: src.cadence (proposed).
- URL: https://cadenceworkflow.io/faq/cadence-faq/.
- Label/type: "Cadence FAQ"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:40:50Z and again at
  2026-11-01T01:24Z; 27,709-byte HTML; ETag "6ae60412-6c3d"; Last-Modified
  Sat, 31 Oct 2026 15:06:58 GMT; raw HTML SHA-256
  a03ad5efa8d5f3de3c03db1e03c172ccf6b9e12dd2ed433401a1ed27ce70aa07 on both
  fetches. Canonical text 3,423 characters / 540 words, SHA-256
  0d04645368eb29413740c1a5e76d21e84022491486c32b7b1923f9d5dabd4e10. The page
  carries "Last updated on Jul 8, 2026".
- Sections read: "When should I use Cadence instead of a message queue (Kafka,
  SQS, RabbitMQ)?" and "How does Cadence handle failures?".
- Sections not read: the Temporal comparison link and other FAQ entries.
- Claims supported: Q23-Q25.
- Limits: vendor FAQ; the queue boundary is stated from the engine's
  perspective and does not measure queue behavior.

### R12 — Cadence, Workflow Engine

- Record: read.cadence-workflow-engine.2026-11-01 (proposed).
- Source: src.cadence (proposed).
- URL: https://cadenceworkflow.io/docs/concepts/workflow-engine/.
- Label/type: "Workflow Engine and Workflow Orchestration | Cadence"; official
  documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:40:49Z and again at
  2026-11-01T01:24Z; 101,617-byte HTML; ETag "6ae60412-18cf1"; Last-Modified
  Sat, 31 Oct 2026 15:06:58 GMT; raw HTML SHA-256
  efca8a8cc5d48d082cb26641cf073cecd9a2c9354afe1351ec00b19b06a91a01 on both
  fetches. Canonical text 10,536 characters / 1,322 words, SHA-256
  ac07901276c04a97d07175adbdf403444e106e7bd74ef90adf730c3bacf7a083. The page
  carries "Last updated on Sep 23, 2026".
- Sections read: "What a workflow engine does", "How Cadence differs from
  queue + database patterns", "Workflows must be deterministic", "Core
  concepts".
- Sections not read: production topology deployment guides and SDK samples.
- Claims supported: Q26-Q28.
- Limits: vendor comparison; states the queue-plus-database alternative and
  its costs, not a benchmark or an operated deployment.

## Selected exact quotes

Quotes reproduce the served prose after the normalization above. Typographic
quotes and dashes are ASCII in this note. Line breaks inside quotes are
editorial wrapping and are not part of the source text. Thirty numbered
fragments were checked against the twelve representations on 2026-11-01;
30/30 were present. The owner and card use a subset; every fragment used there
was also checked.

### Mechanism and replay

- Q1, R1, "How Workflow replay works": "Temporal keeps the Event History. This
  is a complete, ordered log of everything that has already happened in a
  Workflow."
- Q2, R1, "How Workflow replay works": "This history is the source of truth
  for everything that happens in the Workflow."
- Q3, R1, "Resuming a Workflow": "When a Workflow calls an Activity, the
  Activity runs once, its result is recorded in the Event History. During
  replay, that result is reused, not recomputed."
- Q28, R12, "Workflows must be deterministic": "Workflow code is replayed from
  its event history every time a worker picks it up."

### Failure and recovery

- Q4, R2: "Larger pieces of functionality should be broken up into multiple
  Activities. This makes it easier to do failure recovery, have short
  timeouts, and be idempotent."
- Q5, R2: "Each attempt starts from the initial state, unless your code uses a
  Heartbeat detail payload for checkpointing."
- Q6, R3, "Activity Execution lifecycle": "Temporal guarantees that an
  Activity Task either runs or timeouts. There are multiple failure scenarios
  when an Activity Task is lost. It can be lost during delivery to a Worker or
  after the Activity Function is called and the Worker crashed."
- Q7, R3: "If the Activity Task times out, the Activity Execution will be
  retried according to the Activity Execution Retry Policy."
- Q8, R4, "When to register compensations": "For example, a credit card may
  be charged but the Activity fails before returning success."
- Q9, R4, "When to register compensations": "All compensations must be
  idempotent and able to handle cases where the forward Activity never
  executed."
- Q12, R6, "Standard Workflows": "Standard Workflows follow an exactly-once
  model, where your tasks and states are never run more than once, unless you
  have specified Retry behavior in ASL."
- Q13, R6, "Express Workflows": "Express Workflows use an at-least-once model,
  so an execution could potentially run more than once."
- Q14, R7: "If the execution doesn't receive either of these or a
  SendTaskHeartbeat call before the time configured in TimeoutSeconds, the
  execution will fail and the execution history will contain an
  ExecutionTimedOut event."
- Q15, R7: "After the task times out, Step Functions invalidates the task
  token."
- Q16, R8, "Redrive behavior of individual states": "If your workflow
  execution fails at the Task state, and you redrive the execution, the
  execution reschedules and then reruns the Task state."
- Q17, R8, "Redrive behavior of individual states": "Step Functions preserves
  the results and execution history of the successful steps, which are not
  rerun when you redrive an execution."
- Q18, R9: "Without an explicit timeout, Step Functions often relies solely on
  a response from an activity worker to know that a task is complete."
- Q19, R9: "an execution is stuck waiting for a response that will never
  come."
- Q20, R10: "Cadence does not recover activity state in case of failures."
- Q21, R10, "Local Activities": "Though regular activity could also execute
  multiple times when using retry policy, local activity has more chance of
  occurring."
- Q22, R10, "Local Activities": "Because local activity result is not recorded
  into history until DecisionTaskCompleted."

### Alternative

- Q10a, R4, "Comparison with alternatives": "Saga (choreography)"
- Q10b, R4, "Comparison with alternatives": "Event-driven compensations"
- Q10c, R4, "Comparison with alternatives": "Very loose"
- Q11, R5: "Use a Standalone Activity to run one Activity. Use a Workflow to
  orchestrate several, or to hold state between steps."
- Q23, R11: "Message queues are great for point-to-point async delivery. They
  become painful when your process:"
- Q24, R11: "Has to wait minutes, hours, or days between steps"
- Q25, R11: "For simple fire-and-forget fanout or high-throughput streaming, a
  queue is usually the right tool."
- Q26, R12: "The standard alternative to a workflow engine is to center
  coordination around a database and a message queue. A worker polls a queue,
  executes an action, updates a row, and pushes downstream messages."
- Q27, R12: "This works for simple flows, but it fractures state across
  tables, makes the execution history invisible, and turns every failure
  scenario into a bespoke retry loop."

## Owner and card changes

The owner section "Distributed Workflow Orchestration" is rewritten in four
bounded parts. The opening paragraph keeps the state-machine definition and
adds Temporal Event History and Cadence replay. A new "Failure and recovery
(Tycho synthesis)" paragraph binds worker-crash task loss, the Start-To-Close
retry, AWS ExecutionTimedOut and the invalidated task token, redrive, Cadence
activity-state loss, and AWS exactly-once versus at-least-once scope; it keeps
the repair state and completed-flag caution and labels them Tycho guidance. A
new "Alternative (Tycho comparison)" paragraph binds the Temporal job-queue
boundary, the Cadence queue and queue-plus-database statements, and the
Temporal Saga choreography row; it labels the operability condition and final
selection rule as Tycho guidance. A new "Sources and limits" paragraph lists
the twelve proposed records and the limits.

The owner frontmatter changes updated_at from 2026-10-20 to 2026-11-01 and
source_inspection_date from null to 2026-11-01. The owner evidence_scope is
unchanged because the page is covered by the decomposition metadata guard;
adding unregistered source ids there would fail the source-register check.

The V11/C08 card keeps its ten contract fields. Competing alternative and
Failure and recovery are rewritten to name the bound statements and keep the
selection rule and the completed-flag caution as Tycho guidance. Sources lists
the retained record and the twelve proposed records. The chapter frontmatter
notes, review date, updated_at and source_inspection_date are updated. No
source id is added to the chapter evidence_scope for the same register reason.
The Technical owner line and the other eight cards are unchanged.

## Proposed shared metadata

The lane does not edit any shared JSON. The proposals below are for the
integrator; applying them is what moves the entry from 2/4 to 4/4.

### reading-ledger.v1.json

Add twelve records. All use access_date 2026-11-01, access_method "public
HTTPS GET; served representation inspected", reviewer "Automated authoring
agent" and status "read". For Markdown, content_sha256 is the raw
representation SHA-256; for HTML, content_sha256 is the raw HTML SHA-256 and
the canonical-text hash is recorded separately.

- read.temporal-workflows.2026-11-01 — src.temporal; R1 URL; unit_label
  "Temporal Workflow"; document page; sections as R1; content_sha256
  df74cfb4c9a2ea94427afeb8d3912baeece244ab0b09226d31c61045229a184a;
  780 words; Q1-Q3.
- read.temporal-activities.2026-11-01 — src.temporal; content_sha256
  63073f0e815ebf134c6cf165591aca9d66f1ce8ada22cfec0af635bedcc546b6;
  476 words; Q4-Q5.
- read.temporal-activity-execution.2026-11-01 — src.temporal; content_sha256
  710e839d78f8c05445f1d56ee5a6d747c2a46fd6a379185cbadec66f924f9a62;
  1,775 words; Q6-Q7.
- read.temporal-saga-pattern.2026-11-01 — src.temporal; content_sha256
  987aec66a21037418c7f9930c139aaeb2a20b76690ef140769d6886c5e11e5c9;
  2,197 words; Q8-Q10.
- read.temporal-job-queue.2026-11-01 — src.temporal; content_sha256
  ab82e99d3c34b54e6e08e07c850c6f29f60f637b0a40a17e502cd6d76b2feff6;
  752 words; Q11.
- read.aws-step-functions-workflow-types.2026-11-01 —
  src.aws-step-functions; content_sha256
  50c0618a8ebf3971d83f90998e12cad480b2550277ccd948e2500cdb33d79646;
  1,179 words; Q12-Q13.
- read.aws-step-functions-activities.2026-11-01 — src.aws-step-functions;
  content_sha256
  60a969cb473ef6a31578dea9e425739608e08120dda8321e0765e81ea70d5595;
  1,011 words; Q14-Q15.
- read.aws-step-functions-redrive.2026-11-01 — src.aws-step-functions;
  content_sha256
  89d736fbb430bdab823b6ebd749efa183a52d97552e909b1690fb1a813f64ab3;
  1,660 words; Q16-Q17.
- read.aws-step-functions-best-practices.2026-11-01 —
  src.aws-step-functions; content_sha256
  afc807f45a75bfcdb1956796397076526c21f54f4b8c05e377b821bc7843dc9d;
  2,750 words; Q18-Q19.
- read.cadence-activities.2026-11-01 — src.cadence; content_sha256
  af4e7c940c7464fa61c4dea4c14e8dfc6f1b6101b5ef985fa1a001d5ecb0b0e3;
  canonical 11,667 characters / 1,814 words, SHA-256
  d8ea17ad8cf60aa8c27bc11e2ac844322af7b2b73ea5ae1de0c1b89cbcf29a2c;
  Q20-Q22.
- read.cadence-faq.2026-11-01 — src.cadence; content_sha256
  a03ad5efa8d5f3de3c03db1e03c172ccf6b9e12dd2ed433401a1ed27ce70aa07;
  canonical 3,423 characters / 540 words, SHA-256
  0d04645368eb29413740c1a5e76d21e84022491486c32b7b1923f9d5dabd4e10;
  Q23-Q25.
- read.cadence-workflow-engine.2026-11-01 — src.cadence; content_sha256
  efca8a8cc5d48d082cb26641cf073cecd9a2c9354afe1351ec00b19b06a91a01;
  canonical 10,536 characters / 1,322 words, SHA-256
  ac07901276c04a97d07175adbdf403444e106e7bd74ef90adf730c3bacf7a083;
  Q26-Q28.

Each record also carries the unit_url, sections_not_read and limitations from
its R subsection, plus the license note "public documentation; cite short
excerpts and paraphrase; do not mirror".

### sources/register.json

- src.temporal: reading_status full-public-page-inspected; access_checked and
  content_verified 2026-11-01; version "Temporal documentation read 2026-11-01
  as raw Markdown; five pages with per-page ETags and raw and canonical hashes
  recorded in authoring/B67-WORKFLOW-LANE-2026-11-01.md; live pages, not an
  edition pin"; verification_scope listing Workflows, Activities, Activity
  Execution, Saga Pattern and Job queues, and saying linked child pages,
  examples and SDK guides were not read.
- src.aws-step-functions: new public source. Title "AWS Step Functions
  documentation"; publisher Amazon Web Services; kind official-docs; URL
  https://docs.aws.amazon.com/step-functions/latest/dg/; category
  distributed-systems; topics workflows, orchestration, durable-execution;
  priority supporting; planned_use "Durable orchestration failure, redrive
  and alternative boundaries"; admission admitted-for-research; access
  public-web-or-author-download; reading_status full-public-page-inspected;
  version "AWS Step Functions Developer Guide read 2026-11-01 as Markdown;
  four pages with Last-Modified, ETag and raw hashes recorded in the lane
  note"; access_checked and content_verified 2026-11-01; license_notes "Public
  AWS documentation; cite short excerpts and paraphrase; do not mirror";
  verification_scope listing Choosing workflow type, Activities, Redrive and
  Best practices, and saying linked quota, pricing and workshop pages were not
  read.
- src.cadence: new public source. Title "Cadence documentation"; publisher
  Cadence; kind official-docs; URL https://cadenceworkflow.io/; category
  distributed-systems; topics workflows, orchestration, durable-execution;
  priority supporting; planned_use "Durable workflow, activity retry and
  queue alternative boundaries"; admission admitted-for-research; access
  public-web-or-author-download; reading_status full-public-page-inspected;
  version "Cadence documentation read 2026-11-01 as HTML; three pages with
  raw and canonical hashes and per-page Last updated dates recorded in the
  lane note"; access_checked and content_verified 2026-11-01; license_notes
  "Public Cadence documentation; cite short excerpts and paraphrase; do not
  mirror"; verification_scope listing Activities, FAQ and Workflow Engine,
  and saying linked Stack Overflow questions and SDK samples were not read.

### source-plan.v1.json

Replace the single required_units entry for
tycho.pattern.distributed-workflow-orchestration with the twelve units in
R1-R12 order, each with source_id, unit label, unit_type, exact R URL,
sections list, status read, read_record_id and blocked_reason null. Recompute:

- required_units 365 -> 376; read_units 364 -> 375; ledger_records
  327 -> 339; updated 2026-11-01.
- notes: "Temporal workflows, activities, replay, saga and job queue; AWS
  Step Functions workflow types, activities, redrive and best practices; and
  Cadence activities, FAQ and workflow engine bound 2026-11-01; no runtime
  test or promotion."

### owner-units.v1.json

Keep the owner document id, path, heading, anchor, level and line 133. Keep
unit_kind dedicated; add unit terms "repair state", "redrive" and "job table"
if the integrator wants them. Technical evidence:

- mechanism: keep supported and the existing read.batch2 binding. Supporting
  Q1-Q3 and Q28.
- invariant: keep supported and the existing read.batch2 binding. Supporting
  Q3 and Q7.
- failure_recovery: change state to supported. Claim quote: "Keep a repair
  state for an unknown external effect; a completed flag is not proof that
  the effect committed." Reason: Temporal states that an Activity Task can be
  lost after the Activity Function is called and the Worker crashed and is
  retried after the Start-To-Close timeout; AWS Step Functions fails an
  activity with ExecutionTimedOut when no success, failure or heartbeat
  arrives, invalidates the task token and can redrive the Task; Cadence does
  not recover activity state and regular activities can run more than once
  under a retry policy; AWS Express workflows are at-least-once and Standard
  exactly-once is scoped to tasks and states and excludes declared Retry. The
  repair-state rule and completed-flag caution are Tycho guidance. Primary
  binding: src.temporal, record read.temporal-activity-execution.2026-11-01,
  section "Activity Execution lifecycle", quote Q6, revision
  710e839d78f8c05445f1d56ee5a6d747c2a46fd6a379185cbadec66f924f9a62.
  Supporting: Q7; Q8-Q9; Q12-Q13; Q14-Q15; Q16-Q17; Q18-Q19; Q20-Q22.
- alternative: change state to supported. Claim quote: "Use choreography, a
  job table or a simple queue when steps are few, timers are short, or no
  engine can be operated." Reason:
  Temporal reserves a Workflow for several activities or state between steps;
  Cadence says a queue is usually right for simple fire-and-forget fanout and
  that the queue-plus-database pattern works for simple flows while
  dispersing state across tables; Temporal's Saga comparison lists
  event-driven choreography with very loose coupling. The operability
  condition and selection rule are Tycho guidance. Primary binding:
  src.temporal, record read.temporal-job-queue.2026-11-01, section "When to
  use a Standalone Activity instead of a Workflow", quote Q11, revision
  ab82e99d3c34b54e6e08e07c850c6f29f60f637b0a40a17e502cd6d76b2feff6.
  Supporting: Q10a-Q10c; Q23-Q25; Q26-Q27.

Other fields: technical_coverage partial-bounded (all four dimensions
supported but no promotion; the schema-derived value remains partial-bounded);
decision_coverage partial-bounded; review_state self-checked. Notes: "Four
dimensions bound 2026-11-01 to Temporal workflows, activities, replay, saga
and job queue; AWS Step Functions workflow types, activities, redrive and best
practices; and Cadence activities, FAQ and workflow engine. The repair-state
rule, completed-flag caution and selection rule remain Tycho; coverage
partial-bounded; no promotion." Source_support: keep primary
read.batch2-temporal-workflows.2026-10-21; add auxiliary entries for the
twelve proposed records. Summary: failure_recovery_supported 92 -> 93;
alternative_supported 96 -> 97. If the integrator promotes coverage to
sufficient after applying all four supported dimensions,
technical_partial_bounded 14 -> 13 and technical_sufficient 80 -> 81;
otherwise keep partial-bounded and those counters unchanged.

### registry.v1.json

Keep technical_owner.state partial-bounded and atlas_owner.state
partial-bounded; keep coverage technical, decision and overall
partial-bounded; replace source_units with the twelve records above, all
status read; keep review_status self-checked, confidence high and the V11/C08
atlas owner. Replace notes with "Four dimensions bound 2026-11-01 to Temporal
workflows, activities, replay, saga and job queue; AWS Step Functions workflow
types, activities, redrive and best practices; and Cadence activities, FAQ and
workflow engine; coverage partial-bounded; no promotion." The entry has no
updated_at field, so none is added.

### card-batches.v1.json

No change. The card remains inline in V11/C08, so card_path stays absent and
ledger_record stays read.batch2-temporal-workflows.2026-10-21 for the
historical record. After the integrator adds the new records, preflight will
still report card_path missing until a card_path is registered; that is an
integration step, not a lane failure.

### content-revisions.json and derived artifacts

Add one issue-540 revision with authorized_at 2026-11-01 and authorization
"B67 Distributed Workflow Orchestration failure/recovery and alternative
source binding; no promotion or owner acceptance." Raw hashes for reference:

- Owner path: previous
  10c1342b0b96059095e067d77ff9e72b0ae78e51233a67359c14cd80da0709b2; current
  8f34ba35aae092dd35f7740b7475581066264d6adf60fbe45affc8b4ef9722e2.
- Card path: previous
  b7f4b4e8a04a7d7b42242647374b362128697f4d0c8588f6a6d96ef1072e4c69; current
  e8739a592cc7534d3937e44849374cfe8b6d317b7204ed613483e23847d8c47c.

The revision record must use the repository's historical-view hashing, not
these raw hashes; recompute both before saving. The book edit changes one
canonical owner page and one atlas chapter, so the atlas manifest (new V11/C08
chapter SHA-256 e8739a59..., new owner SHA-256 8f34ba35...), route index,
edition inventory and the coverage, census, reverse-map, semantic-audit and
delivery artifacts are stale. Refresh them once at batch end; do not treat a
stale derived hash as a lane content failure.

## Verification

Commands run in /Users/rbaranov/Projects/tycho-worktrees/b67-workflow:

- python3 scripts/check_markdown_line_length.py
  Result: PASS: V11 prose <=100; 145 exact owner-link exceptions.
- python3 scripts/check_boundary.py
  Result: PASS: configured lexical boundary checks; independent-origin review
  still required.
- Quote check: 30 named fragments checked against the twelve canonical
  representations; 30/30 present after whitespace normalization.
- python3 scripts/validate_book_metadata.py
  Result: PASS; 518 documents, complete coverage, 17 topics.
- python3 scripts/validate_pattern_cards.py
  Result: PASS; 11 batches, 145 entries.
- python3 scripts/validate_sources.py
  Result: expected FAIL: "Unknown source reference in
  authoring/B67-WORKFLOW-LANE-2026-11-01.md". The lane note names the two
  proposed source ids before they are registered; the task forbids editing the
  shared register. The source records themselves are proposals below.
- python3 scripts/validate_pattern_owner_units.py
  Result: expected FAIL: "owner-units-alternative". The card's Competing
  alternative field changed and the shared owner-units field was not updated.
  This is the no-shared-JSON constraint.
- python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.distributed-workflow-orchestration
  Result: expected FAIL: failure_recovery and alternative still partial;
  card_path missing or absent. Expected until the proposed metadata is
  applied.
- python3 scripts/validate_pattern_atlas.py
  Result: expected FAIL: atlas-document-sha. Expected because the chapter and
  owner hashes changed and the derived manifest was not refreshed.

git status: exactly the owner page, the V11/C08 landing and this note.

No full unit suite was run. The lane is a content slice; the batch-end suite is
the integrator's step.

## Limits

- Coverage and review are self-checked. No independent AI review, owner
  acceptance, promotion, CI result or production observation is claimed.
- The binding is documentation only. No engine, worker, activity, timer,
  retry, outage, redrive or repair state was exercised.
- AWS Standard exactly-once is scoped to tasks and states and excludes
  declared Retry behavior. It is not evidence that an external effect is
  exactly-once; the page does not state that scope.
- Temporal, AWS and Cadence pages are live documentation. The recorded raw
  hashes and canonical-text hashes pin the 2026-11-01 representations; they do
  not pin the canonical URLs against later changes.
- Cadence pages share a build-time Last-Modified header. The per-page "Last
  updated" dates and the canonical text hashes identify the representation.
- The task coordinate "V11/C04" conflicts with the registry's V11/C08. This
  lane edits V11/C08 and records the discrepancy; V11/C04 hosts different
  saga cards.
- The operability condition "no engine can be operated" is Tycho guidance,
  not a source claim; the selected pages compare queue, database and
  choreography options but do not measure operational cost.
- The card remains inline in V11/C08; this lane did not create a second card.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path book/volumes/v11-pattern-atlas/c08-coordination/README.md.

No shared JSON, promotion, test or generated file is in the lane commit.
