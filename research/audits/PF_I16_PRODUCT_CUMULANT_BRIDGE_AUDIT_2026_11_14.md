# PF-I16 product-cumulant bridge audit

**Review date:** 2026-11-14  
**Scope:** check whether the link-factorized row variables in Section 16 of the joint space-time gate encode cumulants of the intended product insertions. This is an algebraic scope audit, not a new cumulant bound.

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

## Consequence for the proposed route

Equations (16.1)–(16.3) remain valid for their auxiliary variables, as does the one-link estimate for the stated one-link coefficients. What is missing is a justified passage from this auxiliary row factorization to the cumulant of the products \(A_i\). The row-incidence constraint alone does not provide that passage.

A product-compatible formulation can index one formal variable per factor slot \((i,e)\). The product cumulant is then represented by the Leonov–Shiryaev sum over slot partitions whose join with the partition into insertion rows is connected. To improve on the superfactorial absolute majorant, that connected slot-partition sum must be reorganized while preserving cancellation and temporal decay. No such reorganization or all-orders bound is established here.

**Status:** the Section 16 cancellation-preserving product-cumulant route is incomplete at this bridge. The joint space-time/support tree and the associated quantum convergence gate remain **OPEN**. This finding does not refute the target theorem or the exact auxiliary factorization; it narrows what the latter currently proves.
