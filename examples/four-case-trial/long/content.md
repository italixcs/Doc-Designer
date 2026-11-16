# ArchiveLens collection digitization pilot

A project report for the fictional Morrow Museum committee and volunteer coordinators

## Purpose and scope

The committee must decide whether to authorize a second digitization pilot. No decision has been made. The first pilot established a repeatable process for photographing collection objects and preparing descriptive records. This report brings the operating brief, eight weeks of recorded counts, a small data model, and a proposed next step together so the committee can review the project without assuming that activity counts prove quality.

The pilot covers 240 paper objects: 120 postcards, 80 posters, and 40 pamphlets. These figures describe the in-scope collection, not the number completed. Three batches divide the work: B01 contains 80 postcards, B02 contains 40 postcards and 40 posters, and B03 contains 40 posters and 40 pamphlets. Each batch contains 80 objects. No other collection material is included.

The intended users are volunteer coordinators and the museum committee. A coordinator needs to see where a record is in the process and what is missing. The committee needs a cautious account of throughput, resource use and remaining uncertainty. The public audience is outside the current pilot: publication in this exercise means approval into the pilot catalog, not an upload to a public website.

Two volunteers are available for a combined six hours each week. The pilot has eight working weeks, giving 48 planned volunteer hours. Actual time by object or stage was not recorded. Dividing object counts by those 48 planned hours would not give a measured productivity rate. The project uses an existing camera and laptop; purchase costs, storage costs and operating costs were not collected.

The working goal is a consistent image and minimum descriptive record for each in-scope object. There is no approved completion deadline or budget for the full collection. The project does not claim conservation treatment, rights clearance, public access, or a representative sample of the museum's holdings. Those decisions require information that the pilot does not supply.

## Workflow and responsibilities

The workflow has six stages: assign an object identifier, capture an image, enter the minimum metadata, check the image and metadata, resolve any recorded issue, then approve the record into the pilot catalog. A record may move back from checking to metadata entry or image capture when the checker records a correction. The diagram should therefore show a return path rather than imply that every object advances without interruption.

The coordinator assigns each object to one batch and confirms its identifier before image capture. The capture volunteer names the image using the object identifier and enters the image filename into the working record. The metadata volunteer enters a short title, object type, and batch identifier. The checker compares the visible object identifier with the record and checks that the required fields and image filename are present.

A published status means that the checker approved the record into the pilot catalog. A checked status means that checking has occurred but approval has not yet been recorded. A captured status means that an image exists but checking has not yet been recorded. A pending status means the record has not reached capture. These are the four allowed status labels; they do not establish legal permission to share an image.

When a problem is found, record the object identifier, issue, owner role and next action in the issue log. An identifier must not be silently replaced and a difficult object must not be deleted from its batch. Issues can include a missing image filename, inconsistent object type, or an identifier mismatch. The pilot did not collect counts by issue type, so their relative frequency is unknown.

The coordinator reviews open issues before the next working session. The checker records approval only after the minimum fields are present and the identifier matches. These are operating requirements of this fictional pilot, not universal cataloging standards. The next pilot can test whether the requirements are sufficient; the first pilot did not compare them with an external quality standard.

## Eight week activity record

The weekly table records three different events: images captured, records checked and records approved into the pilot catalog. Weekly columns are activity counts, not an object-level cohort. A record approved in one week may have been captured in an earlier week. It would therefore be misleading to subtract the same week's published count from its capture count and call the result a measured weekly backlog.

Across the eight weeks, 191 capture events, 165 checking events and 143 publication approvals were recorded. These totals describe recorded activity. The pilot notes say each object was counted at most once in each activity column across the eight weeks. On that basis, 49 of the 240 in-scope objects had not been captured by the end of the pilot. The difference between captured and approved is 48 objects; the source does not break those objects down into all current status categories.

Capture counts rose from 18 in week 1 to a high of 30 in week 5, then ended at 20 in week 8. Approval counts reached a high of 23 in week 7. These observations describe the table and do not explain why the values changed. No attendance, equipment downtime or object difficulty data was collected, so the source cannot attribute changes to training, motivation or equipment.

The three activity series describe progress across time in objects. Their weekly values remain the source for comparing the pattern of capture, checking and approval. They do not form a same-week cohort or a funnel with measured conversion rates. A recommendation about the next pilot is a separate judgment from the values in the activity record.

The pilot catalog holds 143 approved records from this collection at the close of the period. That is 143 out of 240 in-scope objects, approximately 59.6 percent. This is an approval-completion share for the scoped collection, not a measured image-quality score, public-access rate, or rights-clearance rate.

