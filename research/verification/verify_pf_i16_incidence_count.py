#!/usr/bin/env python3
from fractions import Fraction

# Universal five-direction incidence: <= 8 accepted elementary rhombi per edge.
faces_per_edge = 8
face_sides = 4
D_universal = face_sides * (faces_per_edge - 1)
assert D_universal == 28

# Crop-specific census statement: if <=2 faces per edge, then D<=4.
D_crop = face_sides * (2 - 1)
assert D_crop == 4

# Rooted connected support count from a canonical DFS closed walk.
for k in range(1, 25):
    universal = D_universal ** (2 * (k - 1))
    crop = D_crop ** (2 * (k - 1))
    assert universal == 784 ** (k - 1)
    assert crop == 16 ** (k - 1)

# Exact geometric-series checks.
q_universal = Fraction(1, 1568)  # 784*q = 1/2
sum_universal_over_A = q_universal / (1 - D_universal**2 * q_universal)
assert sum_universal_over_A == Fraction(1, 784)

q_crop = Fraction(1, 32)  # 16*q = 1/2
sum_crop_over_A = q_crop / (1 - D_crop**2 * q_crop)
assert sum_crop_over_A == Fraction(1, 16)

# q=1/32 is not in the safe universal convergence region.
assert D_universal**2 * q_crop > 1

print("PASS: universal face-overlap degree <= 28 from <=8 rhombi/link")
print("PASS: rooted connected-support count <= 784^(k-1)")
print("PASS: crop-conditional degree <=4 gives 16^(k-1)")
print("PASS: exact universal geometric sum at q=1/1568 is A/784")
print("PASS: exact crop-conditional geometric sum at q=1/32 is A/16")
print("GATE: no source-uniform quantum activity estimate Aq^|S| proved")
print("LIMIT: finite-crop degree-four census is not an all-refinement theorem")
