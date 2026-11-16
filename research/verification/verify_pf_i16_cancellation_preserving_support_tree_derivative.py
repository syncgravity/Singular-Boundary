#!/usr/bin/env python3
"""Exact regression for the failed differentiated-cumulant cancellation.

The asymmetric two-state stationary chain gives a nonzero contribution from
the partition {{1,3},{2}} because the {1,3} marginal retains both sides of
the omitted 1--2 transition. All calculations use Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import product

P = F(1, 3)
RHO = F(1, 2)
LAM1 = F(2, 5)
LAM2 = F(3, 7)
VAR = P * (1 - P)
MU3 = P * (1 - P) * (1 - 2 * P)


def check_exact_counterexample():
    # Centered two-state coordinate X=Y-p. The interpolated transition
    # contracts its centered eigenfunction by lambda*rho.
    c1 = LAM1 * RHO
    c2 = LAM2 * RHO

    # A1=X0, A2=1+X1, A3=X2.
    m1 = F(0)
    m2 = F(1)
    m3 = F(0)
    m12 = c1 * VAR
    m23 = c2 * VAR
    m13 = c1 * c2 * VAR
    m123 = c1 * c2 * (VAR + MU3)

    cumulant = (
        m123 - m12 * m3 - m13 * m2 - m1 * m23
        + 2 * m1 * m2 * m3
    )
    expected_cumulant = LAM1 * LAM2 * RHO**2 * MU3
    assert cumulant == expected_cumulant

    # Mixed derivatives with respect to the two distinct edge parameters.
    d2_cumulant = RHO**2 * MU3
    d2_full_moment = RHO**2 * (VAR + MU3)
    partition_residual = d2_full_moment - d2_cumulant
    assert d2_cumulant == F(1, 54)
    assert d2_full_moment == F(2, 27)
    assert partition_residual == F(1, 18)
    assert partition_residual == RHO**2 * VAR
    print("PASS exact three-row counterexample:")
    print(f"  mixed derivative of cumulant = {d2_cumulant}")
    print(f"  mixed derivative of full moment = {d2_full_moment}")
    print(f"  omitted-row partition contribution = {partition_residual}")


def check_omitted_port_parameter_survives():
    # For a centered eigenfunction, K(lambda)=Pi+lambda Q multiplies
    # its correlation by lambda*rho. The marginal on ports 0 and 2
    # therefore depends on BOTH intervening transition parameters.
    for l1, l2 in product((F(0), F(1, 3), F(1)), repeat=2):
        marginal_02 = l1 * l2 * RHO**2 * VAR
        assert marginal_02 == l1 * l2 * F(1, 4) * VAR
        if l1 == 0 or l2 == 0:
            assert marginal_02 == 0
        else:
            assert marginal_02 != 0
    print("PASS omitted-port marginal depends on both intervening reset parameters")


def main():
    check_exact_counterexample()
    check_omitted_port_parameter_survives()


if __name__ == "__main__":
    main()
