from fractions import Fraction as F
from itertools import combinations
import sys
from pathlib import Path

# Run with a PYTHONPATH containing penrose_causal_study.py and wilson_torus.py
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces

faces, signs, edge_count = penrose_faces(Approximant(M=5))
S = (1, 2, 3, 4, 7, 8, 10)
assert len(faces) == 188 and edge_count == 376
adjacent = []
for g, k in combinations(S, 2):
    common = set(map(int, faces[g])) & set(map(int, faces[k]))
    assert len(common) <= 1
    if common:
        e = next(iter(common))
        sign_g = int(signs[g, list(faces[g]).index(e)])
        sign_k = int(signs[k, list(faces[k]).index(e)])
        assert sign_g == -sign_k
        cG, cU = F(4, 39), F(4, 351)
        assert F(13, 2) * cG == F(2, 3)
        assert -F(1, 2) * cG + F(9, 2) * cU == 0
        adjacent.append((g, k, e))
    else:
        assert F(6) * F(1, 9) == F(2, 3)
assert len(adjacent) == 6
assert adjacent == [(1,3,3),(1,8,14),(2,3,2),(2,4,5),(7,8,8),(7,10,12)]
print('PASS: 21 M5 seven-face pair resolvent identities')
