# PF-I16 nilpotent row-projection resummation candidate

**Date:** 2026-11-13  
**Status:** exact algebraic representation; analytic estimate OPEN  
**Scope:** finite product observables built from independent link-path processes

## 1. Why this route is worth testing

The link-coloured Leonov–Shiryaev expansion is exact, but taking absolute values of its individual connected partition summands loses the cancellations needed for an exponential-in-order bound. The degree-eight common-Rademacher witness is decisive: the signed eighth cumulant is only \(-272\), while a restricted family already contains \(105^6\) positive connected summands of size one. A successful argument must keep the local partition family summed before taking absolute values.

The proposed change of representation is to use a squarefree (nilpotent) generating algebra for all elementary link slots, then impose the row-product constraint as a linear diagonal projection, and take the global logarithm only after that projection.

## 2. Exact finite-dimensional identity

Write
\[
A_i=\prod_{e\in X_i}Y_{i,e},\qquad
I_e=\{i:e\in X_i\},\qquad
E_i=\{e:i\in I_e\}.
\]
Assume one factor per row-link slot and independence of the link path processes across distinct links. Let
\[
\mathcal A=\mathbb C[x_{i,e}:(i,e)\text{ a slot}]/(x_{i,e}^2),
\qquad
\mathcal Z=\mathbb C[z_1,\ldots,z_r]/(z_i^2).
\]
For each link define its *whole local moment object*
\[
M_e(x_e)=\mathbb E_e\prod_{i\in I_e}(1+x_{i,e}Y_{i,e})
=\sum_{B\subseteq I_e}m_e(B)x_{B,e},
\quad m_e(B)=\mathbb E_e\prod_{i\in B}Y_{i,e}.
\]
Independence gives the full slot-moment polynomial
\[
M(x)=\prod_e M_e(x_e).
\]

Define a linear row-diagonal projection \(\mathsf D:\mathcal A\to\mathcal Z\) on slot monomials. If \(J\) is a set of slots, write \(J_i=\{e:(i,e)\in J\}\). Set
\[
\mathsf D(x_J)=
\begin{cases}
z_S,&J_i=\varnothing\text{ or }J_i=E_i\text{ for every }i,
\quad S=\{i:J_i=E_i\},\\
0,&\text{otherwise.}
\end{cases}
\]
Then, exactly,
\[
F(z):=\mathsf D\!\left(\prod_eM_e\right)
=\sum_{S\subseteq[r]}\mathbb E\!\left[\prod_{i\in S}A_i\right]z_S,
\qquad
\boxed{\kappa(A_1,\ldots,A_r)=[z_{[r]}]\log F(z).}
\tag{1}
\]
The first identity follows because the coefficient of the complete slot monomial for rows in \(S\) is the expectation of the product of all their link factors; the other rows contribute the empty monomial. The second is the standard squarefree moment-to-cumulant logarithm.

This is a *single-object-per-link* formulation: each \(M_e\) contains all subsets of that link's row incidence at once. It is algebraically equivalent to the LS partition expansion, not a new probabilistic assumption.

## 3. Cumulant coordinates and where temporal decay lives

Within the squarefree algebra,
\[
M_e=\exp K_e,\qquad
K_e(x_e)=\sum_{\varnothing\ne B\subseteq I_e}
\kappa_e(Y_{i,e}:i\in B)x_{B,e}.
\]
Thus the link partition family is encoded by one exponential. For \(|B|\ge2\), the one-link temporal cumulant estimate supplies
\[
|[x_{B,e}]K_e|
\le (2e)^{|B|}|B|!\,
e^{-\Delta_0(\max_{i\in B}t_i-\min_{i\in B}t_i)}
\prod_{i\in B}\|f_{i,e}\|_\infty.
\]
Singleton coefficients are means and carry no temporal decay; they must be separated or absorbed by a controlled centering/tilting step. One cannot silently assign them a decaying edge.

The logarithm in (1) retains global row-connectedness *after* the diagonal projection. This is the crucial order: local link objects first, row constraint second, global connected cumulant last. The projection is linear, not multiplicative; therefore the standard identity \(\log\prod_e M_e=\sum_e\log M_e\) cannot be applied after \(\mathsf D\). That nonmultiplicativity is also the principal analytic difficulty.

## 4. Why the degree-eight incidence budget is relevant—but insufficient

The accepted face/row incidence gives
\[
\sum_e|I_e|=\sum_i|X_i|\le8r.
\]
Hence there are at most \(8r\) slot variables and the squarefree slot algebra has dimension at most \(2^{8r}\). This is a genuinely exponential combinatorial envelope, unlike the Bell-number/connected-partition enumeration in the termwise LS majorant.

However, this dimension count alone does **not** bound the coefficient norm of \(\log\mathsf D(\prod_eM_e)\). In particular:
- the diagonal projection is not an algebra homomorphism;
- a single link may have large \(|I_e|\), so high-order one-link cumulants must be controlled without paying a second factorial;
- singleton means can create nondecaying contributions;
- taking absolute values before the global logarithm reinstates the forbidden loss of cancellations.

