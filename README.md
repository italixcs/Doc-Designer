# Doc designer

An AI agent skill for Word documents and PDFs that look designed for their subject and their readers.

[Skill instructions](skills/doc-designer/SKILL.md) · [Free tools](skills/doc-designer/references/free-tools.md) · [Release notes](RELEASE_NOTES.md) · [Checks](docs/validation.md)

Use it to create a study sheet, explain a project, present an analysis, refine a resume, or redesign an existing document. It guides structure, typography, color, tables, code, diagrams, and page review, then works with the document tools your agent already has.

It can choose a local syntax highlighter, a diagram engine, or a publication-table tool when useful. It can also make a native Word table look considered. Tool count is not the goal: a coherent, readable, editable result is.

## Try it

Copy the complete [skills/doc-designer](skills/doc-designer) folder to your agent's supported skill location. It contains the core instructions, four optional references, UI metadata, and the MIT license. No package installation is needed to read the skill.

For **Codex**, the [documented](https://learn.chatgpt.com/docs/build-skills) repo-scoped location is:

```text
.agents/skills/doc-designer/SKILL.md
```

Keep the references, agents folder, and license alongside it. Invoke:

> Use $doc-designer to redesign this report for a nontechnical reader. Preserve the facts and references. Return an editable DOCX and a matching PDF.

For **ChatGPT**, use the supported skill-creation/import workflow available in your client and supply this folder or its core instructions. This repository is a skill folder, not a plugin or marketplace listing. Other agents can read SKILL.md manually; their native discovery is not verified.

The single **SKILL.md** also works as standalone instructions. Supporting files add tool links and production detail; they are optional, not hidden requirements.

## What changes

- The document's audience and purpose determine its structure.
- One visual system connects prose, tables, diagrams, code, and callouts.
- Editable content stays editable where the task requires it.
- Free specialists improve visuals when they offer a practical benefit.
- A rendered-page review catches problems that file creation alone cannot.

The skill supports new documents and faithful redesigns. It preserves supplied facts, citations, required sections, and the intended revision state. It does not silently rewrite content to fit a layout.

## Requirements and limits

The agent needs file access and a suitable document authoring/export tool. Editable DOCX plus PDF typically needs a DOCX library/editor and an office renderer. PDF-first work can use Typst, ReportLab, or another available engine. The [tool guide](skills/doc-designer/references/free-tools.md) lists free routes and fallbacks; installing the entire catalog is unnecessary.

No paid API, external upload, account, or proprietary font is required. Optional websites do not receive private content without authorization. Rendering varies by viewer, and the skill does not guarantee exact PDF-to-Word reconstruction, ATS results, or accessibility conformance.

## A small public exercise

Try [Borrow a tool](examples/borrow-a-tool/exercise.md): redesign a one-page fictional community handout. The [basic Word file](examples/borrow-a-tool/before.docx), [PDF](examples/borrow-a-tool/before.pdf), source, and exact prompt are included.

The first maintainer trial did not meet the intended visual-design standard: it improved formatting but remained generic. The current revision adds a separate design-acceptance gate. A public showcase still needs visual acceptance; no consistent improvement or finished showcase is claimed.

## Design directions under review

Three [original A4 specimens](examples/design-specimens/README.md) explore a community guide, a study sheet, and an analytical brief. Each includes editable DOCX, matching PDF, source and a preview. The [source map](docs/design-source-map.md) records which real references were inspected and how free tools can reproduce useful patterns. These are review candidates; no improved skill performance or accepted before/after is claimed.

Code-image preference: **ray.so**, with raw code retained. The editor preview was tested; export did not complete in the research browser.

## Evidence

[Research and plan](docs/research-and-plan.md) explains the scope and source decisions. [Validation](docs/validation.md) records structural, behavioral, security, and compatibility evidence, including their limits.

MIT licensed. External tools and templates retain their own terms. No private reference document, upstream template, font, or third-party skill implementation is distributed.
