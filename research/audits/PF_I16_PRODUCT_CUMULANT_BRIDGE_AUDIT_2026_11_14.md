# PF-I16 product-cumulant bridge audit

**Review date:** 2026-11-14  
**Scope:** check whether the link-factorized row variables in Section 16 of the joint space-time gate encode cumulants of the intended product insertions. This is an algebraic scope audit, not a new cumulant bound. The source review below checks prior work to avoid repeating its calculations.

## Finding

For
\[
A_i=\prod_{e\in X_i} f_{i,e}(U_e(t_i)),
\qquad
Y_i(z_i)=\prod_{e\in X_i}(1+z_i f_{i,e}(U_e(t_i))),
\]
the factorization of joint moments of \(Y_i\) over independent links is exact. But
\[
Y_i'(0)=\sum_{e\in X_i}f_{i,e}(U_e(t_i)),
\]
not \(A_i\). Thus the square-free coefficient in the row variables \(z_i\) naturally describes cumulants of sums of link observables. It does not directly give the product-insertion cumulant used by the PF-I16 expansion.

## Exact two-link check

Let \(U_1,U_2\) be independent symmetric Rademacher variables, and use two identical insertion rows with \(X_1=X_2=\{1,2\}\) and \(f_{i,e}(U_e)=U_e\). The target products are \(A_1=A_2=U_1U_2\), and
\[
\operatorname{Cov}(A_1,A_2)=1.
\]
For the auxiliary row variables, one link has moment polynomial \(1+z_1z_2\), so the two-link Boolean-lattice factor is
\[
P_{\{1,2\}}=(1+z_1z_2)^2.
\]
Its \(z_1z_2\) coefficient is \(2\), agreeing with
\(\operatorname{Cov}(U_1+U_2,U_1+U_2)=2\), not with the product covariance \(1\). This is verified by [verify_pf_i16_product_cumulant_bridge.py](../verification/verify_pf_i16_product_cumulant_bridge.py).

## Exact top-degree extraction

Let \(d_i=|X_i|\). The same row polynomial has top-degree coefficient
\[
[s_i^{d_i}]\prod_{e\in X_i}(1+s_i f_{i,e})=A_i.
\]
By multilinearity,
\[
\kappa(A_1,\ldots,A_r)
=[s_1^{d_1}\cdots s_r^{d_r}]
\kappa(Y_1(s_1),\ldots,Y_r(s_r)).
\]
The raw joint moments of these row polynomials still factor exactly over independent links. The full family of Boolean-lattice ratios reconstructs every raw moment by Möbius inversion:
\[
u_\Delta(\mathbf s)=\prod_{\gamma\subseteq\Delta}P_\gamma(\mathbf s).
\]
With \(P_\varnothing=1\), the moment-cumulant polynomial is exactly
\[
\kappa(Y_1(s_1),\ldots,Y_r(s_r))
=[x_1\cdots x_r]\log\!\left(
\sum_{\Delta\subseteq[r]}
\left[\prod_{\gamma\subseteq\Delta}P_\gamma(\mathbf s)\right]
\prod_{i\in\Delta}x_i
\right).
\]
Thus it is the ratio \(P_{[r]}-1\) **alone**, not the full family of ratios, whose higher-degree coefficients need not be the cumulant coefficients. In the first Rademacher example, the full polynomial covariance is
\[
\operatorname{Cov}(Y_1(s_1),Y_2(s_2))
=2s_1s_2+s_1^2s_2^2,
\]
and its top-degree coefficient is the target product covariance \(1\), while its square-free coefficient is \(2\).

The symmetric nonzero-mean choice \(f_e=1+U_e\) is not a counterexample: there, the top coefficient of the two-row ratio happens to equal the product covariance. A valid asymmetric counterexample takes independent symmetric Rademacher links \(U,V\), with both row supports \(\{1,2\}\), and sets
\[
f_{1,1}(U)=f_{2,1}(U)=-1-U,\quad
f_{1,2}(V)=-1-V,\quad f_{2,2}(V)=1.
\]
Then \(A_1=(-1-U)(-1-V)\), \(A_2=-1-U\), and \(\operatorname{Cov}(A_1,A_2)=-1\). The row-polynomial means are \((1-s)^2\) and \(1-t^2\); their covariance is
\[
\operatorname{Cov}(Y_1(s),Y_2(t))=st+st^2-s^2t-s^2t^2.
\]
Dividing by the product of means gives \(P_{\{1,2\}}-1\), whose \(s^2t^2\) coefficient is \(1\), not \(-1\). Multiplying by the two singleton means reconstructs the covariance polynomial, as the Möbius formula requires. The verifier checks the shortcut discrepancy and the valid top-degree coefficient of the full covariance.

## Prior-source check

The preserved [PF-I16 continuation transcript](../../sources/originals/session-2026-11-11/Branch%20%C2%B7%20Branch%20%C2%B7%20Continue%20PF116%20Objective%20(1).md) already develops the fourth-order recursion, the 36-term pair-partition organization, exact cancellation for independent decompositions, and cut interpolation. It also records a space-time contiguous-block factorization estimate and leaves the all-orders classical cumulant-tree conversion open. Those computations were not repeated here; this audit narrows the question to the algebraic relation between the row ratios and product cumulants.

The older [full-Euclidean-measure cumulant record](../../sources/historical/raw/Archive/R3_full_measure_cumulant_2026_10_26.zip/__nested__/R3_full_measure_cumulant_2026_10_26/FORMAL_THEOREM.md) concerns a finite-regulator Gibbs measure. Its model and scope differ from the PF-I16 Hamiltonian ground-state expansion, so it does not close the open all-orders gate.

## Remaining structural and quantitative obligation

The multilinear extraction and Möbius reconstruction are exact, but neither supplies a quantitative bound. Recovering the cumulant uses an outer square-free selector and a logarithmic connected expansion built from the full family of link-factorized ratios; existing one-link estimates do not yet bound this combination with coefficient-uniform temporal weights or summable all-orders growth. The joint space-time/support tree and quantum convergence gates remain **OPEN**.

**Status:** the product-cumulant algebraic bridge is exact when the full family of ratios is retained. The unresolved obligation is quantitative: prove a summable all-orders, temporally weighted bound for that reconstructed connected expansion. This does not close or refute the target theorem.
