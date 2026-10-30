import numpy as np
from collections import defaultdict,Counter
from itertools import product
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import eigsh
import opt_einsum as oe
from time import time

EPS=np.array([[0.,1.],[-1.,0.]])
E=EPS
faces=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
target=(1,1);retained=[x for x in faces if x!=target]
verts=sorted({v for x,y in faces for v in [(x,y),(x+1,y),(x+1,y+1),(x,y+1)]})
edges=sorted({tuple(sorted((a,b))) for x,y in faces for a,b in zip([(x,y),(x+1,y),(x+1,y+1),(x,y+1)],[(x+1,y),(x+1,y+1),(x,y+1),(x,y)])})
ei={e:i for i,e in enumerate(edges)}
faceidx={f:sum(1<<ei[tuple(sorted((a,b)))] for a,b in zip([(f[0],f[1]),(f[0]+1,f[1]),(f[0]+1,f[1]+1),(f[0],f[1]+1)],[(f[0]+1,f[1]),(f[0]+1,f[1]+1),(f[0],f[1]+1),(f[0],f[1])])) for f in faces}
vedges={v:sorted(ei[e] for e in edges if v in e) for v in verts}

# T rank2 and rank4 bases, normalized tensor Euclidean
singlet=EPS/np.sqrt(2.)
def pairing(pairs):
 out=np.empty([2]*4)
 for a in product(range(2), repeat=4):
  out[a]=np.prod([singlet[a[i],a[j]] for i,j in pairs])
 return out
T4a=pairing([(0,1),(2,3)])
T4b=pairing([(0,2),(1,3)])
T4b=T4b-T4a*np.sum(T4a*T4b)
T4b/=np.linalg.norm(T4b)
assert abs(np.sum(T4a*T4b))<1e-12

def tensors(v,active):
 n=len(active)
 if n==0:return [np.array(1.)]
 if n==2: T=[singlet]
 elif n==4:T=[T4a,T4b]
 else:raise ValueError(n)
 out=[]
 for ten in T:
  for axis,idx in enumerate(active):
   if edges[idx][1]==v:
    # incoming index conversion E_{j k} T_k
    ten=np.tensordot(E,ten,axes=(1,axis));ten=np.moveaxis(ten,0,axis)
  out.append(ten)
 return out

# states per mask (mask 22 bits) indexed by face subset xor cycles
states=[];groups={};local={}
for sub in range(1<<len(faces)):
 mask=0
 for i,f in enumerate(faces):
  if (sub>>i)&1:mask ^=faceidx[f]
 loc_opts={v:tensors(v,[e for e in vedges[v] if (mask>>e)&1]) for v in verts}
 options=[(v,len(ts)) for v,ts in loc_opts.items() if len(ts)>1]
 for choices in product(*[range(n) for v,n in options]):
  c=dict(zip([v for v,n in options],choices))
  sid=len(states);states.append((sub,mask,c))
  groups.setdefault(sub,[]).append(sid)
  local[sid]={v:loc_opts[v][c.get(v,0)] for v in verts}
assert len(states)==433
print('states 433, masks',len(groups),flush=True)

# local factor calculate contracted bra*ket*loop vertex tensors
# construct edge contractions at vertex, by pair of named tensors.
def localfactor(v, sid_bra, sid_ket, loop_mask):
  # in q-untouched vertex, identical occupancy, orthonormal basis => delta
  if all(not (loop_mask>>e)&1 for e in vedges[v]):
   return 1. if states[sid_bra][2].get(v,0)==states[sid_ket][2].get(v,0) else 0.
  bra_mask=states[sid_bra][1];ket_mask=states[sid_ket][1]
  vb=[e for e in vedges[v] if (bra_mask>>e)&1]
  vk=[e for e in vedges[v] if (ket_mask>>e)&1]
  vl=[e for e in vedges[v] if (loop_mask>>e)&1]
  A=local[sid_bra][v];B=local[sid_ket][v];L=tensors(v,vl)[0]
  tensorss=[A,B,L];indices=[[],[],[]];connect=[];lab=0
  for e in vedges[v]:
   occ=[(bra_mask>>e)&1,(ket_mask>>e)&1,(loop_mask>>e)&1]
   if sum(occ)==0:continue
   if sum(occ)!=2: return 0.
   axes=[]
   for k,on in enumerate(occ):
    if on:
     axes.append(k)
     indices[k].append(lab if len(axes)==1 else lab+1)
   # if bra and ket, or bra and loop: delta; else ket and loop => epsilon
   mat=E if axes==[1,2] else np.eye(2)
   tensorss.append(mat);indices.append([lab,lab+1]);lab+=2
  args=[]
  for arr,ii in zip(tensorss,indices):args.extend([arr,ii])
  args.append([])
  res=oe.contract(*args,optimize='greedy')
  return float(res)

