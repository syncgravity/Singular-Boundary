#!/usr/bin/env python3
"""Numerical calibration: the proposed three-point bridge HGR bound fails for OU."""
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
    a, T, t, claimed_lambda = 1.0, 2.0, 0.01, 1.0
    rho = sqrt(ou_bridge_hgr_squared(a, t, T))
    claimed_upper = sqrt(1.0 - exp(-2.0 * claimed_lambda * min(t, T - t)))
    endpoint_lower = exp(-a * t)

    # Conditioning on both endpoints is at least as informative as X_0 alone.
    assert rho + 1e-14 >= endpoint_lower
    # The proposed upper bound is violated by a large margin.
    assert rho > claimed_upper
    # Endpoint limit: rho -> 1 while the proposed right side -> 0.
    print("PASS: reversible stationary OU refutes the proposed bridge bound")
    print(f"rho_HGR={rho:.12f}")
    print(f"rho(X_0,X_t)={endpoint_lower:.12f}")
    print(f"proposed_upper={claimed_upper:.12f}")
    print("SCOPE: rejects only the stated sqrt(1-exp(-2 lambda min(t,T-t))) bound")


if __name__ == "__main__":
    main()
