#!/usr/bin/env python3
"""V13 R006 frozen Stage0 evidence-contract and heldout-seal validator.

Default: public-only contract checks + synthetic in-memory acceptance/rejection tests.
--receipts FILE: validate real JSONL receipt syntax+R002 metadata; NOT enough to
                  claim private-text reading.
--receipts FILE --source-dir DIR: additionally verify actual private EPUB SHA,
                  chapter ZIP bytes and anchored paragraph SHA with lxml.
This validator never emits the contents of novels or held-out writing prompts.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "wanming": {
        "sha": "a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082",
        "count": 571,
        "spine": 588,
        "filename": "晚明",
    },
    "tiexuecanming": {
        "sha": "9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf",
        "count": 532,
        "spine": 551,
        "filename": "铁血残明",
    },
}
SHA = re.compile(r"^[a-f0-9]{64}$")
MODES = ("INDEX_ONLY", "STRUCTURAL_SAMPLE", "FULL_TEXT_READ", "CLOSE_READ")
ASPECTS = {
    "scene_entry_exit", "pov_information", "action_reaction",
    "sentence_rhythm", "dialogue_subtext", "emotion_reader",
    "causal_payoff", "chapter_handoff", "historical_constraints"
}
REQUIRED = {
    "book_slug","narrative_ordinal","spine_index","epub_path",
    "source_epub_sha256","chapter_sha256","mode","body_paragraph_count",
    "observed_paragraph_count","anchors","event_chain","open_questions",
    "mechanism_claims","fixture_only"
}
ROOT_FIELDS = REQUIRED | {"reader_session_id","round_id","paragraph_normalization"}
CLAIM_FIELDS = {
    "claim_id","claim_text","aspect","support_anchor_ids",
    "counterexample_status","counterexample_anchor_ids","counterexample_search_note",
    "alternative_rendering_loss","failure_boundary","confidence","verification_state"
}

def problem(errors, test, message):
    if not test:
        errors.append(message)

def load_meta():
    out={}
    for book,cfg in EXPECTED.items():
        filename=ROOT/"sources/metadata"/(book+"_v13_spine.csv")
        with filename.open(encoding="utf-8",newline="") as f:
            rows=list(csv.DictReader(f))
        if len(rows)!=cfg["spine"]:
            raise ValueError("Spine count mismatch: "+book)
        narrated=[r for r in rows if r["narrative_ordinal"]]
        expected=list(range(1,cfg["count"]+1))
        if [int(r["narrative_ordinal"]) for r in narrated]!=expected:
            raise ValueError("Narrative order mismatch: "+book)
        for r in narrated:
            out[(book,int(r["narrative_ordinal"]))]=r
    return out

def validate_receipt(r, metadata, *, private_checked=False):
    errors=[]
    if not isinstance(r,dict):
        return ["receipt is not JSON object"]
    problem(errors,REQUIRED<=r.keys(),"missing required fields")
    problem(errors,set(r)<=ROOT_FIELDS,"unknown top-level fields")
    if not REQUIRED<=r.keys():
        return errors
    book=r["book_slug"];ordn=r["narrative_ordinal"]
    problem(errors,book in EXPECTED,"book slug not locked")
    problem(errors,type(ordn) is int and 1<=ordn<=EXPECTED.get(book,{"count":0})["count"],"invalid narrative ordinal")
    meta=metadata.get((book,ordn)) if type(ordn) is int else None
    problem(errors,meta is not None,"no R002 matched narrative entry")
    if meta is not None:
        problem(errors,r["spine_index"]==int(meta["spine_index"]),"spine index does not match R002")
        problem(errors,r["epub_path"]==meta["epub_path"],"ZIP path does not match R002")
        problem(errors,r["chapter_sha256"]==meta["chapter_sha256"],"chapter file SHA does not match R002")
    problem(errors, isinstance(r["source_epub_sha256"],str) and SHA.fullmatch(r["source_epub_sha256"]) is not None and r["source_epub_sha256"]==EXPECTED.get(book,{}).get("sha"),"entire EPUB SHA invalid")
    problem(errors,isinstance(r["chapter_sha256"],str) and SHA.fullmatch(r["chapter_sha256"]) is not None,"chapter SHA syntax")
    mode=r["mode"]
    problem(errors,mode in MODES,"unknown reading mode")
    total=r["body_paragraph_count"];observed=r["observed_paragraph_count"]
    problem(errors,type(total) is int and total>=0 and type(observed) is int and 0<=observed<=total,"paragraph count impossible")
    anchors=r["anchors"];claims=r["mechanism_claims"];events=r["event_chain"];questions=r["open_questions"]
    problem(errors,isinstance(anchors,list) and isinstance(claims,list) and isinstance(events,list) and isinstance(questions,list),"collections malformed")
    problem(errors,type(r["fixture_only"]) is bool,"fixture marker must be boolean")
    if errors:return errors
    if r["fixture_only"] and mode in ("FULL_TEXT_READ","CLOSE_READ"):
        # A synthetic positive fixture may be validated for structural correctness,
        # but can never contribute to public counted reading.
        pass
    if mode=="INDEX_ONLY":
        problem(errors,observed==0,"INDEX_ONLY cannot read paragraph body")
        problem(errors,len(anchors)==0 and len(claims)==0 and len(events)==0,"INDEX_ONLY cannot assert literary claims")
    elif mode=="STRUCTURAL_SAMPLE":
        problem(errors,total>0 and 0<observed<total,"SAMPLE must be proper nonempty subset, not a full read")
        problem(errors,len(anchors)>0,"SAMPLE needs at least one actual paragraph locator")
    elif mode in ("FULL_TEXT_READ","CLOSE_READ"):
        problem(errors,total>0 and observed==total,"FULL_TEXT_READ requires all nonempty XHTML paragraph positions")
        problem(errors,len(events)>=2 and all(isinstance(x,str) and x.strip() for x in events),"FULL_TEXT_READ needs nonempty event chain of two or more steps")
        problem(errors,len(anchors)>0,"FULL_TEXT_READ needs at least one evidence anchor")
        problem(errors,bool(r.get("reader_session_id")),"FULL_TEXT_READ needs real reader session identifier")
        problem(errors,r.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1","normalization must be recorded")
        problem(errors,len(questions)>0,"FULL_TEXT_READ must record open question or explicitly state none")
        if mode=="CLOSE_READ":
            problem(errors,len(claims)>0,"CLOSE_READ requires at least one mechanism claim")
    ids=set()
    for a in anchors:
        if not isinstance(a,dict):
            errors.append("anchor malformed");continue
        aid=a.get("anchor_id")
        problem(errors,isinstance(aid,str) and bool(aid.strip()),"anchor id missing")
        problem(errors,aid not in ids,"anchor id repeated")
        ids.add(aid)
        cross=a.get("source_ref")
        if cross is not None:
            problem(errors,isinstance(cross,dict) and set(cross)=={"book_slug","narrative_ordinal","chapter_sha256","epub_path"},"cross-chapter source_ref fields")
            if isinstance(cross,dict) and set(cross)=={"book_slug","narrative_ordinal","chapter_sha256","epub_path"}:
                m=metadata.get((cross["book_slug"],cross["narrative_ordinal"]))
                problem(errors,m is not None and cross["chapter_sha256"]==m["chapter_sha256"] and cross["epub_path"]==m["epub_path"],"cross chapter reference mismatch")
        para=a.get("paragraph_index")
        problem(errors,type(para) is int and para>0 and (cross is not None or para<=total),"anchor index beyond current chapter")
        sha=a.get("paragraph_sha256")
        problem(errors,isinstance(sha,str) and SHA.fullmatch(sha) is not None,"paragraph hash missing")
        problem(errors,isinstance(a.get("locator_note"),str) and len(a["locator_note"].strip())>=2,"paragraph locator explanation missing")
    for claim in claims:
        if not isinstance(claim,dict):
            errors.append("claim malformed");continue
        problem(errors,CLAIM_FIELDS<=claim.keys(),"incomplete mechanism claim")
        if not CLAIM_FIELDS<=claim.keys():continue
        problem(errors,claim["aspect"] in ASPECTS,"unknown literary aspect")
        positives=claim["support_anchor_ids"];negatives=claim["counterexample_anchor_ids"]
        if not isinstance(positives,list) or not isinstance(negatives,list):
            errors.append("claim anchors malformed");continue
        problem(errors,len(positives)>0 and all(x in ids for x in positives),"support anchors unresolvable")
        problem(errors,all(x in ids for x in negatives),"counterexample anchors unresolvable")
        status=claim["counterexample_status"];state=claim["verification_state"]
        problem(errors,status in ("FOUND","SEARCHED_NONE","NOT_CHECKED"),"counterexample status invalid")
        problem(errors,state in ("HYPOTHESIS","PROVISIONAL","VERIFIED"),"verification status invalid")
        problem(errors,len(claim["alternative_rendering_loss"].strip())>=5,"missing alternative narrative comparison")
        problem(errors,len(claim["failure_boundary"].strip())>=5,"missing hypothesis failure conditions")
        if status=="FOUND":
            problem(errors,len(negatives)>0,"FOUND counterexample must have anchored evidence")
        else:
            problem(errors,len(negatives)==0,"counterexample anchors without actual FOUND")
            problem(errors,bool(claim["counterexample_search_note"].strip()) or state=="HYPOTHESIS","SEARCHED_NONE must show search")
        if state=="VERIFIED":
            problem(errors,status=="FOUND" and len(negatives)>0,"cannot mark VERIFIED before finding anchored contrary evidence")
        elif status=="SEARCHED_NONE":
            problem(errors,state=="PROVISIONAL","searched but no counterexample = provisional only")
        if status=="NOT_CHECKED":
            problem(errors,state=="HYPOTHESIS","not checked => hypothesis only")
    if private_checked:
        problem(errors,not r["fixture_only"],"synthetic fixture cannot be promoted as a real read")
    return errors

def test_fixtures(meta):
    book="wanming";ordinal=1;row=meta[(book,ordinal)]
    h="a"*64
    base={
        "book_slug":book,"narrative_ordinal":ordinal,
        "spine_index":int(row["spine_index"]),"epub_path":row["epub_path"],
        "source_epub_sha256":EXPECTED[book]["sha"],
        "chapter_sha256":row["chapter_sha256"],"mode":"CLOSE_READ",
        "body_paragraph_count":3,"observed_paragraph_count":3,
        "anchors":[
            {"anchor_id":"a1","paragraph_index":1,"paragraph_sha256":h,"locator_note":"虚构测试段落一"},
            {"anchor_id":"a2","paragraph_index":2,"paragraph_sha256":h,"locator_note":"虚构测试段落二"}
        ],
        "event_chain":["虚构起点","虚构事件变化"],"open_questions":["无；合成用例"],
        "mechanism_claims":[{
            "claim_id":"c1","claim_text":"仅用于检查结构正确性，绝非原书结论。",
            "aspect":"action_reaction","support_anchor_ids":["a1"],
            "counterexample_status":"FOUND","counterexample_anchor_ids":["a2"],
            "counterexample_search_note":"合成反例测试","alternative_rendering_loss":"替代叙法会改变可见反馈",
            "failure_boundary":"没有真实来源则不能视为文学证据",
            "confidence":"LOW","verification_state":"VERIFIED"
        }],
        "fixture_only":True,"reader_session_id":"SYNTHETIC_TEST_NOT_READ",
        "paragraph_normalization":"xhtml_visible_text_trim_whitespace_v1",
        "round_id":"R007"
    }
    import copy
    check=lambda obj:validate_receipt(obj,meta)
    assert not check(base),check(base)
    bad=copy.deepcopy(base);bad["chapter_sha256"]="f"*64;assert check(bad),"wrong chapter hash accepted"
    bad=copy.deepcopy(base);bad["narrative_ordinal"]=999;assert check(bad),"unknown chapter accepted"
    bad=copy.deepcopy(base);bad["mode"]="INDEX_ONLY";assert check(bad),"index faked as full accepted"
    bad=copy.deepcopy(base);bad["mode"]="STRUCTURAL_SAMPLE";assert check(bad),"full corpus masquerading as sample accepted"
    bad=copy.deepcopy(base);bad["observed_paragraph_count"]=2;assert check(bad),"partial read counted full"
    bad=copy.deepcopy(base);bad["anchors"]=[];assert check(bad),"missing original anchors accepted"
    bad=copy.deepcopy(base);bad["mechanism_claims"][0]["support_anchor_ids"]=["missing"];assert check(bad),"missing support accepted"
    bad=copy.deepcopy(base);bad["mechanism_claims"][0]["counterexample_anchor_ids"]=[];assert check(bad),"counterevidence fabricated"
    bad=copy.deepcopy(base);bad["mechanism_claims"][0]["counterexample_status"]="NOT_CHECKED";assert check(bad),"unchecked treated verified"
    bad=copy.deepcopy(base);bad["mechanism_claims"][0]["counterexample_status"]="SEARCHED_NONE";bad["mechanism_claims"][0]["counterexample_anchor_ids"]=[];assert check(bad),"provisional mislabeled verified"
    bad=copy.deepcopy(base);bad.pop("reader_session_id");assert check(bad),"reader session absent accepted"
    bad=copy.deepcopy(base);bad["fixture_only"]=False;assert not check(bad),"fixture real switch should be structurally valid"
    assert not check(base),"valid synthetic positive must stay structurally valid"
    return 12

def check_public():
    errs=[]
    cfg=json.loads((ROOT/"tests/heldout/COMMITMENT.json").read_text("utf-8"))
    parent=ROOT/"tests/heldout"
    expected={"README.md","COMMITMENT.json"}
    problem(errs,{p.name for p in parent.iterdir()}==expected,"Public GitHub leaked a heldout file or missing expected file")
    problem(errs,cfg.get("round")=="R006" and cfg.get("bank_case_count")==12,"Heldout bank size or project mismatch")
    problem(errs,cfg.get("public_release")=="COMMITMENT_ONLY" and cfg.get("execution_status")=="NOT_RUN","Holdout must remain sealed and unused")
    problem(errs,cfg.get("key_stored_in_github") is False and cfg.get("plaintext_stored_in_github") is False,"Key/plaintext marked as public")
    problem(errs,all(SHA.fullmatch(cfg.get(k,"")) for k in ("plaintext_sha256","sealed_packet_sha256")),"Missing SHA commitment")
    problem(errs, cfg.get("case_ids")==[f"H{i:03d}" for i in range(1,13)],"Blind case ID sequence not frozen")
    txt=(ROOT/"cangjie/STAGE0_READING_CONTRACT.md").read_text("utf-8")
    for marker in ("INDEX_ONLY","STRUCTURAL_SAMPLE","FULL_TEXT_READ","CLOSE_READ","Adler","counterexample_status","反例","0/1103"):
        problem(errs,marker in txt,"Contract missing invariant: "+marker)
    schema=json.loads((ROOT/"tests/contracts/reading-receipt.schema.json").read_text("utf-8"))
    problem(errs,schema.get("type")=="object" and schema.get("additionalProperties") is False,"Contract JSON schema malformed")
    source=(ROOT/"SOURCE_MANIFEST.md").read_text("utf-8")
    for val in EXPECTED.values():problem(errs,val["sha"] in source,"R002 source fingerprint missing")
    cursor=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"))
    token=str(cursor.get("current_round",""))
    rnd=int(token[1:]) if token.startswith("R") and token[1:].isdigit() else -1
    problem(errs,6 <= rnd <= 89,"R006 protocol valid only within V13 R006—R089")
    # Frozen R006 invariants govern the original R006 only; later real reading
    # and skill certification MUST NOT be falsely flagged by historical CI.
    if rnd <= 6:
        problem(errs,cursor.get("full_text_read_chapters")=={"wanming":0,"tiexuecanming":0},"R006 cannot increment chapter reads")
        problem(errs,cursor.get("skill_certified_count")==0,"R006 cannot certify writing SKILL")
    return errs

def locate_original(srcdir, filename):
    candidates=sorted(set(srcdir.glob(filename+" *.epub"))|set(srcdir.glob(filename+".epub")))
    if len(candidates)!=1:raise ValueError(f"Expected exactly one private EPUB for {filename}, found {len(candidates)}")
    return candidates[0]

def sha_file(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for part in iter(lambda:f.read(1<<20),b""):h.update(part)
    return h.hexdigest()

def verify_private_anchors(receipts,source_dir,meta):
    # Private source check, not run on GitHub: user-provided novel bytes cannot be in public repo.
    try:
        from lxml import html
    except ImportError as exc:
        raise RuntimeError("lxml is needed for private paragraph hash verification") from exc
    archives={}
    for book,cfg in EXPECTED.items():
        p=locate_original(source_dir,cfg["filename"])
        if sha_file(p)!=cfg["sha"]:raise ValueError("Private EPUB full SHA mismatch: "+book)
        archives[book]=zipfile.ZipFile(p)
    try:
        for receipt in receipts:
            if receipt["mode"] not in ("FULL_TEXT_READ","CLOSE_READ"):
                continue
            if receipt["fixture_only"]:raise ValueError("Fixture passed into production private verification")
            row=meta[(receipt["book_slug"],receipt["narrative_ordinal"])]
            raw=archives[receipt["book_slug"]].read(row["epub_path"])
            if hashlib.sha256(raw).hexdigest()!=row["chapter_sha256"]:
                raise ValueError("Original chapter byte SHA mismatch")
            ps=[s.strip() for x in html.fromstring(raw).xpath("//body//p") if (s:=x.text_content()).strip()]
            if len(ps)!=receipt["body_paragraph_count"]:
                raise ValueError("Actual XHTML paragraph count does not match receipt")
            for anchor in receipt["anchors"]:
                ref=anchor.get("source_ref")
                if ref is None:
                    srcbook=receipt["book_slug"]; paragraphs=ps
                else:
                    srcbook=ref["book_slug"]; cross=meta[(srcbook,ref["narrative_ordinal"])]
                    data=archives[srcbook].read(cross["epub_path"])
                    if hashlib.sha256(data).hexdigest()!=cross["chapter_sha256"]:
                        raise ValueError("Cross chapter original SHA mismatch")
                    paragraphs=[s.strip() for x in html.fromstring(data).xpath("//body//p") if (s:=x.text_content()).strip()]
                n=anchor["paragraph_index"]
                if n<1 or n>len(paragraphs):
                    raise ValueError("Private paragraph anchor index out of range")
                if hashlib.sha256(paragraphs[n-1].encode("utf-8")).hexdigest()!=anchor["paragraph_sha256"]:
                    raise ValueError("Private paragraph SHA mismatch")
    finally:
        for a in archives.values():a.close()

def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--receipts",type=Path,help="Actual per-chapter reading receipts JSONL")
    cli.add_argument("--source-dir",type=Path,help="Private EPUB directory; requires --receipts, verifies exact bytes+paragraphs")
    args=cli.parse_args()
    if args.source_dir and not args.receipts:cli.error("--source-dir requires --receipts")
    errs=check_public()
    meta=load_meta()
    synthetic=test_fixtures(meta)
    if errs:
        for e in errs:print("FAIL:",e)
        return 1
    print(f"PASS R006 public: chapter indices 571+532, frozen four reading modes, sealed 12-case SHA commitments, zero public prompts or keys, {synthetic} synthetic validity/regression checks")
    if args.receipts:
        receipts=[json.loads(l) for l in args.receipts.read_text("utf-8").splitlines() if l.strip()]
        keys=set()
        for idx,r in enumerate(receipts,1):
            for error in validate_receipt(r,meta,private_checked=bool(args.source_dir)):
                errs.append(f"receipt #{idx}: {error}")
            key=(r.get("book_slug"),r.get("narrative_ordinal"))
            if key in keys:errs.append("Duplicate book+ordinal receipt")
            keys.add(key)
        if errs:
            for e in errs:print("FAIL:",e)
            return 1
        if args.source_dir:
            verify_private_anchors(receipts,args.source_dir,meta)
            print("PASS private verified: matched original EPUB SHA and anchored XHTML paragraph hashes")
        else:
            print("SOURCE_STRUCTURE_ONLY: without private original EPUB, a complete read cannot be certified")
        print("Receipt records checked:",len(receipts))
    return 0

if __name__=="__main__":
    try:sys.exit(main())
    except Exception as exc:
        print("FAIL:",type(exc).__name__,str(exc))
        sys.exit(1)
