# Exact SU(2) outer-loop word-invariance certificates (2026-10-31)

On the original-link 3×3 planar cage with the central face deleted, encode original links and target translation G as independent free-group generators. Apply the deterministic tree–cotree link update by exact free-word substitution and cancellation. All eight retained face words are verified invariant; target face word becomes G times its original word. For each of the eight adjacent retained-face pairs, cyclically reduce the six-link exterior boundary word before and after the transport; cyclic rotations and inverse yield identical SU(2) trace for every assignment of original links and G.

**BFS:** changed original link indices 2,9; exact trace-invariance certificates for **seven of eight** retained-neighbor exterior loops; only not-certified pair (1,0)–(2,0).

**DFS:** changed indices 1,3,5,11,12; exact certificates for **five of eight** loops; uncertified pairs (0,0)–(0,1), (2,0)–(2,1), (2,1)–(2,2).

These certify all the numerically observed zero terms. The previous 80 random noncommuting configurations per tree provide nonidentity witnesses for the remaining one and three pairs. Failure of free-word equivalence by itself is not a universal SU(2) trace-inequivalence proof.

Consequently, for these exact finite-cage transport constructions, the exact second-order log-vacuum response reduces to **one outer-loop difference for BFS and three for DFS**, with coefficients from the archived exact Fierz free-resolvent theorem. No claim that BFS is globally optimal among all tree choices, or that this persists at physical coupling or under refinement.

A standalone deterministic Python word verifier, JSON certificate list and SHA256 manifest are included in the Library archive `/The Singular Boundary/Proof Audits/R3_IR_OUTER_LOOP_WORD_CERTIFICATES_2026-10-31.zip`. Signed current, connected covariance and continuum Yang–Mills mass gap remain open.