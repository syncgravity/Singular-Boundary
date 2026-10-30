# Euclidean connected-cumulant representation of the physical four-neighbor Wilson mixed response

**Date:** 2026-10-30. **Status:** exact finite-volume identity for the genuine Gauss-invariant SU(2) Wilson Hamiltonian, followed by an unproved sign/magnitude obligation. This is not a positivity theorem for the eighth mixed derivative, not the continuum mass gap, and not a reconstruction of the original Stage7/26 action.

## Finite-volume operator and heat-trace framework

Let \(H(t)=H_{\rm rest}+\sum_{i=1}^4t_i b_i(1-p_{g_i})\) on the physical Gauss-invariant Hilbert space of a finite SU(2) rhombus disk, with \(t\in[0,1]^4\), \(b_i\ge0\). The plaquette multipliers \(p_i=p_{g_i}\) are bounded real gauge invariant functions. Let \(O=k_a(W_f)\) be the nonnegative, bounded class convolution observable used in archived FN-4; \(0\le O\le\nu_a\). At each real \(t\), the Hamiltonian has a unique physical positive normalized ground state \(\Omega_t\), and \(F_a(t)=\langle\Omega_t,O\Omega_t\rangle\).

At inverse Euclidean-time circumference \(\beta>0\), define the *physical* thermal expectation
\[
F_{a,\beta}(t)=\frac{\operatorname{Tr}_{\rm phys}[O e^{-\beta H(t)}]}{\operatorname{Tr}_{\rm phys} e^{-\beta H(t)}}.
\]
The traces are finite for every \(\beta>0\). The physical heat kernel is a positive gauge-orbit projection of the original-link heat kernel; one may equivalently construct a positive loop/path-space measure using the original-link Feynman–Kac kernel and gauge averaging at the time seam. Do not replace a physical trace by an unrestricted trace unless gauge projection is included.

For a sample path on this positive finite-\(\beta\) measure, let \(P_i=\int_0^\beta p_i(U(\tau))\,d\tau\) and \(X_i=b_iP_i\). Insert \(O(U(0))\) at a distinguished Euclidean time. The centered-normalized expectation of a bounded path functional is denoted \(\mathbf E_{\beta,t}\).

## Theorem EC-1: exact mixed-response cumulant identity

For any nonnegative integers \(n_1,\ldots,n_4\) with \(n=\sum n_i\), and each finite \(\beta\),
\[
\boxed{\quad
\partial_{t_1}^{n_1}\cdots\partial_{t_4}^{n_4}F_{a,\beta}(t)
=\kappa_{\beta,t}\left(
O(U(0)),
\underbrace{X_1,\ldots,X_1}_{n_1},
\ldots,
\underbrace{X_4,\ldots,X_4}_{n_4}
\right).
\quad}\tag{EC-1}
\]
Here \(\kappa\) is the ordinary joint cumulant of \(n+1\) random variables with respect to the **positive physical Euclidean loop measure** at coupling \(t\). In particular,
\[
\boxed{\quad
\partial_1^2\partial_2^2\partial_3^2\partial_4^2F_{a,\beta}(t)
=\kappa_{\beta,t}(O,X_1,X_1,X_2,X_2,X_3,X_3,X_4,X_4).
\quad}\tag{EC-2}
\]
This is a *connected nine-variable Euclidean path cumulant*, not a product of eight ordinary covariances. Every \(X_i\) is an **integrated physical plaquette**, retaining all time orderings and the nonlinear Wilson environment.

**Proof.** The path-space density relative to the reference kinetic bridge is proportional to
\[
\exp\left[-\int_0^\beta V_{\rm rest}(U(\tau))d\tau
-\sum_i t_ib_i\beta+\sum_i t_i X_i\right].
\]
The scalar factors \(\exp(-\beta\sum t_ib_i)\) cancel in normalized expectations. For fixed \(\beta\), all the plaquette integrals are bounded by \(\beta\), and \(O\) is bounded, so repeated differentiation under the path integral is justified. Introduce the moment generating function
\[
K(s,z)=\log\mathbf E_{\beta,t}
\exp\left[sO+\sum_i z_iX_i\right].
\]
Since the derivative with respect to \(t_i\) acts as an exponential tilt by \(X_i\), the repeated mixed derivative of \(\mathbf E_{\beta,t}O\) equals
\(\partial_s\prod_i\partial_{z_i}^{n_i}K(0,0)\), which is exactly the joint cumulant on the right. QED.

## EC-2: physical vacuum limit at each fixed finite lattice

For every fixed real \(t\) on the coupling cube, positivity improving and the finite-volume gap imply
\[
F_a(t)=\lim_{\beta\to\infty}F_{a,\beta}(t).
\]
Furthermore, all fixed finite mixed derivatives converge to those of \(F_a\) for each fixed lattice and \(t\):
\[
\boxed{\quad
\partial_1^2\cdots\partial_4^2 F_a(t)
=\lim_{\beta\to\infty}
\kappa_{\beta,t}(O,X_1,X_1,X_2,X_2,X_3,X_3,X_4,X_4).
\quad}\tag{EC-3}
\]
To justify derivative convergence, for each fixed \(t\) use the isolated simple physical ground eigenvalue and the local complex coupling polydisk obtained by the Riesz-resolvent argument of the October 30 physical response bound. The normalized heat-trace ratio converges there to the analytic rank-one ground-state expectation, uniformly on a sufficiently small compact complex polydisk, by the discrete spectrum, positive finite real gap, and trace-class heat kernel. Cauchy estimates then give convergence of each fixed mixed derivative. This assertion is **not uniform in refinement h** and does not assume or prove a uniform physical gap.

## What this identifies, and what is not proved

Combining EC-3 with archived FN-4 shows that the exact full-coupling cap correction is an integral over the coupling cube of a **connected nine-point Wilson Euclidean time cumulant**, in the zero-temperature limit. Its *negative* part is precisely what the FN-5 center-cap survival theorem requires controlling.

The signed cumulant is not nonnegative merely because the Euclidean path measure is positive: joint cumulants of order nine do not have a general sign under positivity alone. FN-1/FN-3 force cancellation on coordinate hyperplanes and vanishing Taylor orders, but do not establish the required full-coupling sign. The previous absolute Riesz bounds lose all cancellation and become ineffective at the physical coupling scale.

**Next mathematical gate:** prove an original-Wilson-specific inequality or summable connected-polymer/cluster bound for this exact nine-variable cumulant, uniformly over \(0\le t_i\le1\) and completed Penrose interiors, **without assuming the desired mass gap or an unproved uniform Euclidean mixing rate**. If such a condition cannot be established, a different mechanism must replace FN-5.

This is an identity-level advance and a non-circular diagnostic, **not** a successful proof of the remaining full-coupling estimate.
