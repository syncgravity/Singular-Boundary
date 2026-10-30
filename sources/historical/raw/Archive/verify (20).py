"""Exact compact-Haar tests: 3x3 planar disk, one closed quadrilateral prism,
     and a rank-changing 3-step incidence linearized-vs-nonlinear symmetry audit.
"""
import numpy as np, json
from scipy.special import ive
from scipy.linalg import null_space
from scipy.stats import vonmises_fisher
from pathlib import Path
P=Path(__file__).resolve().parent

# ----- 3 x 3 planar disk: chosen interior face has no original free edge.
n=3
vertices=lambda x,y:y*(n+1)+x
edge_idx={};edges=[]
for y in range(n+1):
 for x in range(n):
  a=vertices(x,y);b=vertices(x+1,y);edge_idx[tuple(sorted((a,b)))]=len(edges);edges.append((a,b))
for x in range(n+1):
 for y in range(n):
  a=vertices(x,y);b=vertices(x,y+1);edge_idx[tuple(sorted((a,b)))]=len(edges);edges.append((a,b))
B1=np.zeros(((n+1)**2,len(edges)),dtype=int)
for e,(a,b) in enumerate(edges):B1[a,e]=-1;B1[b,e]=1
B2=np.zeros((len(edges),n*n),dtype=int)
for y in range(n):
 for x in range(n):
  face=y*n+x;cyc=[vertices(x,y),vertices(x+1,y),vertices(x+1,y+1),vertices(x,y+1)]
  for a,b in zip(cyc,cyc[1:]+cyc[:1]):
   e=edge_idx[tuple(sorted((a,b)))];B2[e,face]=1 if edges[e]==(a,b) else -1
assert not (B1@B2).any() and len(edges)==24
center=4
assert all(np.sum(B2[e]!=0)==2 for e in np.flatnonzero(B2[:,center]))
assert np.linalg.matrix_rank(B2)==9 and np.linalg.matrix_rank(np.delete(B2,center,axis=1))==8
remaining=set(range(9)); peeling=[]
while remaining:
 choices=[]
 for f in sorted(remaining):
  if f==center and len(remaining)>1: continue
  for e in np.flatnonzero(B2[:,f]):
   if sum(B2[e,g]!=0 for g in remaining)==1:choices.append((f,int(e)))
 assert choices,(remaining,peeling)
 f,e=choices[0];peeling.append([int(f),int(e)]);remaining.remove(f)
assert peeling[-1][0]==center and len(set(e for f,e in peeling))==9

# ----- 3D single prism as closed sphere, extracted exactly from prior incidence.
z=np.load('/mnt/data/R3_local_conditional_2026_10_27/incidence.npz')
d1=z['d1'];d2=z['d2'];spB2=z['spatial_d2'];d3=np.zeros((48,12),dtype=int)
for tt in range(3):
 nxt=(tt+1)%3
 for ff in range(4):
  d3[12+12*tt:12+12*(tt+1),4*tt+ff]=spB2[:,ff]
  d3[4*nxt+ff,4*tt+ff]+=1
  d3[4*tt+ff,4*tt+ff]-=1
assert not (d2@d3).any()
faces=np.flatnonzero(d3[:,0]);links=np.flatnonzero(np.any(d2[:,faces]!=0,axis=1))
verts=np.flatnonzero(np.any(d1[:,links]!=0,axis=1))
assert (len(verts),len(links),len(faces))==(8,12,6)
assert not (d1@d2).any() and not (d2@d3).any()
assert np.linalg.matrix_rank(d2[np.ix_(links,faces)])==5
assert all(np.sum(d3[f,:]!=0)>=1 for f in faces)

# SU2 sphere character formula for 6 plaquettes on one closed oriented cell.
def q(t):return 1. if t==0 else float(2*ive(1,t)/t)
def r(n,t):return float((n==0) if t==0 else ive(n+1,t)/ive(1,t))
def sphere_insert(beta,cutoff=400):
 # beta list six positive couplings; return normalized sphere correction.
 s=0.
 for nspin in range(cutoff):
  term=(nspin+1)**2*np.prod([r(nspin,t) for t in beta])
  s+=term
  if nspin>40 and term<1e-15:break
 return float(s)
rows=[]
for lam in [0.5,1.,3.,10.,30.,100.,300.,1000.]:
 allbeta=[lam]*6
 corr=sphere_insert(allbeta)
 ratio=q(lam)*corr  # baseline five retained, q*...; denominator correction 1 exactly.
 assert ratio>=q(lam)-1e-12 and ratio<=1.+1e-10
 rows.append({'lambda':lam,'single_face_q':q(lam),'sphere_correction':corr,'exact_insertion_ratio':ratio,'expected_large_lambda':6**(-1.5)})

# independent SU(2) vMF samples confirm one-prism formula at moderate beta
rng=np.random.default_rng(20261027)
def mul(x,y):
 a,b=x[...,0],y[...,0];u,v=x[...,1:],y[...,1:]
 return np.concatenate([(a*b-(u*v).sum(axis=-1))[...,None],a[...,None]*v+b[...,None]*u+np.cross(u,v)],axis=-1)
