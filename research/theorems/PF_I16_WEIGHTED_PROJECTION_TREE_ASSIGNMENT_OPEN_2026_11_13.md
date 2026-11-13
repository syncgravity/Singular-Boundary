# PF-I16 — Weighted projection-to-tree assignment: all-orders port-completion injection

**Date:** 2026-11-13  
**Status (follow-up 2026-11-13):** the all-orders weighted projection-to-tree assignment is CLOSED by the exact port-completion injection in Section 7, with coefficientwise bound \(A_m(c)\le 2^mN_m(c)\) and \(C_{\rm time}=2\). The quantum time-ordered connected-resolvent/tree theorem remains OPEN.

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

## 5. Resolution of the exact coefficient-profile gate

The previous raw estimate \(S_m\le (5/2)^m m^{m-2}\) did not prove the profile inequality because it counted terms before collecting equal Q-forests. The all-orders port-completion injection in Section 7 now resolves that exact coefficient-profile problem:
\[
A_m(c)\le2^mN_m(c),\qquad C_{\rm time}=2.
\]
Consequently the previously proposed local-activity arithmetic is satisfied:
\[
2C_{\rm time}\kappa_H=4\kappa_H<0.09078<1/8.
\]

**Current status:** exact interval-forest completion, all-orders coefficientwise profile domination, and the reference temporal projection-tree inequality are established. The quantum connected-resolvent/tree theorem and the uniform all-orders activity/convergence claim remain OPEN.


## 6. Ursell coefficient on the interval-overlap graph

There is a sharper way to organize the remaining coefficient. Fix a surviving interval forest F and let its path components be C_1,...,C_k. Form the interval-overlap graph G_F on these components: two vertices are adjacent exactly when their temporal hulls overlap. An original moment-cumulant partition can group several components into one block only when their hulls are pairwise disjoint and ordered. Thus the coefficient of F is the hard-core Ursell coefficient
\[
\alpha_m(F)=\sum_{\substack{\pi\text{ partition of }V(G_F)\\\text{each block independent in }G_F}}(-1)^{|\pi|-1}(|\pi|-1)!
=\sum_{\substack{H\subseteq E(G_F)\\(V(G_F),H)\text{ connected}}}(-1)^{|H|}.
\]
The repulsive-graph tree inequality (Penrose tree-graph bound) therefore gives
\[
|\alpha_m(F)|\le\tau(G_F),
\]
where \(\tau(G_F)\) is the number of spanning trees of the component-overlap graph. This explains the small coefficients seen in the finite expansion and replaces the raw Stirling count by a connected-graph quantity.

A stronger, but unnecessary, alternative would be to prove the profile inequality with the Penrose majorant \(\tau(G_F)\) in place of the exact coefficient \(|\alpha_m(F)|\). That stronger assignment is not established here. It is not needed: the interval-graph perfect-elimination formula in Section 7.1 counts the exact coefficient \(|\alpha_m(F)|\) directly by increasing rooted spanning trees, and Section 7.2–7.5 injects precisely those objects into decorated labeled trees with the same cut profile. The finite verifier audits this exact coefficient count.


## 7. All-orders port-completion injection (2026-11-13)

We now prove the required coefficientwise profile inequality for every order.

### 7.1 Increasing rooted-tree representation of the coefficient

Write the components of \(F\) as increasing paths
\[
C_j=(v_{j,1}<\cdots<v_{j,s_j}),\qquad s_j\ge2,
\]
with hulls \(I_j=[\ell_j,r_j]\). Relabel them so that
\[
r_1<r_2<\cdots<r_k.
\]
The interval-overlap graph \(G_F\) has a perfect elimination ordering in this order: every later neighbor of \(C_j\) contains \(r_j\), hence the later neighbors form a clique. Put
\[
d_j=\#\{p>j:I_p\cap I_j\ne\varnothing\}.
\]
Connectedness of \(G_F\) implies \(d_j\ge1\) for \(j<k\). Chordal elimination gives
\[
\chi_{G_F}(q)=q\prod_{j=1}^{k-1}(q-d_j),
\qquad
|\chi'_{G_F}(0)|=\prod_{j=1}^{k-1}d_j.
\]
Choosing one later neighbor \(p(j)>j\) for every \(j<k\) gives an increasing rooted spanning tree of \(G_F\), rooted at \(k\). Every such choice is a tree because the parent index strictly increases and the only vertex with no later neighbor is \(k\). Conversely every increasing rooted spanning tree gives exactly these choices. Therefore
\[
|\alpha_m(F)|=|\chi'_{G_F}(0)|
=\#\{\text{increasing rooted spanning trees of }G_F\}.
\tag{7.1}
\]

