#!/usr/bin/env python3
"""R056 honest Cangjie V3 paired task comparison. Technical consistency ONLY.
The same agent drafted both arms and ratings: NOT independent blinded proof.
"""
from pathlib import Path
import csv,copy,json,re,sys,hashlib
R=Path(__file__).resolve().parents[1]
T=R/'tests/v3';U=R/'tests/v2'
err=[]
def ck(ok,msg):
    if not ok:err.append(msg)
def readj(x):return json.loads((x).read_text(encoding='utf8'))
def readt(x):
    with x.open(encoding='utf8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def errorscore(record,base,cand,criteria):
    problems=[]
    def ensure(x,msg):
        if not x:problems.append(msg)
    fields=('scene_A','scene_B','state_contract','unknowns')
    def actual_text(x):return '\n'.join(str(x.get(f,'')) for f in fields)
    ensure(record.get('id')==base.get('id')==cand.get('id'),'task_id_mismatch')
    evidence_fields=[('baseline_three_criteria_evidence',actual_text(base)),('candidate_three_criteria_evidence',actual_text(cand))]
    for key,txt in evidence_fields:
        quotes=record.get(key)
        ensure(isinstance(quotes,list) and len(quotes)==len(criteria),'wrong_three_criteria_'+key)
        if not isinstance(quotes,list):continue
        for i,quote in enumerate(quotes):
            ensure(isinstance(quote,str) and len(quote)>=3 and quote in txt,'unsupported_quote_'+key+str(i))
    for prefix in ('baseline','candidate'):
        dims=record.get(prefix+'_dims',{})
        expect={'causal_chain','character_agency_continuity','epistemic_boundaries','deliverable_traceability'}
        ensure(set(dims)==expect,'missing_dimension_'+prefix)
        for k,v in dims.items():ensure(type(v) is int and 0<=v<=2,'dimension_range_'+prefix+'_'+k)
        if set(dims)==expect and all(type(x) is int and 0<=x<=2 for x in dims.values()):
            target=3+sum(dims.values())
            ensure(record.get(prefix+'_score')==target,'score_mismatch_'+prefix)
            ensure(0<=target<=11,'score_invalid_max')
    if type(record.get('baseline_score')) is int and type(record.get('candidate_score')) is int:
        ensure(record.get('delta')==record['candidate_score']-record['baseline_score'],'signed_delta_mismatch')
    ensure(record.get('independent_efficacy')=='NOT_ESTABLISHED','false_causal_promotion')
    return problems
frozen=readj(U/'R055_FROZEN_INPUTS.json')
rubric=readj(T/'R056_FROZEN_SCORING.json')
add=readj(T/'R056_PARITY_ADDENDUM.json')
primary=readj(T/'R056_MATCHED_PAIRED_RATINGS.json')
first=readj(T/'R056_PAIRED_RATINGS.json')
ck(rubric['preregistered_before_baselines'] and rubric['max_total']==11 and sum(x['points'] for x in rubric['rubric'])==11,'11pt metric preregistration lost')
ck(add['failed_first_comparison']['invalid_for_causal_V3'] and primary['original_unmatched_comparison']=='INVALID_IMBALANCED_PROMPT','unfair first baseline not quarantined')
ck(first['baseline_written_before_scoring_commit']=='e1ef40c84bd9143ce09533ab501af29977f18c4b','initial biased score provenance lost')
ck(add['parity_baseline']['input_fields_given']==['id','title','input','expected_criteria','expected_output'],'matched baseline was not given identical requirements')
ck(primary['baseline_commit']=='43a51d342f8d94eced48e938a2f013b025db1362' and primary['candidate_commit']=='597b7caa8051db924ba0125e9e0ee4cf37e6c164','unchanged source arm provenance')
ck(primary['scoring_rubric_commit']=='c4d97a582e9b2ec13bad55db3ec00211f9cf9399','rubric was not frozen before output')
cases=frozen['cases'];ids={x['id'] for x in cases}
ck(len(cases)==19 and len(ids)==19 and len(primary['records'])==19,'not exactly 19 independent tasks')
ck(set(x['id'] for x in primary['records'])==ids,'missing or invented scored cases')
ck(len(list((T/'baseline').glob('*.json')))==19,'biased baseline failure examples deleted')
ck(len(list((T/'matched_baseline').glob('*.json')))==19,'matched baseline examples missing')
matched_text_hashes=[]
for tc in cases:
    id=tc['id']
    base=readj(T/'matched_baseline'/(id+'.json'))
    original=readj(T/'baseline'/(id+'.json'))
    candidate=readj(U/'results'/(id+'.json'))
    ck(base['arm']=='MATCHED_REQUIREMENTS_NO_CANDIDATE_METHOD' and base['brief_type']=='FROZEN_STORY_AND_THREE_CRITERIA_NO_METHOD_CARD','not fair baseline arm '+id)
    ck(original['arm']=='BASELINE_NO_CANDIDATE_INSTRUCTIONS','unfair original baseline not preserved '+id)
    ck(candidate['mode']=='PAPER_WALKTHROUGH_SAME_AGENT_VARIANTS','R055 original candidate output mutated '+id)
    for label,arm in [('matched',base),('candidate',candidate)]:
        ck(all(isinstance(arm.get(key),str) and len(arm[key])>=(12 if label=='matched' else 8) for key in ('scene_A','scene_B','state_contract','unknowns')),label+' incomplete output '+id)
        ck(arm['scene_A']!=arm['scene_B'],label+' A/B identical '+id)
        ck('=' in arm['state_contract'],label+' no state tracking '+id)
    r=next((x for x in primary['records'] if x['id']==id),{})
    for x in errorscore(r,base,candidate,tc['expected_criteria']):err.append(id+':'+x)
    matched_text_hashes.append(hashlib.sha256((T/'matched_baseline'/(id+'.json')).read_bytes()).hexdigest())
agg=primary['aggregate'];rr=primary['records']
ck(agg['candidate']==sum(x['candidate_score'] for x in rr) and agg['baseline']==sum(x['baseline_score'] for x in rr),'pair score totals arithmetic drift')
ck(agg['win']==sum(x['delta']>0 for x in rr) and agg['tie']==sum(x['delta']==0 for x in rr) and agg['loss']==sum(x['delta']<0 for x in rr),'W/T/L arithmetic mismatch')
ck((agg['candidate'],agg['baseline'],agg['win'],agg['tie'],agg['loss'])==(201,203,0,17,2),'reported honest no-gain conclusion drift')
ck({x['id'] for x in rr if x['delta']<0}=={'WM-04','WM-09'},'two counterexamples lost')
ck(all(x['independent_efficacy']=='NOT_ESTABLISHED' for x in rr),'candidate independently certified falsely')
v2=readt(U/'R055_CANDIDATE_OUTCOMES.tsv')
v3=readt(T/'R056_CANDIDATE_OUTCOMES.tsv')
ck(len(v2)==len(v3)==187 and {x['candidate_id'] for x in v2}=={x['candidate_id'] for x in v3},'187 candidate status coverage absent')
status={}
for r in v3:
    orig=next((x for x in v2 if x['candidate_id']==r['candidate_id']),{})
    ck(bool(orig),'unknown candidate '+r['candidate_id'])
    if not orig:continue
    expected=('NO_INCREMENTAL_GAIN_DEMONSTRATED_NONBLIND' if orig['V2']=='V2_WALKTHROUGH_PASS_LIMITED' else
              'V2_NOT_TESTED_NO_V3' if orig['V2']=='V1_PASS_V2_NOT_TESTED' else
              'REFERENCE_NO_INDEPENDENT_V3' if orig['V2']=='REFERENCE_ONLY_NOT_EXECUTABLE_METHOD' else
              'BLOCKED_V1_NO_V3')
    ck(r['V3']==expected and r['V1']==orig['V1'] and r['V2']==orig['V2'],'R054/R055 source state changed for '+r['candidate_id'])
    ck(r['book']==orig['book'] and r['linked_actual_task_ids']==orig['actual_input_ids'],'task ID mapping altered for '+r['candidate_id'])
    ck(r['R057_expected_gate']=='R057_USER_CONFIRM_AND_SPECIFIC_SOURCE_REPAIR','R057 user gate skipped')
    status[r['V3']]=status.get(r['V3'],0)+1
ck(status=={'NO_INCREMENTAL_GAIN_DEMONSTRATED_NONBLIND':47,'V2_NOT_TESTED_NO_V3':11,'REFERENCE_NO_INDEPENDENT_V3':90,'BLOCKED_V1_NO_V3':39},'187 V3 disposition totals invalid')
for slug,prefix,count in [('wanming','WM-',9),('tiexuecanming','TX-',10)]:
    report=(R/'books'/slug/'validation/V3_TASK_LIFT.md').read_text(encoding='utf8')
    found=re.findall(r'(?m)^### ('+prefix+r'\d{2})｜',report)
    ck(len(found)==count and set(found)=={x['id'] for x in cases if x['book']==slug},'book report missing scored rows '+slug)
    ck('PROVISIONAL' in report and 'NOT_RUN' in report and '不' in report,'book report overclaims independent utility '+slug)
audit=(R/'books/R056_V3_AUDIT.md').read_text(encoding='utf8')
for token in ['201/209','203/209','47个','11个','90项','39项','168/209','19题','0','17','2','V3','PROVISIONAL','NOT_RUN','WM-04','WM-09','R057','NO_INCREMENTAL']:
    ck(token in audit,'audit lacks '+token)
old=readt(R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(old)==14 and all(r['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for r in old),'14 legacy quality claims incorrectly released')
state=readj(R/'CURRENT_ROUND.json');n=int(state['current_round'][1:])
ck(state['round_status']=='NOT_STARTED' and ((n==56 and state['rounds_completed']==55 and state['last_passed_round']=='R055') or (n>=57 and state['rounds_completed']==n-1 and int(state['last_passed_round'][1:])>=56)),'controller progression invalid')
ck(state['legacy_quality_debt_status']=='OPEN_QUARANTINED' and state['literary_interpretation_status']=='PROVISIONAL' and state['skill_certified_count']==0 and state['heldout_bank_status']=='SEALED_NOT_RUN','quality debt, B, Skill or heldout incorrectly promoted')
ck(state['original_output_test_status']=='NOT_RUN','independent original test C prematurely upgraded')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f: ledger={row['id']:row for row in csv.DictReader(f)}
ck(ledger['R055']['status']=='PASSED' and ledger['R056']['status']==('NOT_STARTED' if n==56 else 'PASSED'),'round R056 ledger status inconsistent')
if n==57:ck(ledger['R057']['status']=='NOT_STARTED','R057 gate triggered without user confirmation')
# Negative mutation controls validate evaluator catches the major forms.
tc=cases[0];r=next(x for x in rr if x['id']==tc['id']);base=readj(T/'matched_baseline'/(tc['id']+'.json'));cand=readj(U/'results'/(tc['id']+'.json'))
def invalid_change(fn):
    item=copy.deepcopy(r);fn(item);return bool(errorscore(item,base,cand,tc['expected_criteria']))
ck(invalid_change(lambda z:z['baseline_three_criteria_evidence'].__setitem__(0,'NO-SUCH-TEXT-EXISTS-13579')),'negative test fake baseline quote not rejected')
ck(invalid_change(lambda z:z['candidate_three_criteria_evidence'].__setitem__(0,'NO-SUCH-CANDIDATE-PROOF')),'negative test fake candidate evidence not rejected')
ck(invalid_change(lambda z:z['baseline_dims'].__setitem__('causal_chain',9)),'negative test impossible dimension not rejected')
ck(invalid_change(lambda z:z.__setitem__('candidate_score',0)),'negative test inflated score consistency not rejected')
ck(invalid_change(lambda z:z.__setitem__('independent_efficacy','VERIFIED')),'negative test unauthorized utility certification not rejected')
print('R056 repeated artifact digest:',hashlib.sha256('|'.join(matched_text_hashes).encode()).hexdigest())
print('R056 intentional corrupted evidence 5/5 checked as failures')
for x in err:print('FAIL:',x)
print('R056', 'FAIL' if err else 'PASS','19 same-input two-arm pairs; 38 unchanged R055 and 38 new matched A/B fiction outputs; unfair first comparator quarantined; matched candidate201 baseline203; 0 wins/17 ties/2 regressions; 187 candidates preserved; NO V3 efficacy certification, Skill0')
sys.exit(bool(err))
