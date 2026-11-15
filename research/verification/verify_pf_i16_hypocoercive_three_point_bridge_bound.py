#!/usr/bin/env python3
"""OU calibration for false bridge bound and corrected two-cut HGR target."""
from math import exp, sqrt


def ou_bridge_hgr_squared(a: float, t: float, T: float) -> float:
    """Exact HGR^2 between X_t and (X_0, X_T) for stationary unit OU."""
    if not (a > 0.0 and 0.0 < t < T):
        raise ValueError("Require a>0 and 0<t<T")
    left = exp(-2.0 * a * t)
    right = exp(-2.0 * a * (T - t))
    total = exp(-2.0 * a * T)
    return 1.0 - ((1.0 - left) * (1.0 - right)) / (1.0 - total)


def main() -> None:
    a, T, claimed_lambda = 1.0, 2.0, 1.0
    for t in (0.01, 0.2, 0.5, 1.0, 1.5, 1.99):
        rho = sqrt(ou_bridge_hgr_squared(a, t, T))
        q_left = exp(-a * t)
        q_right = exp(-a * (T - t))
        two_cut_bound = (q_left + q_right) / (1.0 + q_left * q_right)
        assert rho <= two_cut_bound + 1e-13

    # The proposed square-root bound fails near an endpoint.
    t = 0.01
    rho = sqrt(ou_bridge_hgr_squared(a, t, T))
    endpoint_lower = exp(-a * t)
    proposed_upper = sqrt(
        1.0 - exp(-2.0 * claimed_lambda * min(t, T - t))
    )
    assert rho + 1e-14 >= endpoint_lower
    assert rho > proposed_upper
    print("PASS: OU satisfies the two-cut tanh calibration on the test grid")
    print("PASS: OU refutes sqrt(1-exp(-2 lambda min(t,T-t))) near the endpoint")
    print(f"rho_HGR={rho:.12f}; endpoint_lower={endpoint_lower:.12f}")
    print(f"incorrect_proposed_upper={proposed_upper:.12f}")
    print("SCOPE: finite numerical calibration, not a general semigroup proof")


if __name__ == "__main__":
    main()
