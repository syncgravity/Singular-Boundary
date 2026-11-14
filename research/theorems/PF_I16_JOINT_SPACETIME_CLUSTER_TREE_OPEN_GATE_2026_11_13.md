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

**Important coefficient bookkeeping:** the source objects are not merely \((F,\mathcal S,\text{witnesses})\). The coefficient \(|\alpha_m(F)|\) is represented by the increasing rooted parent trees \(p\in\mathcal T_{\rm inc}(G_F)\). The full source is therefore
\[
(F,p,\mathcal S,\text{witnesses}).
\]
The colored union tree in (9.1) decodes \(F\), \(\mathcal S\), and the spatial witness endpoints, but it does **not** by itself decode \(p\). This is the central bounded-fiber issue. A successful completion must encode the increasing temporal parent tree as additional ports/marks on the same joint tree, or otherwise prove that its multiplicity is absorbed by a uniform \(C^m\) fiber bound. Simply keeping the old temporal completed tree and an independent spatial tree would reintroduce two trees and the superexponential count.

The remaining proof obligations are analytic and combinatorial:
1. Show that the component-level spatial cumulant/decoupling expansion supplies the \(k-1\) witness edges with a product of integrable temporal influence kernels. Mere support connectedness is not enough; each witness edge must carry its actual semigroup decay.
2. Define a canonical witness rule and port decoration so that the **full tuple** \((F,p,\mathcal S,\text{witnesses})\) can be decoded from one completed tree and its decoration, or prove a uniform fiber bound \(C^m\).
3. Combine the temporal profile-preserving injection with this component completion without losing the exact time-cut weights.
4. Sum the resulting single-tree weights against the face/pair activity and verify the actual rooted-cluster/KP criterion.

The quotient-connectivity assertion is exact. The existence of a bounded-fiber decoder for the full source tuple, with the required temporal edge weights, is **not yet proved**. This is now the primary injection/completion target for the joint space-time gate; the one-link weighted-dependency route in Section 8 is a possible way to supply its component-level edge weights.


## 10. Two-channel split-completion: exact edge count, conditional realizability

The source has two component-level trees on the same \(k\) temporal components: the increasing temporal parent tree \(p\) and a spatial support tree \(\mathcal S\). A direct union on the component set has \(2k-2\) edges and generally contains cycles. The following split construction gives the correct one-tree edge count.

For each component path \(C_j\), choose a cut edge \(e_j\) and split it into two nonempty path pieces
\[
C_j=C_j^{T}\sqcup C_j^{S}.
\]
There are now \(2k\) disjoint path pieces, with a T-port and an S-port in each original component. Suppose the following two port-realizability conditions hold:

* for every nonroot vertex \(j\) of \(p\), its T-piece contains a vertex \(c_j^T\) lying strictly inside an edge \((a,b)\) of the T-piece of its parent \(p(j)\);
* for every nonroot vertex \(j\) of \(\mathcal S\), its S-piece contains a vertex \(c_j^S\) whose insertion support overlaps the support of some vertex in the S-piece of its spatial parent.

Starting from the \(2k\) path pieces, perform the existing edge-subdivision completion separately in the T-channel along \(p\), and the corresponding shared-support connector completion in the S-channel along \(\mathcal S\). Each channel joins its \(k\) pieces into a tree using \(k-1\) connector operations. Finally add one bridge between the two root pieces. The resulting graph is connected and has
\[
(m-2k)+ (k-1)+(k-1)+1=m-1
\]
edges, hence is a spanning tree on the original \(m\) insertion labels.

This is a genuine one-tree skeleton for the pair \((p,\mathcal S)\), not a product of two spanning-tree counts. It also makes clear why the assumption \(|C_j|\ge2\) is relevant: it supplies two nonempty pieces per temporal component.

**However, this is not yet an injection.** Three precise issues remain:

1. **Port realizability:** the temporal overlap witness and the spatial shared-link witness for a component may be the same insertion vertex. A cut of \(C_j\) need not place the required T- and S-witnesses in different pieces. The two-port hypotheses above have not been derived from the PF-I16 source constraints.
2. **Component-pair decoder:** after the \(k\) cut edges are removed, the T- and S-pieces must be paired back into their original \(C_j\)'s. The two channel trees and the root bridge do not, by themselves, specify this matching. A canonical pairing mark or a structural decoder is still required, and its fiber must be bounded by \(C^m\).
3. **Temporal profile:** deleting one edge from each \(C_j\) changes the cut profile. The T-channel subdivisions preserve the profile of the forest on which they act, but that fact does not restore the deleted-edge contribution. The S-channel and bridge must be shown to compensate for the lost temporal cut weights, or the construction must be modified to retain a profile-dominating weight.

Thus the edge-count/connectivity lemma is exact **conditional on the two-port hypotheses**, but no bounded-fiber completion theorem is claimed. In particular, the spatial connector must carry a genuine integrable time-influence factor; support overlap alone is only a zero-pattern and supplies no temporal decay.

### 10.1 The next decisive sublemma

Before attempting an all-orders decoder, test whether the actual source data admit a canonical *two-port witness selection*:
\[
(F,p,\mathcal S,\text{witnesses})
\longmapsto
\{(e_j,c_j^T,c_j^S):1\le j\le k\}
\]
such that (i) each cut leaves the two required ports in different pieces, (ii) every T-port is admissible for its parent-edge subdivision, (iii) every S-port realizes its spatial witness, and (iv) the sum of the resulting edge time-lengths dominates the original temporal profile. A single valid family with no such selection would refute this particular two-channel construction, though not every possible joint completion map.


### 10.2 A source-compatible obstruction to the naive two-port hypothesis

