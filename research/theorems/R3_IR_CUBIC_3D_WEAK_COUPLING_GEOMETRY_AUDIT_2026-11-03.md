# R3-IR — Three-dimensional original-link weak-coupling extension and numerical-threshold audit (2026-11-03)

**Scope:** application of published weak-interaction gap stability to 3D finite cubic SU(2) lattice gauge Hamiltonians. No explicit volume-independent numerical coupling threshold, no physical coupling z=1 result, no continuum 4D Yang–Mills mass gap. Complete expanded note, deterministic geometry verifier and log are in the conversation archive R3_IR_CUBIC_3D_WEAK_COUPLING_GEOMETRY_AUDIT_2026-11-03.zip.

For an open cubic lattice of side L plaquettes, there are E_L=3L(L+1)^2 original SU(2) links and F_L=3L^2(L+1) elementary plaquettes. The original-link Hamiltonian is
\[
H_L=K-\frac12\sum_p z_p\chi_1(U_{\partial p}),\quad K=-\sum_{e,a}X_{ea}^2.
\]
Each original link rotor L²(SU2) has a unique constant ground state and gap 3/4. Partition its original links into sites indexed by the starting vertex x (all outgoing x→x+e_mu links in one site). Every site free Hamiltonian is a sum of up to 3 independent electric rotors with unique product ground state and gap >=3/4. The plaquette based at x in plane (mu,nu) uses exactly (x,mu),(x,nu),(x+e_mu,nu),(x+e_nu,mu), so it touches only x,x+e_mu,x+e_nu. This interaction has lattice-cell diameter <=2, each original edge belongs to at most four plaquettes, and each anchor x contributes at most three such interactions. Thus the aggregate anchored interaction norm is <=3 sup_p |z_p|.

Yarotsky's published weak finite-range perturbation theorem (CMP 261, 799–819 (2006), original preprint https://arxiv.org/abs/math-ph/0412040, Theorem 1) includes infinite-dimensional on-site spaces and an *existential*, uniform-in-volume positive spectral gap for sufficiently small local perturbation norms. Boundary/site conventions for finite arbitrary regions and local couplings are discussed in Henheik, Teufel and Wessel, LMP 112, 9 (2022), https://link.springer.com/article/10.1007/s11005-021-01494-y. Applying the standard finite-region version, there exist constants z_*>0, gamma_*>0, independent of L, such that
\[
\boxed{\sup_p|z_p|<z_*\implies {\rm gap}(H_L)\ge\gamma_*>0,\ \forall L.}
\]
The unique ungauged ground state must be Gauss-invariant because SU(2) at every vertex is connected and has no nontrivial one-dimensional unitary character. The physical reducing subspace contains this ground vector, so the physical gap is >= the ungauged gap. This covers *homogeneous nonzero* z in an unspecified weak-coupling interval on full three-dimensional finite cubic spatial lattices, not merely thin strips.

**Threshold audit:** the inspected sources do not furnish a computable numerical value of the local smallness constant c_3D. The mapping only gives symbolic z_*<=c_3D/3. Do not claim an explicit positive numerical volume-uniform threshold.

**Independently explicit but volume-dependent bound:** on the Gauss-invariant open cubic lattice every nontrivial spin network requires a closed occupied edge cycle; the shortest has four links and every nontrivial link Casimir >=3/4. Thus gap(K_physical)=3. Since the operator norm of the whole magnetic perturbation is <=sum_p|z_p|, min–max yields
\[
\boxed{{\rm gap}(H_L^{\rm phys})\ge3-2\sum_p|z_p|\ge3-6L^2(L+1)z_{\max}.}
\]
For homogeneous z the explicit sufficient finite-volume condition is |z|<1/[2L²(L+1)]; it shrinks to zero with L, so cannot replace the nonconstructive uniform small-coupling corollary.

**Checks:** deterministic Python enumerator verifies the 3D cell/face/edge geometry, maximal link-face incidence, and Weyl rational thresholds for L=1,...,10. This is not verification of the imported stability theorem.

**Open:** extract a numerical z_* from a quantitative cluster-expansion stability proof, then address physical z=1 and continuity of a mass gap in physical units along a 3+1D nontrivial continuum limit.