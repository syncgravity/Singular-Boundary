# The Singular Boundary — Double self-weighted SU(2) Wilson-cap response

**Date:** 2026-10-29. **Program:** R3 independent reconstruction. **Status:** new rigorous finite nonlinear physical-sector theorem, conditional Penrose refinement consequence; the low-energy adverse mixed response and physical mass gap remain OPEN.

## 1. Physical Hamiltonian, exact Haar bridge, and cap source

Let the spatial regulator be a finite simply connected edge-to-edge rhombus disk, with four edges per face, no more than two faces per edge, and all-vertex Gauss invariance. Take

\[
H=\sum_e a_e(-\Delta_e)+\sum_k b_k(1-p_k),\quad p_k=\tfrac12\operatorname{ReTr}W_k,
\quad 0<a_-\le a_e\le a_+,\quad b_k\asymp h^{-2}.
\]

Fix an interior target face \(f\), delete its magnetic term, and choose one edge-sharing neighbor \(g\). With \(W=b_gd_g\) and \(d_g=1-p_g\), define the exact interpolation

\[
H(u)=T+\sum_{k\notin\{f,g\}}b_kd_k+uW,\quad 0\le u\le1.
\]

At \(u=0\) the common edge belongs to no magnetic face. The unique positive physical ground state \(\Omega_0\) is independent of this edge; hence the deleted face holonomy is Haar. For all finite \(u\), the finite-volume positive physical ground state \(\Omega_u\) and energy \(E(u)\) are smooth in \(u\), and the reduced resolvent \(G_u=Q_u(H(u)-E(u))^{-1}Q_u\) exists. No uniform physical gap is presumed. Let \(A_f=\sum_{e\in\partial f}a_e\) and \(A_g=\sum_{e\in\partial g}a_e\).

Choose a nonnegative smooth central radial bump \(\zeta_a\), equal to one on the group geodesic ball \(B_{a/4}\), supported in \(B_{a/2}\), with \(|\nabla\zeta_a|\le C_\zeta/a\), for \(0<a<a_0<1\). Put \(\phi_a=\zeta_a^2\), \(k_a=\phi_a*\phi_a^\vee\), \(\alpha_a=\int\phi_a dU\), \(\nu_a=\int\phi_a^2dU\). Then \(\alpha_a,\nu_a\asymp a^3\), and

\[
0\le k_a\le\nu_a\mathbf1_{B_a},\quad \int k_a dU=\alpha_a^2,\quad
F_a(u):=\langle k_a(W_f)\rangle_{\Omega_u}>0,\quad F_a(0)=\alpha_a^2.
\]

## 2. Theorem DS-1: pointwise cap convolution square-root bound

For \(\phi_a=\zeta_a^2\), the extended quotient \(|\nabla\phi_a|^2/\phi_a\) is bounded by \(4C_\zeta^2/a^2\) on its support (and zero where \(\phi_a=0\)). In the Haar convolution \(k_a(U)=\int\phi_a(V)\phi_a(V^{-1}U)dV\), Cauchy–Schwarz weighted by \(\phi_a(V)\phi_a(V^{-1}U)\) yields

\[
\begin{aligned}
|\nabla k_a(U)|^2
&\le k_a(U) \int\phi_a(V)\frac{|\nabla\phi_a(V^{-1}U)|^2}{\phi_a(V^{-1}U)}dV\\
&\le\frac{4C_\zeta^2}{a^2}k_a(U)\int_{V^{-1}U\in B_{a/2}}\phi_a(V)dV\\
&\le\frac{4C_\zeta^2}{a^2}\,H_{SU(2)}(a/2)\,k_a(U)\le C_k a\,k_a(U).
\end{aligned}
\]

The constants depend only on the chosen bump and the fixed Haar metric. Link differentiation of \(k_a(W_f)\) pulls back the bi-invariant group gradient by an isometry, and each of the four incident electric coefficients enters exactly once. Therefore, for **the actual interacting vacuum**,

