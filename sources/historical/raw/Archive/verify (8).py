import numpy as np, json
src='/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz'
z=np.load(src)
B1,B2,B3=z['d1'],z['d2'],z['d3']; Q=z['seam_face_ids'].tolist()
ret=[p for p in range(B2.shape[1]) if p not in Q]
free=np.where(np.count_nonzero(B2[:,ret],axis=1)==0)[0].tolist()
assert len(free)==1
edge=free[0]
assert all(abs(int(B2[edge,p]))==1 for p in Q)
assert not np.any(B1@B2) and not np.any(B2@B3)
assert np.linalg.matrix_rank(B2[:,ret])==15
# Three SU(2) singlet-pairing vectors in (C^2)^tensor4 span dimension 2.
eps=np.array([[0.,1.],[-1.,0.]])/np.sqrt(2)
S=[]
for pairs in [[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]:
 a=np.zeros((2,2,2,2))
 for ix in np.ndindex(2,2,2,2):
  a[ix]=np.prod([eps[ix[i],ix[j]] for i,j in pairs])
 S.append(a.reshape(16))
S=np.stack(S,axis=1)
P=S@np.linalg.pinv(S)
P=(P+P.T)/2
spec=np.linalg.eigvalsh(P)
assert np.allclose(P@P,P,atol=1e-12)
assert np.allclose(sorted(spec),[0.]*14+[1.]*2,atol=1e-12)
# For fixed exterior choice with one plaquette holonomy -U and other three U,
# the genuine four-port fundamental Fourier moment flips sign.
negative_spec=np.linalg.eigvalsh(-P)
assert np.allclose(sorted(negative_spec),[-1.]*2+[0.]*14,atol=1e-12)
np.savez('/mnt/data/R3_four_prism_fourport_audit_2026_10_27/fundamental_blocks.npz',singlet_projector=P,negative_fixed_exterior_block=-P,intertwiner_vectors=S)
report={'model':'constructed four-prism loop, not provenance-certified from Penrose tiles','vertices':int(B1.shape[0]),'edges':int(B1.shape[1]),'faces':int(B2.shape[1]),'cells':int(B3.shape[1]),'retained_faces':len(ret),'interface_faces':Q,'interface_only_link_ids':free,'central_link_incidence_signs':[int(B2[edge,p]) for p in Q], 'retained_face_rank':15,'full_face_rank':int(np.linalg.matrix_rank(B2)), 'four_spin_intertwiner_projector_eigenvalues':[round(float(s),12) for s in spec], 'fixed_exterior_sign_flipped_four_spin_eigenvalues':[round(float(s),12) for s in negative_spec], 'at_zero_retained_couplings_full_effective_kernel':'constant 1; all nontrivial Fourier blocks vanish','scope':'conditional four-port fundamental Fourier moment, NOT fully integrated effective kernel at positive beta'}
with open('/mnt/data/R3_four_prism_fourport_audit_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
