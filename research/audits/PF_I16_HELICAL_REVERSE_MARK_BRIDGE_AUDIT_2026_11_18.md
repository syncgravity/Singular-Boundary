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

A likely data recovery target is the original coupled-Z5 generator, phason/acceptance-window convention, five Conway-worm paths, and observer sampling implementation referenced by the dissertation. If these are not recoverable, the bridge remains a conjectural new construction and must be labelled as such.

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

- **G0 — Recover source geometry:** authenticated Z5 lift, W, phason, failure bands, worm paths, and observer sampling source. OPEN.
- **G1 — Define Psi:** source-derived map from reverse marks to W with covariance and reflection laws. OPEN.
- **G2 — Build and audit reverse-mark graphs:** H1/H2/H3 plus controls at n=6,8,10. BLOCKED on G0/G1.
- **G3 — Capacity experiment:** solve/measure path-supported split-demand allocations and compare against existing exact n=6,8,10 flow certificates. BLOCKED on G2.
- **G4 — Prove an order-uniform capacity lemma:** derive the mixed-fiber Hall dual for arbitrary nonnegative weights. OPEN.
- **G5 — Consequence:** only after G4 does all-orders multivalued-pi Hall follow, and only then does the weighted one-link inequality follow.

## 9. Current conclusion

The helical observer is a promising candidate for a *geometric ordering principle* on the multivalued-pi neighborhood, but the missing map Psi is the decisive mathematical gap. The rational-orbit pretest shows why phase order and a source-derived five-band word matter: the unmarked H2/H3 phase sets coincide, and the m=10 complete-orbit average vanishes. The existing Hall enumerator supplies exact reverse-mark inverses and parent projections, but it does not supply the Z5 geometry needed to label them.

No new Hall theorem, no new matching certificate, and no physical 3D lift are claimed by this audit.
