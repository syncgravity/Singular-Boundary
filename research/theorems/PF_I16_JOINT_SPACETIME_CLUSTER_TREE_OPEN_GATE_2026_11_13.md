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
Equation (3.2) is a proposed target, not an established inequality. The proof must determine whether it holds with \(C_{\rm st}=2\), with a larger explicit constant, or only after replacing the exponential by a weaker influence kernel.

The relevant structure is the product decomposition of the reference path law over links. Each insertion depends on at most eight link paths. A viable proof should exploit that independence before taking absolute values: decompose local insertions into link-coordinate components, express the joint cumulant as a sum of connected coordinate-incidence diagrams, and extract one spanning tree whose edges each correspond to a shared link and carry the associated temporal mixing factor. The tensor/contraction norm used in this step must be controlled by the stated local insertion norm; an uncontrolled \(\ell^1\) Peter–Weyl expansion is not acceptable.

The first concrete proof milestones are:
1. establish the two-observable shared-link covariance bound exactly;
2. prove the three-observable tree inequality for every possible support-overlap graph;
3. prove the four-observable version needed for the exact third- and fourth-order responses in the two-cut identity;
4. identify the induction that gives the all-orders bound with explicit \(C_{\rm st}\).

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

Do not enlarge the local-activity estimates yet. Work at fixed \(m=3\) and \(m=4\) under the product reference path law. Use the tensor product over independent link paths to derive the support-sensitive cumulant decomposition, retaining the complete coordinate-incidence structure. The desired output is an explicit tree formula with constants, or a concrete counterexample to the proposed bond (3.2). Only after this calculation should the all-orders induction and KP constants be attempted.

**No quantum connected-resolvent/tree theorem or interacting-vacuum gap is claimed in this record.**
