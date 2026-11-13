# PF-I16 — Two-cut connected-resolvent identity and weighted local activity audit

**Date:** 2026-11-13  
**Status:** exact finite-volume resolvent identities and conditional local norm arithmetic. The quantum connected-cluster/tree inequality is still OPEN. No source-volume-uniform convergence is claimed.

## 1. Product-rotor Hamiltonian and local interaction family

Write the conjugated multi-cut Hamiltonian as
\[
\widehat H_{\mathbf s,\mathbf t}
=K+\mathcal U_{\Phi_{\mathbf s}}-\sum_i t_i r_i,
\qquad
K=\sum_e a_e(-\Delta_e),
\]
on product Haar space. The unperturbed product ground state is the constant vector and
\[
\operatorname{gap}(K)\ge\Delta_0:=3a_0/4.
\]
For each accepted face \(f\), put \(G_f=|\nabla s_f|^2\), and
\[
v_f(\mathbf s)
=A_f^{\rm kin}\bigl[\alpha_f\Delta s_f+\alpha_f^2G_f\bigr],
\qquad
v_{fg}(\mathbf s)=\alpha_f\alpha_gV_{fg}.
\]
Then
\[
\mathcal U_{\Phi_{\mathbf s}}=\sum_fv_f(\mathbf s)+\sum_{f<g}v_{fg}(\mathbf s).
\]
The singleton support has at most four links; the pair support has at most eight links.

The isolated-rotor identity gives
\[
\Delta s_f+G_f=-\beta_f(p_f+\lambda_f/\beta_f),
\quad
|\lambda_f|\le\beta_f,\quad
\|G_f\|_\infty\le4\beta_f^2,\quad
\beta_f\le b_0/A_f.
\]
Using \(A_f^{\rm kin}/A_f\le32\) and \(A_f\ge a_0/2\),
\[
\boxed{\|v_f(\mathbf s)\|_\infty
\le64b_0+64b_0^2/a_0,}
\qquad
\boxed{\|v_{fg}(\mathbf s)\|_\infty
\le512b_0^2/a_0.}
\tag{1.1}
\]
For the first inequality, use
\[
\alpha_f\Delta s_f+\alpha_f^2G_f
=-\alpha_f\beta_f(p_f+\lambda_f/\beta_f)
-\alpha_f(1-\alpha_f)G_f,
\]
and \(\alpha_f(1-\alpha_f)\le1/4\).

## 2. First and second cut insertions

For distinct cut parameters \(a,b\), set
\[
B_a=\partial_{s_a}\mathcal U_{\Phi_{\mathbf s}},
\qquad
B_{ab}=\partial_{s_a}\partial_{s_b}\mathcal U_{\Phi_{\mathbf s}}.
\]
Writing \(\alpha_{f,a}=\partial_{s_a}\alpha_f\), the first local pieces are
\[
b_{a,f}=A_f^{\rm kin}\alpha_{f,a}
[\Delta s_f+2\alpha_fG_f],
\quad
b_{a,fg}=(\alpha_{f,a}\alpha_g+\alpha_f\alpha_{g,a})V_{fg}.
\]
Since
\[
\Delta s_f+2\alpha_fG_f
=(2\alpha_f-1)G_f-\beta_f(p_f+\lambda_f/\beta_f),
\]
we have
\[
\boxed{\|b_{a,f}\|_\infty\le64b_0+256b_0^2/a_0,\qquad
\|b_{a,fg}\|_\infty\le1024b_0^2/a_0.}
\tag{2.1}
\]

The exact second derivative is
\[
\begin{aligned}
b_{ab,f}
&=A_f^{\rm kin}\left\{
\alpha_{f,ab}[\Delta s_f+2\alpha_fG_f]
+2\alpha_{f,a}\alpha_{f,b}G_f\right\},\\
b_{ab,fg}
&=(\alpha_{f,ab}\alpha_g+\alpha_{f,a}\alpha_{g,b}
+\alpha_{f,b}\alpha_{g,a}+\alpha_f\alpha_{g,ab})V_{fg}.
\end{aligned}
\]
For distinct cuts, \(|\alpha_{f,a}|,|\alpha_{f,b}|,|\alpha_{f,ab}|\le1\). Therefore
\[
\boxed{\|b_{ab,f}\|_\infty\le64b_0+768b_0^2/a_0,\qquad
\|b_{ab,fg}\|_\infty\le2048b_0^2/a_0.}
\tag{2.2}
\]
Thus the two-cut contact term \(B_{ab}\), as well as the two first-cut insertions, is a sum of bounded local multiplication operators. Its local supports are still at most eight links.

