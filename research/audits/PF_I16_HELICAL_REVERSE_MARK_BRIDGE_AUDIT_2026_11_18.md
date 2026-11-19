# PF-I16 / helical-observer bridge: reverse-mark audit and test protocol

Date: 2026-11-18

## Status and conclusion

This is a research formulation and source-faithful audit, not a theorem or a claim that the dissertation geometry has already been embedded in the matching-tree relation.

The proposed bridge is plausible only in a qualified sense: the helical observer may supply an ordering of reverse-mark states if a source-derived map from matching-tree data into the dissertation's complementary-space geometry can be constructed. The current repository definitions do not yet supply that map. Consequently, no honest H1/H2/H3-labelled reverse-mark graph or helical capacity statistic can yet be computed from the matching-tree enumerator without adding an arbitrary embedding.

The immediate result is therefore a precise bridge obstruction and a reproducible test specification. It preserves the active Hall problem and identifies the missing mathematical datum.

## 1. Existing Hall-side objects

For a retained target T, define its reverse-mark state set by
\[
\mathcal R(T)=\{v_J=(J,P_J(T)): J\in\mathcal J(T)\},
\]
where J is an eligible non-root leaf interval and P_J(T) is obtained by inverting the final guarded switch at J and deleting/compressing the two endpoints of J.

The current verifier implementation has the needed local inverse primitive:
- `inverse_last_switch(T,J,n)` reconstructs the replaced edge from the two new endpoints;
- it checks that the induced four-vertex tree is one of the guarded local patterns;
- it returns the unique parent port tree;
- `compress_tree` gives P_J(T) on the parent port set.

This is a fixed-mark uniqueness statement. It does not say that different marks J,K have the same parent projection, preserve one another's witnesses, or admit a global exchange.

The all-orders Hall obligation remains the mixed-fiber inequality
\[
\left|\bigcup_{F\in S}N_k(F)\right|\geq\sum_{F\in S}\delta(F)
\quad(S\subseteq\mathcal F_k),
\]
or equivalently its weighted max-dual. The n=6,8,10 split-demand flows are finite positive evidence; they do not provide an all-orders construction.

## 2. Dissertation geometry: source facts versus bridge inference

### Paper 3, §7

The formal observer path is
\[
z_2(\tau)=A e^{2\pi i p\tau},\qquad
p\in\{3/13,5/13,8/13\}.
\]
The paper calls these H1/H2/H3 helical families and gives the conditional m=10 kinematic frequency relation f=10p, hence 3:5:8. Remark 6 characterizes the construction as kinematic rather than a dynamical field-evolution equation. At fixed A, z2 is a circle in the two-real-dimensional complementary plane; a physical 3D helix needs a separately justified longitudinal coordinate and metric.

### Paper 4, §§4–5

The five complementary-space shift directions are
\[
e_j^\perp=R_W(\cos(4\pi j/5),\sin(4\pi j/5)),
\quad j=0,1,2,3,4,
\]
and the failure-band indicator is
\[
b_j(r_\perp)=
\mathbf 1\{r_\perp\in W,\ r_\perp+e_j^\perp\notin W\}.
\]
Paper 4 also gives the complementary-pair identity for the appropriate 144-degree-separated bands. These five labels are geometrically meaningful in the Penrose acceptance-window model.

### What is not yet established

Paper 3 does give the actual complementary projection once an integer lattice vector m=(m_0,...,m_4) in Z^5 is known: z_2(m)=sum_{j=0}^4 m_j omega^{2j}, with omega=exp(2 pi i/5). It also identifies the acceptance window W as the decagonal domain in this z_2-plane. What neither paper supplies is the preceding map from a PF-I16 port, matching interval, overlap-tree vertex, or reverse mark J to such an integer vector m(T,J), or to a physically justified difference of such vectors. The matching-tree verifier enumerates ordered ports and interval overlaps, but the reverse-mark data do not carry a coupled-Z5 lift, phason, or canonical lattice displacement. Thus the candidate map should be written explicitly as Psi_n(T,J)=z_2(m(T,J)) only after m(T,J) has been derived from authenticated model data; the projection formula itself is known, but its PF-I16 input is not.

Therefore the following would be arbitrary at present and must not be used as evidence:
- assigning a band label by J's endpoint index modulo 5;
- identifying an interval midpoint on a unit circle with a Penrose perpendicular-space point;
- assigning H1/H2/H3 phase after looking at which assignment reduces target congestion;
- treating a graph edge in the reverse-mark incidence graph as a physical helical step without a derived geometric transition rule.

## 3. Exact rational-orbit pretest

For integer sampling k=0,...,12, each p=a/13 with a=3,5,8 has exact period 13 and visits all 13 points of the rational phase grid. Since 8 = -5 (mod 13), H2 and H3 visit the same 13-point set in opposite order.