### 7.2 Canonical completion

Fix one such parent map \(p(j)\). Since \(I_j\) and \(I_{p(j)}\) overlap and \(r_j<r_{p(j)}\), at least one endpoint of \(C_j\) lies strictly inside \(I_{p(j)}\). Choose the least such vertex:
\[
c_j=\min\bigl(C_j\cap(\ell_{p(j)},r_{p(j)})\bigr).
\]
There are consecutive vertices \(a_j<b_j\) of \(C_{p(j)}\) with
\[
a_j<c_j<b_j.
\]
Thus \((a_j,b_j)\) is an original path edge of the parent component.

Process the non-root components in decreasing order of \(r_j\), so every parent has already been inserted. For each original path edge \(e=(a,b)\), maintain its current increasing chain \(\Gamma_e\), initially the single edge \((a,b)\). Earlier insertions may subdivide this chain but never change its endpoints or monotonicity.

When processing \(C_j\), find the unique current chain edge \((x,y)\subset\Gamma_{(a_j,b_j)}\) with
\[
x<c_j<y.
\]
Replace
\[
(x,y)\longmapsto(x,c_j),(c_j,y)
\]
and add all path edges of \(C_j\). The two sides of the removed edge are joined through the connected path \(C_j\), so the new graph is again a tree. At each step, splitting an edge at an interior vertex preserves the number of edges crossing every temporal cut; adding the path edges of \(C_j\) adds exactly the cut profile contributed by that component. Hence the final labeled tree \(T\) satisfies
\[
n_q(T)=n_q(F)\qquad(1\le q<m).
\tag{7.2}
\]

### 7.3 Port decoration

At the insertion of connector \(c_j\), mark the incoming and outgoing edges
\[
e^-_{c_j}=(x,c_j),\qquad e^+_{c_j}=(c_j,y).
\]
If a later insertion subdivides either marked edge, transport that port to the new edge that remains incident to \(c_j\). At completion, each connector has exactly one marked incoming and one marked outgoing port.

Orient all edges of \(T\) from smaller to larger labels. For a vertex \(v\), let \(d^-(v),d^+(v)\) be its indegree and outdegree. Splitting a current edge preserves the indegree of its lower endpoint and the outdegree of its upper endpoint. The only degree increments occur at the newly inserted connector, which receives one incoming and one outgoing edge. Since every component of \(F\) is a path, ordinary vertices have degree pairs
\[
(0,1),\quad(1,0),\quad(1,1),
\]
whereas connectors have degree pairs
\[
(1,2),\quad(2,1),\quad(2,2).
\]
Consequently the connector set is determined by \(T\) alone:
\[
\boxed{\mathcal C(T)=
\{v:d^-(v)+d^+(v)\ge3\}.}
\tag{7.3}
\]

### 7.4 Decoding and injectivity

Construct a transition graph whose vertices are the edges of \(T\). For each connector \(c\), join its marked incoming port edge to its marked outgoing port edge by a transition labelled \(c\).

Inductively through the completion algorithm, each original edge of \(F\) is represented by one increasing chain in \(T\). Every insertion subdivides exactly one edge of exactly one such chain and adds the transition pairing the two new subedges. Port transport preserves transitions at the endpoints of previously subdivided edges. Thus the transition graph is a disjoint union of paths, one path for each original edge of \(F\); an unsplit original edge is an isolated vertex of the transition graph.

Replace each transition path by the single edge joining the endpoints of its corresponding chain, and retain isolated edge-vertices. This reconstructs exactly \(F\).

For a connector \(c_j\), its transition path is the subdivided chain of the original edge \((a_j,b_j)\) in its parent component. Hence the component of reconstructed \(F\) containing that edge is exactly \(C_{p(j)}\). This recovers every parent choice. The unique component containing no connector is the root component. Therefore \((F,p)\) is uniquely recoverable from the completed tree together with its port decoration:
\[
\boxed{(F,p)\longmapsto(T,\pi)\text{ is injective}.}
\tag{7.4}
\]

### 7.5 Fiber bound and coefficientwise domination

