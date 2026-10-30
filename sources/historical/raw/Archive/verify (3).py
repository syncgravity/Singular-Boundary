import json,numpy as np
src='/mnt/data/R3_two_prism_certified_2026_10_27/incidence.npz'
a=np.load(src,allow_pickle=True)
d1,d2,d3=(a[k] for k in ('d1','d2','d3'))
assert (d1@d2==0).all() and (d2@d3==0).all()
internal=np.flatnonzero(np.count_nonzero(d3,axis=1)==2)
assert len(internal)==1
assert np.array_equal(np.sort(np.abs(d3[internal[0]])),np.array([1,1]))
ranks={n:int(np.linalg.matrix_rank(x)) for n,x in [('d1',d1),('d2',d2),('d3',d3),('d2_without_internal_face',np.delete(d2,internal[0],axis=1))]}
assert ranks['d2']==ranks['d2_without_internal_face']==9
cert={'provenance':'constructed local quadrilateral-prism patch; not certified extraction from Penrose tiling', 'vertices':int(d1.shape[0]),'links':int(d1.shape[1]),'faces':int(d2.shape[1]),'prisms':int(d3.shape[1]),'shared_face_index':int(internal[0]),'shared_face_boundary_edges':np.flatnonzero(d2[:,internal[0]]).tolist(),'chain_conditions':True,'ranks':ranks,'theorem_scope':'All links on this finite patch integrated; no fixed external Wilson collar'}
with open('/mnt/data/R3_moser_two_prism_2026_10_27/certificate.json','w') as f:json.dump(cert,f,indent=2)
print(json.dumps(cert,indent=2))