For the m=10 character, the complete 13-sample mean is
\[
\frac1{13}\sum_{k=0}^{12}e^{2\pi i 10ak/13}=0,
\]
because 13 does not divide 10a. Numerically, direct floating-point checks give residual magnitudes of order 6e-16, consistent with exact zero.

Consequences:
1. H2 and H3 cannot be distinguished by an unmarked statistic depending only on the unordered set of sampled phases.
2. A bare discrete phase orbit does not provide three distinct phase supports; the ordering/orientation and an additional field or mark are essential.
3. The five C5 failure-band directions and the 13-site rational orbit are not identified by a single exact phase increment: 3/13, 5/13, and 8/13 are not multiples of 1/5 modulo one. A coupling must come from the actual projection geometry, not an assumed relabelling.

This pretest is a mathematical consequence of the stated rational pitches, not an empirical reconstruction of the dissertation's reported CV measurements.

## 4. Required source-derived bridge map

The first genuine construction task is to recover or define, from the dissertation's original coupled-Z5 model, a map
\[
\Psi_n:\{\text{PF-I16 source/target/reverse-mark data at order }n\}
\longrightarrow W\subset\mathbb R^2.
\]

The map must be specified before Hall loads are inspected and must satisfy all of the following.

**(M1) Provenance.** Each image point must be computed from authenticated Z5 lift/projection data, not from port labels chosen ad hoc.

**(M2) Mark sensitivity.** For a fixed target T, distinct reverse marks J must be allowed to produce distinct points or oriented displacement data. If the map collapses them, the reason must be geometric and explicit.

**(M3) Relabelling covariance.** The map must commute with the actual order-preserving port relabellings used by parent deletion/compression, or provide an explicit transport law.

**(M4) Reflection behavior.** The action induced by reflection of the ordered ports must be stated. This is needed to distinguish a genuine oriented observable from a coordinate convention.

**(M5) Scale and phase.** The amplitude A, origin/phason, phase origin, and any radial rule must come from the source model. Paper 3's constant-A simplification must not be silently replaced by a radial drift.

**(M6) Acceptance-window membership.** The image must lie in W when the failure-band indicators are evaluated. Out-of-window values must be reported, not projected back by an unrecorded repair.

### Source-geometry recovery achieved in the private research Library

The source-side geometry is no longer wholly missing. The private Library contains the original research script `paper6_extend_local.py` (not present in the public repository), whose inspected implementation supplies:
- `make_generic_gamma()`: the five-component generic phason built from fractional parts of j sqrt(2)+j^2 sqrt(3), centered to zero sum;
- `build_penrose_tiling()`: five-integer labels `mi` with the acceptance-layer condition 1 <= sum(mi) <= 4;
- `extract_z5_coordinates()`: z1(mi)=sum mi_j omega^j and z2(mi)=sum mi_j omega^(2j), together with a sample-centroid-centered z2 and its polar angle;
- `build_coupled_z5_laplacian()`: accepted-label neighbors mi±e_j and Fibonacci hopping determined by the integer level.

The companion PF-I9 reconstruction records the four distinct internal windows W_h, h=1,2,3,4, and the exact generic-cell acceptance condition. Thus the source-side projection, phason convention, accepted integer labels, and finite neighbor rule have a concrete implementation to recover and authenticate. This materially advances G0.

It does **not** close G1. The PF-I16 matching-tree source/target/reverse-mark objects still contain ordered port labels and interval data, not one of these accepted five-integer labels. No source document or code found so far specifies an association m(T,J) between a reverse-mark state and a Penrose vertex/edge. The proposed map can now be written more concretely as
\[
\Psi_n(T,J)=z_2(m(T,J))-\overline{z_2},\qquad
\theta_T(J)=\arg\Psi_n(T,J),
\]
with m(T,J) required to be derived from the authentic PF-I16-to-Penrose correspondence, and the correct W_h layer retained. The centroid, gamma, integer-label rule, and five shifts must be taken from the source implementation, not refitted to Hall outcomes.

A likely next data-recovery target is the exact PF-I16/Penrose correspondence (if one exists in the original research archive), including whether a port is a Penrose vertex, a directed basis edge, a boundary label, or only an abstract combinatorial index. If no such correspondence exists, the helical-to-Hall bridge is a new conjectural construction rather than a consequence of the dissertation and must be labelled accordingly.


## 4A. Records-search result: common Z5 substrate found, PF-I16 port map not found

A targeted search of the private research Library and the Hall proof branch located the following source records:

