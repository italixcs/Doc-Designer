# ArchiveLens source notes

Everything below is fictional. Create a complete project report, not a transcript of these notes. The committee and volunteer coordinators need to understand the pilot, its evidence, its record model, operational checks and the proposed next decision. No final decision has been made. Choose the structure yourself.

## Collection and resources

- Institution: Morrow Museum. Project: ArchiveLens collection digitization pilot.
- Scope: photograph paper collection objects and prepare minimum descriptive records.
- 240 in-scope objects: 120 postcards, 80 posters, 40 pamphlets.
- B01: 80 postcards. B02: 40 postcards and 40 posters. B03: 40 posters and 40 pamphlets. Each batch has 80 objects.
- Two volunteers available for a combined six hours/week, eight working weeks: 48 planned volunteer hours.
- Actual time per object or stage not recorded. Planned hours cannot establish a measured productivity rate.
- Existing camera and laptop. Purchase, storage and operating costs not collected. No approved full-collection deadline or budget.
- Working goal: consistent image and minimum record for each scoped object.
- Coordinators need to locate records, see their stage and identify missing information. Committee needs cautious throughput/resource/uncertainty evidence.
- Public release, rights clearance, conservation treatment and a representative sample of all museum holdings are outside scope. No external quality audit.

## Workflow and roles

- Six stages: assign object identifier → capture image → enter minimum metadata → check image and metadata → resolve recorded issue → approve into pilot catalog.
- Corrections can return a record from checking to metadata entry or image capture.
- Coordinator assigns object to one batch and confirms identifier before capture.
- Capture volunteer names image using object identifier and enters image filename.
- Metadata volunteer enters short title, object type and batch identifier.
- Checker compares object identifier with record and verifies minimum fields and image filename.
- Allowed status labels: pending (not captured), captured (image exists, not yet checked), checked (checking occurred, approval not recorded), published (checker approved into pilot catalog).
- Published does not mean public website release or rights clearance.
- Log a problem using object identifier, issue, owner role and next action. No silent identifier replacement or deletion of difficult objects from a batch.
- Possible issue examples: missing image filename, inconsistent object type, identifier mismatch. No counts by issue type; frequency ranking unsupported.
- Coordinator reviews open issues before next session. Checker approves only after minimum fields are present and identifier matches.
- These are pilot operating requirements, not a verified external cataloging standard.

## Weekly evidence

Use activity.csv exactly: week 1–8, capture/check/approval counts. Each object counted at most once in each activity column across the eight weeks.

- Totals: captured 191, checked 165, approved 143.
- 49 scoped objects not captured; 48 captured but not approved; 97 not approved.
- The source does not split every object into its current status category.
- Approval share: 143/240, approximately 59.6% of scoped collection. Not an image-quality, public-access or rights-clearance score.
- Weekly counts are different events, not an object-level cohort. Approval can happen after the capture week. Same-week subtraction is not a measured weekly backlog or conversion rate.
- Capture starts at 18 in week 1, peaks at 30 in week 5, ends at 20 in week 8. Approval peaks at 23 in week 7.
- No attendance, downtime or object-difficulty data, so no supported explanation of the changes.
- No activity by batch, so no evidence that a particular batch is fastest or most complete.

## Data model and query

Use schema.sql for exact keys, field names, required/optional fields and checks. Use query.sql without changing its meaning.

- batch: batch_id primary key, label required.
- object_record: object_id primary key; batch_id required foreign key to batch; title, object_type, status required; image_filename optional.
- Types: postcard, poster, pamphlet. Status labels: pending, captured, checked, published.
- issue: issue_id primary key; object_id required foreign key to object_record; issue_text, owner_role and resolved required. resolved is integer 0 or 1.
- Relationships: batch has many object records; each object belongs to exactly one batch; each object may have zero or more issues; each issue points to one object. No many-to-many relation or account table.
- owner_role is a role, not a person's name.
- Query lists unresolved issues with batch label, object identifier, title and issue text. Joins through object_id and batch_id, filter resolved=0, order by batch label then object identifier.
- The SQLite fixture has three objects and two issues, separate from the 240-object collection and weekly events.
- Query example result: Postcards A / OBJ001 / Harbor postcard / Confirm short title.
- The example demonstrates query behavior; it is not evidence of an executed query on the museum collection.

## Acceptance and unresolved questions

- Record checks: identifier matches object and filename; batch exists; title/type present; status allowed; associated issues reviewed. Checker records approval; do not infer approval from a filename.
- Collection checks: every object assigned to a batch; three batches of planned 80 objects.
- Separate record acceptance from committee decisions on continuation and evidence needs.
- Three uncertainties: no actual stage-time data; no external quality audit; rights/public release outside scope.
- Future review questions: can coordinators find a record from minimum metadata; does each issue description lead to an action; does image naming stay consistent?
- These are future questions, not measured findings. No supplied interviews or error rates.
- No formal sign-off, named reviewer, compliance certificate, completed backup test or security assessment is documented.

## Proposed second pilot

- Four weeks, awaiting committee approval; committee may approve, revise or defer.
- Start with the 49 uncaptured objects and continue resolving outstanding issues.
- Do not promise to finish all 97 unapproved records; stage time and difficulty unknown.
- Week 1: confirm queue; agree how stage time and corrections will be recorded.
- Weeks 2–3: continue capture, metadata and checking; record stage time and issue type.
- Week 4: coordinator summarizes progress, reviews unresolved questions and returns evidence to committee.
- Source recommendation: authorize this limited follow-up only if committee agrees to collect missing time/correction data. It is a recommendation, not a decision.
- No measured cost per object or substantiated savings/cost-effectiveness claim.

## Terms and provenance

Capture means image exists; checking means required checks occurred; approval means entry into pilot catalog; public release is separate. Issue means a recorded problem needing action. Batch means one of the three groups of 80.

The supplied operating brief, inventory, activity table and schema are the evidence for this invented project. External sources may support design/tool use, not verify the fictional operations. Keep design research and production notes outside the report.
