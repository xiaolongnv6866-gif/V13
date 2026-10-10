#!/usr/bin/env python3
"""V13.2 B070 real paired output / frozen contract structural audit only. NOT an independent literary judgment."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
A=['TX-f01','TX-f02','TX-f05','TX-f08','TX-f09','TX-f10','TX-f11']
B=['TX-f12','TX-f13']
IDs=A+B
FREEZE='4e24d782632210c1e1637eba4954bde3d8f3846f'
def must(v,msg):
 if not v: raise AssertionError(msg)
def j(s):return json.loads((P/s).read_text('utf-8'))
def tsv(s):
 with (P/s).open('r',encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def han(s):return len(re.findall('[\u3400-\u9fff]',s))
source=j('v2/v3/FROZEN_TEST_CONTRACT.json')
cases={x['candidate_id']:x for x in source['cases']}
alloc={x['candidate_id']:x for x in tsv('v2/v3/V3_TASK_ALLOCATIONS.tsv')}
st=j('V13_CURRENT_V3.json')
must(21<=st['v3_original_47_completed']<=47,'cumulative V3 count legal')
must(st['skill_certified_count']==0 or st['current_batch'] not in ('B070','B071'),'never grant fabricated certification')
ra=tsv('v2/v3/results/R71_TX_7.tsv')
rb=tsv('v2/v3/results/R72_TX_2_PARTIAL.tsv')
must([x['candidate_id'] for x in ra]==A and [x['candidate_id'] for x in rb]==B,'exact seven+two')
must(len(list((P/'v2/v3/outputs/R71').glob('TX-*.json')))==7,'only seven R071 raw outputs')
for row in ra+rb:
 id=row['candidate_id'];fr=cases[id];folder='R71' if id in A else 'R72';rel='outputs/'+folder+'/'+id+'.json'
 must(fr['allocated_batch']=='B070' and fr['test_id']==row['test_id'] and fr['legacy_round']==row['legacy_round'],'frozen test ID '+id)
 must(row['raw_output_path']==rel,'exact path '+id)
 must([x['id'] for x in fr['scoring']['shared_rubric']]==['S1','S2','S3','S4','S5'],'frozen S1-5 '+id)
 raw=j('v2/v3/'+rel)
 must(raw['test_id']==fr['test_id'] and raw['candidate_id']==id and raw['legacy_round']==row['legacy_round'],'raw identifier '+id)
 must(raw['frozen_contract_blob_sha1']==FREEZE and raw['experiment_mode']=='DIAGNOSTIC_ONLY_NONBLIND','frozen contract and nonblind label '+id)
 must(raw['skill_verified'] is False and raw['independent_judge']=='NOT_AVAILABLE','no fake verified '+id)
 must('NOT ESTABLISHED' in raw['environment_note'] and 'NOT ESTABLISHED' in raw['arm_parity_contract'],'no fake blind isolation '+id)
 for arm in ('baseline','method'):
  t=raw[arm];n=han(t['scene_one']+t['scene_two'])
  must(500<=n<=750 and n==t['chinese_characters']==int(row[arm+'_chars']),'raw two-scene han length '+id+'/'+arm)
  must(t['scene_one'].strip() and t['scene_two'].strip() and len(t['state_ledger'])>=4 and t['unknowns'] and t['failure_risk_note'],'two scenes ledgers unknowns risks '+id+'/'+arm)
  must(all(isinstance(x,dict) and x.get('fact') for x in t['state_ledger']),'valid state entries '+id+'/'+arm)
  score=list(map(int,row[arm+'_scores'].split('/')))
  must(len(score)==5 and all(0<=x<=2 for x in score) and sum(score)==int(row[arm+'_total']),'shared rubric 0-2 '+id+'/'+arm)
  must(row[arm+'_evidence_quote'] in t['scene_one']+t['scene_two'],'short evidence quote belongs to original '+id+'/'+arm)
 must(int(row['delta'])==int(row['method_total'])-int(row['baseline_total']),'delta arithmetic '+id)
 must(row['hypothetical_counterexample_risk'] and row['observed_failure_or_limit'] and row['hard_fail_found'],'negative cases '+id)
 must(row['skill_verified']=='NO' and row['evaluation_mode']=='DIAGNOSTIC_ONLY_NONBLIND','diagnostic result only '+id)
 v=alloc[id];must(v['v3_execution_batch']=='B070','original allocation '+id)
 must(v['baseline_arm_status']=='TESTED_NONBLIND' and v['method_arm_status']=='TESTED_NONBLIND' and v['v3_status']=='TESTED_NONBLIND_NO_DEMONSTRATED_GAIN' and v['certified']=='NO','allocation both arms honest '+id)
if st['v3_original_47_completed']==21:
 must(st['current_batch']=='B070' and st['last_passed_batch']=='B069','allow evidence-first staged commit')
elif st['v3_original_47_completed']==30:
 must(st['current_batch']=='B071' and st['last_passed_batch']=='B070','seal correct')
print('B070 STRUCTURE PASS: 9 IDs, 18 real two-scene original texts, 500-750 Han each, R071 7/7 and R072 2/7, self-rating only. NO INDEPENDENT VERIFIED SKILL.')
