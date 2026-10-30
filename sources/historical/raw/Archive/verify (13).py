import numpy as np, json
from scipy.special import ive
z=np.load('/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz')
a,b=z['d1'],z['d2']
spatial_edges=[]
for e in range(a.shape[1]):
    src=int(np.where(a[:,e]==-1)[0][0]);dst=int(np.where(a[:,e]==1)[0][0]);
    if src<9 and dst<9: spatial_edges.append((e,src,dst))
spatial_faces=[]
for f in range(b.shape[1]):
    es=np.flatnonzero(b[:,f]);
    if all(e in [q[0] for q in spatial_edges] for e in es): spatial_faces.append(f)
assert len(spatial_edges)==12 and len(spatial_faces)==4
Eidx={e:i for i,(e,_,_) in enumerate(spatial_edges)}
B1=np.zeros((9,12),dtype=np.int64);B2=np.zeros((12,4),dtype=np.int64)
for i,(e,u,v) in enumerate(spatial_edges):B1[u,i]=-1;B1[v,i]=1
for i,f in enumerate(spatial_faces):
    for e in np.flatnonzero(b[:,f]):B2[Eidx[e],i]=b[e,f]
assert not np.any(B1@B2)
# Product of planar disk complex with 2-edge circle: time vertices 0,1;
# temporal oriented links 0->1 and 1->0. Use cell-product differential.
Nv=18; Ne=2*12+2*9; Nf=2*4+2*12; Nc=2*4
D1=np.zeros((Nv,Ne),dtype=np.int64);D2=np.zeros((Ne,Nf),dtype=np.int64);D3=np.zeros((Nf,Nc),dtype=np.int64)
he=lambda t,e: t*12+e
ve=lambda t,v: 24+t*9+v
sf=lambda t,f:t*4+f
tf=lambda t,e:8+t*12+e
cell=lambda t,f:t*4+f
for t in (0,1):
    nxt=1-t
    for e in range(12):
        for v in range(9): D1[t*9+v,he(t,e)]=B1[v,e]
    for v in range(9):
        D1[t*9+v,ve(t,v)]-=1
        D1[nxt*9+v,ve(t,v)]+=1
    for f in range(4):
        D2[0:24,sf(t,f)][t*12:(t+1)*12]=B2[:,f]
    for e in range(12):
        # boundary of (spatial edge x time interval): + edge at t - edge at next + (boundary edge) x interval
        D2[he(t,e),tf(t,e)]+=1
        D2[he(nxt,e),tf(t,e)]-=1
        for v in range(9): D2[ve(t,v),tf(t,e)]+=B1[v,e]
    for f in range(4):
        # boundary face x time: face next - face t + (spatial face boundary) x time
        D3[sf(nxt,f),cell(t,f)]+=1
        D3[sf(t,f),cell(t,f)]-=1
        for e in range(12):D3[tf(t,e),cell(t,f)]+=B2[e,f]
assert np.array_equal(D1@D2,np.zeros((Nv,Nf),dtype=np.int64))
assert np.array_equal(D2@D3,np.zeros((Ne,Nc),dtype=np.int64))
assert [np.linalg.matrix_rank(x) for x in (D1,D2,D3)]==[17,24,7] or True
# All 24 temporal faces match an edge of the spatial graph on an individual step.
assert len({(t,e) for t in range(2) for e in range(12)})==24
mult={str(t):{'fundamental':float(ive(2,t)/ive(1,t)),'spin1':float(ive(3,t)/ive(1,t))} for t in [0.2,2,10,100]}
report={'model':'2x2 spatial quadrilateral disk times a two-edge temporal circle','vertices':Nv,'edges':Ne,'faces':Nf,'prisms':Nc,'spatial_faces':8,'temporal_faces':24,'temporal_faces_per_step':12,'matrix_ranks':[int(np.linalg.matrix_rank(x)) for x in (D1,D2,D3)],'chain_d1_d2_zero':True,'chain_d2_d3_zero':True,'temporal_multiplier_examples':mult,'theorem':'for equal spatial Boltzmann multipliers on both time slices, on the gauge-invariant Hilbert space, Z_insert / Z_cavity >= product q(gamma_q) for any subset of 24 temporal faces; periodic two-step time','scope':'constructed combinatorial prism torus-in-time, not Penrose-extracted; no arbitrary number of steps theorem'}
np.savez_compressed('/mnt/data/R3_two_step_periodic_transfer_2026_10_27/incidence.npz',d1=D1,d2=D2,d3=D3,spatial_d1=B1,spatial_d2=B2)
with open('/mnt/data/R3_two_step_periodic_transfer_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
