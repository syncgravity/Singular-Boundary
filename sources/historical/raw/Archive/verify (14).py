import numpy as np,json
from pathlib import Path
root=Path(__file__).resolve().parent
old=np.load('/mnt/data/R3_two_step_periodic_transfer_2026_10_27/incidence.npz')
B1=old['spatial_d1'];B2=old['spatial_d2']
report={}
for n in (3,4):
 nv=9*n;ne=21*n;nf=16*n;nc=4*n
 d1=np.zeros((nv,ne),dtype=np.int8);d2=np.zeros((ne,nf),dtype=np.int8);d3=np.zeros((nf,nc),dtype=np.int8)
 he=lambda t,e:12*t+e
 ve=lambda t,v:12*n+9*t+v
 sf=lambda t,f:4*t+f
 tf=lambda t,e:4*n+12*t+e
 cell=lambda t,f:4*t+f
 for t in range(n):
  nxt=(t+1)%n
  d1[t*9:(t+1)*9,t*12:(t+1)*12]=B1
  for v in range(9):d1[t*9+v,ve(t,v)]-=1;d1[nxt*9+v,ve(t,v)]+=1
  for f in range(4):d2[t*12:(t+1)*12,sf(t,f)]=B2[:,f]
  for e in range(12):
   d2[he(t,e),tf(t,e)]+=1;d2[he(nxt,e),tf(t,e)]-=1
   for v in range(9):d2[ve(t,v),tf(t,e)]+=B1[v,e]
  for f in range(4):
   d3[sf(nxt,f),cell(t,f)]+=1;d3[sf(t,f),cell(t,f)]-=1
   for e in range(12):d3[tf(t,e),cell(t,f)]+=B2[e,f]
 assert not np.any(d1.astype(int)@d2.astype(int))
 assert not np.any(d2.astype(int)@d3.astype(int))
 # integer rank by modular Gaussian elimination, no floating ambiguity
 def rank_mod(A,p=1000003):
  a=A.astype(np.int64)%p;r=0
  for c in range(a.shape[1]):
   hit=np.flatnonzero(a[r:,c]);
   if not len(hit):continue
   k=r+hit[0];a[[r,k]]=a[[k,r]];a[r]=(a[r]*pow(int(a[r,c]),-1,p))%p
   for i in range(r+1,a.shape[0]):
    if a[i,c]:a[i]=(a[i]-a[i,c]*a[r])%p
   r+=1
   if r==a.shape[0]:break
  return r
 ranks=[rank_mod(d) for d in (d1,d2,d3)]
 assert ranks==[9*n-1,12*n,4*n],ranks
 np.savez_compressed(root/f'incidence_{n}step.npz',d1=d1,d2=d2,d3=d3,spatial_d1=B1,spatial_d2=B2)
 report[str(n)]={'vertices':nv,'edges':ne,'faces':nf,'prisms':nc,'spatial_faces':4*n,'temporal_faces':12*n,'boundary_ranks':ranks,'chain_products_zero':True}
# Generic finite-dimensional PSD obstruction to extending pairwise Loewner trace proof to 3 steps
F=np.array([[.32328931,.38289268,.05443869],[.38289268,.76106876,-.16454553],[.05443869,-.16454553,.19296188]])
b=np.array([1,.02102904,.05867105]);c=np.array([1,.625239,.40334433]);B=np.diag(b);C=np.diag(c)
D=np.diag([0,0,1]);derivative=float(np.trace(F@D@F@B@F@C))
assert np.linalg.eigvalsh(F).min()>0 and derivative <0
report['abstract_nonmonotonicity_3step']={'F':F.tolist(),'K2_diagonal':b.tolist(),'K3_diagonal':c.tolist(),'DeltaK1_diagonal':[0,0,1],'derivative_trace':derivative,'F_eigenvalues':np.linalg.eigvalsh(F).tolist(),'warning':'finite-dimensional PSD example; NOT verified realization by Wilson temporal kernels'}
(root/'certificate.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
