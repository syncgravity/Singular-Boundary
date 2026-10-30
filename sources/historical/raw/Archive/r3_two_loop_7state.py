"""Exact disjoint-edge two-loop principal block on 2x2 SU(2) plaquette disk.
This is NOT the complete spin-network basis (adjacent plaquettes recouple).
"""
import json, numpy as np
from scipy.special import ive
from pathlib import Path
out=Path('/mnt/data')
# horizontal edges and vertical edges from 3x3 grid, plaquette index = y*2+x
edgelist=[]
for y in range(3):
 for x in range(2): edgelist.append(((x,y),(x+1,y)))
for x in range(3):
 for y in range(2): edgelist.append(((x,y),(x,y+1)))
edgeids={tuple(sorted(e)):i for i,e in enumerate(edgelist)}
def square_edges(x,y):
 v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 return frozenset(edgeids[tuple(sorted((v[i],v[(i+1)%4])))] for i in range(4))
faces=[square_edges(x,y) for y in range(2) for x in range(2)]
assert len(set().union(*faces))==12
assert faces[0].isdisjoint(faces[3]) and faces[1].isdisjoint(faces[2])
labels=[(),(0,),(1,),(2,),(3,),(0,3),(1,2)]
# Each chosen product of disjoint face characters forms a normalized temporal transfer eigenstate.
def m(k):
 q=2*ive(1,k)/k
 r=ive(2,k)/ive(1,k)
 s=ive(3,k)/ive(1,k)
 return np.array([q, q*2*r, q*(1+3*s)]),q,r,s

def spatial_block(k):
 mu,q,r,s=m(k)
 F=np.zeros((7,7))
 for i,S in enumerate(labels):
  for j,T in enumerate(labels):
   F[i,j]=np.prod([mu[int(a in S)+int(a in T)] for a in range(4)])
 return F,q,r,s

def multiplier(S,temporal_gammas):
 edges=set().union(*(faces[p] for p in S)) if S else set()
 v=1.
 for e in edges:
  beta=temporal_gammas.get(e,0.)
  if beta<=0: return 0.
  v*=ive(2,beta)/ive(1,beta)
 return float(v)

# Overlapping in space at two distinct time intervals, but not identical selected link sets.
gamma1={e:3. for e in faces[0]|faces[3]}
gamma2={e:5. for e in faces[1]|faces[2]}
res={}
for k in [0.5,2.,10.]:
 F,q,r,s=spatial_block(k)
 assert np.linalg.eigvalsh(F).min()>-1e-12
 x=np.array([multiplier(S,gamma1) for S in labels]);y=np.array([multiplier(S,gamma2) for S in labels]);
 # exclude vacuum, which has eigenvalue 1 under all normalized kernels
 mixed=float(sum(x[a]*y[b]*F[0,a]*F[a,b]*F[b,0] for a in range(1,7) for b in range(1,7)))
 # six one-loop/two-loop cross entries as contribution (these have no negative recoupling in this block)
 cross=float(sum(x[a]*y[b]*F[0,a]*F[a,b]*F[b,0] for a in range(1,5) for b in (5,6)) + sum(x[a]*y[b]*F[0,a]*F[a,b]*F[b,0] for a in (5,6) for b in range(1,5)))
 two_two=float(sum(x[a]*y[b]*F[0,a]*F[a,b]*F[b,0] for a in (5,6) for b in (5,6)))
 assert mixed>=0 and cross>=0 and two_two>=0
 res[str(k)]={'q':q,'fundamental_mean':2*r,'fundamental_second_moment':1+3*s,'min_spatial_block_entry':float(F.min()),'min_eigenvalue':float(np.linalg.eigvalsh(F).min()),'mixed_7state':mixed,'one_two_cross':cross,'two_two':two_two,'nonzero_x':int(np.count_nonzero(x[1:])),'nonzero_y':int(np.count_nonzero(y[1:])),'temporal_multipliers_first':x.tolist(),'temporal_multipliers_second':y.tolist()}
 if k==2:
  np.savez_compressed(out/'r3_two_loop_7state_matrix.npz',F=F,x=x,y=y,labels=np.array(['-'.join(map(str,S)) for S in labels]),edge_faces=np.array([list(f) for f in faces],dtype=int))
report={'status':'exact seven-state block for disjoint-edge loop products only; incomplete adjacent-loop recoupling','geometry':'3x3 vertices, 12 edges, four quadrilateral faces; face indices row major','labels':[list(s) for s in labels],'face_edge_indices':[sorted(f) for f in faces],'temporal_step1_links':sorted(gamma1),'temporal_step2_links':sorted(gamma2),'results':res,'complete_mixed_coefficient':'NOT COMPUTED','support_local_theorem_for_arbitrary_3D_cavity':'NOT PROVED'}
(out/'r3_two_loop_7state_certificate.json').write_text(json.dumps(report,indent=2))
print(json.dumps(res,indent=2))