## 3. Exact two-cut reduced-resolvent identity

Fix finite volume and parameters \((\mathbf s,\mathbf t)\) for which the lowest eigenvalue \(E\) of \(\widehat H_{\mathbf s,\mathbf t}\) is simple and isolated. Let \(\Psi\) be its normalized eigenvector,
\[
Q=1-|\Psi\rangle\langle\Psi|,
\qquad
R=Q(\widehat H_{\mathbf s,\mathbf t}-E)^{-1}Q.
\]
Ordinary eigenvalue perturbation theory gives the exact identities
\[
\partial_{s_a}E=\langle B_a\rangle,
\]
and
\[
\boxed{
\partial_{s_a}\partial_{s_b}E
=\langle B_{ab}\rangle
-\langle B_aRB_b\rangle-\langle B_bRB_a\rangle.
}
\tag{3.1}
\]
The \(Q\)'s in \(R\) automatically center the two outer insertions. No global norm bound on \(B_a\) or \(B_b\) is used in (3.1).

For distinct source labels \(i,j\), the coefficient of \(t_it_j\) is therefore exactly the sum of:
- the third connected ground-energy response with marked insertions \(B_{ab},-r_i,-r_j\);
- the fourth connected ground-energy response with marked insertions \(B_a,B_b,-r_i,-r_j\), with the sign fixed by (3.1).

More formally, if
\[
\mathfrak C_m^H(A_1,\ldots,A_m)
:=\left.
\partial_{\theta_1}\cdots\partial_{\theta_m}
E_0\!\left(H+\sum_{k=1}^m\theta_kA_k\right)
\right|_{\boldsymbol\theta=0},
\]
then
\[
\boxed{
[t_it_j]\,\partial_{s_a}\partial_{s_b}E(\mathbf s,\mathbf t)\big|_{\mathbf t=0}
=
\mathfrak C_3^{H_{\mathbf s}}(B_{ab},-r_i,-r_j)
+
\mathfrak C_4^{H_{\mathbf s}}(B_a,B_b,-r_i,-r_j).
}
\tag{3.2}
\]
Here the second term is the full fourth derivative, including the two reduced-resolvent orderings and all normalization subtractions. Equation (3.2) is an identity, not yet a decay estimate.

## 4. Per-link weighted activity sums

A link belongs to at most eight accepted faces. Each such face has at most 28 neighboring faces. Thus, conservatively, a fixed link belongs to at most:
- eight singleton-face interaction supports;
- \(8\cdot28=224\) adjacent-face-pair supports.

For a support \(X\), use the weighted local activity
\[
z_X(a)=\frac{\|v_X\|_\infty}{\Delta_0}e^{a|X|}.
\]
Choose \(a=1/8\). Then \(e^{a|X|}\le e^{1/2}\) for singleton terms and \(\le e\) for pair terms. Using the rigorous elementary upper bounds \(e^{1/2}<1.65\), \(e<2.72\), and \(x=b_0/a_0\le1/50000\), the per-link sums satisfy
\[
\begin{aligned}
\kappa_H
&:=\sup_e\sum_{X\ni e}z_X(1/8)
\\
&\le\frac{8(64x+64x^2)(1.65)+224(512x^2)(2.72)}{3/4}
<0.022695,
\\[2mm]
\kappa_a
&:=\sup_e\sum_{X\ni e}
\frac{\|b_{a,X}\|_\infty}{\Delta_0}e^{|X|/8}
<0.022863,
\\
\kappa_{ab}
&:=\sup_e\sum_{X\ni e}
\frac{\|b_{ab,X}\|_\infty}{\Delta_0}e^{|X|/8}
<0.023199.
\end{aligned}
\tag{4.1}
\]
These sums are uniform in the number of links. The cut insertions are marked-root families; they need not be small as global operators. The source observables \(r_i\) are also marked roots, with \(|S_i|\le25\), so their support-weight factor obeys \(e^{|S_i|/8}<23\).

