# Exact even-coupling curvature transport for the Wilson cap source

**Date:** 2026-10-30. **Claim R3-IR-398.** Exact finite-volume SU(2) Wilson finite-temperature and zero-temperature response identities. No favorable variance ordering or Penrose-uniform cap bound is proved.

## Context and symmetry

Fix one neighbor g of the magnetic-deleted target f. Other couplings are held fixed. Write H(t)=H_0+t b(1-p_g), where H_0 is the true original-link Wilson Hamiltonian with target and neighbor magnetic terms omitted, and O=k_a(W_f) is the positive target cap observable. Assume the independently acting center-flux involution S_g of archived FN-2: S_g H_0 S_g^{-1}=H_0, S_g O S_g^{-1}=O, S_g p_g S_g^{-1}=-p_g. Consequently H(t) is unitarily equivalent to H(-t)+2tb, so normalized thermal and ground-state cap expectations are even functions of t.

For physical finite-temperature traces define
F_beta(t)=Tr_phys(O exp(-beta H(t)))/Tr_phys(exp(-beta H(t)))>0.
The corresponding positive Gauss-projected Feynman-Kac loop ensemble has integrated source X=b integral_0^beta p_g(U_s) ds. Let E_t be ordinary normalized Euclidean expectation and E_t^O[Y]=E_t[O(U_0)Y]/E_t[O(U_0)] the positive cap-biased expectation.

## Theorem (EV-1): exact signed variance-difference curvature

At every finite beta and real t,
d/dt log F_beta(t)=E_t^O X-E_t X,
and
\[
\boxed{\quad
\frac{d^2}{dt^2}\log F_\beta(t)
=\operatorname{Var}_t^O(X)-\operatorname{Var}_t(X).
\quad}\tag{EV-1}
\]
Both variances are for the *same integrated Wilson source*, but in two different positive Euclidean measures. They are nonnegative separately, while their difference has no automatic sign. This follows directly by differentiating twice the logarithms of the cap-inserted and ordinary partition functions under exponential tilting; the scalar tb in the magnetic energy cancels.

Evenness gives (log F_beta)'(0)=0. Therefore
\[
\boxed{\quad
\log\frac{F_\beta(t)}{F_\beta(0)}
=\int_0^t(t-s)
[\operatorname{Var}_s^O(X)-\operatorname{Var}_s(X)]\,ds.
\quad}\tag{EV-2}
\]
For t>=0 this identity is nonperturbative: no Taylor truncation, finite-gap denominator, or unproved spectral clustering appears.

## Vacuum limit and cap survival condition

At fixed finite original-link lattice, the positive physical ground state is simple and separated by a strictly positive finite-volume physical excitation gap at each real t. By local analytic perturbation of the rank-one projector (not any uniform h-gap), fixed-order derivatives of log F_beta converge as beta tends to infinity to those of log F(t)=log <Omega_t,O Omega_t>. Hence
\[
\boxed{\quad
\log\frac{F(1)}{F(0)}
=\lim_{\beta\to\infty}\int_0^1(1-s)
[\operatorname{Var}_s^O(X)-\operatorname{Var}_s(X)]ds.
\quad}\tag{EV-3}
\]
The limit is of the signed difference and weighted integral; neither variance alone has a finite zero-temperature limit in general. At t=0 the private-link Haar identity gives F(0)=alpha_a^2.

Thus the exact half-Haar criterion is that the RHS of EV-3 is at least -log(2). A stronger but unproved sufficient condition is nonnegative curvature difference for all s; this would imply F(1)>=F(0). A weaker condition only needs the *integrated* negative curvature to be controlled.

## Why parity is not enough

Invariance under S_g establishes evenness of F(t) but cannot establish convexity of log F(t): the difference of two convex logarithmic partition functions need not be convex. The two-state reversible countermodel from R3-IR-393 explains why general positivity is inadequate; here the missing estimate concerns a specifically Wilson-coupled variance difference. The full four-neighbor case can be handled by switching couplings sequentially, applying EV-2 to each coupling with the other three held fixed, whenever its independent FN-2 center-flux involution exists.

**Open:** show a uniform lower bound on the *signed variance-difference integral* with genuine original-link Wilson interactions at physical coupling b~h^-2. No such bound, completed-cage cap survival, uniform signed current, physical spectral mass gap or continuum reconstruction is proved.

Dependencies: R3_IR_CENTER_FLUX_ALL_TIME_BRIDGE_VANISHING_2026-10-30.md, R3_IR_CAP_BIASED_EUCLIDEAN_LOG_TRANSPORT_2026-10-30.md, and archived FN-2.
