# The Singular Boundary — R3-IR shared-link strong-field limit and collective soft-mode obstruction

**Date:** 2026-10-28. **Type:** independently derived exact face-incidence, Gaussian gauge-sector and fixed-complex semiclassical results; no Monte Carlo or new historical data. **Status:** finite simply connected SU(2) complexes only. The Penrose volume/regulator-uniform nonlinear mass gap and R2 quantum continuum remain **OPEN**.

## 1. Provenance and correct scope

The earlier repository report `R3_IR_GAUSS_TWIST_AND_STRONG_FIELD_OSCILLATOR_2026-10-28.md` proves the strong-magnetic oscillator limit for **one** open spatial rhombus. We now analyze the exact shared-link quadratic form and its fixed-finite-patch strong-field limit, without assuming that independent plaquette oscillators remain decoupled.

Primary source for the finite authentic-Penrose fixture: `HISTORICAL_Q14_CANONICAL.json`, `seed_faces_z5` (three canonical rhombi). The three face labels are transcribed into a read-only verifier. The verifier checks only the three spatial seed faces; it does **not** reconstruct all original Q14 words or certify the separate twelve-prism object. As a comparison, exact square-face-grid formulas are used only as independent combinatorial controls, **not** as substitute Penrose results. Historical source bytes were not modified. Sources describing standard rhombic cut-and-project Penrose tilings: Mazáč (2023), DOI 10.1107/S2053273323004990. A classical reference for harmonic well asymptotics is Barry Simon, *Semiclassical analysis of low lying eigenvalues I: Non-degenerate minima*, Ann. Inst. H. Poincaré Phys. Théor. 38 (1983), 295–308. The proof below gives the finite-complex local reduction and the compactness/min–max mechanism explicitly.

## 2. Theorem DL-1: exact oriented face-edge incidence and dual Dirichlet Laplacian

Let G be a finite simply connected **planar quadrilateral disk**, with consistently counterclockwise oriented face boundary cycles, no repeated face edge and each edge incident to one or two faces. Let B be its `F × E` integer face-edge incidence matrix, with entries B_fe=±1 when e appears in oriented ∂f and zero otherwise. Define L=B B^T.

Then

`q^T L q = Σ_{e interior between f,g}(q_f−q_g)^2 + Σ_{e boundary incident to f}q_f²`.

Thus L is the positive **Dirichlet dual-graph Laplacian**, with L_ff=4, L_fg=−1 if distinct faces share a single edge and zero otherwise. As a disk has a boundary and each connected component of faces reaches it, L is positive definite. In particular, with N_F faces and N_∂ boundary edges,

`0 < λ_min(L) ≤ N_∂ / N_F`,

by taking q_f=1 for all faces. For any van Hove family of simply connected rhombus patches satisfying N_∂/N_F→0, `λ_min(L)→0`.

**Proof:** on an internal edge, counterclockwise face orientations induce opposite signs, so the column of B has (+1,−1); a boundary column has one ±1. Expand `||B^T q||²`, and test on the all-ones vector. Positivity follows since zero energy forces q constant across the connected dual graph and zero at the boundary. No gauge or continuum assumption enters.

### Stronger geometric estimate for regular Penrose disks

For simply connected face-complete Penrose disk patches containing a Euclidean ball of radius R/2, lying inside a ball of radius R (allowing a bounded O(h) boundary collar), with uniformly scaled rhombus edge length h and R≫h,

`λ_min(L) ≤ C (h/R)²`

for a universal C depending only on Penrose rhombus shape bounds, not patch size. Choose a bounded Lipschitz compactly supported face-centroid test function q_f=φ(x_f/R), with φ=1 inside a smaller fixed ball and zero near the outer patch boundary. Neighboring face centroids are O(h) apart, so the numerator sums O((h/R)²) per edge, with O((R/h)²) edges; the denominator is bounded below by c(R/h)² using the uniform positive rhombus area bounds and coverage of the inner disk. The Rayleigh quotient is therefore O((h/R)²). The weaker `N_∂/N_F` estimate requires no regular-disk assumption.

