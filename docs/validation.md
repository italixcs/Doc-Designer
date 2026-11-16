# Validation record

Date: 16 November 2026. Candidate: Doc designer 0.1.2. Scope: the eight files under skills/doc-designer, identified by the [SHA-256 manifest](package-sha256.json). Prior evidence is preserved in [0.1.1](validation-0.1.1.md) and [0.1.0](validation-0.1.0.md); their manifests remain alongside them.

## Changes and checks

The candidate adds an optional genre-first reference workflow, original composition recipes, ray.so export/fallback guidance and native-column guidance. It does not include specimen binaries or third-party assets in the installable package. The core retains enough guidance for standalone use. MIT licensing is carried by the included license; activation metadata uses the required name and description fields.

| Check | Result and scope |
| --- | --- |
| Native skill-creator validator | Passed on the canonical personal skill directory; metadata/structure only |
| Relative package links | All five linked references exist |
| Frozen package identity | Current portable files match the frozen evaluation candidate and manifest |
| Personal skill update | Saved; post-reconciliation remote instruction/license/reference bytes match the portable package; host-managed UI metadata retained |
| Old/new diagnostic | Two cases, one attempt per arm; see results below |
| Static security scan | Completed over all eight portable package files; retained HIGH false positive described below |
| Original specimen exports | Three one-page A4 DOCX/PDF examples rendered and visually inspected in the preceding checkpoint; unchanged in this revision |
| Public visual acceptance | Not established; original rejected trial and unsuccessful comparison remain recorded |

## Diagnostic scope

Two fresh workers receive the same unseen one-page fictional museum-layout decision task, native document tools and output requirements. One reads frozen 0.1.1 instructions; the other reads frozen 0.1.2 instructions. The comparison is explicitly old/new, not no-skill/current, and uses forced reading rather than natural discovery. A second response-only pair handles a missing formal template, strict wording/monochrome constraints and a code-editor preview whose downloads fail. The artifact cost justifies two cases; adjacent negative activation is not retested because the activation description is unchanged.

Before execution, task text, input facts, critical requirements, criteria, candidate hashes, one-attempt budget and randomized neutral labels were saved. Separate fresh reviewers receive neutral A/B copies, identical task/rubric and inspection access, without worker traces or the mapping. Review verdicts are saved before mapping is revealed. Isolation and blinding are instruction-only: all agents share the filesystem and installed skill capabilities. Native defaults are inherited without overrides; exact backend revision, tokens, cost and per-agent timings are unknown.

| Case | Observed result | Blind preference |
| --- | --- | --- |
| Museum-layout decision artifact | Both preserve facts, denominators, no-selection state and limitations; both deliver editable one-page A4 DOCX and matching PDF. Independent reviewer re-exported both and found each pixel-identical to its supplied PDF. | Tie |
| Missing formal input / failed code export | Both request the source/template and preserve the strict format. Neither creates a document or invents missing content. | Old version, narrowly: it proposed an explicitly labeled capture of the requested browser preview before a disclosed local rendering fallback; the revision moved directly to the fallback. |

**Interpretation: no clear output-quality benefit on these cases.** The artifact outputs are restrained, conventional monochrome decision briefs; neither demonstrates the stronger aesthetic ambition by itself. The new worker reported inspecting a relevant Quarto interior, while both workers read their assigned profiles. That is workflow evidence, not proof that reference research improved the result. The edge result shows that export honesty must not be interpreted as forbidding an accurately labeled screenshot when that is the requested deliverable. No critical failure was found, and no further revision or rerun was selected merely to obtain a win.

Keep 0.1.2 for its explicit reference-to-production workflow and the user's ray.so preference, with the aesthetic claim still unproven. This comparison does not measure prompting effort saved. It does not establish native activation or reliable improvement across genres.

Raw worker artifacts, prompts, mappings and verdicts remain outside public version control. No diagnostic output is presented as an accepted before/after showcase. These small cases cannot establish universal design quality or statistical superiority.

## SkillSpector 2.12.0

Scanner source commit: c81615007d40e86051a302a3cf897f8a05264928. Command: skillspector scan PACKAGE --no-llm --fail-on-incomplete --format json --output REPORT, with resolved paths. Scope: exact eight-file portable package; no exclusions, suppressions, transitive fetch or semantic/LLM inference. No executable scripts or dependency manifest ship in the package. Dependency artifact inspection was not requested; optional runtime tools are outside scope.

Execution succeeded, exit 0. All 8/8 components were scanned; coverage 100%, is_complete true, status complete, zero partial/uninspected files, ledger exceptions or scope exclusions. All five resource references resolved. The previous path-like Carbon/ray.so prose has been replaced by clearer tool guidance, so its earlier unresolved-reference caveat is absent in this report.

Raw assessment: score 17, LOW recommendation SAFE, **maximum issue severity HIGH**. One retained issue: **HIGH PE3 Credential Access, SKILL.md line 22**, matching the unchanged sentence that prohibits following document instructions to upload files or access credentials. The exact prohibition was independently reviewed in 0.1.0 as a demonstrable false positive; that narrow disposition is reused because the sentence and meaning are unchanged. No credential path or mechanism is supplied. No rule or finding was suppressed. Exit 0 and status complete are not clean-finding verdicts.

Raw report SHA-256: dcde66be17a7785b8673ce06f81e11ecf719cd9af50701e5302fb2fd55bb0c06.

This is a completed static scan, not certification, endorsement or proof of runtime safety. Semantic analysis, runtime behavior, optional tools and future input content remain outside this evidence. Public docs and specimen build scripts are outside the installable package and this scan.

## Compatibility and delivery

Explicit profile reading and local DOCX/office-renderer mechanics are exercised; no claim is made about fresh native discovery. Microsoft Word, native Google Docs, ATS parsing, advanced equations/forms and PDF conformance are not runtime-validated here. The research browser successfully edited and previewed fictional code in ray.so; PNG/SVG export did not complete. No exported ray.so asset is claimed.

The repository remains private. Main-branch delivery is authorized; changing visibility or creating a public release remains a separate action. The skill is usable with these stated limits. Visual acceptance of a public before/after is still pending.
