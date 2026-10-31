# R3-IR — Exact angular transport derivative of the nonlinear Wilson fiber energy

**2026-10-31. Finite-volume exact identity, not a uniform signed-current bound.**

Let \(p=p_f=\cos u\) on a simple SU(2) Wilson face, \(A_f=\sum_{e\in\partial f}a_e\), \(G=\sum_e a_e\nabla_e p\cdot\nabla_e\), and \(g=G p=A_f(1-p^2)/4\). The Haar generator gives \(\mathrm{div}_\mu G=-3A_fp/4\). Define the angular face-gradient lift
\[
Y=-\frac{\sin u}{g}G=-\frac4{A_f\sin u}\sum_{e\in\partial f}a_e\nabla_ep\cdot\nabla_e,\qquad Yu=1.
\]
For \(0<u<\pi\), the exact Haar divergence is \(\mathrm{div}_\mu Y=2\cot u=\partial_u\log\omega_0(u)\) where \(\omega_0=2\sin^2u/\pi\). Therefore, for any smooth scalar \(J\), its Haar conditional expectation obeys
\[
\frac{d}{du}\mathbb E_\mu[J\mid u]=\mathbb E_\mu[YJ\mid u].\tag{AT-1}
\]
This is an exact conditional differentiation identity with cancellation of the Haar Jacobian. It can equivalently be proved by integrating \(\mathrm{div}_\mu(q(u)JY)\) and comparing coefficients.

Factor the positive true deleted-face ground state as \(\Omega=\Psi(u)\Phi\), with \(\mathbb E_\mu[\Phi^2\mid u]=1\). The complete conditional fiber energy is
\[
U(u)=\mathbb E_\mu[\sum_{k,a}a_k(X_{k,a}\Phi)^2+V_-\Phi^2\mid u].
\]
Write \(J\) for the integrand. Applying (AT-1) gives the exact derivative
\[
\boxed{U'(u)=\mathbb E_\mu[YJ\mid u].}\tag{AT-2}
\]
Expanding with \([X,Y]=XY-YX\) yields
\[
\begin{split}
U'(u)=\mathbb E_\mu\big[&2\sum_{k,a}a_k(X_{k,a}\Phi)X_{k,a}(Y\Phi)
-2\sum_{k,a}a_k(X_{k,a}\Phi)([X_{k,a},Y]\Phi)\\
& +(YV_-)\Phi^2+2V_-\Phi(Y\Phi)\mid u\big].
\end{split}\tag{AT-3}
\]
Differentiating normalization also proves \(\mathbb E_\mu[\Phi Y\Phi\mid u]=0\). Hence the final potential term can be written as a conditional covariance with \(V_-\), but cannot be dropped. The first two terms are the material derivative and nonadiabatic commutator contribution. In particular, **differentiating the retained potential alone is incorrect**.

For a Wilson plaquette \(g\ne f\) sharing \(e\in\partial f\), the original-link Fierz inequality gives \(|\nabla_ep\cdot\nabla_ep_g|\le\sin u/4\). Thus
\[
\boxed{|YV_-|\le B_f^{\rm inc}:=\frac1{A_f}\sum_{e\in\partial f}a_e\sum_{g\ne f:e\in\partial g} b_g.}\tag{AT-4}
\]
This is a **pointwise, nonsingular, cage-local angular force bound**, including at the centers by continuous extension of the bound. If the rhombus complex is face-complete and edge-to-edge, each interior target boundary edge has at most one retained neighbor. Its physical coupling scale can still be \(O(h^{-2})\).

Define the remainder \(R_f(u)=U'(u)-\mathbb E_{\nu}[YV_-\mid u]\), exactly the other three terms in (AT-3). Combining (AT-4) with the archived fiber-slope maximum principle yields the rigorously **conditional** sufficient inequality
\[
\boxed{\mathfrak T_f\le\frac{\pi}{A_f}\big(B_f^{\rm inc}+\sup_{0<u<\pi/2}[-R_f(u)]_+\big).}\tag{AT-5}
\]
This provides a clean new Wilson-specific separation into a locally bounded direct magnetic force and an uncontrolled nonadiabatic response. There is **no proved favorable sign or refinement-uniform upper bound on \([-R_f]_+\)**. Even the bare magnetic bound is too large at usual \(b\sim h^{-2}\) scaling. Hence (AT-5) does **not** prove \(\sup_f\mathfrak T_{f,h}=o(h^{-1/4})\), connected covariance, or a continuum Yang–Mills mass gap.

**Verification.** `verify.py` uses a nontrivial, conditionally normalized two-SU(2)-rotor class-state \(\Phi(p,q)=(1+\kappa pq)/\sqrt{1+\kappa^2p^2\mathbb E q^2}\) and a coupled scalar potential to check conditional normalization and angular material differentiation at 111 points. This tests the chain rule and normalization algebra, not a Penrose Wilson ground state. The proof of (AT-1)—(AT-5) is analytic.