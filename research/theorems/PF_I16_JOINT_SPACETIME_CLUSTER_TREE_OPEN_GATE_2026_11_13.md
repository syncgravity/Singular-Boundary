# PF-I16 — Joint space-time connected-cluster tree bound: next open gate

**Date:** 2026-11-13  
**Status:** the reference-process temporal projection/cumulant sublemma is closed with \(C_{\rm time}=2\). The all-orders quantum linked-cluster theorem is still OPEN. This note isolates the missing joint space-time estimate and audits the activity arithmetic; it does not promote a convergence claim.

## 1. Inputs that are now established

The companion result
\`PF_I16_WEIGHTED_PROJECTION_TREE_ASSIGNMENT_OPEN_2026_11_13.md\`
proves the all-orders profile inequality
\[
A_m(c)\le 2^mN_m(c)
\]
by a profile-preserving port-completion injection. Consequently, for centered bounded multiplication observables of the stationary product-rotor reference process,
\[
\left|\kappa_0(A_1(t_1),\ldots,A_m(t_m))\right|
\le
2^m\prod_i\|A_i\|_\infty
\sum_{T\in\mathcal T_m}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
\tag{1.1}
\]
The cumulant vanishes exactly if the support-overlap graph of the \(A_i\)'s is disconnected. These are separate facts: (1.1) has a sum over unrestricted temporal trees, while spatial disconnectedness is presently only a zero criterion.

For a fixed labeled tree,
\[
\int_{[0,\mathcal T]^m}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}\,d\mathbf t
\le
\mathcal T(2/\Delta_0)^{m-1}.
\]
Thus the already-recorded normalized temporal estimate is
\[
\frac{1}{m!\mathcal T}
\int_{[0,\mathcal T]^m}|\kappa_0|\,d\mathbf t
\le
\frac{2^m m^{m-2}}{m!}
(2/\Delta_0)^{m-1}\prod_i\|A_i\|_\infty.
\tag{1.2}
\]

## 2. Why the separate spatial and temporal tree bounds do not yet close

In the Feynman–Kac expansion, write the local background interaction as
\[
V=\sum_X V_X,
\]
where each \(X\) is a singleton-face or adjacent-face-pair support. The order-\(m\) logarithmic coefficient contains
\[
\frac{1}{m!\mathcal T}
\int_{[0,\mathcal T]^m}
\sum_{X_1,\ldots,X_m}
\kappa_0(V_{X_1}(t_1),\ldots,V_{X_m}(t_m))
\,d\mathbf t.
\tag{2.1}
\]
A nonzero summand requires the support-overlap graph on \(X_1,\ldots,X_m\) to be connected.

A tempting estimate is to majorize this spatial connectedness by a sum over spatial spanning trees and then apply (1.1), which independently sums over temporal spanning trees. This produces two Cayley factors. Even after the single \(1/m!\) normalization in (2.1), the resulting combinatorial growth contains
\[
\frac{m^{m-2}\,m^{m-2}}{m!}.
\tag{2.2}
\]
By Stirling,
\[
\frac{m^{2m-4}}{m!}
\asymp
e^m m^{m-9/2},
\]
up to a fixed multiplicative constant. This is superexponential in \(m\). No fixed small local activity can make this particular majorant summable at all orders.

This is a failure of the *separate-bound strategy*, not a counterexample to the desired cluster theorem. The temporal and spatial connectivity must be organized jointly, or one of the two tree counts must be eliminated by a sharper argument.

## 3. The missing joint space-time lemma

The natural target is a support-sensitive cumulant tree estimate of the form
\[
\boxed{
|\kappa_0(A_1(t_1),\ldots,A_m(t_m))|
\le
C_{\rm st}^{\,m}\prod_i\|A_i\|_\infty
\sum_{T\in\mathcal T_m}
\prod_{\{i,j\}\in T}
b_{ij}(t_i,t_j),
}
\tag{3.1}
\]
where each bond \(b_{ij}\):
- vanishes when the corresponding local supports are disjoint;
- has integrable temporal decay, uniformly in volume;
- is strong enough that its time integral and local-support sum can be estimated on the *same tree*.

A first candidate is
\[
b_{ij}(t_i,t_j)
=
\mathbf1_{\{X_i\cap X_j\ne\varnothing\}}
e^{-\Delta_0|t_i-t_j|}.
\tag{3.2}
\]
Equation (3.2) is now proved for \(m=2,3\) in Section 7. Its extension to \(m\ge4\) is open. The proof must determine whether it holds with \(C_{\rm st}=2\), with a larger explicit constant, or only after replacing the exponential by a weaker influence kernel.

The relevant structure is the product decomposition of the reference path law over links. Each insertion depends on at most eight link paths. A viable proof should exploit that independence before taking absolute values: decompose local insertions into link-coordinate components, express the joint cumulant as a sum of connected coordinate-incidence diagrams, and extract one spanning tree whose edges each correspond to a shared link and carry the associated temporal mixing factor. The tensor/contraction norm used in this step must be controlled by the stated local insertion norm; an uncontrolled \(\ell^1\) Peter–Weyl expansion is not acceptable.

The two- and three-observable cases are now exact (Section 7). The remaining finite-order milestone is the four-observable version needed for the exact third- and fourth-order responses in the two-cut identity, followed by an induction that gives the all-orders bound with explicit \(C_{\rm st}\).

## 4. Activity arithmetic conditional on the joint lemma

The face/pair decomposition gives the per-face background activity
\[
z_f=32b_0+14336\,b_0^2/a_0,
\qquad
\Delta_0=3a_0/4.
\]
At \(b_0/a_0\le1/50000\),
\[
z_f/\Delta_0<8.610\times10^{-4}.
\]
A local interaction term is supported on one face or on two adjacent faces. The closed neighborhood of those at-most-two face endpoints contains at most
\[
2(1+28)=58
\]
faces. Using the conservative incident-activity sum, the dimensionless continuation bound along a shared-support edge is therefore
\[
q_{\rm face}
\le58\,z_f/\Delta_0
<0.049937.
\tag{4.1}
\]

If (3.1) is proved with \(C_{\rm st}=2\), and if the standard rooted-tree summation introduces only the single Cayley/Stirling factor \(e^m\), then the corresponding background continuation candidate is
\[
q_{\rm joint}
\le 2\cdot2\cdot e\cdot q_{\rm face}
<0.543<1.
\tag{4.2}
\]
The two factors of \(2\) in (4.2) are respectively the proposed \(C_{\rm st}\) and the integral
\(\int_{\mathbb R}e^{-\Delta_0|t-s|}dt=2/\Delta_0\).
The single \(e\) is the rooted-tree/Stirling factor. Formula (4.2) is conditional on (3.1) and on the exact rooted-cluster counting; it is not a Kotecký–Preiss verification.

For comparison, the cut-insertion activity from the conjugated local-rotor decomposition obeys
\[
z_{\rm cut}/\Delta_0<1.723\times10^{-3},
\qquad
58z_{\rm cut}/\Delta_0<0.099882.
\]
These are marked-root weights. Their summation over all cut roots must be handled separately from the unmarked background activity.

## 5. Consequences for the proof ledger

The following distinctions are mandatory:

- **Closed:** exact finite-volume two-cut reduced-resolvent identity.
- **Closed:** bounded local face/pair decomposition after conjugation.
- **Closed:** reference-process temporal projection/tree inequality with \(C_{\rm time}=2\).
- **Closed:** finite-order port-injection audit through \(m=9\).
- **Open:** joint support-sensitive space-time cumulant/tree inequality (3.1).
- **Open:** the all-orders Feynman–Kac/ground-energy linked-cluster expansion and its actual KP application.
- **Open:** uniform mixed multi-cut derivative estimate and transfer to the interacting PF-I16 vacuum.
- **Open:** continuum physical mass-gap conclusion.

In particular, the arithmetic statement
\[
2C_{\rm time}\kappa_H<1/8
\]
is not, by itself, a consequence of (1.1)–(1.2). The actual polymer criterion must be derived from the joint space-time expansion with every time integral, support sum, marked root, and combinatorial factor displayed.

## 6. Immediate next calculation

Do not enlarge the local-activity estimates yet. Work at fixed \(m=4\) under the product reference path law. Classify all connected support-overlap graphs on four insertions and derive the support-sensitive cumulant decomposition, retaining the complete coordinate-incidence structure. The desired output is an explicit tree formula with constants, or a concrete counterexample to the proposed bond (3.2). Only after this calculation should the all-orders induction and KP constants be attempted.

**No quantum connected-resolvent/tree theorem or interacting-vacuum gap is claimed in this record.**


## 7. Exact support-sensitive tree bound at order three

The candidate bond (3.2) is now proved for \(m=2,3\), with no loss in the reference gap.

For \(m=2\), if \(S_1\cap S_2=\varnothing\), the two path observables are independent and the covariance is zero. Otherwise, centering and the product semigroup gap give
\[
|\kappa_0(A_1(t_1),A_2(t_2))|
\le e^{-\Delta_0|t_1-t_2|}
\|A_1\|_\infty\|A_2\|_\infty.
\tag{7.1}
\]

For \(m=3\), center the three observables; the cumulant is unchanged. Relabel their times so that \(t_1\le t_2\le t_3\), and put \(u=t_2-t_1\), \(v=t_3-t_2\). The Markov property and centering give
\[
\kappa_0(A_1(t_1),A_2(t_2),A_3(t_3))
=
\langle A_1,Q_u A_2 Q_v A_3\rangle,
\tag{7.2}
\]
where multiplication by \(A_2\) is understood between the two semigroup factors. Therefore
\[
|\kappa_0(A_1(t_1),A_2(t_2),A_3(t_3))|
\le e^{-\Delta_0(u+v)}
\prod_{i=1}^3\|A_i\|_\infty.
\tag{7.3}
\]

If the support-overlap graph is complete, its temporal path edges \(\{1,2\},\{2,3\}\) are available, and (7.3) is exactly the corresponding tree weight. If the graph is a path with middle vertex \(2\), the same is true.

It remains to consider a path whose center is an endpoint in temporal order. Suppose its edges are \(\{1,2\}\) and \(\{1,3\}\), so \(S_2\cap S_3=\varnothing\). Put
\[
R=S_1\cap S_2,\qquad U=S_1\cap S_3.
\]
Then \(R\cap U=\varnothing\). Integrating out link paths outside \(R\cup U\) replaces \(A_1,A_2,A_3\) by conditional expectations \(\bar A_1(R,U),\bar A_2(R),\bar A_3(U)\), without increasing their \(L^2\) norms. The two path families on \(R\) and \(U\) are independent. Since \(\bar A_2,\bar A_3\) are centered, only the component of \(\bar A_1\) centered in both coordinate groups contributes. The product semigroup therefore gives
\[
|\kappa_0(A_1(t_1),A_2(t_2),A_3(t_3))|
\le
e^{-\Delta_0u}e^{-\Delta_0(u+v)}
\prod_i\|A_i\|_\infty.
\tag{7.4}
\]
This is the tree weight on \(\{\{1,2\},\{1,3\}\}\). The case with center \(3\) is symmetric.

Consequently, for centered bounded local observables,
\[
\boxed{
|\kappa_0(A_1(t_1),A_2(t_2),A_3(t_3))|
\le
\prod_i\|A_i\|_\infty
\sum_{T\in\mathcal T(G_{\rm ov})}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|},
}
\tag{7.5}
\]
where \(\mathcal T(G_{\rm ov})\) denotes the spanning trees of the support-overlap graph. If that graph is disconnected, both sides vanish. For noncentered inputs, replacing each input by its centered version gives the same inequality with an additional factor \(2^3\).

Thus the joint support-sensitive space-time tree bound is established at orders two and three. The proof uses only product-path independence and the reference semigroup gap. It does not use the all-orders unrestricted temporal-tree estimate (1.1).

**Still open:** the order-four version. Cyclic support-overlap graphs on four insertions need not contain the temporal path edges, and the order-three articulation argument does not settle their coordinate-incidence contractions. The next calculation is the complete \(m=4\) support-graph classification and its tensorized path-semigroup estimate. No all-orders quantum cluster theorem is claimed.


## 8. Refined route: weighted dependency graphs

A useful external framework is Féray's weighted dependency graphs. Its definition bounds a joint cumulant by
\[
|\kappa(Y_{\alpha_1},\ldots,Y_{\alpha_m})|
\le C_m\,\Psi(B)\,\mathcal M(\widetilde L[B]),
\]
where \(\mathcal M\) is the **maximum spanning-tree product** of the weighted graph induced by the insertion labels. This is a single-tree majorant, not a sum over all spanning trees. Féray's Proposition 5.2 further reduces the weighted-dependency-graph property to quasi-factorization estimates for products over the connected components of the weight-one subgraph; the Prim-ordering lemma gives a multiplicative representation of the maximum-tree weight.

Reference: V. Féray, *Weighted dependency graphs*, arXiv:1605.03836, Definition 4.5, Lemma 3.3, and Proposition 5.2:
https://arxiv.org/abs/1605.03836

For the PF-I16 reference path process, the candidate weighted graph on marked insertions \(\alpha_i=(X_i,t_i)\) is
\[
w(\alpha_i,\alpha_j)
=
\mathbf1_{\{X_i\cap X_j\ne\varnothing\}}
e^{-\Delta_0|t_i-t_j|}.
\tag{8.1}
\]
The order-two and order-three results in Section 7 are consistent with this candidate. If the full weighted-dependency-graph property can be proved with \(\Psi(B)=\prod_i\|A_i\|_\infty\) and a sequence \(C_m\) of at most exponential growth, then the maximum-tree representation and Prim ordering offer a way to sum local interactions without multiplying independent spatial and temporal Cayley factors.

The missing verification is precise: prove the quasi-factorization bounds required by Proposition 5.2 for products of PF-I16 local path observables, uniformly over repeated labels and arbitrary finite link supports. The product path law is independent across links, but a local observable can couple several link coordinates; this is where the coordinate-incidence contraction must be controlled. The weighted-dependency-graph theorem itself does not supply that model-specific estimate, and its normality criterion is not a quantum Kotecký–Preiss theorem.

**Updated next target:** establish the candidate weighted dependency graph (8.1) for the product SU(2) path process, beginning with the product-cumulant quasi-factorization hypothesis in Proposition 5.2. Then compute the actual weighted-degree/rooted-cluster constants for the face/pair interaction family. The \(m=4\) proof and all-orders activity gate remain OPEN.


### 8.1 Concrete tensor-product reduction

Féray's Section 10 is especially relevant: for a stationary finite-state Markov chain, it proves a time-indexed weighted dependency graph with edge weight \(\lambda_2^{|i-j|}\), using boolean cumulants and the spectral contraction of \(P^n-\Pi\) (Lemmas 10.1–10.3 and Proposition 10.4). The proof mechanism depends on the contraction estimate, not on a special combinatorial property of the state space. Its continuous-time Hilbert-space analogue should therefore be tested for one SU(2) link:
\[
\|P_t-\Pi\|_{2\to2}\le e^{-\Delta_0t}.
\]
The needed output is an explicit one-link weighted-dependency bound for arbitrary bounded one-link multiplication observables at times \(t_i\), with constants \(C_r\) controlled in \(r\).

For elementary tensor insertions
\[
A_i(U_{S_i})=\prod_{e\in S_i}a_{i,e}(U_e),
\qquad |S_i|\le8,
\]
the link path processes are independent. Féray's product/power construction (Proposition 5.11) suggests lifting the one-link graph to monomials of degree at most eight. The resulting edge weight is the maximum over constituent link pairs: it is zero for disjoint supports and \(e^{-\Delta_0|t_i-t_j|}\) when the supports share a link. This is exactly (8.1).

There are two remaining quantitative obligations before this becomes a proof:
1. The actual face and face-pair insertions are not single elementary tensors. Their Peter–Weyl/tensor expansions must have an absolutely summable projective coefficient norm, with an explicit bound compatible with the small local activities. An uncontrolled \(\ell^1\) expansion cannot be used.
2. The constants produced by the degree-eight product construction must have an explicit growth bound in cumulant order \(r\). Existence of constants \(C_r\) alone does not establish analyticity or a nonzero Feynman–Kac activity radius.

This is now the preferred route for the next calculation: first prove the continuous-time one-link weighted-dependency estimate, then lift it to degree-eight elementary tensors, and only then estimate the actual PF-I16 interaction tensor norms.


## 9. Immediate combinatorial target: complete temporal components by a spatial tree

There is a more direct completion formulation that should be tested before attempting a global tensor expansion.

Fix a temporal projection forest \(F\) with path components
\[
C_1,\ldots,C_k\subseteq[m].
\]
Let
\[
S_j=\bigcup_{i\in C_j}X_i
\]
be the union of the link supports in component \(C_j\). If the original support-overlap graph on \([m]\) is connected, its contraction by the partition \(\{C_j\}_{j=1}^k\) is connected. Thus the component support-overlap graph \(H_F\), with \(j\sim p\) whenever \(S_j\cap S_p\ne\varnothing\), is connected.

Choose a spanning tree \(\mathcal S\) of \(H_F\). For each edge \(\{j,p\}\in\mathcal S\), choose a witness pair
\[
i(j,p)\in C_j,\qquad i(p,j)\in C_p,
\qquad
X_{i(j,p)}\cap X_{i(p,j)}\ne\varnothing.
\]
Add the corresponding cross-component edge to \(F\). Since \(F\) has \(m-k\) edges and \(\mathcal S\) has \(k-1\) edges, the union has exactly \(m-1\) edges. It is connected by construction, hence it is a spanning tree on the original \(m\) insertion labels:
\[
T(F,\mathcal S,\text{witnesses})\in\mathcal T_m.
\tag{9.1}
\]

This is the desired *joint completion shape*: retain every temporal \(Q\)-edge of \(F\), and use exactly \(k-1\) shared-link edges to connect its temporal components. Unlike multiplying two spanning-tree counts, (9.1) produces one tree.

The remaining proof obligations are analytic and combinatorial:
1. Show that the component-level spatial cumulant/decoupling expansion supplies the \(k-1\) witness edges with a product of integrable temporal influence kernels. Mere support connectedness is not enough; each witness edge must carry its actual semigroup decay.
2. Define a canonical witness rule and port decoration so that \((F,\mathcal S,\text{witnesses})\) can be decoded from the completed tree and decoration, or prove a uniform fiber bound \(C^m\).
3. Combine the temporal profile-preserving injection with this component completion without losing the exact time-cut weights.
4. Sum the resulting single-tree weights against the face/pair activity and verify the actual rooted-cluster/KP criterion.

The quotient-connectivity assertion is exact. The existence of a bounded-fiber decoder with the required temporal edge weights is **not yet proved**. This is now the primary injection/completion target for the joint space-time gate; the one-link weighted-dependency route in Section 8 is a possible way to supply its component-level edge weights.
