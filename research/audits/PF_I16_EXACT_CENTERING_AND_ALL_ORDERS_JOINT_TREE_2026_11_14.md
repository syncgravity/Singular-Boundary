# PF-I16 — Exact centering of face/pair interactions and all-orders joint-tree reduction

**Date:** 2026-11-14  
**Status:** exact centering identities and local centered activity are established under the product-Haar reference law and the stated face-map geometry. The all-orders support-sensitive joint tree remains open; the precise missing quasi-factorization lemma is isolated below.  
**Scope:** conjugated finite-graph product-rotor Hamiltonian. No quantum KP convergence, interacting-vacuum gap, or continuum theorem.

## 1. The actual local insertions

Use the exact face/pair decomposition
\[
e^\Phi L_\Phi e^{-\Phi}
=K+\sum_f v_f+\sum_{f<g}v_{fg}+\text{scalar},
\]
with
\[
v_f=-\rho_f b_f p_f,\qquad
\rho_f=A_f^{\rm kin}/A_f\le32,
\]
and
\[
v_{fg}=2\sum_{e\in\partial f\cap\partial g}
a_e\langle\nabla_e s_f,\nabla_e s_g\rangle.
\]
The scalar \(-\rho_fE_f\) is irrelevant to cumulants of order at least two.

The isolated-rotor radial coordinate has Haar density proportional to \(\sin^2\theta\,d\theta\), and \(p_f=\cos\theta_f\). Hence
\[
\mathbb E_0p_f
=\frac{\int_0^\pi\cos\theta\sin^2\theta\,d\theta}
{\int_0^\pi\sin^2\theta\,d\theta}=0.
\]
Therefore
\[
\boxed{\mathbb E_0v_f=0,\qquad
\|v_f-\mathbb E_0v_f\|_\infty
=\|v_f\|_\infty\le32b_0.}
\tag{1.1}
\]

## 2. Pair interaction is exactly centered

Fix distinct faces \(f,g\), and let
\[
C=\partial f\cap\partial g,\quad
P_f=\partial f\setminus C,\quad
P_g=\partial g\setminus C.
\]
For distinct elementary faces, both private sets are nonempty and disjoint. Condition on all shared link variables \(U_C\). Under product Haar measure, the private link variables in \(P_f\) and \(P_g\) are independent. Because each face holonomy is a product containing at least one private Haar link, \(H_f\) and \(H_g\) are conditionally independent Haar variables given \(U_C\).

For any shared link \(e\in C\), differentiation with respect to \(U_e\) commutes with integration over the private links. Haar invariance gives
\[
\mathbb E_0[\nabla_e s_f(H_f)\mid U_C]
=\nabla_e\mathbb E_0[s_f(H_f)\mid U_C]
=\nabla_e\int_{SU(2)}s_f(H)\,dH=0,
\]
and likewise for \(g\). Conditional independence then implies
\[
\mathbb E_0[
\langle\nabla_e s_f,\nabla_e s_g\rangle
\mid U_C]=0.
\]
Summing over shared links proves
\[
\boxed{\mathbb E_0v_{fg}=0,\qquad
\|v_{fg}-\mathbb E_0v_{fg}\|_\infty
=\|v_{fg}\|_\infty
\le512\,\frac{b_0^2}{a_0}.}
\tag{2.1}
\]
The proof allows more than one shared link; it uses only that distinct face boundaries have nonempty disjoint private link sets. If the source geometry admits coincident face boundaries under distinct labels, that case must be excluded or separately treated.

**Consequence:** the factor-two centering loss in the previous generic estimate is absent for the actual face and pair insertions in this conjugated decomposition. This conclusion is specific to the product-Haar reference law and these exact insertions; it must not be transferred to a different per-link interaction representation without checking its means.

## 3. Centered face activity and numerical margin

A face has at most 28 neighboring faces. Its one-face interaction plus all incident pair interactions is bounded by
\[
z_f=32b_0+28\cdot512\frac{b_0^2}{a_0}
=32b_0+14336\frac{b_0^2}{a_0}.
\]
With \(x=b_0/a_0\le1/50000\) and \(\Delta_0=3a_0/4\),
\[
\boxed{
\frac{z_f}{\Delta_0}
=\frac{128}{3}x+\frac{57344}{3}x^2
\le0.0008609792.}
\tag{3.1}
\]
For a local insertion supported on one face or a pair of adjacent faces, its closed face-neighborhood contains at most 58 faces. Thus the conservative continuation activity is
\[
\boxed{
q_{\rm face}:=58\frac{z_f}{\Delta_0}
\le0.0499367936.}
\tag{3.2}
\]
If the all-orders support-sensitive tree estimate holds with \(C_{\rm st}=2\), and the rooted-tree/time integration step has exactly the factors recorded in the joint-cluster dossier, the candidate background parameter is
\[
q_{\rm joint}
\le 2\cdot2\cdot e\,q_{\rm face}
<0.543<1.
\tag{3.3}
\]
The first factor 2 is the proposed cumulant-tree coefficient; the second is
\(\int_{\mathbb R}e^{-\Delta_0|t-s|}dt=2/\Delta_0\); and \(e\) is the rooted-tree/Stirling factor. Equation (3.3) is conditional on the all-orders joint tree and the exact rooted-cluster counting. It is not a KP theorem.

