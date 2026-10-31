# R3-IR-536 — Actual M5 Penrose spanning-tree swap (2026-10-30)

Original geometry source was recovered from the user-supplied Archive 4.zip, nested penrose_yang_mills_2p1_causal_study.zip. Using Approximant(M=5) and penrose_faces with the eleven-face selected disk (0,1,3,2,4,154,150,11,10,7,8), the graph contains 30 distinct links and 20 vertices. The deterministic root-0 BFS spanning tree contains edge 4 but not edge 13. Exchanging tree edge 4 for chord 13 gives a second valid spanning tree of the SAME Penrose graph. Therefore the non-tree sufficient criterion used in R3-IR-527–529 is genuinely dependent on transport-tree choice on the actual disk.

Actual incidences: deleted face 0 links (1,4,13,0); retained face 10 links (13,18,26,12); face 10 is the only retained face incident on edge 13. The shared-link incidence is intrinsic and does not change with tree.

IMPORTANT: Loss of a non-tree criterion after swapping trees DOES NOT demonstrate that the Haar projection fails to reduce the other tree's Hamiltonian, nor that spectra differ. It also does not establish an absence of intertwiner. The archived 30x30 Whitney mass matrix is missing from the current runtime, so no actual-matrix principal-symbol comparison has been performed. Next obligation: reconstruct this matrix, then compare gauge-invariant multiloop Wilson forms on both actual Penrose trees.

No refinement-uniform cap or continuum mass gap established. Reproducer: research/scripts/audit_m5_tree_choice.py.
