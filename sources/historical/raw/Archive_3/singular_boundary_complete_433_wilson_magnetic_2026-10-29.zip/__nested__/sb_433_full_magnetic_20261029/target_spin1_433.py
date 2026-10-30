"""Exact spin-one target-character compression in the complete 433 state spin 1/2 shell."""
from pathlib import Path
import runpy
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from itertools import product
import opt_einsum as oe
from math import sqrt
S=runpy.run_path(str(Path(__file__).resolve().parent/'build_433_exact.py'))
faces=S['faces'];target=S['target'];edges=S['edges'];verts=S['verts'];vedges=S['vedges'];faceidx=S['faceidx'];states=S['states'];local=S['local'];tensors=S['tensors'];groups=S['groups'];EPS=S['EPS'];T4=[S['T4a'],S['T4b']];retained=S['retained'];magmat=S['magmat'];K=S['K'];c=S['c'];
qmask=faceidx[target]
all4=[(mask&qmask)==qmask for s,mask,_ in states]
print('all-target4 span',sum(all4))

# four-fundamental Haar integral: int U U U U = sum_A I_A(out) I_A(in).
# Convert first (bra) spin into its complex-conjugate representation with EPS.
L4=[]
for A in T4:
 L4.append(np.tensordot(EPS,A,axes=(1,0)))
# Check direct SU2 group moments using Haar 4th projector.
I4=np.einsum('aijkl,amnop->ijklmnop',np.stack(T4),np.stack(T4))
# Each U_00 at q=1? E[U_00^4] =1/3 for uniform SU2 quaternion (complex moment zero? U_00=a+ib, E[(a+ib)^4]=0!)
# Instead test |U00|^4 = E[U00 U00 barU00 barU00]=1/3
mom=sum(AA[0,0,0,1]**2 for AA in L4)
assert abs(4*mom-4/3)<1e-12,4*mom

# q loop state uses normalized fundamental links, two independent copies.
loopdata={v:tensors(v,[e for e in vedges[v] if (qmask>>e)&1])[0] for v in verts}
qedges=[e for e in range(len(edges)) if (qmask>>e)&1]
vertsq=[v for v in verts if any((qmask>>e)&1 for e in vedges[v])]

def site_4(v, bra, ket, alphas):
 bm=states[bra][1];km=states[ket][1]
 bs=[e for e in vedges[v] if (bm>>e)&1];ks=[e for e in vedges[v] if (km>>e)&1];ls=[e for e in vedges[v] if (qmask>>e)&1]
 A=local[bra][v];B=local[ket][v];L=loopdata[v]
 tensorss=[A,B,L,L];indices=[[],[],[],[]];lab=0
 for e in vedges[v]:
  if (qmask>>e)&1:
   occ=[(bm>>e)&1,(km>>e)&1,1,1]
   assert occ==[1,1,1,1],occ
   for k in range(4):indices[k].append(lab+k)
   tensorss.append(2*L4[alphas[e]])
   indices.append(list(range(lab,lab+4)));lab+=4
  elif (bm>>e)&1:
   assert (km>>e)&1
   indices[0].append(lab);indices[1].append(lab+1)
   tensorss.append(np.eye(2));indices.append([lab,lab+1]);lab+=2
 inp=[]
 for ten,ind in zip(tensorss,indices):inp.extend([ten,ind])
 inp.append([])
 return float(oe.contract(*inp,optimize='greedy'))

# Compute operator P chi1(Wf) P = P (chi_half^2-1) P; only all4 mask blocks nonzero.
entries=[]
for sub,ids in groups.items():
 sel=[i for i in ids if all4[i]]
 if not sel:continue
 for i in sel:
  for j in sel:
   if i<j:continue
   ans=0.
   for vs in product((0,1),repeat=4):
    alphas=dict(zip(qedges,vs));val=1.
    for v in vertsq:
     val*=site_4(v,i,j,alphas)
     if abs(val)<1e-14:break
    ans+=val
   if i==j:ans-=1.
   if abs(ans)>1e-10:
    entries.append((i,j,ans))
    if i!=j:entries.append((j,i,ans))
idx=np.array([[i,j] for i,j,x in entries]);data=np.array([x for i,j,x in entries]);C=coo_matrix((data,(idx[:,0],idx[:,1])),shape=(433,433)).tocsr()
print('target chi1 operator nnz',C.nnz,'norm',np.linalg.norm(C.toarray(),ord=2),'eigen span min max',np.linalg.eigvalsh(C[np.ix_(np.where(all4)[0],np.where(all4)[0])].toarray())[[0,-1]])
assert np.max(np.abs(C.toarray()-C.toarray().T))<1e-10
# reconstruct witness loop inner*outer as basis vector in subspace mask of 16 occupied links.
# At each four-valent vertex, pair inner and outer loop singlets, then convert incoming index using EPS.
star={target,(1,0),(2,1),(1,2),(0,1)}
from collections import Counter
star_edges=Counter(e for f in star for e in [k for k in range(len(edges)) if faceidx[f]>>k&1])
inner=set(qedges);outer={e for e,n in star_edges.items() if n==1};union=inner|outer
maskstar=sum(1<<e for e in union)
substar=next(sub for sub,ids in groups.items() if states[ids[0]][1]==maskstar)
w=np.zeros(433)
for idx in groups[substar]:
 prod_val=1.
 for v in verts:
  es=[e for e in vedges[v] if e in union]
  if len(es)==0:continue
  # witness intertwiner tensor at v is product of two loop singlets in matching edge orientations
  if len(es)==2:T=S['singlet'].copy()
  elif len(es)==4:
   ins=[k for k,e in enumerate(es) if e in inner];outs=[k for k,e in enumerate(es) if e in outer]
   T=np.empty([2]*4)
   for ar in product(range(2),repeat=4):T[ar]=S['singlet'][ar[ins[0]],ar[ins[1]]]*S['singlet'][ar[outs[0]],ar[outs[1]]]
  else:raise RuntimeError('unexpected degree')
  for ax,e in enumerate(es):
   if edges[e][1]==v:
    T=np.tensordot(EPS,T,axes=(1,ax));T=np.moveaxis(T,0,ax)
  prod_val*=float(np.vdot(local[idx][v],T).real)
 w[idx]=prod_val
print('witness expansion norm',np.linalg.norm(w),'c1',w@C@w,'index support',np.sum(abs(w)>1e-12))
assert abs(np.linalg.norm(w)-1)<1e-10
assert abs(w@C@w-1)<1e-10

from scipy.sparse import diags
for b in (1,4,16,64):
 H=diags(K+b*sum(c))
 for ci,q in zip(c,retained): H=H-b*ci*magmat[faces.index(q)]
 eig,U=eigsh(H,k=4,which='SA',tol=1e-12,maxiter=100000)
 v=U[:,0];p=float(v@C@v)
 wgt=float(np.sum(v[np.array(all4)]**2))
 print('b',b,'ritz c1',p,'p2',(1+p)/4,'target4 weight',wgt,'ratio c1/w',p/wgt,flush=True)
 assert abs(p)<=3*wgt+1e-12
 np.savez_compressed(str(Path(__file__).resolve().parent/f'ritz_b_{b}_c1.npz'),evals=eig,vector=v,chi1=p,target_four_weight=wgt)
from scipy.sparse import save_npz
save_npz(str(Path(__file__).resolve().parent/'target_spin1.npz'),C)
print('PASS exact compressed target spin1 and winding witness')
