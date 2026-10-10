#!/usr/bin/env python3
"""B072 genuine real paired output consistency audit ONLY, not independent literary efficacy validation."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
R73_OLD=['TX-p06','TX-p07','TX-p08','TX-p09']
R73_NEW=['TX-p11','TX-p12']
R74=['TX-p13','TX-p14','TX-p17','TX-p19','TX-p20','TX-p21']
NEW=R73_NEW+R74
FREEZE='4e24d782632210c1e1637eba4954bde3d8f3846f'
def must(x,m):
 if not x:raise AssertionError(m)
def j(p):return json.loads((P/p).read_text(encoding='utf-8'))
def tsv(path):
 with (P/path).open('r',encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def han(s):return len(re.findall('[\u3400-\u9fff]',s))
state=j('V13_CURRENT_V3.json')
fr={c['candidate_id']:c for c in j('v2/v3/FROZEN_TEST_CONTRACT.json')['cases']}
alloc={a['candidate_id']:a for a in tsv('v2/v3/V3_TASK_ALLOCATIONS.tsv')}
old=tsv('v2/v3/results/R73_TX_4_PARTIAL.tsv')
r73=tsv('v2/v3/results/R73_TX_6.tsv')
r74=tsv('v2/v3/results/R74_TX_6.tsv')
must([x['candidate_id'] for x in old]==R73_OLD,'prior R073 four unchanged')
must([x['candidate_id'] for x in r73]==R73_OLD+R73_NEW,'R073 full six')
must([x['candidate_id'] for x in r74]==R74,'R074 exact six')
must(r73[:4]==old,'prior four results must preserve each field')
must(39<=state['v3_original_47_completed']<=47,'B072 39->47')
must(state['skill_certified_count']==0,'no fabricated certification')
must(len(list((P/'v2/v3/outputs/R73').glob('TX-*.json')))==6,'R073 full 6 raw outputs')
must(len(list((P/'v2/v3/outputs/R74').glob('TX-*.json')))==6,'R074 full 6 raw outputs')
for row in r73[4:]+r74:
 ident=row['candidate_id'];src=fr[ident]
 must(src['allocated_batch']=='B072' and src['test_id']==row['test_id'] and src['legacy_round']==row['legacy_round'],'frozen identity '+ident)
 must([q['id'] for q in src['scoring']['shared_rubric']]==['S1','S2','S3','S4','S5'],'frozen rubric '+ident)
 path=f'outputs/{"R73" if ident in R73_NEW else "R74"}/{ident}.json'
 must(row['raw_output_path']==path,'output path '+ident)
 obj=j('v2/v3/'+path)
 must(obj['test_id']==row['test_id'] and obj['candidate_id']==ident and obj['legacy_round']==row['legacy_round'],'original raw IDs '+ident)
 must(obj['frozen_contract_blob_sha1']==FREEZE and obj['experiment_mode']=='DIAGNOSTIC_ONLY_NONBLIND','preregistered and nonblind '+ident)
 must(obj['skill_verified'] is False and obj['independent_judge']=='NOT_AVAILABLE','not verified '+ident)
 must('NOT ESTABLISHED' in obj['environment_note'] and 'NOT ESTABLISHED' in obj['arm_parity_contract'],'no simulated independent arms '+ident)
 for arm in ('baseline','method'):
  p=obj[arm];s=p['scene_one']+p['scene_two'];n=han(s)
  must(p['scene_one'].strip() and p['scene_two'].strip() and 500<=n<=750 and n==p['chinese_characters']==int(row[arm+'_chars']),'real two scene Han length '+ident+'/'+arm)
  must(len(p['state_ledger'])>=4 and all(isinstance(x,dict) and x.get('fact') for x in p['state_ledger']) and p['unknowns'] and p['failure_risk_note'],'ledger and negative boundary '+ident+'/'+arm)
  rubric=[int(x) for x in row[arm+'_scores'].split('/')]
  must(len(rubric)==5 and all(0<=x<=2 for x in rubric) and sum(rubric)==int(row[arm+'_total']),'five-score arithmetic '+ident+'/'+arm)
  must(row[arm+'_evidence_quote'] in s,'quotes grounded in authored scenes '+ident+'/'+arm)
 must(int(row['delta'])==int(row['method_total'])-int(row['baseline_total']),'correct delta '+ident)
 must(row['observed_failure_or_limit'] and row['hypothetical_counterexample_risk'] and row['hard_fail_found'],'counterevidence present '+ident)
 must(row['skill_verified']=='NO' and row['evaluation_mode']=='DIAGNOSTIC_ONLY_NONBLIND','no independent certification '+ident)
 a=alloc[ident]
 must(a['v3_execution_batch']=='B072' and a['legacy_round']==row['legacy_round'],'frozen allocation '+ident)
 must(a['baseline_arm_status']=='TESTED_NONBLIND' and a['method_arm_status']=='TESTED_NONBLIND' and a['v3_status']=='TESTED_NONBLIND_NO_DEMONSTRATED_GAIN' and a['certified']=='NO','logged both arms without certification '+ident)
if state['v3_original_47_completed']==39:
 must(state['current_batch']=='B072' and state['last_passed_batch']=='B071','valid evidence-first stage')
elif state['v3_original_47_completed']==47:
 # B072's 47-case invariant remains valid after later batches advance the legitimate cursor.
 current=state['current_batch'];last=state['last_passed_batch']
 must(re.fullmatch(r'B[0-9]{3}',current) is not None and re.fullmatch(r'B[0-9]{3}',last) is not None,'valid V13.2 batch IDs')
 must(73<=int(current[1:])<=96 and 72<=int(last[1:])<=int(current[1:]),'B072 complete and no cursor regression')
# Check all 47 frozen candidate IDs have one result row, one raw file, and one tested-not-verified allocation.
results=[]
for f in ['R68_WM_7.tsv','R69_WM_7.tsv','R70_WM_7.tsv','R71_TX_7.tsv','R72_TX_7.tsv','R73_TX_6.tsv','R74_TX_6.tsv']:
 results.extend(tsv('v2/v3/results/'+f))
must(len(results)==47 and len(set(x['candidate_id'] for x in results))==47,'original V3 47 unique rows')
must(set(x['candidate_id'] for x in results)==set(fr),'all 47 frozen IDs present')
for row in results:
 ident=row['candidate_id'];path='v2/v3/'+row['raw_output_path']
 must((P/path).exists(),'one actual archived raw output for '+ident)
 a=alloc[ident]
 must(a['baseline_arm_status']=='TESTED_NONBLIND' and a['method_arm_status']=='TESTED_NONBLIND','both arms tested for all 47 '+ident)
 must(a['certified']=='NO' and row['skill_verified']=='NO','47 tasks do not imply certified skills '+ident)
print('B072 STRUCTURE PASS: R073 6/6 + R074 6/6, 8 new original paired outputs, 16 arms 500-750 Han, original 47 unique results and sources archived; 0 independently verified skills')
