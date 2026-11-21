# PF-I16 — Group-cut covariance for multi-time super-rows

**Date:** 2026-11-15  
**Status:** Group-cut covariance estimate ESTABLISHED under the uniform one-link SU(2) heat-kernel gap hypothesis. All-orders support-labelled cumulant tree extraction remains OPEN.  
**Scope:** One stationary temporal link path and bounded observables carried by finite sets of original row-time ports. This is not a Yang–Mills mass-gap result and promotes no P0–P5 gate.

## 1. Input estimate

Assume the one-link stationary path has the compact SU(2) heat-kernel transition density and the refinement-uniform lower gap \(\Delta_h\ge\Delta_0>0\). The bridge-Doeblin argument in PF_I16_COMPACT_GROUP_BRIDGE_DOEBLIN_SUBJECTIVE_HGR_2026_11_15.md supplies a function \(\psi(d)\le C_0e^{-\Delta_0d}\), for \(d>0\), such that for any two distinct observed times \(s,t\), and every finite subfamily \(\mathcal H\) of the other observations,
\[
\rho_{\max}(X_s,X_t\mid\mathcal H)\le\psi(|s-t|).
\tag{1.1}
\]
The bound is uniform in the conditioned endpoint values. Set \(w(0)=1\) and \(w(d)=C_0e^{-\Delta_0d}\) for \(d>0\), enlarging \(C_0\) if necessary so that \(w(d)\ge\psi(d)\).

The conditional, or “subjective,” quantifier in (1.1) is essential. Unconditional semigroup contraction cannot replace it; the endpoint-conditioned CTMC obstruction is recorded in the companion bridge audit.

## 2. Group-cut covariance corollary

Let \(F_1,\ldots,F_r\) be bounded observables on this one link path. Each \(F_i\) is measurable with respect to the finite set of its original temporal ports \(S_i\); repeated times are allowed and are counted with multiplicity in the estimates below. For disjoint nonempty row-index sets \(A,B\subseteq[r]\), put
\[
U_A=\prod_{i\in A}F_i,\qquad
U_B=\prod_{j\in B}F_j.
\]
Then
\[
\boxed{
|\operatorname{Cov}(U_A,U_B)|
\le C_*\left(\prod_{i\in A\cup B}\|F_i\|_\infty\right)
\sum_{i\in A,j\in B}
\sum_{s\in S_i,t\in S_j}
e^{-\Delta_0|s-t|}.
}
\tag{2.1}
\]
Here \(C_*\) depends only on the uniform heat-kernel gap and normalization, not on the number of ports, their interlacing pattern, or the row partition.

**Proof.** If the two unions of port times are disjoint, \(U_A\) and \(U_B\) are arbitrary square-integrable functionals of the two corresponding time vectors. The N-against-M subjective-HGR tensorization estimate gives
\[
|\operatorname{Cov}(U_A,U_B)|
\le C_0\|U_A-\mathbb EU_A\|_2
\|U_B-\mathbb EU_B\|_2
\sum_{s\in S_A,t\in S_B}e^{-\Delta_0|s-t|}.
\]
Use \(\|U_A-\mathbb EU_A\|_2\le2\prod_{i\in A}\|F_i\|_\infty\) and the analogous bound for \(B\). Expanding the port sets as labelled unions gives (2.1), with multiplicity only enlarging the right-hand side. If the two unions share a time, the sum in (2.1) contains at least one zero-distance term. The elementary bound \(|\operatorname{Cov}(U_A,U_B)|\le2\|U_A\|_\infty\|U_B\|_\infty\) proves (2.1) after taking \(C_*\ge2\). \(\square\)

This is stronger than a pairwise row covariance estimate: it controls the covariance across **every bipartition of the row labels**, with the full cross-port temporal profile retained.

## 3. What this does not yet prove

The target is the support-labelled tree estimate
\[
|\kappa(F_1,\ldots,F_r)|
\le C^r\prod_i\|F_i\|_\infty
\sum_{T\in\mathcal T_r}
\prod_{\{i,j\}\in T}
\left(\sum_{s\in S_i,t\in S_j}
e^{-\Delta_0|s-t|}\right).
\tag{3.1}
\]
Equation (2.1) is a cut-factorization estimate for products on the two sides of any row partition. It is **not**, by itself, a proof of (3.1): the cumulant is a Möbius combination over all set partitions, and a single cut covariance bound does not automatically supply a product of \(r-1\) independently chosen row-pair bonds. A valid passage must track how the cut errors compose and prove that the selected bonds form a connected spanning graph; simply multiplying arbitrary cut sums can select a disconnected multigraph.

This distinction matters for the Féray weighted-dependency-graph route. Proposition 5.2 of *Weighted dependency graphs* (arXiv:1605.03836) reduces verification to cumulants of products over connected components of an induced graph; Proposition 5.11 then propagates an already-established weighted dependency graph to bounded-degree monomials. Neither proposition turns (2.1) into the base cumulant bound for arbitrary path-functional super-rows. Using either as if it did would be circular. The Markov-chain Boolean-cumulant identity in Section 10 of that paper handles ordered one-time insertions; a general multi-time block insertion requires an additional argument.

## 4. Precise next lemma

A sufficient next result is a conditional projection-tree theorem for a finite family of port variables with the subjective coefficients (1.1):

For bounded \(F_i=F_i((X_s)_{s\in S_i})\), construct an explicit expansion of \(\kappa(F_1,\ldots,F_r)\) into terms indexed by connected graphs on the original row labels, where each edge \(\{i,j\}\) contributes one factor from the full cross-port profile
\[
W_{ij}=\sum_{s\in S_i,t\in S_j}e^{-\Delta_0|s-t|},
\]
and the total absolute coefficient of all terms is at most \(C^r\). The proof must:
1. allow arbitrary interlacing and repeated temporal ports;
2. use the endpoint-uniform subjective estimate, not unconditional \(L^2\) contraction;
3. preserve the row labels when a port-level projection is assigned to an edge;
4. establish connectedness of the selected row graph, not merely one crossing edge for each cut;
5. keep the coefficient exponential in \(r\), uniformly in the number of ports per super-row once the plaquette incidence bound is imposed.

If this lemma is proved, the existing four-dimensional port budget (four ports per face, at most six original face ports per link, total at most \(4r\)) and the Bell(6) conditional partition overhead can be combined with it without introducing a superexponential local incidence loss. Until then, the recursive multi-row support-tree closure remains OPEN.

## 5. Disposition

- Uniform compact SU(2) bridge minorization, conditional HGR, and arbitrary two-block covariance: **ESTABLISHED under \(\Delta_h\ge\Delta_0\)**.
- Covariance across every bipartition of products of multi-time super-rows, with labelled cross-port bonds: **ESTABLISHED**, equation (2.1).
- Conditional projection-tree expansion converting those cut estimates into a connected row tree with \(C^r\) total coefficient: **OPEN**.
- Recursive multi-row support-labelled cumulant tree: **OPEN**.
- Marked-root spatial summation, quantum connected-resolvent/KP convergence, interacting-vacuum Poincaré inequality, scale-setting along the physical bare-coupling trajectory, and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
