# PF-I16 — Star-source open-arc support obstruction

Date: 18 November 2026  
Branch: `research/pf-i16-z5-incidence-lift-2026-11-18`  
Scope: the L7b open-arc necessary condition for the explicit three-interval star source, on the PF-I16 original-source accepted complex at Ngrid=7. The PF-I11 completed-window core is a subcomplex of the PF-I16 face population used here.

## 1. Source and condition

Take
[
M=\{[1,6],[2,3],[4,5]\},\qquad
\tau=\{(I_1,I_2),(I_1,I_3)\}.
]
The root interval is (I_1=[1,6]); the two leaves (I_2,I_3) are disjoint. Deleting either leaf gives the same parent, and the retained leaf origin maps to the same second parent interval.

Write the three interval supports as (S_1,S_2,S_3). L5 requires
[
S_1\cap S_2\ne\varnothing,\qquad
S_1\cap S_3\ne\varnothing,\qquad
S_2\cap S_3=\varnothing,
]
where the last condition is disjointness as subcomplexes, including vertices.

Orient the boundary of (S_1) so its distinguished matched edge is directed from the lower-port image to the upper-port image. The open-arc condition requires both nonempty root/leaf footprints to lie strictly in the complementary boundary arc, avoiding the distinguished edge and both of its endpoints. Since (S_2,S_3) are disjoint, the two footprints must also be disjoint.

This is a necessary condition under the adopted L7b convention, not a sufficient condition for full parent naturality.

## 2. Bounded-support calculation

The PF-I16 Ngrid=7 target has 1,550 accepted vertices and 1,468 accepted rhombi. The calculation enumerated connected face-supported candidates containing exactly one incident face of the corresponding distinguished matched edge, with at most six rhombi per support. Candidates were then restricted to supports with a simple oriented boundary cycle, as required for the boundary-position test.

| Distinguished edge | Connected candidates, at most 6 faces | Candidates with simple boundary cycle |
|---|---:|---:|
| Root edge (e_1) | 1,236 | 1,223 |
| Leaf edge (e_2) | 1,111 | 1,099 |
| Leaf edge (e_3) | 1,040 | 1,020 |

For each root candidate, the two leaf candidate sets were filtered by the nonempty open-arc footprint condition. All 1,223 root candidates admitted candidate footprints for both leaves. The resulting 84,599,931 leaf-pair comparisons were then tested for full subcomplex disjointness, including vertices.

**Result: zero admissible triples.** Thus no triple of connected face supports, each of size at most six rhombi and each having a simple oriented boundary, satisfies this star source's open-arc condition and L5 leaf-leaf disjointness in the Ngrid=7 PF-I16 target.

The calculation also generated vertex-connected supports. It found no additional vertex-connected candidates with a simple boundary cycle beyond the shared-edge-connected list above; the boundary-cycle candidate counts therefore remained 1,223, 1,099, and 1,020.

Because the PF-I11 completed-window core is a subcomplex of the PF-I16 face population used for this bounded search, the same bounded-size no-go applies to that core.

## 3. Identifiable structural pattern

The obstruction is a **two-branch packing problem on one anchored boundary arc**:

1. The root support's distinguished edge and its two endpoints are forbidden to the two attachment footprints.
2. Both leaf branches must attach to the same remaining open boundary arc.
3. Their attachment footprints must be disjoint.
4. The leaf supports themselves must be disjoint even at vertices.
5. Each leaf support must also reach its own distinguished matched edge.

In the planar support complex, this suggests replacing a broad enumeration of connected supports by a linkage/separation calculation. A valid triple would induce two mutually vertex-disjoint paths from the two leaf matched edges to two disjoint attachment footprints on the root's open boundary arc, with the paths and their leaf-side supports avoiding one another. The cyclic order of the two attachment footprints is then constrained by the planar embedding.

This is the next proof lead, not yet a theorem: compute the minimum vertex-disjoint linkage / separator obstruction in the face-adjacency and vertex-incidence structure, while retaining the exact anchored open arc. In particular, determine whether every pair of candidate attachment regions forces a shared vertex, a crossing in the planar dual, or an intersection with the root's marked edge/endpoints. Such a certificate could extend beyond the six-rhombus cutoff.

## 4. Limits and interpretation

- This is a bounded-support impossibility result for one explicit star source in one finite PF-I16 crop.
- It does not rule out supports of seven or more rhombi, other target crops, or alternative incidence-lift constructions.
- It is not a counterexample to Hall's theorem and says nothing by itself about Hall deficiency.
- The search used the PF-I16 Ngrid=7 accepted-face population. The PF-I11 conclusion follows only because its completed-window core is a subcomplex of that population.
- The calculation was independently executed in the analysis environment. No repository verifier was created or run from a clean checkout in this session. Treat the numerical result as a recorded session calculation pending a committed reproducibility script and clean-checkout replay.

## 5. Next check

Build a graph-level certificate for the two-branch linkage obstruction:
1. Freeze the exact PF-I16 Ngrid=7 face/vertex incidence graph and the three distinguished matched edges.
2. Enumerate candidate open-arc attachment regions on root-support boundaries, without first enumerating all root supports.
3. For each pair of disjoint attachment regions, test for two vertex-disjoint leaf-edge-to-attachment linkages in the complement of the root support, enforcing the full subcomplex disjointness rule.
4. Extract a minimum separator or explicit noncrossing-order contradiction for every candidate pair.
5. Only after this graph-level test is validated, generalize the argument to arbitrary support size or state precisely why it remains crop-dependent.

Do not infer a global impossibility from the bounded calculation, and do not use Hall demands or flow values to select supports.
