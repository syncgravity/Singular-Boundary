#!/usr/bin/env python3
"""Exact free-word algebra and quaternion SU(2) evaluations for generated candidates."""
import json,hashlib,numpy as np
from pathlib import Path
from certificate import invert,reduce,build_spacetime,label_face
ROOT=Path(__file__).resolve().parent

def qm(a,b):
 return np.array([a[0]*b[0]-np.dot(a[1:],b[1:]),*(a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:]))])
def dag(a):return a*np.array([1,-1,-1,-1])
def mul(U,w):
 a=np.array([1.,0.,0.,0.])
 for e,s in w:a=qm(a,U[e] if s==1 else dag(U[e]))
 return a

reports={};rng=np.random.default_rng(271828)
for volume in ['5','6_5','8','10']:
 fp=ROOT/f'certificate_radius_{volume}.json';j=json.loads(fp.read_text());W=j['words_all'];H=j['H'];Q=set(j['Q']);R=set(range(len(W)))-Q
 assert len(Q)==14
 assert all(len(w)==4 and len({e for e,s in w})==4 for w in W)
 assert all(s in (-1,1) for w in W for _,s in w)
 assert all(not reduce(w+invert(w)) for w in W)
 seen=set()
 for q in Q:
  for e,s in W[q]:seen.add(e)
 assert sorted(seen)==H
 A=sorted(p for p in R if any(e in seen for e,s in W[p])); assert A==j['A']
 S=sum(1 for e in H if str(e) not in j['star_words'] or not j['star_words'][str(e)])
 maxdiff=0.;maxcyc=0.;total_pairs=0
 n=max(e for w in W for e,s in w)+1
 U=rng.normal(size=(n,4));U/=np.linalg.norm(U,axis=1)[:,None]
 for e in H:
  star=j['star_words'][str(e)]
  for item in star:
   f=item['face'];a=mul(U,item['staple_word']);w=mul(U,W[f]);
   # cyclic quaternion trace = scalar part of U_e dot a; energy =1-dot
   d=abs(float(w[0])-float(np.dot(U[e],a)));maxcyc=max(maxcyc,d)
  for item in j['pair_staple_loop_words'][str(e)]:
   f1,f2=item['faces'];sa=next(x['staple_word'] for x in star if x['face']==f1);sb=next(x['staple_word'] for x in star if x['face']==f2)
   actual=qm(mul(U,sa),dag(mul(U,sb)));word=mul(U,item['loop_word']);
   err=np.max(np.abs(actual-word));maxdiff=max(maxdiff,float(err));total_pairs+=1
 assert maxcyc<1e-12 and maxdiff<1e-12,(maxcyc,maxdiff)
 reports[volume]={'faces_Q':len(Q),'local_H':len(H),'affected_R_faces':len(A),'H_links_with_no_retained_incident_faces':S,
      'pair_staple_loop_words_checked':total_pairs,'max_cycle_trace_err':maxcyc,'max_pair_word_quaternion_err':maxdiff,
      'peeling_success':j['Bianchi_peel']['success']}
 print(volume,reports[volume])
(ROOT/'verification.json').write_text(json.dumps(reports,indent=2))
