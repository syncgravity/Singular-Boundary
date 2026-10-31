# R3-IR-551 — Original Penrose Wilson edge-center parity and vanishing first-order two-center-cap response

Date: 2026-10-30. This result **uses the actual Wilson potential and original rooted SU(2) electric operator**, rather than a constructed rotor potential.

## Verified geometry and exact unitary intertwining

On the archived 11-face M5 Penrose disk, edge 13 belongs to exactly selected faces f0 (deleted; oriented edge IDs [1,4,13,0]) and f10 (retained; oriented edge IDs [13,18,26,12]). Under the original BFS tree T1, edge 13 is non-tree; every rooted source transport V_j(T1) is independent of U13.

Let J13 act on L2(SU2^30) by central left translation U13→−U13. This is a unitary involution and it commutes with each transported derivative D_j=Ad(V_j)X_j: the source transport never contains chord U13, and central left translation commutes with left invariant link derivatives. Thus [J13,H_E]=0 exactly, including all inverse Whitney mixed electric terms.

Let H_b=H_E+V_other(U)-b p10(U), where the only U13-dependent retained magnetic term is -b p10, and V_other is independent of U13 (arbitrary strength). Since p10 is linear in U13, J13 p10 J13=−p10. Consequently

**J13 H_b J13 = H_{−b}.**

The deleted-face trace p0 is also odd under J13, so any two-center cap event C_delta={|p0|≥1−delta} is J13 invariant. If H_b has a unique normalized strictly positive ground-state amplitude Ω_b (true at finite connected compact elliptic regularization with bounded real potential), then Ω_{−b}=J13 Ω_b, energies satisfy E(−b)=E(b), and

**Pr_b(C_delta)=Pr_{−b}(C_delta)**

exactly for every b, not only perturbatively. The individual + and − center caps are exchanged.

At b=0, V_other is independent of the non-tree U13, while P13 Haar-link average reduces H0. Positivity and simplicity force Ω0 to be U13 independent. Because p0 is a translated SU2 trace of U13 for fixed other links, its Ω0² marginal is exactly Haar; Pr_0(C_delta)=c_delta.

By analytic perturbation of the isolated finite-volume simple eigenstate, b↦Pr_b(C_delta) is even analytic near 0 and hence

**Pr_b(C_delta)=c_delta+O_delta(b²)** for each fixed 0<delta≤1.

This does NOT provide a bound uniform in delta or graph refinement: the analytic Taylor coefficient can diverge relative to c_delta, and the gap/elliptic constants can deteriorate as the regulator changes.

## Exact conditional Haar geometry of the adjacent Wilson interaction

Fix *all links except U13*, and let p=p0 and z=p10. Each is a real linear functional of the same unit quaternion u=U13:

p=a·u, z=bvec·u, |a|=|bvec|=1. Define c=a·bvec∈[-1,1] (depends on the spectator configuration). Condition U13 on p=a·u while retaining Haar geometry on the orthogonal 2-sphere. Then

**E_Haar[z|p,others]=c p,**

**E_Haar[z²|p,others]=c²p²+(1−c²)(1−p²)/3.**

Thus the **bare Wilson local force has exactly affine radial conditional mean** and computable variance, before weighting by the interacting Ω_b. The Ω_b-weighted effective radial potential is NOT given by this Haar conditional formula without an additional estimate on fiber reweighting. It does not follow that osc(v_eff) is bounded by b alone when arbitrary strong background and kinetic couplings interact.

## Exact-source verification

Executable source `research/scripts/audit_m5_wilson_center_parity.py` verifies original archive geometry; 6 seeded link configurations yield exact sign flips for f0/f10 and unchanged other faces, plus unchanged root transports; fixed-fiber Monte Carlo tests conditional Haar first and second moments at p=±0.8, ±0.2 across 6 configurations (20,000 samples each), maximum empirical error 0.006228 under 0.014 tolerance. This tests the algebra but does not numerically diagonalize the interacting 30-link Hamiltonian.

Original 30×30 Whitney matrix is archived in ChatGPT Library `/The Singular Boundary/Source/global_whitney_11face.npz` with SHA-256 `d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf`. No binary outputs committed to Git.

**Remaining proof obligation:** uniform-in-refinement *relative* quadratic response bound |Pr_b(C_delta)/c_delta−1|≤C b² with C controlled through physical coupling and the full kinetic dynamics; or a suitable nonperturbative local Harnack/current theorem. The continuum mass gap is unproved.
