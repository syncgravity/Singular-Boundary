#!/usr/bin/env python3
"""Verify the two-link distinction between row-sum and row-product cumulants."""
from fractions import Fraction
from itertools import product


states = list(product((-1, 1), repeat=2))


def mean(values):
    return sum((Fraction(value) for value in values), Fraction(0)) / len(states)


u1 = [state[0] for state in states]
u2 = [state[1] for state in states]
products = [a * b for a, b in zip(u1, u2)]
row_sums = [a + b for a, b in zip(u1, u2)]

product_covariance = mean(a * b for a, b in zip(products, products)) - mean(products) ** 2
row_sum_covariance = mean(a * b for a, b in zip(row_sums, row_sums)) - mean(row_sums) ** 2

# Each independent link contributes (1 + z1*z2) to P_{1,2}.
one_link_factor = {(0, 0): 1, (1, 1): 1}
two_link_factor = {}
for (a1, b1), c1 in one_link_factor.items():
    for (a2, b2), c2 in one_link_factor.items():
        key = (a1 + a2, b1 + b2)
        two_link_factor[key] = two_link_factor.get(key, 0) + c1 * c2
square_free_row_coefficient = two_link_factor[(1, 1)]

assert product_covariance == 1
assert row_sum_covariance == 2
assert square_free_row_coefficient == row_sum_covariance
assert square_free_row_coefficient != product_covariance

print("PASS: product-insertion covariance is 1")
print("PASS: auxiliary row-sum covariance and [z1*z2] P_{1,2} are 2")
print("LIMIT: the row-factorized coefficient does not encode the product cumulant")
