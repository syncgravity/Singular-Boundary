# PF-I16 — Star-source relative face-separator calculation

Date: 18 November 2026  
Branch: `research/pf-i16-z5-incidence-lift-2026-11-18`  
Target: PF-I16 original-source accepted complex, Ngrid=7 (1,550 vertices, 3,017 edges, 1,468 accepted rhombi).  
Source: the three-interval star
[
M=\{[1,6],[2,3],[4,5]\},\qquad
\tau=\{(I_1,I_2),(I_1,I_3)\}.
]

## 1. Frozen motif edges and the separator vertex

Use the unchanged L1-L3 motif assignment:
[
\begin{aligned}
e_1 &: (0,1,0,0,0)\to(0,1,0,0,1),\\
e_2 &: (0,1,0,1,0)\to(0,1,0,1,1),\\
e_3 &: (0,1,1,0,0)\to(0,1,1,1,0).
\end{aligned}
]
Let
[
v_*=(0,1,1,1,0).
]
This is the upper endpoint of (e_3). Consequently every face-supported interval support containing the distinguished matched edge (e_3) contains (v_*).

The two accepted rhombi incident to (e_3) both contain (v_*). Of the two accepted rhombi incident to (e_2), one contains (v_*) and one does not. The full accepted-face star of (v_*) has seven rhombi:
[
egin{gathered}
((-1,0,1,1,0);0,1),\
((-1,1,1,1,0);0,2),\
((0,0,1,1,0);1,4),\
((0,1,0,0,0);2,3),\
((0,1,0,1,0);2,4),\
((0,1,1,0,-1);3,4),\
((0,1,1,1,-1);2,4).
end{gathered}
]
Here ((m;j,k)) denotes the accepted rhombus with lower label (m) and direction pair ((j,k)).

## 2. Strict root-boundary target and face graph

For a candidate root support (S_1), take its simple oriented boundary cycle beginning with the directed matched edge (e_1). Let (A(S_1)) be the vertices strictly on the open complementary boundary arc: neither endpoint of (e_1) is included.

Let (B(S_1)=V(S_1)\setminus A(S_1)). These are forbidden intersection vertices: a leaf footprint containing any of them is not wholly on the required open arc.

Construct the face-adjacency graph whose nodes are accepted rhombi and whose edges join rhombi sharing an elementary edge. For the root support (S_1):
- delete every face in (S_1);
- delete every face containing a vertex of (B(S_1));
- define the target faces to be the remaining faces meeting (A(S_1)).

A connected face-supported leaf support that meets the root only on the open complementary arc must contain a face-adjacency path from one of its two matched-edge incident seed faces to this target set. If it avoids (v_*), that path must remain after deleting all seven faces incident to (v_*).

## 3. Exhaustive bounded-root census

Enumerated connected face supports containing exactly one of the two faces incident to (e_1), and having one simple boundary cycle with (e_1) on that boundary. Counts by number of rhombi:

| Root support size | Candidate root supports |
|---:|---:|
| 1 | 2 |
| 2 | 6 |
| 3 | 20 |
| 4 | 70 |
| 5 | 247 |
| 6 | 878 |
| 7 | 3,113 |
| 8 | 10,959 |
| **Total** | **15,295** |

The size-1 through size-6 census is the previously used connected-support enumeration. The size-7 extension was checked against all 12,770 connected size-7 supports before the simple-boundary filter, yielding 3,113. The size-8 extension was checked against all 140,642 connected size-8 supports before the simple-boundary filter, yielding 10,959. Thus the size-7 and size-8 simple-boundary root lists were not generated merely by extending already-simple parents.

For **every one of the 15,295 root supports**, after deleting the seven faces incident to (v_*), the remaining face-adjacency graph has no path from either (e_2)-incident seed face to the strict open-arc target set.

Equivalently, for every root support in this census, every face-adjacency path from the (e_2) matched edge to an admissible root open-arc footprint contains a face incident to (v_*). This is the relative separator statement.

The root-support position of (v_*) in the census is:
- outside the root support: 7,246;
- on the open complementary arc: 8,048;
- interior to the root support: 1.

These cases have the same obstruction interpretation:
- If (v_*) is outside the root support, an (e_2) support reaching the open arc must contain (v_*), and so intersects the (e_3) support there.
- If (v_*) is on the open arc, both leaf supports are forced to contain the same vertex (v_*), again violating their required disjointness.
- If (v_*) is interior to the root support, the (e_3) support already meets a root vertex forbidden by the open-arc condition.

## 4. Consequence

**Bounded-root separator conclusion:** for this explicit star source, in the PF-I16 Ngrid=7 target, no L4-L5-L7b support triple exists with a simple-boundary root support of at most eight rhombi, even if the two leaf supports are allowed arbitrarily many rhombi.

Reason: every admissible (e_2)-to-root-open-arc face path must use (v_*), while every (e_3) support contains (v_*) by virtue of its distinguished matched edge. The two leaf supports therefore cannot be disjoint as subcomplexes.

This is stronger than the previous six-rhombus-per-support search: the leaf-support size cutoff has been removed for the bounded root-support family.

## 5. Failed relaxation and why the face separator matters

A relaxed primal one-skeleton linkage test was also run. It allowed paths along any accepted elementary edge and did not require a path to be realizable as a connected union of accepted rhombi with the strict root-footprint condition. For the 1,223 root supports of size at most six, it found two vertex-disjoint primal paths in 1,105 cases. Thus that relaxation is too weak to certify the obstruction.

The successful test is the strict face-adjacency test above. It preserves the rhombus support condition and removes every face touching a root vertex outside the open complementary arc. The seven-face star of (v_*) then acts as a relative separator.

## 6. Limits and next step

- The result is exhaustive for simple-boundary root supports of sizes 1 through 8 in this finite Ngrid=7 PF-I16 target.
- Leaf supports are not size-bounded in the separator argument, provided they are connected face-supported subcomplexes and satisfy the adopted simple-boundary/open-arc requirements.
- Root supports of size 9 and above have not been exhaustively enumerated. A preliminary expansion from already-simple size-8 parents produced 38,440 size-9 candidates, all passing the same (v_*)-separator test, but that size-9 list has not been proved exhaustive and is not included in the theorem statement.
- This is not an all-target or all-orders theorem, and it is not a Hall counterexample.
- The calculation was executed in the analysis environment. No clean-checkout verifier run was performed in this session.

Next: seek a topological/planar argument that the relative (v_*)-separator persists for every connected disk-like root support containing the distinguished edge (e_1), without a root-size cutoff. The relevant geometry is the cyclic order of (e_1,e_2,e_3) and the fact that the (e_2)-to-open-arc route is forced through the (e_3) endpoint (v_*). If this cannot be proved from the planar embedding, retain the finite root-size-8 result as a diagnostic only.
