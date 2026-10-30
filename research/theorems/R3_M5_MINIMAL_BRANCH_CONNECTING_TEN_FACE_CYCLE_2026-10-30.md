# M5 periodic Penrose: first branch-connecting ten-face dual cycle
Date: 2026-10-30
Status: EXACT combinatorial incidence and shortest-path result, NOT a proof of nonzero SU(2) deleted response.

Using user-provided penrose_study.zip: Approximant(M=5), wilson_torus.penrose_faces, 188 face words and 376 links. Build dual adjacency by putting an undirected dual edge between faces whenever they share a primal edge.

Previously verified truncated seven-face tree S={1,2,3,4,7,8,10}, with edges (1,3),(3,2),(2,4),(1,8),(8,7),(7,10), covers all four primal edge-neighbors {1,2,4,10} of deleted face zero. The 13-face radius-two set has localized cycles, but the two ends 4 and 10 are not linked by a path within that radius-two set avoiding the seven-face core. A BFS in the COMPLETE M5 dual graph, excluding central face 0 and excluding internal tree vertices {1,2,3,7,8}, yields the shortest outer branch-connecting path
4 - 154 - 150 - 11 - 10,
of length 4 dual edges. Three added faces {154,150,11} therefore produce the ten-face simple cycle
1 - 3 - 2 - 4 - 154 - 150 - 11 - 10 - 7 - 8 - 1.
Exact corresponding primal shared-edge IDs are [3,2,5,19,296,17,18,12,8,14], respectively. The ten distinct faces are S10={1,2,3,4,7,8,10,11,150,154}. On this selected ten-face subgraph the induced graph has exactly ten edges and a single cycle (verify with code), so this is a unicyclic candidate. The shortest-path result establishes that, among outer 4-to-10 paths disjoint from the interior vertices of the original seven-tree, three additional faces are necessary. It does not establish optimality among ALL possible cycles or prove winding number around f=0.

The three cycles already in the 13-face radius-two graph are localized on (2,3,47), (4,143,154), (7,10,15), not the missing 4-to-10 outer branch connector. Merely having ANY cycle is not a sufficient non-Haar diagnostic. To claim deleted-holonomy sensitivity, reconstruct actual toroidal coordinates and test winding/linking relative to face zero, then evaluate an SU(2) electric block with appropriate rooted Wilson observables. A dual cycle surrounding the deleted face is a candidate, not a proof of non-Haar vacuum or mass gap. Repeated face insertions remain a separate untested mechanism.
