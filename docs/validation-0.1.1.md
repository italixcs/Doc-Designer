# Validation record

Date: 15 November 2026. Candidate: Doc designer 0.1.1. Scope: seven files under skills/doc-designer, identified by the [current SHA-256 manifest](package-sha256.json). The [0.1.0 record](validation-0.1.0.md) and its [manifest](package-sha256-0.1.0.json) are preserved.

## Why the earlier result was insufficient

The maintainer rejected the first public exercise trial as visually too generic. It preserved content and produced a readable document, but its conventional heading stack, standard shaded table and bold reminder fell short of the requested design ambition. Earlier correctness and legibility checks did not establish adequate visual quality. The original positive diagnostic remains recorded, with this counterexample added rather than hidden.

The new instructions distinguish technical validity from composition, specificity, hierarchy, craft and meaningful before/after improvement. They ask for a concrete organizing idea, relevant free visual precedents where available, active consideration of specialist tools, and deliberate component treatment. They preserve required plain/formal templates.

## Current checks

| Check | Result and limits |
| --- | --- |
| Native skill-creator validation | Passed on the managed skill checkout; checks metadata/scaffolding only |
| Resource links and package identity | Passed; four relative references present; frozen package identity checked |
| Managed personal skill saving | Updated and saved; instruction and resource bytes checked against the candidate; host-managed UI metadata differs |
| Old/new handout diagnostic | Completed; results discussed below; one run per arm |
| Formal-template response diagnostic | Both passed; reviewer narrowly preferred the old response for its explicit conflict handling |
| Static security scan | Completed with retained finding/caveat, detailed below |
| Public visual acceptance | Not passed; the first maintainer trial was rejected and the current revision is not claimed as a visual fix |

## Behavioral diagnostic

The comparison used the original 0.1.0 instructions and revised 0.1.1 instructions, explicitly supplied to fresh native agents. Both received the same fictional tool-library source, task, free native tools, output requirements and office renderer. Both also received the same scope/budget reminder. One attempt per arm; no repetitions or selected-best output.

The task was the same public one-page exercise. That directly targets the demonstrated failure but is not an unseen generalization test. Both produced editable one-page A4 DOCX and matching PDFs, preserved the supplied facts and table values, removed only the allowed repeated reminder, and inspected their renders. Neither used paid services or remote publication.

The blind reviewer narrowly preferred the **old** handout for consistent alignment, clearer topic grouping and page balance. The revised handout had a stronger complete numbered process. Both were judged competent but conventional, with limited subject-specific character. The reviewer independently rendered both DOCX files at 144 dpi; each matched its supplied PDF pixel-for-pixel. The original source was initially omitted from the neutral review packet, then supplied unchanged before the source-fact verdict; criteria and candidates did not change.

The formal check was an unseen response-only request for a mandated black-and-white single-column application statement with fixed headings and unchanged wording, with inputs not yet attached. Both respected the constraints and deferred production until input arrived. The blind reviewer narrowly preferred the old response for explicitly flagging conflicts before any content/structure changes. There were no critical failures; actual document execution was not tested in this case.

Each reviewer had a fresh history and randomized neutral candidate labels. Quality verdicts were saved before the controller read the mapping. Both workers and reviewers shared a filesystem; separation and blinding were instruction-only. Native automatic discovery was not tested. Exact backend model revision, token usage, cost and per-worker timings were not reported and remain unknown.

The controller's visual review found that the revised handout remained close to a conventional office layout. The instructions are more explicit, but this run does not justify claiming that the user's aesthetic requirement is solved. Small preference differences do not substitute for maintainer acceptance. No benchmark, statistical superiority or reliable improvement across document genres is claimed.

**Result: no clear benefit from this instruction-only revision on these cases.** Both narrow preferences favored the old version; neither case had a critical failure. Keep 0.1.1 as an unproven candidate that clarifies the intended design bar, not as a demonstrated quality improvement. Do not repeat the same comparison until a further material change is justified.

Raw artifacts, mappings, prompts and review packets remain private. No rejected document or private reference screenshot is published as a finished showcase.

## SkillSpector 2.12.0

A fresh static scan covered the exact current seven-file package. Scanner source commit: c81615007d40e86051a302a3cf897f8a05264928. Invocation: skillspector scan PACKAGE --no-llm --fail-on-incomplete --format json --output REPORT, with paths resolved locally. No LLM inference, suppressions or exclusions.

Execution succeeded, exit 0; 7/7 components fully inspected, zero partially/uninspected, coverage 100%, is_complete true. Status remains **complete_with_caveats**. The raw assessment is score 17, LOW recommendation SAFE, but **maximum issue severity HIGH**. Exit 0 is not a clean-finding verdict.

- **HIGH PE3, SKILL.md line 23:** unchanged prohibition on following document instructions to upload files or access credentials. The exact sentence was independently reviewed in 0.1.0 as a demonstrable false positive. The disposition is reused because that text and its meaning are unchanged; the finding is retained rather than suppressed.
- **Nonfatal missing-reference caveat, line 76:** unchanged optional Carbon/ray.so prose. The prior narrow review found no intended bundled artifact at that location; all actual relative resource links exist. The suspected path-parser interpretation remains an inference.

Raw report SHA-256: 6b5d7f55bcaddd802ee97e8deaaad04c1af1adcd9993389460974cfdb3357425.

No scripts or dependency manifest ship in the skill. Optional external tools and runtime dependencies are not security-validated by this scan. Semantic analysis, runtime behavior and future document contents remain outside scope. This is not certification or a clean scan.

## Compatibility and publication

Explicit instruction reading and python-docx/LibreOffice production were exercised. Codex repository discovery paths were documentation-checked; native automatic discovery, Microsoft Word and Google Docs were not runtime-tested. Other catalog tools, ATS parsing, advanced equations/forms and PDF conformance have no new claims.

The earlier README browser preview remained blocked by local Chromium/socket restrictions; no GitHub/mobile/theme render claim was added. Repository visibility remains private. No public release or finished before/after showcase is created. The next design iteration should use stronger worked visual references and actual output review, not another assertion that more rules guarantee quality.
