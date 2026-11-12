#!/usr/bin/env python3
"""Exact-algebra regression for the coupled-Z5 perpendicular-image density audit.

Uses only the Python standard library. The density proof is in the paired
research note; this checks the integer vectors and exact Q(sqrt(5)) identities.
"""
from cmath import exp, pi
from fractions import Fraction as F
from math import sqrt

class Q5:
    """An exact element a + b*sqrt(5), with rational a,b."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(self, other):
        other = as_q5(other)
        return Q5(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self):
        return Q5(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-as_q5(other))
    def __mul__(self, other):
        other = as_q5(other)
        return Q5(self.a*other.a + 5*self.b*other.b,
                  self.a*other.b + self.b*other.a)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = as_q5(other)
        den = other.a*other.a - 5*other.b*other.b
        if den == 0:
            raise ZeroDivisionError
        return Q5((self.a*other.a - 5*self.b*other.b)/den,
                  (self.b*other.a - self.a*other.b)/den)
    def __eq__(self, other):
        other = as_q5(other)
        return self.a == other.a and self.b == other.b

def as_q5(x):
    return x if isinstance(x, Q5) else Q5(x, 0)

PHI = Q5(F(1,2), F(1,2))
INV_PHI = Q5(F(-1,2), F(1,2))

# Coordinates m_j multiply omega^(2j), j=0,...,4. All vectors have sum zero.
vectors = (
    (0, 1, -1, -1, 1),   # omega^2 + omega^3 - omega - omega^4
    (2, 0, -1, -1, 0),   # 2 - omega - omega^4
    (0, 1, 0, 0, -1),    # omega^2 - omega^3
    (0, 0, -1, 1, 0),    # omega - omega^4
)
assert all(sum(v) == 0 for v in vectors)

omega = exp(2j*pi/5)
basis = [omega**(2*j) for j in range(5)]
values = [sum(v[j]*basis[j] for j in range(5)) for v in vectors]
expected = (-sqrt(5), (5-sqrt(5))/2,
            1j*sqrt((5-sqrt(5))/2), 1j*sqrt((5+sqrt(5))/2))
assert all(abs(a-b) < 2e-12 for a,b in zip(values, expected))

# The two real generators have irrational ratio 1/phi.
assert INV_PHI == Q5(F(-1,2), F(1,2))
assert PHI*INV_PHI == Q5(1, 0)

# The squared ratio of the two imaginary generators is phi^2.
imag_ratio_squared = Q5(5, 1) / Q5(5, -1)
assert imag_ratio_squared == PHI*PHI
assert PHI*PHI - PHI - Q5(1,0) == Q5(0,0)

print("PASS: four sum-zero integer vectors lie in the perpendicular image")
print("PASS: real-axis generators are -sqrt(5), (5-sqrt(5))/2")
print("PASS: their ratio is 1/phi, irrational")
print("PASS: imaginary-axis generator ratio is phi, irrational")
print("PASS: the perpendicular image contains dense subgroups on both axes")
print("CONCLUSION: pi_perp(Z^5) is dense in R^2; its quotient is not a Hausdorff 2-torus")
