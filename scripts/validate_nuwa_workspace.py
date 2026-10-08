#!/usr/bin/env python3
"""R005: verify self-contained Nuwa Phase0.5 workspace without inventing Phase1 work."""
import csv, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WS=ROOT/"nuwa/workspace"
ERRORS=[]
def check(ok,msg):
    if not ok: ERRORS.append(msg)
def git_blob(p):
    return subprocess.check_output(["git","hash-object","--",str(p)],text=True).strip()
def main():
    state=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"))
    token=str(state.get("current_round",""))
    cursor_num=int(token[1:]) if token.startswith("R") and token[1:].isdigit() else -1
    manifest=json.loads((WS/"references/upstream/COPIED_FILES.json").read_text("utf-8"))
    check(manifest.get("nuwa_git_commit")=="fe0374687037c4cc51a65c1e0c145afe2981dc69","Nuwa original commit mismatch")
    check(len(manifest.get("upstream",[]))==9,"Must preserve full Nuwa Skill, 3 refs, 4 scripts, license")
    check(len(manifest.get("v13",[]))==3,"Must preserve 2 spine indices + R002 source manifest")
    for record in manifest.get("upstream",[])+manifest.get("v13",[]):
        p=WS/record["workspace_path"]
        check(p.is_file(),"Missing required source "+str(p))
        if p.is_file(): check(git_blob(p)==record["expected_git_blob"],"Source Git blob mismatch "+str(p))
    must=["SKILL.md","README.md","sources/SOURCE_REGISTER.csv","sources/books/README.md","sources/transcripts/README.md","sources/articles/README.md","references/research/README.md","references/research/00-school-map.md"]
    for p in must:check((WS/p).is_file(),"Missing "+p)
    draft=(WS/"SKILL.md").read_text("utf-8")
    # Phase0.5 is a draft; Phase3 (R081 onward) must be allowed to replace it.
    if cursor_num < 81:
        check("DRAFT_NOT_INSTALLED" in draft and "research_count: 0" in draft,"Prematurely activated Nuwa skill")
    research=WS/"references/research"
    chapters=["writings","conversations","expression-dna","external-views","decisions","timeline"]
    placeholders=[research/f"{i:02d}-{slug}.md" for i,slug in enumerate(chapters,1)]
    placeholders += [research/f"school_{i:02d}.md" for i in range(1,6)]
    placeholders += [research/"00-school-map.md"]
    check(len(placeholders)==12,"Placeholder count")
    for p in placeholders:
        check(p.is_file(),"Missing research slot "+str(p))
        if p.is_file():
            s=p.read_text("utf-8")
            if cursor_num < 70:
                check("status: NOT_STARTED" in s and "source_count: 0" in s and "research_agent_runs: 0" in s,"Research prematurely claimed before R070 "+str(p))
    with (WS/"sources/SOURCE_REGISTER.csv").open(encoding="utf-8",newline="") as f: source_rows=list(csv.DictReader(f))
    originals={r["source_id"]:r for r in source_rows}
    check({"wm_epub","tx_epub"}.issubset(originals),"Original V13 two novel entries missing")
    check(all(originals[k]["access_status"]=="PRIVATE_USER_EPUB_NOT_BUNDLED" for k in ("wm_epub","tx_epub") if k in originals),"Original novel EPUBs cannot be bundled in public GitHub")
    for slug,total,narrative in [("wanming",588,571),("tiexuecanming",551,532)]:
        with (WS/"sources/books"/(slug+"_v13_spine.csv")).open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
        ords=[int(r["narrative_ordinal"]) for r in rows if r["narrative_ordinal"]]
        check(len(rows)==total and ords==list(range(1,narrative+1)),slug+" chapters metadata mismatch")
    for ext in ["*.epub","*.mobi","*.azw","*.azw3","*.pdf"]:
        check(not list(WS.rglob(ext)),"Illegal raw original in workspace: "+ext)
    for p in (WS/"scripts").glob("*.py"):
        try:compile(p.read_text("utf-8"),str(p),"exec")
        except SyntaxError as e:ERRORS.append(str(e))
    state=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"))
    # Historical R005 integrity must stay green as V13 moves through later rounds.
    token=str(state.get("current_round",""))
    cursor_num=int(token[1:]) if token.startswith("R") and token[1:].isdigit() else -1
    check(5 <= cursor_num <= 89,"Unexpected cursor before R005 or outside the 89 rounds")
    check(state["nuwa_phase0"]=="APPROVED_THEME_STANDARD","R004 not authorized")
    if cursor_num <= 6:
        check(state["full_text_read_chapters"]=={"wanming":0,"tiexuecanming":0},"False early literary progress")
    if cursor_num <= 6:
        check(state["skill_certified_count"]==0,"False early certified skill count")
    for e in ERRORS:print("FAIL:",e)
    if ERRORS:return 1
    print("PASS R005 invariant: exact pinned Nuwa originals, original metadata, stage-appropriate workspace state, 2 private EPUBs external, 1103 indexed narrative chapters, no public EPUB")
    return 0
if __name__=="__main__":sys.exit(main())