The numerical path-contraction candidate
\[
q_{\rm path}:=8e\,\kappa_H
<8(2.72)(0.022695)<0.494<1
\tag{4.2}
\]
allows for at most eight choices of the next link inside an interaction support and an additional factor \(e\) in the rooted connected-cluster count. Equation (4.2) is only a combinatorial candidate. It does not by itself bound the time-ordered reduced-resolvent integrals.

The arithmetic in (4.1)–(4.2) is checked by the verifier
research/verification/verify_pf_i16_connected_resolvent_activity.py.

## 5. The exact connected-resolvent/tree lemma still required

The needed quantum statement is a finite-volume, graph-uniform linked-cluster estimate for the product-rotor reference \(K\) perturbed by the bounded local family \(\{v_X(\mathbf s)\}\). For marked local operators \(A_k\) with supports \(S_k\), it must prove
\[
\boxed{
|\mathfrak C_m^{H_{\mathbf s}}(A_1,\ldots,A_m)|
\le C_*^m\left(\prod_{k=1}^m\|A_k\|\right)
\sum_{T\in\mathcal T_m}
\prod_{\{p,q\}\in T}w_*(S_p,S_q),
}
\tag{5.1}
\]
where:
1. \(C_*\) is independent of source volume and grows at most exponentially in \(m\);
2. \(w_*(S,T)\le C_0e^{-\mu d_{\rm int}(S,T)}\), with \(d_{\rm int}\) the interaction-support graph distance;
3. the proof controls the time-ordered reduced-resolvent integrals for unbounded one-link rotor kinetic energies and bounded finite-support multiplication perturbations;
4. disconnected support families cancel exactly in \(\mathfrak C_m\);
5. the cluster activity criterion is stated with its actual constants and verified against \(\kappa_H\), rather than inferred from (4.2).

The elementary spatial combinatorics are favorable: a connected sequence of local interaction supports has at most eight choices of the next link within each support, and its weighted continuation is governed by (4.2). What is not yet established is the quantum temporal/resolvent estimate that turns this path count into (5.1). In particular, the factor \(e\) in (4.2) is not a substitute for a proof that the ordered time integrals and all vacuum-return subtractions are bounded by the claimed rooted-cluster weight.

Applying (5.1) to (3.2), then summing the marked cut-root families using \(\kappa_a,\kappa_{ab}\), would give the two-cut connected tree estimate. The same argument must then be extended to \(m=n-1\) cut insertions. The higher mixed derivatives of \(\alpha_f^2\) grow at most as \(2^m\) for distinct cuts, so their coefficient combinatorics are exponential; the unresolved issue remains the uniform quantum connected-resolvent estimate.

**Status:** exact two-cut identity and local activity sums derived; (5.1) OPEN. No all-orders activity radius is claimed.


## 6. Feynman–Kac reduction to a product Markov-path cumulant problem

Because \(K\) is a sum of independent compact-group Laplacians and every \(v_X\) is a bounded multiplication operator, the finite-volume Feynman–Kac formula gives
\[
Z_T(\mathbf s,\mathbf t)
:=\langle\mathbf1,e^{-T\widehat H_{\mathbf s,\mathbf t}}\mathbf1\rangle
=
\mathbb E_0\exp\left[
-\int_0^T\left\{
\sum_Xv_X(\mathbf s;U_X(\tau))
-\sum_i t_ir_i(U_{S_i}(\tau))
\right\}d\tau
\right],
\tag{6.1}
\]
where \(\mathbb E_0\) is the stationary path law of independent SU(2) Brownian motions, one for each link. In finite volume, positivity improvement gives nonzero overlap of the positive ground state with \(\mathbf1\), and hence
\[
E_0(\widehat H_{\mathbf s,\mathbf t})
=-\lim_{T\to\infty}\frac1T\log Z_T(\mathbf s,\mathbf t).
\tag{6.2}
\]
Thus the reduced-resolvent derivatives in (3.2) can equivalently be studied as long-time connected cumulants of local observables along independent reference paths, tilted by the local potential family \(v_X\).

