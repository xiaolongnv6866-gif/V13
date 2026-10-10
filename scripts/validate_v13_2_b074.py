#!/usr/bin/env python3
"""B074 actual original output evidence/structure; NOT a literary validity certificate."""
import csv,json,pathlib,re,subprocess
P=pathlib.Path(__file__).resolve().parents[1]
def gitsha(path):return subprocess.check_output(["git","hash-object",str(path)],cwd=P,text=True).strip()
def table(path):
 with (P/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def han(text):return sum(0x3400<=ord(c)<=0x9fff for c in text)
fr=P/"v2/v3/B074_TX_PREREGISTERED_INPUTS.json"
assert gitsha(fr)=="b44928f5728e771127dacdeefb0ad61a12ad8c28"
assert gitsha(P/"v2/v3/FROZEN_TEST_CONTRACT.json")=="4e24d782632210c1e1637eba4954bde3d8f3846f"
assert gitsha(P/"v2/v3/results/WANMING_ADDITIONAL.tsv")=="4a5801439861faee3afccc005d09b9c24169da3f"
tests=json.loads(fr.read_text("utf-8"))["cases"]
rows=table("v2/v3/results/TIEXUE_ADDITIONAL.tsv")
new=[r for r in rows if r["record_type"]=="ADDITIONAL"]
old=[r for r in rows if r["record_type"]=="QUARANTINED"]
route=table("v2/v3/B074_TX_ELIGIBILITY_ROUTE.tsv")
manifest=table("v2/v3/B074_TX_BLOB_MANIFEST.tsv")
assert len(tests)==len(new)==len(manifest)==12
assert len(old)==7 and len(route)==19
assert len({x["candidate_id"] for x in rows})==19
assert {r["candidate_id"] for r in old}=={r["candidate_id"] for r in route if r["v3_route"]=="INELIGIBLE_NO_NEW_V1_V2"}
assert all(r["eligibility"]=="NOT_ELIGIBLE_NO_REBUILT_V1_V2" and r["V3_outcome"]=="OPEN_QUARANTINED" for r in old)
sum_plus=0
for i,c in enumerate(tests):
 r=new[i]; id=c["candidate_id"];tid=c["id"];p=P/("v2/v3/outputs/B074/"+tid+".json")
 assert r["test_id"]==tid and r["candidate_id"]==id and r["eligibility"]=="ELIGIBLE_SCOPED_DIAGNOSTIC"
 assert r["source_path"]==c["epub_path"] and int(r["paragraph_no"])==int(c["paragraph"])
 assert r["paragraph_SHA256"]==c["original_paragraph_sha256"]
 o=json.loads(p.read_text("utf-8"))
 assert o["candidate_id"]==id and o["case_id"]==tid and o["frozen_contract_blob"]==gitsha(fr)
 assert o["baseline"]["method_card"]=="NONE"
 assert o["method"]["method_card"]=="ONE_NARROW_PREREGISTERED_CARD"
 assert o["baseline"]["scene_one"]==o["method"]["scene_one"]
 for arm,col in [("baseline","baseline_han"),("method","method_han")]:
  a=o[arm]; count=han(a["scene_one"]+a["scene_two"])
  assert 500<=count<=750 and count==a["han_characters"]==int(r[col]),(id,arm,count)
  assert len(a["state_ledger"])>=5 and all(x["fact"] for x in a["state_ledger"])
  assert a["unknowns"] and a["failure_risk_note"]
 b=o["rating"]["baseline_scores"];m=o["rating"]["method_scores"]
 assert len(b)==len(m)==5 and all(isinstance(v,int) and 0<=v<=2 for v in b+m)
 delta=sum(m)-sum(b)
 assert delta==o["rating"]["delta"]==int(r["delta"])
 assert sum(b)==int(r["baseline_total"]) and sum(m)==int(r["method_total"])
 assert delta<2 and r["V3_outcome"]=="DIAGNOSTIC_ONLY_NOT_VERIFIED"
 assert r["independent_judge"]=="NOT_ESTABLISHED" and o["rating"]["independent_judge"]=="NOT_ESTABLISHED"
 assert manifest[i]["path"]==str(p.relative_to(P)) and gitsha(p)==manifest[i]["git_blob_sha1"]
 assert route[i]["candidate_id"]==id and route[i]["independent_verified"]=="NO"
 sum_plus+=int(delta==1)
assert sum_plus==3 and sum(int(r["delta"])==0 for r in new)==9
state=json.loads((P/"V13_CURRENT_V3.json").read_text("utf-8"))
assert state["v3_original_47_completed"]==47 and state["skill_certified_count"]==0
assert int(state["current_batch"][1:])>=74
print("B074 PASS 12/12 paired original diagnostics, 24 arms, 7 historical quarantine; verified=0")
