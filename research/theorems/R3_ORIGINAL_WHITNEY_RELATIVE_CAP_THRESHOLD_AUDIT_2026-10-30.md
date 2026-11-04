# R3-IR-543 — Exact shrinking-center-cap threshold for the protected-link additive estimate

Date: 2026-10-30. Scope: the finite rooted-tree SU(2) Penrose Hamiltonian of R3-IR-528–529 with original SHA-256-verified Whitney matrix, not a 3+1D continuum Yang–Mills proof.

## Exact threshold and relative-cap criterion

R3-IR-529 states, conditionally on the finite-model protected-gap theorem, P_h(C_delta) >= [c_delta - rho_h/(1-rho_h)]_+, 0<=rho_h<1, with

rho_h = b_(10,h)/gamma_(13,h) = 8 b_(10,h) M_(13,13)(h)/(3 g2_squared(h)),

and c_delta=(2/pi){acos(1-delta)-(1-delta)sqrt(2delta-delta²)} for the two-center SU2 cap 0<delta<=1.

For any 0<=theta<1, the sufficient criterion to prove P_h(C_delta) >= theta c_delta using this additive estimate is EXACTLY

rho_h <= [(1-theta)c_delta]/[1+(1-theta)c_delta].

A strictly positive bound requires rho_h<c_delta/(1+c_delta). Because c_delta~(8 sqrt(2)/(3pi)) delta^(3/2), a fixed relative fraction theta>0 along delta_h->0 is certified if rho_h <= (1-theta+o(1)) c_(delta_h), while rho_h=o(delta_h^(3/2)) is sufficient for asymptotic Haar-relative lower coefficient 1. These conditions describe **sufficiency by this specific inequality** and are not necessary for the actual physical measure.

For fixed rho>0, the bound has a strictly positive lower value only when delta>delta_min(rho)=c_inverse[rho/(1-rho)], provided rho<1/2 (since c_1=1); for rho>=1/2 the bound cannot be positive for any delta<=1.

## Archived exact-matrix evaluation

Original Library file: /The Singular Boundary/Source/global_whitney_11face.npz, SHA-256 d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf. Edge13 diagonal .7778590280946629, gamma13=.4820924954982508 for g2_squared=1. With b10=3/32000, rho=.00019446475702366572, epsilon=rho/(1-rho)=.00019450258092080497. Critical cap width delta_min=.00297297 approximately. The exact Haar masses and corresponding upper bounds on rho are: delta=.1: c=.0373860734685, rho_crit=.0360387269741; delta=.01: c=.0011986195114, rho_crit=.0011971845427; delta=.001: c=.000037954974374, rho_crit=.000037953533848.

## Conditional refinement scaling and limitation

Only if physical couplings and local mass satisfy rho_h=rho_1 h^-2 (an illustrative assumption carried from R3-IR-531, NOT measured Penrose matrices) does rho diverge as h->0. In that scenario this additive proof cannot yield a positive fixed or shrinking cap bound at sufficiently fine spacing. Under any scaling delta_h=h^alpha, alpha>0, a sufficient relative cap criterion requires rho_h=O(h^(3alpha/2)), incompatible with the stated h^-2 scenario.

This does **not** disprove continuum cap probabilities or Yang–Mills gap. It proves an obstruction to a particular perturbative inequality. A useful next result must bound conditional marginal score, logarithmic density oscillation, or other regularity uniformly enough to get an actual multiplicative comparison. The earlier signed radial vacuum-current criterion R3-IR-289–292 is a separate candidate requiring independent interacting-vacuum estimates, not automatically implied by R3-IR-528.

## Reproducer and persistence

Exact original matrix hash, numerical threshold inversion, and refinement examples: research/scripts/audit_relative_cap_refinement.py. Executed locally with PASS. Binary datasets remain in ChatGPT Library; do not commit NPZ. Continuum mass gap remains OPEN.
