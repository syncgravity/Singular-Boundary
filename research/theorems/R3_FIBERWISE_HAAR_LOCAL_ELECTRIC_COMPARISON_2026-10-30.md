# R3-IR-515 — Fiberwise Haar comparison using one-link electric energy

Date 2026-10-30. This is a finite-regulator local comparison criterion, **not** a uniform estimate on the actual interacting ground-state link energy.

Let e be a free boundary edge occurring once in selected plaquette f. Product Haar on SU(2)^E disintegrates as du dY. For fixed Y, the plaquette U_f is obtained from U_e by fixed left/right group translations and possibly inversion. Hence Haar(C_delta) = c_delta is the fiber Haar probability of the double center cap, independent of Y.

For any normalized nonnegative psi in H1(SU2^E), define h(Y)=int_SU2 psi(u,Y)^2 du. When h>0, let phi_Y(u)=psi(u,Y)/sqrt(h(Y)), normalized in L2(du). Poincare on SU2 gives

1-|<1,phi_Y>|² = ||phi_Y-<1,phi_Y>||² <= (4/3) sum_a ||X_e^a phi_Y||²,

using fundamental Casimir 3/4. For any measurable cap event A_Y of fixed Haar mass c_delta, pure-state trace-distance contraction under the measurement {A_Y,A_Y^c} implies

|int_A_Y phi_Y² du-c_delta| <= sqrt(1-|<1,phi_Y>|²) <= sqrt((4/3) sum_a ||X_e^a phi_Y||²).

Multiply by h(Y), integrate Y and use Cauchy-Schwarz and int h=1 to obtain

Pr_psi(C_delta) >= [c_delta - sqrt((4/3) E_e(psi))]_+,
E_e(psi)=sum_a||X_e^a psi||².

This proof is **fiberwise**, works with arbitrary correlations with the background, and needs no assumption that the free-link Haar projector commutes with H. Nonnegative psi is the positive elliptic ground state.

For K=M^-1 and transported link derivatives D_j, minimize the positive quadratic expression over all j !=e. The effective one-edge coefficient is

K_ee - K_eB K_BB^-1 K_Be = 1/M_ee.

Thus for the finite inverse-Whitney electric kinetic form,

H_E[psi] >= (g2_squared/(2 M_ee)) E_e(psi).

The actual ground state of the switched-off Hamiltonian satisfies H_E[Omega0]<=B0=sum_(j !=f)b_j, leading only to E_e(Omega0)<=2M_ee B0/g2_squared and an *additional* bound

Pr_Omega0(C_delta) >= [c_delta - sqrt(8 M_ee B0/(3 g2_squared))]_+.

This bound remains total-coupling-dependent, but can be numerically better than the prior global-vacuum estimate for some edges. It does not remove the local-energy obstruction. The strict local comparison itself is independent of total magnetic strength and may become valuable if E_e can be bounded by a localized conditional-energy method.

A further structural caveat: c_delta itself is of order delta^(3/2) as delta goes to 0. A fixed nonzero E_e leaves this additive estimate vacuous for sufficiently small delta; it does not yield a uniform lower coefficient times delta^(3/2) without a stronger density or relative comparison. No refinement-uniform cap probability or continuum mass gap is proved.

Reproducible numeric checks: research/scripts/validate_fiberwise_haar_energy.py.
