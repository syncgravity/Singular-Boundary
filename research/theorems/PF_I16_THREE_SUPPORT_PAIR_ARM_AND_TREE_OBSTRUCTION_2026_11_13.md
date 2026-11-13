# PF-I16 — Three-support nested-resolvent estimate and the remaining tree obstruction

**Date:** 2026-11-13  
**Program:** canonical source-native coupled-\(\mathbb Z^5\), intrinsic \(2+2\), PF-I16 interacting-vacuum route.  
**Status:** a conditional, volume-independent *pair-arm* bound for the exact nested third-order resolvent term is derived from the corrected two-point theorem. A genuine three-support connected tree bound is **not** obtained: the undifferentiated inner resolvent creates a non-decaying local-amplitude term. The missing estimate and a precise test configuration are identified below.

This report does not import the older straight-strip R3 constants as PF-I16 theorems. It uses only the new PF-I16 reversible-flow result, its stated finite-graph incidence assumptions, and explicit local residual norms.

## 1. Inputs and notation

Let \(M=\prod_{e\in E}\mathrm{SU}(2)_e\) be a finite accepted-link graph, with reversible dressed measure
\[
d\nu_\Phi=Z_\Phi^{-1}e^{2\Phi}dU,
\]
positive generator \(L_\Phi\), centered inverse \(G=L_\Phi^{-1}Q\), and link-overlap graph of maximum degree \(24\). Write
\[
K_\mu(e,g)=e^{-\mu d(e,g)},\qquad \mu=\log25.
\]
The corrected derivative-flow estimate is
\[
\|\mathsf D_eGf\|_\infty
\le\lambda^{-1}\sum_gK_\mu(e,g)\|\mathsf D_gf\|_\infty.
\tag{1.1}
\]
The local oscillation estimate is
\[
\operatorname{osc}(P_tf)
\le26\pi e^{-\lambda t}\sum_g\|\mathsf D_gf\|_\infty.
\tag{1.2}
\]
For centered \(f\), integrating (1.2) gives
\[
\|Gf\|_\infty\le\operatorname{osc}(Gf)
\le\frac{26\pi}{\lambda}
\sum_g\|\mathsf D_gf\|_\infty.
\tag{1.3}
\]
All three statements are conditional on the corrected face-pullback and finite-product Kato comparison inputs in the PF-I16 derivative-flow record.

For centered local residuals \(r_i\), let \(S_i=\operatorname{supp}r_i\),
\[
A_{i,e}=\|\mathsf D_er_i\|_\infty,\quad
M_i=\sum_{e\in S_i}A_{i,e},\quad
B_i=\|r_i\|_\infty.
\]
The exact third-order coefficient under consideration is
\[
E_{123}
=-\sum_{\sigma\in S_3}
\nu_\Phi\!\left[
r_{\sigma(1)}G\bigl(r_{\sigma(2)}G r_{\sigma(3)}\bigr)
\right].
\tag{1.4}
\]
The centering projection inside the inner product is implicit because \(G=L_\Phi^{-1}Q\).

## 2. A quasilocal extension of the two-point identity

The Dirichlet identity gives, for centered smooth \(f,h\),
\[
\nu_\Phi(fGh)
=\nu_\Phi\!\left[
\Gamma_\Phi(Gf,Gh)
\right].
\tag{2.1}
\]
Using (1.1) twice and the product carré-du-champ bound,
\[
|\nu_\Phi(fGh)|
\le\lambda^{-2}
\sum_{a,c}
\|\mathsf D_af\|_\infty
\|\mathsf D_ch\|_\infty
P_2(a,c),
\tag{2.2}
\]
where
\[
P_2(a,c)=\sum_eK_\mu(a,e)K_\mu(e,c).
\]
The sum over \(c\) may include every link, not just a finite support, provided
\(\sum_c\|\mathsf D_ch\|_\infty<\infty\). On a finite regulator this is automatic; the estimates below give a bound uniform in its size.