At fixed \(T\), the formal cumulant expansion around the independent path law is
\[
\log Z_T
=
\sum_{m\ge1}\frac{(-1)^m}{m!}
\sum_{X_1,\ldots,X_m}
\int_{[0,T]^m}
\kappa_0\!\left(
v_{X_1}(t_1),\ldots,v_{X_m}(t_m)
\right)\,d\mathbf t,
\tag{6.3}
\]
with source and cut insertions treated as marked local vertices when differentiating in \(\mathbf t\) and \(\mathbf s\). Equation (6.3) is initially a coefficient identity near zero coupling; its uniform convergence as \(T\to\infty\) is part of the open task.

There is an exact spatial cancellation before any estimate: if the overlap graph of \(X_1,\ldots,X_m\) is disconnected, the corresponding groups depend on disjoint sets of independent link paths. Their joint cumulant in (6.3) is therefore zero. This is the desired disconnected-subsystem cancellation, now expressed directly on the product-path reference measure.

The temporal estimate is now established as follows. For bounded local multiplication observables \(A_k\) supported on \(S_k\), prove
\[
\left|\kappa_0(A_1(t_1),\ldots,A_m(t_m))\right|
\le C_{\rm time}^{\,m}
\left(\prod_k\|A_k\|_\infty\right)
\mathbf1_{\{\mathcal G_{\rm ov}\ {\rm connected}\}}
\sum_{T\in\mathcal T_m}
\prod_{\{p,q\}\in T}e^{-\Delta_0|t_p-t_q|},
\tag{6.4}
\]
where \(\mathcal G_{\rm ov}\) is the graph joining support-overlapping local observables, and \(\mathcal T_m\) is the set of all labeled spanning trees on the time indices (the temporal tree is not required to be an edge of \(\mathcal G_{\rm ov}\)). The constant \(C_{\rm time}\) must be explicit and at most exponential in \(m\). The one-link spectral gap supplies
\[
\|P_\tau-\Pi\|_{2\to2}\le e^{-\Delta_0\tau};
\]
the all-orders proof propagates this estimate through the full cumulant partition formula by the port-completion injection; exact spatial cancellation follows independently from product-path independence when the support-overlap graph is disconnected. The resulting constant is \\(C_{\\rm time}=2\\), not merely the earlier target \\(C_{\\rm time}\\le2.5\\).

For every fixed temporal tree \(T\), the time integral is elementary:
\[
\int_{[0,T_0]^m}
\prod_{\{p,q\}\in T}e^{-\Delta_0|t_p-t_q|}
\,d\mathbf t
\le
T_0\left(\frac{2}{\Delta_0}\right)^{m-1}.
\tag{6.5}
\]
Root the tree at one time variable, integrate the root over an interval of length \(T_0\), and integrate each remaining vertex relative to its parent over the real line. The resulting local polymer activity is
\[
z_X=\frac{2C_{\rm time}\|v_X\|_\infty}{\Delta_0}.
\]
For the standard support-incompatibility criterion, it is sufficient that
\[
\sup_e\sum_{X\ni e}z_Xe^{a|X|}\le a.
\tag{6.6}
\]
At \(a=1/8\), our verified \(\kappa_H<0.022695\) makes (6.6) hold whenever
\[
C_{\rm time}\le \frac{a}{2\kappa_H}<2.754.
\tag{6.7}
\]
Thus the local activity arithmetic is sufficient for this explicit KP target provided the temporal cumulant tree inequality is proved with \(C_{\rm time}\le2.75\). The marked cut-root sums \(\kappa_a,\kappa_{ab}\) and the source support factor \(e^{25/8}<23\) then contribute only finite external-root prefactors; they are not background convergence activities. The provisional \(q_{\rm path}\) in (4.2) is not used as a substitute for (6.4).

