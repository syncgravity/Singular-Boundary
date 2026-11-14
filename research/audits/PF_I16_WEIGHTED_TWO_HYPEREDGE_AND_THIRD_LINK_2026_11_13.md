# PF-I16 weighted two-hyperedge estimate and third-link attachment test

**Date:** 2026-11-13  
**Status:** exact interpolation structure and finite three-link regressions; weighted estimate OPEN  
**Parent:** \`PF_I16_TWO_HYPEREDGE_CONNECTED_LOG_INTERPOLATION_2026_11_13.md\`

## 1. What the weighted estimate must actually say

For two links, write
\[
F_\lambda=\mathsf D(M_1[1+\lambda(M_2-1)]),\qquad
Q_\lambda=(\partial_\lambda F_\lambda)F_\lambda^{-1}.
\]
The candidate Feynman–Kac estimate is not a pointwise bound on \(Q_\lambda\). It is a bound after the time integral and row-order normalization:
\[
\boxed{
\left|\frac1{r!}\int_{[0,T]^r}
[z_{[r]}]Q_\lambda(\mathbf t)\,d\mathbf t\right|
\le T\,C^r\,\mathfrak W(H_1,H_2)
}
\tag{W2?}
\]
or, more robustly when interpolation cancellations are needed,
\[
\boxed{
\left|\frac1{r!}\int_{[0,T]^r}\int_0^1
[z_{[r]}]Q_\lambda(\mathbf t)\,d\lambda\,d\mathbf t\right|
\le T\,C^r\,\mathfrak W(H_1,H_2).
}
\tag{W2}
\]
Here \(\mathfrak W\) must be an explicit sum of connected row-spanning-tree temporal weights, with exactly one maximum-tree decay charged to each connected component; the constants must be stable under summing link supports with \(\sum_e|I_e|\le8r\). The second version is the safer target: it allows cancellation across the activity parameter, which is not controlled by a bound on \(|Q_\lambda|\) at each \(\lambda\).

For ordered times \(t_1<\cdots<t_r\), a maximum-tree factor is \(e^{-\Delta(t_r-t_1)}\), whose ordered-simplex integral is at most \(T\Delta^{-(r-1)}\). Thus a pointwise \(C^r r!\) tree estimate would be compatible with (W2) *if* the connected-tree multiplicity and spatial support sum were already controlled. It is not yet shown that \(Q_\lambda\) admits such a tree representation without expanding local moment objects into absolute LS terms.

### Explicit candidate tree norm

Let \(G(H_1,H_2)\) be the graph on \([r]\) whose edges join rows lying together in \(H_1\) or together in \(H_2\). If the hyperedges overlap and cover all rows, \(G\) is connected. Define the integrated tree norm
\[
\mathcal T_{\Delta}(H_1,H_2;T)
=\frac1{r!}\int_{[0,T]^r}
\sum_{T_0\in\mathcal T(G)}
\prod_{\{i,j\}\in T_0}e^{-\Delta|t_i-t_j|}
\,d\mathbf t.
\]
For each fixed spanning tree, root it and integrate leaves successively; each leaf integral is at most \(2/\Delta\), while the root contributes \(T\). Hence
\[
\mathcal T_{\Delta}
\le \frac{|\mathcal T(G)|}{r!}\,T(2/\Delta)^{r-1}
\le \frac{r^{r-2}}{r!}\,T(2/\Delta)^{r-1}
\le T C_\Delta^r.
\]
Each tree product is also bounded pointwise by the single span factor
\(e^{-\Delta(\max_i t_i-\min_i t_i)}\). Thus this explicit tree norm has the desired Feynman–Kac order growth after \(1/r!\) normalization. The unresolved theorem is the domination of the unexpanded activity-integrated projected-log coefficient by \(C^r\) times this norm. Establishing that domination—not integrating the proposed tree norm—is the outstanding two-hyperedge estimate.

## 2. Why the inverse cannot be bounded in isolation

The formal inverse is
\[
F_\lambda^{-1}=\sum_{k=0}^{r}(-1)^k(F_\lambda-1)^k
\]
in the nilpotent row algebra. Taking absolute coefficient norms term-by-term loses the global logarithmic cancellation and creates ordered set decompositions with factorial growth. Therefore the proof cannot estimate \(\partial_\lambda F_\lambda\) and \(F_\lambda^{-1}\) separately in a naive coefficient \(\ell^1\) norm.

The only viable target here is a *joint* connected-log estimate for the unexpanded coefficient of \(Q_\lambda\), or its activity-integrated version. Any estimate that first replaces \(F_\lambda^{-1}\) by the absolute geometric series is disallowed by the degree-eight cancellation witness.

## 3. Three-hyperedge activation identity

For a third link with complete moment object \(M_3\), introduce independent whole-link Bernoulli activities \(a,b\):
\[
F_{a,b}=\mathsf D\big(M_1[1+a(M_2-1)][1+b(M_3-1)]\big).
\]
The exact derivatives are
\[
\partial_a\log F=F_aF^{-1},\qquad
\partial_b\log F=F_bF^{-1},
\]
and the mixed derivative is
\[
\boxed{
\partial_a\partial_b\log F
=F_{ab}F^{-1}-F_aF_bF^{-2}.
}
\tag{M3}
\]
Consequently,
\[
\begin{aligned}
[z_{[r]}]\log F_{1,1}
={}&[z_{[r]}]\log F_{0,0}\\
&+\int_0^1[z_{[r]}]\partial_a\log F_{a,0}\,da\\
&+\int_0^1[z_{[r]}]\partial_b\log F_{1,b}\,db.
\end{aligned}
\tag{T3}
\]
This is the sequential two-hyperedge attachment: activate link 2, then attach link 3 to the already activated object. The rectangular mixed-derivative identity is
\[
\begin{aligned}
&[z_{[r]}](\log F_{1,1}-\log F_{1,0}
-\log F_{0,1}+\log F_{0,0})\\
&\qquad=\int_0^1\!\!\int_0^1
[z_{[r]}](F_{ab}F^{-1}-F_aF_bF^{-2})\,da\,db.
\end{aligned}
\tag{R3}
\]
The common activity switch is used for every row and time on each hyperedge. Nonzero means remain in the full local moment objects.

The mixed derivative is the exact diagnostic for whether the two activation increments interact through the global row logarithm. It is not generally zero merely because the third link touches one row: if the first two links already connect all rows, changing one row's moments can change the full connected cumulant. This is why "third link must touch two rows" is not a valid general rule.

## 4. Third-link tests

The executable \`research/experiments/pf_i16_three_hyperedge_attachment.py\` checks:
- arbitrary third-link overlap size \(q=1,\ldots,r\), for \(r=3,\ldots,6\), with nonzero means and within-link dependence;
- sequential activation telescoping;
- the exact mixed logarithmic derivative (M3) and its double activity integral;
- a one-row third-link attachment, which can modulate an already connected two-link row cumulant.

These are exact finite squarefree-algebra checks, implemented with floating-point coefficients for regression convenience. They do not establish any temporal decay or factorial absorption.

## 5. Present status of the weighted estimate

**Established:** the exact two-link interpolation, the normalized time-integrated identity, the three-link sequential activation and mixed derivative, and finite arbitrary-overlap regressions.

**Open:** (W2), including the connected-tree temporal majorant, the \(C^r\) normalized growth, and stability under spatial/support summation. The third-link mixed derivative contains a subtraction \(F_aF_bF^{-2}\); bounding its two terms separately would erase the desired logarithmic cancellation. This is the first explicit algebraic location where the multi-link cancellation must be retained.

No P0–P5 gate is promoted.