The shell estimate already used in the two-point theorem gives, with
\[
\nu=\frac12\log\frac{25}{23},
\qquad C_1=
1+\frac{24e^{-(\mu-\nu)}}{1-23e^{-(\mu-\nu)}}<25.511,
\]
the pointwise bound
\[
P_2(a,c)\le C_1e^{-\nu d(a,c)}.
\tag{2.3}
\]

A second convolution is also controlled, but with a smaller exponent. Put
\[
\gamma=\frac{\nu}{2}
=\frac14\log\frac{25}{23}>0,
\]
and
\[
C_2=1+\frac{24e^{-(\mu-\gamma)}}{1-23e^{-(\mu-\gamma)}}<18.264.
\]
Since \(0<\gamma<\nu\), the triangle inequality gives
\[
\begin{aligned}
\sum_c e^{-\nu d(a,c)}e^{-\mu d(c,b)}
&\le e^{-\gamma d(a,b)}
\sum_c e^{-(\nu-\gamma)d(a,c)}
e^{-(\mu-\gamma)d(c,b)}\\
&\le C_2e^{-\gamma d(a,b)}.
\end{aligned}
\]
The last step drops the first factor, which is at most one, and uses
\(\mu-\gamma>\log23\) to sum the second factor over graph shells. Hence
\[
P_3(a,b):=\sum_{c,e}
K_\mu(a,e)K_\mu(e,c)K_\mu(c,b)
\le C_1C_2e^{-\gamma d(a,b)},
\tag{2.4}
\]
with \(C_1C_2<465.933\). This is the three-kernel estimate needed below; it does not assert preservation of the original exponent \(\mu\).

## 3. Nested term: exact derivative decomposition

Fix an ordering \((i,j,k)\) and set
\[
u_k=Gr_k,\qquad h_{jk}=Q(r_ju_k).
\]
Then
\[
\mathsf D_ch_{jk}
=(\mathsf D_cr_j)u_k+r_j\mathsf D_cu_k.
\tag{3.1}
\]
The two terms have different localization behavior.

From (1.3),
\[
\|u_k\|_\infty\le\frac{26\pi}{\lambda}M_k.
\tag{3.2}
\]
From (1.1),
\[
\|\mathsf D_cu_k\|_\infty
\le\frac1\lambda\sum_{b\in S_k}
K_\mu(c,b)A_{k,b}.
\tag{3.3}
\]
Therefore
\[
\|\mathsf D_ch_{jk}\|_\infty
\le
\mathbf1_{c\in S_j}\frac{26\pi}{\lambda}M_k A_{j,c}
+\frac{B_j}{\lambda}
\sum_{b\in S_k}K_\mu(c,b)A_{k,b}.
\tag{3.4}
\]

Apply (2.2) to \(f=r_i\), \(h=h_{jk}\). Inserting (3.4), then (2.3) and (2.4), yields the following bound.

## 4. Theorem — conditional three-support pair-arm estimate

For every ordering \((i,j,k)\),
\[
\boxed{
\begin{aligned}
&\left|\nu_\Phi\!\left[
r_iGQ(r_jGr_k)
\right]\right|\\
&\quad\le
\frac{26\pi C_1}{\lambda^3}
M_iM_jM_k\,e^{-\nu d(S_i,S_j)}
+
\frac{C_1C_2}{\lambda^3}
B_jM_iM_k\,e^{-\gamma d(S_i,S_k)}.
\end{aligned}}
\tag{4.1}
\]
Here \(d(S,T)=\min\{d(a,b):a\in S,b\in T\}\). The constants are independent of the number of links, conditional on (1.1)–(1.2).

Summing the six orderings gives
\[
\boxed{
\begin{aligned}
|E_{123}|
\le\frac1{\lambda^3}\Bigg[
&52\pi C_1M_1M_2M_3
\sum_{i<j}e^{-\nu d(S_i,S_j)}\\
&+2C_1C_2
\sum_{j=1}^3B_jM_iM_k
e^{-\gamma d(S_i,S_k)}
\Bigg],
\end{aligned}}
\tag{4.2}
\]
where in the second sum \(\{i,k\}=\{1,2,3\}\setminus\{j\}\).

Equation (4.2) is a genuine volume-independent estimate for the six-term coefficient, but it is **not** a connected tree estimate.