\[
\boxed{m_{1,u}(k_a(W_f))=\mathbb E_{\Omega_u^2}\Gamma(k_a(W_f))\le C_k A_f a\,F_a(u).}\tag{DS1}
\]

This source-weighted \(f\)-sum is substantially sharper near a depleted center cap than the earlier uniform estimate \(m_1(k_a)\le C A_f a^4\). It is an exact SU(2) inequality for every finite regulator.

## 3. Theorem DS-2: integrated neighboring-face \(f\)-sum

The SU(2) class-function gradient identity is

\[
\Gamma(d_g)=\frac{A_g}{4}(1-p_g^2)=\frac{A_g}{4}(2d_g-d_g^2)\le\frac{A_g}{2}d_g.
\]

Thus \(m_{1,u}(W)\le\frac12b_g^2A_g\langle d_g\rangle_u\). Hellmann–Feynman gives \(E'(u)=b_g\langle d_g\rangle_u\) and hence

\[
\int_0^1 m_{1,u}(W)du\le\frac12 b_g A_g\,[E(1)-E(0)].
\]

At \(u=0\), the edge shared by \(f,g\) is private to \(g\) because both face magnetic terms are absent. The previously proved exact gauge-invariant private-edge variational bound applies to restoring \(g\):

\[
E(1)-E(0)\le\frac{3}{2\sqrt2}\sqrt{A_gb_g}.
\]

Therefore

\[
\boxed{\int_0^1m_{1,u}(W)du\le\frac{3}{4\sqrt2}A_g^{3/2}b_g^{3/2}.}\tag{DS2}
\]

This integrated \(f\)-sum is independent of the total face count or the number of other cycles.

## 4. Theorem DS-3: nonlinear ultraviolet cap response with self-weighting

The exact finite physical ground-state derivative is

\[
F_a'(u)=-2\operatorname{Re}\langle Q_u k_a\Omega_u, G_uQ_uW\Omega_u\rangle.
\]

Let \(P_{u,\le\Lambda}\) and \(P_{u,>\Lambda}\) be the strictly positive excitation-energy spectral projections of \(K_u=H(u)-E(u)\). Define

\[
\begin{aligned}
\ell_{a,\Lambda}(u)&=2\operatorname{Re}\langle Q_uk_a\Omega_u,G_uP_{u,\le\Lambda}Q_uW\Omega_u\rangle,\\
v_{a,\Lambda}(u)&=2\operatorname{Re}\langle Q_uk_a\Omega_u,G_uP_{u,>\Lambda}Q_uW\Omega_u\rangle.
\end{aligned}
\]

For the high-energy term, spectral Cauchy–Schwarz and DS-1 imply

\[
|v_{a,\Lambda}(u)|\le\frac2{\Lambda^2}\sqrt{m_{1,u}(k_a)m_{1,u}(W)}
\le\frac{2\sqrt{C_k A_faF_a(u)m_{1,u}(W)}}{\Lambda^2}.
\]

As \(F_a(u)>0\), differentiate \(y_a(u)=\sqrt{F_a(u)}\), retaining the adverse part \([\ell]_+\):

\[
y_a'(u)\ge-\frac{[\ell_{a,\Lambda}(u)]_+}{2y_a(u)}
-\frac{\sqrt{C_k A_f a}}{\Lambda^2}\sqrt{m_{1,u}(W)}.
\]

Integrate from \(u=0\) to \(1\), apply Cauchy–Schwarz in the coupling parameter and DS-2. Define the **normalized adverse low-energy physical response**

\[
\boxed{\mathcal B_{a,\le\Lambda}=\int_0^1\frac{[\ell_{a,\Lambda}(u)]_+}{2\sqrt{F_a(u)}}du.}\tag{DS3a}
\]

Then, with \(C_*=\sqrt{\frac{3C_k}{4\sqrt2}}\),

\[
\boxed{\sqrt{F_a(1)}\ge\alpha_a-\mathcal B_{a,\le\Lambda}
-\frac{C_*A_f^{1/2}A_g^{3/4}\,a^{1/2}b_g^{3/4}}{\Lambda^2}.}\tag{DS3b}
\]

Since \(k_a\le\nu_a\mathbf1_{B_a}\), this yields the fully nonlinear finite-volume cap-probability inequality

\[
\boxed{\Pr_{\Omega_1}(W_f\in B_a)\ge
\frac{\bigl[\alpha_a-\mathcal B_{a,\le\Lambda}-C_*A_f^{1/2}A_g^{3/4}a^{1/2}b_g^{3/4}/\Lambda^2\bigr]_+^2}{\nu_a}.}\tag{DS3c}
\]

No positive physical gap, source covariance decay, or Gaussian approximation is assumed. The low-energy budget is generally nonnegative but **not yet controlled**.

## 5. DS-4: refined Penrose energy cutoff \(h^{-11/8}\)

Choose physical cap \(a_h=\arccos(1-h)\asymp\sqrt h\), and assume \(a_e\in[a_-,a_+]\), \(b_g\le\beta_+h^{-2}\). Then \(A_f,A_g\le4a_+\), \(\alpha_{a_h}\ge c_\phi a_h^3\asymp h^{3/2}\) and

\[
\frac{a_h^{1/2}b_g^{3/4}}{(Lh^{-11/8})^2}=O(L^{-2}h^{3/2})=O(L^{-2}\alpha_{a_h}).
\]

Choose a sufficiently large *fixed* \(L\) so that the last term in DS3b is at most \(\alpha_{a_h}/4\), uniformly in face count. We have the unconditional finite-regulator alternative

\[
\boxed{\begin{cases}
\mathcal B_{a_h,\le Lh^{-11/8}}\le\alpha_{a_h}/4 &\Rightarrow\ \Pr_{\Omega_f^-}(d_f\le h)\ge\alpha_{a_h}^2/(4\nu_{a_h})\ge c h^{3/2},\\
\mathcal B_{a_h,\le Lh^{-11/8}}>\alpha_{a_h}/4 &\Rightarrow\ \text{adverse normalized mixed physical response }\gtrsim h^{3/2}\text{ below }Lh^{-11/8}.
\end{cases}}\tag{DS4}
\]

This moves the necessary UV cutoff from the previous \(h^{-2}\) to **\(h^{-11/8}\)**. The proof uses **two distinct non-Gaussian self-weighted identities**: one for the positive cap source and one for the neighboring magnetic coupling integrated along its interpolation. Importantly, the new low-energy budget is *normalized by* \(\sqrt{F_a(u)}\); it is not the same quantity as the earlier unnormalized \(O(h^3)\) budget. Its quantitative meaning and the narrower spectral window are both recorded.

The first outcome would close the earlier polynomial deleted-vacuum flat-ball requirement and thus the fixed-support Wilson–angle comparison under the previously declared regional hypotheses. But the first outcome has **not** been proved for the cycle-rich nonlinear Penrose vacuum.

## 6. Independent deterministic verification

The included Python verifier computes the SU(2) central convolution by direct radial Haar integration and a sphere-angle integral (no Fourier truncation), verifies its support and \(k_a(I)=\nu_a\), checks exact SU(2) rotor first spectral moments against Hellmann–Feynman for \(b=4,25,100\), and checks the \(h^{-11/8}\) scaling at five refinements. The one-face rotor serves only as a finite non-Gaussian interacting test of the local identities, **not** as a Penrose-vacuum simulation. The theory itself is a fully nonlinear finite-volume SU(2) inequality.

## 7. Open obligations and audit notes

**PROVED:** DS-1, DS-2, DS-3, DS-4 at the stated scope. **OPEN:** independently control \(\mathcal B_{a_h,\le Lh^{-11/8}}\le\alpha_{a_h}/4\) or otherwise prove polynomial flat-ball mass for the *actual connected, cycle-rich magnetic-deleted Penrose vacuum*; full bulk face deletion; fixed-support centered Wilson-angle covariance; physical continuum mass gap; nonlinear quartic resolvent; continuum reconstruction. No Stage 26 archives or historical datasets were modified.