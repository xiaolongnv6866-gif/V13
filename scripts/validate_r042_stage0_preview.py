#!/usr/bin/env python3
"""R042 two-book Cangjie Stage0 preview: SOURCE_STRUCTURE_ONLY public integrity.
Never assert user signoff, full-literary-B or unseen-fiction-C success from CI.
"""
import csv, re, json, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
issues=[]
def check(b,why):
    if not b:issues.append(why)
SOURCES={
 "wanming":("a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082",9),
 "tiexuecanming":("9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf",10)}
for book,(sha,task_count) in SOURCES.items():
    f=root/"books"/book/"BOOK_OVERVIEW.md"
    check(f.is_file(),f"{book} overview missing")
    if not f.is_file():continue
    s=f.read_text(encoding="utf-8")
    check(sha in s,f"{book} source fingerprint missing")
    check("STAGE0_FRAMEWORK_USER_APPROVED_WITH_LEGACY_DEBT" in s,f"{book} lacks approved-with-debt boundary")
    check("**用户确认时间**：2026-10-09" in s and "R042_USER_APPROVAL.md" in s,f"{book} explicit user approval missing")
    for section in ["## 基本信息","## 1. 结构","## 2. 解释","## 3. 批判","## 4. 应用潜力","## ✅ 质量门检查"]:
        check(section in s,f"{book} template section {section} missing")
    p1=s[s.find("## 1. 结构"):s.find("## 2. 解释")]
    check(len(re.findall(r"^\d+\. \*\*S[1-6]",p1,re.M))==6,f"{book} must have six independent source-based arcs")
    check("### 一句话主旨" in s and "### 作者要解决的核心问题" in s,f"{book} Adler overview logic missing")
    check(len(re.findall(r"^\d+\. \*\*P\d\d",s,re.M))==10,f"{book} ten propositions missing")
    check(len(re.findall(r"^\|"+("WM-" if book=="wanming" else "TX-")+r"\d\d\|",s,re.M))==task_count,f"{book} grounded independent original tasks wrong count")
    check("未被证明" in s and "最强反对意见" in s,f"{book} critical failure boundaries missing")
    check("NOT_RUN" in s and "PROVISIONAL" in s and "NOT_PASSED" not in s.split("## ✅ 质量门检查")[0],f"{book} wrong B/C display")
    loc=set()
    for nm in ["STRUCTURE_EVIDENCE.tsv","INTERPRETATION_EVIDENCE.tsv","CRITIQUE_EVIDENCE.tsv"]:
        ef=root/"books"/book/"adler"/nm
        check(ef.is_file(),f"{book}: {nm} missing")
        if ef.is_file():
            with ef.open(encoding="utf8",newline="") as f:
                for x in csv.DictReader(f,delimiter="\t"):
                    loc.add((int(x["narrative_ordinal"]),int(x["paragraph_index"])))
    used={(int(a),int(b)) for a,b in re.findall(r"n(\d{3})/p(\d+)",s)}
    unsupported=used-loc
    check(not unsupported,f"{book} locator not present in Stage0 evidence: {sorted(unsupported)}")
    print(book,"overview",len(s),"chars",len(used),"original numbered loci",len(loc),"prior original anchor locations",task_count,"original-task entries")
audit=root/"cangjie/reading/R042_STAGE0_QUALITY_AUDIT.md"
check(audit.is_file(),"R042 quality/debt review audit missing")
if audit.is_file():
    a=audit.read_text(encoding="utf8")
    for word in ["R008","R010","R013","R015","R017","R018","R023","R024","NEEDS_REVIEW","SOURCE","PROVISIONAL","NOT_RUN","61处","用户审阅"]:
        check(word in a,"R042 debt audit missing "+word)
run=root/"runs/R042.md"
check(run.is_file(),"R042 run receipt missing")
if run.is_file():
    s=run.read_text(encoding="utf8")
    check("BLOCKED_PENDING_USER_CONFIRMATION" in s,"R042 run not visibly blocked")
cur=json.loads((root/"CURRENT_ROUND.json").read_text())
pre_commit=cur["current_round"]=="R042" and cur["round_status"]=="BLOCKED" and cur["rounds_completed"]==41 and cur["last_passed_round"]=="R041" and cur["cangjie_stage0_gate"]=="NOT_PASSED"
accepted=int(cur["current_round"][1:])>=43 and int(cur["last_passed_round"][1:])>=42 and cur["rounds_completed"]>=42 and cur["cangjie_stage0_gate"]=="PASSED"
check(pre_commit or accepted,"R042 must be pending evidence-commit or formally approved and R043 NOT_STARTED")
check(cur["skill_certified_count"]>=0 and (not pre_commit or cur["heldout_bank_status"]=="SEALED_NOT_RUN"),"Invalid skill count or premature Stage0 opening")
check((root/"cangjie/reading/R042_USER_APPROVAL.md").is_file(),"Explicit user approval receipt missing")
if (root/"cangjie/reading/R042_USER_APPROVAL.md").is_file():
    ack=(root/"cangjie/reading/R042_USER_APPROVAL.md").read_text(encoding="utf8")
    check("批准R042两份BOOK_OVERVIEW研究框架，保留历史质量债按原文继续核查" in ack and "EXPLICIT_USER_APPROVAL_RECEIVED" in ack,"Approval receipt not tied to actual user phrase")
if accepted:
    check(cur.get("legacy_quality_debt_status") in ("OPEN_QUARANTINED","UNDER_REVIEW","CLOSED_WITH_SOURCE_PROOF") and cur.get("literary_interpretation_status") in ("PROVISIONAL","VERIFIED") and cur.get("original_output_test_status") in ("NOT_RUN","RUN","PASS"),"A/B/C state invalid")
with (root/"ROUND_LEDGER.csv").open(encoding="utf8",newline="") as f:
    rows={x["id"]:x for x in csv.DictReader(f)}
check(rows["R042"]["status"]==("PASSED" if accepted else "BLOCKED"),"ledger must reflect correct R042 gate state")
check(rows["R043"]["status"] in (("NOT_STARTED",) if not accepted else ("NOT_STARTED","PASSED")),"R043 status is inconsistent with R042 approval")
for x in issues:print("FAIL:",x)
print("R042",("FAIL" if issues else "PASS"),"SOURCE_STRUCTURE_ONLY; approved two-book Stage0 scope, 8-batch legacy risk audit; status="+("FORMAL_PASSED" if accepted else "AWAITING_FORMAL_COMMIT")+" B PROVISIONAL C NOT_RUN")
sys.exit(bool(issues))
