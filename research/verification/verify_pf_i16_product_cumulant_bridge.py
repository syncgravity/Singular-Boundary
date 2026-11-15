#!/usr/bin/env python3
"""Verify square-free versus top-degree extraction for a two-link product cumulant."""
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


def multiply(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            key = (i + k, j + ell)
            result[key] = result.get(key, Fraction(0)) + a * b
    return result


def add(left, right):
    result = dict(left)
    for degree, coefficient in right.items():
        result[degree] = result.get(degree, Fraction(0)) + coefficient
    return result


def scale(poly, scalar):
    return {degree: scalar * coefficient for degree, coefficient in poly.items()}


def subtract(left, right):
    result = dict(left)
    for degree, coefficient in right.items():
        result[degree] = result.get(degree, Fraction(0)) - coefficient
    return result


def truncate_bidegree(poly, max_i=2, max_j=2):
    return {
        degree: coefficient
        for degree, coefficient in poly.items()
        if degree[0] <= max_i and degree[1] <= max_j and coefficient
    }


y1 = [{(0, 0): 1, (1, 0): a + b, (2, 0): a * b} for a, b in states]
y2 = [{(0, 0): 1, (0, 1): a + b, (0, 2): a * b} for a, b in states]

expected_y1y2 = {}
for left, right in zip(y1, y2):
    expected_y1y2 = add(expected_y1y2, multiply(left, right))
expected_y1y2 = scale(expected_y1y2, Fraction(1, len(states)))
expected_y1 = {}
expected_y2 = {}
for poly in y1:
    expected_y1 = add(expected_y1, poly)
for poly in y2:
    expected_y2 = add(expected_y2, poly)
expected_y1 = scale(expected_y1, Fraction(1, len(states)))
expected_y2 = scale(expected_y2, Fraction(1, len(states)))
polynomial_covariance = subtract(expected_y1y2, multiply(expected_y1, expected_y2))

# Asymmetric two-row example: both supports contain both independent links.
asymmetric_y1 = []
asymmetric_y2 = []
product_row1 = []
product_row2 = []
for u, v in states:
    f11, f12 = -1 - u, -1 - v
    f21, f22 = -1 - u, 1
    asymmetric_y1.append(
        {(0, 0): 1, (1, 0): f11 + f12, (2, 0): f11 * f12}
    )
    asymmetric_y2.append(
        {(0, 0): 1, (0, 1): f21 + f22, (0, 2): f21 * f22}
    )
    product_row1.append(f11 * f12)
    product_row2.append(f21 * f22)

asymmetric_joint = {}
asymmetric_mean1 = {}
asymmetric_mean2 = {}
for left, right in zip(asymmetric_y1, asymmetric_y2):
    asymmetric_joint = add(asymmetric_joint, multiply(left, right))
    asymmetric_mean1 = add(asymmetric_mean1, left)
    asymmetric_mean2 = add(asymmetric_mean2, right)
asymmetric_joint = scale(asymmetric_joint, Fraction(1, len(states)))
asymmetric_mean1 = scale(asymmetric_mean1, Fraction(1, len(states)))
asymmetric_mean2 = scale(asymmetric_mean2, Fraction(1, len(states)))
asymmetric_covariance = subtract(
    asymmetric_joint, multiply(asymmetric_mean1, asymmetric_mean2)
)
product_mean1 = mean(product_row1)
product_mean2 = mean(product_row2)
product_covariance_asymmetric = (
    mean(a * b for a, b in zip(product_row1, product_row2))
    - product_mean1 * product_mean2
)

# P_{1,2} = u_{1,2} / (u_1*u_2) for the two-row Boolean ratio.
inverse_mean1 = {(0, 0): 1, (1, 0): 2, (2, 0): 3}  # (1-s)^(-2)
inverse_mean2 = {(0, 0): 1, (0, 2): 1}  # (1-t^2)^(-1)
inverse_product_means = multiply(inverse_mean1, inverse_mean2)
asymmetric_ratio_minus_one = truncate_bidegree(
    multiply(asymmetric_covariance, inverse_product_means)
)
asymmetric_boolean_ratio = add({(0, 0): 1}, asymmetric_ratio_minus_one)
boolean_ratio_top_coefficient = asymmetric_boolean_ratio.get((2, 2), Fraction(0))
reconstructed_asymmetric_joint = truncate_bidegree(
    multiply(
        asymmetric_boolean_ratio,
        multiply(asymmetric_mean1, asymmetric_mean2),
    )
)

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
assert polynomial_covariance[(1, 1)] == 2
assert polynomial_covariance[(2, 2)] == product_covariance
assert {k: v for k, v in asymmetric_mean1.items() if v} == {
    (0, 0): 1,
    (1, 0): -2,
    (2, 0): 1,
}
assert {k: v for k, v in asymmetric_mean2.items() if v} == {
    (0, 0): 1,
    (0, 2): -1,
}
assert {k: v for k, v in asymmetric_covariance.items() if v} == {
    (1, 1): 1,
    (1, 2): 1,
    (2, 1): -1,
    (2, 2): -1,
}
assert product_covariance_asymmetric == -1
assert boolean_ratio_top_coefficient == 1
assert boolean_ratio_top_coefficient != product_covariance_asymmetric
assert reconstructed_asymmetric_joint == truncate_bidegree(asymmetric_joint)

print("PASS: product-insertion covariance is 1")
print("PASS: auxiliary row-sum covariance and [z1*z2] P_{1,2} are 2")
print("PASS: top-degree coefficient of the full row-polynomial covariance is 1")
print("PASS: asymmetric example has product covariance -1 but Boolean ratio top coefficient 1")
print("PASS: the full Boolean ratio reconstructs the joint moment polynomial")
print("LIMIT: higher quasi-factorization coefficients still need uniform weighted bounds")
