# R3-IR-435 — Uniform-in-environment conditional SU(2) Poincare coercivity

2026-10-30. Finite-volume full-coupling Wilson theorem; its constant depends on magnetic/electric ratio and is not uniform under strong-coupling refinement.

Assume exactly the original-link private-edge geometry and normalization of R3-IR-427. Write the genuine physical vacuum probability as mu(dx,dy)=rho_y(x)dx nu(dy), with Haar-normalized dx. For any s>0, HK-1 states Omega(x,y)>=r_s Omega(x',y) where r_s=e^(-2b_g s)m(a_x s), 0<r_s<=1. Thus for every fixed y,

max_x rho_y(x)/min_x rho_y(x) <= r_s^(-2). (PC-1)

The Haar SU(2) Poincare inequality for the Laplacian convention -Delta chi_j=j(j+1)chi_j has sharp first nonzero eigenvalue lambda_H=3/4 (spin 1/2):
Var_Haar(phi) <= (4/3) int |grad_x phi|² dx.

For any density rho with 0<rho_min<=rho<=rho_max, take the Haar-mean c_H of phi and use variational definition of variance:
Var_rho(phi) <= int (phi-c_H)²rho dx <= rho_max Var_Haar(phi)
<= (4/3)rho_max int |grad phi|²dx
<= (4/3)(rho_max/rho_min) int |grad phi|²rho dx.
Consequently the conditional Poincare constant satisfies

boxed: lambda_x(y) >= (3/4) r_s² = (3/4)e^(-4b_gs)m(a_x s)², for ALL y. (PC-2)

This is uniform over all environmental link configurations y, all environmental couplings and finite volume, but is NOT uniform in b_g/a_x.

Combining with R3-IR-434, if v(y) is an admissible marginal environmental flux, the full cap susceptibility obeys

A <= [8/(3 a_x r_s²)] int [Var_rho_y(O)+Var_rho_y(v dot grad_y log rho_y)] dnu
  + sum_(e in environment) a_e^(-1) int |v_e(y)|²dnu. (PC-3)

The optimized heat-kernel bound of R3-IR-428 implies the existence of universal positive c,C such that
lambda_x(y)>=c exp[-C sqrt(1+b_g/a_x)]
with constants revised from the square of the heat-kernel ratio. This gives a completely explicit finite-volume local coercivity scale without assuming an interacting physical spectral gap.

Caution: the conditional-score variance and the marginal environmental flux cost remain uncontrolled under physical Penrose refinement. Even the conditional Poincare coefficient can decay as b_g/a_x grows. Neither (PC-2) nor (PC-3) proves the half-Haar completed-cage cap bound, an infrared spectral gate, or a continuum Yang-Mills mass gap.
