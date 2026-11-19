# PF-I16 — Bounded Hall-to-PF incidence check: L4–L5

**Date:** 18 November 2026  
**Branch:** \`research/pf-i16-z5-incidence-lift-2026-11-18\`  
**Scope:** the two distinct \(N_{\rm grid}=7\) finite target domains; Hall source orders \(n=4,6\).  
**Status:** bounded L4–L5 support and full-overlap witness checks pass for all 24 enumerated source records (2 at \(n=4\), 22 at \(n=6\)). This extends the frozen L1–L3 motif check; it does not establish L6–L8 or Hall.

## 1. Frozen data and target domains

The L1–L3 assignment is retained without modification:

\[
\begin{aligned}
e_1 &: (0,1,0,0,0)\to(0,1,0,0,1), &&+e_4,\\
e_2 &: (0,1,0,1,0)\to(0,1,0,1,1), &&+e_4,\\
e_3 &: (0,1,1,0,0)\to(0,1,1,1,0), &&+e_3.
\end{aligned}
\]

Sorted Hall intervals \(I_1<\cdots<I_s\) continue to use \(e_i\) in order. The target domains remain separate:

| Target | Vertices | Edges | Accepted rhombi |
|---|---:|---:|---:|
| PF-I16 original-source replay | 1,550 | 3,017 | 1,468 |
| PF-I11 completed-window core | 1,432 | 2,761 | 1,330 |

The local face neighborhood used by the supports is contained in both targets. No target populations are merged. The PF-I16 source remains an independent reimplementation of the private indexed source, not byte-identical execution of its unavailable private bytes. The PF-I11 completed-core vertex and face hashes are checked by the verifier against the frozen control values.

## 2. L4 support definition tested

For each matched interval \(I_i=[p_i,q_i]\), the distinguished ordered boundary trace is the oriented elementary edge
\[
\Phi(p_i)\longrightarrow\Phi(q_i).
\]
The interval support is a connected union of one or two accepted rhombi containing that edge. The edge is required to occur in exactly one selected rhombus, so it remains a boundary 1-cell of the support. When two rhombi are selected, they must share an elementary edge; thus the support is edge-connected, not merely vertex-connected.

The candidate search was bounded and explicit:
- exactly two accepted rhombi are incident to each of the three frozen matching edges in each target;
- each matching edge has eight admissible one- or two-face support candidates under the boundary-edge and edge-connectivity conditions;
- all selected rhombi pass the strict \(T_{jk,h}\) test and all their vertices pass strict \(W_h\) acceptance;
- the selected support sets are drawn from the common accepted local patch in both targets.

The largest support used contains two faces. This is a finite construction for the fixed \(N_{\rm grid}=7\) motif, not a claim that all interval supports in all orders have size at most two.

## 3. L5 full-overlap witnesses

For each source, the support assignment is chosen against the **full** interval-overlap graph from the Hall source record, not merely the selected spanning tree \(\tau\). Every overlapping pair receives an explicit witness. Every non-overlapping pair has disjoint support subcomplexes (no common vertex), a stronger separation check than merely declining to identify their boundaries.

All three possible \(n=6\) full-overlap patterns appearing in the source enumeration are realized:

| Full-overlap graph on sorted intervals | Source records | Witness pattern |
|---|---:|---|
| \(\{(1,2),(2,3)\}\) | 2 | shared edge for both overlap pairs; supports 1 and 3 disjoint |
| \(\{(1,2),(1,3)\}\) | 2 | shared face for (1,2), shared vertex for (1,3); supports 2 and 3 disjoint |
| \(\{(1,2),(1,3),(2,3)\}\) | 18 | shared face, shared face, and shared edge respectively |

For \(n=4\), both source records have the single overlap edge \((1,2)\), witnessed by a shared accepted rhombus.

Across the 24 source records, the verifier records:
- 40 shared-face witnesses;
- 22 shared-edge witnesses;
- 2 shared-vertex witnesses;
- zero non-overlap pairs with shared incidence.

The typed witness counts include repeated source records with different selected spanning trees. They are not counts of distinct geometric cells.

## 4. Results in both finite target domains

| Hall order | Sources | PF-I16 original-source L4/L5 | PF-I11 completed-core L4/L5 |
|---:|---:|---:|---:|
| \(n=4\) | 2 | 2/2 pass | 2/2 pass |
| \(n=6\) | 22 | 22/22 pass | 22/22 pass |

The minimum strict acceptance margins among selected support vertices and faces are:
\[
\min \text{ vertex-window margin}=0.023695385039079087,
\]
\[
\min \text{ face-triangle margin}=0.023695385039078865.
\]
Both are positive. The same support assignments and typed witnesses work in the two target domains.

**L4 verdict:** every interval has a connected, edge-supported realization with an oriented boundary trace from its lower to upper port image.  
**L5 verdict:** every edge of the full interval-overlap graph has a typed shared-incidence witness, and non-overlapping interval pairs have disjoint supports, for all enumerated \(n=4,6\) sources.

## 5. Construction independence and limitations

The support candidate sets are generated solely from the frozen target face complex and the three frozen matching edges. A support assignment is then selected using only the source's full overlap graph and a fixed lexicographic tie-break. No Hall deficiency, demand, flow, congestion, matching outcome, phase, or helical observer data enters the construction.

The bounded verifier is:
\`research/scripts/verify_pf_i16_hall_l45_bounded_support.py\`.

The finite L4–L5 analysis was executed in this session by an independent Python reconstruction of the \(N_{\rm grid}=7\) indexed source target, local strict-window face neighborhood, and connected-support search. A GitHub checkout was unavailable in this session, so the newly committed repository verifier itself has **not** been run from a checkout here. Its assertions are included for reproducible repository-side replay; do not describe that as a completed checkout test.

## 6. What remains open

This result does not establish:
- **L6:** parent naturality for every eligible reverse mark, support-exclusive deletion, or certified collapse compatibility;
- **L7:** global compatibility of the full port order and all interval boundary orders beyond each local lower-to-upper trace;
- **L8:** an all-orders construction or a canonical compatible family of lifts;
- any helical observer interpretation;
- any all-orders Hall inequality.

The next check is L6: for every eligible non-root leaf mark, compare the child support family with the parent support family after deleting the marked interval, and test whether the removed support is support-exclusive and collapses by explicitly certified free-edge moves while preserving all retained incidences. Keep the multivalued parent relation intact. A failure of this chosen support family is not a Hall counterexample; it would be a failure of this bounded geometric lift candidate.
