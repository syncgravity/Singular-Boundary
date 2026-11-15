# PF-I16 two-hyperedge connected-log interpolation

**Date:** 2026-11-13  
**Status:** exact finite interpolation identity and regression tests; time-integrated multi-link bound OPEN  
**Parent:** \`PF_I16_NILPOTENT_ROW_PROJECTION_RESUMMATION_CANDIDATE_2026_11_13.md\`

## 1. Setup

Take two independent link processes, with incident row sets \(H_1,H_2\subseteq[r]\), and assume \(H_1\cup H_2=[r]\). Dependence among the slots of one link is unrestricted. For \(e=1,2\), retain the complete local squarefree moment object
\[
M_e(x_e)=\sum_{B\subseteq H_e}m_e(B)x_{B,e},\qquad
m_e(B)=\mathbb E_e\prod_{i\in B}Y_{i,e},\quad m_e(\varnothing)=1.
\]
No centering is imposed; in particular, \(m_e(\{i\})\) may be nonzero. Let \(\mathsf D\) be the row-diagonal projection from the parent audit.

Define the one-parameter *whole-hyperedge activity interpolation*
\[
M_{2,\lambda}=1+\lambda(M_2-1),\qquad 0\le\lambda\le1,
\]
and
\[
F_\lambda(z)=\mathsf D\!\left(M_1M_{2,\lambda}\right)
=1+\sum_{\varnothing\ne S\subseteq[r]}
m_1(S\cap H_1)m_2(S\cap H_2)
\lambda^{\mathbf1_{\{S\cap H_2\ne\varnothing\}}}z_S.
\tag{1}
\]
The convention \(m_e(\varnothing)=1\) makes (1) valid for every subset, including rows incident to only one hyperedge. \(F_\lambda\) has constant term one, so it is invertible in the finite squarefree row algebra \(\mathcal Z\).

The interpolation has a genuine probability interpretation: take one Bernoulli switch \(\eta_\lambda\), independent of the entire second-link path, with \(\mathbb P(\eta_\lambda=1)=\lambda\), and replace every slot on that link by \(\eta_\lambda Y_{i,2}\). The *same* switch is used for every row and time on the link. Hence every nonempty joint moment of the second link is multiplied by exactly \(\lambda\), including its singleton means, while its internal dependence structure is retained whenever the link is active. Independent switches per row would instead produce \(\lambda^{|B|}\) and would not give (1).

## 2. Exact interpolation lemma

**Lemma (two-hyperedge projected-log interpolation).** For every finite \(r\), every pair \(H_1,H_2\) covering \([r]\), and arbitrary finite local moments \(m_1,m_2\) (including nonzero means),
\[
\boxed{
[z_{[r]}]\log F_1
=[z_{[r]}]\log F_0+
\int_0^1
[z_{[r]}]\left((\partial_\lambda F_\lambda)F_\lambda^{-1}\right)d\lambda .
}
\tag{2}
\]
If \(H_1\ne[r]\), then \([z_{[r]}]\log F_0=0\), so the integral alone is the full joint row cumulant. If \(H_1=[r]\), the \(F_0\) term is exactly the one-hyperedge cumulant for link 1; the integral is the increment from activating the complete second-link moment object. The formula is symmetric after averaging it with the analogous interpolation that activates link 1 from link 2.

**Proof.** The row algebra is commutative and nilpotent in its augmentation ideal. Since \(F_\lambda(0)=1\), the formal identity
\[
\partial_\lambda\log F_\lambda
=(\partial_\lambda F_\lambda)F_\lambda^{-1}
\]
holds exactly. Integrate from zero to one and extract the full-row coefficient. At \(\lambda=1\), \(F_1=\mathsf D(M_1M_2)\), so the parent row-diagonal identity identifies the coefficient with \(\kappa(A_1,\ldots,A_r)\). At \(\lambda=0\), \(F_0=\mathsf D(M_1)\), which contains no monomial involving any row outside \(H_1\); its full-row logarithmic coefficient is therefore zero unless \(H_1=[r]\). \(\square\)

This is an exact interpolation of the *whole* second-link moment object. It does not center the slots and does not expand either \(M_e\) into link cumulants or LS partition summands. The global inverse/logarithm is left intact, which is where row connectedness remains encoded.

## 3. Connectedness and overlap

If \(H_1\cap H_2=\varnothing\), row-diagonal projection factorizes over the disjoint row sets:
\[
F_1(z)=F^{(1)}(z_{H_1})F^{(2)}(z_{H_2}),
\quad
\log F_1=\log F^{(1)}+\log F^{(2)}.
\]
Thus the full-row coefficient vanishes. If \(H_1\cap H_2\ne\varnothing\), the two projected factors share row variables and the projection no longer factorizes. The full-row coefficient of \(\log F_1\), and its interpolation representation (2), is the connected row contribution. It may of course vanish for special moment choices; connectedness is a structural selection, not a positivity assertion.

For \(r=2\), \(H_1=H_2=\{1,2\}\), write \(\mu_{e,i}=m_e(\{i\})\) and \(q_e=m_e(\{1,2\})\). Then
\[
F_\lambda=1+\lambda a z_1+\lambda b z_2+\lambda c z_1z_2,
\quad
a=\mu_{1,1}\mu_{2,1},\quad
b=\mu_{1,2}\mu_{2,2},\quad c=q_1q_2.
\]
Consequently
\[
[z_1z_2](\partial_\lambda F_\lambda)F_\lambda^{-1}
=c-2\lambda ab,
\]
and integration gives \(c-ab\). Writing \(q_e=c_e+\mu_{e,1}\mu_{e,2}\) yields exactly
\[
\kappa(A_1,A_2)
=c_1c_2+c_1\mu_{2,1}\mu_{2,2}
+\mu_{1,1}\mu_{1,2}c_2,
\tag{G2}
\]
including all nonzero-mean terms. This is the bridge identity already observed in the two-row calculation, now as a derivative of the projected global logarithm.

## 4. Time-integrated form with the Feynman–Kac normalization

Let the local moments depend measurably on \(\mathbf t=(t_1,\ldots,t_r)\), and assume the finite-regulator moments make the expressions integrable on \([0,T]^r\). Applying (2) at each \(\mathbf t\), then Fubini (the interpolation is finite-dimensional), gives the exact identity
\[
\begin{aligned}
\frac1{r!}\int_{[0,T]^r}[z_{[r]}]\log F_1(\mathbf t)\,d\mathbf t
={}&\frac1{r!}\int_{[0,T]^r}[z_{[r]}]\log F_0(\mathbf t)\,d\mathbf t\\
&+\int_0^1\frac1{r!}\int_{[0,T]^r}
[z_{[r]}]\big((\partial_\lambda F_\lambda)F_\lambda^{-1}\big)
\,d\mathbf t\,d\lambda.
\end{aligned}
\tag{3}
\]
Thus the \(1/r!\) normalization is present before any estimate. No pointwise no-factorial claim is made, and no factorial is discarded by interchanging the interpolation and time integrals.

## 5. Regression coverage

The executable \`research/experiments/pf_i16_two_hyperedge_interpolation.py\` tests:
- every overlap size \(q=1,\ldots,r\) for \(r=3,\ldots,7\), with both local means nonzero and nontrivial within-link dependence;
- the exact two-row nonzero-mean G2 formula;
- disjoint hyperedges, where the full connected row coefficient must vanish;
- the logarithmic derivative identity by computing \((\partial_\lambda F_\lambda)F_\lambda^{-1}\) in the squarefree row algebra and integrating its polynomial in \(\lambda\) exactly.

These are exact finite algebra checks (floating-point arithmetic is used only in the regression implementation).

## 6. What this does—and does not—solve

**Established:** the general two-hyperedge interpolation identity (2), its arbitrary-overlap and nonzero-mean form, the connected-log selection, and the normalized time-integrated identity (3).

**Not established:** any bound on the interpolation integrand uniform in \(r\), the time variables, or the number of overlapping links. In particular, \((\partial_\lambda F_\lambda)F_\lambda^{-1}\) can still have large coefficients; the identity alone does not absorb the high-degree one-link factorial. The key open estimate is a bound on the *integrated full-row coefficient of this unexpanded quotient*, with constants compatible with \(C^r r!\) before normalization (or \(C^r\) after normalization), and stable under iterative gluing of several hyperedges.

The interpolation is not the BKAR forest formula. BKAR remains a possible next step for a multi-hyperedge tree organization, but it must act on these whole-object activities and preserve the projected logarithm; standard forest interpolation by itself supplies no required coefficient estimate. No P0–P5 gate is promoted.