The two-port hypothesis is not automatic, even in the smallest interval configuration. Take two temporal components
\[
C_1=(0,2),\qquad C_2=(1,4),
\]
ordered by right endpoint. Their hulls overlap, and the increasing temporal parent of \(C_1\) is \(C_2\). The only vertex of \(C_1\) lying strictly inside the parent edge \((1,4)\) is \(2\). Thus the temporal subdivision port is forced to be \(c^T_1=2\).

Now assign link supports so that
\[
X_2\cap X_1\ne\varnothing,\qquad
X_2\cap X_4\ne\varnothing,
\]
but
\[
X_0\cap X_1=X_0\cap X_4=\varnothing,
\]
and choose the remaining supports so that the only cross-component shared-link witness is insertion \(2\) against \(C_2\). Then the spatial connector port is also forced to be \(c^S_1=2\). No cut of the two-vertex path \(C_1\) can put these two required uses into distinct nonempty pieces.

This example satisfies the interval-overlap condition needed by the temporal parent construction and has a connected spatial support-overlap graph, but it violates the proposed distinct-port selection. Therefore Section 10's two-port split map cannot be made universal merely from \(|C_j|\ge2\), temporal hull overlap, and spatial support connectedness. A successful replacement must allow a shared port to serve both channels, use a different local gadget, or abandon this particular split architecture.


## 11. Shared-port fusion: exact local case and a profile obstruction

The shared-port issue from Section 10.2 has two different outcomes, depending on the location of the spatial witness inside the temporal parent component.

### 11.1 Exact fusion when the witness is a subdivision endpoint

Suppose the temporal completion processes a child component containing connector vertex (c), and subdivides the current parent-chain edge ((x,y)) with
[
x<c<y.
]
The operation replaces ((x,y)) by
[
(x,c),qquad(c,y).
]
If the selected spatial witness in the parent component is (x) or (y), then the corresponding cross-component edge is already one of these two subdivision edges. Thus the same local operation performs both jobs:

* it inserts (c) into the temporal parent chain, as required by the profile-preserving temporal completion;
* it realizes the selected shared-support edge, because (X_ccap X_x
earnothing) or (X_ccap X_y
earnothing).

No extra edge is added, so the completed graph remains the temporal spanning tree and its cut profile is unchanged. This is a valid **local shared-port fusion lemma**. It applies only when the spatial witness endpoint is one of the two endpoints of the actual parent-chain edge being subdivided. It does not establish a component-level spatial spanning tree or a bounded-fiber decoder for the full source tuple.

### 11.2 Non-endpoint witness: exact-profile completion is impossible

The endpoint condition cannot simply be dropped. Consider the temporal forest on ordered labels
[
0<1<2<4<7
]
with components
[
C_1=(0,2),qquad C_2=(1,4,7).
]
The temporal parent of (C_1) is (C_2), and the canonical temporal connector is (c=2), lying strictly inside the parent edge ((1,4)). Choose supports so that the only cross-component shared-link witness is
[
X_2cap X_7
earnothing.
]
In particular, the spatial witness endpoint (7) is not an endpoint of the temporal parent edge ((1,4)).

The temporal forest edges are
[
F={(0,2),(1,4),(4,7)}.
]
Its exact cut-crossing profile, for cuts (q=0,ldots,6), is
[
igl(n_q(F)igr)_{q=0}^{6}=(1,2,1,1,1,1,1).
	ag{11.1}
]
Any tree realizing the required spatial witness must contain edge ((2,7)). This edge crosses both the cut at (q=2) and the cut at (q=4). By (11.1), each of those cuts has exactly one crossing edge, so ((2,7)) would have to be the unique crossing edge at both cuts.

In a tree, if an edge is the unique edge crossing a cut, deleting it separates the vertex set into exactly the two sides of that cut. But the two cuts have different bipartitions:
[
{0,1,2}mid{4,7},
qquad
{0,1,2,4}mid{7}.
]
One deleted edge cannot induce both bipartitions. This is a contradiction.

Therefore:
[
oxed{	ext{No spanning tree contains }(2,7)	ext{ and preserves the full profile }(11.1).}
	ag{11.2}
]
This is stronger than failure of the particular subdivision algorithm: no alternative tree topology can meet both requirements in this example.

The support assignment is compatible with the local-support setting: take one link shared by (X_2) and (X_7), and choose all other links in the five supports distinct. The spatial overlap graph on the two temporal components is connected, while its only cross-component witness is the non-endpoint pair ((2,7)).

### 11.3 Consequence for the bounded-fiber map

The shared-port recommendation is therefore only partially successful:

1. **Closed locally:** if the spatial witness is an endpoint of the temporal parent-chain edge, one temporal subdivision edge serves both channels.
2. **Refuted in general:** if the only spatial witness is elsewhere in the parent component, exact temporal-profile preservation may be impossible, even before any decoder or fiber-count issue is considered.
3. **Still open:** a weighted completion that permits controlled profile loss, or a different joint cumulant argument that does not require an exact-profile spatial witness edge.

The next viable route is consequently not to force the two-channel split map. It is to return to the weighted-dependency-graph route of Section 8, where a spatial witness edge may carry its own integrable temporal influence kernel and need not be an edge in the exact temporal-profile tree. The model-specific quasi-factorization and explicit order-growth bounds remain to be proved. No all-orders joint space-time tree inequality or quantum cluster theorem is claimed here.


## 12. Continuous-time one-link weighted-dependency estimate

The obstruction in Section 11 rules out an exact-profile completion for arbitrary spatial witnesses. The analytic alternative in Section 8 can be advanced one level without any tensor expansion: the one-link stationary reference process itself has an explicit weighted-dependency estimate.

