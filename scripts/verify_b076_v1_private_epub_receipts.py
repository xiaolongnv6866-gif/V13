#!/usr/bin/env python3
"""Optional PRIVATE-EPUB source proof check; DO NOT commit copyrighted EPUBs."""
import argparse,csv,hashlib,re,zipfile
from pathlib import Path
from lxml import html
P=Path(__file__).resolve().parents[1]
D={"wanming":"a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082","tiexuecanming":"9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"}
def rows(p):
 with (P/p).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def sha(b):return hashlib.sha256(b).hexdigest()
def source_paths(book):
 path_map={}
 for t in ["FRAMEWORK","PRINCIPLE","CASE","COUNTEREXAMPLE","GLOSSARY"]:
  for row in rows(f"books/{book}/candidates/{t}_EVIDENCE.tsv"):
   n=row.get("narrative_ordinal","")
   path=row.get("epub_path","")
   if str(n).isdigit() and path:
    n=int(n)
    if n in path_map and path_map[n]!=path:raise ValueError(f"conflicting ordinal {book} n{n}")
    path_map[n]=path
 return path_map
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--wanming",required=True)
 p.add_argument("--tiexue",required=True)
 v=p.parse_args()
 ebooks={"wanming":v.wanming,"tiexuecanming":v.tiexue}
 for book,fn in ebooks.items():
  if sha(Path(fn).read_bytes())!=D[book]:raise ValueError(f"{book} EPUB checksum mismatch")
 mapping={book:source_paths(book) for book in ebooks}
 receipts=rows("gates/B076_V1_28_ACTUAL_SOURCE_RECHECK.tsv")
 assert len(receipts)==28
 parts=set();files=set();count=0
 for r in receipts:
  book=r["book"]
  anchors=[]
  with zipfile.ZipFile(ebooks[book]) as z:
   for n,p in re.findall(r"n(\d+)/p(\d+)",r["source_loci"]):
    n,p=int(n),int(p)
    filepath=mapping[book][n];raw=z.read(filepath)
    ps=["".join(t.itertext()).strip() for t in html.fromstring(raw).xpath("//p")]
    ps=[t for t in ps if t]
    assert 1<=p<=len(ps),(book,n,p)
    name=f"n{n:03}/p{p}"
    anchors.append(name+"="+sha(ps[p-1].encode("utf-8")))
    count+=1;parts.add((book,n,p));files.add((book,filepath))
  digest=sha("|".join(anchors).encode("utf-8"))
  assert r["paragraph_digest_sha256"]==digest,r["candidate_id"]
 assert count==89 and len(parts)==76 and len(files)==36,(count,len(parts),len(files))
 print("PASS: 28 IDs / 89 loci / 76 distinct paragraphs / 36 chapter files; 2 exact approved EPUBs; no original text uploaded")
if __name__=="__main__":main()
