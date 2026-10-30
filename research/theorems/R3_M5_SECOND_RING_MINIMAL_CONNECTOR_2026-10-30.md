# M5 Penrose periodic face-0 second-ring exact incidence and minimum active connector
Date: 2026-10-30
Status: verified combinatorial computation using attached penrose_study.zip, not an SU2 non-Haar coefficient or open-disk result.

Source modules penrose_causal_study.py and wilson_torus.py. For Approximant(M=5), fidx,sgn,E=penrose_faces(a), prepare_cellulation gives F=188 faces E=376 edges. Build dual face adjacency from each edge's two incident faces. BFS from deleted face f=0:
ring1=[1,2,4,10], ring2=[3,7,8,11,15,43,47,143,154].
Retained active faces from both rings: 13, induce connected adjacency graph with 15 undirected edges and cycle rank 15-13+1=3. Per-face active neighbors:
1:[3,8,43]
2:[3,4,47]
3:[1,2,47]
4:[2,143,154]
7:[8,10,15]
8:[1,7]
10:[7,11,15]
11:[10]
15:[7,10]
43:[1]
47:[2,3]
143:[4,154]
154:[4,143]
All central face edges are shared with retained ring1 faces, with incidence e1:face2, e4:face4, e13:face10, e0:face1.

Exhaustively checking all 2^9 subsets of ring2 to connect all four ring1 vertices in the induced retained face graph yields minimum connector count=3 and UNIQUE minimum set {3,7,8}. The resulting seven retained active faces are {1,2,3,4,7,8,10}. Their six edges are (1,3),(3,2),(2,4),(1,8),(8,7),(7,10), forming a TREE. Two arms meet at face 1; they do not join by an edge between 3 and 8. This is the smallest CONNECTED support spanning the four immediate neighbors *among subsets of the first two rings*. Full 13-face graph contains three cycles.

For truncated deleted Hamiltonian with only four neighbor faces active, face1 was an isolated retained component and exact Q Omega=0. Activating {3,7,8} destroys THAT particular full-link factorization: face 1 is no longer link-disjoint from all other active retained faces. A connected retained plaquette adjacency graph is an important nontriviality diagnostic, NOT a theorem that Q Omega !=0; gauge invariance and retained link variables may support further cancellation. No SU2 coefficient was evaluated, no fourth-order nonzero claim, and no continuum mass gap.

Reproducibility pseudocode: construct adjacency from fidx/prepare_cellulation; BFS ring1/2; iterate combinations of ring2 by size; retain first subset for which induced BFS on ring1 union subset is connected. The finding depends on periodic torus M5 indices and cannot be cited as an open Penrose disk geometric certificate.
