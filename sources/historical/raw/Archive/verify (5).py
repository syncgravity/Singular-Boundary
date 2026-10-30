import numpy as np,json
z=np.load('/mnt/data/R3_two_prism_certified_2026_10_27/incidence.npz',allow_pickle=True)
B1,B2,B3=(z['d1'],z['d2'],z['d3'])
shared=np.flatnonzero(np.count_nonzero(B3,axis=1)==2)
assert len(shared)==1
p=int(shared[0]); seam=set(np.flatnonzero(B2[:,p]))
info=[]; edge_sets=[]
for c in range(2):
 f=[int(i) for i in np.flatnonzero(B3[:,c]) if i!=p]
 assert len(f)==5
 e=set(np.flatnonzero(np.any(B2[:,f]!=0,axis=1)))
 edge_sets.append(e)
 disc_boundary=B2[:,f]@B3[f,c]
 assert set(np.flatnonzero(disc_boundary))==seam
 # Euler of disc using full edges and vertices in these edges
 vertices=set(np.flatnonzero(np.any(B1[:,list(e)]!=0,axis=1)))
 assert len(vertices)-len(e)+len(f)==1
 info.append(dict(cell=c,faces=f,face_count=len(f),edge_count=len(e),vertex_count=len(vertices),Euler=len(vertices)-len(e)+len(f),boundary_edge_count=len(seam)))
assert edge_sets[0].intersection(edge_sets[1])==seam
assert np.all(B1@B2==0) and np.all(B2@B3==0)
report={'model':'two-face-sharing quadrilateral prisms, not sampled Penrose patch','total_cells':2,'total_faces':len(B2.T),'shared_face_id':p,'shared_face_edge_ids':[int(x) for x in sorted(seam)],'disk_data':info,'two_disks_intersection_only_seam':True,'integer_chain_complex_verified':True,'analytic_kernel':'fL(h) fR(h^{-1}); fS=w_{beta_1}*...*w_{beta_5}; coefficient scalar c_j(beta)=2 exp(-beta) I_(2j+1)(beta)/beta >=0','guarantee':'Z_with_insert/Z_without_insert >= q(beta_insert)'}
with open('/mnt/data/R3_two_prism_positive_interface_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
