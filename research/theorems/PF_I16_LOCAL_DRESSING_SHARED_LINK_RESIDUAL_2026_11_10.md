# PF-I16 — Exact single-face dressing and shared-link residual reduction

**Date:** 2026-11-10  
**Status:** exact finite-graph operator identity. Uniform residual norm and derivative bounds require the stated isolated-face estimates; all-orders summability and an interacting gap remain open.

## 1. Setup

On the authentic accepted-rhombus complex let \(E\) be original links and \(F\) accepted faces. Consider the auxiliary Hamiltonian
\[
H=K-\sum_{f\in F}b_fp_f,\qquad K=\sum_{e\in E}a_eC_e,
\]
where \(p_f=\tfrac12\operatorname{Tr}U_f\), \(a_e>0\), and \(d_e=\#\{f:e\in\partial f\}\). Allocate
\[
\alpha_{fe}=a_e/d_e,\quad
K_f=\sum_{e\in\partial f}\alpha_{fe}C_e,\quad
A_f=\sum_{e\in\partial f}a_e/d_e.
\]
Then \(K=\sum_fK_f+K_0\) exactly, where \(K_0\) contains uncovered links. Restricted to functions of the face holonomy, \(K_f=A_f(-\Delta_{SU(2)})\).

Let \(\psi_f(U_f)>0\) be the isolated-face ground state of \(K_f-b_fp_f\), with energy \(E_f\), and set \(s_f=\log\psi_f\), \(\Phi=\sum_fs_f\). The one-face ground-state equation is
\[
K_fs_f-\Gamma_{K_f}(s_f,s_f)-b_fp_f=E_f.
\]

## 2. Exact residual identity

With \(\Gamma_K(g,h)=\sum_ea_e\nabla_eg\cdot\nabla_eh\), define
\[
v_{fe}=\nabla_es_f,\qquad
R_e=a_e\left|\sum_{f:e\in\partial f}v_{fe}\right|^2
-\frac{a_e}{d_e}\sum_{f:e\in\partial f}|v_{fe}|^2,
\]
and \(R_e=0\) for \(d_e=0\). Summing the isolated-face equations gives
\[
K\Phi-\Gamma_K(\Phi,\Phi)-\sum_fb_fp_f
=\sum_fE_f-\sum_eR_e.
\]
Consequently the exact ground-state conjugation identity is
\[
\boxed{e^{-\Phi}He^{\Phi}=L_\Phi+\sum_fE_f-\sum_eR_e,\qquad
L_\Phi=K-2\Gamma_K(\Phi,\cdot).}
\]
The conjugation is unitary from \(L^2(e^{2\Phi}d\mu)\) to \(L^2(d\mu)\); \(L_\Phi\) is nonnegative, symmetric in the dressed measure, and annihilates constants.

**Structural consequence:** if \(d_e=1\), then \(R_e=0\). Repeated insertions confined to one face are absorbed into its exact isolated-face dressing. The residual is supported only at shared links.

## 3. Uniform locality and conditional norm bound

The elementary five-direction inventory gives \(d_e\le8\). Thus \(R_e\) depends on at most \(1+3d_e\le25\) original links. If
\[
\ell_f:=\max_{e\in\partial f}\|\nabla_es_f\|_\infty
\le C_1b_f/A_f,
\]
then Cauchy–Schwarz and \(A_f\ge a_e/d_e\ge a_e/8\) imply the conservative estimate
\[
\boxed{\|R_e\|_\infty\le4160C_1^2b_0^2/a_0}
\]
under \(a_e\ge a_0>0\) and \(0\le b_f\le b_0\). The residual interaction-overlap degree is at most 800 by the crude support count \(25\cdot8\cdot4\).

For the eight recorded original source crops, the observed incidence is at most two, giving crop-specific support size at most seven and \(d_e^2+1\le5\). The universal proof continues to use eight.

A sharper rotor estimate developed in the current working derivation gives \(\|\nabla s_f\|_\infty\le\beta_f\), \(\beta_f=b_f/A_f\), and hence \(\|R_e\|_\infty\le1040b_0^2/a_0\) under \(a_e\ge a_0\), \(b_f\le b_0\), \(b_0/a_0\le1\). This sharper numerical constant is a derived analytic bound and should be treated as conditional on the stated rotor metric and derivative lemma until the standalone verifier is merged.

## 4. What this does not prove

The identity is exact at finite graph size. It does not by itself prove a volume-uniform Poincaré estimate for \(L_\Phi\), stability under the extensive sum \(\sum_eR_e\), a convergent all-orders cluster expansion, source-derived physical time, a continuum limit, or a mass gap. The remaining hard step is local space-time connected cancellation/stability, not a global Kato bound on the extensive residual.