# compute loop sign at identity, from product local singlets and contraction per link
# For simple closed plaquette with normalized link D, trace at I equals 2.
def loop_at_identity(qmask):
 ten=[];idxs=[];labels={};
 for v in verts:
  active=[e for e in vedges[v] if (qmask>>e)&1]
  if not active: continue
  T=tensors(v,active)[0];labels[v,tuple(active)]=0
  ten.append(T);idxs.append([(e,v) for e in active])
 # each edge link sqrt2*I, contract origin/dest indices
 for e in range(len(edges)):
  if (qmask>>e)&1:
   u,w=edges[e];ten.append(np.sqrt(2.)*np.eye(2));idxs.append([(e,u),(e,w)])
 index={k:i for i,k in enumerate({z for ii in idxs for z in ii})}
 inp=[]
 for t,ii in zip(ten,idxs):inp.extend([t,[index[z] for z in ii]])
 return float(oe.contract(*inp,[],optimize='greedy'))

lsgn={q:2/loop_at_identity(faceidx[q]) for q in faces}
print('loop signs',lsgn,flush=True)
assert all(abs(abs(x)-1)<1e-10 for x in lsgn.values())

# build sparse matrix magnetic p_q, each sub to sub xor face coordinate
magmat=[]
for q in faces:
 qbit=1<<faces.index(q);qmask=faceidx[q]
 rows=[];cols=[];dat=[]
 t0=time()
 for sub,srcids in groups.items():
  destids=groups[sub^qbit]
  if sub>sub^qbit:continue
  for sr in srcids:
   for de in destids:
    val=lsgn[q]
    for v in verts:
     if any((qmask>>e)&1 for e in vedges[v]):
      val*=localfactor(v,de,sr,qmask)
      if abs(val)<1e-14:break
     elif states[de][2].get(v,0)!=states[sr][2].get(v,0):val=0;break
    val*=.5
    if abs(val)>1e-12:
     rows.extend([de,sr]);cols.extend([sr,de]);dat.extend([val,val])
 M=coo_matrix((dat,(rows,cols)),shape=(433,433)).tocsr()
 print('q',q,'nnz',M.nnz,'valminmax',M.data.min() if M.nnz else 0,M.data.max() if M.nnz else 0,'time',round(time()-t0,2),flush=True)
 magmat.append(M)

# vacuum to plaquette char matrix entry should 1/2 for p_q, and vacuum p_q vacuum=0
vac=groups[0][0]
for q,M in zip(faces,magmat):
 assert abs(np.linalg.norm(M[:,vac].toarray())-.5)<1e-10,(q,np.linalg.norm(M[:,vac].toarray()))
print('matrix block validated vacuum to pure chi loop',flush=True)

# occupancy electrical energies
avec=np.array([.8+.07*(i%6)+.013*(i%3) for i in range(len(edges))]);K=np.array([.75*sum(avec[e] for e in range(len(edges)) if (mask>>e)&1) for sub,mask,c in states])
c=np.array([.78+.09*i for i,q in enumerate(retained)])
# Build operator and eigen values
for b in (1,4,16,64):
 H=diags(K+b*sum(c))
 for c_i,q in zip(c,retained):H=H-b*c_i*magmat[faces.index(q)]
 eig,V=eigsh(H,k=4,which='SA',tol=1e-10,maxiter=100000)
 j=np.argmin(eig);v=V[:,j];
 y=np.array([(-1 if (sub>>faces.index(target))&1 else 1) for sub,mask,t in states]);
 purity=np.vdot(v,y*v).real
 energy_bound=sum(3/(2*np.sqrt(2))*np.sqrt(sum(avec[e] for e in range(len(edges)) if (faceidx[q]>>e)&1)*b*c_i) for c_i,q in zip(c,retained))
 
 # Target center+ response is restricted to masks occupying all four target edges.
 mask_target=faceidx[target]
 full=np.array([((mask&mask_target)==mask_target) for sub,mask,_ in states]);fullweight=np.linalg.norm(v[full])**2
 m_target=magmat[faces.index(target)]
 # p_f compressed: norm supplies a rigorous lower bound on the target second moment in this Ritz state.
 proj_p2=np.linalg.norm(m_target@v)**2
 # Seven exact omitted spin1 channels give rigorous lower bound on outgoing residual.
 res2=0.
 for ci,q in zip(c,retained):
  idx=groups[1<<faces.index(q)][0]
  res2+=(b*ci*v[idx]/2.)**2
 print('b',b,'eigs',eig,'gap',eig[1]-eig[0],'center parity',purity,'true E upper',energy_bound,'p2_projected',proj_p2,'target4_weight',fullweight,'residual_floor',np.sqrt(res2),flush=True)
 out=__import__('pathlib').Path('/mnt/data/sb_433_exact_mag');out.mkdir(exist_ok=True)
 np.savez(out/f'ritz_b_{b:g}.npz',evals=eig,v=v,projected_target_p2=proj_p2,target_all_four_weight=fullweight,residual_lower=np.sqrt(res2))

from pathlib import Path
import json
out=Path(__file__).resolve().parent;out.mkdir(exist_ok=True)
from scipy.sparse import save_npz
for i,m in enumerate(magmat): save_npz(out/f'magnetic_{i}.npz',m)
np.savez_compressed(out/'basis.npz',occupancies=np.array([s[1] for s in states],dtype=np.int64),face_subsets=np.array([s[0] for s in states]),electric=K,links=np.array(edges))
print('DONE',flush=True)
