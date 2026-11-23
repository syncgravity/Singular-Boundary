# PF-I16 Parent-Fiber Exchange Lemma: reverse-mark transition graph and capacity program

**Date:** 2026-11-23  
**Branch:** `research/pf-i16-parent-fiber-exchange-2026-11-23`  
**Base:** `research/pf-i16-direct-mixed-hall-2026-11-18` at `72c7b0fdebd488a9a084667b8fe7ab2b4e464d65`  
**Status:** proof program / proposed lemma; no all-orders exchange theorem is claimed.

## 0. Purpose and proof boundary

This note records the attempt to replace matching-cut capacity by reverse-mark, parent-fiber, and transition capacity, and advances the next proof obligation: a Parent-Fiber Exchange Lemma.

The target remains the all-orders multivalued-parent Hall inequality for the source-target relation (R_n), followed by the weighted one-link inequality. Finite positive evidence at (n=6,8,10) is not an all-orders proof. The present work does not close Hall, the weighted inequality, the helical bridge, or any Yang--Mills mass-gap gate.

The motivating change is substantive: a linear cut profile records endpoint crossing counts but not the branching information of an overlap tree. The six-port endpoint-path counterexample already shows that a particular endpoint-union construction cannot dominate all cut costs. The proposed replacement is to retain the richer reverse-mark lift and its parent projections, and to study how competing parent fibers can exchange target capacity.

## 1. Authenticated source-side definitions

A source is (x=(M,\tau)), with (M) a perfect matching of ordered ports and (\tau) a spanning tree of its interval-overlap graph. For every eligible non-root leaf interval (J\in L_0(\tau)), deleting (J) and its two endpoints and order-compressing gives a parent source
[
p=\pi_J(x).
]

For a parent source (p), let (C_{\rm can}(p)) be the canonical-leaf-last parent target neighborhood. For a child source (x), the retained multivalued neighborhood is
[
R_n(x)=\bigcup_{J\in L_0(\tau_x)}
\{T:T\text{ is a }J\text{-last guarded output of }x,P_J(T)\in C_{\rm can}(\pi_J(x))\}.
]
Here (P_J(T)) is obtained by the unique inverse of the final guarded switch at the fixed mark (J), followed by deletion/compression of (J).

For each parent-leaf pair (F=(p,J)), define its source fiber and target neighborhood by
[
X(F)=\{x:\pi_J(x)=p\},\qquad N(F)=\bigcup_{x\in X(F)}R_{p,J}(x).
]
The fixed-((p,J)) row-equality result says this target neighborhood is independent of the particular child source in (X(F)). Define split demand
[
\delta(F)=\sum_{x\in X(F)}\frac1{d(x)},\qquad d(x)=|L_0(\tau_x)|.
]
Every source contributes total demand one across its eligible leaves.

The sufficient quotient Hall target is
[
\left|\bigcup_{F\in S}N(F)\right|\ge\sum_{F\in S}\delta(F)
\quad\text{for every fiber family }S. \tag{QH}
]
Equivalently, its weighted max-dual is
[
\sum_F\delta(F)z_F
\le\sum_T\max_{F:T\in N(F)}z_F
\quad(z_F\ge0). \tag{QH*}
]
A fractional transport \(\lambda(F,T)\ge0\) satisfying
[
\sum_{T\in N(F)}\lambda(F,T)=\delta(F),\qquad
\sum_{F:T\in N(F)}\lambda(F,T)\le1
\]
is sufficient for (QH), and hence for source-level Hall.

## 2. What is already established locally

