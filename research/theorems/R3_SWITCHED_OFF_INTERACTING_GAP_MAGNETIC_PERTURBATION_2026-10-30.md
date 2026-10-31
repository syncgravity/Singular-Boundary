# R3-IR-523: finite switched-off interacting gap by magnetic norm perturbation

Date 2026-10-30. Assume the finite compact gauge-covariant inverse-Whitney electric Hamiltonian H_E has unique constant zero state and first excited spectral energy at least gamma=3g2_squared/(8 lambda_max(M)). Consider H0=H_E+V0 with V0=-sum_(j!=f)b_j p_j and B0=sum b_j, so -B0<=V0<=B0. Since the constant electric vacuum has zero expectation of each fundamental plaquette character, E0(H0)<=0. Min-max gives lambda_1(H0)>=lambda_1(H_E)-B0>=gamma-B0. Therefore the *interacting switched-off gap* Delta0=lambda_1(H0)-E0(H0)>=gamma-B0, which is positive whenever B0<gamma. This bound is sharper than the generic gamma-2B0 Weyl estimate because the variational reference E0<=0 is known.

Combining the electric-vacuum ground-state comparison R3-IR-514 with the direct ground-state event shift R3-IR-522, for selected local coupling b>=0 and center flip at b=0, yields for all measurable events A:
Prob_(Omega_b)(A)>=[Prob_Haar(A)-sqrt(B0/gamma)-sqrt(b/(gamma-B0))]_+.
For a selected four-link plaquette cap Cdelta, Prob_Haar(Cdelta)=c_delta exactly. This is rigorous at each finite graph if gamma>B0; no interval-certified numerical eigenvalue estimate is claimed.

For the archived 30-link 11-face disk, g2_squared=1, B0=9*3/32000, b=3/32000 and lambda_max(M)=1.1046593441618966, approximate numbers: gamma=.3394711699872615, gamma-B0=.33862741998726154, baseline probability error=.04985462390154264, local event error=.01663889868606366, cap lower at delta=.2 is .03759451607422154 (delta=.1 yields zero). Numeric values are double precision.

Strong magnetic coupling or increasing face count defeats the condition B0<gamma; the estimate is a weak-magnetic finite-volume result, NOT refinement uniform. This is a spectral gap for an interacting finite regulator, not the 3+1D continuum Yang-Mills mass gap.

Regression: research/scripts/validate_switched_off_gap_perturbation.py.
