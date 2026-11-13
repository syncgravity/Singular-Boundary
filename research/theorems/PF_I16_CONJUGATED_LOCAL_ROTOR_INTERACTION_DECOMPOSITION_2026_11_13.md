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
=\sum_f A_f^{\rm kin}\left[\Delta s_f+|\nabla s_f|^2\right]
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
A_f^{\rm kin}:=\sum_{e\in\partial f}a_e.
\tag{1.3}
\]
The sum \(V_{fg}\) is zero unless the two accepted faces share an original link. Its support is contained in \(\partial f\cup\partial g\), of size at most eight links.

The isolated-face ground-state equation in the refined-rotor dossier is
\[
A_f(-\Delta)\psi_f-b_fp_f\psi_f=E_f\psi_f,\qquad
s_f=\log\psi_f,
\]
so
\[
A_f\left[\Delta s_f+|\nabla s_f|^2\right]
=-b_fp_f-E_f.
\tag{1.4}
\]
Do not identify \(A_f\) with \(A_f^{\rm kin}\) unless that equality is separately established. The recorded allocation bounds give
\[
\rho_f:=\frac{A_f^{\rm kin}}{A_f}
\le4\cdot8=32.
\]
Thus the one-face term is \(-\rho_fb_fp_f-\rho_fE_f\); after dropping the scalar, its norm is at most \(32b_0\). Therefore, up to a scalar energy shift,
\[
\boxed{
e^\Phi L_\Phi e^{-\Phi}
=K-\sum_f \rho_fb_fp_f+\sum_{f<g}V_{fg}.
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
z_f:=32b_0+14336\,\frac{b_0^2}{a_0}.
\]
At the corrected threshold \(x=b_0/a_0\le1/50000\),
\[
\frac{z_f}{\Delta_0}
\le\frac{128}{3}x+\frac{57344}{3}x^2
<8.610\times10^{-4}.
\tag{3.1}
\]
Multiplying by the face-overlap degree gives
\[
28\,\frac{z_f}{\Delta_0}<2.411\times10^{-2},
\qquad
e\cdot28\,\frac{z_f}{\Delta_0}<6.554\times10^{-2}.
\tag{3.2}

These are encouraging numerical margins for a polymer criterion on the face-overlap graph.

**Important limitation:** (3.2) is not yet a verified Kotecký–Preiss condition for the quantum ground-state problem. The required polymer activity norm must account for the unbounded local rotor Hilbert spaces, reduced-resolvent insertions, temporal ordering, and exact connected cancellation. No convergence claim is made until that theorem is proved with its actual constants.

## 4. Cut derivatives become bounded multiplication insertions after conjugation

For the multi-cut interpolation, write
\[
\Phi_{\mathbf s}=\sum_f\alpha_f(\mathbf s)s_f(H_f),
\qquad
\alpha_f(\mathbf s)=\prod_{a\in C_f}s_a,\qquad 0\le\alpha_f\le1.
\]
The exact face/pair decomposition becomes
\[
\mathcal U_{\Phi_{\mathbf s}}
=\sum_f A_f^{\rm kin}
\left[\alpha_f\Delta s_f+\alpha_f^2|\nabla s_f|^2\right]
+\sum_{f<g}\alpha_f\alpha_gV_{fg}.
\tag{4.1}
\]
For a tree-cut parameter \(s_a\), put \(\alpha_{f,a}=\partial_{s_a}\alpha_f\), which is zero unless \(a\in C_f\) and otherwise has magnitude at most one. Then
\[
\begin{aligned}
\partial_{s_a}\mathcal U_{\Phi_{\mathbf s}}
={}&\sum_f A_f^{\rm kin}\alpha_{f,a}
\left[\Delta s_f+2\alpha_f|\nabla s_f|^2\right]\\
&+\sum_{f<g}
(\alpha_{f,a}\alpha_g+\alpha_f\alpha_{g,a})V_{fg}.
\end{aligned}
\tag{4.2}
\]
This is a bounded multiplication operator, supported on face and adjacent-face-pair terms crossing cut \(a\).

The isolated-rotor equation gives
\[
\Delta s_f+2\alpha_f|\nabla s_f|^2
=(2\alpha_f-1)|\nabla s_f|^2-\beta_fp_f-\lambda_f.
\]
Using \(|\lambda_f|\le\beta_f\), \(\|p_f\|_\infty\le1\), \(\|\nabla s_f\|_\infty\le2\beta_f\), \(A_f^{\rm kin}/A_f\le32\), and \(A_f\ge a_0/2\), each one-face derivative insertion is bounded by
\[
\left\|A_f^{\rm kin}\alpha_{f,a}
[\Delta s_f+2\alpha_f|\nabla s_f|^2]\right\|_\infty
\le64b_0+256\,\frac{b_0^2}{a_0}.
\tag{4.3}
\]
The pair derivative coefficient in (4.2) is at most two, so
\[
\|(\alpha_{f,a}\alpha_g+\alpha_f\alpha_{g,a})V_{fg}\|_\infty
\le1024\,\frac{b_0^2}{a_0}.
\tag{4.4}
\]
Since each face has at most 28 neighbors, the incident cut-insertion weight per face is bounded by
\[
z_{\rm cut}
\le64b_0+28928\,\frac{b_0^2}{a_0}.
\tag{4.5}
\]
Relative to \(\Delta_0=3a_0/4\), at \(x=b_0/a_0\le1/50000\),
\[
\frac{z_{\rm cut}}{\Delta_0}
\le\frac{256}{3}x+\frac{115712}{3}x^2
<1.723\times10^{-3},
\quad
28\frac{z_{\rm cut}}{\Delta_0}<4.822\times10^{-2}.
\tag{4.6}
\]
These are candidate local insertion margins only; they are not a quantum polymer criterion.

Let \(\widehat H_{\mathbf s,\mathbf t}
=K+\mathcal U_{\Phi_{\mathbf s}}-\sum_i t_ir_i\) on product Haar space. Its spectrum agrees with that of \(L_{\Phi_{\mathbf s}}-\sum_i t_ir_i\), and ordinary Hellmann–Feynman gives
\[
\partial_{s_a}E_{\mathbf s}(\mathbf t)
=\langle\Psi_{\mathbf s,\mathbf t},
(\partial_{s_a}\mathcal U_{\Phi_{\mathbf s}})
\Psi_{\mathbf s,\mathbf t}\rangle
\]
for the corresponding simple ground state; the desired source coefficient is obtained by taking \([t_I]\) on both sides. Thus the multi-cut derivatives become insertions of bounded local multiplication operators, rather than the first-order differential insertion \(\Gamma(W_a,g)\) in the dressed-measure picture. Mixed derivatives still require connected resolvent/cumulant bounds, but the \(D^2g\) obstruction in (4.2) of the multi-cut note is avoided at the level of the insertion itself.

## 5. External framework audit: Yarotsky

Yarotsky's theorem is a relevant comparison: it treats weak local perturbations of a gapped product-ground-state model, explicitly allows possibly infinite-dimensional one-site Hilbert spaces, and proves a volume-uniform gap, exponential truncated-correlation decay, and analytic dependence under a sufficiently small perturbation hypothesis. Its stated setting, however, is translation-invariant interactions on \(\mathbb Z^\nu\), with a smallness threshold depending on the dimension and interaction range. The PF-I16 accepted-link graph is nonperiodic, and the theorem's threshold is existential rather than the explicit numerical criterion needed here. Therefore this is not yet an application to the present graph or a certification that \(b_0/a_0\le1/50000\) lies below its threshold.

Reference: D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, arXiv:math-ph/0412040, especially Theorem 1 and the space-time polymer proof in Section 2.

## 6. Next theorem required
Prove a source-volume-uniform linked-cluster expansion for
\[
K-\sum_f \rho_fb_fp_f+\sum_{f<g}V_{fg}
\]
with local interaction graph degree at most 28 and weights (2.1)–(2.2). The theorem must:
1. express the \(n\)-source ground-energy coefficient as a sum over connected face-overlap clusters or trees;
2. retain the exact disconnected-subsystem cancellation;
3. control the reduced-resolvent/time-ordering constants with at most exponential growth after the \(1/n!\) coefficient normalization;
4. yield a nonzero source-volume-uniform activity radius.

The exact two-cut reduced-resolvent identity and the corrected along-interpolation local activity sums are now recorded in `research/theorems/PF_I16_TWO_CUT_CONNECTED_RESOLVENT_TREE_LEMMA_2026_11_13.md`. The weighted per-link background sum is \(\kappa_H<0.022695\) at \(a=1/8\); this is a candidate local activity input, not a verified quantum polymer criterion. The one-cut and multi-cut interpolation routes remain independent alternatives. Neither is silently identified with this quantum cluster theorem. No R3-IR constants are imported.


## 7. Source inputs and verification

The isolated-rotor derivative and face-map bounds are conditional source inputs from:
- `research/audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md`
- `research/theorems/PF_I16_CORRECTED_REVERSIBLE_FLOW_AND_TWO_POINT_RESOLVENT_DECAY_2026_11_13.md`

The arithmetic in (3.1)–(3.2) is checked by `research/verification/verify_pf_i16_local_rotor_cluster_margin.py`. The verifier checks only the numerical inequalities; it does not certify the quantum cluster expansion.
