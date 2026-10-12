#!/usr/bin/env python3
"""V13 Creative Harness: executable local, auditable stages.

Deterministic artifact host, not an LLM engine. Prevents pretend execution:
locks task intent, captures full text and sourced observations, verifies that
revisions actually modify the parent. Never promotes work into novel canon.
"""
import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def read_text(p):
    raw = p.read_bytes()
    if not raw.strip():
        raise ValueError('empty artifact: '+str(p))
    return raw.decode('utf-8')


def save_new(path, text):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:
        f.write(text)
        f.flush(); os.fsync(f.fileno())


def atomic_json(path, obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,t=tempfile.mkstemp(prefix='.run_',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f:
            json.dump(obj,f,ensure_ascii=False,indent=2)
            f.write('\n'); f.flush(); os.fsync(f.fileno())
        os.replace(t,path)
    finally:
        if os.path.exists(t): os.unlink(t)


def rootdir(a):
    if not re.fullmatch('[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}',a.case):
        raise ValueError('invalid case ID')
    return a.root.resolve()/a.case


def manifest(d):
    m=json.loads((d/'run.json').read_text('utf-8'))
    if m['schema']!=1: raise ValueError('unrecognized manifest')
    for item in [m['lock'],*m['drafts'],*m['reviews']]:
        f=d/item['path']
        if digest(f.read_bytes())!=item['sha256']:
            raise ValueError('artifact changed: '+str(f))
    return m


def cmd_init(a):
    d=rootdir(a)
    if d.exists(): raise ValueError('run exists, refusing overwrite')
    lock=read_text(a.lock)
    d.mkdir(parents=True)
    save_new(d/'TASK_LOCK.md',lock)
    atomic_json(d/'run.json',{'schema':1,'case':a.case,'canon_mutated':False,'created_at':now(),
       'lock':{'path':'TASK_LOCK.md','sha256':digest(lock.encode())},'drafts':[],'reviews':[]})
    print('CREATED',d,'CANON_UNTOUCHED')


def cmd_draft(a):
    d=rootdir(a); m=manifest(d)
    raw=read_text(a.file)
    if len(raw)<600: raise ValueError('not a complete scene: fewer than 600 characters')
    n=len(m['drafts'])+1; vid='V%03d'%n
    if n>1:
        parent=m['drafts'][-1]['id']
        rev=next((x for x in m['reviews'] if x['draft']==parent),None)
        if rev is None: raise ValueError('cannot revise without sourced review of parent')
        old=(d/m['drafts'][-1]['path']).read_text('utf-8')
        if raw==old: raise ValueError('revision unchanged')
    else: parent=None
    path='drafts/'+vid+'.md'
    save_new(d/path,raw)
    m['drafts'].append({'id':vid,'parent':parent,'path':path,'sha256':digest(raw.encode()),
       'hypothesis':a.hypothesis,'created_at':now(),'status':'MODEL_CANDIDATE_UNRATED'})
    atomic_json(d/'run.json',m)
    print('DRAFT',vid,len(raw),'characters','sha256='+digest(raw.encode()))


def cmd_review(a):
    d=rootdir(a); m=manifest(d)
    dr=next((x for x in m['drafts'] if x['id']==a.version),None)
    if dr is None: raise ValueError('unknown draft')
    if any(r['draft']==a.version for r in m['reviews']):
        raise ValueError('review exists, no silent overwrite')
    review=json.loads(read_text(a.file))
    if not isinstance(review.get('observations'),list) or not review['observations']:
        raise ValueError('expected at least one concrete observation')
    lines=(d/dr['path']).read_text('utf-8').splitlines()
    for i,o in enumerate(review['observations']):
        ln=o['line']; quote=o['quote']
        if not isinstance(ln,int) or not 1<=ln<=len(lines) or quote not in lines[ln-1]:
            raise ValueError('observation %d not supported by exact source line'%i)
        if not o.get('reader_cost') or not o.get('repair'):
            raise ValueError('observation must explain reader cost and repair')
    path='reviews/'+a.version+'.json'
    doc=json.dumps(review,ensure_ascii=False,indent=2)+'\n'
    save_new(d/path,doc)
    m['reviews'].append({'draft':a.version,'path':path,'sha256':digest(doc.encode()),
                         'created_at':now(),'authorship':'MODEL_REVIEW_NOT_HUMAN_RATING'})
    atomic_json(d/'run.json',m)
    print('REVIEW',a.version,len(review['observations']),'SOURCED_OBSERVATIONS')


def cmd_status(a):
    d=rootdir(a); m=manifest(d)
    assert m['canon_mutated'] is False
    print('VERIFIED',a.case,'drafts',len(m['drafts']),'reviews',len(m['reviews']),'CANON_UNTOUCHED')
    for e in m['drafts']:
        print(' ',e['id'],'parent',e['parent'],'reviewed',any(r['draft']==e['id'] for r in m['reviews']),e['status'])


def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='cmd',required=True)
    for name,fn in [('init',cmd_init),('draft',cmd_draft),('review',cmd_review),('status',cmd_status)]:
        s=sub.add_parser(name)
        s.add_argument('--root',type=Path,default=Path('training/creative_runs'))
        s.add_argument('--case',required=True)
        if name=='init': s.add_argument('--lock',type=Path,required=True)
        if name=='draft':
            s.add_argument('--file',type=Path,required=True)
            s.add_argument('--hypothesis',required=True)
        if name=='review':
            s.add_argument('--version',required=True)
            s.add_argument('--file',type=Path,required=True)
        s.set_defaults(fn=fn)
    a=p.parse_args()
    try:a.fn(a)
    except (ValueError,OSError,KeyError,json.JSONDecodeError) as e:p.exit(2,'ERROR: '+str(e)+'\n')


if __name__=='__main__': main()