For the two-cut coefficient, the marked vertices are \(B_{ab}\), \(B_a\), \(B_b\), \(r_i\), and \(r_j\); the unmarked vertices are the background \(v_X\) insertions from (6.3). A connected tree on these marked and unmarked vertices, summed over the background vertices, is the precise object that should yield the two-cut spatial tree estimate. This gives a concrete route to (5.1): (6.4) is now CLOSED, while the resulting uniform-in-volume polymer convergence and the full estimate (5.1) remain OPEN pending a proof of the joint space-time/support cluster summation.



## 7. Explicit temporal cumulant checks through four marked vertices

The first three temporal orders can be controlled directly under the independent product path law. Center each \(A_k\) with respect to product Haar and order the times \(t_1\le\cdots\le t_m\). Write \(g_k=t_{k+1}-t_k\), \(P_t=e^{-tK}\), \(Q_t=P_t-\Pi\). Since the product semigroup has gap \(\Delta_0\),
\[
\|Q_t\|_{2\to2}\le e^{-\Delta_0t}.
\]

For \(m=2\),
\[
\kappa_0(A_1(t_1),A_2(t_2))
=\langle A_1Q_{g_1}A_2\rangle,
\qquad
|\kappa_0|\le e^{-\Delta_0g_1}\prod_k\|A_k\|_\infty.
\tag{7.1}
\]
For \(m=3\), centering kills both one-point partition terms and
\[
\kappa_0(A_1(t_1),A_2(t_2),A_3(t_3))
=\langle A_1Q_{g_1}A_2Q_{g_2}A_3\rangle,
\]
so
\[
|\kappa_0|\le
e^{-\Delta_0(g_1+g_2)}\prod_k\|A_k\|_\infty.
\tag{7.2}
\]
For \(m=4\), the exact centered partition subtraction gives
\[
\begin{aligned}
\kappa_0(A_1,A_2,A_3,A_4)
={}&\langle A_1Q_{g_1}A_2Q_{g_2}A_3Q_{g_3}A_4\rangle\\
&-\langle A_1Q_{g_1+g_2}A_3\rangle
 \langle A_2Q_{g_2+g_3}A_4\rangle\\
&-\langle A_1Q_{g_1+g_2+g_3}A_4\rangle
 \langle A_2Q_{g_2}A_3\rangle.
\end{aligned}
\tag{7.3}
\]
Each of the three terms is bounded by
\(e^{-\Delta_0(g_1+g_2+g_3)}\prod_k\|A_k\|_\infty\), hence
\[
|\kappa_0(A_1,A_2,A_3,A_4)|
\le3e^{-\Delta_0(t_4-t_1)}\prod_k\|A_k\|_\infty.
\tag{7.4}
\]
These identities verify the temporal decay mechanism for the marked orders needed by the bare two-cut response. They do not control the higher cumulant orders generated when the background interaction family \(v_X\) is expanded.

For each ordered time simplex,
\[
\int_{0\le t_1\le\cdots\le t_m\le T_0}
e^{-\Delta_0(t_m-t_1)}\,d\mathbf t
\le T_0\Delta_0^{-(m-1)}.
\tag{7.5}
\]
The missing all-orders step is to extend the explicit projection/cumulant cancellation in (7.1)–(7.3) to arbitrary \(m\), with a sufficiently sharp exponential-in-\(m\) coefficient after the time-ordering normalization. A factorial bound here would not establish a nonzero activity radius. This is the remaining temporal core of (6.4).


## 8. Cumulant projection count and the numerical threshold for the temporal lemma

