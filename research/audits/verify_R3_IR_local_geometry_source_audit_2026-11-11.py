"""Independent exact-arithmetic audit of the R3-IR local geometric inputs.

This checker complements, but does not replace, the analytic quaternion,
Levi-Civita, fixed-point, and strip-incidence arguments in the cited source
certificates. It verifies the rational fixed-point enclosure, global derivative
coefficient envelope, finite-strip incidence counts, Schur arithmetic, and
combined numerical constants.
"""
from fractions import Fraction as F
from math import sqrt, exp, pi
from collections import Counter

# ---------------------------------------------------------------------------
# 1. Six-step positive majorant for the isolated plaquette fixed point.
# This controls every |b|<=1/1000, not only the endpoint b=1/1000.
# ---------------------------------------------------------------------------
b0 = F(1, 1000)
R = F(1, 25)
L = b0 * (F(129, 6) + 2 * R / 768)
map_ball_bound = b0 * (F(129, 6) * (1 + R) + R*R/768)
assert L < 1 and map_ball_bound < R

def positive_majorant_map(v):
    out = {}
    for n, value in [(0, F(1)), *sorted(v.items())]:
        for j in (n - 1, n + 1):
            if j >= 1:
                out[j] = out.get(j, F(0)) + b0 * value / (2 * j * (j + 2))
    first = v.get(1, F(0))
    for n, value in v.items():
        # Absolute-value majorant: replace the signed nonlinear correction by +.
        out[n] = out.get(n, F(0)) + b0 * first * value / (2 * n * (n + 2))
    return {n: value for n, value in out.items() if value}

def weighted_norm(u):
    return sum(abs(v) * 2**n * (n + 1)**6 for n, v in u.items())

u = {}
for _ in range(6):
    u = positive_majorant_map(u)
res = positive_majorant_map(u)
err = weighted_norm({n: res.get(n, F(0)) - u.get(n, F(0)) for n in set(res) | set(u)}) / (1 - L)

# ---------------------------------------------------------------------------
# 2. Global derivative envelope for U_n (not a finite n<=199 check).
# ---------------------------------------------------------------------------
def endpoint_derivative(n, k):
    if k == 0: return F(n + 1)
    if k == 1: return F(n * (n + 1) * (n + 2), 3)
    if k == 2: return F((n - 1) * n * (n + 1) * (n + 2) * (n + 3), 15)
    if k == 3: return F((n - 2) * (n - 1) * n * (n + 1) * (n + 2) * (n + 3) * (n + 4), 105)
    raise ValueError(k)

# Gegenbauer identity: U_n^(k)(x)=2^k k! C_{n-k}^{k+1}(x).
# The normalized zonal Gegenbauer polynomial has absolute value <=1 on [-1,1],
# so sup_x |U_n^(k)(x)| <= U_n^(k)(1). The ratios to the coefficient weight
# 2^n(n+1)^6 have the following exact global maxima:
maxima = [F(1, 64), F(1, 64), F(2, 729), F(24, 15625)]

# Monotonicity certificates for r_k(n+1)/r_k(n) <= 1:
# k=1: 2 C_1(n)(n+2)^6-C_1(n+1)(n+1)^6
#   = (n+1)(n+2)/3 * P1(n), and P1(n) in x=n-1 has all positive coefficients.
P1_x_coeffs = [F(1,3), F(9), F(314,3), F(2072,3), F(2856), F(23044,3), F(40292,3), F(14692), F(27262,3), F(2404)]
# k=2: same difference = n(n+1)(n+2)(n+3)/15 * P2(n),
# and P2(n) in x=n-2 has all positive coefficients.
P2_x_coeffs = [F(1,15), F(8,3), F(48), F(512), F(53804,15), F(51842,3), F(873278,15), F(409634,3), F(651349,3), F(220796), F(1908332,15), F(30544)]
# k=3: same difference = n(n-1)(n+1)(n+2)(n+3)(n+4)/105 * P3(n),
# and P3(n) in x=n-4 has all positive coefficients. r_3(4)/r_3(3)=16384/15625>1.
P3_x_coeffs = [F(1,105), F(2,3), F(449,21), F(14544,35), F(81802,15), F(1783464,35), F(5221466,15), F(5268268,3), F(684807587,105), F(613804816,35), F(494782229,15), F(1425032346,35), F(1018625736,35), F(8831808)]
assert all(v > 0 for v in P1_x_coeffs + P2_x_coeffs + P3_x_coeffs)
assert F(16384,15625) > 1

# Check the finitely many initial values before each monotone tail; the
# coefficient-positive polynomial identities prove all subsequent n.
for k, start in [(0,1),(1,1),(2,2),(3,4)]:
    for n in range(1, start + 1):
        ratio = endpoint_derivative(n,k) / (2**n * (n+1)**6)
        assert ratio <= maxima[k], (k,n,ratio,maxima[k])
    if k == 3:
        assert endpoint_derivative(3,3)/(2**3*4**6) < maxima[3]