The target is a weighted connected norm, not merely an unweighted coefficient count.

## 5. Candidate analytic route and the correct Feynman–Kac target

A plausible route is a **nilpotent hyperedge polymer / BKAR forest estimate** on the projected moment functional:

1. Keep each \(M_e\), or equivalently its cumulant exponent \(K_e\), as one local hyperedge object. Do not expand its set-partition exponential into separate LS terms.
2. Introduce a row-coupling interpolation for the diagonal constraint. Apply a multivariate forest formula (BKAR or a hypergraph analogue) to \([z_{[r]}]\log F\). The forest derivatives should select connected row blocks while differentiating each link object as a whole.
3. Prove a tree-graph bound in which each selected non-singleton link block contributes its one-link maximum-tree temporal weight. The union of these link trees is connected; select one row-spanning tree from the union. Since all extra exponential factors are at most one, their product is bounded by that **single maximum spanning-tree** weight. The challenge is to sum all choices *before* taking absolute values and to avoid an extra Cayley factor.
4. Use \(\sum_e|I_e|\le8r\) to bound the number of active slot/link incidences charged by the forest derivatives. The desired pointwise form, if obtainable, is
\[
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le C^r\prod_i\|A_i\|_{\rm slot}
\max_{T\in\mathcal T_r}\prod_{\{i,j\}\in T}
e^{-\Delta_*|t_i-t_j|}.
\tag{2a}
\]
Note **there is no extra \(r!\) in (2a)**. That distinction matters for Feynman–Kac summability.

The more flexible target is a direct **time-integrated cumulant coefficient**:
\[
\left|\frac1{r!}\int_{[0,\mathcal T]^r}
\kappa(A(t_1),\ldots,A(t_r))\,d\mathbf t\right|
\le \mathcal T C^r,
\tag{2b}
\]
after the spatial/support sums appropriate to the interaction have also been performed. Equivalently, the absolute value of the integrated cumulant before the Feynman–Kac normalization is at most \(\mathcal T C^r r!\). This is the precise normalization-compatible statement to target if cancellations in time integration are needed.

For ordered times \(t_1<\cdots<t_r\), the maximum spanning tree is the adjacent-time path and
\[
\max_{T\in\mathcal T_r}\prod_{\{i,j\}\in T}e^{-\Delta|t_i-t_j|}
=e^{-\Delta(t_r-t_1)}.
\]
Its ordered-simplex integral is
\[
\int_{0<t_1<\cdots<t_r<\mathcal T}
e^{-\Delta(t_r-t_1)}\,d\mathbf t
=\int_0^{\mathcal T}ds\int_0^{\mathcal T-s}
e^{-\Delta L}\frac{L^{r-2}}{(r-2)!}\,dL
\le \mathcal T\Delta^{-(r-1)}
\quad(r\ge2).
\]
Thus (2a) implies (2b), up to the exponential factor \(\Delta_*^{-(r-1)}\), because the cube divided by \(r!\) is the ordered simplex for a symmetric cumulant integrand. Crucially, a weaker pointwise estimate \(C^r r!\) times the maximum-tree weight does **not** by itself imply (2b): integrating the pointwise factorial against the maximum-tree kernel leaves an additional factorial. The temporal port-injection result \(C_{\rm time}=2\) is useful but does not establish (2a) or (2b). The expansion convention (cube with \(1/r!\), or ordered simplex with its permutation sum) must match the Hamiltonian/Feynman–Kac expansion exactly.
## 6. Immediate falsification tests / next lemmas

- Re-derive the two-row/two-shared-link, three-row path, and four-row path identities directly from (1), and compare with the LS hypergraph formula.
- Reproduce the eight-link Rademacher cancellation witness. The projected logarithm must return \(-272\), not the sum of absolute LS terms.
- Test one high-degree shared link \(|I_e|=r\), with centered bounded observables and the exact one-link temporal cumulant estimate. This is the stress test for whether the squarefree dimension bound conceals an \(r!\) from the link object itself.
- Prove a two-link gluing lemma: when two independent link families meet a common row, the projected logarithm's connected coefficient should be expressible as a finite interpolation integral with one bridge factor. Then iterate by a tree, with a uniform cost per incidence.
- Establish a norm estimate for the row-diagonal projection under the interpolation; plain \(\ell^1\) coefficient norm is unlikely to retain temporal decay.

## 7. Status and proof boundary

**Exact:** (1), the slot-moment factorization, the row-diagonal projection, and the moment-to-cumulant logarithm.

**Candidate only:** a nilpotent hyperedge polymer/BKAR reorganization that bounds the projected logarithm while preserving a single maximum-tree temporal factor.

**Open:** the weighted connected-log estimate, high-degree link control, singleton-mean treatment, \(C^r r!\) or Feynman–Kac-integrable growth, actual quantum Feynman–Kac/ground-energy convergence, and transfer to the physical interacting vacuum.

This construction does not close the P2/P3 analytic gate, establish the actual interacting-vacuum Poincaré inequality, or imply a Yang–Mills continuum mass gap.
