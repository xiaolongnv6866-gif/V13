#!/usr/bin/env python3
"""V13 R042 Stage0 approval brief & legacy-claim quarantine verification.
All evidence here is GitHub SOURCE_STRUCTURE_ONLY; this cannot approve Stage0.
"""
from pathlib import Path
import csv,json,sys
R=Path(__file__).resolve().parents[1]
fail=[]
def expect(good,what):
 if not good:fail.append(what)
p=R/"cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv"
with p.open(encoding="utf8",newline="") as f: rows=list(csv.DictReader(f,delimiter="\t"))
expect(len(rows)==14,"14 case-specific historic claims required")
expect(len(set(x["legacy_claim_id"] for x in rows))==14,"duplicate legacy claim")
reviewed={'R008','R009','R011','R012','R013','R014','R016','R017','R018','R019','R020','R021','R022','R023'}
expect(set(x['round_id'] for x in rows)==reviewed,"unexpected source round coverage")
for x in rows:
 original=R/f'cangjie/reading/{x["round_id"]}/{ "wanming" if x["book_slug"]=="wanming" else "tiexue"}_receipts.jsonl'
 expect(original.is_file(),"missing old source "+str(original))
 if original.is_file():
  found=False
  with original.open(encoding='utf8') as f:
   for line in f:
    if not line.strip():continue
    rec=json.loads(line)
    if rec.get('narrative_ordinal')==int(x['narrative_ordinal']):
     found=any(z.get('claim_id')==x['legacy_claim_id'] for z in rec.get('mechanism_claims',[]))
     expect(x['legacy_support'] in [z['anchor_id'] for z in rec.get('anchors',[])], 'old support anchor absent '+x['legacy_claim_id'])
     break
  expect(found,'historical claim missing '+x['legacy_claim_id'])
 expect(x['routing_status'].startswith(('REVISED_PROVISIONAL','CONFIRMED_NARROW_PROVISIONAL')),'false B verification '+x['legacy_claim_id'])
 expect(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE','unquarantined legacy claim '+x['legacy_claim_id'])
 expect(len(x['source_boundary'])>=18,'missing source scope')
audit_files={'R042_TARGETED_REPAIR.md','R042_RISK_WAVE2_AUDIT.md'}
for x in rows:
 expect(x['audit_file'] in audit_files,'unlinked audit '+x['legacy_claim_id'])
 expect((R/'cangjie/reading'/x['audit_file']).is_file(),'referenced audit missing')
brief=(R/'cangjie/reading/R042_APPROVAL_BRIEF.md').read_text(encoding='utf8')
for key in ['《晚明》','《铁血残明》','WM-01','TX-01','14条','296条','SOURCE_STRUCTURE_ONLY','NOT_RUN','BLOCKED','明确回复']:
 expect(key in brief,'decision brief gap '+key)
for name in ['wanming','tiexuecanming']:
 s=(R/f'books/{name}/BOOK_OVERVIEW.md').read_text(encoding='utf8')
 expect('R042_APPROVAL_BRIEF.md' in s,'overview lacks linked decision context '+name)
 expect('R042_OLD_CLAIM_QUARANTINE.tsv' in s,'overview lacks legacy-claim warning '+name)
 expect('**用户确认时间**：2026-10-09' in s and 'STAGE0_FRAMEWORK_USER_APPROVED_WITH_LEGACY_DEBT' in s,'approval date/scope missing '+name)
cur=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
pre_commit=cur['current_round']=='R042' and cur['round_status']=='BLOCKED' and cur['last_passed_round']=='R041' and cur['rounds_completed']==41 and cur['cangjie_stage0_gate']=='NOT_PASSED'
accepted=int(cur['current_round'][1:])>=43 and int(cur['last_passed_round'][1:])>=42 and cur['rounds_completed']>=42 and cur['cangjie_stage0_gate']=='PASSED'
expect(pre_commit or accepted,'R042 or R043 state violates explicit approval flow')
expect(cur['skill_certified_count']>=0 and (not pre_commit or cur['heldout_bank_status']=='SEALED_NOT_RUN'),'Invalid Stage0 control state')
approval=(R/'cangjie/reading/R042_USER_APPROVAL.md')
expect(approval.is_file(),'no explicit user approval receipt')
if approval.is_file():
 a=approval.read_text(encoding='utf8')
 expect('EXPLICIT_USER_APPROVAL_RECEIVED' in a and '批准R042两份BOOK_OVERVIEW研究框架，保留历史质量债按原文继续核查' in a,'user confirmation not exact')
if accepted:
 expect(cur.get('legacy_quality_debt_status') in ('OPEN_QUARANTINED','UNDER_REVIEW','CLOSED_WITH_SOURCE_PROOF') and cur.get('literary_interpretation_status') in ('PROVISIONAL','VERIFIED'),'legacy quality status unrecognized')
with (R/'ROUND_LEDGER.csv').open(encoding="utf8",newline="") as f: ledger={x['id']:x for x in csv.DictReader(f)}
expect(ledger['R042']['status']==('PASSED' if accepted else 'BLOCKED') and ledger['R043']['status']=='NOT_STARTED','R043 started or R042 gate inconsistent')
for e in fail:print('FAIL:',e)
print('R042 BRIEF & LEGACY QUARANTINE', 'FAIL' if fail else 'PASS',str(len(rows))+' verified legacy IDs; user approved Stage0 scope; public SOURCE_STRUCTURE_ONLY; R042 '+('PASSED' if accepted else 'pending state commit'))
sys.exit(bool(fail))
