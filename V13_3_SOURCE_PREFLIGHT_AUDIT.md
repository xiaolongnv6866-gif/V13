# V13.3 | Global pre-N01 source audit and historical errata

Date: 2026-10-11. Authorized by user choice B. Administrative correction only, not an extra round, NOT_STARTED N01 and 0/48 unchanged.

## Findings, fully audited
- Frozen 426 issues: 296 Stage0 literature B claims, 14 R042 quarantines, 39 V1, 11 V2, 47 V3, 19 R057 topics; all source paths exist. Original issue IDs match old frozen registry 426/426.
- **290/296 wrong-round source pointers**, all wrongly routed to `cangjie/reading/R007/wanming_receipts.jsonl` in original registry and Stage0 audit. Only 6 R007 paths were correct. All 290 corrected in active V13.3 426-row map.
- Eighteen original chapter receipt files (nine each book) were inspected. All 720 JSONL records parse successfully, hold the expected EPUB hashes, and span correct successive 40-chapter ordinal ranges. **296/296 chapter locators and 314/314 paragraph anchors were found in corresponding original-round receipts.** Six R007 frozen source anchors were `nundefined`, now resolved to real narrative ordinals in new operational locator table without overwriting originals.
- All 187 candidate Markdown links resolve to actual section headings. Crosswalk identity checks: WM91/TX96, historical reference108 / needs_review79 / verified0, 69 V3=47+22 all linked to candidate IDs, original Stage0 20 tasks retained alongside historical R057 19 topic links, 44 original contracts mapped without deletion.
- Pre-existing `scripts/validate_v13_3_plan.py` wrongly froze N01 NOT_STARTED / 0/48 and old future V3/Stage0 state forever. Now it checks sequential live V4 cursor against ledger, while retaining historical baseline and enforcing source+anchor correspondence in CI.

## Auditable fix / authority
- Active `V13_3_ISSUES_426_TO_ROUNDS.tsv`: 290 corrected source cells, all original ID, round, quality and coverage fields unchanged.
- `V13_3_SOURCE_RESOLUTION_296.tsv`: per-ID old path, historical source anchor, actual round/book/ordinal/anchors, receipt Git blob and exact scope. All entries explicitly `LOCATOR_VERIFIED_ONLY_B_PROVISIONAL`.
- Original `v2/ISSUE_REGISTRY.tsv` and `v2/stage0/STAGE0_B_AUDIT_STATUS_V2.tsv` are deliberately *not edited*. They are historically frozen and contain those old mislinks. Do not use their source pointer as live truth; use active V13.3 mapping plus source resolution.
- GitHub Actions source check validates existence, original round, correct book, chapter, original anchors, receipt Git blob SHA and 187 heading links. It is a structural/locator test, **not** a literary content verdict.

## Unaltered quality debts
296 B literary interpretation verdicts still require their original N01-N15 true EPUB scene reading, context, alternative loss and boundary. 192 old B claims remain not individually reviewed; 14 original quarantine items remain isolated; 69 independent V3 not run; original Stage0 independent C 0/20; certified Skill=0. No verified promotion is inferred from valid locators. User's next `继续` starts N01 alone, with 17 original B IDs + 1 R042 quarantined ID. The original V13.3 48-round plan, current progress and every user confirmation/independent-test gate are unchanged.
