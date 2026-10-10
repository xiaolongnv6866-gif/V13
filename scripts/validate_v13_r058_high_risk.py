#!/usr/bin/env python3
"""R058 structural/provenance regression: source claims and 43 observations, never automatic literary B certification."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def ok(test,msg):
 if not test:raise AssertionError(msg)
def tsv(path):
 with (P/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def js(path):return json.loads((P/path).read_text(encoding="utf-8"))
orig={}
sizes={}
for n in [8,9,10,11,12,13,14,15,17]:
 rn="R%03d"%n
 book="wanming" if n%2 else "tiexue"
 path=P/"cangjie"/"reading"/rn/(book+"_receipts.jsonl")
 rec=[json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
 ok(len(rec)==40,rn+" wrong reading coverage")
 all_claims=[(entry,c) for entry in rec for c in entry["mechanism_claims"]]
 sizes[rn]=len(all_claims)
 for entry,c in all_claims:
  k="STAGE0:"+rn+":"+c["claim_id"]
  ok(k not in orig,k+" duplicate source")
  orig[k]=(entry,c)
ok(sum(sizes.values())==130,"high-risk original 130 source claims")
src=tsv("v2/ISSUE_REGISTRY.tsv")
s34={x["issue_id"] for x in src if x["issue_type"]=="STAGE0_B_CLAIM" and x["assigned_round"]=="R058" and x["audit_sampling"]=="PRESELECTED_FOR_R058_R059"}
ok(len(s34)==34,"R057 originally preregistered high-risk 34 missing")
wm=tsv("v2/stage0/R058_WM_24_DECISIONS.tsv")
tx=tsv("v2/stage0/R058_TX_19_DECISIONS.tsv")
out=wm+tx
ids={x["issue_id"] for x in out}
ok(len(wm)==24 and len(tx)==19 and len(out)==len(ids)==43,"R058 reviewed 43 row identity/count")
ok(s34.issubset(ids),"R057 preregistered item not actually audited")
extra=[x for x in out if x["review_level"]=="SYSTEMIC_EXPANSION"]
ok(len(extra)==9 and {x["source_round"] for x in extra}==set(sizes),"must extend one original source round each")
ok(all(sum(x["source_round"]==rn for x in extra)==1 for rn in sizes),"must be exactly one expansion per source round")
ok({x["issue_id"] for x in extra}==ids-s34,"not all extra IDs declared")
ok(all(x["review_level"]=="R057_FROZEN_SAMPLE" for x in out if x["issue_id"] in s34),"frozen sample flag drift")
for x in out:
 k=x["issue_id"]
 ok(k in orig,k+" not in original receipts")
 entry,c=orig[k]
 ok(x["source_round"] in sizes and entry["book_slug"]==x["book"],k+" book/round drift")
 ok(str(entry["narrative_ordinal"])==str(x["narrative_ordinal"]),k+" narrative ordinal drift")
 oldindex=int(x["original_support_p"])
 ok(oldindex>0 and oldindex<=entry["body_paragraph_count"],k+" old p outside original chapter")
 oldanchors={a["paragraph_index"] for a in entry["anchors"] if a["anchor_id"] in c["support_anchor_ids"]}
 ok(oldindex in oldanchors,k+" old anchor does not match frozen claim")
 ok(x["decision"] and x["observed_in_original_reconstructed"] and x["reason_original_claim_must_be_limited"] and x["counterexample_or_boundary"],k+" missing literary observations")
 for part in x["rechecked_loci"].split(";"):
  match=re.fullmatch(r"(\d+)(?:-(\d+))?",part)
  ok(bool(match),k+" bad actual locus "+part)
  start=int(match.group(1));end=int(match.group(2) or start)
  ok(1<=start<=end<=entry["body_paragraph_count"],k+" source range not in real chapter")
 ok(x["next_gate"].startswith("R06"),k+" must remain in later literary/debt gate")
 ok("PASS" not in x["decision"] and "VERIFIED" not in x["decision"],k+" illicit literary source promotion")
ok(len(orig)-len(out)==87,"87 unreviewed high risk must stay unresolved")
legacy=tsv("gates/R057_LEGACY_QUARANTINE.tsv")
olds={x["legacy_claim_id"] for x in legacy}
overlap=[x for x in out if x["issue_id"].split(":")[-1] in olds]
ok(len(overlap)==7 and all("LEGACY_HOLD" in x["decision"] or "LEGACY_HOLD" in x["next_gate"] for x in overlap),"old R042 quarantines must remain explicit")
ok(all(x["stage1_permission"]=="NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE" for x in legacy),"old quarantine leaked")
alt=tsv("v2/stage0/R058_REBASED_PRIVATE_PARAGRAPH_SHA.tsv")
ok(len(alt)==19 and len({(x["book"],x["narrative_ordinal"],x["rechecked_paragraph_index"]) for x in alt})==19,"19 new source locators")
for x in alt:
 ok(bool(re.fullmatch(r"[0-9a-f]{64}",x["private_epub_verified_paragraph_sha256"])),"bad added SHA field")
 ok(any(y["book"]==x["book"] and y["narrative_ordinal"]==x["narrative_ordinal"] for y in out),"new SHA has no reviewed narrative chapter")
 ok(int(x["rechecked_paragraph_index"])>=1,"bad alt anchor location")
memo=(P/"v2/stage0/HIGH_RISK_SOURCE_AUDIT.md").read_text(encoding="utf-8")
receipt=(P/"runs/R058_V2.md").read_text(encoding="utf-8")
ok("43/130" in memo and "87/130" in memo and "43条" in receipt,"R058 scope must declare residual uncovered")
cur=js("V13_CURRENT_V2.json")
ledger=tsv("V13_LEDGER_V2.csv") if False else None
ok(cur["rounds_total"]==110 and cur["rounds_completed"]>=57,"new runtime plan drift")
if cur["rounds_completed"]==57:
 ok(cur["current_round"]=="R058" and cur["round_status"]=="NOT_STARTED","R058 current/pending mismatch")
elif cur["rounds_completed"]>=58:
 ok(cur["last_passed_round"]>="R058","R058 completed falsely")
if cur["rounds_completed"]<=58:
 ok(cur["skill_certified_count"]==0 and cur["heldout_bank_status"]=="SEALED_NOT_RUN" and cur.get("v3_full47_completed",0)==0,"R058 did not certify creative skills")
print("R058 STRUCTURE PASS: 9 old high risk source rounds, 34 prereg+9 systemic expansion =43/130; 87 remain B provisional, 7 overlaps remain quarantined, 19 rechecked SHA, no fake skill.")
