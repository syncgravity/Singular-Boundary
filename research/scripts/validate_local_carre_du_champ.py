"""Independent finite-disk block bound and SU(2) invariant-gradient identity."""
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path('/mnt/data/penrose_study_src')))
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces

d = np.load('/mnt/data/global_whitney_11face.npz')
ids = list(map(int, d['edge_ids']))
K = np.linalg.inv(d['matrix'])
a = Approximant(M=5)
face_edges, _, _ = penrose_faces(a)
selected_faces = (0, 1, 3, 2, 4, 154, 150, 11, 10, 7, 8)
coefficients = {}
for face in selected_faces:
    indices = [ids.index(int(e)) for e in face_edges[face]]
    local = K[np.ix_(indices, indices)]
    coefficients[face] = np.linalg.eigvalsh(local)[-1] / 2
assert abs(coefficients[7]-3.4922466271) < 1e-7
assert max(coefficients, key=coefficients.get)==7

rng = np.random.default_rng(630)
for _ in range(10000):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    link_gradient = -q[1:]/2
    assert abs(np.dot(link_gradient,link_gradient)-(1-q[0]**2)/4)<2e-15

for face in selected_faces:
    print(face,format(coefficients[face],'.10f'))
print('PASS 11 local K blocks and 10,000 SU2 gradient identities')
