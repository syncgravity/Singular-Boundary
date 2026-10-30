import numpy as np,json
from pathlib import Path
out=Path(__file__).parent
faces=[(0,1,4,3),(1,2,5,4),(3,4,7,6),(4,5,8,7)]
edge_dict={};elist=[]
for ff in faces:
 for a,b in zip(ff,ff[1:]+ff[:1]):
  pair=tuple(sorted([a,b]))
  if pair not in edge_dict:edge_dict[pair]=len(elist);elist.append(pair)
B1=np.zeros((9,12),dtype=int);B2=np.zeros((12,4),dtype=int)
for i,(a,b) in enumerate(elist): B1[a,i]=-1;B1[b,i]=1
for f,ff in enumerate(faces):
 for a,b in zip(ff,ff[1:]+ff[:1]):
  e=edge_dict[tuple(sorted([a,b]))];B2[e,f]=1 if a<b else -1
assert not (B1@B2).any()
n=3;V=9*n;E=21*n;F=16*n
D1=np.zeros((V,E),dtype=int);D2=np.zeros((E,F),dtype=int)
h=lambda t,e:12*t+e;v=lambda t,x:12*n+9*t+x;s=lambda t,f:4*t+f;z=lambda t,e:4*n+12*t+e
for t in range(n):
 nxt=(t+1)%n
 for e in range(12):
  D1[t*9:(t+1)*9,h(t,e)]=B1[:,e]
  D2[h(t,e),z(t,e)]+=1;D2[h(nxt,e),z(t,e)]-=1
  for x in range(9):D2[v(t,x),z(t,e)]+=B1[x,e]
 for x in range(9):D1[9*t+x,v(t,x)]-=1;D1[9*nxt+x,v(t,x)]+=1
 for f in range(4):D2[t*12:(t+1)*12,s(t,f)]=B2[:,f]
assert not (D1@D2).any()
def rank(a):return int(np.linalg.matrix_rank(a.astype(float),tol=1e-9))
fullrank=rank(D2)
# overlapping irregular supports: temporal plaquettes on boundaries of face 0,1 first step and face0,2 second
q0={z(0,e) for f in [0,1] for e in np.flatnonzero(B2[:,f])}
q1={z(1,e) for f in [0,2] for e in np.flatnonzero(B2[:,f])}
Q=sorted(q0|q1)
loc=np.flatnonzero(np.any(D2[:,Q]!=0,axis=1));R=sorted(set(range(F))-set(Q));rankR=rank(D2[:,R]);rankQ=fullrank-rankR
# local conditional theorem requires cost proportional to number of variable links: no exterior assumptions used
report={'vertices':V,'edges':E,'faces':F,'rank_boundary_faces':fullrank,'q0_temporal_face_ids':sorted(map(int,q0)),'q1_temporal_face_ids':sorted(map(int,q1)),'q_total':len(Q),'local_links_touching_Q':len(loc),'local_link_ids':loc.tolist(),'curvature_rank_retained':rankR,'additional_linearized_curvature_rank':rankQ,'topological_redundancy_in_Q':len(Q)-rankQ,'conditional_bound':'R(xi)>=c lambda^(-3 m /2) exp(-Delta_lambda(xi)), m=local_links_touching_Q, under smooth uniformly bounded degree action at couplings <= C lambda','warning':'rank result only linearized and does not prove uniform expectation of exp(-Delta_lambda); Q touches its entire temporal-face boundary link set'}
(out/'certificate.json').write_text(json.dumps(report,indent=2));np.savez_compressed(out/'incidence.npz',d1=D1,d2=D2,spatial_d1=B1,spatial_d2=B2,Q=np.array(Q),local_links=loc)
print(json.dumps(report,indent=2))
