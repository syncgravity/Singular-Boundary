"""Gauge-only intertwiner audit for actual M5 Penrose roots (requires Library-restored dependencies).
Run from a runtime with validate_actual_m5_two_tree_wilson_forms.py under /mnt/data.
"""
import runpy,numpy as np
m=runpy.run_path('/mnt/data/validate_actual_m5_two_tree_wilson_forms.py')
rng=np.random.default_rng(540)
U=rng.normal(size=(30,4));U/=np.linalg.norm(U,axis=1)[:,None]
verts=sorted(m['adj'])
h={v:(lambda q:q/np.linalg.norm(q))(rng.normal(size=4)) for v in verts}
Ug=U.copy()
for i,e in enumerate(m['edge_ids']):
 s,t,_=m['A'].edges[e]
 Ug[i]=m['mul'](m['mul'](h[int(s)],U[i]),m['inv'](h[int(t)]))
def energy(X,tree):
 g=m['grads'](X)
 v=m['transports'](tree,X)
 D=np.array([m['rot'](v[i],g[i]) for i in range(30)])
 return float(np.einsum('ia,ij,ja->',D,m['K'],D))
qa=[energy(U,t) for t in (m['T1'],m['T2'])]
qb=[energy(Ug,t) for t in (m['T1'],m['T2'])]
assert abs(m['obs'](U)-m['obs'](Ug))<1e-10
assert np.allclose(qa,qb,atol=5e-9,rtol=5e-9)
assert abs(qa[0]-qa[1])>1e-6
print('PASS separately gauge invariant energies with nonzero tree difference')
print('F:',m['obs'](U),m['obs'](Ug),'Q:',qa,qb)
