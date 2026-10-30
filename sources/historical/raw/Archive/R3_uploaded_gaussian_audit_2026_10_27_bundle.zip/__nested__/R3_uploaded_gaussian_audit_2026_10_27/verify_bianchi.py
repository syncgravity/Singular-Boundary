#!/usr/bin/env python3
"""Independent cell-by-cell Bianchi face-factor bound for the Penrose 14-face support.
Nonabelian face factors are counted WITHOUT abelian cancellations, and
conjugating paths are allowed; d is conjugation-invariant.
"""
import json
from collections import Counter
from pathlib import Path
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
root=Path(__file__).resolve().parent
def run():
 g,_=build(5.,0);W,meta=product_collar(g);Q=Q_from_seed(g,seed_support(g));R=set(range(len(W)))-Q
 V,E,F=len(g.labels),len(g.edges),len(g.faces)
 edgeindex={tuple(sorted(pair)):e for e,pair in enumerate(g.edges)}
 cells=[]
 for t in range(3):
  for f,face in enumerate(g.faces):
   p={((t+1)%3)*F+f:1,t*F+f:-1}
   for a,b in zip(face,face[1:]+face[:1]):
    e=edgeindex[tuple(sorted((a,b)))]; p[3*F+t*E+e]=1 if a<b else -1
   assert len(p)==6
   # Check ∂2∂3=0 integer exactly
   dd={}
   for fid,coef in p.items():
    for edge,s in W[fid]:dd[edge]=dd.get(edge,0)+coef*s
   assert all(v==0 for v in dd.values())
   cells.append(p)
 pending=set(Q);record=[];expanded={}
 while pending:
  opts=[]
  for j,c in enumerate(cells):
   single=set(c)&pending
   if len(single)==1:
    q=next(iter(single));opts.append((len(set(c)&Q),j,q))
  assert opts, f'unpeeled Q left {len(pending)}'
  _,j,q=min(opts);pending.remove(q);occ=Counter()
  for f in cells[j]:
   if f!=q:occ.update(expanded[f] if f in expanded else {f:1})
  assert all(x not in Q for x in occ)
  expanded[q]=occ
  record.append({'face':q,'cell':j,'noncommuting_face_factors':sum(occ.values())})
 count=Counter()
 for q,v in expanded.items():
  ell=sum(v.values());count.update({f:ell*c for f,c in v.items()})
 assert set(count).issubset(R)
 K=max(count.values());ml=max(r['noncommuting_face_factors'] for r in record)
 print('Q',len(Q),'retained distinct faces',len(count),'max face factors',ml,'Wilson coefficient',K)
 assert K==44 and ml==17 and len(count)==54
 cert={'model':'direct Z5 Penrose 14 inserted temporal faces','Q_count':len(Q),'retained_face_support':len(count),'maximum_noncommuting_factor_count':ml,'pointwise_nonabelian_Wilson_energy_coefficient':K,'justification':'Six-face prism boundary group identities express each peeled face as a product of transported (conjugated) other plaquette holonomies. Counting occurrences without abelian cancellation and using sqrt(d(AB))<=sqrt(d(A))+sqrt(d(B)) yields Σ_Q d≤44 Σ_Afill d.','steps':record}
 (root/'bianchi_certificate.json').write_text(json.dumps(cert,indent=2))
if __name__=='__main__':run()
