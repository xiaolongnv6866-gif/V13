#!/usr/bin/env python3
"""R053: merged Stage1 RAW 2-book source/coverage consistency, not literary V1/V2/V3."""
from pathlib import Path
import csv,json,re,sys
R=Path(__file__).resolve().parents[1]
err=[]
def ck(cond,msg):
    if not cond:err.append(msg)
def tsv(path):
    with path.open(encoding="utf8",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))
TYPES=[
    ("framework","frameworks.md","FRAMEWORK_EVIDENCE.tsv","f"),
    ("principle","principles.md","PRINCIPLE_EVIDENCE.tsv","p"),
    ("case","cases.md","CASE_EVIDENCE.tsv","c"),
    ("counter-example","counter-examples.md","COUNTEREXAMPLE_EVIDENCE.tsv","ce"),
    ("term","glossary.md","GLOSSARY_EVIDENCE.tsv","g")
]
BOOKS={"wanming":{"prefix":"WM","count":91,"each":[17,23,14,19,18],"tasks":9,"positions":145,"overlaps":154,"chapters":571},
       "tiexuecanming":{"prefix":"TX","count":96,"each":[17,22,16,21,20],"tasks":10,"positions":177,"overlaps":130,"chapters":532}}
def extract(path,pfx):
    raw=path.read_text(encoding="utf8")
    matches=[m for m in re.finditer(r"(?m)^- id: ((?:ce|f|p|c|g)\d{2})$",raw) if m.group(1).startswith(pfx)]
    out=[]
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else raw.find("\n\`\`\`",m.start())
        if end<0:end=len(raw)
        block=raw[m.start():end]
        title=re.search(r'(?m)^  (?:title|term): (.+)$',block)
        task=re.search(r"(?m)^  task_ids: \[([^\]]+)\]",block)
        source=re.search(r'(?m)^  source_loci:\n((?:    - "n\d{3}/p\d+"\n?)+)',block)
        tp=re.search(r"(?m)^  type: (.+)$",block)
        ck(title is not None and task is not None and source is not None and tp is not None,"missing source fields "+str(path)+" "+m.group(1))
        if not (title and task and source and tp):continue
        title=title.group(1).strip().strip('"')
        tasks=[x.strip() for x in task.group(1).split(",")]
        locs=re.findall(r'n\d{3}/p\d+',source.group(1))
        ck(bool(locs) and bool(tasks),"missing locator/task "+m.group(1))
        ck('source_quote: ""' in block,"copyright source quote leaked or schema missing "+m.group(1))
        ck('NOT_STARTED_STAGE1_5' in block or 'STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN' in block,"candidate falsely promoted "+m.group(1))
        out.append({"id":m.group(1),"title":title,"tasks":set(tasks),"locs":set(locs),"type":tp.group(1).strip()})
    return out
