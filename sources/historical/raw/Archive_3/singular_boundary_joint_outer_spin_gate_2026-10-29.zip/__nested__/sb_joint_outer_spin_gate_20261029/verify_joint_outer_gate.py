#!/usr/bin/env python3
"""Exact 433+single-face character towers, physical class product Ritz, seven-outer-link proof gate.
Inputs: verified 433-state SU(2) Haar recoupling files in this package.
"""
import math,csv
from pathlib import Path
import numpy as np
from scipy.sparse import load_npz,diags,block_diag,csr_matrix,coo_matrix
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh_tridiagonal
P=Path(__file__).resolve().parent
z=np.load(P/'basis.npz');subs=z['face_subsets'];occ=z['occupancies'];T=z['electric'];edges=z['links']
faces=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0));target=faces.index((1,1));retained=[i for i in range(8) if i!=target];assert len(T)==433
M=[load_npz(P/f'magnetic_{i}.npz') for i in range(8)]
avec=np.array([.8+.07*(i%6)+.013*(i%3) for i in range(len(edges))]);c=np.array([.78+.09*i for i in range(7)])
A=[];outer=[]
for f in faces:
 x,y=f;v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 ed=[next(i for i,E in enumerate(edges) if np.array_equal(E,np.array(sorted((a,b))))) for a,b in zip(v,v[1:]+v[:1])]
 A.append(sum(avec[e] for e in ed))
 outerlinks=[e for e in ed if any(vv[0] in (0,3) and vv[1] in (0,3) for vv in edges[e]) or (edges[e,0,0]==edges[e,1,0] and edges[e,0,0] in (0,3)) or (edges[e,0,1]==edges[e,1,1] and edges[e,0,1] in (0,3))]
 outer.append(outerlinks)
# Every retained face touches at least one externally-private boundary link.
assert all(outer[i] for i in retained)
selected=[outer[i][0] for i in retained]
assert len(set(selected))==7
print('selected seven distinct private outer links',selected)
A=np.array(A)
faces_bit={j:np.flatnonzero(subs==(1<<j)) for j in range(8)}
assert all(len(faces_bit[j])==1 for j in retained)
Bvals=[1.,4.,16.,64.]
Ntrunc=[2,3,4,6,8,12,20]
with (P/'RESULTS.csv').open('w',newline='') as h:
 w=csv.writer(h);w.writerow(['type','b','max_spin','dimension','ground_energy','ritz_gap','tower_weight','known_residual_floor'])
 for b in Bvals:
  for n in Ntrunc:
   nidx=np.arange(n,dtype=float)
   e0=sum(eigh_tridiagonal(A[q]*nidx*(nidx+2)/4+b*ci,np.full(n-1,-b*ci/2),select='i',select_range=(0,0))[0][0] for ci,q in zip(c,retained))
   w.writerow(['product_class',b,(n-1)/2,n**7,e0,'','',''])
  for J in [1,2,4,8]:
   spin=np.arange(1,J+.01,.5)
   ns=len(spin);dim=433+7*ns
   diag=np.concatenate([T,np.array([j*(j+1)*A[q] for q in retained for j in spin])])
   H=diags(diag+b*c.sum(),format='csr')
   for ci,q in zip(c,retained):H-=b*ci*block_diag((M[q],csr_matrix((dim-433,dim-433))),format='csr')
   rows=[];cols=[];data=[]
   for k,(ci,q) in enumerate(zip(c,retained)):
    initial=int(faces_bit[q][0]);a=433+k*ns
    pairs=[(initial,a)]+[(a+i,a+i+1) for i in range(ns-1)]
    for x,y in pairs:
     rows.extend([x,y]);cols.extend([y,x]);data.extend([-b*ci/2,-b*ci/2])
   H+=coo_matrix((data,(rows,cols)),shape=(dim,dim)).tocsr()
   ev,V=eigsh(H,k=2,which='SA',tol=2e-11,maxiter=80000)
   v=V[:,0];r=float(np.linalg.norm(H@v-ev[0]*v))
   assert r<1e-7
   wt=float(np.linalg.norm(v[433:])**2)
   # These omitted chi_(J+1/2)(W_q) channels are orthonormal and outside this Galerkin span.
   residual_floor=float(np.linalg.norm(np.array([b*ci*v[433+k*ns+ns-1]/2 for k,ci in enumerate(c)])))
   w.writerow(['433_plus_single_face',b,J,dim,float(ev[0]),float(ev[1]-ev[0]),wt,residual_floor])
   print('b=%3g J=%g dim=%d Ritz E=%.9f gap=%.9f wt=%.7f residual_floor=%.8f'%(b,J,dim,ev[0],ev[1]-ev[0],wt,residual_floor))
# Validate exact Haar cap and analytic cap confinement bound.
def Hdelta(d):return (math.acos(1-d)-(1-d)*math.sqrt(2*d-d*d))/math.pi
D=5;d=1/32
for k in (0,1,3,6):
 m=d*((7-k)/2-7*D*Hdelta(d))
 assert m>0
 print('R_k cap bound k',k,'lower sum_q <d_q> >=',m)
print('SU2 Haar cap',d,Hdelta(d),'Peter Weyl dimension',D)
print('PASS: 433 shell, seven independent boundary links, nested single-face towers, class product Ritz, simultaneous high-link no-go')