| Week | Captured objects | Checked objects | Approved records |
| --- | --- | --- | --- |
| 1 | 18 | 12 | 8 |
| 2 | 22 | 18 | 14 |
| 3 | 25 | 21 | 17 |
| 4 | 28 | 24 | 20 |
| 5 | 30 | 26 | 22 |
| 6 | 26 | 24 | 21 |
| 7 | 22 | 22 | 23 |
| 8 | 20 | 18 | 18 |

## Record model and example query

The small relational model has three tables: batch, object_record and issue. Each batch can contain many object records. Each object record belongs to exactly one batch. Each object record can have zero or more issues. The issue table points to an object record. No many-to-many relation or personal account table is part of this pilot.

batch has batch_id as its primary key and label as a required text field. object_record has object_id as its primary key, batch_id as a required foreign key to batch, title as required text, object_type as required text, status as required text, and image_filename as optional text. Allowed object types are postcard, poster and pamphlet. Allowed status labels are pending, captured, checked and published.

issue has issue_id as its primary key, object_id as a required foreign key to object_record, issue_text as required text, owner_role as required text, and resolved as a required integer flag of 0 or 1. The owner_role field stores a role, not a person's name. The fixture contains no real personal data.

The query below lists unresolved issues and includes the object title and batch label. It joins issues to objects through object_id, then objects to batches through batch_id. It orders the output by batch label and object identifier. The code explains the model. It is not a result table or evidence of query execution on the museum collection.

The accompanying SQL fixture can be run locally with SQLite to demonstrate the query. It has three example objects and two issues, separate from the 240-object collection and the weekly activity table. Its rows are not additional pilot activity and do not represent the complete collection. The example produces one unresolved issue for OBJ001 in Postcards A, with the title Harbor postcard and the issue text Confirm short title.

```sql
SELECT b.label, o.object_id, o.title, i.issue_text
FROM issue AS i
JOIN object_record AS o ON o.object_id = i.object_id
JOIN batch AS b ON b.batch_id = o.batch_id
WHERE i.resolved = 0
ORDER BY b.label, o.object_id;
```

## Checks and unresolved questions

Before a record is approved, confirm that its object identifier matches the object and image filename, that its batch exists, that title and object type are present, and that its status uses one of the four allowed labels. Review any issue associated with the object. Approval should be recorded by the checker, not inferred from a completed image filename.

The coordinator should confirm that every in-scope object belongs to one of the three batches and that each batch contains the planned 80 objects. The batch inventory totals are a planning control. The weekly activity table does not provide activity by batch, so no batch can be called the fastest or the most complete from this evidence.

The report should preserve three kinds of uncertainty. First, actual working time by stage was not measured. Second, no external quality audit was performed. Third, rights clearance and public release were outside the scope. A large approval count does not resolve any of those uncertainties. Clear presentation should make them easy to find without repeating a warning after every paragraph.

A trial review can ask whether the minimum metadata is enough for coordinators to find a record, whether issue descriptions lead to a clear next action, and whether the image naming convention remains consistent. These are questions for the next pilot, not findings from the first. The brief does not supply interview responses or measured error rates.

Record acceptance and committee review have distinct purposes. Acceptance concerns whether a record satisfies the operating checks; committee review concerns whether the project should continue and what further evidence is needed. No formal sign-off, named reviewer, compliance certification, completed backup test or security assessment is documented in the source.

## Proposed next pilot and reference notes

The source proposes a four-week second pilot, using the remaining uncaptured objects as its starting queue and continuing to resolve outstanding issues. This is a proposal awaiting committee approval. It does not promise to complete all 97 records not yet approved, because time per stage and object difficulty remain unknown. The committee can choose to approve, revise or defer the proposal.

In week 1, the proposal is to confirm the remaining queue and agree how time and corrections will be recorded. In weeks 2 and 3, volunteers would continue capture, metadata and checking while recording stage time and issue type. In week 4, the coordinator would summarize progress, review unresolved questions and bring the evidence back to the committee. This sequence is a proposed plan, not an account of work already completed.

The suggested decision is to authorize that limited follow-up only if the committee agrees to collect the missing time and correction data. That recommendation follows from the gaps in the first pilot; it is not a claim that the follow-up is cost-effective. Budget figures were not supplied. There is no measured cost per object or substantiated savings claim.

For this report, capture means that the image exists; checking means that the required checks have occurred; approval means entry into the pilot catalog. Public release is a separate question. An issue is a recorded problem requiring action, and a batch is one of the three planned groups of 80 objects.

The weekly activity record, batch inventory, operating brief and schema description form the evidence for this fictional project. The full collection, example SQL fixture and weekly activities are different scopes. External references do not verify the invented museum operations. This report records a project proposal and its limits rather than a completed public-release program.