counts={};books_data={}
for slug,config in BOOKS.items():
    base=R/"books"/slug
    prefix=config["prefix"];nexpected=config["count"]
    with (R/"sources/metadata"/(slug+"_v13_spine.csv")).open(encoding="utf8",newline="") as f:
        metadata={int(z["narrative_ordinal"]):z for z in csv.DictReader(f) if z["is_narrative_chapter"]=="1"}
    ck(len(metadata)==config["chapters"],slug+" OPF narrative spine drift")
    parsed={}; allpos={}; bykind={}
    for (i,(kind,file,ev,pfx)) in enumerate(TYPES):
        candidates=extract(base/"candidates"/file,pfx)
        ck(len(candidates)==config["each"][i],slug+" "+kind+" count")
        bykind[kind]=[x["id"] for x in candidates]
        for x in candidates:
            ck(x["id"] not in parsed,slug+" duplicate candidate ID")
            parsed[x["id"]]=dict(x,kind=kind,file=file,ev=ev)
        for evrow in tsv(base/"candidates"/ev):
            try:
                locus=evrow["source_locus"];n,p=map(int,re.fullmatch(r"n(\d{3})/p(\d+)",locus).groups())
                m=metadata[n];sha=evrow["paragraph_sha256"]
                ck(evrow["epub_path"]==m["epub_path"] and evrow["chapter_sha256"]==m["chapter_sha256"],slug+" source member ref mismatch "+locus)
                ck(1<=p<=int(m["nonempty_paragraphs"]),slug+" source paragraph range "+locus)
                ck(bool(re.fullmatch(r"[a-f0-9]{64}",sha)),slug+" source original p hash bad "+locus)
                old=allpos.get(locus)
                ck(old is None or old==sha,slug+" contradictory source SHA same paragraph "+locus)
                allpos[locus]=sha
            except Exception as ex:
                err.append(slug+" corrupted original evidence "+str(ex))
    ck(len(parsed)==nexpected,slug+" input 5 extractor completeness")
    ck(len(allpos)>=config["positions"],slug+" source positions suspiciously missing")
    for id,cand in parsed.items():
        ck(cand["locs"]<=set(allpos),slug+" missing real origin evidence "+id)
        ck(cand["tasks"] and all(re.fullmatch(prefix+r"-(?:0[1-9]"+("|10" if prefix=="TX" else "")+r")",x) for x in cand["tasks"]),slug+" unknown Stage0 task on "+id)
    matrix=tsv(base/"R053_CANDIDATE_MATRIX.tsv")
    ck(len(matrix)==nexpected,slug+" incomplete merged candidate matrix")
    ids=set()
    for row in matrix:
        id=row["original_id"];ids.add(id);c=parsed.get(id)
        ck(row["book"]==slug and row["candidate_id"]==prefix+"-"+id,slug+" candidate stable key invalid "+id)
        if c:
            ck(row["title"]==c["title"] and row["extractor_type"]==c["kind"],slug+" title/type not preserved "+id)
            ck(set(row["task_ids"].split(","))==c["tasks"],slug+" Stage0 map modified "+id)
            ck(set(row["original_source_loci"].split(";"))==c["locs"],slug+" actual original source coords modified "+id)
            ck(row["candidate_source_file"]==str(Path("books")/slug/"candidates"/c["file"]),slug+" original file lost "+id)
            ck(row["input_evidence_file"]==str(Path("books")/slug/"candidates"/c["ev"]),slug+" evidence provenance lost "+id)
        ck(row["merge_status"]=="RETAIN_RAW_PENDING_DEDUP_REVIEW",slug+" unauthorized destructive dedup "+id)
        for gate in ("V1","V2","V3"):
            ck(row[gate]=="NOT_STARTED",slug+" "+gate+" falsely passed "+id)
    ck(ids==set(parsed),slug+" merged matrix missing/unknown candidates")
    pairs={}
    raw=list(parsed.values())
    for i,a in enumerate(raw):
        for b in raw[i+1:]:
            both=a["locs"]&b["locs"]
            if both:pairs[frozenset((a["id"],b["id"]))]=both
    ck(len(pairs)==config["overlaps"],slug+" source overlap expected count changed")
    recorded=tsv(base/"R053_SOURCE_OVERLAPS.tsv")
    ck(len(recorded)==len(pairs),slug+" overlap pair ledger incomplete")
    pairseen=set()
    for row in recorded:
        a=row["candidate_A"];b=row["candidate_B"]
        ck(a.startswith(prefix+"-") and b.startswith(prefix+"-"),slug+" wrong book shared-source IDs")
        p=frozenset((a[len(prefix)+1:],b[len(prefix)+1:]))
        pairseen.add(p)
        ck(p in pairs,slug+" invented shared original source positions "+str(p))
        if p in pairs:
            ck(set(row["shared_original_loci"].split(";"))==pairs[p],slug+" incorrect overlap source position "+str(p))
        ck(row["dedup_decision"]=="RETAIN_BOTH_UNTIL_V1_AND_SEMANTIC_ADJUDICATION",slug+" premature dedup")
    ck(pairseen==set(pairs),slug+" dropped source overlaps")
    index=(base/"CANDIDATES_INDEX.md").read_text(encoding="utf8")
    indexids=re.findall(r"(?m)^\|"+prefix+r"-((?:ce|f|p|c|g)\d{2})\|",index)
    ck(len(indexids)==nexpected and set(indexids)==set(parsed),slug+" full readable index mismatch")
    coverage=(base/"TASK_COVERAGE_DRAFT.md").read_text(encoding="utf8")
    taskrows={m.group(1):m.group(0) for m in re.finditer(r"(?m)^\|("+prefix+r"-(?:0[1-9]"+("|10" if prefix=="TX" else "")+r"))\|.*$",coverage)}
    ck(len(taskrows)==config["tasks"],slug+" Stage0 tasks lost")
    for j in range(1,config["tasks"]+1):
        task=prefix+f"-{j:02}";x=taskrows.get(task)
        ck(x is not None,slug+" no task audit "+task)
        if not x:continue
        parts=x.split("|")
        expect={kind:[prefix+"-"+v["id"] for v in parsed.values() if v["kind"]==kind and task in v["tasks"]] for kind,_,_,_ in TYPES}
        ck(all(expect[kind] for kind in expect),slug+" task not mapped in all five extractors "+task)
        for ix,(kind,_,_,_) in enumerate(TYPES):
            actual=set(re.findall(r"\b"+prefix+r"-(?:ce|f|p|c|g)\d{2}\b",parts[3+ix]))
            ck(actual==set(expect[kind]),slug+" draft task omissions "+task+" "+kind)
        num=sum(len(v) for v in expect.values())
        ck(parts[8]==str(num),slug+" wrong task raw count "+task)
        ck("RAW_MAPPED_V1_REVIEW_PENDING" in x,slug+" false verification "+task)
    books_data[slug]=parsed;counts[slug]=len(parsed)
