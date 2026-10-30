#!/usr/bin/env python3
"""Local Gaussian Schur-curvature test on a genuine Bianchi-fillable Penrose Q14.
Includes the Bianchi retained-face support, not only faces touching Q links.
"""
import json,math
from pathlib import Path
import numpy as np
from scipy.linalg import null_space
from scipy.linalg import eigvalsh
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent

def bianchi_face_support(g,words,Q):
 V,E,F=len(g.labels),len(g.edges),len(g.faces)
 eind={tuple(sorted(p)):i for i,p in enumerate(g.edges)}
 cells=[]
 for t in range(3):
  for f,vs in enumerate(g.faces):
   cell={t*F+f,((t+1)%3)*F+f}
   cell.update(3*F+t*E+eind[tuple(sorted((a,b)))] for a,b in zip(vs,vs[1:]+vs[:1]))
   cells.append(cell)
 pending=set(Q);express={}
 while pending:
  opts=[(len(c&Q),j,next(iter(c&pending))) for j,c in enumerate(cells) if len(c&pending)==1]
  assert opts,('not peelable',len(pending))
  _,j,q=min(opts);pending.remove(q)
  exp=set()
  for f in cells[j]-{q}:exp.update(express.get(f,{f}))
  assert not exp&Q
  express[q]=exp
 return set().union(*express.values())

def schur(A,B):
 # A: m faces x local links; B: m faces x boundary links
 null=null_space(A.T,rcond=1e-11)
 return (B.T@null)@(null.T@B)

def test(g,seed):
 words,_=product_collar(g)
 Q=Q_from_seed(g,seed);R=set(range(len(words)))-Q
 L={e for q in Q for e,sgn in words[q]}
 A_fill=bianchi_face_support(g,words,Q)
 assert len(A_fill)==54
 A_touch={p for p in R if any(e in L for e,sign in words[p])}
 M=sorted(A_touch|A_fill)
 Bsorted=sorted({e for p in M for e,_ in words[p] if e not in L})
 Lsorted=sorted(L)
 lid={e:i for i,e in enumerate(Lsorted)};bid={e:i for i,e in enumerate(Bsorted)}
 A=np.zeros((len(M),len(Lsorted)));B=np.zeros((len(M),len(Bsorted)))
 for i,p in enumerate(M):
  for e,sgn in words[p]:
   if e in lid:A[i,lid[e]]+=sgn
   else:B[i,bid[e]]+=sgn
 F=np.zeros((len(Q),len(Lsorted)))
 for i,q in enumerate(sorted(Q)):
  for e,sgn in words[q]:F[i,lid[e]]+=sgn
 C0=schur(A,B);C1=schur(np.vstack([A,F]),np.vstack([B,np.zeros((len(Q),len(Bsorted)))]))
 C0=(C0+C0.T)/2;C1=(C1+C1.T)/2
 delta=C1-C0
 d=np.linalg.eigvalsh(delta)
 psdtest=np.linalg.eigvalsh(45*C0-C1)
 r=int((d>1e-7).sum())
 assert d.min()>-1e-7,(d.min(),r)
 assert psdtest.min()>-5e-7,(psdtest.min(),r)
 assert r<=len(Q)
 evals=[]
 for eta,lam in [(1,1),(1,300),(.001,1)]:
  # generalized log-det ratio
  l0=np.linalg.slogdet(eta*np.eye(len(Bsorted))+lam*C0)
  l1=np.linalg.slogdet(eta*np.eye(len(Bsorted))+lam*C1)
  assert l0[0]>0 and l1[0]>0
  h=1.5*(l1[1]-l0[1]);assert h<=1.5*len(Q)*math.log(45)+1e-6
  evals.append({'eta':eta,'lambda':lam,'Schur_exterior_cost':h})
 return {'radius':float(g.xy.max()),'Q_faces':len(Q),'retained_local_faces':len(M),'retained_Bianchi_support':len(A_fill),'H_links':len(L),
       'exterior_boundary_links':len(Bsorted),'delta_rank':r,
       'delta_min_eigenvalue':float(d.min()),'largest_delta_eigenvalue':float(d.max()),
       'min_eig_45C0_minus_C1':float(psdtest.min()),'bounds':evals}

def main():
 g0,_=build(5.,0);seed=seed_support(g0)
 rows=[]
 for rad in (5.,6.5,8.,10.):
  g,_=build(rad,0);a=test(g,seed);a['radius']=rad;rows.append(a)
  print('radius',rad,'local faces',a['retained_local_faces'],'ext links',a['exterior_boundary_links'],'rank',a['delta_rank'],'Schur H beta300',a['bounds'][1]['Schur_exterior_cost'],flush=True)
 (ROOT/'local_schur_certificate.json').write_text(json.dumps({'source':'Genuine direct-Z5 Penrose rhombus disk x three-periodic time','nature':'eta regularized linear tangent model, NOT the compact SU(2) Wilson model','theorem':'If pointwise Bianchi quadratic bound S_Q<=44 S_R, then C0<=C1<=45 C0 and rank(C1-C0)<=|Q|; hence (3/2)log det((eta+lambda C1)/(eta+lambda C0))<=(3/2)|Q|log45 for all eta>0, lambda>=0, uniformly in volume.','data':rows},indent=2))
if __name__=='__main__':main()