## 3. Theorem DL-2: physical Hilbert space and the exact quadratic electric cross-coupling

Assume G is a simply connected open spatial disk, so Euler's formula gives `rank π₁(graph)=E−V+1=F`. After vertex-spanning-tree gauge fixing, its gauge-invariant Hilbert space identifies unitarily with

`L²(SU(2)^F, product Haar)^{Ad SU(2)}`,

where the F based face holonomies are a free generating set, and the residual SU(2) gauge action is simultaneous conjugation. The free-basis coordinate transformations preserve product Haar (Nielsen multiplication/inversion). This identification is exact for a disk but not for periodic/non-simply-connected spatial topologies without extra winding variables.

Use canonical su(2) coordinates `U_e=exp(i σ·x_e/2)` near the trivial flat connection. To first order, the based face log coordinates obey `y_f=Σ_e B_fe x_e+O(|x|²)`; the local quadratic magnetic potential is `Σ_f b_f|y_f|²/8`. For smooth based face functions, the electric Dirichlet form has principal second-order coefficient at the flat connection

`M_{fg}=Σ_e a_e B_fe B_ge`.

Thus **shared links produce off-diagonal differential couplings** even though the magnetic potential is diagonal in based face holonomies. If a_e=a and b_f=b, the exact tangent harmonic operator on `L²(R^{3F})^{SO(3)}` is

`H_harm = −a Σ_{f,g} L_fg ∇_{y_f}·∇_{y_g} + (b/8)Σ_f |y_f|²`.

This is an exact statement about the quadratic/tangent operator, **not** an identity for the nonlinear Wilson Hamiltonian at finite b.

## 4. Theorem DL-3: fixed-disk strong-magnetic harmonic limit (not uniform in disk size)

Let `H_G(a,b)=a Σ_e (−Δ_e)+b Σ_f(1−p_f)` with **uniform** positive electric and magnetic coefficients on a fixed finite simply connected quad disk. Let `E_k(a,b;G)` be its ordered eigenvalues on the **physical gauge-invariant** Hilbert space, including multiplicity. Define ε=(a/b)^(1/4). In based face coordinates, the completed Wilson potential has a **unique** zero at all face holonomies equal I, the transformed electric operator is smooth uniformly elliptic on SU(2)^F, and its principal form at that minimum is L⊗I₃.

Under `y=ε z`, the operator normalized by `√(ab)` converges in its low-lying spectral/min–max problem to the SO(3)-invariant oscillator

`ℒ_G = −Σ_{f,g}L_fg ∇_{z_f}·∇_{z_g} + (1/8)Σ_f |z_f|²`

on `L²(R^{3F})^{SO(3)}`. Accordingly, for every **fixed G and fixed index k**,

`E_k(a,b;G)/√(ab) → eigenvalue_k(ℒ_G)` as b/a→∞.

**Proof mechanism (with no volume-uniform assertion).** The spanning-tree reduction gives a smooth compact SU(2)^F manifold before imposing residual conjugation. The Wilson potential is nonnegative, with exactly one zero in these coordinates; its Hessian at that zero is positive definite (1/4 times identity in the standard logarithm convention). A fixed finite low-energy test space built from oscillator eigenfunctions localized at scale ε gives upper min–max bounds. Conversely, any bounded-rescaled-energy sequence has vanishing mass outside a fixed neighborhood of the unique potential well, and, in rescaled coordinates, uniformly bounded gradient and second-moment energy (via local positive quadratic lower bound on the potential). Compactness on bounded balls plus tail control produces strong L² limits; weak lower semicontinuity of the quadratic forms and convergence of local coefficients provide lower min–max bounds. Simultaneous conjugation is an exact compact SO(3) symmetry of the local logarithm chart and all quadratic forms, so these tests and limits restrict to invariant subspaces. This is the standard single-well harmonic approximation/min–max proof for each **fixed finite dimension**; its constants can and generally do deteriorate with F.

