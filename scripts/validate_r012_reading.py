#!/usr/bin/env python3
import csv,json,sys,re
from pathlib import Path
r=Path(__file__).resolve().parents[1]
a=[json.loads(x) for x in (r/"cangjie/reading/R012/tiexue_receipts.jsonl").read_text().splitlines() if x]
with (r/"sources/metadata/tiexuecanming_v13_spine.csv").open(newline="") as f:
 m={int(x["narrative_ordinal"]):x for x in csv.DictReader(f) if x["narrative_ordinal"]}
focus={81,83,88,91,94,100,103,105,109,110,116,120}
assert len(a)==40 and [x["narrative_ordinal"] for x in a]==list(range(81,121))
assert sum(x["body_paragraph_count"] for x in a)==2745
assert sum(len(x["anchors"]) for x in a)==64
assert sum(x["mode"]=="CLOSE_READ" for x in a)==12
h=2166136261
for x in a:
 n=x["narrative_ordinal"];v=m[n]
 assert x["spine_index"]==int(v["spine_index"])
 assert x["chapter_sha256"]==v["chapter_sha256"]
 assert x["epub_path"]==v["epub_path"]
 assert x["body_paragraph_count"]==int(v["nonempty_paragraphs"])==x["observed_paragraph_count"]
 assert len(x["event_chain"])==2 and all(len(t)>24 for t in x["event_chain"])
 assert len(x["anchors"])==(3 if n in focus else 1)
 assert x["mode"]==("CLOSE_READ" if n in focus else "FULL_TEXT_READ")
 for p in x["anchors"]:
  assert 0<p["paragraph_index"]<=x["body_paragraph_count"]
  assert re.fullmatch("[0-9a-f]{64}",p["paragraph_sha256"])
  s=f'{n}/{p["paragraph_index"]}/{p["paragraph_sha256"]}\n'
  for ch in s:h=((h^ord(ch))*16777619)&0xffffffff
assert f"{h:08x}"=="41912408"
s=json.loads((r/"CURRENT_ROUND.json").read_text())
assert int(s["current_round"][1:])>=12
assert s["full_text_read_chapters"]["tiexuecanming"]==(80 if s["current_round"]=="R012" else s["full_text_read_chapters"]["tiexuecanming"])
assert s["full_text_read_chapters"]["tiexuecanming"]>=80
print("PASS R012: 40 original chapters, 2745 paragraph counts, 64 source hashes, 12 focused literature cases")
