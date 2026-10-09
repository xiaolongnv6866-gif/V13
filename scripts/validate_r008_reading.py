#!/usr/bin/env python3
"""V13 R008: deterministic regression audit of *public* per-chapter source receipts.
Does not claim GitHub Action has original novel bytes. Private source SHA+anchors
were verified separately; all original excerpts remain outside public git.
"""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
F=ROOT/"cangjie/reading/R008/tiexue_receipts.jsonl"
INDEX=ROOT/"cangjie/reading/R008/tiexue_source_index.csv"
CSV=ROOT/"sources/metadata/tiexuecanming_v13_spine.csv"
BOOKSHA="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
CLOSE={1,20,29,31,32,33,35,37,39,40}
def main():
  errors=[]
  def ck(ok,msg):
    if not ok:errors.append(msg)
  with CSV.open(encoding="utf-8",newline="") as f:
    meta={int(r["narrative_ordinal"]):r for r in csv.DictReader(f) if r["narrative_ordinal"]}
  with INDEX.open(encoding="utf-8",newline="") as f:ix=list(csv.DictReader(f))
  records=[json.loads(line) for line in F.read_text("utf-8").splitlines() if line.strip()]
  ck(len(records)==40 and len(ix)==40,"R008 must include 40 separate receipts and indices")
  ck([r["narrative_ordinal"] for r in records]==list(range(1,41)),"missing/reordered narrative ordinal")
  ck([int(r["narrative_ordinal"]) for r in ix]==list(range(1,41)),"source index order inconsistent")
  paras=0;anchors=0;close=0;events=set()
  for r,idx in zip(records,ix):
    n=r["narrative_ordinal"];m=meta.get(n)
    if m is None:errors.append(f"R002 missing chapter {n}");continue
    ck(r["book_slug"]=="tiexuecanming" and r["source_epub_sha256"]==BOOKSHA,f"source EPUB mismatch {n}")
    ck(r["spine_index"]==int(m["spine_index"])==int(idx["spine_index"]),f"OPF spine mismatch {n}")
    ck(r["epub_path"]==m["epub_path"]==idx["epub_path"],f"ZIP member mismatch {n}")
    ck(r["chapter_sha256"]==m["chapter_sha256"]==idx["chapter_sha256"],f"source chapter bytes mismatch {n}")
    p=int(m["nonempty_paragraphs"])
    ck(r["body_paragraph_count"]==p==r["observed_paragraph_count"]==int(idx["nonempty_paragraphs"]),f"paragraph count mismatch {n}")
    ck(r["mode"]==("CLOSE_READ" if n in CLOSE else "FULL_TEXT_READ"),f"wrong real-reading mode {n}")
    ck(r["fixture_only"] is False and r["round_id"]=="R008" and r.get("reader_session_id"),f"invalid session provenance {n}")
    ck(r["paragraph_normalization"]=="xhtml_visible_text_trim_whitespace_v1",f"source normalization mismatch {n}")
    ck(len(r["event_chain"])==2 and all(isinstance(s,str) and len(s)>18 for s in r["event_chain"]),f"actual distinct narrative reasoning not recorded {n}")
    ck(r["event_chain"][0] not in events,f"repeated non-distinct episode {n}");events.add(r["event_chain"][0])
    ck(len(r["open_questions"])>=1,f"missing unresolved consequence {n}")
    hashes=[f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in r["anchors"]]
    ck(len(hashes)>=1 and all(0<a["paragraph_index"]<=p and re.fullmatch(r"[0-9a-f]{64}",a["paragraph_sha256"]) for a in r["anchors"]),f"invalid paragraph SHA anchor {n}")
    ck(";".join(hashes)==idx["paragraph_index_sha256_anchors"],f"local-public index anchors disagree {n}")
    if n in CLOSE:
      close+=1
      ck(len(r["mechanism_claims"])>=1,f"missing close-read claim {n}")
      for claim in r["mechanism_claims"]:
        ck(claim["verification_state"]=="PROVISIONAL",f"claim falsely marked verified {n}")
        ck(claim["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"claim without honest counterexample status {n}")
        ck(all(s in {a["anchor_id"] for a in r["anchors"]} for s in claim["support_anchor_ids"]),f"claim missing original locator {n}")
    paras+=p;anchors+=len(hashes)
  ck(paras==2712,"source paragraph count must be 2712")
  ck(anchors==60,"source anchor count must be 60")
  ck(close==10,"10 verified-close-scope notes required")
  for f in ["cangjie/reading/tiexue_001_040.md","cangjie/reading/R008/tiexue_continuity.md","cangjie/reading/R008/LOCAL_SOURCE_VERIFICATION.md"]:
    ck((ROOT/f).is_file(),"missing R008 artifact "+f)
  c=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"))
  rid=c["current_round"];num=int(rid[1:]) if rid.startswith("R") and rid[1:].isdigit() else -1
  ck(8<=num<=89,"historical R008 validator must not run before R008")
  if num==8:
    ck(c["full_text_read_chapters"]["tiexuecanming"]==0,"R008 cannot count before PASS")
    ck(c["full_text_read_chapters"]["wanming"]==40,"R007 count regressed")
  elif num>8:
    ck(c["full_text_read_chapters"]["tiexuecanming"]>=40,"R008 previously certified count regressed")
    ck(c["full_text_read_chapters"]["wanming"]>=40,"R007 count regressed")
  for e in errors:print("FAIL",e)
  if errors:return 1
  print("PASS R008: 40 unique original ordinals 001-040, R002 ZIP hashes, 2712 original paragraph-count receipts, 60 anchored SHA, 10 provisional close studies, all 40 causal reports, current-state guard; no claim of independent blind writing test")
  return 0
if __name__=="__main__":sys.exit(main())
