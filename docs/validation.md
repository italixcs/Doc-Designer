# Validation record

Date: 15 November 2026. Candidate: Doc designer 0.1.0. Scope: the seven files under skills/doc-designer, identified by [SHA-256 manifest](package-sha256.json). Public docs and the fictional exercise are outside the installable package.

## Checks

| Check | Result | Scope and limits |
| --- | --- | --- |
| Native skill-creator validator | Passed | Metadata/name/scaffold checks; not proof of behavior |
| Package resource links and identity | Passed | Four linked references present; package matches the frozen candidate |
| Explicit skill loading | Passed | Independent workers read the frozen core; native automatic discovery was not tested |
| Real artifact pair | Both passed; modest preference for skill-assisted result | One task and one attempt per arm; best-effort blind review |
| Missing-input pair | Both passed; modest preference for skill-assisted response | Neither invented an unseen document; both requested source |
| Adjacent negative smoke | Passed | Both answered 3 kg = 3000 g directly; not a native activation test |
| Public exercise | Passed | Baseline generator executed; editable DOCX and one-page A4 PDF rendered and inspected; factual text checked |
| README local browser preview | Blocked | Playwright browser unavailable; system Chromium failed because local socket creation is restricted. No rendered GitHub/mobile/light-dark claim |
| Public screenshot exercise | Pending maintainer | Exact prompt and fictional source are included; not yet presented as a completed showcase |

## Behavioral diagnostic

Two fresh workers performed the same one-page fictional volunteer handout task. Both received identical facts, output requirements, native tools and renderer access. One additionally received an explicit path to the frozen skill. A separate fresh reviewer received randomized neutral labels, original task, frozen criteria, and both artifacts. Verdicts were saved before the controller revealed the mapping.

Both outputs preserved all operating facts, exact warning, table values and planning-estimate qualification. Both contained native editable Word text and tables. The reviewer rendered the supplied PDFs and independently converted both DOCX files at the same 140 dpi. Each supplied PDF matched its corresponding DOCX render pixel-for-pixel in the installed LibreOffice environment. Neither had clipping or overlap.

The reviewer modestly preferred the skill-assisted version for coordinated visual grouping, warning placement before the process, and more explicit estimate labeling. The other output remained usable and compliant. No critical failure occurred in either arm.

The missing-input case requested an exact illustrated redesign without attaching its source. Both responses requested the missing file and avoided fabricated artifacts. The reviewer modestly preferred the skill-assisted response for explaining equation/diagram editability limits and a page-verification plan.

**Interpretation: helps on these cases, with low confidence about generalization.** This is one attempt per arm per case, not a statistical benchmark. No additional repeats were run. The artifact task was the expensive case; the second case was response-only. A nearby unit-conversion task was a small negative smoke check.

Model/harness: native agent defaults inherited from the controller; no model override. Exact backend revision, token usage, cost, and per-worker timing were not reported and remain unknown. Fresh histories and neutral labels reduced leakage, but all agents shared a filesystem and installed capabilities. Separation and blinding were instruction-only, not enforced. The target was explicitly supplied rather than naturally discovered. No causal or universal superiority claim follows.

Raw worker artifacts, mapping, traces, reviewer packets and scanner output remain outside public version control. The public summary retains the observed limits; no private reference input was used as a diagnostic fixture.

## SkillSpector

- Tool: NVIDIA SkillSpector 2.12.0, source commit c81615007d40e86051a302a3cf897f8a05264928.
- Invocation: skillspector scan PACKAGE --no-llm --fail-on-incomplete --format json --output REPORT, with PACKAGE/REPORT resolved locally.
- Scope: exact seven-file installable package, including references, UI metadata and license; no exclusions or suppressions.
- Execution: successful; exit 0; 7/7 fully inspected, 0 partial/uninspected; coverage 100%; is_complete true.
- Report status: **complete_with_caveats**. Semantic/LLM analysis was disabled; no inference was run.
- Raw static assessment: score 17, LOW recommendation SAFE, **maximum issue severity HIGH**. Exit 0 is not a clean-finding verdict.
- Dependencies: no executable scripts or dependency manifest are distributed. No claim is made about vulnerabilities in optional runtime tools or their dependencies.
- Raw report SHA-256: 6893bc60e3554690c0c974f1a848be58c0b5f303c36f4ea3fea662a71ba99c1c.

### Retained finding and triage

**HIGH PE3 Credential Access, SKILL.md line 21:** the scanner matched “access credentials” in a sentence explicitly prohibiting following embedded document instructions to upload files or access credentials.

Disposition: demonstrable false positive for this exact hit. The prohibition grants no credential access, supplies no credential path or mechanism, and denies operational authority to untrusted source content. A separate fresh reviewer examined that sentence and confirmed the narrow disposition. The finding remains recorded; no baseline suppressed it, no wording was changed to obtain a clean scan, and no vendor correction is claimed.

**Nonfatal reference-resolution caveat, SKILL.md line 64:** a path-like reference did not match a bundled artifact. The line names optional Carbon/ray.so code-image tools in prose. Independent review found no intended bundled file at that location; interpreting the slash as a local reference is a likely parser explanation, not a verified scanner trace. All actual relative Markdown resource links were checked separately and exist.

This is a completed static scan with reviewed caveats, not certification, endorsement, a clean scan, or proof of runtime safety. LLM semantic analysis, external tool security and future document contents are outside this evidence.

## Compatibility

| Route | Evidence level |
| --- | --- |
| Manual/explicit reading by native agents | Exercised in this diagnostic |
| Managed personal skill saving | Saved and remote reconciled path verified |
| Codex .agents/skills/doc-designer | Official discovery documentation checked; package copy is complete; fresh automatic-discovery runtime not exercised |
| Other Agent Skills hosts | Standard metadata/folder structure; manual use only, native discovery untested |
| python-docx + LibreOffice DOCX/PDF | Exercised on the one-page diagnostic and baseline fixture |
| Microsoft Word / native Google Docs | Not runtime-tested |
| Other optional catalog tools | Documentation/source-reviewed selection guidance; not comprehensively runtime-tested |
| PDF/UA, PDF/A, ATS parsing, advanced equations/forms | No conformance or performance claim |

The instructions can be used now. Public launch preparation still includes the maintainer's screenshot review and an explicit visibility/release action.
