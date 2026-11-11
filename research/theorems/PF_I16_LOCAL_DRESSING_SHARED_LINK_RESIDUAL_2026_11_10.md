# PF-I16 — Exact single-face dressing and shared-link residual reduction

**Date:** 2026-11-10  
**Status:** exact finite-graph operator identity; local residual support and norm reduction established conditionally on a one-face derivative bound. This is a new route toward, not a proof of, uniform connected-cycle summability or an interacting gap.

## 1. Setup and allocation of the electric operator

Consider the centered auxiliary Hamiltonian \(H=K-\sum_{f\in F}b_fp_f\), with \(K=\sum_{e\in E}a_eC_e\). For each link define its accepted-face incidence
\[
d_e=\#\{f\in F:e\in\partial f\}.
\]
For \(d_e>0\), allocate its electric coefficient equally among incident faces:
\[
\alpha_{fe}=a_e/d_e,\qquad
K_f=\sum_{e\in\partial f}\alpha_{fe}C_e,\qquad K=\sum_{f\in F}K_f+K_0,
\]
where \(K_0\) is the sum over links with \(d_e=0\). The equality is exact because each covered link receives total coefficient \(a_e\).

For a face define
\[
A_f=\sum_{e\in\partial f}a_e/d_e.
\]
Since every link derivative acting on a function of the face holonomy gives the same SU(2) group Laplacian, \(K_f\) restricted to functions of \(U_f\) is \(A_f(-\Delta_{SU(2)})\).

Let \(p_f=(1/2)\operatorname{Tr}(U_f)\), and let \(\psi_f(U_f)>0\) be the normalized isolated-face ground state of \(K_f-b_fp_f\), with energy \(E_f\). Put \(s_f=\log\psi_f\) and
\[
\Phi=\sum_{f\in F}s_f(p_f).
\]
The one-face ground-state equation, divided by \(\psi_f\), is the exact identity
\[
K_fs_f-\Gamma_{K_f}(s_f,s_f)-b_fp_f=E_f.
\]

## 2. Exact shared-link residual identity

Use the carré du champ convention
\[
\Gamma_K(g,h)=\sum_e a_e\nabla_eg\cdot\nabla_eh.
\]
For each covered link let
\[
v_{fe}=\nabla_es_f,\qquad
R_e=a_e\left|\sum_{f:e\in\partial f}v_{fe}\right|^2
-\frac{a_e}{d_e}\sum_{f:e\in\partial f}|v_{fe}|^2.
\]
Set \(R_e=0\) when \(d_e=0\). Since \(K\Phi=\sum_f K_fs_f\), summing the isolated-face equations gives
\[
K\Phi-\Gamma_K(\Phi,\Phi)-\sum_fb_fp_f
=\sum_fE_f-\sum_eR_e.
\]
The ground-state conjugation formula therefore yields
\[
\boxed{
e^{-\Phi}He^{\Phi}=L_\Phi+\sum_fE_f-\sum_eR_e,
\qquad L_\Phi=K-2\Gamma_K(\Phi,\cdot).
}
\]
Multiplication by \(e^\Phi\) is a unitary map from \(L^2(e^{2\Phi}d\mu)\) to \(L^2(d\mu)\). Thus this is an exact unitary equivalence between the original Hamiltonian and the dressed diffusion plus the shared-link residual potential. \(L_\Phi\) is nonnegative, symmetric in \(e^{2\Phi}d\mu\), and annihilates constants.

**Key structural point:** if \(d_e=1\), then \(R_e=0\) exactly. Every residual term is attached to a link shared by at least two accepted faces. Repeated insertions confined to one face have been absorbed into the exact isolated-face dressing rather than expanded perturbatively.

## 3. Uniform locality and conditional residual norm

The elementary five-direction inventory gives \(d_e\le8\). Hence \(R_e\) depends only on the union of faces incident to \(e\), containing at most
\[
1+3d_e\le25
\]
original links.

Let
\[
\ell_f=\max_{e\in\partial f}\|\nabla_es_f\|_\infty.
\]
For \(d=d_e\), Cauchy–Schwarz gives
\[
|R_e|\le a_e(d+1/d)\sum_{f:e\in\partial f}|v_{fe}|^2
\le a_e(d^2+1)\max_{f:e\in\partial f}\ell_f^2.
\]
If a separate isolated-face estimate proves
\[
\ell_f\le C_1 b_f/A_f,
\]
then \(A_f\ge a_e/d_e\ge a_e/8\) for every \(f\) incident to \(e\), so
\[
\boxed{\|R_e\|_\infty\le4160 C_1^2\,b_0^2/a_0}
\]
under \(a_e\ge a_0>0\), \(0\le b_f\le b_0\). The constant 4160 is deliberately conservative: it uses \(d_e\le8\) and \(d_e^2+1\le65\).

The residual interaction-overlap graph also has a crude uniform degree bound. \(\operatorname{supp}(R_e)\) contains at most 25 links. Each such link lies in at most 8 faces, each with 4 links, so at most \(25\cdot8\cdot4=800\) link-indexed residual terms can have support intersecting \(\operatorname{supp}(R_e)\). Thus the residual potential is a bounded-range interaction family with uniformly bounded overlap degree, provided the one-face derivative estimate holds.

On the eight recorded original source crops, the PF-I11 incidence evidence reports no link with more than two accepted-face incidences. On those finite crops the corresponding residual support bound improves to 7 links and the local norm factor to \(d_e^2+1\le5\). The universal proof continues to use 8 until the stronger incidence statement is proved for all source regions.

## 4. What this reduction does and does not solve

The identity isolates the analytic bottleneck in a cleaner form:

1. Prove a uniform isolated-face derivative/Hessian estimate for \(s_f\) in the intrinsic SU(2) rotor, with constants controlled by \(A_f\).
2. Use bounded face incidence to prove a volume-independent Bakry–Émery curvature/Poincaré estimate for the dressed diffusion \(L_\Phi\).
3. Prove a local-potential stability or time-space connected-cumulant theorem for \(L_\Phi-\sum_eR_e\), using support size at most 25 and residual overlap degree at most 800 (or sharper source-proved constants).

Step 2 alone is not enough: an extensive sum of small bounded potentials is not a small operator in global norm. Step 3 must use locality and connected cancellations, not a global Kato norm estimate. The residual's quadratic order in \(b_0\) is the useful improvement over the original face interaction.

No all-orders cluster expansion, physical-coupling gap, source-derived time, continuum construction, or Yang–Mills mass gap is claimed.
