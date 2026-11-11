"""Independent arithmetic check for sharpened R3-IR analytic inputs.

The scalar derivative ceilings are imported from the certified positive-majorant
source audit. This script checks their propagation through the weighted
Bakry-Emery, conditional Holley-Stroock, leakage, Codazzi and 2x2 energy bounds.
"""
from fractions import Fraction as F
from math import exp, pi, sqrt

# Conservative rational ceilings from the global scalar derivative certificate.
S1 = F(333528, 10**9)
S2 = F(194619, 10**12)
q = S1 + S2
assert q == F(333722619, 10**12)

# Weighted Bochner: row/column Schur bound = 8*(q/4)*(6/5) = 12q/5;
# the Bakry-Emery loss is twice that bound.
row = F(12, 5) * q
c = F(1, 2) - 2 * row
assert c > F("0.49839813")

# Conditional score, oscillation and Holley-Stroock comparison.
B = S1
osc = 4 * pi * float(B)
c_tr = F(3, 4) * exp(-osc)
ell = F(4, 3) * c_tr * float(B * B)
assert c_tr > 0.7468631508
assert ell < 1.108e-7

# Existing local ordered tensor / Hessian dressing constants, conservatively rounded up.
T = F(250292, 10**9)       # 0.000250292
h = F(166813, 10**9)       # 0.000166813
C3 = 2 * F(6, 5) * sqrt(float(F(24 * 288)) ) * float(T)
CH = F(912, 5) * h
CR = sqrt(2) * float(B) / 2  # 2*kappa*sqrt(2)*B, kappa=1/4
CG = C3 + CR

a = float(c) - ell
b = float(c_tr) - float(CH)
lam = (a + b - sqrt((a - b)**2 + CG**2)) / 2

assert float(c) > 0.4983981314
assert float(c_tr) > 0.7468631508
assert float(ell) < 1.108e-7
assert float(CH) < 0.030426692
assert C3 < 0.049941327
assert CR < 0.000235840
assert CG < 0.050177167
assert a > 0.4983980206
assert b > 0.7164364596
assert lam > 0.4955484

print("PASS: rational scalar derivative ceilings and q envelope")
print("S1 =", float(S1), "S2 =", float(S2), "q =", float(q))
print("weighted Bochner row/column =", float(row), "c_* =", float(c))
print("conditional score B_* =", float(B), "oscillation <=", osc)
print("c_tr,* =", float(c_tr), "ell_* =", float(ell))
print("C3 <=", C3, "CH <=", float(CH), "CR,* <=", CR, "CG,* <=", CG)
print("a_* =", a, "b_* =", b, "lambda_min(Q_*) =", lam)
print("PASS: sharpened common-measure finite-strip energy matrix is positive")
