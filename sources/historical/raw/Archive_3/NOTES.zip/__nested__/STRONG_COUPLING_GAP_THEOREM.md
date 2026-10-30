# A uniform strong-coupling gap for SU(2) gauge Hamiltonians on Penrose rhombus patches

**Status:** rigorous reduction to an existing weak-interaction stability theorem; existential threshold, not an explicit numerical strong-coupling range; not a continuum gap theorem. October 26, 2026.

## 1. Setting

Take finite, connected, face-complete subcomplexes `G_N=(V_N,E_N,F_N)` of a fixed-scale *genuine* Penrose rhombus tiling (edge length `a>0`) with natural/free spatial boundary: only included edges and complete included faces enter the Hamiltonian. Assume the standard nondegenerate rhombus embedding. Define the full link Hilbert space `H_N^full = L²(SU(2)^{E_N}, Haar^{E_N})` and the gauge invariant subspace `H_N^phys` fixed by vertex gauge transformations. With right/left-invariant Laplace operators acting on links, let

`H_N = sum_{e in E_N} a_e (-Delta_e) + sum_{f in F_N} b_f (1 - (1/2) Re Tr U_f)`, with `a_e >= a_* >0` and `0<=b_f<=b^*`. All constants are independent of N. No uniform upper bound for `a_e` is needed if applying the variable on-site theorem with on-site gaps bounded below. For uniform application of some variant theorems that impose more, bound `a_e/a_*` above as well.

The magnetic term is a bounded real multiplication operator, with individual norm <=2 b_f. The full Hamiltonian is selfadjoint on the electric operator domain (the magnetic perturbation is bounded in each finite volume) and commutes with vertex gauge transformations. Normalizing by `a_*` gives an on-site gap >=3/4 and local perturbations of strength O(b^*/a_*).

## 2. Uniform geometric embedding lemma

Choose a fixed square grid of side `ell = a/4` in the physical plane, independent of N. Assign each spatial edge to the grid cell containing its midpoint (with a fixed tie-break rule). The rhombus tiling is a Delone set of bounded local complexity, and there is a uniform bound `M` on the number of edge midpoints falling inside one grid cell, independent of N. A direct argument avoids relying on a deep quasicrystal theorem: (i) each edge is a unit-length segment in one of finitely many directions; (ii) the Penrose tiling has uniformly bounded vertex degree `D`, and (iii) vertex locations are uniformly discrete, with minimum distinct-vertex separation `r0>0`; all edge midpoints in a fixed cell have endpoints in a fixed-radius enlargement of that cell, where packing bounds the vertex count, and each vertex contributes at most D incident edges. Hence at most M edge midpoints per cell.

Every face has four edges, diameter <=2a, and its edge-midpoint cells lie within a fixed grid graph distance `R` (depending on a/ell only) of a face reference cell. Assign each face to one of its edge cells. At most `Q` faces are assigned to one cell, where `Q <= 2M` because each edge belongs to at most two rhombi; no dependence on N. The occupied cells form an arbitrary finite subset `Lambda_N` of Z²; no periodicity or translation covariance is needed.

Group the links assigned to a cell x into one local Hilbert space `K_x = tensor_{e in E_x} L²(SU(2))`. Then `H_N^full = tensor_{x in Lambda_N} K_x`. Define `h_x=sum_{e in E_x} (a_e/a_*)(-Delta_e)`; each `h_x` has unique constant ground state and a gap >=3/4 (because each cell is occupied). Let `Phi_x` be the sum of the normalized magnetic plaquette potentials assigned to cell x. Each `Phi_x` is selfadjoint, supported on the Z² ball `B_R(x)`, and `||Phi_x|| <= 2Q b^*/a_*`.

This verifies *exactly* the structural hypotheses of the weakly interacting on-site-gapped framework on arbitrary finite subsets of Z², including inhomogeneous local on-site terms and interactions. The geometry is fixed scale: changing a changes the identification constants unless ell scales proportionally.

## 3. Stability theorem invoked, with attribution

Theorem of Yarotsky on weak finite-range perturbations of product-gapped Hamiltonians, as cited and restated in Henheik–Teufel–Wessel, **Local stability of ground states in locally gapped and weakly interacting quantum spin systems**, *Letters in Mathematical Physics* 112:9 (2022), Introduction and Sections 1–3. Their definition permits site-dependent `h_x` with a uniform on-site gap, and site-dependent bounded interactions `Phi_x` on balls of fixed radius on arbitrary finite subsets of `Z^nu`. They explicitly state that sufficiently small interaction strength gives a unique ground state and a gap independent of volume (Introduction, after the weak-interaction definition). This *stability result is imported*; its underlying proof is not reproduced here.

For the fixed range R and gap g=3/4 there exists a strictly positive, possibly non-explicit threshold `c_stab(2,R,3/4)` and a positive `gamma_stab(2,R,3/4)` (possibly depending on the chosen interaction size below threshold) such that for all finite patches, when `2Q b^*/a_* < c_stab`, the normalized full Hilbert-space Hamiltonian has a unique ground state and `gap(H_N^full) >= a_* gamma_stab >0`, with gamma independent of N.

