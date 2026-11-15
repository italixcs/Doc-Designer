# Design sources and production routes

Research checkpoint: 15 November 2026. This map separates visual inspection from discovery. A platform listing is not evidence that every template is good, free, or reusable. These are starting points for choosing a direction for the actual brief, not a universal house style.

## Sources inspected

| Use case | Source and inspection | Useful pattern | Adaptation and limits |
| --- | --- | --- | --- |
| Study notes | [Typst Universe: non-boring-notes](https://typst.app/universe/package/non-boring-notes/), version 0.3.0; manifest and rendered thumbnail inspected | Distinct semantic treatments for definitions and worked material | Give examples and errors different roles. Avoid a large title block or contents list on a short sheet. Package manifest declares MIT. |
| Compact reference sheets | [cram-snap](https://typst.app/universe/package/cram-snap/), version 0.2.2; manifest and rendered Git-sheet thumbnail inspected | Command/explanation pairing and compact topic groups | Use density only when readers need rapid lookup. The small landscape typography is unsuitable as a default teaching format. Manifest declares MIT. |
| Resumes | [modern-cv](https://github.com/ptsouchlos/modern-cv); README and rendered resume image inspected | Dates and roles have consistent alignment and section rhythm | Adapt alignment, not the crowded contact/icon header. License was not checked in this checkpoint; no assets or template code reused. No ATS guarantee. |
| Analytical reports | [Quarto gallery](https://quarto.org/docs/gallery/) and its [Tufte PDF](https://quarto-dev.github.io/quarto-gallery/page-layout/tufte.pdf); PDF page 5 visually inspected | Evidence, code, prose and captions share a considered reading order | Put a finding beside its supporting figure and limits. Do not copy tutorial whitespace indiscriminately. No upstream material redistributed. |
| Quantitative tables | [flextable gallery](https://ardata.fr/en/flextable-gallery/) and [source README](https://github.com/davidgohel/flextable); actual mtcars README figure visually inspected | Selective cell emphasis and numeric patterns | Conditional color should explain data. A simple loan table benefits more from spacing and clear durations than a heatmap. No upstream table or code copied. |
| Editorial reports and showcases | [Ingka report archive](https://www.ingka.com/reports/), linked [Life at Home report](https://assets.site.ingka.com/ingka-com/reports/GC-CF-LAHR-FY25-External-Report-BringJoyHome.pdf); PDF pages 5 and 12 visually inspected | Wide reading columns; large thematic anchors; repeated category structures | Translate hierarchy into portrait pages rather than copying landscape geometry. Page 12 uses large colored circles to structure four themes; this is a specific editorial device, not a default decoration. Copyrighted reference only. No report assets redistributed. |
| Code specimens | [ray.so](https://ray.so/) actual editor tested with fictional SQL | Syntax-colored code in a controlled frame | Preferred code-image route. Editing and preview worked without a sign-in wall in this session. PNG/SVG export did not complete in this browser; do not claim a successful exported specimen. Keep raw source and offer a reproducible setup. |

These sources demonstrate individual patterns. They do not prove the current skill produces a better document. The original specimens in [examples/design-specimens](../examples/design-specimens/) test translations into editable A4 documents; they are authored examples, not a new blind evaluation or accepted showcase.

## Platforms to explore by brief

| Brief | Starting platform | What to inspect before choosing |
| --- | --- | --- |
| Worksheets and learning packs | [Canva worksheet templates](https://www.canva.com/worksheets/templates/), Typst Universe | Actual page density, space for answers, worked examples, reading level. Canva mixes free and premium resources; select a genuinely free route and verify export. |
| Guides, portfolios and general documents | [Canva document templates](https://www.canva.com/documents/templates/), [Behance editorial projects](https://www.behance.net/search/projects/editorial%20report) | Inspect several relevant interior pages, not only a cover mockup. Behance is inspiration, not permission to reuse. |
| CVs and academic reports | Typst Universe; Quarto gallery | Role/date alignment, long-entry behavior, references, page breaks and output format. |
| Charts and analytical elements | [Matplotlib gallery](https://matplotlib.org/stable/gallery/index.html), [gt articles](https://gt.rstudio.com/articles/index.html), flextable gallery | Match chart type to the question, make units and sources visible, keep underlying data. |
| Technical diagrams | [Graphviz gallery](https://graphviz.org/gallery/) | Choose notation for the actual relationship, then inspect labels at final print size. |

These broader platform entries are discovery routes, not a claim that selected template pages were visually reviewed in this checkpoint.

## Free production routes

| Element/output | Route | Why and tradeoff |
| --- | --- | --- |
| Editable DOCX | python-docx; free office renderer for PDF | Native paragraphs, styles, columns and real data tables remain editable. Viewer pagination can vary; render the actual final file. [Official docs](https://python-docx.readthedocs.io/en/latest/) were checked through Context7 for keep-with-next and picture sizing. |
| Publication-oriented PDF | Typst or Quarto | Good typesetting; PDF-first geometry does not automatically become an equally editable DOCX. Pick the required deliverable before the engine. |
| Data tables | Native DOCX tables, flextable, or gt | Native tables are appropriate for comparisons. [gt export documentation](https://gt.rstudio.com/reference/gtsave.html) describes DOCX and other export routes; image/PDF routes have dependencies. Check the requested format rather than relying on a README summary. |
| Exact charts | Matplotlib, with saved data and SVG | Precise labels and reproducible calculations. Embed a suitable image in DOCX and retain editable chart source; a chart image is not native Word chart data. |
| Code artwork | ray.so preferred; local syntax highlighter if unavailable | Preserve raw code when readers need to copy it. Explicitly disclose a fallback. Avoid private source in share URLs or external editors without authorization. |
| Diagrams | Graphviz or another free exact diagram engine | Retain source and inspect printed labels; do not use image generation for exact relations. |
| Icons | Original drawings or [Lucide](https://lucide.dev/icons/) | Lucide uses ISC, with Feather-derived material under MIT. Check attribution/license obligations for the selected assets. No Lucide assets are used in the current specimens. |

No paid API or premium font is required. Free tool availability and website terms can change, so verify the chosen route at task time. The specimens use installed Liberation and DejaVu fonts; no font files are bundled.

## What should enter the skill after review

1. A brief-specific reference search: inspect real interior pages and name the useful pattern.
2. A small composition recipe tied to purpose, not a fixed palette or ornament list.
3. Element-level routing: editable table, exact chart, code artwork or diagram only when useful.
4. A visual checkpoint before final export, including density, wrapping and continuity.
5. Honest capability reporting: preview, export, editability and successful delivery are separate checks.

Review the specimens first. Do not expand the core instructions merely to make them longer, and do not describe the rejected trial as a successful before/after.
