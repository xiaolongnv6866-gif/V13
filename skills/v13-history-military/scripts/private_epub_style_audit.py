#!/usr/bin/env python3
"""Run on private user EPUB files only; output aggregate statistics without quotes."""
import argparse, json, random, re, statistics, zipfile
from pathlib import Path
from bs4 import BeautifulSoup
def sample(epub:Path):
    ps=[]
    with zipfile.ZipFile(epub) as z:
        for name in z.namelist():
            if not name.lower().endswith((".html",".xhtml")):continue
            soup=BeautifulSoup(z.read(name),"html.parser")
            for item in soup.find_all("p"):
                text=item.get_text("",strip=True)
                if 90<=len(text)<=600 and len(re.findall("[，。！？；]",text))>=5:ps.append(text)
    if len(ps)<20:raise ValueError("Insufficient suitable paragraphs")
    rnd=random.Random(20261012)
    chosen=[ps[i] for i in sorted(rnd.sample(range(len(ps)),20))]
    joined="".join(chosen)
    lengths=[len(x.strip()) for line in chosen for x in re.split("[。！？]",line) if x.strip()]
    return dict(eligible_paragraphs=len(ps),sample_n=20,total_chars=len(joined),
                mean_paragraph_chars=round(statistics.mean(map(len,chosen)),1),
                mean_sentence_chars=round(statistics.mean(lengths),1),median_sentence_chars=statistics.median(lengths),
                question_marks=joined.count("？"),dialogue_open_quotes=joined.count("“"),
                contrast_words=sum(joined.count(w) for w in ["但是","然而","不过","可是"]),
                certainty_words=sum(joined.count(w) for w in ["一定","显然","必然","绝对"]),
                hedge_words=sum(joined.count(w) for w in ["似乎","可能","大概","或许"]))
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("epubs",nargs="+",type=Path)
    args=ap.parse_args()
    print(json.dumps({p.name:sample(p) for p in args.epubs},ensure_ascii=False,indent=2))
