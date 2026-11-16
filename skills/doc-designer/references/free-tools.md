# Free tools and templates

Read when selecting a production or visual tool. No paid account or subscription is necessary. Recheck current web export limits before use; a free local route must remain viable. Links are documentation, not authorization to upload material.

## Document engines

| Official source | Suitable work | Limits / fallback |
| --- | --- | --- |
| [python-docx](https://python-docx.readthedocs.io/) | Editable DOCX, styles, tables, inline figures, targeted edits | Does not render or paginate; complex OOXML needs care. Use an available office editor for unsupported features. |
| [docx for JavaScript](https://docx.js.org/) | New DOCX in Node environments | Do not assume existing-file preservation; python-docx is an alternative. |
| [Pandoc](https://pandoc.org/MANUAL.html) | Structured prose, highlighting, citations, conversion | DOCX uses a reference document; PDF requires an engine. Conversion is not lossless redesign. |
| [Quarto](https://quarto.org/docs/output-formats/ms-word.html) | Reproducible analyses, figures, cross-references | Format-specific layout varies; Pandoc plus local figures is a smaller alternative. |
| [docxtpl](https://docxtpl.readthedocs.io/) | Repeated use of approved DOCX templates | Tag placement and long substitutions need testing; targeted edits are a fallback. |
| [LibreOffice](https://www.libreoffice.org/) | Free editing and DOCX→PDF export/rendering | Word fidelity can differ. Without an office renderer, report visual/export validation blocked. |
| [Typst](https://typst.app/docs/) | PDF-first reports and math | Free local compiler; no DOCX route. ReportLab or another installed engine is an alternative. |
| [ReportLab](https://docs.reportlab.com/) | Programmatic PDF, measured layout and flowables | Use the open-source toolkit. Not editable Word; accessibility needs explicit checks. |
| [WeasyPrint](https://doc.courtbouillon.org/weasyprint/) | Paged PDF from HTML/CSS | System dependencies and CSS support vary; available browser print is an alternative with pagination checked. |

## Visual specialists

| Need / source | Decision |
| --- | --- |
| [Pygments](https://pygments.org/docs/formatters/) | Local lexing to editable Word runs, or SVG/PNG code images; preserve raw source. |
| [ray.so](https://ray.so/) | Preferred optional code-artwork editor. Choose a page-compatible theme, language, padding and background; export PNG/SVG if supported. Verify the actual downloaded file, not only the preview. Retain raw source. If export fails or external use is unsuitable, disclose a local Pygments fallback. |
| [Carbon](https://carbon.now.sh/about) | Alternative optional code-image editor; check current free export and privacy before use. |
| [gt](https://gt.rstudio.com/reference/gtsave.html), [flextable](https://davidgohel.github.io/flextable/) | Publication tables when an R toolchain is suitable. Actual DOCX and HTML output differ; test the chosen format. gt image/PDF export has extra rendering dependencies. Native Word tables remain a good fallback. |
| [Matplotlib](https://matplotlib.org/stable/users/explain/figure/backends.html), [ggplot2](https://ggplot2.tidyverse.org/) | Charts generated from actual data; size for the document and save editable source. |
| [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli), [Graphviz](https://graphviz.org/) | Reproducible diagram source and SVG/PNG; use authored SVG for notation the engine cannot express. |
| [draw.io Desktop](https://www.drawio.com/docs/security/diagrams-offline/) | Free local diagram editing; preserve .drawio source. Desktop and offline browser features differ. |
| [Inkscape](https://inkscape.org/), [GIMP](https://www.gimp.org/) | Vector/image refinement when simpler tools do not suffice. |
| [Google Fonts FAQ](https://developers.google.com/fonts/faq), [Font Library](https://fontlibrary.org/) | Verify font license, language coverage, embedding, and availability. Installed free fonts avoid downloads. |

## Template discovery

For a genre-first search, inspected-pattern examples, and the transition from reference to an original composition, use the reference-workflow guide linked from SKILL.md. Browse only what the brief needs; no gallery requires registration or copying assets to use the core workflow.


- [Typst Universe](https://typst.app/universe/): browse by genre, inspect source and individual package/template licenses. Implementation and starter files can have different terms.
- [Pandoc reference documents](https://pandoc.org/MANUAL.html#option--reference-doc) and [Quarto Word templates](https://quarto.org/docs/output-formats/ms-word-templates.html): style references for repeatable Word reports. Reference body content is not a page template.
- [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template): optional PDF/LaTeX starting point for lecture notes/exercises. Requires compatible Pandoc and LaTeX; not a Word theme.

Templates are examples, not evidence of suitability. Inspect source before running builds, avoid macros, pin incorporated versions, and preserve required license notices. Open-source code does not automatically license accompanying logos, fonts, images, or sample content. No upstream templates or fonts are bundled with this skill.

If a specialist improves only decoration, use an installed alternative. If a missing tool is necessary for a promised format or check, disclose the missing capability. Do not claim a website was used when a locally created asset merely resembles its style.