**Technical caveat:** the primary 2004/2005 Yarotsky formulations should be checked at theorem-and-assumption level before submitting this corollary for publication. In particular, one must ensure the version used to conclude *finite-volume spectral gap* applies to arbitrary `x`-dependent on-site terms, not just to the stated uniform local response theorem. The 2022 source explicitly asserts the gap for its weakly interacting class, supporting the corollary. This memorandum documents a formal theorem-application proof, not an independently reproduced Yarotsky cluster expansion.

## 4. Restriction to Gauss-law physical Hilbert space

All terms are invariant under local SU(2) transformations. The unique ground state in the full Hilbert space is gauge invariant (the symmetry group preserves the one-dimensional ground-state eigenspace; and the ground state can be chosen strictly positive, while connected gauge transformations cannot act by a nontrivial continuous positive character). More directly, positivity improving of the elliptic kinetic operator with bounded real potential on the connected compact configuration manifold gives a strictly positive ground-state eigenfunction; uniqueness plus invariance of its absolute value enforces gauge invariance. Hence its ground energy coincides with that of `H_N^phys` and the restricted physical gap is at least the full gap:

`H_N^phys - E0(N) >= a_* gamma_stab (I - |Omega_N><Omega_N|)`.

This is an **interacting and spatial-volume-uniform strong-coupling result**. The constant is existential, depends on bounded local Penrose geometry and the ratio b*/a*, but NOT on the patch size. It does NOT use the J operator, require every face to have nontrivial holonomy, or assert a continuum gap.

## 5. Additional sharp unperturbed Gauss-law bound

The electric Hamiltonian on the physical Hilbert space alone admits `H_E|phys >= 3 a_* (I - P_const)` for connected triangle-free Penrose rhombus patches containing a face. Proof: Peter–Weyl spin networks assign SU(2) irreps to edges. An occupied vertex of the nontrivial-spin support cannot have support-degree one because `Inv(V_j)=0` for j>0; therefore the finite nonempty support contains a cycle. The Penrose tiling graph is bipartite with no cycles shorter than four, so it has >=4 nontrivial edges, each costing at least `(3/4) a_*`. The fundamental Wilson loop on a four-edge rhombus witnesses sharpness for equal coefficients. The unperturbed **full-space** gap remains only `(3/4) a_*`, which is the relevant lower gap for the generic product-state stability theorem above.

## 6. Limits, negative results and research interpretation

* This argument gives no explicit numerical threshold. It does not certify that the beta_ref=3.5 Stage 26 Wilson action lies within the strong-coupling neighborhood, and the transfer-to-Hamiltonian coupling map still requires an exact action-level audit.
* A positive gap in electric Hamiltonian energy units is **not** a uniform nonzero gap in physical energy units as `a ->0`; the local scales `a_*`, `b*`, and their beta dependence must be renormalized.
* Site-dependent geometry can be embedded in `Z²` for theorem applicability without changing the physical gauge graph. The embedding is a grouping of tensor factors, not an equivalence to a square-lattice gauge action.
* The theorem applies to Penrose, square and any uniformly discrete, bounded local-complexity rhombus/quadrilateral complex satisfying the same packing/overlap conditions. It is NOT a Penrose-specific mass-gap mechanism; C5 covariance transports the bound but does not strengthen it.
* We did NOT prove uniform conditional tensorization for the interacting ground-state density. That alternate approach is unnecessary for an **existential** strong-coupling gap after the stability-theorem reduction, but deriving mixing may still be valuable for explicit thresholds.
* Local conditional Poincare constants alone never imply dimension-independent tensorization without a separate high-temperature/uniqueness condition (standard metastability counterexamples).

## 7. Literature

1. D. A. Yarotsky, *Perturbations of ground states in weakly interacting quantum spin systems*, J. Math. Phys. 45 (2004), 2134–2152, DOI 10.1063/1.1705718.
2. D. A. Yarotsky, *Uniqueness of the ground state in weak perturbations of non-interacting gapped quantum lattice systems*, J. Stat. Phys. 118 (2005), 119–144, DOI 10.1007/s10955-004-8780-x.
3. D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, Comm. Math. Phys. 261 (2006), 799–819, DOI 10.1007/s00220-005-1456-9.
4. J. Henheik, S. Teufel, T. Wessel, *Local stability of ground states in locally gapped and weakly interacting quantum spin systems*, Lett. Math. Phys. 112 (2022), article 9, https://doi.org/10.1007/s11005-021-01494-y. They restate the finite-subset, site-dependent local weak-interaction class and discuss the Yarotsky uniform-gap consequence.

**Proof-status conclusion:** the graph-embedding lemma, Gauss-law electric bound, and implication from the quoted generic weak-interaction stability theorem to a volume-independent *interacting* gap are mathematically specified. The gap threshold is existential, not numerically computed; independent proof of the imported stability theorem and a continuum limit are not claimed.
