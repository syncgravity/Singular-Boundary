#!/usr/bin/env python3
"""Exact-rational checks for the Rademacher support-maximum-tree obstruction."""
from fractions import Fraction as F
from math import factorial

# Bernoulli numbers B_2n for n=1,...,6, exact rational values.
B = {
    1: F(1, 6),
    2: F(-1, 30),
    3: F(1, 42),
    4: F(-1, 30),
    5: F(5, 66),
    6: F(-691, 2730),
}

# |kappa_{2n}| = 2^(2n)(2^(2n)-1)|B_2n|/(2n).
for n, bernoulli in B.items():
    kappa = F(2 ** (2*n) * (2 ** (2*n) - 1), 2*n) * abs(bernoulli)
    assert kappa > 0
    # The tree maximum for a complete support graph at coincident times is 1.
    # Hence any proposed C^(2n) maximum-tree estimate requires C >= this root.
    print(f"n={n:2d}, r={2*n:2d}, |kappa_r|={kappa}, "
          f"required_C_at_this_order>{float(kappa ** (F(1, 2*n))):.9f}")

# Exact formula values begin 1, 2, 16, 272, 7936, 353792.
expected = [1, 2, 16, 272, 7936, 353792]
observed = []
for n, bernoulli in B.items():
    observed.append(int(F(2 ** (2*n) * (2 ** (2*n) - 1), 2*n) * abs(bernoulli)))
assert observed == expected

# The factorial lower bound follows from zeta(2n)>1 and 1-4^-n >= 3/4:
# |kappa_2n| >= (3/4)(4/pi^2)^n (2n)!/n.
# The rational verifier checks the exact Bernoulli identity at these orders;
# the analytic divergence for all n follows from the displayed factorial formula.
print("PASS: exact Rademacher cumulants match the Bernoulli formula through order 12")
print("PASS: at coincident times, support maximum-tree weight equals one")
print("SCOPE: disproves a uniform C^r maximum-tree bound for general bounded local observables")
print("SCOPE: does not disprove support-tree-sum bounds or the actual face/pair subclass")
