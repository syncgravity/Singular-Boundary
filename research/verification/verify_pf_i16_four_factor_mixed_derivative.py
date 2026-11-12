#!/usr/bin/env python3
"""Independent quaternion audit of PF-I16 four-factor SU(2) mixed derivatives."""
import numpy as np

SEED = 20261111
NTRIAL = 20
EPS = 1.0e-6
rng = np.random.default_rng(SEED)

def qnorm(q):
    return q / np.linalg.norm(q)

def qmul(a, b):
    return np.r_[a[0]*b[0] - np.dot(a[1:], b[1:]),
                 a[0]*b[1:] + b[0]*a[1:] + np.cross(a[1:], b[1:])]

def qinv(q):
    return np.r_[q[0], -q[1:]]

def qexp(x):
    t = np.linalg.norm(x)
    if t == 0:
        return np.array([1., 0., 0., 0.])
    return np.r_[np.cos(t), np.sin(t)*x/t]

def adjoint(q, x):
    return qmul(qmul(q, np.r_[0., x]), qinv(q))[1:]

def bracket(x, y):
    # Components in the radius-two orthonormal basis (i,j,k)/2.
    return 2.0*np.cross(x, y)

def factor(U, sign):
    return U if sign == 1 else qinv(U)

def factor_velocity(U, xi, sign):
    return xi if sign == 1 else -adjoint(U, xi)

def transported_components(Us, xis, signs):
    xs = [factor(U, s) for U, s in zip(Us, signs)]
    Xs = [factor_velocity(U, xi, s) for U, xi, s in zip(Us, xis, signs)]
    etas = []
    for i in range(4):
        suffix = np.array([1., 0., 0., 0.])
        for x in xs[i+1:]:
            suffix = qmul(suffix, x)
        etas.append(adjoint(qinv(suffix), Xs[i]))
    return etas

worst, cases = 0.0, 0
for mask in range(16):
    signs = [1 if (mask >> i) & 1 else -1 for i in range(4)]
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            for _ in range(NTRIAL):
                Us = [qnorm(rng.normal(size=4)) for _ in range(4)]
                xis = [rng.normal(size=3) for _ in range(4)]
                eta = transported_components(Us, xis, signs)
                moved = list(Us)
                moved[i] = qmul(Us[i], qexp(EPS*xis[i]))
                eta_moved = transported_components(moved, xis, signs)
                derivative = (eta_moved[j] - eta[j])/EPS
                target = np.zeros(3) if i < j else -bracket(eta[i], eta[j])
                worst = max(worst, np.linalg.norm(derivative-target))
                cases += 1

signs = [-1, 1, -1, 1]
Us = [qnorm(rng.normal(size=4)) for _ in range(4)]
xis = [rng.normal(size=3) for _ in range(4)]
eta = transported_components(Us, xis, signs)
def convergence_error(step):
    moved = list(Us)
    moved[3] = qmul(Us[3], qexp(step*xis[3]))
    moved_eta = transported_components(moved, xis, signs)
    return np.linalg.norm((moved_eta[0]-eta[0])/step + bracket(eta[3], eta[0]))

e1, e2 = convergence_error(1.e-4), convergence_error(5.e-5)
assert cases == 3840
assert worst < 1.e-4, worst
assert e2 < .7*e1, (e1, e2)
print(f"PASS: {cases} orientation/ordered-pair quaternion finite differences")
print(f"PASS: max absolute derivative residual < {worst:.6e}")
print(f"PASS: halving step reduces error ({e1:.6e} -> {e2:.6e})")
print("ANALYTIC: ∇_X Y = D_X Y + 1/2[X,Y] in left trivialization")
print("ANALYTIC: mixed covariant derivative is +1/2 bracket for i<j,")
print("          -1/2 bracket for i>j, and zero for i=j.")
print("LIMIT: group-product sign/trivialization only; no continuum gate closes.")
