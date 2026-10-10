#!/usr/bin/env python3
"""B069 structural and authenticity audit. Same-agent writing/review is NOT independent literary proof."""
import csv, json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1]
R69_OLD=['WM-f13','WM-f14','WM-p01','WM-p03']
R69_NEW=['WM-p04','WM-p05','WM-p07']
R70=['WM-p08','WM-p12','WM-p14','WM-p19','WM-p20','WM-p21','WM-p23']
NEW=R69_NEW+R70
CONTRACT_SHA='4e24d782632210c1e1637eba4954bde3d8f3846f'

def fail(b,msg):
    if not b: raise AssertionError(msg)
def readj(s): return json.loads((P/s).read_text('utf-8'))
def tsv(s):
    with (P/s).open('r',encoding='utf-8',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
def han(s): return len(re.findall('[\u3400-\u9fff]',s))

state=readj('V13_CURRENT_V3.json')
frozen=readj('v2/v3/FROZEN_TEST_CONTRACT.json')
contracts={x['candidate_id']:x for x in frozen['cases']}
allocation={x['candidate_id']:x for x in tsv('v2/v3/V3_TASK_ALLOCATIONS.tsv')}
old=tsv('v2/v3/results/R69_WM_4_PARTIAL.tsv')
r69=tsv('v2/v3/results/R69_WM_7.tsv')
r70=tsv('v2/v3/results/R70_WM_7.tsv')
fail([x['candidate_id'] for x in old]==R69_OLD,'do not alter original four R069 evidence')
fail([x['candidate_id'] for x in r69]==R69_OLD+R69_NEW,'original R069 complete 7/7')
fail([x['candidate_id'] for x in r70]==R70,'original R070 complete 7/7')
fail(r69[:4]==old,'B068 legacy R069 first four must be exactly preserved in merged table')
fail(len(NEW)==len(set(NEW))==10,'B069 exact 10 new candidates')
fail(11<=state['v3_original_47_completed']<=47,'B069 in progression')
fail(state['skill_certified_count']==0 or state['current_batch'] not in ('B069','B070'),'no premature certified SKILL')
for row in r69[4:]+r70:
    ident=row['candidate_id'];src=contracts[ident]
    fail(src['allocated_batch']=='B069','correct frozen batch '+ident)
    fail(src['test_id']==row['test_id'] and src['legacy_round']==row['legacy_round'],'frozen identifiers '+ident)
    fail([x['id'] for x in src['scoring']['shared_rubric']]==['S1','S2','S3','S4','S5'],'five fixed scoring dimensions '+ident)
    expected='outputs/R69/'+ident+'.json' if ident in R69_NEW else 'outputs/R70/'+ident+'.json'
    fail(row['raw_output_path']==expected,'canonical path '+ident)
    raw=readj('v2/v3/'+expected)
    fail(raw['test_id']==row['test_id'] and raw['candidate_id']==ident and raw['legacy_round']==row['legacy_round'],'raw ID '+ident)
    fail(raw['frozen_contract_blob_sha1']==CONTRACT_SHA,'unchanged prereg blob '+ident)
    fail(raw['experiment_mode']=='DIAGNOSTIC_ONLY_NONBLIND' and raw['skill_verified'] is False and raw['independent_judge']=='NOT_AVAILABLE','no fabricated evaluator '+ident)
    fail('NOT ESTABLISHED' in raw['arm_parity_contract'] and 'not established' in raw['environment_note'].lower(),'real nonblind disclosure '+ident)
    for arm in ('baseline','method'):
        p=raw[arm];body=p['scene_one']+p['scene_two']
        n=han(body)
        fail(500<=n<=750 and n==p['chinese_characters']==int(row[arm+'_chars']),'genuine narrative length '+ident+'/'+arm)
        fail(len(p['state_ledger'])>=4 and all(isinstance(x,dict) and x.get('fact') for x in p['state_ledger']),'state ledgers '+ident+'/'+arm)
        fail(p['unknowns'] and p['failure_risk_note'],'unknowns and risk '+ident+'/'+arm)
        scores=[int(x) for x in row[arm+'_scores'].split('/')]
        fail(len(scores)==5 and all(0<=x<=2 for x in scores) and sum(scores)==int(row[arm+'_total']),'shared rubric and arithmetic '+ident+'/'+arm)
    fail(int(row['delta'])==int(row['method_total'])-int(row['baseline_total']),'delta '+ident)
    fail(row['baseline_evidence_quote'] in raw['baseline']['scene_one']+raw['baseline']['scene_two'],'baseline quote supported '+ident)
    fail(row['method_evidence_quote'] in raw['method']['scene_one']+raw['method']['scene_two'],'method quote supported '+ident)
    fail(row['observed_failure_or_limit'] and row['hypothetical_counterexample_risk'] and row['hard_fail_found'],'failure and counterexample '+ident)
    fail(row['skill_verified']=='NO' and row['evaluation_mode']=='DIAGNOSTIC_ONLY_NONBLIND','diagnostic only '+ident)
    alloc=allocation[ident]
    fail(alloc['v3_execution_batch']=='B069' and alloc['legacy_round']==row['legacy_round'],'allocation preserved '+ident)
    fail(alloc['baseline_arm_status']=='TESTED_NONBLIND' and alloc['method_arm_status']=='TESTED_NONBLIND','both arms logged '+ident)
    fail(alloc['v3_status']=='TESTED_NONBLIND_NO_DEMONSTRATED_GAIN' and alloc['certified']=='NO','not certified '+ident)
# Specific staging: B069 real outputs can arrive while B069 cursor is still NOT_STARTED
if state['v3_original_47_completed']==11:
    fail(state['last_passed_batch']=='B068' and state['current_batch']=='B069','legal evidence-first staging state')
elif state['v3_original_47_completed']==21:
    fail(state['last_passed_batch']=='B069' and state['current_batch']=='B070','B069 sealed state')
fail(len(list((P/'v2/v3/outputs/R69').glob('WM-*.json')))==7,'R069 seven real independent method identifiers')
fail(len(list((P/'v2/v3/outputs/R70').glob('WM-*.json')))==7,'R070 seven real independent method identifiers')
print('B069 STRUCTURAL PASS: R069 7/7 + R070 7/7, 10 new real paired texts, 20 arms 500-750 Han, freeze and scores consistent. NONBLIND ONLY.')