The earlier quantity \(\kappa_H\) from the separate per-link insertion inventory is a different activity majorant. Equations (1.1)–(3.3) replace the generic centering step only for the exact face/pair Hamiltonian above; they do not retroactively alter that other inventory.

## 4. The all-orders support-sensitive target

For local bounded multiplication insertions \(A_i(t_i)\) with link supports \(X_i\), the desired theorem is
\[
\boxed{
|\kappa_0(A_1(t_1),\ldots,A_m(t_m))|
\le C_{\rm st}^{m}\prod_i\|A_i\|_\infty
\sum_{T\in\mathcal T(G_{\rm ov})}
\prod_{\{i,j\}\in T}
\mathbf1_{\{X_i\cap X_j\ne\varnothing\}}
e^{-\Delta_0|t_i-t_j|},
}
\tag{4.1}
\]
where \(G_{\rm ov}\) is the support-overlap graph. Disconnected support families have zero cumulant exactly, by independence of link path processes.

If (4.1) holds, every tree term has the uniform integral
\[
\int_{[0,\mathcal T]^m}
\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|}\,d\mathbf t
\le \mathcal T\left(\frac2{\Delta_0}\right)^{m-1},
\]
by rooting and integrating leaves. The remaining sum is over trees of the actual support graph, not the complete graph. Repeated interaction labels are allowed; their incompatibility is represented by the corresponding repeated-vertex clique. The rooted-cluster estimate must sum these repetitions with the activities in (3.1), rather than replace the graph by a volume-dependent maximum degree.

## 5. Exact quasi-factorization reduction

A sufficient model-specific input is the following weighted quasi-factorization estimate. For every finite row set \(I\) and every nontrivial split \(I=J\sqcup K\),
\[
\left|
\mathbb E_0\prod_{i\in I}A_i(t_i)
-\mathbb E_0\prod_{i\in J}A_i(t_i)\,
 \mathbb E_0\prod_{i\in K}A_i(t_i)
\right|
\le C_{\rm qf}^{|I|}
\prod_{i\in I}\|A_i\|_\infty
\sum_{\substack{i\in J,\,j\in K}}
\mathbf1_{\{X_i\cap X_j\ne\varnothing\}}
e^{-\Delta_0|t_i-t_j|}.
\tag{5.1}
\]
If (5.1) is proved uniformly, the standard connected-partition/forest expansion can be organized by first separating components and then attaching them across cross-split bonds. A tree-graph majorant would then give (4.1), with an explicit exponential renormalization of \(C_{\rm qf}\). The reduction is useful because it identifies exactly what the product-path law must supply: approximate factorization across a row split, with no dependence unless a shared link is present, and with the temporal cost paid on that same shared-link edge.

**Important:** (5.1) is not yet proved here. The one-link Boolean-cumulant estimate gives a full-span bound but its classical-cumulant conversion has a factorial envelope. The global product-process projection tree gives exponential-order coefficients but its tree edges are unrestricted in support. The Leonov–Shiryaev slot expansion has large partition fibers if absolute values are taken term by term. None of these three facts alone proves (5.1).

## 6. Why the current all-orders routes do not yet close (4.1)

1. The global product-process estimate is
\[
|\kappa_0(A_1(t_1),\ldots,A_m(t_m))|
\le2^m\prod_i\|A_i\|_\infty
\sum_{T\in\mathcal T_m}\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|}.
\]
It has the correct exponential-in-order coefficient, but the complete-graph tree sum does not imply the support-restricted sum in (4.1).

2. The exact Leonov–Shiryaev formula connects rows through shared link labels, and every individual connected slot-partition term contains a support-overlap spanning tree. However, the number of slot-partition fibers can be superexponential. Taking absolute values before resumming loses the cancellations demonstrated by the degree-eight Rademacher witness.

3. The temporal-forest plus spatial-component-tree completion has the correct edge count, but the full source tuple includes two component trees. The proposed two-port split is refuted by the recorded non-endpoint witness example; exact temporal-profile preservation can be impossible for that completion architecture.

4. The weighted-dependency-graph route still needs a continuous-time product quasi-factorization estimate with explicit order growth. The one-link estimate alone has a factorial envelope after conversion from Boolean to classical cumulants; the degree-eight product lift does not yet provide the required exponential-order coefficient.

## 7. Concrete next proof obligation

Prove (5.1) directly for products of local multiplication observables of the independent stationary link processes, with a constant \(C_{\rm qf}\) whose growth is exponential in \(|I|\), and with the cross-split edge carrying the same shared-link temporal kernel. A promising route is a link-by-link interpolation between the shared path and independently copied paths, but the interpolation must handle interlaced time sets; a simple separation-of-time-blocks argument is insufficient.

After (5.1), write the connected-partition tree-graph reduction with all coefficients and constants, then insert the centered activities (3.1)–(3.2). Until that is done, (4.1), the KP expansion, and P3 remain OPEN.

**Gate status:** exact centered local activity — established under the stated product-Haar geometry; all-orders support-sensitive joint tree — OPEN; KP convergence — OPEN; no P0–P5 status promoted.
