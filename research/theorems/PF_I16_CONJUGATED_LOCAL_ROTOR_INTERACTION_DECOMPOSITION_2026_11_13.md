# PF-I16 — Conjugated local-rotor interaction decomposition and candidate cluster margin

**Date:** 2026-11-13  
**Status:** exact operator decomposition and conditional local norm bounds. A quantum linked-cluster/Kotecký–Preiss theorem for the resulting product-rotor Hamiltonian has not yet been proved or applied. The numerical margin below is a candidate activity estimate, not a convergence theorem.

## 1. Exact conjugation and face/pair decomposition

Let
\[
L_\Phi=K-2\Gamma(\Phi,\cdot),\qquad
K=\sum_e a_e(-\Delta_e),\qquad
\Phi=\sum_f s_f(H_f).
\]
Multiplication by \(e^\Phi\) is unitary from \(L^2(e^{2\Phi}dU)\) to product Haar space. Direct differentiation gives
\[
e^\Phi L_\Phi e^{-\Phi}
=K+\mathcal U_\Phi,\qquad
\mathcal U_\Phi=\sum_e a_e\left[\Delta_e\Phi+|\nabla_e\Phi|^2\right].
\tag{1.1}
\]
For a fixed face \(f\), varying any one of its links is an isometry of the radius-two SU(2) group. Thus
\[
\Delta_e(s_f\circ H_f)=(\Delta s_f)(H_f),\qquad
|\nabla_e(s_f\circ H_f)|=|\nabla s_f|(H_f).
\]
Expanding the square in (1.1) and grouping the diagonal face terms gives
\[
\boxed{
\mathcal U_\Phi
=\sum_f A_f\left[\Delta s_f+|\nabla s_f|^2\right]
+\sum_{f<g}V_{fg},
}
\tag{1.2}
\]
where
\[
V_{fg}
=2\sum_{e\in\partial f\cap\partial g}
a_e\langle\nabla_e s_f,\nabla_e s_g\rangle,
\qquad
A_f=\sum_{e\in\partial f}a_e.
\tag{1.3}
\]
The sum \(V_{fg}\) is zero unless the two accepted faces share an original link. Its support is contained in \(\partial f\cup\partial g\), of size at most eight links.

The isolated-face ground-state equation
\[
A_f(-\Delta)\psi_f-b_fp_f\psi_f=E_f\psi_f,\qquad
s_f=\log\psi_f,
\]
implies the exact identity
\[
A_f\left[\Delta s_f+|\nabla s_f|^2\right]
=-b_fp_f-E_f.
\tag{1.4}
\]
The variational bound \(|E_f|\le|b_f|\le b_0\) shows that, after dropping the irrelevant scalar \(-E_f\), the one-face interaction is exactly \(-b_fp_f\), with norm at most \(b_0\). Therefore, up to a scalar energy shift,
\[
\boxed{
e^\Phi L_\Phi e^{-\Phi}
=K-\sum_f b_fp_f+\sum_{f<g}V_{fg}.
}
\tag{1.5}
\]
This is a face-indexed one-body/two-body interaction representation. It is sharper than assigning one anchor term \(U_e\) to every link.

## 2. Shared-link interaction bound

Use the corrected isolated-face gradient estimate
\[
\|\nabla s_f\|_\infty\le2\beta_f,\qquad
\beta_f=\frac{|b_f|}{A_f},
\]
and the universal PF-I16 allocation bounds
\[
d_e\le8,\qquad A_f\ge a_0/2,\qquad a_e\le8A_f.
\]
For each shared link \(e\in\partial f\cap\partial g\),
\[
a_e\beta_f\beta_g
\le8A_f\frac{b_0}{A_f}\frac{b_0}{A_g}
\le\frac{16b_0^2}{a_0}.
\]
There are at most four shared links, and the factor in (1.3) contributes \(2(2\beta_f)(2\beta_g)=8\beta_f\beta_g\). Hence
\[
\boxed{
\|V_{fg}\|_\infty\le512\,\frac{b_0^2}{a_0}.
}
\tag{2.1}
\]
A face has at most \(4(8-1)=28\) neighboring accepted faces. Thus the total pair-interaction norm incident to a face is at most
\[
28\cdot512\,\frac{b_0^2}{a_0}
=14336\,\frac{b_0^2}{a_0}.
\tag{2.2}
\]
The face-overlap graph therefore has degree at most 28. This uses the universal \(d_e\le8\), not the stronger two-incidence observation from finite crops.

## 3. Candidate local activity margin

The product-rotor kinetic operator has one-link gap \(3a_e/4\) in the radius-two SU(2) normalization. In the product metric \(\tilde g_e=a_e^{-1}g_e\), the Ricci endomorphism on link \(e\) is \(a_e/2\); hence the corrected lower bound \(\operatorname{Ric}^{\sharp}_{\tilde g}\ge a_0/2\) gives \(a_e\ge a_0\). Therefore,
\[
\operatorname{gap}(K)\ge\Delta_0:=\frac{3a_0}{4}.
\]
A conservative per-face interaction weight, including all incident pair terms, is
\[
z_f:=b_0+14336\,\frac{b_0^2}{a_0}.
\]
At the corrected threshold \(x=b_0/a_0\le1/50000\),
\[
\frac{z_f}{\Delta_0}
\le\frac43x+\frac{57344}{3}x^2
<3.432\times10^{-5}.
\tag{3.1}
\]
Multiplying by the face-overlap degree gives
\[
28\,\frac{z_f}{\Delta_0}<9.608\times10^{-4},
\qquad
e\cdot28\,\frac{z_f}{\Delta_0}<2.612\times10^{-3}.
\tag{3.2}
\]
These are encouraging numerical margins for a polymer criterion on the face-overlap graph.

**Important limitation:** (3.2) is not yet a verified Kotecký–Preiss condition for the quantum ground-state problem. The required polymer activity norm must account for the unbounded local rotor Hilbert spaces, reduced-resolvent insertions, temporal ordering, and exact connected cancellation. No convergence claim is made until that theorem is proved with its actual constants.

## 4. Next theorem required

Prove a source-volume-uniform linked-cluster expansion for
\[
K-\sum_f b_fp_f+\sum_{f<g}V_{fg}
\]
with local interaction graph degree at most 28 and weights (2.1)–(2.2). The theorem must:
1. express the \(n\)-source ground-energy coefficient as a sum over connected face-overlap clusters or trees;
2. retain the exact disconnected-subsystem cancellation;
3. control the reduced-resolvent/time-ordering constants with at most exponential growth after the \(1/n!\) coefficient normalization;
4. yield a nonzero source-volume-uniform activity radius.

The one-cut and multi-cut interpolation routes remain independent alternatives. Neither is silently identified with this quantum cluster theorem. No R3-IR constants are imported.
