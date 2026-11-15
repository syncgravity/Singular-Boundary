# PF-I16: simultaneous temporal-cut interpolation

**Date:** 2026-11-14  
**Status:** exact full-span extraction established; mixed-derivative coefficient bound open  
**Scope:** finite-regulator row cumulants. No P0–P5 gate is promoted.

## 1. Ordered temporal cuts

Order the row times as
\[
t_{(1)}\le\cdots\le t_{(r)},\qquad
g_j=t_{(j+1)}-t_{(j)},\quad j=1,\ldots,r-1.
\]
Let \(L_j\) and \(R_j\) be the rows on the left and right of the \(j\)-th cut. For a nonempty row set \(B\), define
\[
C(B)=\{j:B\cap L_j\ne\varnothing,\ B\cap R_j\ne\varnothing\}.
\]
If \(j\in C(B)\), then
\[
\operatorname{span}(B)\ge g_j.
\]

For each link \(e\), let \(\kappa_e(B)\) be its local joint cumulant on the incident rows in \(B\). Define the formal cut-interpolated local moments
\[
m_{e,\boldsymbol\lambda}(S)
=
\sum_{\pi\in\Pi(S\cap I_e)}
\prod_{B\in\pi}
\left[
\kappa_e(B)\prod_{j\in C(B)}\lambda_j
\right],
\qquad \boldsymbol\lambda\in[0,1]^{r-1}.
\]
The empty-set moment is one. For rows outside \(I_e\), the link contributes the neutral factor one. At \(\boldsymbol\lambda=\mathbf1\), this is exactly the ordinary local moment by moment-cumulant inversion.

Independence between links gives the row-product moment functional
\[
m_{\boldsymbol\lambda}(S)=\prod_e m_{e,\boldsymbol\lambda}(S).
\]
Define its formal full cumulant by
\[
K(\boldsymbol\lambda)
=
\sum_{\rho\in\Pi([r])}
(|\rho|-1)!(-1)^{|\rho|-1}
\prod_{D\in\rho}m_{\boldsymbol\lambda}(D).
\]
Then \(K(\mathbf1)=\kappa(A_1,\ldots,A_r)\).

## 2. Exact vanishing on every cut face

Fix a cut \(j\) and set \(\lambda_j=0\). In the local moment sum, every partition containing a block crossing that cut vanishes. Every surviving partition consists entirely of blocks contained in \(L_j\) or entirely in \(R_j\). The partition sum therefore factors:
\[
m_{e,\boldsymbol\lambda}(S)
=
m_{e,\boldsymbol\lambda}(S\cap L_j)\,
m_{e,\boldsymbol\lambda}(S\cap R_j).
\]
Multiplying over independent links preserves this factorization:
\[
m_{\boldsymbol\lambda}(S)
=
m_{\boldsymbol\lambda}(S\cap L_j)\,
m_{\boldsymbol\lambda}(S\cap R_j).
\]
This is precisely the moment functional of two independent row families on the two sides of the cut. Since both sides are nonempty, its full \(r\)-point cumulant vanishes:
\[
K(\lambda_1,\ldots,\lambda_{j-1},0,\lambda_{j+1},\ldots,\lambda_{r-1})=0.
\]
Thus the polynomial \(K\) is divisible by every \(\lambda_j\), and hence by their product.

Applying the fundamental theorem of calculus successively in all cut variables gives the exact identity
\[
\boxed{
\kappa(A_1,\ldots,A_r)
=
\int_{[0,1]^{r-1}}
\partial_{\lambda_1}\cdots\partial_{\lambda_{r-1}}
K(\boldsymbol\lambda)\,d\boldsymbol\lambda.
}
\]
There are no omitted boundary terms: every face with at least one \(\lambda_j=0\) has \(K=0\).

## 3. Full temporal-span factor in every differentiated summand

Expand the mixed derivative by the ordinary product rule, retaining the local moment-cumulant sums. Each derivative \(\partial_{\lambda_j}\) must land on at least one local block factor whose row set crosses cut \(j\); otherwise that summand's derivative is zero. Consequently, every nonzero differentiated summand contains, among its local cumulant factors, at least one block crossing each temporal cut.

For every such selected block \(B_j\),
\[
|\kappa_e(B_j)|
\le a_e(B_j)e^{-\Delta\operatorname{span}(B_j)}
\le a_e(B_j)e^{-\Delta g_j}.
\]
If one block is selected by several cut derivatives, its single span contains all those gaps. Multiplying the selected decay factors therefore yields
\[
\boxed{
\text{decay factor of each nonzero mixed-derivative summand}
\ \le\
e^{-\Delta\sum_{j=1}^{r-1}g_j}
=
e^{-\Delta(\max_i t_i-\min_i t_i)}.
}
\]
This recovers the full temporal span at rate \(\Delta\), rather than the weaker largest-gap rate obtained from a single cut.

## 4. Exact progress versus the missing estimate

**Established**
1. A simultaneous \(r-1\)-parameter cut interpolation exists at the level of formal local cumulants.
2. The full row-product cumulant vanishes on every coordinate face \(\lambda_j=0\).
3. The full cumulant is exactly the integral of its mixed derivative over the unit cube.
4. Every nonzero differentiated summand has the full-span exponential factor \(e^{-\Delta(\max t-\min t)}\).

**Not established**
The mixed derivative still expands into many marked local partitions and row partitions. The number and coefficient sizes of those terms may be superfactorial. The full-span factor alone does not bound their sum. In particular, this construction does **not** prove
\[
|\kappa(A_1,\ldots,A_r)|
\le C^r(r-1)!\,e^{-\Delta(\max t-\min t)}
\]
or the normalized integrated W2-tree estimate.

The next required result is a cancellation-preserving bound on the mixed derivative of \(K\), uniform in \(r\), the number of links, and all supports satisfying the row-incidence constraint \(\sum_e|I_e|\le 8r\). No P3 status is promoted.
