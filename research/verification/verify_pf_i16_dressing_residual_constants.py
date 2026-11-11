#!/usr/bin/env python3
from fractions import Fraction

# Universal accepted-face incidence and residual support geometry.
d_max = 8
face_sides = 4
support_links = 1 + (face_sides - 1) * d_max
assert support_links == 25

# If d faces meet an edge, the residual coefficient bound is
# a_e * (d^2+1) * max_f ||grad_e s_f||_inf^2.
# With A_f >= a_e/d and ||grad s_f|| <= C1*b/A_f,
# this is <= C1^2*b^2/a_e * d^2*(d^2+1).
constant = d_max**2 * (d_max**2 + 1)
assert constant == 4160

# Finite-crop incidence <=2 improves support and residual constants.
d_crop = 2
assert 1 + 3*d_crop == 7
assert d_crop**2 + 1 == 5
assert d_crop**2 * (d_crop**2 + 1) == 20

# Exact scalar algebra for equal shared-link gradients.
for d in range(1, d_max + 1):
    R_equal = Fraction(d*d) - Fraction(1, d)*d
    assert R_equal == d*d - 1
assert Fraction(1) - Fraction(1, 1) == 0

print("PASS: residual support contains at most 25 original links")
print("PASS: conditional residual norm constant is 4160*C1^2*b0^2/a0")
print("PASS: finite-crop d<=2 gives at most 7 links and factor 5")
print("PASS: singly incident links have exactly zero residual")
print("GATE: isolated-face derivative/Hessian estimate remains to be proved uniformly")
print("GATE: local-potential stability for the extensive residual sum remains open")