Let (U_t) be one stationary reversible link process with invariant law (pi), Markov semigroup (P_t), projection (Pi f=pi(f)mathbf1), and
[
|P_t-Pi|_{L^2(pi)	o L^2(pi)}
le e^{-Delta_0t}.
	ag{12.1}
]
For bounded multiplication observables (f_1,ldots,f_r), put (Z_j=f_j(U_{t_j})), and order the times
[
t_1le t_2lecdotsle t_r,qquad g_j=t_{j+1}-t_j.
]

### 12.1 Boolean cumulants factor across every temporal gap

The Boolean cumulant is the alternating sum over interval partitions:
[
B_r(Z_1,ldots,Z_r)
=
sum_{Dsubseteq[r-1]}(-1)^{|D|}
prod_{Iinoperatorname{Int}(D)}
mathbb E!left[prod_{jin I}Z_jight],
	ag{12.2}
]
where (operatorname{Int}(D)) is the interval partition obtained by cutting between (j) and (j+1) for (jin D).

The Markov moment formula expresses each interval-block moment by inserting (P_{g_j}) between consecutive multiplication operators. The product over interval blocks inserts (Pi) at each cut. Thus the alternating sum (12.2) is exactly the operator identity
[
B_r(Z_1,ldots,Z_r)
=
leftlangle
mathbf1,,
M_{f_1}(P_{g_1}-Pi)M_{f_2}
cdots
(P_{g_{r-1}}-Pi)M_{f_r}mathbf1
ightangle_{L^2(pi)}.
	ag{12.3}
]
Consequently, by (12.1) and (|M_f|_{2	o2}le|f|_infty),
[
oxed{
|B_r(Z_1,ldots,Z_r)|
le
e^{-Delta_0(t_r-t_1)}
prod_{j=1}^r|f_j|_infty.
}
	ag{12.4}
]
This is an exact continuous-time analogue of the Boolean-cumulant step in Féray's finite-state Markov-chain argument.

### 12.2 Classical cumulants and an explicit factorial envelope

The classical/Boolean cumulant relation expresses the classical cumulant as
[
kappa_r(Z_1,ldots,Z_r)
=
sum_{hoinmathcal P_{mathrm{irr}}[r]}
d_ho
prod_{Cinho}B_{|C|}(Z_j:jin C),
	ag{12.5}
]
where (mathcal P_{mathrm{irr}}[r]) consists of the set partitions that are not separated by any cut ({1,ldots,q}mid{q+1,ldots,r}), and (d_ho) are universal coefficients.

For every irreducible (ho), the index intervals
[
[min C,max C],qquad Cinho,
]
cover every consecutive gap ([j,j+1]). Therefore
[
sum_{Cinho}(t_{max C}-t_{min C})
ge t_r-t_1.
	ag{12.6}
]
Applying (12.4) to every block in (12.5) gives the same full-span exponential factor.

An explicit crude bound on the total absolute coefficient mass follows directly by expanding the classical moment-cumulant formula into Boolean moment-cumulant formulas. A set partition with (k) blocks has Möbius coefficient of magnitude ((k-1)!), and its (k) block moments produce at most (2^{r-k}) interval-partition terms. Hence
[
sum_{hoinmathcal P_{mathrm{irr}}[r]}|d_ho|
le
sum_{k=1}^r
left{egin{matrix}r\kend{matrix}ight}
(k-1)!,2^{r-k}
le 2^rsum_{k=1}^r k^{r-1}
le 2^r r^r
le (2e)^r r!.
	ag{12.7}
]
Combining (12.4)–(12.7),
[
oxed{
|kappa_r(f_1(U_{t_1}),ldots,f_r(U_{t_r}))|
le
(2e)^r r!,
e^{-Delta_0(t_{max}-t_{min})}
prod_{j=1}^r|f_j|_infty.
}
	ag{12.8}
]

For the complete graph on the (r) time-labelled observables with edge weights
[
w_{ij}=e^{-Delta_0|t_i-t_j|},
]
the maximum spanning-tree product is exactly
[
mathcal M(w)=e^{-Delta_0(t_{max}-t_{min})},
]
because the minimum-length spanning tree on the line joins consecutive ordered times. Thus (12.8) proves a one-link weighted-dependency-graph estimate with the explicit factorial envelope (C_rle(2e)^r r!). Repeated times are allowed: zero gaps simply give (P_0-Pi=I-Pi), whose (L^2) norm is at most one.

### 12.3 What this does and does not lift

For elementary tensor insertions
[
A_i(U_{X_i})=prod_{ein X_i}f_{i,e}(U_e),
qquad |X_i|le8,
]
independence of the link path processes and the product-stability theorem for weighted dependency graphs suggest the lifted edge weight
[
w_{ij}
=
mathbf1_{{X_icap X_j
earnothing}}
e^{-Delta_0|t_i-t_j|}.
	ag{12.9}
]
This is the desired spatial-incidence/time-decay bond, now supported by an explicit one-link estimate rather than only a finite-state analogy.

There are still two nontrivial gates:

1. **Degree-eight product constants.** Féray's product-stability proposition gives constants (D_{8,r}) depending on the one-link constants through order (8r), but does not itself give the growth estimate needed here. A direct count in the Leonov–Shiryaev product-cumulant formula must show that the lifted constants, after the (1/r!) Feynman–Kac normalization, are compatible with a nonzero activity radius.
2. **Actual PF-I16 insertions.** The face and face-pair observables are not known here to be elementary tensors. Their finite-link tensor/projective expansions must have an absolutely summable coefficient norm with an explicit bound compatible with the local activities. No uncontrolled Peter–Weyl (ell^1) expansion is allowed.

Accordingly, the one-link estimate (12.8) is **closed under (12.1)**. The degree-eight lift with a usable order-growth bound, the projective tensor estimate for the actual PF-I16 insertions, and the all-orders joint space-time/KP theorem remain **open**. This is the new preferred analytic route; it does not revive the refuted exact-profile completion in Section 11.2.


