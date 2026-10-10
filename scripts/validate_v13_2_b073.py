#!/usr/bin/env python3
import csv,json,pathlib,subprocess
R=pathlib.Path(__file__).resolve().parents[1]
def sha(p):return subprocess.check_output(['git','hash-object',str(p)],cwd=R,text=True).strip()
def han(s):return sum(0x3400<=ord(c)<=0x9fff for c in s)
f=R/'v2/v3/B073_WM_PREREGISTERED_INPUTS.json'
assert sha(f)=='a62d1ade7017fca01e405edbcb93368489c9122f'
assert sha(R/'v2/v3/FROZEN_TEST_CONTRACT.json')=='4e24d782632210c1e1637eba4954bde3d8f3846f'
tests=json.loads(f.read_text('utf-8'))['cases']
def tab(p):
 with (R/p).open('r',encoding='utf-8',newline='') as h:return list(csv.DictReader(h,delimiter='\t'))
rows=tab('v2/v3/results/WANMING_ADDITIONAL.tsv')
new=[r for r in rows if r['record_type']=='NEW'];rollback=[r for r in rows if r['record_type']=='ROLLBACK']
assert len(tests)==len(new)==10 and {r['test_id'] for r in rollback}=={'WM-04','WM-09'}
route=tab('v2/v3/B073_WM_ELIGIBILITY_ROUTE.tsv');manifest=tab('v2/v3/B073_WM_BLOB_MANIFEST.tsv')
assert len(route)==len(manifest)==10
for i,t in enumerate(tests):
 id=t['test_id'];r=new[i];path=R/('v2/v3/outputs/B073/'+id+'.json')
 obj=json.loads(path.read_text('utf-8'))
 assert obj['candidate_id']==t['candidate_id']==r['candidate_id']
 assert obj['test_id']==id==r['test_id'] and obj['frozen_blob']==sha(f)
 assert obj['baseline']['method_card']=='NONE' and obj['method']['method_card']=='ONLY_FROZEN_NARROW_CARD'
 assert obj['baseline']['scene_1']==obj['method']['scene_1']
 for arm,key in [('baseline','baseline_han'),('method','method_han')]:
  a=obj[arm];n=han(a['scene_1']+a['scene_2'])
  assert 500<=n<=750 and n==a['han_characters']==int(r[key]),(id,arm,n)
 assert len(obj['state_ledger'])>=5 and obj['negative_control_failure']
 b=obj['ratings']['baseline'];m=obj['ratings']['method']
 assert len(b)==len(m)==5 and all(isinstance(v,int) and 0<=v<=2 for v in b+m)
 assert sum(m)-sum(b)==obj['ratings']['delta']==int(r['delta'])
 assert sum(b)==int(r['baseline_rating']) and sum(m)==int(r['method_rating'])
 assert int(r['delta'])<2 and r['v3_outcome']=='DIAGNOSTIC_NONBLIND_NO_VERIFIED'
 assert manifest[i]['path']==str(path.relative_to(R)) and manifest[i]['git_blob_sha1']==sha(path)
 assert route[i]['candidate_id']==t['candidate_id'] and route[i]['independent_verified']=='NO'
assert [int(r['delta']) for r in new].count(1)==4
assert all(r['eligibility']=='NO_NEW_REPAIR' for r in rollback)
print('B073 structural audit PASS: ten paired 500-750 Chinese-char outputs; diagnostic only')
