#!/usr/bin/env python3
"""Verify normalized C5 family weights and gauge invariance of closed-loop inputs."""
import math
import numpy as np

PHI = (1 + math.sqrt(5)) / 2
RHO = PHI ** -2
OMEGA = np.exp(2j * math.pi / 5)
J = np.arange(5)

def weights(n):
    theta = 2 * math.pi * RHO * n
    return math.sqrt(2 / 5) * np.cos(4 * math.pi * J / 5 - theta)

def random_su2(rng):
    q = rng.normal(size=4)
    q = q / np.linalg.norm(q)
    a, b, c, d = q
    return np.array([[a + 1j*d, c + 1j*b],
                     [-c + 1j*b, a - 1j*d]], dtype=complex)

def holonomy(links):
    out = np.eye(2, dtype=complex)
    for link in links:
        out = out @ link
    return out

def defect(links):
    return float(1 - 0.5 * np.trace(holonomy(links)).real)

checks = 0
for n in range(1, 101):
    u = weights(n)
    assert abs(np.dot(u, u) - 1) < 1e-12
    assert abs(u.sum()) < 1e-12
    z1 = np.dot(u, OMEGA ** J)
    z2 = np.dot(u, OMEGA ** (2 * J))
    theta = 2 * math.pi * RHO * n
    assert abs(z1) < 1e-12
    assert abs(z2 - math.sqrt(5/2) * np.exp(1j * theta)) < 1e-12
    checks += 4

# C5 covariance of the observer frame and its scalar family contraction.
theta = 0.731
u0 = math.sqrt(2/5) * np.cos(4 * math.pi * J / 5 - theta)
u1 = math.sqrt(2/5) * np.cos(4 * math.pi * J / 5 - (theta + 4 * math.pi / 5))
assert np.max(np.abs(u1 - np.roll(u0, 1))) < 1e-12
F = np.array([0.13, 0.82, 0.37, 1.12, 0.61])
assert abs(np.dot(np.roll(u0, 1), np.roll(F, 1)) - np.dot(u0, F)) < 1e-12
checks += 2

# Synthetic closed SU(2) Wilson loops: local gauge transformations conjugate
# each loop holonomy at its basepoint, preserving its trace and defect.
rng = np.random.default_rng(419)
family_defects = []
family_defects_gauged = []
for family in range(5):
    vals = []
    vals_gauged = []
    for loop_index in range(4):
        length = 5 + (family + loop_index) % 4
        links = [random_su2(rng) for _ in range(length)]
        gauge = [random_su2(rng) for _ in range(length)]
        transformed = [
            gauge[k] @ links[k] @ gauge[(k + 1) % length].conj().T
            for k in range(length)
        ]
        H = holonomy(links)
        Hg = holonomy(transformed)
        assert abs(np.trace(H).imag) < 1e-12
        assert abs(np.trace(Hg).imag) < 1e-12
        assert abs(np.trace(H) - np.trace(Hg)) < 1e-11
        vals.append(defect(links))
        vals_gauged.append(defect(transformed))
        checks += 1
    family_defects.append(float(np.mean(vals)))
    family_defects_gauged.append(float(np.mean(vals_gauged)))

F = np.asarray(family_defects)
Fg = np.asarray(family_defects_gauged)
assert np.max(np.abs(F - Fg)) < 1e-11
checks += 1

# O_n(t)=sum_j u_j(n) F_j(t); full-family average is a separate control.
for n in range(1, 14):
    u = weights(n)
    O = float(np.dot(u, F))
    Og = float(np.dot(u, Fg))
    assert abs(O - Og) < 1e-11
    assert abs(O) <= 2 * math.sqrt(5) + 1e-12
    checks += 2
full = float(np.mean(F))
full_gauged = float(np.mean(Fg))
assert abs(full - full_gauged) < 1e-11
checks += 1

print(f"PASS {checks} normalized C5 family-weight and closed-SU2-loop gauge checks")
print(f"rho={RHO:.15f}; family_defects={F.tolist()}")
print(f"observer_O_n1={float(np.dot(weights(1), F)):.12f}; full_control={full:.12f}")
print("Design test only: source-authenticated loop catalogue and family labels are required for Stage 26.")
