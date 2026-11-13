# PF-I16 — Multi-cut forest interpolation: exact reduction and remaining connected-tree lemma

**Date:** 2026-11-13  
**Status:** exact multivariate factorization reduction; mixed-derivative tree estimate remains OPEN. This is the next gate after the conditional third- and fourth-order tree bounds.

## 1. Why one cut is not an all-orders argument

For \(n\) terminal supports, let \(\ell_{\rm MST}\) be the minimum spanning-tree length and \(L\) its longest edge. A single cut across that edge gives
\[
L\ge\frac{\ell_{\rm MST}}{n-1}.
\]
The cut-layer argument used at fourth order then gives, at best,
\[
e^{-\gamma L/2}
\le e^{-\gamma\ell_{\rm MST}/[2(n-1)]}.
\]
Thus the single-cut exponent is
\[
\eta_n^{\rm one\ cut}=\frac{\gamma}{2(n-1)},
\qquad
\gamma=\frac14\log\frac{25}{23}.
\tag{1.1}
\]
It decreases to zero with \(n\). This is a geometric limitation of the one-longest-edge argument, not a proof that an all-orders estimate is impossible. A uniform activity radius requires a forest/multi-cut argument that retains a decay factor for each connecting tree edge.

## 2. Exact multi-cut interpolation

First merge labels whose support sets overlap; the remaining terminal support clusters are disjoint. Choose a tree \(T\) on the terminal clusters. For each tree edge \(a\in E(T)\), choose a link-coordinate cut \(A_a|A_a^c\) separating the two terminal groups obtained by deleting \(a\).

For an accepted face \(f\), let \(C_f\subseteq E(T)\) be the set of tree cuts crossed by that face. Define the multivariate interpolation
\[
\Phi_{\mathbf s}
=\sum_f\left(\prod_{a\in C_f}s_a\right)s_f(H_f),
\qquad
\mathbf s=(s_a)_{a\in E(T)}\in[0,1]^{n-1}.
\tag{2.1}
\]
If \(C_f=\varnothing\), the product is one. At \(\mathbf s=\mathbf1\), this is the original \(\Phi\).

If any one parameter \(s_a=0\), every face crossing the corresponding cut is removed. The remaining face terms lie wholly on one side or the other, so the dressed measure and generator factorize across \(A_a|A_a^c\). Since that cut separates the source labels,
\[
E_I(\mathbf s)=0
\quad\text{whenever any }s_a=0,
\qquad |I|=n.
\tag{2.2}
\]
This is exact finite-product factorization; it does not assume that disjoint supports on the original connected graph are independent.

For a smooth function vanishing on every coordinate hyperplane, repeated one-variable fundamental theorems of calculus give
\[
\boxed{
E_I(\mathbf1)
=\int_{[0,1]^{n-1}}
\left(\prod_{a\in E(T)}\partial_{s_a}\right)
E_I(\mathbf s)\,d\mathbf s.
}
\tag{2.3}
\]
Thus only the full mixed derivative over the tree edges contributes. The lower-face terms vanish because of (2.2).

The first derivative has the exact cut-response form
\[
\partial_{s_a}E_s(\mathbf t)
=-\frac{\pi_{\mathbf s}
[g_{\mathbf s}(\mathbf t)\Gamma(W_a(\mathbf s),g_{\mathbf s}(\mathbf t))]}
{\pi_{\mathbf s}(g_{\mathbf s}(\mathbf t)^2)},
\qquad
W_a(\mathbf s)=2\partial_{s_a}\Phi_{\mathbf s}.
\tag{2.4}
\]
Each \(W_a\) is a sum of local cross-face terms. Its first link derivative has the same per-link bound as the one-cut insertion. Higher mixed derivatives of \(W_a\), however, also see faces crossing several tree cuts.

## 3. The missing multi-cut connected-response lemma

The open analytic task is to control
\[
\left(\prod_{a\in E(T)}\partial_{s_a}\right)E_I(\mathbf s)
\]
without replacing the full dependence by one global mixing error. Differentiating (2.4) produces:
- derivatives of the normalized eigenfunction and its reduced-resolvent coefficients;
- derivatives of the measure and its centering terms;
- derivatives of the denominator \(\pi_{\mathbf s}(g_{\mathbf s}^2)\);
- mixed derivatives of \(W_a(\mathbf s)\) for faces crossing multiple cuts.

A successful estimate must retain one spatial influence factor for every tree edge. The desired schematic form is
\[
\left|
\left(\prod_{a\in E(T)}\partial_{s_a}\right)E_I(\mathbf s)
\right|
\le C^n
\sum_{\mathcal T\text{ connecting the terminals}}
\prod_{\{p,q\}\in\mathcal T}w(S_p,S_q),
\tag{3.1}
\]
where each \(w\) contains a genuine edgewise spatial decay and \(C\) is controlled uniformly in source volume and with explicit growth in \(n\). The full Dobrushin influence resolvent \((I-\mathsf C)^{-1}\) is a candidate way to retain these individual dependence edges; a single covariance coefficient is not enough.

The face assignment in (2.1) is itself part of the combinatorial audit: a face may cross several tree cuts, so the mixed derivatives of its product coefficient must be counted without losing the edgewise factors or introducing uncontrolled \(2^{|C_f|}\) growth.

## 4. Alternative local-rotor linked-cluster route

The preserved PF116 continuation also records the exact conjugation
\[
e^\Phi L_\Phi e^{-\Phi}=K+\mathcal U_\Phi,\qquad
K=\sum_e a_e(-\Delta_e),
\]
with \(\mathcal U_\Phi=\sum_e U_e\) and \(|\operatorname{supp}U_e|\le25\). The overlap graph of the \(U_e\) terms has the conservative degree bound \(24+24\cdot23=576\). This gives a second route: prove a four-source linked-cluster lemma for the product-rotor Hamiltonian, then extend it to all orders. The local support identity is exact; the required connected-cluster estimate is not yet proved.

The universal accepted-face incidence remains \(d_e\le8\). Do not substitute the sharper two-incidence observation from finite crops as a source-volume theorem. Do not import R3-IR constants without the seven-part equivalence certificate.

## 5. Proof ledger

**Derived exactly:** the product interpolation (2.1); factorization on every coordinate hyperplane (2.2); the multi-variable integral identity (2.3); and the first cut-response identity (2.4).

**Open:** a bound for the full mixed derivative in (2.3) that retains one influence/decay factor per tree edge; controlled counting of faces crossing multiple cuts; uniform-in-\(n\) growth of the resulting constants; connected support-history summability; transfer to the actual interacting Wilson vacuum.

The single-cut order-four theorem remains conditional with exponent \(\eta_4=\frac1{24}\log(25/23)\). Equation (1.1) explains why it cannot, by itself, establish the all-orders activity radius.
