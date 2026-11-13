# PF-I16 — Weighted projection-to-tree assignment: structural reduction and open multiplicity gate

**Date:** 2026-11-13  
**Status:** structural reduction proved at the level of individual surviving projection terms; coefficientwise tree-profile domination checked through order eight; all-orders weighted assignment remains OPEN. No temporal tree constant is certified.

## 1. Ordered-time projection expansion

Let t_1 <= ... <= t_m, g_k=t_{k+1}-t_k, and let A_1,...,A_m be centered bounded multiplication observables for the stationary product reference process. Write P_t=Pi+Q_t, with ||Q_t||_{2 to 2} <= exp(-Delta_0 t).

In a moment belonging to a block B={i_1<...<i_r} of the moment-cumulant formula, expand each semigroup between consecutive members of B as Pi+Q. A choice of Pi cuts the block into consecutive segments. Any segment containing one observable has zero expectation because the observables are centered. Thus every nonzero term is represented by a collection of segments of length at least two. Each segment contributes a path of Q-intervals between consecutive labels in that segment.

After summing the Möbius coefficients over set partitions and collecting identical Q-edge families, write the resulting expansion as a sum over interval forests F with signed coefficients alpha_m(F). Each F is a linear forest on the m labels: each component is a path, and every label belongs to a non-singleton segment.

## 2. Connected interval support and exact tree completion

If some temporal gap g_k is crossed by no Q interval, the Q expansion separates into a left and right family at that gap. The corresponding moment-cumulant Möbius sum factorizes across that separation and its coefficient is zero. Consequently every surviving family F has at least one interval crossing every adjacent temporal gap. Equivalently, the union of its closed time intervals is all of [t_1,t_m].

There is an exact completion operation. Take two distinct path components of F whose time hulls overlap. Since their vertex sets are disjoint, a vertex c of one component lies strictly between two consecutive vertices a<b of the other component. The edge (a,b) is present in that path. Replace it by (a,c) and (c,b). Removing (a,b) splits its path into two pieces; the two new edges attach both pieces to the component containing c. The result is again a forest, with one fewer component and one more edge. It remains acyclic and all vertices remain present.

For every temporal gap g_k, exactly one of (a,b), or the two replacement edges, crosses that gap. Hence this operation preserves the complete gap-crossing profile n_k(F)=#{(a,b) in F: a<=k<b}. Because the interval union of F is connected, the component hull-overlap graph is connected. Repeating the operation therefore produces a spanning tree T(F) on the m labels with n_k(T(F))=n_k(F) for every k.

In particular, the exponential weight of the projection term is exactly the tree weight:
product over (a,b) in F of exp(-Delta_0(t_b-t_a))
equals exp(-Delta_0 sum_k n_k(F)g_k), which equals product over edges (p,q) in T(F) of exp(-Delta_0|t_p-t_q|).

This proves that every surviving projection term has at least one temporal spanning-tree representative with no loss in its semigroup exponent. It does not yet control how many projection terms are assigned to the same tree.

## 3. The remaining weighted multiplicity inequality

For a nonnegative integer profile c=(c_1,...,c_{m-1}), define
a_m(c)=sum over F with n_k(F)=1+c_k for all k of |alpha_m(F)|,
and let N_m(c) be the number of labeled spanning trees T for which the number of edges crossing cut k is 1+c_k for every k.

The exact tree completion above reduces the desired all-orders temporal estimate to the coefficientwise comparison
a_m(c) <= C_time^m N_m(c)
for every m>=2 and every c.

Indeed, multiplying this inequality by exp(-Delta_0 sum_k(1+c_k)g_k) and summing profiles gives the desired temporal tree bound with C_time^m times the sum over all labeled spanning trees. Thus this profile-by-profile inequality, not the unweighted Stirling count alone, is the exact weighted projection-to-tree assignment gate.

## 4. Finite-order coefficient audit

The new verifier research/verification/verify_pf_i16_projection_tree_profiles.py constructs the centered Pi+Q expansion, collects equal interval forests with their signed Mobius coefficients, enumerates labeled trees by Prufer sequences, and compares a_m(c) with N_m(c) profile by profile.

The exact finite enumeration gives:

| m | surviving projection forests | absolute coefficient mass | projection profiles | tree profiles | coefficientwise violations |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 | 0 |
| 3 | 1 | 1 | 1 | 3 | 0 |
| 4 | 3 | 3 | 2 | 13 | 0 |
| 5 | 9 | 9 | 4 | 67 | 0 |
| 6 | 33 | 39 | 9 | 383 | 0 |
| 7 | 135 | 189 | 21 | 2,349 | 0 |
| 8 | 609 | 1,107 | 51 | 15,165 | 0 |

The audited orders satisfy the stronger finite statement a_m(c)<=N_m(c), i.e. C_time=1 at those orders. This is computational evidence only; it is not an all-orders proof.

## 5. Exact open point and consequence for the activity criterion

The previous raw estimate S_m <= (5/2)^m m^(m-2) does not prove the profile inequality: it counts terms before collecting equal Q-forests and does not control profile-specific multiplicity. The tree completion lemma removes the exponent-mismatch issue, but not the matching/multiplicity issue.

The next proof task is an all-orders injection or weighted matching from the absolute projection-forest coefficient mass in each profile class into the labeled trees with the same profile, or a direct proof with C_time<=2.5. If established, the already-recorded local activity bound would imply
2 C_time kappa_H <= 5(0.022695)=0.113475<1/8.

Until this profile inequality is proved, neither C_time=1 nor C_time<=2.5 is certified, and the KP convergence gate remains OPEN.

**Status:** exact interval-forest-to-tree exponent-preserving completion proved; finite coefficientwise profile domination verified for 2<=m<=8; all-orders coefficientwise domination, temporal cumulant tree inequality, and quantum connected-resolvent tree bound remain OPEN.
