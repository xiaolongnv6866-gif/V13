#!/usr/bin/env python3
"""V13.2 B071: structural audit of 9 new real paired source files; no independent literary approval."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
R72_OLD=['TX-f12','TX-f13']
R72_NEW=['TX-f16','TX-p01','TX-p03','TX-p04','TX-p05']
R73_FIRST=['TX-p06','TX-p07','TX-p08','TX-p09']
NEW=R72_NEW+R73_FIRST
FREEZE='4e24d782632210c1e1637eba4954bde3d8f3846f'
def must(v,m):
 if not v:raise AssertionError(m)
def j(s):return json.loads((P/s).read_text('utf-8'))
def tsv(s):
 with (P/s).open('r',encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def han(s):return len(re.findall('[\u3400-\u9fff]',s))
state=j('V13_CURRENT_V3.json');fr=j('v2/v3/FROZEN_TEST_CONTRACT.json');cases={x['candidate_id']:x for x in fr['cases']}
alloc={x['candidate_id']:x for x in tsv('v2/v3/V3_TASK_ALLOCATIONS.tsv')}
prior=tsv('v2/v3/results/R72_TX_2_PARTIAL.tsv')
full=tsv('v2/v3/results/R72_TX_7.tsv')
part=tsv('v2/v3/results/R73_TX_4_PARTIAL.tsv')
must([x['candidate_id'] for x in prior]==R72_OLD,'preserve R072 original first two')
must([x['candidate_id'] for x in full]==R72_OLD+R72_NEW,'R072 seven complete')
must(full[:2]==prior,'R072 B070 first two must be byte-equivalent fields')
must([x['candidate_id'] for x in part]==R73_FIRST,'R073 exactly first 4 partial')
must(len(list((P/'v2/v3/outputs/R72').glob('TX-*.json')))==7,'R072 seven files')
must(len(list((P/'v2/v3/outputs/R73').glob('TX-*.json'))) in (4,6),'R073 first four remain and subsequent B072 may legally add two')
must(30<=state['v3_original_47_completed']<=47,'rolling V3 in range')
must(state['skill_certified_count']==0 or state['current_batch'] not in ('B071','B072'),'no premature certified skill')
for row in full[2:]+part:
 id=row['candidate_id'];source=cases[id]
 must(source['allocated_batch']=='B071' and source['test_id']==row['test_id'] and source['legacy_round']==row['legacy_round'],'frozen allocation '+id)
 must([q['id'] for q in source['scoring']['shared_rubric']]==['S1','S2','S3','S4','S5'],'frozen five dimensions '+id)
 folder='R72' if id in R72_NEW else 'R73';path='outputs/'+folder+'/'+id+'.json'
 must(row['raw_output_path']==path,'original path '+id)
 obj=j('v2/v3/'+path)
 must(obj['candidate_id']==id and obj['test_id']==source['test_id'] and obj['legacy_round']==row['legacy_round'],'source ID '+id)
 must(obj['frozen_contract_blob_sha1']==FREEZE and obj['experiment_mode']=='DIAGNOSTIC_ONLY_NONBLIND','frozen & no fake blind '+id)
 must(obj['skill_verified'] is False and obj['independent_judge']=='NOT_AVAILABLE','no independent judge '+id)
 must('NOT ESTABLISHED' in obj['environment_note'] and 'NOT ESTABLISHED' in obj['arm_parity_contract'],'arm isolation disclosure '+id)
 for arm in ('baseline','method'):
  p=obj[arm];body=p['scene_one']+p['scene_two'];n=han(body)
  must(500<=n<=750 and n==p['chinese_characters']==int(row[arm+'_chars']),'500-750 Han real narrative '+id+'/'+arm)
  must(p['scene_one'].strip() and p['scene_two'].strip() and p['unknowns'] and p['failure_risk_note'],'two scenes and unknowns '+id+'/'+arm)
  must(len(p['state_ledger'])>=4 and all(isinstance(x,dict) and x.get('fact') for x in p['state_ledger']),'valid narrative state ledger '+id+'/'+arm)
  parts=list(map(int,row[arm+'_scores'].split('/')))
  must(len(parts)==5 and all(0<=x<=2 for x in parts) and sum(parts)==int(row[arm+'_total']),'S1-5 scores '+id+'/'+arm)
  must(row[arm+'_evidence_quote'] in body,'quoted evidence grounded in original writing '+id+'/'+arm)
 must(int(row['delta'])==int(row['method_total'])-int(row['baseline_total']),'score arithmetic '+id)
 must(row['observed_failure_or_limit'] and row['hypothetical_counterexample_risk'] and row['hard_fail_found'],'negative example present '+id)
 must(row['evaluation_mode']=='DIAGNOSTIC_ONLY_NONBLIND' and row['skill_verified']=='NO','provisional only '+id)
 a=alloc[id];must(a['v3_execution_batch']=='B071' and a['legacy_round']==row['legacy_round'],'allocation intact '+id)
 must(a['baseline_arm_status']=='TESTED_NONBLIND' and a['method_arm_status']=='TESTED_NONBLIND' and a['v3_status']=='TESTED_NONBLIND_NO_DEMONSTRATED_GAIN' and a['certified']=='NO','both arms noted and not certified '+id)
if state['v3_original_47_completed']==30:
 must(state['current_batch']=='B071' and state['last_passed_batch']=='B070','evidence-first B071 stage')
elif state['v3_original_47_completed']==39:
 must(state['current_batch']=='B072' and state['last_passed_batch']=='B071','final B071 seal')
print('B071 STRUCTURAL PASS: original R072 7/7 incl preserved prior 2, R073 partial 4/6, 9 new paired real outputs, 500-750 Han, score states and quote invariants; no verified skill')