### 12.4 Explicit degree-eight Leonov–Shiryaev constant

We now make the product-stability constant explicit, using the precise Leonov–Shiryaev formula in Féray, Proposition 5.11.

Let
\[
A_i=\prod_{a=1}^{d_i}Y_{\alpha_{i,a}},\qquad 1\le d_i\le8,
\]
where the \(Y_\alpha\) are elementary link-time observables. Write
\[
\mathfrak I=I_1\uplus\cdots\uplus I_r,\qquad
I_i=\{\alpha_{i,1},\ldots,\alpha_{i,d_i}\},
\qquad n:=|\mathfrak I|\le8r.
\]
The Leonov–Shiryaev identity is
\[
\kappa(A_1,\ldots,A_r)
=
\sum_{\substack{\pi\vdash\mathfrak I\\
\pi\vee\{I_1,\ldots,I_r\}=\{\mathfrak I\}}}
\prod_{B\in\pi}\kappa(Y_\alpha:\alpha\in B).
\tag{12.10}
\]
Here \(\pi\) ranges over multiset partitions, and the join condition says that the block hyperedges connect all \(r\) product rows.

For each block \(B\), the one-link estimate (12.8) gives
\[
|\kappa(Y_\alpha:\alpha\in B)|
\le (2e)^{|B|}|B|!\,
\mathcal M(w[B]),
\tag{12.11}
\]
with the convention that the term is zero unless the block is monochromatic in its link label. The maximum-spanning-tree product inequality for connected joins, together with supermultiplicativity of the trivial factor \(\Psi\equiv1\), gives
\[
\prod_{B\in\pi}\mathcal M(w[B])
\le \mathcal M(w^{[8]}[A_1,\ldots,A_r]),
\tag{12.12}
\]
where
\[
w^{[8]}(A_i,A_j)
=\max_{a\le d_i,\,b\le d_j}
w((i,a),(j,b))
=\mathbf1_{\{X_i\cap X_j\ne\varnothing\}}
e^{-\Delta_0|t_i-t_j|}.
\tag{12.13}
\]
The inequality follows because the union of the block trees is connected on the product rows; it contains a spanning tree, and every omitted edge weight is at most one.

Consequently an explicit admissible product constant is
\[
D_{8,r}
:=
\max_{d_1,\ldots,d_r\le8}
\sum_{\substack{\pi\vdash I_1\uplus\cdots\uplus I_r\\
\pi\vee\{I_1,\ldots,I_r\}=\{\mathfrak I\}}}
\prod_{B\in\pi}(2e)^{|B|}|B|!.
\tag{12.14}
\]
This is a genuine finite formula, not merely the existence statement in Proposition 5.11.

A uniform closed-form upper bound follows by dropping both the monochromatic restriction and the join restriction. For \(n=8r\), define
\[
S_n:=\sum_{\pi\vdash[n]}\prod_{B\in\pi}|B|!.
\]
The exponential formula gives
\[
S_n=n![z^n]\exp\!\left(\sum_{s\ge1}z^s\right)
=n![z^n]\exp\!\left(\frac z{1-z}\right).
\tag{12.15}
\]
Taking \(x=1-n^{-1/2}\) in Cauchy's coefficient estimate, for \(n\ge4\),
\[
[z^n]\exp\!\left(\frac z{1-z}\right)
\le
\exp\!\left(\frac{x}{1-x}\right)x^{-n}
\le e^{2\sqrt n}.
\tag{12.16}
\]
Thus, for every \(r\ge1\),
\[
\boxed{
D_{8,r}
\le (2e)^{8r}(8r)!\,e^{2\sqrt{8r}}.
}
\tag{12.17}
\]
For \(n<4\), the same displayed bound follows directly by inspection.

This proves an explicit degree-eight product-stability bound and retains the desired maximum-tree weight (12.13). It is, however, **too large for the intended Feynman–Kac use**:
\[
\frac{D_{8,r}}{r!}
\le
(2e)^{8r}\frac{(8r)!}{r!}e^{2\sqrt{8r}}
=
\exp\!\bigl(7r\log r+O(r)\bigr).
\tag{12.18}
\]
The right side is superexponential in \(r\), so (12.17) does not yield a nonzero activity radius after the \(1/r!\) normalization.

This is a limitation of the absolute Leonov–Shiryaev partition sum, not a proof that the actual product cumulants have superexponential growth. The sum discards cancellations between different multiset partitions and also ignores the monochromatic link restriction. In particular, (12.17) is a valid but deliberately coarse \(D_{8,r}\) estimate; it does not close the order-growth gate.

### 12.5 The sharper combinatorial gate

The remaining task is now an explicit cancellation-sensitive estimate for (12.10), not another application of the raw Bell-number bound. The needed statement is:

\[
\boxed{
\sum_{\substack{\pi\vdash\mathfrak I\\
\pi\vee\{I_1,\ldots,I_r\}=\{\mathfrak I\}}}
\prod_{B\in\pi}
\left|\kappa(Y_\alpha:\alpha\in B)\right|
\ \le\
C_8^r r!\,
\mathcal M(w^{[8]}[A_1,\ldots,A_r])
}
\tag{12.19}
\]
with \(C_8\) independent of \(r\), the number of links, and the insertion supports.

The absolute-value version (12.19) may itself be too strong: the actual Leonov–Shiryaev sum is signed/complex and can have substantial cancellation. The analytically relevant alternative is to reorganize the full sum before taking absolute values, using a connected-partition/Ursell or quasi-factorization representation that keeps the same maximum-tree weight. This is the precise unresolved subproblem.

**Status update:** the degree-eight product constant now has an explicit finite formula and a rigorous closed-form upper bound, but the bound is superexponential after Feynman–Kac normalization. The desired \(C_8^r r!\) growth, or another summable cancellation-sensitive replacement, remains OPEN. No all-orders joint space-time/KP theorem is claimed.