Diagonalizing L gives 3D oscillators with mode frequencies `ω_i=√(λ_i(L)/8)` in units of √(ab). Their ground state is rotation invariant. Any **one-quantum** mode transforms as SO(3) spin 1, and is not physical. Two quanta in a lowest-frequency vector mode can form a singlet, so the lowest physical excitation has energy `4 ω_min`. Therefore

`lim_{b/a→∞} gap_phys(H_G(a,b))/√(ab) = √(2 λ_min(L))`.

This reduces to the independently established one-rhombus value `2√2` when L=[4]. It is a real **multi-face interacting Wilson fixed-patch strong-field asymptotic**, not merely an assertion about a formal Gaussian model. It does **not** allow interchange of b/a→∞ with F→∞ or h→0 without further uniform analysis.

## 5. Corollary: the Gaussian collective low-mode cannot inherit a uniform one-face gap

From DL-1 and DL-3 the **sequential** limits obey

`lim_{G→∞ along van Hove patches} lim_{b/a→∞} gap_phys(H_G)/√(ab)=0`

for fixed uniform a,b scale parameters understood as taking the inner strong-field limit separately for each finite G. The implication follows from `gap/√(ab)→√(2λ_min(L))` and `λ_min(L)→0`. This is **not** a claim that `gap(H_G(a,b))→0` at any fixed finite ratio b/a, nor that 2+1D interacting Yang–Mills is gapless. The order of limits is crucial.

At geometric spatial refinement with h the physical link length, the *formal quadratic* gap scale `√(ab λ_min(L))` is at most O(1/R) for regular disks of fixed physical radius R because `ab∼h⁻²` and `λ_min(L)≤C(h/R)²`. The physical interacting continuum may develop a nonperturbative mass not contained in the harmonic approximation. This calculation demonstrates why one cannot infer a volume-uniform spectral theorem by tensorizing independent strong-field one-rhombus oscillator gaps.

## 6. Authentic-Penrose fixture and separate controls

The three canonical spatial seed rhombi transcribed from `HISTORICAL_Q14_CANONICAL.json/seed_faces_z5` have 10 unique edges, 8 exterior boundary edges and oriented incidence Gram matrix (after the verified consistent orientation)

`L_seed = [[4,-1,-1],[-1,4,0],[-1,0,4]]`,

with exact eigenvalues `4−√2,4,4+√2`. The constant Rayleigh quotient is 8/3. Hence the fixed-patch physical harmonic singlet gap coefficient is `√(8−2√2)`, **not** three times the one-rhombus coefficient. The report's exact script constructs B from the Z5 vertex words, orienting each face by its physical 5-star projection, and verifies matrix and eigenvalues with symbolic rational arithmetic.

For an m×m *square* quadrilateral patch, used only as an independent control, the exact dual Dirichlet eigenvalue is `λ_min=4−4cos(π/(m+1))`, which is asymptotic to `2π²/(m+1)²`. The physical Gaussian singlet gap coefficient is `√(2λ_min)` and decays as m⁻¹. **No square configuration is substituted for an original Penrose archive or spectrum.**

## 7. Next noncircular proof obligation

The needed result is not another fixed-block oscillator estimate: it must quantify *nonlinear, gauge-invariant collective coercivity* beyond the vanishing dual Dirichlet stiffness. A legitimate next certificate would control source-inserted physical transfer or a gap-producing Dirichlet form uniformly in (a) volume, (b) spatial refinement, (c) based Wilson paths and conjugation/Gauss projection, and (d) large-field/noncommutative configurations. It must retain the collective dual-Laplacian soft mode in its hypotheses rather than replace it with an assumed positive uniform local oscillator frequency. A gauge-invariant Wilson observable for a soft collective curvature mode requires actual based parallel transports and nontrivial control of logarithms/large holonomies; the formal vector field `Σ_f q_f log W_f` alone is not a globally defined spectral source.

**Classifications:** DL-1 independently proved; DL-2 independently proved local symbol and exact disk gauge identification; DL-3 independently derived fixed-disk harmonic asymptotics using standard min–max localization, with no asserted uniform constants; Gaussian soft-mode corollary independently proved **in the stated order of limits**; interacting volume/cutoff-uniform gap and quantum continuum **OPEN**.