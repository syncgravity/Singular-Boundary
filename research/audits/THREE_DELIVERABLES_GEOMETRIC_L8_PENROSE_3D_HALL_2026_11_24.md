# Three coordinated proof deliverables: source obstruction and exact closure obligations

**Date:** 2026-11-24  
**Branch:** `research/three-deliverable-proof-program-2026-11-24`  
**Status:** research-program record; one exact source-level obstruction proved below. No geometric L8, physical 3D regulator, or all-orders Hall theorem is claimed closed.

## Executive disposition

The three requested deliverables are separate mathematical obligations:

1. **Geometric L8:** compare the actual relative collapse maps and prove restriction naturality, not merely equality of terminal inventories or a classification of elementary matching differences.
2. **Source-faithful physical 3D Penrose regulator:** resolve whether the literal Paper 2 assignment admits a three-dimensional equal-time spatial lattice before attempting an SU(2) regulator certification.
3. **All-orders multivalued-π Hall:** lift parent exchange paths coherently to child incidence states and then prove a capacity-preserving transport.

A source-level calculation establishes a sharp obstruction to the literal Paper 2 equal-time spatial lattice. The other two obligations are stated precisely below, with current evidence and next verification tasks.

---

## I. Paper 2 source-coordinate obstruction

### I.1 Source assignment

Paper 2, *The Gravitational Path Integral on the Penrose Lattice: From Z5 to Minkowski Spacetime via Lapidus Complex Dimensions*, §§2.2–3.1, equations (1), (2), and (6)–(7), defines

\[
z_1(m)=\sum_{j=0}^{4}m_j\omega^j,\qquad
z_2(m)=\sum_{j=0}^{4}m_j\omega^{2j},\qquad
\omega=e^{2\pi i/5},
\]
and assigns
\[
x=\Re z_1,\quad y=\Im z_1,\quad
u=\Re z_2,\quad ict=\Im z_2.
\]

Thus the source's equal-time condition on an integer displacement
\(n\in\mathbb Z^5\) is \(\Im z_2(n)=0\).

### I.2 Exact equal-time displacement lemma

**Lemma.** If \(n\in\mathbb Z^5\) and \(\Im z_2(n)=0\), then
\[
n=(a,b,c,c,b)
\]
for integers \(a,b,c\), and \(z_1(n)\in\mathbb R\). In particular, every equal-time integer displacement has \(\Delta y=0\).

**Proof.** Since
\[
\Im z_2(n)
=\sin(4\pi/5)(n_1-n_4)+\sin(8\pi/5)(n_2-n_3)
\]
and \(\sin(8\pi/5)=-\sin(2\pi/5)\), while
\(\sin(4\pi/5)=\sin(\pi/5)\) and
\(\sin(2\pi/5)=\varphi\sin(\pi/5)\), the equal-time equation is
\[
(n_1-n_4)-\varphi(n_2-n_3)=0.
\]
The two differences are integers and \(\varphi\) is irrational, so both vanish:
\(n_1=n_4\), \(n_2=n_3\). Hence \(n=(a,b,c,c,b)\). Then
\[
z_1(n)=a+2b\cos(2\pi/5)+2c\cos(4\pi/5)\in\mathbb R.
\]
Therefore \(\Delta y=0\). \(\square\)

The conclusion is unchanged by removing the trivial constant-coordinate direction: that direction has zero \(z_1\) and \(z_2\) coordinates, so it does not alter the equal-time condition or the conclusion.

### I.3 Certification consequence and boundary

Under the literal coordinate assignment, the integer lattice does **not** supply a three-dimensional equal-time spatial displacement lattice. Its equal-time integer displacements project into the one-dimensional real axis of the \(z_1\) plane, together with the real \(z_2\) coordinate.

This obstructs certifying a three-dimensional spatial Penrose regulator by simply declaring the Paper 2 \(u\)-coordinate to be a third spatial direction while retaining \(\Im z_2=ict\) as time.

This is **not** a no-go theorem for every spacetime complex or every revised 3D construction. A time-changing coupled spacetime graph could be studied, but it would need an explicit causal/transfer structure, a spatial-slice definition, and a physical action. Alternatively, changing the time/spatial decomposition is a model revision and must be labelled as such.

### I.4 Immediate source-faithful tests

