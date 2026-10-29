# R3-IR — SU(2) shared-link spin selection, cap survival and exact gap obstruction (2026-10-29)

**Status:** exact finite Gauss-invariant SU(2) Wilson theorems, with a gap-dependent small-coupling center-cap bound. **NOT proved:** the full-coupling \`t=1\` cap estimate, cycle-rich all-bulk deletion scaling, fixed-support covariance, physical mass gap, or continuum reconstruction. Complete independent proof and exact rational verifier are also packaged in \`singular_boundary_wilson_spin_selection_2026-10-29.zip\` (SHA256 \`496a72e19570e286e866a54bdf98df99139fe37ffefedcf497a1179477c20061\`).

## Physical model and double-deleted link

For edge-sharing faces \`f,g\` of a finite simply connected face-complete rhombus disk with at most two faces touching each edge, let
\[
H_0=T+\sum_{k\notin\{f,g\}} b_k(1-p_k),\quad
H(t)=H_0+t b_g(1-p_g),\quad p_k=\tfrac12\operatorname{ReTr}W_k.
\]
The shared link \`e\` appears in no \`H_0\` magnetic term. The unique positive physical \`H_0\` ground state \(\Omega_0\) is independent of \`U_e\`. Write \(\delta_0>0\) for its **finite-volume physical spectral gap**, \(B=b_gp_g\), \(\|B\|\le b_g\). Scalar \(tb_g\) does not affect the eigenprojector, so use \(H_0-tB\). All statements concern the full nonlinear SU(2) Wilson Hamiltonian with all other plaquettes retained.

## SS-1: all-order shared-edge spin-selection

Define \(c_j(t)=\langle\Omega_t,\chi_j(W_f)\Omega_t\rangle\) for spin \(j\in\frac12\mathbb N\). On the shared link, \(\chi_j(W_f)\) is a representation-\(j\) matrix coefficient. The private-edge ground state has link spin zero; the \`H_0\` reduced resolvent preserves link-spin sectors; each insertion of the neighbor multiplier \(p_g\) carries link spin \(\frac12\) and changes spin by at most \(\frac12\). In the locally analytic intermediate-normalized eigenvector \(\psi(t)=\sum_{n\ge0}t^n\psi_n\), the shared link spins of \(\psi_n\) are at most \(n/2\). Clebsch–Gordan orthogonality forces a matrix element of \(\chi_j(W_f)\) between orders \(n_1,n_2\) to vanish when \(j>(n_1+n_2)/2\). The normalized expectation therefore satisfies
\[
\boxed{\quad c_j^{(n)}(0)=0\quad\text{for every integer }n<2j.\quad}
\]
The independent target center-flux symmetry also makes half-odd-spin \(c_j(t)\) vanish at every real coupling; the first *possible* integer-spin responses occur at \(t^{2j}\): spin 1 at order 2, spin 2 at order 4, etc. This is an exact nonlinear *selection rule*, not an assertion that any coefficient has favorable sign.

## SS-2: explicit analytic coefficient bound using the finite gap

On the spectral contour \(|z-E_0|=\delta_0/2\), the resolvent of \(H_0\) has norm \(\le2/\delta_0\). For complex \(|t|\le r=\delta_0/(4b_g)\), the Neumann resolvent is bounded by \(4/\delta_0\). The isolated ground-state Riesz projector \(P(t)\) has rank one and trace norm \(\le2\). Thus the analytic \(c_j(t)=\operatorname{Tr}(\chi_j(W_f)P(t))\) has \(|c_j(t)|\le2(2j+1)\). Its Taylor coefficients below degree \(2j\) vanish by SS-1. Cauchy estimates give, when \(|t|\le r/2\),
\[
\boxed{|c_j(t)|\le4(2j+1)\left(4b_g|t|/\delta_0\right)^{2j}.}
\]

## SS-3: cap-radius-uniform Haar-order survival in the permitted window

Let \(\phi_a\ge0\) be a real central SU(2) bump supported in the half-angle ball \(B_{a/2}\); define \(\alpha_a=\int\phi_a\), \(\nu_a=\int\phi_a^2\), \(\beta_j=\int\phi_a\chi_j\) and \(k_a=\phi_a*\phi_a^\vee\). Then \(0\le k_a\le\nu_a1_{B_a}\), \(\int k_a=\alpha_a^2\), and the exact expansion is
\[
\langle k_a(W_f)\rangle_t=\alpha_a^2+\sum_{j>0}\frac{\beta_j^2}{2j+1}c_j(t).
\]
Target center symmetry removes half-odd spins; \(|\beta_j|\le(2j+1)\alpha_a\). Put \(\rho=4b_g|t|/\delta_0\), \(x=\rho^2\). The proven coefficient bounds imply
\[
\langle k_a(W_f)\rangle_t\ge\alpha_a^2\left[1-4\sum_{j=1}^\infty(2j+1)^2\rho^{2j}\right]
=\alpha_a^2\left[1-\frac{4x(9-2x+x^2)}{(1-x)^3}\right].
\]
For \(|t|\le\delta_0/(64b_g)\), \(\rho\le1/16\), the bracket is at least \(14224123/16581375=0.8578373627036359\). Consequently
\[
\boxed{\Pr_{\Omega_t}(W_f\in B_a)\ge
\frac{14224123}{16581375}\frac{\alpha_a^2}{\nu_a}.}
\]
For the fixed scaled bump \(\alpha_a,\nu_a\asymp a^3\), this is an **unconditional Haar-order \(ca^3\) cap bound for every cap radius**, but only within the stated finite-gap perturbative coupling window.

## SS-4: exact physical excitation upper-bounds the gap and blocks continuation to t=1

The same private edge makes \(W_f,W_g\) exactly Haar distributed in \(|\Omega_0|^2\). For each \(k=f,g\), the *physical* gauge-invariant trial state \(\Xi_k=\chi_{1/2}(W_k)\Omega_0=2p_k\Omega_0\) satisfies \(\langle\Omega_0,\Xi_k\rangle=0\) and \(\|\Xi_k\|^2=1\), by Haar character orthogonality. The exact positive-ground-state Dirichlet identity and SU(2) class gradient \(|\nabla_{e'}(2p_k)|^2=1-p_k^2\) give
\[
\langle\Xi_k,(H_0-E_0)\Xi_k\rangle
=A_k\langle1-p_k^2\rangle_{\Omega_0^2}
=\tfrac34 A_k,\qquad A_k=\sum_{e'\in\partial k}a_{e'}.
\]
By the physical min–max principle,
\[
\boxed{\delta_0\le\tfrac34\min(A_f,A_g).}
\]
If \(a_e\le a_+\) and \(b_g\ge\beta_-h^{-2}\), then
\[
\boxed{\frac{\delta_0(h)}{64b_g(h)}\le\frac{3a_+}{64\beta_-}h^2.}
\]
The SS-3 survival window is therefore **provably at most \(O(h^2)\)** and cannot reach \(t=1\) as \(h\to0\). This is a rigorous *negative conclusion* about gap-based analytic continuation, not just a missing estimate.

## Verification and remaining obligations

An exact rational SU(2) character-basis rotor test verifies the selection hierarchy \(t^{2j}\) at spins \(j=\frac12,1,\frac32,2,\frac52,3\), the exact 0.857837… convolution constant, and normalized fundamental Haar trial energy 3/4 per incident edge. The rotor verifies representation algebra and is **not** a simulation of a cycle-rich Penrose vacuum. A valid global proof must instead control the nonlinear, adverse low-energy mixed response throughout \(0\le t\le1\), or establish another gap-insensitive global inequality. The physical continuum mass gap and reconstruction remain open.
