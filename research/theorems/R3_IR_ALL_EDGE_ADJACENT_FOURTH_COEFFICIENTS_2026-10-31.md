# Complete exact unit-weight SU(2) fourth-order edge-adjacent domino covariance classification

**2026-10-31; original-link SU(2) Wilson Hamiltonian; perturbative coefficient at λ=0.** The four symmetry classes of face-disjoint domino loop pairs with shared original links are: straight 4×1, bent L, staggered zigzag (each **one** common link), and aligned 2×2 (**two** common links). Previous claim that straight and aligned exhaust all geometries was incorrect.

**Exact signed coefficient of λ⁴ in connected covariance, for a_e=b_f=1:**
- Straight 4×1: **30757/1843845120** (prior theorem).
- Bent four-face L: **30757/1843845120** (**new exact rational calculation**).
- Staggered four-face zigzag: **30757/1843845120** (**new exact rational calculation**).
- Aligned 2×2: **19667/420526080** (prior theorem).

Each one-link geometry has raw fourth moment **1967237/1843845120** and connected mean-product subtraction **49/46656**. Every coefficient is strictly positive. The equality across different one-link geometries is verified at **unit weights and fourth order only**, not asserted at arbitrary weights or higher order.

The new exact calculations use a *primal spanning tree of the actual original-link lattice*, four external chord holonomies, their correct left/right electric generators, and exact 1,2,5,14-dimensional SO(3)-invariant tensor-sector rational solves with all 24 square-free insertion orderings. Every elementary trace has K-eigenvalue 3, every domino exterior trace 9/2, and every bent/staggered ten-link union exterior trace 15/2. An independent full 256-dimensional numerical tensor solve checks each new coefficient within 3e−19 with maximum linear residual 2.22e−16.

For 21×21 cages the four unordered pair counts are straight **756**, bent **3040**, staggered **1520**, aligned **800** (total **6116**). The maximum neighbors of each type per domino are **2,8,4,2**. All other face-disjoint pairs are link-disconnected and have zero fourth connected coefficient by exact factorization. Therefore, for the **unit-weight face-disjoint fourth Taylor coefficient matrix**,
**||C_disjoint^(4)||₂ ≤14·30757/1843845120+2·19667/420526080 = 1959953/5992496640 ≈ 3.270678513e−4.**
For the **fourth derivative** matrix multiply by 24: **1959953/249687360 ≈ 0.007849628431**.

This is NOT a bound on the *whole* fourth-order covariance matrix: off-diagonal fourth coefficients of **face-overlapping dominoes are still unknown**, even though the diagonal fourth coefficient was evaluated separately. No physical coupling λ=1, arbitrary-weight sign, signed-current estimate, or continuum Yang–Mills mass gap follows.

Full mathematical report, exact SymPy and independent numerical verifiers, geometric enumeration, results, SHA256 checksums: Library `/The Singular Boundary/Proof Audits/R3_IR_ALL_EDGE_ADJACENT_FOURTH_COEFFICIENTS_2026-10-31.zip`.