1. **PF-I2 source pentagrid recovery** (`PF_I2_SOURCE_PENTAGRID_GENERATOR_RECOVERY_2026_11_07.md`, with revised companion `PF_I2_REVISED_SOURCE_PENTAGRID_GENERATOR_RECOVERY.md`). This records the source-defined integer labels K in Z5, the physical projection z1(K), the perpendicular projection z2(K), the four accepted height layers sum(K) in {1,2,3,4}, the elementary adjacency K -> K +/- e_j, and the rhombus corners K,K+e_j,K+e_j+e_k,K+e_k. The revised record explicitly distinguishes the Paper 1 P3 graph from any not-fully-specified additional Paper 2 coupled bonds.
2. **PF-I9 cut-project source bridge** (`PF_I9_CUT_PROJECT_SOURCE_BRIDGE_AND_EXACT_TRACE_2026_11_07.md`). This records the four internal height windows W_h, h=1,2,3,4, and the source acceptance construction.
3. **PF-I16 authenticated source geometry** (`PF_I16_AUTHENTICATED_THREE_FACE_MOTIF_AND_SHARP_INCIDENCE_2026_11_09.md`) and the exact two-/three-/four-face follow-up records. These explicitly retain original five-integer lower-face labels and direction pairs, e.g. ((0,1,0,0,0);(2,3)), and verify accepted source rhombi and original-link incidence across the eight finite source complexes.
4. **Hall proof program** (`PF_I16_MULTIVALUED_PI_ALL_ORDERS_PROOF_PROGRAM_2026_11_16.md`). Its source is explicitly (M,tau), with M a perfect matching of ordered ports and tau a spanning tree of the interval-overlap graph. Its operations are interval deletion, order-preserving relabelling, overlap-tree deletion, guarded local switches, and port-tree compression. The verifier's data model exposes interval endpoints and port-tree edges; the inspected source definitions do not attach a five-integer K label, a pentagrid cell, a physical vertex, a face-family pair, a phason, or a perpendicular-space coordinate to a port or interval.

### Exact conclusion of the search

There is a well-defined Z5 substrate in the Penrose/Fibonacci source records, and there is a well-defined ordered-port matching-tree system in the Hall records. **No record found defines a map between them.** In particular, none of the searched records identifies:
- a port index with a Penrose vertex label K;
- an interval [a,b] with a source rhombus, directed edge, or pair of Z5 labels;
- an overlap-tree edge with a physical adjacency K -> K +/- e_j;
- a reverse mark J with a source face, basis direction, or accepted perpendicular-space point.

This is stronger than saying the map is absent from the current verifier: the recovered published pentagrid construction and the PF-I16 accepted-rhombus audits define their geometric labels independently, while the Hall proof program defines its port objects independently. The records do not supply a bridge axiom or a shared indexing table. It remains possible that an unindexed historical notebook, generator input, or separate archive contains one, but it is not in the records searched here.

### A constrained candidate, not yet a correspondence

The only source-faithful way to construct a bridge would be to exhibit a labelled incidence-preserving map from the Hall port/interval complex into the accepted Penrose source complex. At minimum it would need to send:
- each port to a specified accepted source vertex K;
- each matching pair/interval to a specified source path or face-supported object with endpoints determined by those K labels;
- each overlap-tree adjacency to an explicitly stated relation among those source objects;
- each reverse mark J and its parent projection to a marked source subconfiguration whose Z5 labels can be read without choices.

It must preserve the relevant incidence, order, root, and deletion/compression operations, and its action under reflection and parent relabelling must be proved. If it only preserves abstract graph incidence, that may suffice for a new combinatorial observer construction, but it would not automatically inherit the Paper 3/4 perpendicular-space observer or failure-band semantics. To inherit those, the map must also preserve the actual five direction labels and accepted-window coordinates.

The Hall problem has arbitrary even port order n and includes every matching of those ports. The Penrose source complex has a specific accepted subset of Z5 labels and local rhombus/edge incidence. Thus a proposed embedding must explain how the entire Hall source family at each n is represented, not merely embed one selected target tree or a few convenient examples. It must also explain whether the map is injective, equivariant, or many-to-one and how that affects reverse-mark multiplicities. No such map has been found or tested.

### G1 status update

G0 source geometry is recovered at the indexed-definition level, subject to the byte-authentication caveat in the PF-I9/PF-I16 records. G1 is now **records-search negative / mathematically unconstructed**. The next useful action is not to assign phases to ports. It is to search the original dissertation/archive bundle for a shared data table, source generator, or notebook that constructs the Hall ordered ports from the accepted Z5 source. If no such artifact exists, the bridge must be proposed as a new labelled-complex construction and proved on its own terms before any H1/H2/H3 graph statistics are interpreted geometrically.

## 5. Reverse-mark graph once the map exists

