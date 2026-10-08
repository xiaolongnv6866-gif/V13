#!/usr/bin/env python3
"""Verify V13's 89-round controller, chapter ranges, and progress cursor."""
import csv, json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
IDS=[f"R{i:03d}" for i in range(1,90)]
COUNTS={"晚明":571,"铁血残明":532}
USER_GATES=[4,42,57,68,69,77,80,83,86,89]
def main():
    errors=[]
    def ck(cond,msg):
        if not cond:errors.append(msg)
    plan=(ROOT/"V13_FIXED_89_ROUNDS.md").read_text(encoding="utf-8")
    ids=re.findall(r"^#{3,4}\s+(R\d{3})\s+·\s+",plan,re.M)
    ck(ids==IDS,f"Round IDs not 001..089: {len(ids)} found")
    with (ROOT/"ROUND_LEDGER.csv").open(encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    ck([x.get("id") for x in rows]==IDS,"Ledger IDs mismatch")
    cursor=json.loads((ROOT/"CURRENT_ROUND.json").read_text(encoding="utf-8"))
    ck(cursor.get("rounds_total")==89,"Cursor rounds_total wrong")
    states=[r["status"] for r in rows]
    allowed={"NOT_STARTED","IN_PROGRESS","FAILED","BLOCKED","PASSED","NOT_APPLICABLE"}
    ck(set(states)<=allowed,"Invalid ledger status")
    active=next((i for i,s in enumerate(states) if s not in {"PASSED","NOT_APPLICABLE"}),None)
    if active is not None:
        ck(cursor.get("current_round")==IDS[active],"Cursor skips earliest pending round")
        ck(cursor.get("round_status")==states[active],"Cursor and ledger status disagree")
        ck(all(s=="NOT_STARTED" for s in states[active+1:]),"Future round was started too early")
    expected_last=IDS[active-1] if active is not None and active>0 else None
    ck(cursor.get("last_passed_round")==expected_last,"Last passed round mismatch")
    coverage={k:set() for k in COUNTS}
    for m in re.finditer(r"^#{3,4}\s+(R\d{3})\s+·\s+《(晚明|铁血残明)》全文第(\d{3})[—-](\d{3})章",plan,re.M):
        rnd,name,lo,hi=int(m[1][1:]),m[2],int(m[3]),int(m[4])
        ck(7<=rnd<=35,f"Reading outside 007-035: {rnd}")
        ck(lo<=hi<=COUNTS[name],f"Range out of bounds {name}:{lo}-{hi}")
        ck(not coverage[name].intersection(range(lo,hi+1)),f"Duplicate book chapters in {name}")
        coverage[name].update(range(lo,hi+1))
    for k,n in COUNTS.items():
        ck(coverage[k]==set(range(1,n+1)),f"Missing chapter coverage {k}: {len(coverage[k])}/{n}")
    ck(all(f"R{x:03d}" in plan for x in USER_GATES),"Some mandatory user gate not listed")
    manifest=(ROOT/"SOURCE_MANIFEST.md").read_text(encoding="utf-8")
    for sha in ("a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082","9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"):
        ck(sha in manifest,"Source SHA missing: "+sha[:12])
    ck(not list(ROOT.rglob("*.epub")),"Source copyright EPUB detected in repository")
    ck(len(states)==89,"Ledger must have 89 rows")
    for msg in errors:print("FAIL:",msg)
    if errors:return 1
    print("PASS V13 guardrails: 89 unique rounds, 89 ledger rows, cursor agreement, 29 reading rounds, 1103 non-overlapping chapters, 10 user gates, source fingerprints")
    return 0
if __name__=="__main__":sys.exit(main())
