# PF-I16 — Bounded Hall-to-PF incidence check: L1–L3

**Date:** 18 November 2026  
**Branch:** \`research/pf-i16-z5-incidence-lift-2026-11-18\`  
**Scope:** finite \(N_{\rm grid}=7\) targets; Hall orders \(n=4,6\); partial port/matching-edge realization only.  
**Status:** L1–L3 pass for every enumerated Hall source in both target domains under the frozen motif assignment. L4–L7 remain untested; no full marked incidence lift is claimed.

## 1. What was checked

This check takes the next step after the 32/32 marked-parent source checks. It constructs two separate finite accepted targets:

1. **PF-I16 original-source replay:** the indexed original pentagrid selection is independently reimplemented, with the strict PF-I16/PF-I11 face-triangle test.
2. **PF-I11 completed-window core:** the direct accepted-window incident-star construction, at the same \(N_{\rm grid}=7\) physical center and cutoff, with its own completed face population.

The targets are not merged. Both use the PF-I16 generic phason
\[
\gamma_j=((j\sqrt2+j^2\sqrt3)\bmod1),\quad
\gamma\leftarrow\gamma-\operatorname{mean}(\gamma),\quad
\gamma_4=-\sum_{j=0}^3\gamma_j.
\]
The PF-I11 completed-core construction was reconstructed from the direct-window generator using the original-source replay's center and cutoff. Its Ngrid=7 vertex-label and ordered-face hashes match the existing PF-I11 control record exactly:
- vertex labels: \`bb9aa7fca99bea4e32e2014190588e43d1913a179ecd1c2cccb25854d6cc4114\`
- accepted faces: \`005605e2253ce7e04fe5ed6f5d512b1c19f54ca3d6ecacaca12c6dc5a86467b4\`

This is a strong exact finite-data cross-check of the completed core. The PF-I16 original-source replay remains an independent reimplementation of the indexed private source; the private original bytes were not executed byte-identically.

## 2. Frozen target-side motif and edge matching

The target-side construction is fixed before the Hall source records are consumed. It uses the authenticated three-face motif from the PF-I16 source-incidence audit:
\[
\begin{aligned}
f_1&=((0,1,0,0,0);(2,3)),\\
f_2&=((0,1,0,0,0);(3,4)),\\
f_3&=((0,1,0,0,1);(0,3)).
\end{aligned}
\]
All three faces occur in both finite Ngrid=7 targets and pass their strict face-triangle tests. The motif has eight vertices and ten original links.

A fixed three-edge matching of its one-skeleton is:
\[
\begin{aligned}
e_1 &: (0,1,0,0,0)\longrightarrow(0,1,0,0,1), && +e_4,\\
e_2 &: (0,1,0,1,0)\longrightarrow(0,1,0,1,1), && +e_4,\\
e_3 &: (0,1,1,0,0)\longrightarrow(0,1,1,1,0), && +e_3.
\end{aligned}
\]
The six endpoints are pairwise distinct. Each edge is an actual positive elementary basis edge in both accepted target complexes. The edge list and its ordering are frozen; no Hall load, deficiency, flow, or helical phase enters their selection.

The assigned endpoint heights are \(1,2,2,3,2,3\), all in the permitted four-layer vertex range. The minimum strict vertex-window margin among these six endpoints is
\[
0.023695385039079087>0.
\]
The three strict face-triangle margins are
\[
0.03489770772309764,\quad
0.023695385039078865,\quad
0.023695385039079087,
\]
all positive.

## 3. Assignment rule and finite results

For each Hall source \(x=(M,\tau)\), sort its matching intervals lexicographically as
\[
I_1<\cdots<I_s,\qquad I_i=[a_i,b_i].
\]
Map the lower endpoint \(a_i\) to the lower label of \(e_i\), and \(b_i\) to its upper label. For \(n=4\), use \(e_1,e_2\); for \(n=6\), use \(e_1,e_2,e_3\).

This gives an injective port map for every perfect matching, and each matched pair maps to one of the fixed accepted \(\pm e_j\) edges. The construction uses only the ordered matching intervals and the pre-frozen target motif.

| Hall order | Hall sources | Eligible marks | PF-I16 original-source L1/L2/L3 | PF-I11 completed-core L1/L2/L3 |
|---:|---:|---:|---:|---:|
| \(n=4\) | 2 | 2 | 2/2 pass | 2/2 pass |
| \(n=6\) | 22 | 30 | 22/22 pass | 22/22 pass |

For both targets:
- **L1:** all ports in every source map to distinct accepted vertices.
- **L2:** every matched pair maps to an actual accepted elementary edge with its signed direction recorded.
- **L3:** every assigned vertex passes strict \(W_h\) acceptance; the three host rhombi pass strict \(T_{jk,h}\) acceptance.

The complete finite checker is:
\`research/scripts/verify_pf_i16_hall_l123_motif_lift.py\`.

## 4. What this result does not establish

This is a positive finite result for L1–L3, not a complete \(\mathfrak L_n=(\Phi_n,\epsilon_n,\kappa_n)\).

It does **not** yet establish:

- **L4:** connected face-supported realization of every Hall interval with a compatible ordered boundary trace;
- **L5:** typed shared-incidence witnesses for every edge of each full interval-overlap graph;
- **L6:** parent naturality for every reverse mark, including support deletion and certified collapses;
- **L7:** compatibility of the full linear port order and interval boundary order with the target incidence;
- any all-orders lift or any connection to the helical observer.

The assignment deliberately does not claim that the three motif faces are the interval supports \(\kappa_n(I)\). They are a common accepted host patch for the matched edges. That distinction is essential: L1–L3 alone do not encode the overlap tree or the multivalued parent operation.

The result is scoped to these two finite Ngrid=7 target domains and \(n=4,6\). It is not a global existence theorem and its failure under any later support or witness variant would not be a counterexample to Hall.

## 5. Next mathematical check

The next check should retain the frozen port map and test L4/L5 as separate model variants:
1. enumerate connected face supports containing each assigned matching edge;
2. test oriented simple-cycle and repeated-vertex boundary-walk variants separately;
3. record each strict-overlap pair's witness type (shared vertex, edge, or face), including non-tree overlap edges;
4. reject any candidate that cannot represent the full interval structure without collisions.

Only after a candidate passes L4/L5 should the support-exclusive deletion and free-edge-collapse rule for L6 be applied to every eligible mark. No phase assignment or Hall allocation should be introduced during these steps.

**Verdict:** a common authenticated local PF motif supplies enough disjoint accepted basis edges to realize every n=4 and n=6 matching source at the L1–L3 level in both finite target constructions. The geometric realization of the intervals and their multivalued parent transitions remains open.
