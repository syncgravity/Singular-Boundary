# PF-I16 — Proposed Hall-to-Penrose–Fibonacci labelled incidence lift

**Date:** 18 November 2026  
**Branch:** `research/pf-i16-z5-incidence-lift-2026-11-18`  
**Status:** definition and research program proposed; no lift constructed or existence theorem proved.  
**Purpose:** replace the unsupported search for a historical port-to-ℤ^5 association with an explicit, independently testable correspondence.

## 1. Separation of structures

For (n=2s), the Hall source is (x=(M,\tau)), where (M) is a perfect matching of the ordered port set (P_n=\{p_1,\ldots,p_{2s}\}) and \(\tau\) is a spanning tree of the interval-overlap graph. The source includes port order, matched pairs, intervals, interval endpoints, overlap incidences, and eligible non-root leaf deletions. A reverse mark (J) selects an allowed parent projection (P_J(x)). The relation remains genuinely multivalued: no canonical leaf selector is introduced.

The Penrose–Fibonacci target is the accepted labelled face complex. Its vertices carry labels (K\in\mathbb Z^5); elementary directed edges have increments \(\pm e_j\); rhombi carry a lower-corner label and a direction pair \((j,k)\). With the source phason \(\gamma\), vertex acceptance uses the four height windows
\[
W_h=\left\{\sum_{j=0}^4u_je_j^\perp:0\leq u_j\leq1,\ \sum_j u_j=h\right\},\quad h=1,2,3,4,
\]
and face acceptance uses the stricter face triangles
\[
T_{jk,h}=\left\{\sum_{f\notin\{j,k\}}u_fe_f^\perp:
0\leq u_f\leq1,\ \sum_{f\notin\{j,k\}}u_f=h\right\},\quad h=1,2.
\]
The face criterion, not vertex acceptance alone, certifies a rhombus. The source projections are
\[
z_1(K)=\sum_{j=0}^4K_j\zeta^j,\qquad
z_2(K)=\sum_{j=0}^4K_j\zeta^{2j},\qquad \zeta=e^{2\pi i/5}.
\]
No physical-time interpretation is assumed for the second plane.

## 2. Marked incidence lift

A lift at order (n) is a triple
\[
\mathfrak L_n=(\Phi_n,\epsilon_n,\kappa_n).
\]
Here:

* \(\Phi_n:P_n\to V_{\rm acc}\) maps ports to accepted \(\mathbb Z^5\)-labelled vertices.
* \(\epsilon_n\) assigns each matched pair an oriented accepted elementary edge and its unique direction label \(j\in\{0,1,2,3,4\}\).
* \(\kappa_n\) assigns each Hall interval a connected, face-supported subcomplex of the accepted rhombus complex, with an ordered boundary trace.

An interval is **not** assumed to be one rhombus. Its support may contain multiple faces. Distinct reverse marks remain distinct marked states even when their parent projections coincide.

## 3. Lift axioms

**L1 — Port injectivity.** Distinct Hall ports have distinct accepted vertex images.

**L2 — Matching realization.** For each \(\{p,q\}\in M\), the images satisfy \(\Phi_n(q)-\Phi_n(p)=\pm e_j\) for exactly one direction \(j\).

**L3 — Acceptance.** Every port image satisfies the appropriate \(W_h\) test. Every face used by \(\kappa_n\) satisfies its corresponding \(T_{jk,h}\) test. No face is inferred from vertex acceptance alone.

**L4 — Interval realization.** Each \(\kappa_n(I)\) is a connected face-supported subcomplex with an ordered boundary trace compatible with the order of ports in (I).

**L5 — Overlap witnesses.** Every edge of the interval-overlap graph has an explicit shared-incidence witness between the corresponding supports. Non-overlapping intervals are not silently identified as sharing a boundary. Initially record the exact intersection type (vertex, edge path, or face); do not assume equality of all intersections until tested.

**L6 — Parent naturality.** For every eligible reverse mark (J), the lift of (P_J(x)) agrees with the target operation that removes the support exclusive to the deleted leaf interval and performs only explicitly certified collapses. All retained port and interval incidences are preserved. If no such target operation exists, that mark is not geometrically realized by this candidate lift.

**L7 — Order and orientation.** Port order, interval boundary order, and directed edge orientations are retained as data.

**L8 — Hall independence.** The lift definition and its construction use no Hall deficiency, target congestion, allocation, or desired matching outcome. The lift must be frozen before testing the Hall inequality.