For each target T:
1. Enumerate every admissible reverse mark J and its unique parent target P_J(T).
2. Compute r_J=Psi_n(T,J) and the five-bit failure signature
   \[
   \mathbf b_J=(b_0(r_J),\ldots,b_4(r_J)).
   \]
3. Retain the full state v_J=(J,P_J(T),r_J,b_J); do not quotient away the parent target.
4. Define directed candidate transitions only from a source-derived observer rule. For a pitch p, the idealized phase condition is
   \[
   \arg z_2(K)-\arg z_2(J)=2\pi p\pmod{2\pi},
   \]
   but a transition also needs an actual admissible geometric path/step and a stated tolerance derived from the lattice model. Phase proximity alone is not an edge.
5. Record whether the transition preserves the cut-load bound and whether the parent-target transition is a legal guarded-switch/exchange relation.
6. Build separate H1/H2/H3 directed graphs, and also reflection-reversed and shuffled-phase controls.

The graph must retain multiple parent targets even when they project to the same source parent; parent-projection multiplicity is part of the capacity problem, not noise to be discarded.

## 6. Measurements and falsification controls

Run at n=6,8,10, with source counts 22, 608, and 31,744 respectively. For each order report:

- total source count, reverse-mark incidences, distinct targets, and distinct (T,J,P_J(T)) states;
- reverse marks per target and parent targets per target, including multiplicity histograms;
- inverse uniqueness failures (expected zero under the current fixed-mark primitive);
- graph components, in/out-degree distributions, path/cycle lengths, and phase coverage;
- H1/H2/H3 transition coverage of all eligible reverse marks;
- fraction of transitions preserving the coordinatewise cut-load condition;
- target congestion induced by any proposed capacity allocation;
- stability of all statistics under n growth and under the prescribed port-reflection action.

Controls:
- **unmarked-set control:** erase transition orientation and phase order; H2/H3 should be indistinguishable at the 13-site orbit level;
- **reflection control:** reverse the observer word and reflect band labels; any purported handedness statistic must transform with the predicted sign;
- **shuffle control:** shuffle the ordered five-bit failure signatures while preserving their one-point frequencies;
- **null embedding control:** compare the proposed source-derived map with an explicitly arbitrary endpoint-mod-5 map, which is diagnostic only and cannot count as support;
- **Hall-blind construction:** freeze the map and graph before evaluating target loads, to prevent phase fitting to Hall success.

The 12-port retained-grandparent sibling-rerouting counterexample remains a mandatory regression test. A helical ordering must not be used to resurrect that invalid shortcut.

## 7. Candidate capacity statement

Once the map and transitions are independently justified, the useful theorem target is not merely that reverse marks form helical-looking paths. It is a capacity statement.

For each first-crowded-cut block k, seek a decomposition of the split demand among directed reverse-mark paths such that:
- every fiber F receives exactly delta(F);
- every target T receives total mass at most one;
- each positive allocation uses a retained incidence (F,T);
- every reroute follows an admissible transition and preserves cut-load domination.

Such a decomposition would prove the blockwise mixed-fiber Hall inequality. The path decomposition must be simultaneous across all fibers; local path existence or one-at-a-time rerouting is insufficient.

## 8. Decision gates

- **G0 — Recover source geometry:** source script and phason/accepted-label implementation located in the private Library; authenticate original archive bytes and recover exact worm/observer sampling inputs. PARTIAL.
- **G1 — Define Psi:** records search found no PF-I16 port/interval-to-Z5 correspondence; a labelled incidence-preserving map remains mathematically unconstructed. BLOCKED (search negative).
- **G2 — Build and audit reverse-mark graphs:** H1/H2/H3 plus controls at n=6,8,10. BLOCKED on G1.
- **G3 — Capacity experiment:** solve/measure path-supported split-demand allocations and compare against existing exact n=6,8,10 flow certificates. BLOCKED on G2.
- **G4 — Prove an order-uniform capacity lemma:** derive the mixed-fiber Hall dual for arbitrary nonnegative weights. OPEN.
- **G5 — Consequence:** only after G4 does all-orders multivalued-pi Hall follow, and only then does the weighted one-link inequality follow.

## 9. Current conclusion

The helical observer is a promising candidate for a *geometric ordering principle* on the multivalued-pi neighborhood, but the missing map Psi is the decisive mathematical gap. The rational-orbit pretest shows why phase order and a source-derived five-band word matter: the unmarked H2/H3 phase sets coincide, and the m=10 complete-orbit average vanishes. The existing Hall enumerator supplies exact reverse-mark inverses and parent projections, but it does not supply the Z5 geometry needed to label them.

No new Hall theorem, no new matching certificate, and no physical 3D lift are claimed by this audit.
