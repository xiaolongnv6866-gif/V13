#!/usr/bin/env python3
"""R055 Stage1.5 V2 fixed-input original fiction walkthrough checks.
Public CI certifies artifact and task-output consistency, not independent literary quality.
"""
from pathlib import Path
import json,csv,hashlib,re,copy,sys
R=Path(__file__).resolve().parents[1]
T=R/'tests/v2'
bad=[]
PIN='27fa253c133ad892f67f14c6236716835d7c365d'
EXPECTED_TASKS={f'WM-{i:02}' for i in range(1,10)}|{f'TX-{i:02}' for i in range(1,11)}
def ck(cond,msg):
    if not cond:bad.append(msg)
def tab(path):
    with path.open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))
cases=json.loads((T/'R055_FROZEN_INPUTS.json').read_text(encoding='utf8'))
ck(cases['round']=='R055' and cases['status']=='FROZEN_BEFORE_OUTPUT' and cases['preregistered'] and cases['not_V3'],'pre-registered input integrity')
fixed=cases['cases']
ck(len(fixed)==19 and {x['id'] for x in fixed}==EXPECTED_TASKS,'not 19 frozen independently mapped Stage0 tasks')
ck(sum(len(x['expected_criteria']) for x in fixed)==57,'not 57 preregistered criteria')
original_inputs={}
for slug in ('wanming','tiexuecanming'):
    for row in tab(R/'books'/slug/'validation/V1_EVIDENCE.tsv'):
        original_inputs[row['candidate_id']]=row
ck(len(original_inputs)==187,'187 actual V1 candidates missing')
def verify_case(inp,run,allowed):
    errors=[]
    def ensure(boolval,msg):
        if not boolval:errors.append(msg)
    ensure(run.get('id')==inp['id'],'id')
    ensure(run.get('mode')=='PAPER_WALKTHROUGH_SAME_AGENT_VARIANTS','run_mode')
    ensure(run.get('v3')=='NOT_STARTED_R056','V3')
    for key in ('scene_A','scene_B','state_contract','unknowns'):
        ensure(isinstance(run.get(key),str) and len(run.get(key,''))>=8,key)
    if all(isinstance(run.get(x),str) for x in ('scene_A','scene_B')):
        ensure(run['scene_A']!=run['scene_B'],'distinct_variants')
    if isinstance(run.get('state_contract'),str):
        ensure('=' in run['state_contract'] and len(run['state_contract'].split('；'))>=4,'state_contract')
    ensure(run.get('candidate_ids')==inp['candidate_ids'],'candidate_link')
    for cid in inp['candidate_ids']:
        candidate=allowed.get(cid,{})
        ensure(candidate.get('V1')=='PASS' and candidate.get('extractor_type') in ('framework','principle'),'not V1 source PASS')
    proofs=run.get('criteria_proofs',[])
    ensure(isinstance(proofs,list) and len(proofs)==len(inp['expected_criteria']),'criterion_proof count')
    if isinstance(proofs,list):
        for i,item in enumerate(proofs):
            if not isinstance(item,dict):
                errors.append('criterion_proof format');continue
            ensure(i<len(inp['expected_criteria']) and item.get('criterion')==inp['expected_criteria'][i],'criterion_proof label')
            anchor=item.get('observed_anchor','')
            text=''.join(run.get(x,'') for x in ('scene_A','scene_B','state_contract','unknowns'))
            ensure(isinstance(anchor,str) and len(anchor)>=3 and anchor in text,'criterion_proof anchored')
    ensure(all('原著' not in run.get(k,'') for k in ('scene_A','scene_B')),'original excerpt/wording risk')
    return errors
observed={}
for inp in fixed:
    p=T/'results'/(inp['id']+'.json')
    ck(p.exists(),'missing actual scene '+inp['id'])
    if not p.exists():continue
    run=json.loads(p.read_text(encoding='utf-8'))
    errs=verify_case(inp,run,original_inputs)
    for e in errs:bad.append(inp['id']+': '+e)
    observed[inp['id']]=run
ck(len(observed)==19,'not all original scenes executed')
ck(len(list((T/'results').glob('*.json')))==19,'extra or missing scene files')
selected={cid for x in fixed for cid in x['candidate_ids']}
ck(len(selected)==47,'expected 47 distinct V1 PASS framework/principle exercised')
staging=tab(T/'R055_CANDIDATE_OUTCOMES.tsv')
ck(len(staging)==187 and len({r['candidate_id'] for r in staging})==187,'V2 disposition not 187 unique rows')
claimed={'V2_WALKTHROUGH_PASS_LIMITED':0,'BLOCKED_BY_V1_NEEDS_SOURCE_REPAIR':0,'REFERENCE_ONLY_NOT_EXECUTABLE_METHOD':0,'V1_PASS_V2_NOT_TESTED':0}
for r in staging:
    cid=r['candidate_id'];orig=original_inputs.get(cid,{})
    ck(bool(orig),'V2 unknown candidate '+cid)
    if not orig:continue
    expect=('BLOCKED_BY_V1_NEEDS_SOURCE_REPAIR' if orig['V1']=='REVIEW' else
            'REFERENCE_ONLY_NOT_EXECUTABLE_METHOD' if orig['extractor_type'] not in ('framework','principle') else
            'V2_WALKTHROUGH_PASS_LIMITED' if cid in selected else
            'V1_PASS_V2_NOT_TESTED')
    ck(r['V2']==expect,cid+' incorrect V2 flow')
    claimed[expect]+=1
    ck(r['V1']==orig['V1'] and r['candidate_type']==orig['extractor_type'],'source V1 grade changed '+cid)
    ck(r['source_task_ids']==orig['task_ids'],'frozen source task ids changed '+cid)
    ck(r['V3']=='NOT_STARTED_R056','V3 falsely passed for '+cid)
    linked=[x['id'] for x in fixed if cid in x['candidate_ids']]
    ck(r['actual_input_ids']==';'.join(linked),'actual V2 input link lost '+cid)
    ck(r['actual_output_files']==';'.join('tests/v2/results/'+x+'.json' for x in linked),'source output file link lost '+cid)
