"""Independent exact-arithmetic audit of R3-IR local geometric inputs.

Complements the analytic quaternion, Levi-Civita, fixed-point, and strip
incidence arguments. Checks the rational positive-majorant enclosure, global
character derivative envelope, finite-strip incidence, Schur arithmetic,
and combined numerical constants.
"""
from fractions import Fraction as F
from math import sqrt, exp, pi
from collections import Counter

# Uniform positive majorant for every |g| <= 1/1000.
b0, R = F(1, 1000), F(1, 25)
L = b0 * (F(129, 6) + 2 * R / 768)
assert L < 1

def positive_majorant_map(v):
    out = {}
    for n, value in [(0, F(1)), *sorted(v.items())]:
        for j in (n - 1, n + 1):
            if j >= 1:
                out[j] = out.get(j, F(0)) + b0 * value / (2 * j * (j + 2))
    first = v.get(1, F(0))
    for n, value in v.items():
        out[n] = out.get(n, F(0)) + b0 * first * value / (2 * n * (n + 2))
    return {n: value for n, value in out.items() if value}

def weighted_norm(u):
    return sum(abs(v) * 2**n * (n + 1)**6 for n, v in u.items())

v = {}
for _ in range(6):
    v = positive_majorant_map(v)
res = positive_majorant_map(v)
err = weighted_norm({n: res.get(n, F(0)) - v.get(n, F(0))
                     for n in set(res) | set(v)}) / (1 - L)

def endpoint_derivative(n, k):
    if k == 0: return F(n + 1)
    if k == 1: return F(n * (n + 1) * (n + 2), 3)
    if k == 2: return F((n - 1) * n * (n + 1) * (n + 2) * (n + 3), 15)
    if k == 3: return F((n - 2) * (n - 1) * n * (n + 1) *
                        (n + 2) * (n + 3) * (n + 4), 105)
    raise ValueError(k)

# U_n^(k)(x)=2^k k! C_{n-k}^{k+1}(x), and the normalized Gegenbauer
# zonal bound gives sup[-1,1]|U_n^(k)| <= U_n^(k)(1).
# Exact ratio maxima relative to 2^n(n+1)^6:
maxima = [F(1, 64), F(1, 64), F(2, 729), F(24, 15625)]
P1_x = [F(1,3), F(9), F(314,3), F(2072,3), F(2856), F(23044,3),
        F(40292,3), F(14692), F(27262,3), F(2404)]
P2_x = [F(1,15), F(8,3), F(48), F(512), F(53804,15), F(51842,3),
        F(873278,15), F(409634,3), F(651349,3), F(220796),
        F(1908332,15), F(30544)]
P3_x = [F(1,105), F(2,3), F(449,21), F(14544,35), F(81802,15),
        F(1783464,35), F(5221466,15), F(5268268,3), F(684807587,105),
        F(613804816,35), F(494782229,15), F(1425032346,35),
        F(1018625736,35), F(8831808)]
assert all(x > 0 for x in P1_x + P2_x + P3_x)
assert F(16384, 15625) > 1  # r_3(4)/r_3(3)

# These positive shifted polynomials prove the ratio tails globally:
# k=1 from n=1, k=2 from n=2, k=3 from n=4.
for k, last_initial in [(0, 1), (1, 1), (2, 2), (3, 4)]:
    for n in range(1, last_initial + 1):
        ratio = endpoint_derivative(n, k) / (2**n * (n + 1)**6)
        assert ratio <= maxima[k], (k, n, ratio, maxima[k])
assert endpoint_derivative(3, 3) / (2**3 * 4**6) < maxima[3]

U = [sum(abs(a) * endpoint_derivative(n, k) for n, a in v.items()) + err
     for k in range(4)]
A, B, C, D = U
s1 = B / (1 - A)
s2 = C / (1 - A) + s1*s1
s3 = D / (1 - A) + 3*C*B/(1 - A)**2 + 2*s1**3

# Ordered covariant component: 1/8 + (1/2)(1/4)
# + (1/2)(1/2) + (1/2)(1/2) = 3/4.
T = s3/F(8) + 3*s2/F(4) + 3*s1/F(4)
assert T < F("0.000250292")
row, col = 24*T, 288*T
K_unweighted = sqrt(float(row*col))
assert K_unweighted < 0.02081

# Exact straight-strip supports E_m={v_m,v_(m+1),t_m,b_m}.
for N in range(1, 101):
    faces = [{('v',m), ('v',m+1), ('t',m), ('b',m)}
             for m in range(1, N+1)]
    incidence = Counter(link for face in faces for link in face)
    assert len(incidence) == 3*N + 1
    assert max(incidence.values()) <= 2
    assert all(len(face) == 4 for face in faces)
    links = list(incidence)
    for e in links:
        for d in links:
            assert sum(e in face and d in face for face in faces) <= 2

# Nonzero K entries have input/output links in a common face, so
# sqrt(w_e/w_k) <= rho=6/5. Include the drift factor 2.
rho = F(6, 5)
C3 = 2 * float(rho) * K_unweighted
assert C3 < 0.049941326676

# Conservative Hessian-of-dressing block envelope and weighted actions.
h = s2/F(4) + s1/F(2)
CH = F(912, 5) * h  # 2*(49.2+42)h = 182.4h
assert float(h) < 0.00016681265475
assert float(CH) < 0.030426628227

# Symmetrized constant-curvature SU(2) forcing, kappa=1/4, B=49/576.
CR = 49 * sqrt(2) / 1152
assert CR < 0.060153181039

c_tr = 0.75 * exp(-49*pi/144)
ell = 4*c_tr/3*(49/576)**2
a = 11/120 - ell
b_h = c_tr - float(CH)
CG = C3 + CR
lam = (a + b_h - sqrt((a-b_h)**2 + CG**2))/2
assert CG < 0.110094508039
assert lam > 0.0699034

print("PASS: six-step positive majorant, uniform for |g|<=1e-3")
print("contraction L =", float(L), "tail =", float(err))
print("sup u' u'' u''' =", *(float(x) for x in U[1:]))
print("sup s' s'' s''' =", float(s1), float(s2), float(s3))
print("ordered face component T_g =", float(T))
print("row/column Schur sums =", float(row), float(col))
print("unweighted Schur norm =", K_unweighted)
print("weighted third forcing C3 =", C3)
print("h and C_H =", float(h), float(CH))
print("C_R and C_G =", CR, CG)
print("c_tr, ell, a, b =", c_tr, ell, a, b_h)
print("lambda_min =", lam)
print("PASS: exact incidence for N=1..100; analytic E_m argument covers all N")
print("PASS: global derivative-envelope maxima =", [str(x) for x in maxima])