These are proposed axioms, not established properties. In particular, L1 and L2 may prove too rigid; if so, weaken them only by stating the precise quotient or multiplicity structure required, not by silently allowing collisions.

## 4. Reverse-mark observer coordinate

For a lifted parent and reverse mark (J), let \(\mathcal F_J(x)\) be the rhombi in the support of the lifted parent. Let \(c_\perp(f)\) be the arithmetic mean of the four (z_2)-coordinates of the face's corner labels. With a root-reference support fixed as part of the lift, define
\[
r_\perp(J;x)=\frac1{|\mathcal F_J(x)|}\sum_{f\in\mathcal F_J(x)}c_\perp(f),
\qquad
\Psi_J(x)=r_\perp(J;x)-r_\perp(J_0;x).
\]
When \(\Psi_J(x)\ne0\), set \(\theta_J(x)=\arg\Psi_J(x)\). When it vanishes, phase is undefined and the degeneracy is recorded. Do not regularize it away. The root reference and the uniform face measure are part of this candidate definition and must be sensitivity-tested against other intrinsic measures.

Only after the lift is constructed independently may the observer families (p=3/13,5/13,8/13) be evaluated on the derived perpendicular-space data. The helical observer is a candidate geometric ordering principle, not a port-index assignment or an input to the lift solver.

## 5. Construction strategy: solve for all admissible lifts

Do not choose one convenient embedding and then report it as canonical. Define
\[
\mathscr L_n(x)=\{\mathfrak L_n:\text{L1--L8 hold for }x\}.
\]
First determine whether \(\mathscr L_n(x)\) is nonempty. If it is nonempty, retain the admissible-lift set (or a certified representation of it), and test uniqueness, symmetry, and parent compatibility. A deterministic tie-break may be used for reproducible computation only after the full admissible set and the tie-break's non-invariance are disclosed.

The finite solver should be a constraint problem with variables for port labels, edge directions/orientations, face labels, and interval supports. Constraints come only from the Hall source combinatorics and the independently defined accepted ℤ^5 face complex. No objective function may contain Hall loads or phase-fit terms.

## 6. Validation ladder

1. **Unit geometry:** independently verify the (W_h) vertex and (T_{jk,h}) face acceptance of every assigned label; verify every matched pair is a genuine accepted basis edge.
2. **Smallest nontrivial Hall order:** construct or refute a lift for (n=4), then (n=6). Report all admissible lifts if enumerable, otherwise certified counts/bounds.
3. **Parent naturality:** for every eligible (J), compare lift-then-delete with delete-then-lift. Preserve multiple marks with coincident parents.
4. **Growth:** repeat at (n=8,10); test whether restrictions of higher-order lifts agree with lower-order lifts on retained substructures.
5. **Reflection and phason:** distinguish a fixed-phason symmetry from the hull-pairing transformation ((K,\gamma)\mapsto(\mathbf1-K,-\gamma)). Do not call central inversion a physical time reflection.
6. **Observer tests:** only after steps 1–5, calculate phase coverage, ordered transitions, H1/H2/H3 behavior, and degeneracies. Compare against unmarked, reflected, shuffled, and phase-blind controls.
7. **Hall relevance:** only after the lift is frozen, test whether admissible reverse-mark transitions support a capacity-preserving rerouting or split-demand decomposition. A geometric correlation alone does not prove blockwise Hall.

## 7. Failure conditions and interpretation

A failed sufficient axiom set is not a Hall counterexample. If no lift exists, identify the first incompatible incidence requirement and decide whether it exposes a genuine mismatch or an unnecessarily rigid definition. Any relaxation must remain independent of Hall loads and preserve a meaningful source interpretation.

An abstract incidence lift, if found, would support a combinatorial observer. It would not by itself establish that the perpendicular plane is physical time, that the Hall reverse mark is a temporal reversal, or that the dissertation's physical observer interpretation transfers to the Hall theorem.

## 8. Immediate implementation target

Implement an independent accepted-face-complex enumerator/interface and a finite constraint checker. Start with (n=4) and (n=6), then (n=8,10). The first deliverable is not a positive embedding: it is a reproducible feasibility result, with a minimal obstruction certificate when infeasible. Preserve the existing 12-port retained-grandparent sibling-rerouting counterexample as a regression test; do not revive that invalid shortcut.

**Research verdict:** the correspondence is now a precise proposed object with explicit axioms and falsifiable finite tests. Its existence, compatibility across orders, and usefulness for the all-orders Hall theorem remain open.
