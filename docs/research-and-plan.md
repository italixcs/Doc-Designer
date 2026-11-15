# Doc designer: research and implementation plan

Research date: 15 November 2026. Recommendation: build a focused design layer over existing document engines, rather than another file-conversion framework.

## Need and boundaries

Agents can already create DOCX and PDF. The recurring gap is the chain from subject and reader to structure, visual system, specialist assets, and inspected pages. A polished code image with an unrelated chart theme is not a coherent document. Conversely, a well-styled editable table can be better than a screenshot.

The skill covers new documents and faithful redesigns: study sheets, portfolios, analyses, reports, guides, resumes, and showcases. It chooses hierarchy, page rhythm, typography, semantic color, tables, code, diagrams, and export checks. It preserves required content and supports user-supplied themes.

It does not implement a renderer, guarantee universal Word/PDF fidelity, supply missing sources, guarantee ATS parsing, certify accessibility from appearance, or replace specialist editorial/subject review. Simple conversion and text-only tasks are outside its activation scope. It adds no paid API, hosted account, installer, or mandatory third-party service.

## Existing work reviewed

| Source | Finding | Decision |
| --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | Small metadata entrypoint with optional resources | Standard folder, concise activation, progressive disclosure |
| [Anthropic DOCX skill](https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md) | Existing mechanics, OOXML gotchas, rendering and preservation | Complement existing mechanics; no copied implementation or bundled upstream skill |
| [python-docx documentation](https://python-docx.readthedocs.io/en/latest/user/text.html) | Semantic formatting and pagination properties | Editable Word route; explicitly require a separate renderer |
| [Pandoc manual](https://pandoc.org/MANUAL.html) | Reference DOCX controls styles/properties; current syntax-highlighting options | Good structured-document route; not a universal visual template |
| [Quarto Word basics](https://quarto.org/docs/output-formats/ms-word.html) and [templates](https://quarto.org/docs/output-formats/ms-word-templates.html) | Reproducible analytical documents and Word style references | Optional for analysis-heavy work; avoid making a large toolchain mandatory |
| [Typst PDF documentation](https://typst.app/docs/reference/pdf/) | PDF-first typesetting; semantic accessibility with additional manual obligations | PDF route, no promise of DOCX conversion or automatic conformance |
| [Typst Universe licensing](https://github.com/typst/packages/blob/main/docs/licensing.md) | Packages, starter templates, and assets can carry different terms | Link discovery sources; do not redistribute unreviewed templates/fonts |
| [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) | Lecture/exercise PDF template with Pandoc/LaTeX prerequisites | Useful optional reference, not a default for every topic or Word output |
| [Pygments formatters](https://pygments.org/docs/formatters/) | Local code lexing and SVG/image output | Local editable-token or image paths, retain source |
| [Carbon accessibility note](https://carbon.now.sh/about) and [ray.so](https://ray.so/) | Attractive code-image tools, with image-text limitations | Optional free export; verify current limits; no private uploads by inference |
| [gt export](https://gt.rstudio.com/reference/gtsave.html) | Export paths and dependencies differ across Word, HTML, and images | Inspect actual target output; native table remains valid |
| [Matplotlib backends](https://matplotlib.org/stable/users/explain/figure/backends.html) | Data-driven raster/vector export | Match final document size and visual system |
| [Mermaid](https://mermaid.js.org/config/usage.html) and [draw.io offline](https://www.drawio.com/docs/security/diagrams-offline/) | Reproducible text diagrams or local editing | Select notation deliberately and preserve source |
| [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) | Static analysis with explicit coverage and optional semantic analysis | Static-only release check, triage findings, no paid inference |

GitHub MCP supplied repository/source evidence. Context7 supplied library documentation for python-docx, Pandoc, and Typst. Primary websites filled tool/export/template gaps. Source review is not a runtime test of every listed tool. Optional catalog entries should be checked against current official documentation when selected for a real task.

## Design translation

The supplied visual reference was inspected privately. No source text, images, personal details, filenames, or screenshots from it are distributed here. Only general observations informed the skill: coordinate typography and accent color; give callouts a clear role; make code and diagrams feel part of the same document; inspect final-scale labels.

| Interface-design principle | Document adaptation | Excluded web-specific rule |
| --- | --- | --- |
| Clear focal point | Useful opening and strongest evidence at readable scale | Mandatory cinematic hero |
| Shared tokens | Word styles / named typesetting parameters | Framework-specific CSS |
| Structural variety | Content-led report, study, resume, guide patterns | Random layouts, universal sales funnels |
| Deliberate framing | Crop authentic evidence without cutting meaning | Fake application/device chrome |
| Actual-size review | Rendered pages, print/grayscale, export checks | Hover/scroll animation requirements |
| Restraint and specificity | Purposeful callouts and topic-specific diagrams | Generic decorative bento/card systems |

The instructions are newly written. No source text, code, template, logo, or font from the reviewed projects is redistributed. External tools retain their own licenses; the repository MIT license applies to this project's original material and does not relicense those tools.

## Package architecture

- Core: self-contained SKILL.md, usable even without optional files.
- Optional references: design patterns, free tools, production routes, quality review.
- Host metadata: agents/openai.yaml, no required MCP dependencies.
- License: preserved MIT license.
- No executable code, template binaries, fonts, private inputs, or scanner inside the installable folder.
- Public README, research, checks, release notes, and synthetic showcase exercise live outside the package.

## Implementation and acceptance

1. Inspect the reference privately and identify transferable choices.
2. Verify existing workflows and free/local alternatives.
3. Author through the native skill creator and validate metadata/resources.
4. Freeze package hashes before behavioral checks.
5. Run one real artifact pair and one missing-input pair with a blind reviewer; check a nearby non-document task. Fresh agents share a filesystem, so report instruction-only isolation and forced invocation honestly.
6. Scan the exact package using SkillSpector static mode. Preserve raw evidence privately; publish scope, caveats, and triage without claiming certification.
7. Prepare truthful installation, tool requirements, release notes, and a small fictional before/after exercise.
8. Push the authorized candidate to main, retaining private repository visibility. The maintainer's screenshot exercise precedes a public launch; do not create a public release or change visibility now.

Acceptance: complete portable core; no mandatory paid tools; differentiated use cases; faithful redesign safeguards; format-aware tool selection; content/visual checks; real evidence with limits; no private content; complete package and linked public docs.

## What remains a real-world test

The maintainer exercise is a one-page fictional tool-library handout, unrelated to any personal project. It tests a different reader and subject from the internal repair-desk case. It can demonstrate hierarchy, callouts, tables, and consistency, but cannot establish quality across all document genres. Native discovery on additional hosts, Microsoft Word/Google Docs rendering, advanced mathematical layouts, and conformance-specific PDF workflows need their own tests.

## Maintainer feedback and revision

The first maintainer trial was rejected as visually too generic. A stacked heading/paragraph layout, conventional shaded table, and bold reminder met the content and legibility requirements without meeting the intended design ambition. The initial validation therefore set too low a bar for the stated goal.

Version 0.1.1 adds a separate design-acceptance gate, concrete composition decisions, relevant visual-precedent inspection, active consideration of specialist visual tools, and genre-sensitive examples. Technical validity remains necessary, but no longer stands in for visual acceptance. A formal-template smoke check guards against adding decoration where the user explicitly forbids it. The revision must earn its design claims through actual output and review; instruction changes alone are not evidence of success.
