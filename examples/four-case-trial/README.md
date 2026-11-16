# Four document design trials

Two tracks, each with a short and long task. These are ready-to-run maintainer exercises for Doc designer 0.1.2, not completed tests or evidence that the skill improves output. All content is fictional, purpose-written, and safe to use in a public demonstration. No private reference or upstream template is included.

| Case | Task | Input to attach | Expected result |
| --- | --- | --- | --- |
| R1 | Short redesign | short/before.docx and short/before.pdf | One A4 page; editable DOCX and matching PDF |
| R2 | Long redesign | long/before.docx and long/before.pdf; long/activity.csv, long/schema.sql, long/query.sql | 6–8 A4 pages; editable DOCX and matching PDF; technical sources |
| C1 | Short creation | short/create-brief.md only | One A4 page; editable DOCX and matching PDF |
| C2 | Long creation | long/create-brief.md, long/activity.csv, long/schema.sql, long/query.sql | 6–8 A4 pages; editable DOCX and matching PDF; technical sources |

Use the corresponding prompt in [prompts.md](prompts.md). The creation inputs contain matching substantive facts as raw notes, rather than the already written report or its layout. This makes creation test planning and writing as well as formatting. Do not attach the before documents or previously designed examples to creation runs.

## Why this scope

The short task tests useful hierarchy, a compact comparison, practical instructions and a reminder under a strict one-page limit. The long task adds continuity, different content roles, page breaks, a chart, a relationship model and a code excerpt. Six to eight pages is enough to expose many production problems without padding the report to make it look substantial.

The short document is a first-time workshop guide. The long document is a project report for a committee and volunteer coordinators. They share a fictional museum identity but have different audiences and purposes. This tests some adaptation; it does not cover resumes, math-heavy notes, legal documents, forms, or every subject.

The baseline is deliberately basic, not broken or falsely attributed to another agent. A polished after image alone does not prove that the skill caused the improvement. These trials test practical fitness and visual acceptance, not superiority over a no-skill baseline.

## Run fairly

1. Keep version 0.1.2 unchanged during the four attempts. Record the model, available tools and version used; use the same environment where practical.
2. Start a fresh chat for each case. Supply only the listed inputs and exact prompt. Save the first completed result, including failures and limitations.
3. Do not show a worker another case's result, our earlier specimens, or the review checklist. Otherwise later runs may borrow an answer rather than use the skill independently.
4. Run once per case. Record corrections you had to request. Do not keep rerunning until one output looks good. If a tool blocks, keep that limitation visible.
5. Review actual DOCX and PDF files using [review.md](review.md), not screenshots alone. Keep scores or notes outside the reader-facing documents.

This is an explicitly invoked skill trial. It does not test automatic activation. Running all four through one chat introduces carryover and should be disclosed. Human effort saved, token cost and speed are unknown unless measured.

## Inputs and rebuild

- [Short baseline DOCX](short/before.docx) / [PDF](short/before.pdf)
- [Long baseline DOCX](long/before.docx) / [PDF](long/before.pdf)
- [Short creation notes](short/create-brief.md)
- [Long creation notes](long/create-brief.md); the full baseline [text](long/content.md) and [structured source](long/content.json) remain available for inspection, not creation attachments
- [Activity data](long/activity.csv), [SQL fixture](long/schema.sql), [example query](long/query.sql)

Free dependencies for the original fixture builder: Python and python-docx. Run python build_fixtures.py. It also verifies activity totals and executes the example query using SQLite. Render the resulting files with an available free office renderer to create matching PDFs; the builder alone does not export PDFs. Fonts are installed Liberation Sans, not bundled files. These sources use the repository MIT license.

The baseline DOCX/PDF files have been built and visually inspected. That verifies the exercise inputs only. No redesigned or newly created trial output has been produced or graded yet.

## Public evidence

For redesign, use equal paper size, page scale and comparable crops. For the long document, show a full-document overview plus the corresponding data and code/model pages; do not pick only the best page. If page order changes, compare the same content and explain the change.

Creation has no before document. Show the brief or content excerpt beside the result and label it **brief to document**, not before/after. Keep all four outcomes visible in the summary, even if only one becomes a showcase. Do not publish traces, private account details or unrelated filenames. A benchmark or consistent-improvement claim would require a separate controlled comparison.