### 13. Order-four support-sensitive bound from the full Leonov–Shiryaev formula

The cancellation-sensitive all-orders estimate in Section 12.5 is still open. There is, however, a useful finite-order result: for four elementary-tensor insertions, the full Leonov–Shiryaev expansion gives an explicit support-sensitive maximum-tree bound. This closes the order-four combinatorial estimate with a large but finite constant, without asserting exponential-in-order control.

Let
\[
A_i(t_i)=\prod_{a=1}^{d_i}Y_{i,a}(t_i),\qquad
d_i\le8,\qquad i=1,\ldots,4,
\]
where each elementary factor is a bounded observable of one link path, and within a row the four-or-fewer (in fact at most eight) link labels are distinct. Let \(X_i\) be the link support of row \(i\), and let \(G_{\rm ov}\) be the graph on \(\{1,2,3,4\}\) with \(ij\) an edge exactly when \(X_i\cap X_j\ne\varnothing\).

For a connected \(G_{\rm ov}\), define
\[
\mathcal M(G_{\rm ov};\mathbf t)
=\max_{T\in\mathcal T(G_{\rm ov})}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|},
\]
where \(\mathcal T(G_{\rm ov})\) is its set of spanning trees. Put
\[
D_{8,4}:=
\max_{\substack{1\le d_i\le8\\
\ell:\mathfrak I\to\mathcal E\\
\ell\text{ injective on each }I_i}}
\sum_{\substack{\pi\vdash I_1\uplus\cdots\uplus I_4\\
\pi\vee\{I_1,\ldots,I_4\}=\{\mathfrak I\}\\
\ell\text{ is constant on every block }B\in\pi}}
\prod_{B\in\pi}(2e)^{|B|}|B|!.
\tag{13.1}
\]
This is a finite, explicit integer-real sum over partitions of at most 32 labeled slots.

For each partition \(\pi\) in the Leonov–Shiryaev formula, every block \(B\) is monochromatic in its link label. The one-link estimate (12.8) bounds its cumulant by
\[
(2e)^{|B|}|B|!\,
\exp\{-\Delta_0(\max_{i\in J(B)}t_i-\min_{i\in J(B)}t_i)\}
\prod_{(i,a)\in B}\|Y_{i,a}\|_\infty,
\]
where \(J(B)\) is the set of rows represented in \(B\). Since the maximum-spanning-tree product of the complete temporal graph on \(J(B)\) is exactly this exponential, choose such a tree for every block. Each chosen edge joins two rows sharing the link label of \(B\), hence is an edge of \(G_{\rm ov}\).

The join condition in (13.1) says that the union of these block trees is connected on the four rows. Delete cycle edges until a spanning tree remains. All edge weights lie in \([0,1]\), so deleting edges can only increase the product. The resulting tree is a spanning tree of \(G_{\rm ov}\), and its product is at most \(\mathcal M(G_{\rm ov};\mathbf t)\). Therefore every partition summand has the same common majorant, and
\[
\boxed{
|\kappa(A_1(t_1),A_2(t_2),A_3(t_3),A_4(t_4))|
\le
D_{8,4}\,\mathcal M(G_{\rm ov};\mathbf t)
\prod_{i=1}^4\prod_{a=1}^{d_i}\|Y_{i,a}\|_\infty.
}
\tag{13.2}
\]
If \(G_{\rm ov}\) is disconnected, the cumulant is zero by independence, so (13.2) extends with a zero right-hand side under the convention \(\mathcal M=0\) for disconnected graphs. Since a maximum is bounded by the sum,
\[
\mathcal M(G_{\rm ov};\mathbf t)
\le
\sum_{T\in\mathcal T(G_{\rm ov})}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|},
\tag{13.3}
\]
which is precisely the proposed support-restricted tree form at order four.

A fully closed, deliberately crude numerical envelope follows from the same generating function as (12.15):
\[
D_{8,4}
\le
(2e)^{32}\,32!\,[z^{32}]
\exp\!\left(\frac z{1-z}\right)
\le
(2e)^{32}\,32!\,1020
<9.2\times10^{61}.
\tag{13.4}
\]
The first inequality drops both the monochromatic and connected-join restrictions. The coefficient bound uses the exact recurrence a_0=1, n a_n=sum_{j=0}^{n-1}(n-j)a_j for A(z)=exp(z/(1-z)), giving a_32=[z^32]A(z)<1020. The elementary rational estimate e<2.719 then proves the displayed numerical envelope; see [the exact-rational verifier](../verification/verify_pf_i16_degree_eight_ls_constant.py). This constant is not optimized and is not proposed as an activity constant.

For general local insertions with an absolutely convergent elementary-tensor representation
\[
A_i=\sum_\nu c_{i,\nu}\prod_{a=1}^{d_{i,\nu}}Y_{i,\nu,a},
\qquad d_{i,\nu}\le8,
\]
the same estimate follows by multilinearity, with the elementary product norm replaced by the projective coefficient norm
\[
\|A_i\|_{\pi,8}
:=\inf\sum_\nu |c_{i,\nu}|
\prod_a\|Y_{i,\nu,a}\|_\infty.
\]
No assertion is made that the actual PF-I16 face and face-pair insertions have finite, uniformly controlled \(\|\cdot\|_{\pi,8}\); establishing that remains a separate open gate.

**Scope.** Equation (13.2) proves the support-sensitive maximum-tree estimate for four elementary-tensor insertions, and (13.3) gives the requested spanning-tree form at that fixed order. It does not prove the all-orders estimate (3.1), does not give an order-uniform \(C_{\rm st}^m\) constant, and does not close the Feynman–Kac/KP expansion. The cancellation-sensitive all-orders product-cumulant bound and the actual insertion projective norms remain OPEN.


