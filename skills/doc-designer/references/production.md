# Production procedures

Read only the relevant route. Resolve actual paths, versions, permissions, and capabilities in the current host. Host document-tool procedures take precedence.

## Editable Word

1. Inventory drawings, equations, fields, revisions, comments, links, headers, footnotes, and other objects before editing. Paragraph extraction alone misses important content.
2. Build named title, heading, body, caption, table, code, and note styles. Prefer inheritance to direct formatting. Set page size and margins explicitly.
3. Fit table widths to usable page width. Repeat headers; avoid exact heights on wrapping rows. Prevent short rows splitting where appropriate, but let long tables flow. Simplify merged cells when possible.
4. Use native section columns for genuine multi-column reading flow, not tables that merely position prose. Calculate column widths plus gaps against usable page width, and inspect section transitions and reading order. Use a real table for related records and comparisons.
5. Use keep-with-next for headings/captions and widow/orphan controls for prose. Applying it everywhere can move entire sections. Use section breaks for landscape or changed headers and inspect transitions.
6. Prefer inline figures for stable flow. Test SVG support in the target consumer; retain vector originals with PNG fallbacks when needed.
7. Update/verify TOC and reference fields through the office renderer. An XML field instruction can have a blank or stale displayed value.
8. Render the latest file and inspect its pages. Reopening through a library verifies structure, not appearance.

python-docx exposes distinct paragraph_format properties: keep_with_next, keep_together, page_break_before, and widow_control. Some other features require reviewed OOXML changes; preserve unrelated package parts. Avoid rebuilding a complex source solely from extracted text.

Pandoc's reference DOCX controls styles and properties rather than copying its body. Current documentation uses --syntax-highlighting; check installed help before choosing version-sensitive flags. Label code languages and inspect the export theme.

For editable highlighted code, map local Pygments lexer tokens to Word runs. Preserve indentation, whitespace, and semantics. Use a limited light-background theme for normal print. Keep line numbers out of copyable source or provide raw source separately.

## Matching PDF from DOCX

Author DOCX first and export that exact final version. Use the host's renderer when available. Otherwise an installed LibreOffice can convert with --headless --convert-to pdf --outdir followed by source path. Use a unique writable user profile for concurrent conversions. Check actual output existence, nonzero size, and freshness; a process exit alone is insufficient.

Render PDF pages with an available viewer/renderer such as Poppler pdftoppm. Inspect every page, compare text/values, and check font substitution, links, and pagination. State which renderer was used; LibreOffice export is not a Microsoft Word runtime test.

## PDF-first

Choose Typst/LaTeX for structured typesetting and math, ReportLab for programmatic flow/layout, or HTML/CSS print for suitable source. Use semantic selectable text and flow layout for long content. Set dimensions, language, fonts, margins, and metadata; retain source/data/diagrams.

Inspect exported pages through an actual PDF renderer. Check searchable text, links, symbols, figures, notes, and reading order where relevant. PDF/UA, PDF/A, forms, signatures, and production-print color requirements need additional suitable workflows/validators. Visual inspection does not certify them. Do not flatten forms or alter signed files as routine styling.

## Dimensions and assets

Usable width = page width − left margin − right margin. At 160 mm wide, a 300 PPI raster needs about 1890 pixels across. Check final label size separately. Keep vector originals rather than repeatedly resampling screenshots.

Check transparency on actual paper color. Remove unwanted export padding and control surrounding spacing in the document. Harmonize rules, fonts, and captions. Check grayscale when relevant.

## Native documents

For Google Docs or another native service, use its supported host capabilities and preserve file identity/collaboration state. A DOCX copy is an interchange artifact, not verification of the live file. Inspect requested exports separately and state which surface was checked.