For fixed (F=(p,J)), the fixed-mark inverse is unique. For distinct parent targets (P\ne P'\) at fixed (J), their lift sets are disjoint:
[
L_J(P)\cap L_J(P')=\varnothing.
]
For each (P\in C_{\rm can}(p)), there are at least two guarded (J)-last lifts. Hence
[
|N(F)|\ge 2|C_{\rm can}(p)|\ge 2^{s-1}
\ge s-1\ge |X(F)|
]
for a child with (s) matching intervals, under the recorded fiber hypotheses.

This proves local expansion for one fixed parent/deleted-interval fiber. It does not control collisions between different (J)'s or different parent sources. The uniform row transport
[
\lambda(F,T)=\delta(F)/|N(F)|
\]
is not sufficient: its exact rational target columns overload at the recorded finite orders. That failure rejects uniform allocation, not (QH) or nonuniform transport.

## 3. Reverse-mark incidence data: retain all three identities

For a retained target (T), the source audit defines a reverse mark (J\in\mathcal J(T)) and its unique projected parent target (P_J(T)). For the capacity problem, the incidence record must retain
[
v=(p,J,P,T),
\qquad P=P_J(T),\quad P\in C_{\rm can}(p).
]

Do not collapse the three projections
[
(p,J,P,T)\mapsto(p,J),\qquad
(p,J,P,T)\mapsto P,\qquad
(p,J,P,T)\mapsto T.
]
Different parent sources can contribute distinct demand even when some lower-level data coincide. Fixed-mark inverse uniqueness is not a uniqueness theorem across different marks.

The basic bipartite incidence graph is
[
B_n=(\mathcal F_n\sqcup\mathcal Y_n,E_n),
\qquad (F,T)\in E_n\iff T\in N(F),
]
where \(\mathcal F_n\) is the set of parent-leaf fibers and \(\mathcal Y_n\) the target trees. The exchange problem is a capacity-constrained fractional matching problem on this graph.

## 4. Certified reverse-mark transition relation

A transition must be witnessed by a common source, not inferred merely because two marks occur on the same target.

Let (x=(M,\tau)) have two distinct eligible non-root leaves (J,K) for which the simultaneous deletion is defined. Put
[
p=\pi_J(x),\quad q=\pi_K(x),\quad
r=\pi_K(p)=\pi_J(q).
]
For a target (T) retained through both projections, write
[
P=P_J(T),\qquad Q=P_K(T).
]
When both guarded reverse operations survive in the opposite order, the source-side deletion diamond gives the common double inverse
[
U=P_K(P_J(T))=P_J(P_K(T)).
]
The authenticated conclusion is (U\in C(r)), the ordinary common-parent neighborhood.

**Do not replace (C(r)) by (C_{\rm can}(r)).** The stronger canonical-parent implication is false at (n=10), including distinct-parent examples. The explicit audit records (2{,}906) distinct-parent source diamonds and (286{,}440) failures of the proposed canonical common-parent membership among the common-target incidences. This counterexample does not invalidate the ordinary common-parent diamond.

Define a witnessed transition between incidence states
[
(p,J,P,T)\longleftrightarrow(q,K,Q,T)
]
only when the same source (x), both eligible leaves, both retained inverse records, and the common double inverse (U\in C(r)) are supplied as a certificate. Store the witness tuple ((x,J,K,U)) on the transition.

This graph, denoted \(\Gamma_T\) when restricted to one target (T), records certified coexistence and deletion-diamond compatibility of reverse marks. It is not yet a capacity theorem.

### Critical limitation

An edge of \(\Gamma_T\) connects two incidences at the **same target**. By itself it does not move assigned mass from target (T) to a different target (T'). Therefore connectivity of \(\Gamma_T\) alone cannot prove (QH). A proof must additionally construct a target-changing exchange operation, or a sequence of alternating paths in the bipartite graph (B_n), whose local switches are certified by the reverse-mark diamonds.

This distinction corrects an over-strong reading of the previous proposal: same-target deletion-diamond edges are witness structure, not automatically augmenting edges.

## 5. Parent-Fiber Exchange Lemma: precise target

The following is the desired intermediate theorem, stated in a form that would imply (QH).

**Parent-Fiber Exchange Lemma (PFEL), proposed.** For every even order (n), there is a deterministic or canonically specified fractional transport (\lambda_n(F,T)) on (B_n) such that:

1. **Fiber conservation:** \(\sum_{T\in N(F)}\lambda_n(F,T)=\delta(F)\) for every fiber (F).
2. **Unit target capacity:** \(\sum_{F:T\in N(F)}\lambda_n(F,T)\le1\) for every target (T).
3. **Mark-resolved support:** every positive assignment carries at least one exact reverse-mark witness ((p,J,P,T)).
4. **Exchange locality:** whenever the construction changes an assignment along an alternating path or cycle, each local reroute is certified by a guarded switch and a source deletion diamond; the common grandparent target is required only to lie in (C(r)), not (C_{\rm can}(r)).
5. **Multiplicity preservation:** parent-source identity, deleted-mark identity, and projected-parent-target identity remain separately recorded throughout; no unsupported quotient identifies different fibers.
6. **Order-uniform rule:** the construction and its capacity proof use constants/rules independent of (n), and do not depend on a computed maximum matching or a finite-order congestion outcome.

Items 1--2 imply (QH) and source-level Hall. Items 3--6 are the structural content sought; they are not needed for the abstract max-flow equivalence, but are needed for a proof that explains the finite allocations and can be extended to all orders.

A stronger *helical* refinement would additionally order or orient the certified transitions by a source-derived map into the Penrose--Fibonacci complementary-space geometry. That is a separate later gate.

## 6. Candidate exchange mechanism: what must actually be proved

A valid augmenting operation must have the following form.

Start with a feasible partial transport. A fiber (F_0) has unsent demand, or a target (T_0) is saturated. An alternating path in (B_n) has the schematic form
[
F_0-T_0-F_1-T_1-\cdots-F_k-T_k,
]
where each \(F_iT_i\) is an eligible incidence and each backward step releases mass from an already-used fiber-target arc. The path is useful only if the final target (T_k) has spare capacity and the net update preserves every fiber demand and every target capacity.

The reverse-mark transition certificates should constrain which such alternating paths are allowed. In particular, a proposed local reroute must explicitly specify:

- the two fiber incidences before the move;
- the source(s) and leaf marks witnessing them;
- the inverse projected parent targets;
- the guarded forward switch producing the replacement target;
- the exact reason the replacement remains in the relevant fiber neighborhood;
- the net change in all affected fiber and target loads.

The source deletion diamond supplies a common grandparent (U), but it does not yet supply the replacement target (T') or prove that (T'\in N(F')) for the required fiber. That is the central missing local exchange calculation.

## 7. Finite evidence and negative controls

### n=10 nonuniform split-demand flow

The successful exact certificate records:
- 31,744 sources and 21,280 parent-leaf fibers;
- 95,864 eligible target trees;
- 49,584 positive fiber-target arcs;
- total demand 31,744;
- scaled maximum flow 380,928 at scale 12;
- 32,414 used targets, all with load at most one after scaling;
- 31,040 used targets saturated, 1,374 partially loaded;
- at most five fiber owners per used target in this particular allocation.

The allocation is nonuniform and depends on the finite max-flow construction/order. The replay verifies the exported certificate against the canonical enumeration and switch/compression primitives, independently of the flow algorithm and serialization; it is not a wholly independent implementation of the relation. The histogram is diagnostic only and is not an all-orders bound.

### Rejected shortcuts to preserve

- A fixed canonical child leaf fails at (n=10), with deficiency 92.
- Uniform split-demand transport overloads target columns; this does not disprove nonuniform transport.
- Equal reciprocal reverse-degree splitting is rejected at (n=8,10).
- The retained-grandparent sibling rerouting shortcut fails at the four-interval parent.
- The implication from distinct parent sources to canonical common-parent membership is false at (n=10).
- The terminal-target-access strengthening fails at (n=6,8,10); it is separate from full split-demand Hall.
- The six-port endpoint-union cost-domination construction fails for the nested three-interval star example; this is not a counterexample to (QH).

These obstructions are candidate-specific. None disproves the full multivalued Hall relation.

## 8. First exact research task: discover a target-changing exchange square

The next computation should not merely count connected components of \(\Gamma_T\). It should enumerate candidate exchange squares and test whether the guarded switch system supplies the missing target-changing move.

For every finite source (x) and pair of eligible leaves (J,K):

1. Enumerate targets (T) retained through both marks and verify the two inverse orders and common ordinary parent (U\in C(r)).
2. Enumerate all guarded forward insertions of (J,K) from (U), in both orders, retaining the full local switch records.
3. Compare the resulting target trees (T_{JK}) and (T_{KJ}). Determine whether they are equal, distinct, or related by a bounded sequence of allowed local switches.
4. For each candidate replacement (T'), check exact membership in both relevant fiber neighborhoods by inverse reconstruction—not by cut-load compatibility alone.
5. Record the incidence changes as a signed vector on (B_n); test whether the operation is a circulation that preserves fiber balances and moves load to an unsaturated target.
6. Search first at (n=6,8), then replay the discovered rule at (n=10), including the known canonical-parent counterexamples.

A successful local square would not alone prove PFEL. It would give the elementary move from which an alternating-path or cycle decomposition might be built. If no target-changing square exists, the proof must use longer paths or a different exchange primitive.

## 9. Helical bridge boundary

Paper 3 supplies the kinematic observer paths
[
z_2(\tau)=Ae^{2\pi i p\tau},\qquad p\in\{3/13,5/13,8/13\},
]
and Paper 4 supplies five complementary-space shift/failure-band directions. But the bridge audit found no source-derived map from a PF-I16 reverse mark ((T,J)) to an authenticated \(\mathbb Z^5\) label (m(T,J)). Therefore no helical phase, H1/H2/H3 label, or five-band transition label is assigned in this note. The combinatorial exchange lemma must be developed without arbitrary phase assignment; a geometric/helical refinement can follow only after the map is derived from authenticated source data.

## 10. Deliverables and acceptance criteria

The next research increment is complete only when it supplies:

1. A precise target-changing exchange operation, including source and target witnesses.
2. A proof that the operation preserves eligibility and all fiber/target balances.
3. A termination or path-decomposition argument yielding a feasible transport for every finite order.
4. An order-uniform invariant or counting estimate proving the construction at arbitrary even (n).
5. A separate source-derived geometric map if the helical refinement is pursued.

Until then, PFEL, (QH), all-orders multivalued-\(\pi\) Hall, and the weighted one-link inequality remain **OPEN**.

## 11. Source records

- `research/audits/PF_I16_MULTIVALUED_PI_ALL_ORDERS_PROOF_PROGRAM_2026_11_16.md` — source relation, fixed-fiber expansion, split-demand quotient Hall reduction, and all-orders obligation.
- `research/verification/verify_pf_i16_fixed_parent_leaf_fiber_expansion.py` — exact rational fixed-fiber expansion and uniform quotient-load diagnostic.
- `research/verification/verify_pf_i16_n10_multivalued_pi_projection.py` — finite n=10 multivalued matching verifier.
- `research/audits/PF_I16_N10_SPLIT_DEMAND_FLOW_CERTIFICATE_RESULT_2026_11_18.md` — exact nonuniform n=10 flow certificate and replay boundary.
- `research/audits/PF_I16_DISTINCT_PARENT_DIAMOND_THEOREM_2026_11_18.md` — canonical-parent diamond counterexample and valid ordinary-parent boundary.
- `research/audits/PF_I16_HELICAL_REVERSE_MARK_BRIDGE_AUDIT_2026_11_18.md` — missing PF-I16-to-\(\mathbb Z^5\) map and helical bridge requirements.
- `docs/research/PF_MULTIVALUED_PI_HELICAL_L1_L8_SOURCE_AUDIT_2026-11-19.md` — integrated source/proof boundary.
- `research/verification/verify_pf_i16_two_mark_projection_uniqueness.py` — exact n=6,8 fixed-(P,Q) stable-set census; verified by GitHub Actions run 45240343178.
- `.github/workflows/pf-i16-two-mark-projection-uniqueness.yml` — reproducible CI entry point for the two-mark census.

**Final status:** a corrected reverse-mark transition relation and a precise Parent-Fiber Exchange Lemma target are now recorded. The transition graph is not yet an augmenting mechanism; constructing a target-changing exchange square/path is the immediate open proof step.


## 8A. Refined two-colour incidence complex: the candidate exchange graph

The preceding sections distinguish same-target deletion diamonds from target-changing moves. The next refinement is to put both kinds of move on one graph whose vertices retain source identity.

Let
[
\widehat E_n=\{(x,J,T):J\in L_0(\tau_x),\ T\text{ is retained through }J\}.
]
Each vertex carries the full parent data (p=\pi_J(x)), (P=P_J(T)), and fiber (F=(p,J)). Do not quotient away (x): two different child sources can inhabit the same parent-leaf fiber, and a target shared by two fibers need not be witnessed by one common child source.

Define two kinds of certified edges.

**(S) Sibling-lift edges (target-changing, fixed parent target).** Join ((x,J,T)) to ((x',J,T')) when
[
\pi_J(x)=\pi_J(x')=p,\qquad
P_J(T)=P_J(T')=P\in C_{\rm can}(p),
]
and both (T,T'\in L_J(P)). The fixed-fiber theorem gives
[
|L_J(P)|\ge2,
]
and fixed-mark inverse uniqueness makes the blocks (L_J(P)) disjoint as (P) varies for fixed (J). These edges are genuine target-changing alternatives. They are certified by the common parent target and the exact guarded insertion records.

**(D) Deletion-diamond edges (same target, different marks).** Join ((x,J,T)) to ((x,K,T)) only when the same source (x) has both eligible leaves, both reverse operations are valid and mutually survive, and the common double inverse (U\in C(r)) is recorded. The edge stores ((x,J,K,U)). It is not enough that two unrelated sources have incidences at the same target.

The resulting graph (\mathscr X_n) is bipartite by edge colour: S-edges change the target while retaining a parent-target block; D-edges change the mark/fiber while retaining the target. An alternating path
[
(x_0,J_0,T_0)
\xrightarrow{S}
(x_1,J_1,T_1)
\xrightarrow{D}
(x_1,K_1,T_1)
\xrightarrow{S}\cdots
]
is a candidate witnessed reroute. The source and mark identities make it possible to track the split demand (1/d(x)) at every D-step.

### What this graph does and does not solve

It now contains both ingredients that were missing from the one-target graph \(\Gamma_T\): a certified way to change target (S) and a certified way to change parent mark/fiber (D). This is a better candidate for the exchange mechanism.

But it is not yet sufficient. A shared target may be incident to two fibers through two different child sources (x\ne x'\); there is then no D-edge between those incidences. Such a collision is a **non-diamond collision**. The graph \(\mathscr X_n\) must either:
- prove that every collision relevant to a minimal deficient family can be resolved into a chain of S/D moves, or
- classify non-diamond collisions and show they have a separate capacity surplus.

That is the next genuine structural obstacle. One cannot assert that all target collisions are deletion diamonds.

### Candidate exchange invariant

For a partial assignment, direct every S-edge from the currently occupied incidence toward its alternative target, and every D-edge toward the competing mark incidence at the same target. An augmenting component is a directed alternating path ending at a target with unused capacity. A closed component is a possible obstruction.

The desired lemma can be sharpened to:

> **No-closed-deficient-component criterion.** Every nonempty component of (\mathscr X_n) reachable from unsent fiber demand either reaches a target with positive spare capacity, or admits a local redistribution of split demand that strictly decreases a well-founded source/mark potential.

A plausible potential is lexicographic in (i) parent-source deletion depth, (ii) the ordered pair of deleted interval endpoints after compression, and (iii) the guarded-switch history length. This is only a candidate: the two deletion orders commute at the source level, so deletion depth alone cannot strictly decrease around a diamond. Any well-founded potential must include a target-side switch datum that changes under S-edges and is invariant under the D-square.

No such potential or no-closed-component proof has yet been found.

## 8B. Exact logical reduction for the next proof pass

The standard fractional max-flow network has source-to-fiber capacities \(\delta(F)\), infinite fiber-to-target arcs for \(T\in N(F)\), and target-to-sink capacities one. If a maximum flow is deficient, the residual-reachable fibers (A) and their target neighborhood (N(A)) satisfy
[
\sum_{F\in A}\delta(F)>|N(A)|.
]
Conversely, any such family is a Hall obstruction. Thus proving PFEL is equivalent at the capacity level to excluding every deficient residual-reachable family.

The reverse-mark complex is intended to add structure to this min-cut certificate. The precise next task is:

1. Start from an arbitrary hypothetical deficient family (A) and its target set (B=N(A)).
2. Mark every incidence in (A\times B) with its full source/mark/parent-target witness.
3. Separate collisions into diamond collisions (same source, two marks) and non-diamond collisions (different source witnesses).
4. Use S-edges to expose alternate targets inside each fixed parent-target block.
5. Determine whether the no-closed-deficient-component criterion follows from the local two-lift expansion plus a source/mark potential.
6. If not, extract the smallest finite non-diamond obstruction and identify the missing geometric or combinatorial invariant.

This formulation prevents a circular proof: one may not assume a maximum matching's chosen assignment has a canonical form, and one may not infer a target-changing exchange merely from equality of the two inverse orders.

**Updated status:** the two-colour source-mark incidence complex is now the preferred candidate exchange object. The immediate proof gap is the treatment of non-diamond collisions and the exclusion of closed deficient components.


## 8C. A concrete local exchange-square criterion: preserve the other reverse mark

The two-colour graph suggests a first local lemma that is stronger than mere coexistence of two reverse marks and weaker than a global Hall theorem.

Fix a source (x), two eligible leaves (J,K), and a common retained target (T). Let
[
P=P_J(T)\in C_{\rm can}(p),\qquad
Q=P_K(T)\in C_{\rm can}(q),
]
where (p=\pi_J(x)), (q=\pi_K(x)). Let (R_K(T)) denote the four-vertex reverse footprint for the (K)-inverse: the two endpoints of (K) and the two outside neighbors recovered by the fixed-mark inverse. Mutual survival ensures that this inverse record remains meaningful after the (J)-projection.

Define the (K)-stable (J)-lift set
[
L_J^K(P;Q)=
\{T'\in L_J(P):
K\text{ is still a valid guarded reverse mark of }T'
\text{ and }P_K(T')=Q\}.
]
This set contains (T).

**Separated-support criterion.** If there is an alternative guarded (J)-insertion from (P) whose four-vertex switch support is disjoint from (R_K(T)), then its output (T'\ne T) lies in (L_J^K(P;Q)).

Reason: the switch changes edges only on its four-vertex support. If that support is disjoint from the (K)-reverse footprint, all edges incident to the two (K)-endpoints and the two recovered outside neighbors are unchanged. Thus the same guarded (K)-inverse record survives, with the same compressed parent target (Q). Since (T'\in L_J(P)), it remains in the (J)-fiber as well. This gives the witnessed square
[
(p,J,P,T)\xrightarrow{S}(p,J,P,T')
\xrightarrow{D}(q,K,Q,T').
]

This criterion is exact but conditional. The fixed-fiber theorem only gives at least two (J)-lifts; it does not guarantee that one of the alternative switch supports avoids the (K)-reverse footprint. If the supports meet, a more refined local check is needed: the alternative local pattern may still preserve the specific (K)-incident edges even when the four-vertex supports intersect.

### The first obstruction to classify

Let (E_J(P)) be the set of old edges of the parent target (P) on which a guarded insertion of (J) is allowed. A crude obstruction to separated support is that every (e\in E_J(P)) meets the (K)-reverse footprint after the appropriate port identifications. This is a small vertex-cover condition on the candidate insertion edges.

The sharper obstruction is pattern-sensitive: every allowed local pattern on every candidate edge destroys either the (K)-guard or the exact projected parent target (Q). Call this a **K-blocking footprint**.

The proposed next local theorem is:

> **Two-mark stability lemma (candidate).** For every simultaneous retained pair ((J,K,T)), either (L_J^K(P;Q)) contains an alternative target (T'\ne T), or the (K)-blocking footprint has a rigid, explicitly classifiable form that forces a third eligible mark or a monotone parent-fiber descent.

This dichotomy is not yet proved. It is a sharper, falsifiable step toward PFEL: it asks whether a collision between two fibers can be carried to a second target while preserving the other reverse mark, or whether the failure of that move exposes additional branching elsewhere.

### Exact finite test to run

For (n=6,8), and then (n=10), enumerate every source (x), every pair of distinct eligible non-root leaves (J,K), and every target (T) retained through both marks. For each record:

1. Compute the exact (J)-parent target (P) and (K)-parent target (Q).
2. Enumerate all (J)-last lifts in (L_J(P)), using the actual guarded local switch records.
3. Apply the exact (K)-inverse to each lift and retain those whose compressed target equals (Q).
4. Record \(|L_J^K(P;Q)|\), the candidate old edges, and which local patterns preserve the (K)-footprint.
5. For singleton stable sets, record the blocking footprint and all other eligible leaves of (x).

The output must be an exact census with explicit first witnesses for every exceptional class. A positive census would be finite evidence only; an all-orders proof still needs a structural classification of the blocking configurations.


## 8D. Reproducible exact two-mark projection census (n=6,8)

The stable-set calculation has now been implemented and run in GitHub Actions against the repository's guarded-output, fixed-mark inverse, compression, and source-enumeration routines.

For each source x, each pair of eligible non-root leaves (J,K), and each common retained target T in the J-last and K-last rows, the verifier computes
[
P=P_J(T),\qquad Q=P_K(T).
]
It groups common targets by the ordered pair (P,Q). For each group, its members are exactly the targets in the tested source/pair incidence with both reverse marks valid and both projected parent targets fixed. Thus the group containing T computes the finite stable set L_J^K(P;Q).

**Verified run:** GitHub Actions run [45240343178](https://github.com/syncgravity/Singular-Boundary/actions/runs/45240343178), conclusion SUCCESS, commit `e5380129a451886e990311a83ae9611a0e911fc5`.

| Order | Sources | Eligible leaf pairs | Common-target incidences | (P,Q)-groups | Stable-group histogram | Maximum stable-set size |
|---|---:|---:|---:|---:|---|---:|
| n=6 | 22 | 8 | 37 | 37 | {1: 37} | 1 |
| n=8 | 608 | 490 | 15,533 | 15,533 | {1: 15,533} | 1 |

The run output is exact and finite. Every tested stable set is a singleton:
[
L_J^K(P;Q)=\{T\}
]
for all simultaneous retained two-mark incidences at n=6 and n=8. Therefore the proposed local exchange square cannot change T while preserving both P and Q at these orders.

The verifier is `research/verification/verify_pf_i16_two_mark_projection_uniqueness.py`; the workflow is `.github/workflows/pf-i16-two-mark-projection-uniqueness.yml`. The first workflow attempt failed because the verifier passed the set returned by `inverse_last_switch` directly to `compress_tree`; this was corrected by extracting its unique tree witness. The successful run above is on the corrected commit.

**Scope:** this calculation does not enumerate n=10. It also does not prove that no target-changing move exists if one allows the K projection Q to change, nor does it construct a capacity-preserving reroute. The earlier unverified n=10 counts and any claim of an n=10 singleton census are not part of this authenticated result.

## 8E. Correction: separated support preserves K-inverse validity, not the full K projection

The separated-support criterion in Section 8C is withdrawn in its original form. A J-switch whose support is disjoint from the K reverse footprint can leave the local K inverse pattern valid. But this does **not** imply that the compressed K-parent target Q is unchanged: edges modified by the J-switch may be disjoint from the K footprint and still survive deletion of K, so they remain visible in the K-parent tree.

Accordingly, the implication
[
\operatorname{supp}(s_J)\cap R_K(T)=\varnothing
\quad\Longrightarrow\quad
P_K(T')=P_K(T)
]
is not established and must not be used. The valid conclusion from footprint disjointness is only preservation of the relevant local K inverse data, subject to the guard conditions; exact K-row membership and the value of P_K(T') must be checked by applying the full inverse/compression routine.

This correction narrows the next target. The fixed-(P,Q) two-mark exchange square is rigid at n=6,8. The next computation should instead retain projection-shifting transitions Q to Q' (with Q' allowed to differ), record exact forward switch witnesses and both inverse projections, and then test whether those transitions support a circulation or fractional reroute on the fiber-target incidence graph. No such capacity argument is yet proved.

**Updated status:** the n=6,8 fixed-(P,Q) rigidity census is verified. The two-mark stability dichotomy, projection-shifting transition theorem, Parent-Fiber Exchange Lemma, quotient Hall, all-orders multivalued-π Hall theorem, and WI remain **OPEN**.