### 14. Absolute Leonov–Shiryaev summation has an intrinsic superfactorial obstruction

The failure of the absolute partition majorant is not merely an artifact of the estimate \(n\le8r\) in (12.17). Its combinatorics already contains a superfactorial contribution for the maximally overlapping support pattern.

Fix \(r\ge2\). Take eight link labels \(e_1,\ldots,e_8\), and let every row contain all eight labels:
\[
I_i=\{(i,e_1),\ldots,(i,e_8)\},\qquad i=1,\ldots,r.
\]
For each link \(e_a\), choose the single-block partition
\[
\pi_a=\bigl\{\{(1,e_a),\ldots,(r,e_a)\}\bigr\},
\]
and put \(\pi=\pi_1\cup\cdots\cup\pi_8\). Each block is monochromatic, and the join of \(\pi\) with the row partition is the one-block partition: every one of the eight blocks meets every row. Thus \(\pi\) is an admissible connected Leonov–Shiryaev partition.

Its contribution to the absolute coefficient envelope (12.14) is exactly
\[
\prod_{a=1}^8 (2e)^r r!
=(2e)^{8r}(r!)^8.
\]
Consequently the explicit absolute partition envelope necessarily obeys
\[
\boxed{
D_{8,r}\ge (2e)^{8r}(r!)^8,
\qquad
\frac{D_{8,r}}{r!}\ge(2e)^{8r}(r!)^7.
}
\tag{14.1}
\]
In particular, no refinement of the *counting* of the absolute Leonov–Shiryaev terms can produce a bound \(D_{8,r}\le C^r r!\) uniformly in \(r\). The obstruction is present in the admissible partition family itself.

This is **not** a lower bound on the actual product cumulant. The Leonov–Shiryaev identity is a signed/complex sum, and the eight large one-link contributions can cancel against the other admissible partitions. The elementary example in which all eight link coordinates are shared by all rows makes the point: at equal times, if \(Y_{i,a}=Z_a\) for every row \(i\), then all row observables are the same bounded variable \(A=\prod_{a=1}^8Z_a\). Their joint cumulant is the ordinary repeated-variable cumulant \(\kappa_r(A,\ldots,A)\), whose growth is governed by the one-variable log moment-generating function, not by eight independent factors of \(r!\). The LS representation must cancel its large absolute terms to recover this behavior.

**Consequence.** The all-orders gate is now sharply identified: one must exploit algebraic cancellation in the full product-cumulant identity, or use a different quasi-factorization/interpolation before taking absolute values. A stronger absolute-value estimate of the form (12.19) is impossible for this general degree-eight product class. The fixed-order \(m=4\) theorem in Section 13 is unaffected, since its finite constant is allowed to be large. The all-orders cancellation-sensitive bound and the actual PF-I16 insertion norm control remain OPEN.


### 15. Actual face/pair insertion projective norms: Peter–Weyl reduction and the remaining regularity constant

This section replaces the earlier abstract assumption that the actual insertions possess projective tensor representations. It gives a concrete Peter–Weyl representation and an explicit norm bound in terms of a one-rotor \(H^6\) norm. The latter is finite by compact elliptic regularity, but its uniform numerical value has not yet been extracted from the radial ODE.

For a function \(F\) on \(G^k\), \(G=\mathrm{SU}(2)\), define the \(L^\infty\)-projective norm
\[
\|F\|_{\pi,k}
=\inf\left\{\sum_\nu |c_\nu|
\prod_{j=1}^k\|F_{\nu,j}\|_\infty:
F=\sum_\nu c_\nu\bigotimes_{j=1}^kF_{\nu,j}\right\}.
\tag{15.1}
\]
The infimum is over absolutely convergent representations. This is the norm needed to apply a monomial/weighted-dependency-graph lift to elementary one-link path observables.

#### 15.1. The one-face plaquette insertion is an explicit finite tensor

With the normalized PF-I16 plaquette convention \(p_f(H)=\frac12\operatorname{Tr}H\), and oriented face word \(H=U_1^{\epsilon_1}\cdots U_4^{\epsilon_4}\), the fundamental representation gives
\[
p_f(H)=\frac12\sum_{i_0,i_1,i_2,i_3=1}^{2}
D(U_1^{\epsilon_1})_{i_0i_1}
D(U_2^{\epsilon_2})_{i_1i_2}
D(U_3^{\epsilon_3})_{i_2i_3}
D(U_4^{\epsilon_4})_{i_3i_0}.
\]
Every matrix coefficient has supremum norm at most one. There are \(2^4=16\) summands, so
\[
\boxed{\|p_f(H_f)\|_{\pi,4}\le8,\qquad
\|v_f\|_{\pi,4}\le8\rho_fb_f\le256b_0,}
\tag{15.2}
\]
after discarding the scalar energy shift in the one-face interaction. This is an actual finite decomposition, not a smoothness assumption.

#### 15.2. Gradient insertions have an explicit Fourier projective majorant

Write the radial one-face logarithm in the normalized character basis
\[
s_f(H)=\sum_{n=0}^\infty c_{f,n}\chi_n(H),
\]
where \(\chi_n\) is the character of the \((n+1)\)-dimensional irreducible representation. The radius-two Laplacian eigenvalue is
\[
\lambda_n=\frac{n(n+2)}4,
\]
and a unit Lie-algebra generator has operator norm \(n/2\) in this representation.

