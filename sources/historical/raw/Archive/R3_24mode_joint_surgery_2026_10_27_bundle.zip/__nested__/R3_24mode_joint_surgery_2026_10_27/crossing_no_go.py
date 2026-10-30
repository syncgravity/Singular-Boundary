#!/usr/bin/env python3
"""Exact two-prime differential no-go for crossing-face preserving repairs.
Allows correlated variation of *all* 89 exterior halo links; not just one-link pivots.
"""
import json
from pathlib import Path
from collections import Counter
import numpy as np
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
from classify_modes import pivot_basis,link_key
ROOT=Path(__file__).resolve().parent

def nullspace_mod(M,p):
    A=np.array(M,dtype=np.int64)%p;m,n=A.shape
    rr=0;pivs=[]
    for j in range(n):
        good=np.flatnonzero(A[rr:,j]) if rr<m else np.array([])
        if len(good)==0:continue
        k=rr+int(good[0]);A[[rr,k]]=A[[k,rr]]
        A[rr]=(A[rr]*pow(int(A[rr,j]),-1,p))%p
        for i in range(m):
            if i!=rr and A[i,j]:A[i]=(A[i]-A[i,j]*A[rr])%p
        pivs.append(j);rr+=1
        if rr==m:break
    free=[j for j in range(n) if j not in pivs]
    N=np.zeros((n,len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        N[j,k]=1
        for i,pp in enumerate(pivs):N[pp,k]=(-A[i,j])%p
    assert np.all((M@N)%p==0)
    return N,len(pivs)

def rank_mod(M,p):
    mm=np.array(M,dtype=np.int64)%p;m,n=mm.shape;basis={}
    # exploit sparse pivots, use column rank
    for j in range(n):
        col={i:int(mm[i,j]) for i in range(m) if mm[i,j]}
        while col:
            t=min(col)
            if t not in basis:
                inv=pow(col[t],-1,p)
                basis[t]={i:(v*inv)%p for i,v in col.items()};break
            v=col[t]
            for i,c in basis[t].items():
                z=(col.get(i,0)-v*c)%p
                if z:col[i]=z
                else:col.pop(i,None)
    return len(basis)

def main():
 out=[]
 for radius in (5.,6.5,8.,10.):
  g,_=build(radius,0);words,_=product_collar(g);Q=Q_from_seed(g,seed_support(build(5.,0)[0]));R=set(range(len(words)))-Q
  H=sorted({e for q in Q for e,s in words[q]});A=sorted(f for f in R if any(e in H for e,s in words[f]));E=sorted({e for f in A for e,s in words[f]}-set(H));C=sorted(f for f in R if f not in A and any(e in E for e,s in words[f]))
  def mat(fs,es):
    ind={e:j for j,e in enumerate(es)};m=np.zeros((len(fs),len(es)),dtype=np.int64)
    for i,f in enumerate(fs):
      for e,s in words[f]:
        if e in ind:m[i,ind[e]]+=s
    return m
  D_H=mat(A,H);D_A=mat(A,E);D_cross=mat(C,E)
  result=[]
  for p in (1000003,1000033):
    N,r_cross=nullspace_mod(D_cross,p)
    old=rank_mod(D_H,p)
    r_plain=rank_mod(np.column_stack((D_H,D_A)),p)-old
    r_safe=rank_mod(np.column_stack((D_H,(D_A@N)%p)),p)-old
    result.append({'prime':p,'local_rank':old,'unrestricted_exterior_rank':r_plain,'crossing_fixed_exterior_rank':r_safe,'crossing_constraint_rank':r_cross,'crossing_fixed_available_free_tangents':len(E)-r_cross})
  assert result[0]=={**result[1],'prime':1000003}
  out.append({'radius':radius,'H_links':len(H),'A_faces':len(A),'exterior_links':len(E),'crossing_retained_faces':len(C),'results':result})
  print('radius',radius,'crossing',len(C),'rank allowed',result[0]['crossing_fixed_exterior_rank'],'of 24','nullity',result[0]['crossing_fixed_available_free_tangents'],flush=True)
 (ROOT/'crossing_no_go_certificate.json').write_text(json.dumps({'scope':'Exact linearization at the fully flat connection; strong restriction of any smooth correlated surgery that preserves all crossing plaquette holonomies while changing only H and its immediate 89-link halo. Does NOT rule out repairs that also change crossing plaquettes or links in an enlarged collar.','results':out},indent=2))
if __name__=='__main__':main()