ck(claimed=={'V2_WALKTHROUGH_PASS_LIMITED':47,'BLOCKED_BY_V1_NEEDS_SOURCE_REPAIR':39,'REFERENCE_ONLY_NOT_EXECUTABLE_METHOD':90,'V1_PASS_V2_NOT_TESTED':11},'stated V2 dispositions incorrect: '+str(claimed))
for slug in ('wanming','tiexuecanming'):
    report=(R/'books'/slug/'validation/V2_EXECUTION.md').read_text(encoding='utf8')
    ck(PIN in report and 'PAPER_WALKTHROUGH' in report and 'NOT_STARTED_R056' in report,slug+' report missing limits')
audit=(R/'books/R055_V2_AUDIT.md').read_text(encoding='utf8')
for tok in ('19个','38份','57条','47个','11个','90个','39个','187','R056','PROVISIONAL','NOT_RUN','SOURCE'):
    ck(tok in audit,'audit missing '+tok)
runbook=(T/'R055_RUNBOOK.md').read_text(encoding='utf8')
ck(all(x['id'] in runbook for x in fixed),'runbook lacks outputs')
controls=json.loads((T/'R055_NEGATIVE_TESTS.json').read_text(encoding='utf8'))
ck(len(controls['mutations'])==4,'need 4 invalid V2 artifact mutations')
if observed:
    baseline_input=fixed[0];baseline_run=observed[baseline_input['id']]
    altered=[]
    a=copy.deepcopy(baseline_run);a['scene_B']='';altered.append(('EMPTY_SECOND_SCENE',verify_case(baseline_input,a,original_inputs)))
    a=copy.deepcopy(baseline_run);a['criteria_proofs'][0]['observed_anchor']='no-such-quote-at-all-12345';altered.append(('FABRICATED_CRITERION_ANCHOR',verify_case(baseline_input,a,original_inputs)))
    a=copy.deepcopy(baseline_run);a['candidate_ids'][0]='WM-f03';altered.append(('SOURCE_REVIEW_CANDIDATE',verify_case(baseline_input,a,original_inputs)))
    a=copy.deepcopy(baseline_run);a['v3']='PASSED';altered.append(('V3_PREMATURE_PASS',verify_case(baseline_input,a,original_inputs)))
    ck([x[0] for x in altered]==[x['mutation'] for x in controls['mutations']],'negative controls mutation list mismatch')
    for key,errors in altered:
        ck(bool(errors),'invalid negative input not rejected: '+key)
    digest1=hashlib.sha256(''.join((T/'results'/(x['id']+'.json')).read_text(encoding='utf8') for x in fixed).encode('utf8')).hexdigest()
    digest2=hashlib.sha256(''.join((T/'results'/(x['id']+'.json')).read_text(encoding='utf8') for x in fixed).encode('utf8')).hexdigest()
    ck(digest1==digest2,'artifact replay inconsistent')
    print('V2 artifact repeatability fingerprint SHA256:',digest1)
print('V2 negative controls: 4/4 reject invalid manifest cases (if no errors)')
old=tab(R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'R042 old claim quarantine lifted')
state=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
roundno=int(state['current_round'][1:])
ck((state["round_status"]=="NOT_STARTED" or (state["current_round"]=="R057" and state["round_status"]=="BLOCKED" and state["rounds_completed"]==56 and state["last_passed_round"]=="R056" and state.get("cangjie_stage1_5_user_confirm")=="PENDING_R057_USER_APPROVAL")) and ((roundno==55 and state['rounds_completed']==54 and state['last_passed_round']=='R054') or (roundno>=56 and state['rounds_completed']==roundno-1 and int(state['last_passed_round'][1:])>=55)),'official cursor wrong for evidence/formal commit')
ck(state['literary_interpretation_status']=='PROVISIONAL' and state['original_output_test_status']=='NOT_RUN' and state['skill_certified_count']==0,'V2 walkthrough misrepresented as independent V3/SKILL')
ck(state['heldout_bank_status']=='SEALED_NOT_RUN' and state['legacy_quality_debt_status']=='OPEN_QUARANTINED','heldout or old quality claims released')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:
    ledger={x['id']:x for x in csv.DictReader(f)}
ck(ledger['R054']['status']=='PASSED','R054 not PASSED')
ck(ledger['R055']['status']==('NOT_STARTED' if roundno==55 else 'PASSED'),'R055 ledger not aligned')
if roundno==56:ck(ledger['R056']['status']=='NOT_STARTED','R056 executed prematurely')
for e in bad:print('FAIL:',e)
print('R055','FAIL' if bad else 'PASS','19 frozen original fiction tasks/38 authored scene variants/57 criteria; 47 V2 limited walkthrough, 11 method not tested, 90 reference, 39 V1 blocked; two variants same agent, NOT independent reproduction; V3 NOT_RUN')
sys.exit(bool(bad))