The four-factor trace expansion of \(\chi_n(U_1^{\epsilon_1}\cdots U_4^{\epsilon_4})\) has \((n+1)^4\) terms, each a product of four one-link matrix coefficients of norm at most one. Differentiating in one link replaces one matrix coefficient by a matrix coefficient of \(D^{(n)}(X)\), whose norm is at most \(n/2\). Thus every scalar component of the pulled-back one-link gradient has projective norm at most
\[
P_f:=\frac12\sum_{n\ge1}n(n+1)^4|c_{f,n}|.
\tag{15.3}
\]
Define
\[
\|s_f\|_{H^6}^2
:=\sum_{n\ge0}(1+\lambda_n)^6|c_{f,n}|^2.
\]
Cauchy–Schwarz gives
\[
P_f\le C_6\|s_f\|_{H^6},\qquad
C_6:=\frac12\left[
\sum_{n\ge1}
\frac{n^2(n+1)^8}{(1+n(n+2)/4)^6}
\right]^{1/2}<9.1.
\tag{15.4}
\]
For the displayed strict bound, use \(1+n(n+2)/4\ge(n+1)^2/4\) and
\(\sum_{n\ge1}n^2/(n+1)^4<0.324\). In particular, the projective gradient expansion is absolutely convergent whenever \(s_f\in H^6(\mathrm{SU}(2))\).

The radial ground-state branch is analytic in \(b_f/A_f\) near zero: the isolated compact-rotor operator is an analytic family with a simple positive ground state, and elliptic regularity transfers this analyticity to \(H^6\). On the compact parameter interval \(0\le\beta_f\le1/25000\), simplicity and compactness therefore give a finite constant
\[
K_6:=
\sup_{0<\beta\le1/25000}
\frac{\|s_\beta-\int s_\beta\,dH\|_{H^6}}{\beta}<\infty.
\tag{15.5}
\]
The quotient has a finite limit at zero by analytic perturbation. The value of \(K_6\) is not yet evaluated from the radial ODE; it is an explicit remaining numerical regularity input, not an assumed projective norm.

Since \(\beta_f\le2b_0/a_0\), (15.3)–(15.5) give
\[
P_f\le 2C_6K_6\,\frac{b_0}{a_0}.
\tag{15.6}
\]

#### 15.3. Actual pair and cut insertions

The shared-link term is
\[
V_{fg}=2\sum_{e\in\partial f\cap\partial g}
a_e\sum_{\alpha=1}^3
(D_{e,\alpha}s_f)(D_{e,\alpha}s_g).
\]
Products of two elementary tensor expansions combine their factors on a shared link into one bounded one-link function. Therefore
\[
\|V_{fg}\|_{\pi,8}
\le6\sum_{e\in\partial f\cap\partial g}a_eP_fP_g
\le384\,C_6^2K_6^2\,\frac{b_0^2}{a_0}.
\tag{15.7}
\]
Here there are at most four shared links and \(a_e\beta_f\beta_g\le16b_0^2/a_0\).

For the first cut insertion, the exact identity
\[
\Delta s_f+2\alpha_f|\nabla s_f|^2
=(2\alpha_f-1)|\nabla s_f|^2
-\beta_f p_f-\lambda_f
\]
and \(\||\nabla s_f|^2\|_{\pi,4}\le3P_f^2\) give the local bounds
\[
\boxed{
\|b_{a,f}\|_{\pi,4}
\le256b_0+192\,C_6^2K_6^2\,\frac{b_0^2}{a_0},
\quad
\|b_{a,fg}\|_{\pi,8}
\le768\,C_6^2K_6^2\,\frac{b_0^2}{a_0}.
}
\tag{15.8}
\]
The scalar \(\lambda_f\) is omitted because it contributes no cumulant of order at least two. For distinct cuts \(a,b\), the coefficient of \(|\nabla s_f|^2\) is at most three, so
\[
\boxed{
\|b_{ab,f}\|_{\pi,4}
\le256b_0+576\,C_6^2K_6^2\,\frac{b_0^2}{a_0},
\quad
\|b_{ab,fg}\|_{\pi,8}
\le1536\,C_6^2K_6^2\,\frac{b_0^2}{a_0}.
}
\tag{15.9}
\]
These are termwise local bounds. A global cut insertion is a marked sum of such terms; its rooted activity must be summed with the actual cut-incidence profile, not bounded by its volume-dependent global operator norm.

For the shared-link residual
\[
R_e=a_e\left(\left|\sum_{f:e\in\partial f}D_es_f\right|^2
-\frac1{d_e}\sum_{f:e\in\partial f}|D_es_f|^2\right),
\]
the same tensor multiplication gives the safe local estimate
\[
\boxed{
\|R_e\|_{\pi,25}
\le3120\,C_6^2K_6^2\,\frac{b_0^2}{a_0}.
}
\tag{15.10}
\]
This uses \(d_e\le8\), at most three tangent components, and the same \(a_e\beta_f\beta_g\) allocation. Any source observable \(r_i\) that is a sum of these residuals inherits the sum of (15.10) over its specified link support. The exact \(r_i\) definition and its support multiplicity must be inserted before assigning a numerical marked-root norm.

#### 15.4. Projective activity audit and the KP threshold

Put \(x=b_0/a_0\). With the universal eight-face and 224-pair incidences, \(e^{|X|/8}\le e^{1/2}<1.65\) for face terms and \(\le e<2.72\) for pair terms, (15.2) and (15.7) yield
\[
\kappa_\pi(x)
:=\sup_e\sum_{X\ni e}
\frac{\|v_X\|_{\pi,|X|}}{\Delta_0}e^{|X|/8}
\le
4505.6\,x+2.5890\times10^7 K_6^2x^2.
\tag{15.11}
\]
The displayed decimals are upward-rounded. At the currently recorded \(x=1/50000\), the linear face contribution alone is \(0.090112\), so this projective-norm majorant does **not** meet the candidate KP threshold \(a=1/8\), even before the pair term and before the unknown joint-cumulant constant are included.