1. Enumerate the five source edge displacements \(e_j\) and tabulate \((\Delta x,\Delta y,\Delta u,\Delta ct)\), including signs and exact algebraic values.
2. Determine whether the source's accepted Penrose complex uses only these edges or introduces additional composite displacements that could change the equal-time graph. Any such additions must be source-prescribed, not selected after seeing the obstruction.
3. If the intended object is a coupled spacetime graph, specify a time orientation, a transfer relation, and a positive/elliptic operator or Lorentzian action on it. The current coordinate assignment alone does not provide those.
4. Keep the 2+1D Stage26 SU(2) simulation and cubic 3D control as distinct models; neither certifies this missing source-faithful 3D spatial regulator.

---

## II. Geometric L8: map-level relative confluence

### II.1 What the finite evidence establishes

The current four-support records and verifiers establish finite facts about relative collapse *pair sequences*:

- differing elementary-pair sets have a connected alternating-cycle symmetric difference in the audited finite family;
- selected four-cell cases admit a common prefix / dependency-closed suffix factorization;
- the third-mark restriction verifier checks that the recorded operations remain inside the restricted support and that both restricted paths replay to the root support;
- eight audited cases retain order-sensitive common-extra suffix order.

The verifier itself explicitly records that this is finite restriction naturality only and sets `general_restriction_naturality_proved=False` and `geometric_L8_closed=False`.

### II.2 Required theorem statement