There is a useful combinatorial reduction for the arbitrary-order projection expansion. Center all \(A_i\). In the moment-cumulant formula, a partition \(\pi\) with \(k\) blocks has Möbius coefficient \((k-1)!\). Expanding each semigroup between consecutive times in each block as \(P_\tau=\Pi+Q_\tau\) produces at most \(2^{m-k}\) projection terms. Thus the total absolute coefficient count before cancellations is bounded by
\[
S_m:=\sum_{k=1}^m {m\brace k}(k-1)!\,2^{m-k},
\tag{8.1}
\]
where \({m\brace k}\) is a Stirling number of the second kind. Since
\[
{m\brace k}\le\frac{k^m}{k!},
\]
we get
\[
S_m\le\sum_{k=1}^m k^{m-1}2^{m-k}
\le m^{m-2}\sum_{k=1}^m k\,2^{m-k}
<2^{m+1}m^{m-2}.
\tag{8.2}
\]
For \(m\ge4\), \(2^{m+1}\le(5/2)^m\); the cases \(m=2,3\) satisfy the same final bound directly. Hence
\[
\boxed{S_m\le(5/2)^m\,m^{m-2}\quad(m\ge2).}
\tag{8.3}
\]
The factor \(m^{m-2}\) is exactly the number of labeled spanning trees. This shows that the raw projection-partition count is no worse than a \(2.5^m\) multiple of the tree count.

This raw count alone was not the temporal tree inequality. The required profile-preserving bounded-multiplicity assignment is now proved in Section 10 and the companion port-injection theorem; it gives the sharper \\(C_{\\rm time}=2\\) for the exact coefficient, not the stronger Penrose \\(\\tau(G_F)\\) majorant.

The numerical consequence is useful. If the weighted assignment can be made with \(C_{\rm time}\le2.5\), then the proposed Kotecký–Preiss condition (6.6) is satisfied because
\[
2(2.5)\kappa_H
<5(0.022695)=0.113475<1/8.
\tag{8.4}
\]
Thus a temporal tree inequality with constant at most \(2.5\) would be sufficient for the present local activity margin. The exact weighted assignment and its compatibility with the support-overlap graph remain OPEN.


## 9. Weighted projection-to-tree structural reduction (2026-11-13)

The next combinatorial step is recorded in
research/theorems/PF_I16_WEIGHTED_PROJECTION_TREE_ASSIGNMENT_OPEN_2026_11_13.md.
Every surviving centered Pi+Q projection term is a linear interval forest whose intervals cover every adjacent temporal gap. If two path components have overlapping time hulls, split an edge (a,b) of one component at a vertex c of the other lying strictly between a and b, replacing (a,b) by (a,c),(c,b). This merges components without a cycle and preserves the number of Q intervals crossing every temporal gap. Iteration completes the forest to a labeled spanning tree with exactly the same temporal cut profile and therefore exactly the same exponential semigroup weight.

The multiplicity issue is now resolved for the exact coefficient: the all-orders port-completion injection proves \\(a_m(c)\\le2^mN_m(c)\\), hence \\(C_{\\rm time}=2\\). The finite verifier now checks the decoder and parent-tree recovery through \\(m=9\\). The stronger assignment with the Penrose majorant \\(\\tau(G_F)\\) is not proved and is unnecessary for the exact cumulant coefficient. The remaining KP gate concerns the joint space-time/support polymer summation, not this profile multiplicity.


## 10. Follow-up — temporal projection multiplicity and reference cumulant bound closed (2026-11-13)

The weighted projection-to-tree assignment previously identified as a missing combinatorial input is now proved by the all-orders port-completion injection:
- every increasing rooted interval-overlap tree completes to a labeled tree with exactly the same temporal cut profile;
- the connector set is determined by the completed tree's directed degrees;
- incoming/outgoing port decorations decode the original forest and its parent tree;
- each completed tree has at most \(2^m\) decorated preimages.

Thus \(C_{\rm time}=2\), and the previously proposed numerical condition is satisfied:
\[
2C_{\rm time}\kappa_H=4\kappa_H<0.09078<1/8.
\]
See [the updated projection/tree proof and verifier](PF_I16_WEIGHTED_PROJECTION_TREE_ASSIGNMENT_OPEN_2026_11_13.md) and [the finite-order audit](../verification/verify_pf_i16_projection_tree_profiles.py).

**The quantum connected-resolvent/tree theorem (5.1) remains OPEN.** The temporal reference-process inequality (6.4), exact disconnected-support cancellation, and the per-tree time integral (6.5) are now established, and the numeric KP activity condition (6.6) is satisfied. What remains open is the rigorous joint space-time/support polymer organization, uniform-in-volume convergence of (6.3), and the resulting marked two-cut and higher-cut connected tree estimates for the actual conjugated rotor Hamiltonian.