mc=[]
for lam in [1.,3.,10.,30.]:
 count=60000
 x=vonmises_fisher.rvs([1,0,0,0],kappa=lam,size=(5,count),random_state=rng)
 word=np.zeros((count,4));word[:,0]=1
 for k in range(5):word=mul(word,x[k])
 vals=np.exp(-lam*(1-word[:,0]));estimate=float(vals.mean());sem=float(vals.std(ddof=1)/np.sqrt(count))
 formula=q(lam)*sphere_insert([lam]*6)
 assert abs(estimate-formula)<5*sem+0.001,(lam,estimate,formula,sem)
 mc.append({'lambda':lam,'n':count,'mean':estimate,'se':sem,'exact':formula,'zscore':(estimate-formula)/sem})

# Relative linear null-vector for rank-changing eight-face support: does NOT produce nonlinear symmetry automatically.
Q=np.array([13,18,22,25,26,29,32,37],dtype=int)
R=np.setdiff1d(np.arange(d2.shape[1]),Q)
individually_free_edges=np.flatnonzero(np.any(d2[:,Q]!=0,axis=1)&~np.any(d2[:,R]!=0,axis=1))
assert len(individually_free_edges)==0
U=null_space(d2[:,R].T,rcond=1e-12);V=null_space(d2.T,rcond=1e-12)
project=U@U.T-V@V.T
qface=25;t=project@d2[:,qface].astype(float)
t/=np.linalg.norm(t)
assert np.linalg.norm(d2[:,R].T@t)<1e-9
assert np.linalg.norm(d2[:,Q].T@t)>1e-4
# Orient square face words consistently for each face. Starting at lowest incident vertex.
def word(f):
 es=list(map(int,np.flatnonzero(d2[:,f])));
 starts={e:int(np.flatnonzero(d1[:,e]<0)[0]) for e in es}
 ends={e:int(np.flatnonzero(d1[:,e]>0)[0]) for e in es}
 pos=min(set(starts.values())|set(ends.values()));ret=[]
 for _ in es:
  opts=[]
  for e in es:
   if e in [x[0] for x in ret]:continue
   if starts[e]==pos and d2[e,f]==1:opts.append((e,1,ends[e]))
   if ends[e]==pos and d2[e,f]==-1:opts.append((e,-1,starts[e]))
  assert len(opts)==1,(f,pos,opts)
  e,s,pos=opts[0];ret.append((e,s))
 return ret
words=[word(f) for f in range(d2.shape[1])]
G=rng.normal(size=(d2.shape[0],4));G/=np.linalg.norm(G,axis=1)[:,None]
def inv(x):return x*np.array([1,-1,-1,-1])
def hol(U,face):
 a=np.array([1.,0.,0.,0.])
 for e,s in words[face]:a=mul(a,U[e] if s==1 else inv(U[e]))
 return a
v_before=np.array([hol(G,int(f))[0] for f in R]);
epsilon=.07;axis=np.array([0.,0.,0.,1.])
rot=np.column_stack([np.cos(epsilon*t),np.zeros((len(t),2)),np.sin(epsilon*t)])
Gp=mul(rot,G)
v_after=np.array([hol(Gp,int(f))[0] for f in R])
dev=float(np.max(np.abs(v_after-v_before)))
assert dev>1e-6
# Countercheck derivative of face words at global flatness is zero for retained R.
flat=np.zeros_like(G);flat[:,0]=1
v_flat=np.array([hol(mul(rot,flat),int(f))[0] for f in R]);
assert np.max(abs(v_flat-1))<1e-12

report={'timestamp':'2026-10-27','spatial_disk':{'vertices':16,'edges':24,'faces':9,'center_face':4,'center_original_free_edges':0,'curvature_rank_cavity':8,'curvature_rank_inserted':9,'face_elimination_pivots':peeling,'exact_Z_factorization':'product of q(beta_p) for arbitrary face couplings, including an interior face with zero originally unique links'},'single_prism':{'vertices':len(verts),'edges':len(links),'faces':list(map(int,faces)),'boundary_rank':5,'sphere_formula':'Z = (product q(beta_p)) sum_(n>=0) (n+1)^2 product_p I_(n+1)(beta_p)/I_1(beta_p); r_n(0)=delta_n0','coupling_rows':rows,'independent_quaternion_MC':mc},'rank_changing_eight_face':{'Q':Q.tolist(),'individual_free_Haar_edges':individually_free_edges.tolist(),'linearized_null_residual':float(np.linalg.norm(d2[:,R].T@t)),'new_curvature_linear_response_norm':float(np.linalg.norm(d2[:,Q].T@t)),'generic_nonlin_wilson_trace_change_at_epsilon_007':dev,'flat_connection_retained_max_change':float(np.max(abs(v_flat-1))),'interpretation':'A linear relative null vector is not automatically an exact retained-action symmetry under noncommutative SU2 link rotations.'},'scope':'Exact nonlinear compact-Haar result for planar disks and one closed prism surface. NOT for arbitrary glued 3D Penrose prism supports.'}
(P/'certificate.json').write_text(json.dumps(report,indent=2));np.savez_compressed(P/'incidence_tests.npz',spatial_d1=B1,spatial_d2=B2,prism_d1=d1[np.ix_(verts,links)],prism_d2=d2[np.ix_(links,faces)],rank_changing_linear_vector=t,rank_changing_Q=Q)
print(json.dumps({'disk_last_peel':peeling[-1],'sphere_coupling_rows':rows,'mc':mc,'relative_linear_obstruction':report['rank_changing_eight_face']},indent=2))