Let \(K\) be a finite accepted-face simplicial complex with retained subcomplex \(A\). Let
\[
\mathcal C=(c_1,\ldots,c_r),\qquad
\mathcal C'=(c'_1,\ldots,c'_s)
\]
be two valid relative elementary-collapse sequences from \(K\) to \(A\). Write
\[
R_{\mathcal C}:|K|\to |A|,\qquad
R_{\mathcal C'}:|K|\to |A|
\]
for the actual composite collapse retractions, not merely their lists of free face/coface pairs.

**Relative geometric L8 target.** For every source-legal restriction \(K'\subseteq K\) for which both collapse sequences restrict to valid sequences ending at \(A'=A\cap K'\), construct a homotopy
\[
H:|K|\times[0,1]\to |A|
\]
between the two induced retractions, relative to \(|A|\), and a restricted homotopy \(H'\) such that the restriction square commutes:
\[
H|_{|K'|\times[0,1]}=H'.
\]
The construction must be compatible with composition of successive source-legal restrictions. If the correct target is a homotopy-coherent diagram rather than strict equality, specify the coherence data and prove its compatibility.

### II.3 Why the present certificates do not imply it

The existing verifier replays combinatorial free-pair operations and checks terminal inventories. It does not yet construct the piecewise-linear collapse retraction for each elementary step, compare the composite maps, or construct a homotopy between them. A common intermediate inventory and valid adjacent commutations of pair operations are useful ingredients, but do not themselves provide the required map-level comparison.

### II.4 Next proof task

For the 64 graph-5 source-mark-[1,2] restriction rows, construct explicit elementary collapse maps and their restriction maps. First handle the 56 rows whose common-extra suffix orders agree; then isolate the eight order-sensitive rows and produce either:
- an explicit local homotopy-coherent switch valid under restriction, or
- a counterexample showing that the proposed strict naturality target is too strong and must be replaced by a precisely stated weaker coherent version.

Only after this finite map-level result should the local switch be abstracted to arbitrary alternating cycles and arbitrary source-legal restrictions. The order-eight census alone does not establish that abstraction.

Primary source records:
- `research/scripts/verify_pf_i16_four_cell_switch_restriction_naturality.py`
- `research/scripts/verify_pf_i16_four_cell_switch_factorization.py`
- `research/audits/PF_I16_SOURCE_LABELLED_FOUR_SUPPORT_RESTRICTION_AUDIT_2026_11_20.md`

---

## III. All-orders multivalued-π Hall: coherent path lifting plus capacity transport

### III.1 Existing parent-projection result

The current parent-fiber branch reports:
- 4,881 residual order-eight collision pairs project to connected order-six parent-block pairs;
- 155 distinct order-six parent-block endpoint pairs;
- all are connected in the order-six S/C/D graph;
- maximum shortest parent path length is six.

This is connectivity **after projection**. It is not an order-eight path-lifting theorem.

### III.2 Required path-lifting statement

Let \(G_{n-2}\) be the parent exchange graph and \(G_n\) the child incidence/exchange graph. Let
\[
p:V(G_n)\to V(G_{n-2})
\]
be the canonical parent projection on the audited states.

**Parent-fiber path-lifting target.** For every parent edge \(u\leftrightarrow v\) occurring in the recursive projection paths, and every child state \(x\) over \(u\) in the relevant marked fiber, construct a child edge or a uniformly bounded child path from \(x\) to a state over \(v\), preserving:
1. the exact outer deleted mark;
2. the child source identity and permitted child-source extension;
3. exact target-neighborhood membership;
4. both guarded inverse conditions on D-edges;
5. the ordinary common-parent witness;
6. the compatibility needed to concatenate successive lifts at the same child state.

The lift must be proved for each edge type (S, C, D) under its actual definition. It is not enough to lift an edge from some child over \(u\) to some child over \(v\): the endpoint must match the preceding lift, or a separately proved within-fiber connector must join them.

### III.3 Capacity-preserving transport remains a second theorem

Even coherent connectivity does not prove Hall. For every finite fiber family \(\mathcal F\), the needed result is a nonnegative transport
\[
\lambda(F,T)\ge0,\qquad
\sum_{T\in N(F)}\lambda(F,T)=\delta(F),\qquad
\sum_{F:T\in N(F)}\lambda(F,T)\le1.
\]
This implies the reverse-mark-sensitive quotient Hall inequality
\[
\left|\bigcup_{F\in S}N(F)\right|
\ge \sum_{F\in S}\delta(F)
\quad\text{for every }S\subseteq\mathcal F.
\]

The transport must be constructed from the original relation and its exact neighborhoods. It cannot assume canonical-parent membership, since that stronger property has a finite counterexample. It cannot infer capacity transfer from same-target diamonds or graph connectivity alone.

### III.4 Next proof task

1. Export every parent path edge with its endpoint states, edge type, mark data, inverse witnesses, and target witnesses.
2. For each edge, enumerate all compatible child lifts and record the exact child endpoint state. Do not discard source identity.
3. Test concatenation constraints at consecutive edges. A path is liftable only if the endpoint state of one lifted edge is the starting state of the next, or a certified within-fiber connector exists.
4. If any edge has no lift, retain it as a counterexample to the proposed lifting lemma and refine the lemma's hypotheses; do not silently remove it from the path family.
5. After path lifting, formulate a separate local rerouting rule that moves fractional demand across target-changing edges while preserving every target capacity. Prove a uniform potential/termination bound and derive the transport above.
6. Only then pass from finite order to all orders by induction or a uniform decomposition theorem.

Primary source record:
- `research/audits/PF_I16_RECURSIVE_PARENT_PROJECTION_PATHS_2026_11_24.md`
- `research/audits/PF_I16_PARENT_FIBER_EXCHANGE_LEMMA_PROGRAM_2026_11_23.md`

---

## IV. Certification gates and model separation

| Deliverable | Current status | What closes the gate |
|---|---|---|
| Geometric L8 | Open | Explicit collapse-map comparisons and restriction-compatible homotopy/coherence, then an all-orders local decomposition |
| Source-faithful physical 3D Penrose regulator | Obstructed under literal Paper 2 equal-time assignment | Source-prescribed resolution of the missing equal-time spatial dimension, followed by geometry, operator, action, and refinement certification |
| All-orders multivalued-π Hall | Open | Coherent child path lifting plus a capacity-preserving transport proving the quotient Hall inequality |

The following remain separate and must not be used as substitutes for one another:
- accepted-face geometric L8;
- abstract multivalued-π Hall;
- Paper 2's coupled-Z5 spacetime proposal;
- the Stage26 2+1D SU(2) simulation;
- the cubic 3D SU(2) control;
- the R3-IR interacting-vacuum and mass-gap program.

No finite computation, workflow pass, or graph-connectivity result by itself certifies an all-orders theorem or a physical continuum regulator.

## V. No promotion or destructive reconciliation

This record does not overwrite earlier finite results, counterexamples, or failed approaches. In particular:
- the eight order-sensitive L8 cases remain explicit;
- the parent-projection connectivity result remains a projection-level result;
- the Paper 2 coordinate obstruction is conditional on retaining its literal equal-time assignment;
- no alternative 3D geometry is silently substituted;
- no claim-ID collision is resolved by numeric ID alone.

**No theorem is marked closed by this record.**
