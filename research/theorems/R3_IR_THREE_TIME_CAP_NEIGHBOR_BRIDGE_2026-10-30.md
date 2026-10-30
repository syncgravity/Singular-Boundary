# Exact three-time cap–neighbor Wilson bridge and integrated second-moment bound

2026-10-30 | R3-IR-409 | **PROVED** for the true finite-volume SU(2) Wilson vacuum when the selected last-neighbor coupling is ZERO. Neither a full-coupling cap comparison nor a continuum mass gap is proved.

## Model

Let f be the magnetically deleted target face and g the neighboring face whose magnetic coupling is zero. Their shared original link x appears in no retained magnetic potential. All other plaquettes may have full physical Wilson couplings. The unrestricted positive normalized ground state factorizes as Omega_0(x,y)=omega(y) and is Gauss invariant. Its stationary ground-state process is independent Haar-stationary SU(2) Brownian motion x_u, with generator a_e Delta_x, and an interacting stationary environment y_u.

Choose face words W_f(0)=x_0 L_0 and W_g(u)=x_u^{-1}M_u, consistent with the shared-link orientation. Let p(A)=Tr(A)/2, O=k(W_f(0)) with k nonnegative central, a0=int k>0, a1=int k chi_1, chi_1(A)=4p(A)^2-1.

## Theorem (TT-1): the exact three-time covariance

For 0<=s<=t, let A_s=M_s L_0 and A_t=M_t L_0. Then

Cov_0(O,p_g(s)p_g(t))
= (a1/12) exp[-2a_e s-(3a_e/4)(t-s)]
  E_y[4p(A_s)p(A_t)-p(A_s^{-1}A_t)]. (TT-1)

For arbitrary s,t>=0, replace s with min(s,t) and t-s with |t-s|, with A_s and A_t at their respective times.

**Proof.** Condition on the complete environment path. The fundamental matrix coefficient p(x^{-1}M) has heat eigenvalue -3/4, so Markov conditioning from t to s gives
E_x[p_g(s)p_g(t)|x_s,y(.)]
=exp[-3a_e(t-s)/4]p(x_s^{-1}M_s)p(x_s^{-1}M_t).
For fixed M_s,M_t, the product of two fundamental coefficients in x decomposes into the SU(2) left-spin 0 and 1 sectors; the Haar spin-zero projection is (1/4)p(M_s^{-1}M_t). Its orthogonal spin-one part propagates from s to zero with factor exp(-2a_e s). At x_0, integrate against the central cap k(x_0L_0). Polarization of the exact one-time Schur identity in R3-IR-407 gives
int k(xL_0)p(x^{-1}M_s)p(x^{-1}M_t)dx
= (a0/4)p(M_s^{-1}M_t)
 +(a1/12)[4p(M_sL_0)p(M_tL_0)-p(M_s^{-1}M_t)].
The bracket reduces to chi_1(M_sL_0) for s=t, confirming the earlier equal-time identity. The uncapped covariance vanishes on the spin-zero part because E_x O=a0. Integrate the interacting y path with omega² to obtain TT-1. QED.

Here the expression in square brackets is an environmental mixed-time bilinear and is not individually an ordinary single-time gauge-invariant loop. Its averaged product is part of a gauge-invariant physical vacuum correlator.

## Corollary (TT-2): gap-free integrated-source bound

Let X_beta=b_g int_0^beta p_g(u)du, b_g>=0. Integrating TT-1 over the two source times, and using |p|<=1 so |4p(A_s)p(A_t)-p(A_s^{-1}A_t)|<=5, gives

| E_0^O[X_beta²]-E_0[X_beta²] |
<= (5 |a1| b_g²/(12a0))
   int_0^beta int_0^beta exp[-2a_e min(s,t)-(3a_e/4)|t-s|] ds dt
<= 5 |a1| b_g² / (9 a0 a_e²). (TT-2)

Indeed the full quadrant integral is 2 * (1/(2a_e)) * (4/(3a_e)) = 4/(3a_e²). This estimate is independent of beta and of the interacting environmental physical gap. It is an **actual three-time cap-biased second-moment estimate** for the zero-neighbor-coupling vacuum reference, not the earlier squared-plaquette two-time surrogate.

For an identity-centered small cap, a1/a0 approaches 3, so the RHS is O((b_g/a_e)²). At physical refinement b_g~h^-2 this bound diverges strongly and cannot establish positive even-moment ordering or the cosh comparison. It bounds a signed difference in absolute value, not its favorable sign.

## Important physical thermal caveat

TT-1 and TT-2 are formulated in the **stationary ground-state** process for H_0. They do NOT claim that the Gauss-projected finite-beta reference measure coincides with this process. A vacuum-source limit of the finite-beta cosh ratio involves a globally tilted bridge and cannot be controlled simply by inserting TT-2. All higher moments and the full t_g=1 response remain open.

No Penrose-uniform cap survival, infrared spectral estimate, or continuum Yang-Mills mass gap is inferred.
