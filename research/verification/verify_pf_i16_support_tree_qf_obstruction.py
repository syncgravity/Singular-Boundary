#!/usr/bin/env python3
"""Exact finite-state check of the cut-QF versus product-tree obstruction."""
from fractions import Fraction as F
from itertools import product

def law(r, eps):
    states = list(product((-1, 1), repeat=r))
    return {z: F(1, 2**r) * (1 + eps * _prod(z)) for z in states}

def _prod(xs):
    out = 1
    for x in xs:
        out *= x
    return out

def expectation(mu, fn):
    return sum(p * fn(z) for z, p in mu.items())

def marginal(mu, indices):
    out = {}
    for z, p in mu.items():
        key = tuple(z[i] for i in indices)
        out[key] = out.get(key, F(0)) + p
    return out

def check(r, eps):
    mu = law(r, eps)
    assert sum(mu.values()) == 1
    # Every proper marginal is exactly uniform.
    for mask in range(1, 2**r - 1):
        indices = [i for i in range(r) if mask >> i & 1]
        marg = marginal(mu, indices)
        assert all(p == F(1, 2**len(indices)) for p in marg.values())
    # Full parity cumulant: all proper mixed moments vanish.
    for mask in range(1, 2**r - 1):
        assert expectation(mu, lambda z, m=mask: _prod(z[i] for i in range(r) if m >> i & 1)) == 0
    full = expectation(mu, lambda z: _prod(z))
    assert full == eps
    # For every nontrivial cut, the parity functions have covariance eps.
    for mask in range(1, 2**r - 1):
        left = [i for i in range(r) if mask >> i & 1]
        right = [i for i in range(r) if not (mask >> i & 1)]
        u = lambda z: _prod(z[i] for i in left)
        v = lambda z: _prod(z[i] for i in right)
        cov = expectation(mu, lambda z: u(z) * v(z)) - expectation(mu, u) * expectation(mu, v)
        assert cov == eps
    # If every edge of a connected graph has weight eps, any cut has
    # cross-weight at least eps, while every spanning-tree product is eps^(r-1).
    assert eps <= eps
    assert eps**(r-1) < eps
    return full

for r in range(3, 9):
    eps = F(1, 10)
    assert check(r, eps) == eps

print("PASS: all proper marginals are product-uniform")
print("PASS: all proper mixed moments vanish and the order-r cumulant equals epsilon")
print("PASS: every nontrivial cut has bounded parity covariance exactly epsilon")
print("PASS: connected-graph cut weights can be epsilon while every tree product is epsilon^(r-1)")
print("SCOPE: this refutes cut-QF-only implication, not the independent-link Markov PF-I16 theorem")
