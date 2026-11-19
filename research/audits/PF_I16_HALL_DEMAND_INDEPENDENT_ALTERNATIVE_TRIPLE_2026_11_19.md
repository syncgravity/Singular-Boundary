# PF-I16 — Demand-independent alternative three-edge incidence motif

Date: 19 November 2026  
Branch: `research/pf-i16-z5-incidence-lift-2026-11-18`  
Verifier: `research/scripts/verify_pf_i16_hall_demand_independent_alternative_triple.py`

## 1. Search design and independence

The rejected L7b motif was not modified. A new search was run directly on the accepted PF target geometry, without reading Hall source records, reverse-mark demands, source loads, deficiencies, matching outcomes, or flow results.

Search domain:
- PF-I11 completed-window core at Ngrid=7, with 1,432 vertices, 2,761 elementary edges, and 1,330 accepted rhombi.
- Matched edges with exactly two incident accepted rhombi, so the support boundary condition is stable under the finite target crop.
- Connected interval supports consisting of one or two accepted rhombi, with the distinguished matched edge on a simple boundary cycle.
- Pairwise vertex-disjoint matched edges.
- For every overlap pair, its full common face/edge/vertex footprint lies on the open complementary boundary arc of both supports.
- Exact support intersection graphs for all three three-interval patterns: star, path, and triangle.

The core has 2,585 elementary edges with exactly two incident accepted rhombi. All 2,585 admit at least one simple-boundary support among the one-/two-rhombus candidates. Candidate selection used only these geometric and combinatorial conditions.

## 2. Alternative matched-edge triple

The search finds the following ordered, pairwise vertex-disjoint edges:
\[
\begin{aligned}
e_1 &: ( -7,-4,5,7,0)\to(-6,-4,5,7,0), &&+e_0,\\
e_2 &: ( -7,-3,5,7,-1)\to(-7,-3,6,7,-1), &&+e_2,\\
e_3 &: ( -6,-3,5,6,-1)\to(-6,-3,5,6,0), &&+e_4.
\end{aligned}
\]
Each edge is an actual accepted elementary basis edge in the PF-I11 core and the PF-I16 original-source replay. All nine support-face occurrences used across the three graph patterns are drawn from eight distinct accepted rhombi, all present in both target domains.

## 3. Support realizations

A face is denoted `(m;j,k)`, meaning the accepted rhombus with vertices
\[
m,\quad m+e_j,\quad m+e_j+e_k,\quad m+e_k.
\]

### Star: edges 1–2 and 1–3 overlap; 2–3 do not

\[
\begin{aligned}
S_1&=\{((-7,-4,5,7,0);0,1)\},\\
S_2&=\{((-7,-3,5,7,-1);2,4)\},\\
S_3&=\{((-6,-3,4,6,0);2,3),((-6,-3,5,6,-1);3,4)\}.
\end{aligned}
\]

The root-leaf footprints are single vertices:
- (S_1\cap S_2): ((-7,-3,5,7,0)).
- (S_1\cap S_3): ((-6,-3,5,7,0)).
- (S_2\cap S_3=\varnothing), including vertices.

Both root footprints are distinct points on the root's open complementary arc, and each is on the corresponding leaf's open complementary arc.

### Path: edges 1–2 and 2–3 overlap; 1–3 do not

\[
\begin{aligned}
S_1&=\{((-7,-4,5,7,0);0,1)\},\\
S_2&=\{((-7,-3,5,7,-1);0,2),((-7,-3,5,7,-1);0,4)\},\\
S_3&=\{((-6,-3,5,6,-1);1,3),((-6,-3,5,6,-1);1,4)\}.
\end{aligned}
\]

The footprints are:
- (S_1\cap S_2): one shared edge.
- (S_2\cap S_3): one shared vertex, ((-6,-3,5,7,-1)).
- (S_1\cap S_3=\varnothing), including vertices.

Both nonempty footprints lie on the open complementary arcs of both supports in the pair.

### Triangle: all three pairs overlap

\[
\begin{aligned}
S_1&=\{((-7,-4,5,7,0);0,1)\},\\
S_2&=\{((-7,-3,5,7,-1);0,2),((-7,-3,5,7,-1);0,4)\},\\
S_3&=\{((-6,-3,4,6,0);2,3),((-6,-3,5,6,-1);3,4)\}.
\end{aligned}
\]

The footprints are:
- (S_1\cap S_2): one shared edge.
- (S_1\cap S_3): one shared vertex, ((-6,-3,5,7,0)).
- (S_2\cap S_3): one shared edge.

Each footprint lies on the open complementary arcs of both supports.

In all cases, each support is connected, has a simple boundary cycle, and contains exactly one accepted face incident to its distinguished edge. Thus the matched edge remains a boundary edge. Supports contain at most two rhombi.

## 4. Strict acceptance and target controls

Across all supports used in all three patterns:
- Eight distinct accepted rhombi.
- Sixteen distinct support vertices.
- Minimum strict vertex-window margin: (0.06831334502945263).
- Minimum strict face-triangle margin: (0.06831334502945297).

The candidate and all listed supports were checked against both target domains:
- PF-I11 completed-window core: ((V,E,F)=(1432,2761,1330)).
- PF-I16 original-source replay: ((V,E,F)=(1550,3017,1468)).

The completed-window core face set is contained in the original-source replay, so the same local support certificates are present in both.

## 5. What this advances

This is a genuine alternative to the rejected frozen motif at the L4/L5 level and passes the necessary open-arc placement test for all three three-interval overlap graphs. In particular, it avoids the previous local obstruction: no middle-edge incident-face choice forces either a root marked-edge endpoint into the root footprint or a common vertex between the two non-overlapping leaves.

It is not yet a full L7b result. The test establishes boundary-arc placement, not the complete orientation-preserving subdivision/collapse comparison of cyclic footprint signatures. Nor does it establish L6c parent naturality across the 30 marked projections. The next check is therefore parent restriction and coherence for this fixed triple, followed by the full L7b signature comparison. The direct mixed-fiber Hall proof remains the principal all-orders route.

## 6. Reproducibility status

The committed verifier rebuilds both target complexes, performs the geometric support search on the completed-window core, and verifies the resulting triple and all three support patterns in both target domains.

The numerical search and the listed support certificates were independently carried out in the analysis session. The newly committed verifier was fetched back and checked for content, but it has **not** yet been run from a clean checkout. No Hall demand or flow data was used in the search.
