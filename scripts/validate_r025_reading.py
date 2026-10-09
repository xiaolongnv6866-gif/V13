#!/usr/bin/env python3
"""R025 public SOURCE_STRUCTURE_ONLY. Non-copyright metadata and literary provenance integrity only."""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf-8"))
with (root/"sources/metadata/wanming_v13_spine.csv").open(encoding="utf-8",newline="") as f:
    master={int(r["narrative_ordinal"]):r for r in csv.DictReader(f) if r["narrative_ordinal"]}
with (root/"cangjie/reading/R025/wanming_source_index.csv").open(encoding="utf-8",newline="") as f: source=list(csv.DictReader(f))
receipts=[json.loads(s) for s in (root/"cangjie/reading/R025/wanming_receipts.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
original_map=[json.loads(s) for s in (root/"cangjie/reading/R025/wm_chapter_observations.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
studies=[json.loads(s) for s in (root/"cangjie/reading/R025/close_studies.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
anchor_map=json.loads((root/"cangjie/reading/R025/wanming_private_locator_hashes.json").read_text(encoding="utf-8"))["anchors"]
errors=[]
def ck(test,message):
    if not test:errors.append(message)
def fnv(h,s):
    for ch in s:h=((h^ord(ch))*16777619)&0xffffffff
    return h
ck(len(receipts)==len(source)==len(original_map)==40,"R025 requires 40 source index and unique independent receipts")
ck([r["narrative_ordinal"] for r in receipts]==list(range(361,401)),"missing/out-of-order narrative ordinals")
ck([int(x["narrative_ordinal"]) for x in source]==list(range(361,401)),"source index order")
ck(len(studies)==20,"20 separate high-quality close studies")
close={s["n"] for s in studies}
ck(len(close)==20 and 361 in close and 400 in close and 381 in close,"fixed first/mid/last + extra independent review")
ck(len(set(s["failure_boundary"] for s in studies))==20,"repeated weak generic boundaries")
ck(len(set(s["alternative_rendering_loss"] for s in studies))==20,"repeated generic alternate prose")
ck(len(set(s["counter_search"] for s in studies))==20,"repeated counterexample notes")
ck(len(set(s["aspect"] for s in studies))>=7,"missing independent narrative study dimensions")
count=0;anchor_count=0;member_hash=2166136261;locator_hash=2166136261
for r,s,note in zip(receipts,source,original_map):
    n=r["narrative_ordinal"];m=master[n];idx=int(m["spine_index"]);path=m["epub_path"];hash=m["chapter_sha256"];ps=int(m["nonempty_paragraphs"])
    ck(r["book_slug"]=="wanming" and r["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082",f"{n}: wrong book")
    ck(r["spine_index"]==int(s["spine_index"])==idx==n+15,f"{n}: spine mismatch")
    ck(r["epub_path"]==s["epub_path"]==path==f"OEBPS/Text/Chapter_{n+12:04d}.xhtml",f"{n}: path mismatch")
    ck(r["chapter_sha256"]==s["chapter_sha256"]==hash,f"{n}: chapter sha mismatch")
    ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(s["nonempty_paragraphs"])==ps,f"{n}: wrong paragraphs")
    ck(r["mode"]==s["mode"]==("CLOSE_READ" if n in close else "FULL_TEXT_READ"),f"{n}: mode mismatch")
    ck(r["fixture_only"] is False and r.get("round_id")=="R025" and len(r.get("reader_session_id",""))>15,f"{n}: provenance missing")
    ck(note["ordinal"]==n and r["event_chain"]==note["event_chain"] and len(set(r["event_chain"]))==2,f"{n}: missing independent event notes")
    ck(bool(r["open_questions"]) and all(len(x)>16 for x in r["open_questions"]),f"{n}: missing specific unresolved question")
    a=r["anchors"];expected=anchor_map[str(n)]
    ck(len(a)==(len(expected)) and (len(a)>1 if n in close else len(a)==1),f"{n}: anchor count mismatch")
    ck(all(str(z["paragraph_index"]) in expected and z["paragraph_sha256"]==expected.get(str(z["paragraph_index"])) and re.fullmatch(r"[0-9a-f]{64}",z["paragraph_sha256"]) for z in a),f"{n}: bad anchors")
    ck(";".join(str(z["paragraph_index"])+":"+z["paragraph_sha256"] for z in a)==s["paragraph_sha256_anchors"],f"{n}: private locator disagreement")
    ck(len(r["mechanism_claims"])==(1 if n in close else 0),f"{n}: wrong close claims")
    if n in close:
        st=next(x for x in studies if x["n"]==n);cl=r["mechanism_claims"][0]
        ck(cl["claim_text"]==st["claim"] and cl["aspect"]==st["aspect"],f"{n}: close claim diverged")
        ck(cl["support_anchor_ids"]==["p"+str(j) for j in st["support"]],f"{n}: support does not match studied original scene")
        ck(cl["verification_state"]=="PROVISIONAL" and cl["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"{n}: unearned verification")
        ck(len(cl["failure_boundary"])>35 and len(cl["alternative_rendering_loss"])>35 and len(cl["counterexample_search_note"])>35,f"{n}: shallow criticism")
    member_hash=fnv(member_hash,f"{n}|{idx}|{path}|{hash}|{ps}\n")
    for z in a:locator_hash=fnv(locator_hash,f"{n}/{z['paragraph_index']}/{z['paragraph_sha256']}\n")
    count+=ps;anchor_count+=len(a)
ck(count==2099 and anchor_count==99,"corpus 2099 paragraphs and 99 original locators required")
ck(f"{member_hash:08x}"=="6c6bbbf5","member FNV mismatch")
ck(f"{locator_hash:08x}"=="f7ac26dc","paragraph SHA FNV mismatch")
for p in ["cangjie/reading/wanming_361_400.md","cangjie/reading/R025/wanming_continuity.md","cangjie/reading/R025/LOCAL_SOURCE_VERIFICATION.md","runs/R025.md"]:
    ck((root/p).is_file(),"missing "+p)
cur=int(rows["current_round"][1:]);ck(cur>=25,"R025 not yet authorized")
if cur==25:
    ck(rows["full_text_read_chapters"]=={"wanming":360,"tiexuecanming":360},"premature PASS count")
else:
    ck(rows["full_text_read_chapters"]["wanming"]>=400 and rows["full_text_read_chapters"]["tiexuecanming"]>=360,"regressed official full reading counts")
for e in errors:print("FAIL:",e)
if errors:sys.exit(1)
print("PASS R025 PUBLIC SOURCE_STRUCTURE_ONLY: 40 distinct original Wanming ordinals 361-400, 2099 paragraphs, 20 CLOSE_READ, 99 exact paragraph SHA, member FNV 6c6bbbf5, locator FNV f7ac26dc; literary B PROVISIONAL and independent C NOT_RUN")