## 5. Why the pair-arm estimate does not imply a tree bound

The obstruction is visible in the first term of (3.1). It contains the undifferentiated amplitude \(u_k\) multiplied by the local derivative \(\mathsf D_cr_j\). The global oscillation bound (3.2) controls that amplitude but carries no information about the distance from \(S_j\) to \(S_k\).

Take \(S_1=S_2\) and let \(d(S_1,S_3)=R\to\infty\). The \((i,j,k)=(1,2,3)\) contribution to (4.1) contains
\[
\frac{26\pi C_1}{\lambda^3}M_1M_2M_3,
\]
with no factor tending to zero as \(R\to\infty\). The second term decays in \(d(S_1,S_3)\), but it does not control the first. Thus the derived majorant cannot imply any bound of the form
\[
C\,e^{-\gamma_T\,\ell_{\rm MST}(S_1,S_2,S_3)}
\]
with \(\gamma_T>0\), where \(\ell_{\rm MST}\) is the length of a minimum spanning tree on the three supports.

This is a limitation of the estimate, **not** a counterexample showing that the actual third-order coefficient fails to decay. The six terms in (1.4) may contain connected cancellations that are lost when absolute values are taken term by term.

## 6. Exact missing input for a connected tree estimate

The product rule identifies the missing analytic object. To replace the global \(B_k\)-bound in the first term of (3.4), we need a *local amplitude estimate* for \(Gr_k\) near a support disjoint from \(S_k\), in a norm strong enough to multiply it by the other resolvent gradient.

A sufficient form would be a conditional \(L^4\) estimate of the type
\[
\left\|Gr_k-\mathbb E_{\nu_\Phi}
[Gr_k\mid\mathcal F_{S_j^c}]
\right\|_{L^4(\nu_\Phi)}
\le C_{\rm amp}
e^{-\eta d(S_j,S_k)}
\mathcal M_k,
\tag{6.1}
\]
together with:
1. a regulator-uniform conditional Poincaré inequality for the actual PF-I16 dressed measure on the variables in \(S_j\);
2. a conditional-centering or boundary-term estimate for \(r_j\), since global centering \(\nu_\Phi(r_j)=0\) does not imply \(\mathbb E[r_j\mid\mathcal F_{S_j^c}]=0\);
3. a local \(L^4\) bound on the relevant gradients \( \mathsf D_{S_j}Gr_i\), so Hölder can combine the two separated resolvent responses;
4. an exact six-permutation connected-cancellation identity retaining the interaction-history labels, rather than deleting outputs with disconnected minimal spin support.

The last point is essential. The source record contains a nonzero disconnected-output channel in the actual three-face logarithmic score at source multiplicities \((1,2,1)\), with coefficient
\(-1381/1261578240\). Thus physical connected source history cannot be replaced by a requirement that the reconstructed spin-network support itself be connected. The separate PF-I16 single-face recurrence also shows a nonzero third-order return to the fundamental spin channel. A proof cannot assume that electric denominators necessarily increase with insertion order.

The earlier straight-strip R3 conditional-amplitude and weighted-\(L^4\) results are useful design precedents, but they are not automatically PF-I16 estimates: their reference measures, geometry, and operator normalizations differ. An equivalence certificate or a fresh proof for \(d\nu_\Phi\) is required.

## 7. Research verdict and next step

**Derived:** the three-kernel convolution bound (2.4), the exact product-rule decomposition (3.1), and the uniform pair-arm estimate (4.1) for each nested ordering, hence (4.2) for the six-term coefficient.

**Still open:** the local amplitude/conditional \(L^4\) estimate for the PF-I16 dressed measure, conditional centering control, and the connected cancellation identity. Therefore the requested three-support connected tree estimate has not yet been proved.

The next mathematically decisive step is to derive (or disprove) (6.1) for the actual PF-I16 measure, beginning with a single residual support and conditioning on its complement. In parallel, the six-permutation coefficient should be rewritten in a history-labelled cumulant form before any absolute-value estimate is applied. These are the two missing bridges; further pairwise resolvent bounds alone will not close them.
