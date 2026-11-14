#!/usr/bin/env python3
"""Exact-rational algebra checks for the PF-I16 radial/Casimir audit.

This verifies the displayed perturbative coefficient equations and the
low-spin Casimir eigenvalues only. It does not bound the character tail,
projective tensor norm, actual-insertion QF, or any cluster expansion.
"""
from fractions import Fraction as F


def radial_operator(poly):
    """Apply L[R]=(1-p^2)R' - 3 p R to a sparse {degree: coefficient} map."""
    out = {}
    for degree, coeff in poly.items():
        if degree:
            out[degree - 1] = out.get(degree - 1, F(0)) + degree * coeff
            out[degree + 1] = out.get(degree + 1, F(0)) - degree * coeff
        out[degree + 1] = out.get(degree + 1, F(0)) - 3 * coeff
    return {k: v for k, v in out.items() if v}


def clean(poly):
    return {k: v for k, v in poly.items() if v}


# R_1=4/3 solves L[R_1]=-4p.
R1 = {0: F(4, 3)}
assert clean(radial_operator(R1)) == {1: F(-4, 1)}

# lambda_2=-(3/4)R_1^2=-4/3 and R_2=-16p/9.
lambda2 = -F(3, 4) * R1[0] ** 2
assert lambda2 == F(-4, 3)
R2 = {1: F(-16, 9)}
assert clean(radial_operator(R2)) == {0: F(-16, 9), 2: F(64, 9)}

# Character-gradient identities: chi_1=2p, chi_2=4p^2-1.
# R_1 grad(p)=(2/3) grad(chi_1);
# R_2 p grad(p)=(-2/9) grad(chi_2).
assert F(4, 3) == 2 * F(2, 3)
assert F(-16, 9) == 8 * F(-2, 9)

def casimir(j):
    return j * (j + 1)


def omega_eigenvalues(j, k):
    lo = abs(j - k)
    hi = j + k
    # j,k are half-integers; step through allowed total spins.
    count = int(hi - lo)
    return [
        (J, F(1, 2) * (casimir(j) + casimir(k) - casimir(J)))
        for J in (lo + n for n in range(count + 1))
    ]


def omega_norm(j, k):
    return max(abs(value) for _, value in omega_eigenvalues(j, k))


assert omega_eigenvalues(F(1, 2), F(1, 2)) == [
    (F(0), F(3, 4)), (F(1), F(-1, 4))
]
assert omega_norm(F(1, 2), F(1, 2)) == F(3, 4)
assert omega_norm(F(1, 2), F(1)) == F(1)
assert omega_norm(F(1), F(1)) == F(2)

print("PASS: exact first- and second-order radial coefficient equations")
print("PASS: lambda_2=-4/3 and the two displayed character-gradient coefficients")
print("PASS: shared-link Casimir contraction norms (1/2,1/2)=3/4, (1/2,1)=1, (1,1)=2")
print("SCOPE: no character-tail, projective-norm, QF, WDG, KP, or mass-gap claim")