The connector set is determined by \(T\). At a connector there are at most two choices of incoming port and two choices of outgoing port, so there are at most four possible port pairs. If \(F\) has \(k\) components, it has exactly \(k-1\) connectors. Since every component has at least two vertices,
\[
k\le\lfloor m/2\rfloor.
\]
For each fixed labeled tree \(T\), the number of possible port decorations is therefore at most
\[
4^{k-1}\le4^{m/2}=2^m.
\]
Combining this fiber bound with (7.1), injectivity, and profile preservation (7.2), we obtain for every profile \(c\):
\[
\boxed{
A_m(c)=
\sum_{F:n(F)=1+c}|\alpha_m(F)|
\le2^m N_m(c).
}
\tag{7.5}
\]
Thus the all-orders temporal projection assignment is established with
\[
\boxed{C_{\rm time}=2.}
\]

Multiplying (7.5) by the common profile weight
\[
\exp\!\left[-\Delta_0\sum_{q=1}^{m-1}(1+c_q)(t_{q+1}-t_q)\right]
\]
and summing over profiles gives the corresponding weighted temporal tree inequality without any loss in the semigroup exponent.

### 7.6 Verification and exact scope

The updated verifier enumerates the complete projection expansion through \(m=9\), constructs every increasing rooted parent map, completes it, and decodes the forest and parent map from the port decoration. It checks profile preservation and injectivity. The audited pair counts are
\[
1,1,3,9,39,189,1107,7281
\]
for \(m=2,\ldots,9\), respectively. This finite audit corroborates the all-orders proof; it is not the proof itself.

With the previously recorded \(\kappa_H<0.022695\), the proposed numerical activity condition is now
\[
2C_{\rm time}\kappa_H=4\kappa_H
<0.09078<\frac18.
\]
This closes the weighted projection multiplicity subgate and verifies that stated numerical condition.

**It does not close the quantum connected-resolvent/tree theorem.** The uniform Feynman–Kac/ground-energy linked-cluster expansion, its full time-ordered reduced-resolvent control, and the application of an actual quantum Kotecký–Preiss theorem remain open. The PF-I16 interacting-vacuum and physical continuum mass-gap obligations are unchanged.


### 7.7 Reference-process temporal cumulant consequence

Let \(A_1,\ldots,A_m\) be centered bounded multiplication observables of the stationary product SU(2) reference process, and let \(P_t=\Pi+Q_t\) with
\[
\|Q_t\|_{2\to2}\le e^{-\Delta_0t}.
\]
The projection expansion, the semigroup contraction on each Q interval, and (7.5) give the all-orders temporal tree bound
\[
\boxed{
\left|\kappa_0(A_1(t_1),\ldots,A_m(t_m))\right|
\le
2^m\left(\prod_{i=1}^m\|A_i\|_\infty\right)
\sum_{T\in\mathcal T_m}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
}
\tag{7.6}
\]
This is uniform in the number of link rotors. It is a theorem for the independent reference process, not yet for the perturbed interacting ground state.

For a fixed labeled tree \(T\), order the times and write \(g_q=t_{q+1}-t_q\). Its exponent is
\[
\sum_{\{i,j\}\in T}|t_i-t_j|
=\sum_{q=1}^{m-1}n_q(T)g_q,
\qquad n_q(T)\ge1.
\]
Consequently its ordered time integral is bounded by
\[
\int_{0\le t_1\le\cdots\le t_m\le\mathcal T}
e^{-\Delta_0\sum_q n_q(T)g_q}\,d\mathbf t
\le \mathcal T\,\Delta_0^{-(m-1)}.
\]
Using the symmetry of the cumulant and the \(1/m!\) normalization in the Feynman–Kac logarithm, this yields the fixed-order estimate
\[
\boxed{
\frac1{m!\mathcal T}
\int_{[0,\mathcal T]^m}
\left|\kappa_0(A_1(t_1),\ldots,A_m(t_m))\right|\,d\mathbf t
\le
2^m m^{m-2}\Delta_0^{-(m-1)}
\prod_i\|A_i\|_\infty.
}
\tag{7.7}
\]
This controls the reference-process time integrals at every fixed order. The remaining task is to combine them with spatial connected-support summation and the marked cut insertions in a uniform-in-volume, all-orders linked-cluster theorem. The factor \(m^{m-2}\) in (7.7) is not by itself an all-orders convergence estimate.