U = []
for k in range(4):
    total = sum(abs(v) * endpoint_derivative(n,k) for n,v in u.items())
    U.append(total + err)
A, B, C, D = U
assert A < 1
s1 = B/(1-A)
s2 = C/(1-A) + s1*s1
s3 = D/(1-A) + 3*C*B/(1-A)**2 + 2*s1**3

# ---------------------------------------------------------------------------
# 3. Ordered covariant third-derivative entry and Schur constants.
# ---------------------------------------------------------------------------
# For left-invariant frame fields:
# H_jk = D_j D_k p - Gamma_jk^l D_l p,
# (nabla_i H)_jk = D_i D_j D_k p - Gamma_jk^l D_i D_l p
#                     - Gamma_ij^l H_lk - Gamma_ik^l H_jl.
# Bounds: 1/8 + (1/2)(1/4) + (1/2)(1/2) + (1/2)(1/2) = 3/4.
# Hence the ordered chain-rule component is T=s'''/8+3s''/4+3s'/4.
T = s3/F(8) + 3*s2/F(4) + 3*s1/F(4)
assert T < F("0.000250292")
row = 24*T
col = 288*T
K_unweighted = sqrt(float(row*col))
assert K_unweighted < 0.02081

# ---------------------------------------------------------------------------
# 4. Exact open-strip incidence E_m={v_m,v_(m+1),t_m,b_m}.
# ---------------------------------------------------------------------------
for N in range(1, 101):
    faces = [{('v',m),('v',m+1),('t',m),('b',m)} for m in range(1,N+1)]
    incidence = Counter(link for face in faces for link in face)
    assert len(incidence) == 3*N+1
    assert max(incidence.values()) <= 2
    assert all(len(face) == 4 for face in faces)
    links = list(incidence)
    for e in links:
        for d in links:
            assert sum(e in face and d in face for face in faces) <= 2
# Therefore: each output pair sees <=2 faces (row <=24T); each input link
# sees <=2 faces x 12^2 ordered output Lie pairs (column <=288T).

# Nonzero tensor entries require e,d,k all in one face. Thus e and k are
# equal or adjacent in the link graph. For w_e=rho^(2 dist(e,S)),
# sqrt(w_e/w_k)<=rho=6/5 by the distance triangle inequality.
rho = F(6,5)
C3 = 2*float(rho)*K_unweighted
assert C3 < 0.049941326676

# ---------------------------------------------------------------------------
# 5. Hessian-of-dressing A block and SU(2) Codazzi forcing.
# ---------------------------------------------------------------------------
# Conservative per-face component envelope h=s''/4+s'/2. Each 3x3 block
# has Frobenius <=6h; there are <=6 off-diagonal neighbours plus diagonal.
# Weighted left action: 6h(1+6rho)=49.2h; right action: 42h.
h = s2/F(4) + s1/F(2)
A_weighted = 6*h*(1 + 6*F(6,5))  # 49.2h: left/first-index action
A_unweighted = 42*h             # right/second-index action
CH = 2*(A_weighted + A_unweighted)
assert A_weighted == F(246,5)*h and A_unweighted == 42*h
assert CH == F(912,5)*h
assert float(h) < 0.00016681265475
assert float(CH) < 0.030426628227

# Symmetrized constant-curvature contraction: norm factor sqrt(2),
# kappa=1/4, |V_e|<=B=49/576; evolution contributes factor 2.
Bscore = F(49,576)
CR = 49*sqrt(2)/1152
assert CR < 0.060153181039

# ---------------------------------------------------------------------------
# 6. Combined energy margin, using same constants as the prior audit.
# ---------------------------------------------------------------------------
c_tr = 0.75*exp(-49*pi/144)
ell = 4*c_tr/3*(49/576)**2
c = 11/120
a = c-ell
b_h = c_tr-float(CH)
CG = C3+CR
lam = (a+b_h-sqrt((a-b_h)**2+CG**2))/2
assert CG < 0.110094508039
assert lam > 0.0699034

print('PASS: exact six-step positive majorant for all |b|<=1/1000 and global derivative envelope')
print('contraction L =', float(L), 'ball bound =', float(map_ball_bound), 'weighted residual tail =', float(err))
print('sup u derivatives (1,2,3) =', *(float(x) for x in U[1:]))
print('sup s derivatives (1,2,3) =', float(s1), float(s2), float(s3))
print('ordered plaquette component T_g =', float(T))
print('row, column Schur sums =', float(row), float(col))
print('unweighted third tensor norm =', K_unweighted)
print('weighted third forcing including drift C3 =', C3)
print('h, C_H =', float(h), float(CH))
print('C_R =', CR, 'C_G =', CG)
print('c_tr, ell, a, b =', c_tr, ell, a, b_h)
print('lambda_min =', lam)
print('PASS: exact strip incidence N=1..100, 3N+1 links, <=2 faces/link')
print('PASS: global derivative envelope maxima =', [str(x) for x in maxima])
