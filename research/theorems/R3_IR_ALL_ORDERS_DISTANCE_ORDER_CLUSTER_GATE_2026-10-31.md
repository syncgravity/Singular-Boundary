# R3-IR — All-orders coupling-order versus distance cluster selection

31 October 2026. Finite original-link SU(2) Wilson Hamiltonian on a simply connected planar square disk. For face-disjoint two-plaquette domino regions D and E at minimum face-edge adjacency distance d≥1, with normalized unique positive ground state of H(λ)=K−λΣ_(f≠f0)b_f p_f, the connected covariance obeys:

**(d^n/dλ^n) Cov_νλ(r_D,r_E)|_(λ=0)=0 for every n<2d+2.**

**Proof:** multivariate analyticity near the free ground state; independent SU(2) center flips of elementary face traces in the planar disk force all four faces in D∪E to occur with odd multiplicity in any contributing monomial, all other faces with even multiplicity. A monomial whose participating face-edge adjacency components do not connect D to E contributes zero connected covariance, by exact original-link Hamiltonian tensor factorization after turning off other couplings. Connecting regions at distance d requires d−1 extra faces, each with even positive exponent at least two. Total degree therefore ≥4+2(d−1)=2d+2. The leading permitted coefficient may still vanish.

Examples: d=1 first permitted order 4; d=2 order 6; d=3 order 8; d=4 order 10. The rule is exact for each finite disk and is not physical-coupling exponential decay. No uniform Taylor coefficient bound or convergence radius at λ=1 has been proved.

Standalone deterministic checker on 3×3 through 21×21 square disks: 114 distance-class bridging-witness checks, zero failures. Full proof, verifier, per-grid distance counts and SHA256 manifest: Library `/The Singular Boundary/Proof Audits/R3_IR_ALL_ORDERS_DISTANCE_ORDER_CLUSTER_GATE_2026-10-31.zip`. Nonperturbative connected covariance, unweighted signed current, continuum 3D SU(2) Yang–Mills mass gap remain OPEN.