#!/usr/bin/env python3
"""Only checks that all original stages are mapped; DOES NOT certify actual Skill execution."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"V13_3_FULL_SKILL_REQUIREMENTS.tsv").open(encoding="utf-8",newline="") as fp:
    rows=list(csv.DictReader(fp,delimiter="\t"))
required={"CJ00","CJ01F","CJ01P","CJ01C","CJ01E","CJ01G","CJ01I","CJ15V1","CJ15V2","CJ15V3","CJ15FLOW","CJ16","CJ02","CJ03","CJ04T","CJ04O","CJ04R","CJ05B","CJ05D","CJ20","NW00","NW05","NW01","NW15","NW02","NW25","NW03","NW04","NW04G","NW05R","FUSION","FINALE","DELIVERY","WORLD","SRC"}
ids=[r["id"] for r in rows]
assert len(rows)==len(required)==len(set(ids)) and set(ids)==required
valid={f"N{i:02d}" for i in range(1,49)}
for x in rows:
    for column in ("upstream","stage","exact_applicable_duty","required_evidence","responsible_rounds","do_not_forge"):
        assert x[column].strip(), (x["id"],column)
    for item in x["responsible_rounds"].split(","):
        if "-" in item:
            first,last=item.split("-")
            assert first in valid and last in valid and int(first[1:])<=int(last[1:])
        else: assert item in valid
for p in ("V13_3_FINISH_TO_SKILL_PLAN.md","V13_3_SKILL_DELIVERY_ACCEPTANCE.md"):
    t=(ROOT/p).read_text(encoding="utf-8")
    assert len(t)>250 and ("SKILL" in t)
text=(ROOT/"V13_3_FIXED_48_ROUNDS.md").read_text(encoding="utf-8")
for p in ("V13_3_FULL_SKILL_REQUIREMENTS.tsv","V13_3_FINISH_TO_SKILL_PLAN.md","V13_3_SKILL_DELIVERY_ACCEPTANCE.md"):
    assert p in text
print(f"PASS upstream full-fidelity requirements coverage map: {len(rows)} distinct obligations; administrative validation ONLY")
