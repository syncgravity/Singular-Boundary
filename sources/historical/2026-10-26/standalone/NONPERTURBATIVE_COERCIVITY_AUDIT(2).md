# Nonperturbative coercivity audit — Singular Boundary
Date: 2026-10-26

## Claim ledger

- **Proved (finite volume):** For the SU(2) electric-plus-bounded-Wilson-potential Hamiltonian on a finite graph, the lowest eigenvalue is simple with a strictly positive gauge-invariant ground state (under strictly positive electric coefficients), and its physical gap has an exact weighted Poincaré variational characterization.
- **Proved (equivalence):** Uniform physical gap along any family of finite graphs, couplings, and boundary conditions is equivalent to a uniform Poincaré inequality for the corresponding interacting ground-state measures restricted to gauge-invariant functions.
- **Not proved:** Uniform bounds on these Poincaré constants outside perturbative strong coupling, particularly along a physical continuum trajectory. Geometry and the C5/J complex structure do not establish the missing mixing/coercivity inequality.
- **Not proved:** A unique infinite-volume ground state, continuum limit, or a positive continuum mass gap.

## The precise theorem

Let E be the finite edge set of a spatial SU(2) gauge graph, X=SU(2)^E with product normalized Haar measure, and physical Hilbert space H_phys=L^2(X)^G with G=SU(2)^V acting at vertices. Let a_e>0 and let B:X→R be bounded and gauge invariant. Define the self-adjoint Friedrichs operator H=Σ_e a_e(-Δ_e)+B on H_phys, where Δ_e is the SU(2) Laplace–Beltrami operator normalized to eigenvalues -j(j+1).

The finite-volume operator has a simple lowest eigenvalue E_0 with normalized strictly positive gauge-invariant eigenfunction Ψ_0, by compactness and positivity improvement of the elliptic heat semigroup (finite links, connected compact configuration space; B bounded). Set dν=Ψ_0²dU.

For a gauge-invariant f in the transformed form domain,

⟨Ψ_0 f,(H−E_0)Ψ_0 f⟩ = Σ_e a_e ∫_X |∇_e f|² dν.

The identity follows from the Leibniz rule and weak ground-state equation. The corresponding exact physical gap is

 gap(H|H_phys) = inf_{f gauge-invariant, Var_ν(f)>0} [Σ_e a_e ∫|∇_e f|² dν]/Var_ν(f).

Therefore gap(H_{G,a,b})≥m_* for every member of a specified graph/cutoff/boundary family IF AND ONLY IF the corresponding gauge-invariant weighted Poincaré constants are ≤1/m_*. This does not establish that such uniform constants exist.

If a_e≥a_*(a) and one obtains Var_ν(f)≤C(a) Σ_e∫|∇_e f|²dν uniformly in volume and allowed boundary conditions, then gap≥a_*(a)/C(a). The required continuum target is liminf_{a→0} a_*(a)/C(a)>0 **in a fixed physical energy normalization**. Different anisotropy conventions alter a_e and physical time conversion.

## Transfer operator formulation

For a positive self-adjoint transfer operator T with simple maximal eigenvalue λ_0>0, define H_T=−a_t^{-1}log(T/λ_0). Then gap(H_T)≥m_* iff ||(T/λ_0)|_{Ω⊥}||≤exp(−a_t m_*), where Ω⊥ is taken in the physical fibre. Showing reflection positivity and T≥0 is not enough to imply this bound. The exact Stage 26 transfer kernel and its time anisotropy still need source-level certification.

## Boundary issues

Free-boundary Penrose rhombus patches and periodic pentagrid approximants have different gauge-complex topology. Periodic noncontractible loops yield globally supported gauge-invariant functions absent from simply connected patches. No boundary-uniform estimate follows from a free-patch result without a separate argument. The demanded theorem must state its boundary family and treat interface/seam interactions explicitly.

## Geometry and J

C5 covariance of isomorphic weighted Penrose gauge complexes transports spectra and any established Poincaré constant, but does not bound the constant. J²=−I on the effective geometric representation likewise neither supplies a ground-state log-Sobolev estimate nor a physical operator inequality. Any proposed J-dependent strengthening needs a rigorously defined intertwiner and a demonstrated bound on the ground-state measure or its spectral contraction.

## Next proof obligations (not computed)

1. Audit the exact electric/magnetic Hamiltonian and temporal anisotropy of the original Wilson action.
2. Prove volume-uniform mixing/functional inequality for ν_{G,a} outside strong coupling, perhaps via scale-dependent multiscale estimates; weak-interaction stability cannot be applied once local magnetic/electric ratios diverge.
3. Establish boundary-stable estimates for free/open patch and periodic torus families.
4. Determine a continuum trajectory and prove scale-uniform control in physical units.
5. Only thereafter identify a physical scalar-sector bound and mass interpretation.

## Literature context

- Henheik, Teufel, Wessel (2022), *Local stability of ground states in locally gapped and weakly interacting quantum spin systems* (Theorem 7 quotes a Yarotsky gap/locality theorem); weak interaction setting, not a continuum result.
- Guo and Zheng (1989), *Universality and mass gaps for a series of lattice Hamiltonians with exact ground states*: variational **upper** bounds on 2+1 SU(2) mass gaps do not establish lower bounds.
- Standard SU(2) Peter–Weyl, compact-group elliptic operator theory, and ground-state (Doob) transforms underpin the finite-volume equivalence.

The gap beyond strong coupling and continuum remains unproved here.