If a cancellation-preserving joint support/time WDG theorem were proved with coefficient-growth constant \(C_{\rm st}\), the standard integrated-tree KP input would require, in this normalization,
\[
2C_{\rm st}\,\kappa_\pi(x)\le\frac18.
\tag{15.12}
\]
Equations (15.11)–(15.12) give an explicit conditional smaller-coupling radius once \(K_6\) and \(C_{\rm st}\) are known. They do not certify the present \(1/50000\) threshold.

**Conclusion of this audit.** The actual one-face insertion has a finite eight-term projective representation; the pair, first-cut, second-cut, and residual insertions have explicit projective majorants controlled by the one-rotor \(H^6\) constant \(K_6\). The required numerical value of \(K_6\), the marked source multiplicity, and—most importantly—the cancellation-preserving all-orders joint support/time cumulant constant are not yet established. Consequently no KP convergence theorem is claimed. The present projective-norm *upper majorant* is too costly to certify the KP inequality at the recorded coupling threshold; this is not a lower bound on the true projective norm and does not refute convergence. A direct tensorized semigroup proof in the \(L^\infty\) norm, avoiding the factor-eight plaquette projective loss, is now the preferred route for preserving the existing activity margin.


### 16. Cancellation-preserving route: exact link-factorization of quasi-factorization variables

The absolute Leonov–Shiryaev envelope in Sections 12 and 14 is too large. A more promising route is to apply the quasi-factorization formulation of weighted dependency graphs *before* expanding products into Leonov–Shiryaev partitions. This section records the exact reduction and isolates the remaining combinatorial estimate.

Take elementary tensor insertions
\[
A_i(t_i)=\prod_{e\in X_i}f_{i,e}(U_e(t_i)),\qquad |X_i|\le8,
\]
and let \(I_e=\{i:e\in X_i\}\). For formal variables \(z_i\), use the shifted row variables
\[
Y_i(z_i)=\prod_{e\in X_i}(1+z_i f_{i,e}(U_e(t_i))).
\]
Their joint moments are polynomials with constant term one:
\[
u_\Delta(\mathbf z)
=\mathbb E_0\prod_{i\in\Delta}Y_i(z_i)
=\prod_e u^e_{\Delta\cap I_e}(\mathbf z),
\quad
u^e_J(\mathbf z)
=\mathbb E_e\prod_{i\in J}(1+z_i f_{i,e}(U_e(t_i))).
\tag{16.1}
\]
Thus all \(u_\Delta\) are invertible as formal power series at \(\mathbf z=0\), with no positivity or nonzero-moment assumption.

Define the Boolean-lattice quasi-factorization variable
\[
P_\Delta(\mathbf z)
=\prod_{\delta\subseteq\Delta}
u_\delta(\mathbf z)^{(-1)^{|\Delta|-|\delta|}}.
\tag{16.2}
\]
Taking formal logarithms in (16.1) and applying Möbius cancellation gives the exact identity
\[
\boxed{
P_\Delta(\mathbf z)
=\prod_{e:\,\Delta\subseteq I_e}
P^e_\Delta(\mathbf z),\qquad
P^e_\Delta
=\prod_{\delta\subseteq\Delta}
(u^e_\delta)^{(-1)^{|\Delta|-|\delta|}}.
}
\tag{16.3}
\]
In particular, if no single link belongs to every support \(X_i\), \(i\in\Delta\), then \(P_\Delta\equiv1\). Otherwise there are at most eight factors in (16.3), since every row support has size at most eight. This is the precise way in which the bounded local support enters *before* the cumulant partition expansion.

For one link, the semigroup identity from Section 12 gives the classical-cumulant estimate
\[
|\kappa_e(f_{i_1}(U(t_{i_1})),\ldots,
f_{i_k}(U(t_{i_k})))|
\le(2e)^k k!\,
e^{-\Delta_0(\max t_i-\min t_i)}
\prod_j\|f_{i_j}\|_\infty.
\tag{16.4}
\]
The desired one-link quasi-factorization estimate is therefore
\[
|P^e_\Delta-1|
\le K^{|\Delta|}\,
e^{-\Delta_0(\max_{i\in\Delta}t_i-\min_{i\in\Delta}t_i)}
\prod_{i\in\Delta}|z_i|
\quad\text{at the square-free coefficient level},
\tag{16.5}
\]
with a controlled analytic majorant for the higher powers of the \(z_i\). The square-free coefficient of \(\log P^e_\Delta\) is the one-link cumulant and is controlled by (16.4). This does not by itself bound the square-free coefficient of \(P^e_\Delta-1\), which also contains products of lower-order connected terms, nor the higher powers of the \(z_i\). A uniform analytic majorant for the full formal series in (16.5) has not yet been derived.

Féray's Proposition 5.8 identifies quasi-factorization bounds of this type with weighted-dependency-graph cumulant bounds; its proof organizes the cumulant as a sum over connected collections of subsets, so the disconnected terms cancel before absolute values are taken. The present product structure makes every nontrivial quasi-factorization subset \(\Delta\) a subset of at least one link-incidence set \(I_e\). The remaining combinatorial task is to bound the total connected collection of such subsets by \(K_8^r\), using the row-incidence constraint
\[
\sum_e |I_e|=\sum_i|X_i|\le8r,
\tag{16.6}
\]
while preserving the maximum-tree product. A naive count of all subsets of all \(I_e\) is not acceptable: a single link can have \(|I_e|=r\), and its power set already has \(2^r\) members. The link's entire quasi-factorization series must be summed as one object before counting interactions between different links.

**Exact reduction:** (16.1)–(16.3). **One-link input:** (16.4). **Still open:** the analytic one-link quasi-factorization majorant (16.5), the connected-subset resummation with \(K_8^r\) growth, and the resulting all-orders maximum-tree bound for products. This is the cancellation-preserving target; it does not rely on the superfactorial absolute LS majorant and does not yet prove the desired theorem.
