import numpy as np,json
from collections import defaultdict
src='/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz'
z=np.load(src); B=np.asarray(z['d2'],dtype=int); Q=z['seam_face_ids'].tolist(); R=[i for i in range(B.shape[1]) if i not in Q]
assert np.max(np.abs(B))<=1
assert np.array_equal(z['d1']@B,np.zeros((18,20),int))
assert np.array_equal(B@z['d3'],np.zeros((33,4),int))
cols=[sum((int(B[e,p])&1)<<e for e in range(B.shape[0])) for p in R]
ports=[sum((int(B[e,p])&1)<<e for e in range(B.shape[0])) for p in Q]
# All Z2 plaquette-surface boundaries of the retained faces, cost is number of half-integer faces.
# Fully exact GF(2) enumeration: 2^16 terms, no floating point.
best={}; count=defaultdict(int); reps={}
cur=0; size=0; prev_gray=0
for t in range(1<<len(cols)):
 gray=t^(t>>1)
 if t:
  delta=gray^prev_gray
  i=delta.bit_length()-1
  cur ^=cols[i]
  size+= 1 if gray>>i&1 else -1
 prev_gray=gray
 if cur not in best or size<best[cur]:
  best[cur]=size;count[cur]=1;reps[cur]=gray
 elif size==best[cur]:count[cur]+=1
report={}
for mask in range(1<<len(Q)):
 target=0
 for i in range(len(Q)):
  if mask>>i&1:target^=ports[i]
 d=best.get(target)
 report[f'{mask:04b}']={'selected_port_indices':[Q[i] for i in range(4) if mask>>i&1], 'minimum_half_integer_retained_faces':d,'minimal_surface_count': count[target] if d is not None else 0,'one_minimal_retained_face_set':[R[i] for i in range(16) if reps[target]>>i&1] if d is not None else []}
assert sum(v['minimum_half_integer_retained_faces'] is None for k,v in report.items() if k!='0000')==8
assert report['1111']['minimum_half_integer_retained_faces']==8
assert report['1111']['minimal_surface_count']==2
out={'model':'constructed four-prism 2x2 quadrilateral extrusion; not provenance certified as Penrose tile geometry','face_ids_Q':Q,'retained_face_count':len(R),'exact_port_spin_parity_selection':report,'interpretation':'None = Fourier block with fundamental representations on selected ports and trivial on others is exactly zero at arbitrary positive Wilson couplings. Non-None = necessary parity condition, not guaranteed positivity/nonzero; minimum number of retained half-integer spins in a character expansion.','scope':'Exact center-parity constraints on the FULL exterior-integrated positive-coupling Fourier matrices. Numerical values of allowed nonzero matrices not computed.'}
path='/mnt/data/R3_four_prism_exterior_spin_selection_2026_10_27/selection_certificate.json'
with open(path,'w') as f:json.dump(out,f,indent=2)
print(json.dumps({k:(v['minimum_half_integer_retained_faces'],v['minimal_surface_count']) for k,v in report.items()},indent=2))