cross=tsv(R/"books/R053_CROSS_BOOK_LINKS.tsv")
ck(len(cross)==23,"23 curated crossbook comparisons expected")
for row in cross:
    w=row["WM_candidate_id"];t=row["TX_candidate_id"]
    ck(w.startswith("WM-") and w[3:] in books_data["wanming"],"crossbook WM ID invalid "+w)
    ck(t.startswith("TX-") and t[3:] in books_data["tiexuecanming"],"crossbook TX ID invalid "+t)
    ck(row["relation_status"] in ("ANALOGOUS_THEME_DISTINCT_CAUSAL_STRUCTURE","ANALOGOUS_AUTHORITY_NOT_DUPLICATE","ANALOGOUS_RESOURCE_TIMELINE","ANALOGOUS_ORGANIZATION_FEEDBACK","ANALOGOUS_INFORMATION_ASYMMETRY","ANALOGOUS_OTHERS_AS_AGENTS","ANALOGOUS_POST_EVENT_RESPONSIBILITY","ANALOGOUS_RULE_VS_CONSENT","ANALOGOUS_REFORM_SCOPE","RELATED_DISTINCT_NARRATIVE_FUNCTION","ANALOGOUS_PERSONAL_AUTONOMY","ANALOGOUS_OPEN_OBLIGATION","RELATED_SOURCE_ACCOUNTING_NOT_FORMULA","RELATED_STATE_TRANSITIONS","RELATED_RECORD_VS_RECOLLECTION","ANALOGOUS_FAMILY_CHOICE_DISTINCT_EVENT","ANALOGOUS_RESOURCE_DEPENDENCE","ANALOGOUS_POWER_IMBALANCE","ANALOGOUS_BUDGET_NOT_IDENTICAL","ANALOGOUS_INSTITUTION_UNTESTED","SHARED_TERM_DIFFERENT_IN_STORY_CONTEXT"),"unreviewed relation type")
    ck(row["V1_recheck"]=="NOT_STARTED" and len(row["reason_for_not_destructive_merging"])>12,"crossbook false verification/empty differentiation")
report=(R/"books/R053_MERGE_AUDIT.md").read_text(encoding="utf8")
for txt in ("187","91","96","154","130","23","WM-09","TX-10","R054","R055","R056","R057","SOURCE_STRUCTURE_ONLY","PROVISIONAL","NOT_RUN"):
    ck(txt in report,"no audit of "+txt)
with (R/"cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv").open(encoding="utf8",newline="") as f:
    old=list(csv.DictReader(f,delimiter="\t"))
ck(len(old)==14 and all(x["stage1_permission"]=="NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE" for x in old),"historical debt quarantine lifted")
c=json.loads((R/"CURRENT_ROUND.json").read_text(encoding="utf8"))
n=int(c["current_round"][1:])
ck((c["round_status"]=="NOT_STARTED" or (c["current_round"]=="R057" and c["round_status"]=="BLOCKED" and c["rounds_completed"]==56 and c["last_passed_round"]=="R056" and c.get("cangjie_stage1_5_user_confirm")=="PENDING_R057_USER_APPROVAL")) and ((n==53 and c["rounds_completed"]==52 and c["last_passed_round"]=="R052") or (n>=54 and c["rounds_completed"]==n-1 and int(c["last_passed_round"][1:])>=53)),"official cursor inconsistent")
ck(c["legacy_quality_debt_status"]=="OPEN_QUARANTINED" and c["literary_interpretation_status"]=="PROVISIONAL" and c["original_output_test_status"]=="NOT_RUN","ABC claims inappropriately upgraded")
ck(c["skill_certified_count"]==0 and c["heldout_bank_status"]=="SEALED_NOT_RUN","skill/heldout incorrectly promoted")
with (R/"ROUND_LEDGER.csv").open(encoding="utf8",newline="") as f:ledger={r["id"]:r for r in csv.DictReader(f)}
ck(ledger["R052"]["status"]=="PASSED","R052 preceding gate lost")
ck(ledger["R053"]["status"]==("NOT_STARTED" if n==53 else "PASSED"),"R053 not aligned with stage gate")
if n==54:ck(ledger["R054"]["status"]=="NOT_STARTED","R054 started in R053 turn")
for e in err:print("FAIL:",e)
print("R053","FAIL" if err else "PASS","187 RAW preserved; 91 WM/96 TX; 284 exact shared-source pairs; 23 cross-book analogies; all 19 independent task mappings; SOURCE_STRUCTURE_ONLY B PROVISIONAL C NOT_RUN")
sys.exit(bool(err))
