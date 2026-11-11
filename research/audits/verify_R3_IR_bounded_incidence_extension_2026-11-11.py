"""Arithmetic verifier for the bounded-incidence R3-IR extension."""
from fractions import Fraction as F
from math import exp, pi, sqrt

S1 = F(333528, 10**9)
S2 = F(194619, 10**12)
q = S1 + S2
T = F(250292, 10**9)
h = F(166813, 10**9)
rho = F(6, 5)
kappa = F(1, 4)

def constants(r):
    # r is maximum number of four-link faces incident to one link.
    c = F(1, 2) - 2 * r * rho * q
    B = F(r, 2) * S1
    c_tr = F(3, 4) * exp(-4 * pi * float(B))
    ell = F(4, 3) * c_tr * float(B * B)
    C3 = 2 * float(rho) * sqrt(1728) * r * float(T)
    CH = 6 * r * float(h) * (2 + 3 * r * (1 + float(rho)))
    CR = 2 * float(kappa) * sqrt(2) * float(B)
    CG = C3 + CR
    a = float(c) - ell
    b = float(c_tr) - CH
    lam = (a + b - sqrt((a - b)**2 + CG**2)) / 2
    return map(float, (c, B, c_tr, ell)), C3, CH, CR, CG, a, b, lam

assert q == F(333722619, 10**12)
v2 = constants(2)
v4 = constants(4)
(c2, B2, tr2, ell2), C32, CH2, CR2, CG2, a2, b2, lam2 = v2
(c4, B4, tr4, ell4), C34, CH4, CR4, CG4, a4, b4, lam4 = v4

# Degree two reproduces the sharpened straight-strip envelope.
assert c2 > 0.49839813 and tr2 > 0.74686315
assert lam2 > 0.4955484

# Degree four (open cubic plaquette incidence) retains a positive margin.
assert c4 > 0.4967962628
assert B4 <= 0.000667056
assert tr4 > 0.7437394215
assert ell4 < 4.413e-7
assert C34 < 0.099882654
assert CH4 < 0.113699741
assert CR4 < 0.000471680
assert CG4 < 0.100354334
assert a4 > 0.4967958216
assert b4 > 0.6300396807
assert lam4 > 0.4800

print("PASS: degree-r formulas reproduce the straight-strip r=2 constants")
print("r=2: c, c_tr, ell, C3, CH, CR, CG, a, b, lambda =",
      c2, tr2, ell2, C32, CH2, CR2, CG2, a2, b2, lam2)
print("PASS: degree-four bounded-incidence quadratic form is positive")
print("r=4: c, B, c_tr, ell, C3, CH, CR, CG, a, b, lambda =",
      c4, B4, tr4, ell4, C34, CH4, CR4, CG4, a4, b4, lam4)
