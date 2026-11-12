#!/usr/bin/env python3
"""Verify the five-family Z2 observer frame and its independent 3D lift."""
import math
import numpy as np

PHI = (1 + math.sqrt(5)) / 2
M1 = np.array([[1, 1], [1, 0]], dtype=float)
eig = np.linalg.eigvals(M1)
lam_plus = max(eig.real)
lam_minus = min(eig.real)
rho = abs(lam_minus / lam_plus)
assert abs(rho - PHI ** -2) < 1e-14

omega = np.exp(2j * math.pi / 5)
j = np.arange(5)
indices = np.arange(1, 1601)
theta = 2 * math.pi * rho * indices
amp = np.sqrt(indices)
W = amp[:, None] * np.cos(4 * math.pi * j[None, :] / 5 - theta[:, None])

s = W.sum(axis=1) / math.sqrt(5)
z1 = W @ (omega ** j)
z2 = W @ (omega ** (2 * j))
expected_z2 = 2.5 * amp * np.exp(1j * theta)
assert np.max(np.abs(s) / amp) < 1e-12
assert np.max(np.abs(z1) / amp) < 1e-12
assert np.max(np.abs(z2 - expected_z2) / amp) < 1e-12

# Orthonormal Fourier coordinate and the observer's three-dimensional state.
Z2 = math.sqrt(2 / 5) * z2
h, T = 0.7, 0.2  # explicit model scales, not source constants
longitudinal = h * indices
clock = T * indices
Gamma = np.column_stack((longitudinal, Z2.real, Z2.imag))
assert np.allclose(np.diff(longitudinal), h)
assert np.allclose(np.diff(clock), T)
assert np.max(np.abs(np.diff(longitudinal) / np.diff(clock) - h / T)) < 1e-10

# C5 covariance: theta -> theta+4pi/5 cyclically relabels the five families.
test_theta = np.linspace(0, 2 * math.pi, 101)
W0 = np.cos(4 * math.pi * j[None, :] / 5 - test_theta[:, None])
W1 = np.cos(4 * math.pi * j[None, :] / 5 - (test_theta[:, None] + 4 * math.pi / 5))
assert np.max(np.abs(W1 - np.roll(W0, 1, axis=1))) < 1e-12

# Equal-area radial law and Fibonacci near-return residuals.
area = math.pi * np.abs(Z2) ** 2
assert np.max(np.abs(np.diff(area) - math.pi * (5 / 2))) < 1e-8
fib = [0, 1]
for _ in range(2, 11):
    fib.append(fib[-1] + fib[-2])
res34 = 2 * math.pi * (34 * rho - fib[7])
res55 = 2 * math.pi * (55 * rho - fib[8])
assert abs(res34 + 2 * math.pi * PHI ** -9) < 1e-12
assert abs(res55 - 2 * math.pi * PHI ** -10) < 1e-12
assert res34 < 0 < res55

checks = 12
print(f"rho={rho:.15f}; phi^-2={PHI**-2:.15f}")
print(f"z2(n)=(5/2)*sqrt(n)*exp(i*2*pi*rho*n); max projection error={np.max(np.abs(z2-expected_z2)):.3e}")
print(f"C5 covariance: PASS; equal-area increment={math.pi*2.5:.12f}")
print(f"3D lift: s_n={h}*n, t_n={T}*n, longitudinal speed={h/T}")
print(f"34 residual={res34:.12e}; 55 residual={res55:.12e}")
print(f"PASS {checks} family-frame and 3D-lift checks")
