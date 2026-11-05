# The Singular Boundary — Uniform Interacting Theorem Bridge

**Prepared November 4, 2026 (America/Denver).** Proposed theorem-integration specification, not a proof of the continuum Yang–Mills mass gap. All audit and publication classifications remain provisional until independent mathematical review. The private main branch's existing Observatory is v2.24 (740 indexed theorem paths); this document does **not** certify any individual path by indexing it.

## 0. The problem and the model identity

**Desired conclusion:** Construct a nontrivial, four-dimensional, gauge-invariant quantum SU(2) Yang–Mills theory on Minkowski spacetime (via, for example, a rigorously reconstructed Euclidean theory on R^4) with a unique vacuum and a self-adjoint physical Hamiltonian H such that

    spec(H) ⊂ {0} ∪ [Δ,∞),    Δ>0,

with Δ a fixed physical mass/energy rather than a lattice-unit lower bound. This is the project's SU(2) target; the Clay problem's official wording quantifies over *any compact simple gauge group*, so an SU(2)-specific proof alone is not a certification of that broader statement. The Clay site continues to describe the problem as unsolved.

**Do not identify distinct regulators without an explicit comparison theorem:**
- Z5/Penrose: the historical coupled 5D integer-lattice construction and computational Penrose/square sweep programs. The dissertation's 3D extension question and the attached Stage26 data do not themselves certify a refining three-dimensional spatial SU(2) action.
- Prism: an independently constructed extruded planar Penrose complex with exact cellular chains, rooted electric form proposal, and separate coupling conventions; no established action-level equivalence to the coupled Z5 construction or genuine fixed-domain h→0 prism sequence.
- Cubic: a benchmark with *genuine geometric refinement* already present in R3-IR-586 (2026-10-31), followed by finite SU(2) Gauss Hamiltonian R3-IR-587 and finite transfer R3-IR-590. The November 4/5 P0 audit supplies independent regression and a new exact **naive quantum intertwining obstruction**; it is not the first cubical chain-refinement theorem.
- Straight-strip: many strong corrected-original-link P2 results, finite interacting states, and local spectral moments, but a 1D row is **not** a 3D spatial regulator. Transport to the cubic model is not currently justified.

## 1. Quantified target / common regulator certificate

Choose one fixed spatial domain topology and physical box-size sequence R→∞, a lattice sequence h→0, and time discretization a_t(h)→0 (or a directly justified positive-time semigroup), with locally shape-regular 3D cell complexes K_(h,R). At each scale specify a gauge-invariant algebra A_(h,R), physical Hilbert space H_(h,R)^Gauss, normalized vacuum Ω_(h,R), and a positive, reflection-compatible Euclidean transfer T_(h,R) or rigorously equivalent physical Hamiltonian H_(h,R). Derive electric and magnetic normalizations from **one** regulated action, including face measures, time anisotropy, Casimir conventions, boundary conditions, and a bare coupling trajectory g0(h). Require compatibility of observables through renormalization/blocking maps, not exact equality of fine and coarse bare Hamiltonians.

**Operator model check (cubic reference only):** the finite Hamiltonian in R3-IR-587 has H_h = [g0(h)^2/(2h)] sum_e C_e + [2/(g0(h)^2 h)] sum_f (1 - Tr(U_f)/2). This is a proposed test model and does *not* certify that R3-IR-590's symmetric Trotter transfer equals the transfer of a unique 4D Wilson action at every time-spacing.

**Exact obstruction to naive scale intertwining (audited separately):** for the fundamental coarse Wilson loop W and the coarse→fine holonomy pullback J_h, K_h W = 3 α_h W while K_(h/2)J_hW = 6 α_(h/2)J_hW. Intertwining this example demands 2 α_(h/2)=α_h, or g0(h/2)^2=g0(h)^2/4 in the above normalization. A naive sum of fine Wilson face potentials likewise does not equal the coarse Wilson potential on all fine connections. Thus geometric incidence compatibility, isometric cylindrical pullback, and *Hamiltonian* compatibility are three different questions. This is not a no-go theorem for renormalized Yang–Mills.

**Proposed continuum observables:** gauge-invariant, renormalized/smeared local Wilson-derived fields indexed by fixed *physical* supports; keep supports fixed as h→0. Bare microscopic character χ1 at one shrinking plaquette, without an appropriate renormalization, cannot automatically serve as a nontrivial continuum observable.

### The quantifiers that must survive

Let F run over a **specified dense gauge-invariant continuum test algebra** (or an approximating family F_(h,R) whose OS-created vectors are dense after reconstruction). Let C_(h,R)^F(t) denote the connected positive-time two-point function of the *interacting* vacuum at physical time separation t≥0. A target bound strong enough to imply the gap is

    for some M>0, independent of h and R,
    for every fixed F there are t_F≥0 and C_F<∞, independent of h and R, such that
    0 ≤ C_(h,R)^F(t) ≤ C_F exp(-M t),   for all t≥t_F,

along the exact regulator/refinement and large-box sequence used to construct the continuum theory. The lower zero uses reflection positivity and self-correlations of centered F; mixed complex correlations require Cauchy–Schwarz or polarization and need not be nonnegative. The common decay rate M must not deteriorate as h→0 or R→∞; each amplitude C_F may depend on F. If time steps are discrete, the bound must be expressed in *physical time* t=k a_t and the continuum extension must be justified.

Independently prove convergence of the full renormalized Euclidean Schwinger functions/distributions with sufficient regularity, Euclidean covariance, symmetry, reflection positivity and clustering to apply an appropriate corrected OS reconstruction theorem. Establish that the OS Hilbert space is nontrivial, that a nonvacuum state or observable has nonzero limit norm, and that reconstructed gauge-invariant fields/dynamics meet the field-theoretic existence requirements. Quantify convergence rather than merely select incompatible subsequences for different observables.

## 2. Elementary conditional bridge lemma (proved here, not a Yang–Mills gap proof)

**Lemma — positive-time spectral support from common-rate decay.** Let (H,Ω,H_phys) be an OS-reconstructed Hilbert space with H_phys≥0, H_phys Ω=0, and a dense linear set D contained in Ω^⊥ of vacuum-centered positive-time test vectors. Suppose there is M>0 such that for every ψ∈D,

    0 ≤ ⟨ψ,exp(-t H_phys)ψ⟩ ≤ C_ψ exp(-M t),  t≥t_ψ,

where C_ψ<∞ and t_ψ<∞ may depend on ψ, but M does not. Then the spectral projection 1_([0,M))(H_phys) vanishes on Ω^⊥, so spec(H_phys)⊂{0}∪[M,∞). If Ω is cyclic and D is dense in Ω^⊥, no hidden physical excitation of energy between 0 and M can be missed.

*Proof.* Write μ_ψ(B)=⟨ψ,1_B(H_phys)ψ⟩, a finite positive measure. For any 0≤a<M,

    exp(-a t) μ_ψ([0,a]) ≤ ∫_[0,a] exp(-tE) dμ_ψ(E)
                                ≤ ⟨ψ,exp(-tH_phys)ψ⟩
                                ≤ C_ψ exp(-M t).

Let t→∞ to obtain μ_ψ([0,a])=0. Exhaust [0,M) by a↗M. Thus the spectral projection onto [0,M) kills each ψ∈D; boundedness of the projection and density extend this to Ω^⊥. QED.

**How the lemma is actually useful:** if finite-regulator connected self-correlations obey a common physical-rate bound, and their limit is the continuum OS correlation of the corresponding centered test vectors, the bound passes to the limit; the lemma then proves a spectral gap *conditional on* all other reconstruction assumptions. The lemma merely exposes the missing estimate: it does not establish uniform decay, the 3D interacting state, or the required OS limit. A finite-volume gap with h-dependent Δ_h does **not** meet the lemma's uniform M condition.

**Nontriviality is independent:** the zero-field limit can satisfy the same decay inequality vacuously. Require, for a physically renormalized nontrivial field F,

    liminf_(h→0,R→∞) ||[F_(h,R)-⟨F_(h,R)⟩] Ω_(h,R)||_OS^2 > 0,

in a precise positive-time OS test-vector setting, with an actual finite limiting value and a compatible limit. Also show the dynamics is the claimed Yang–Mills theory, rather than just an arbitrary massive Gaussian or zero theory.

## 3. Gate-interface matrix and required bridge certificates

| Gate | Currently source-supported | Continuum-facing bridge certificate not yet supplied | Stop rule |
|---|---|---|---|
| P0 identity/topology/action | Existing cubical dyadic chain refinement (R3-IR-586), finite Gauss Hamiltonian (R3-IR-587), finite symmetric positive transfer (R3-IR-590), independent incidence/restriction audit (draft PR #56) | Specify a single 3+1D action and g0(h), a_t(h), compatible gauge observables/blocked fields and coherent R→∞,h→0 measures; separately identify or distinguish historical Z5/prism family | No genuine 3D refinement, no common action or no physical-time meaning |
| P1 original-link and Gauss | Corrected exact link/face operators and local spin-network recoupling, mostly on strips; cubic finite gauge covariance | Self-adjoint Gauss-restricted physical H_(h,R), plaquette and electric operators with scale- and volume-controlled domains and correct unbroken gauge symmetry on the *chosen* P0 model | Strip result transported without a proved intertwiner/inequality |
| P2 interacting state and nonlinear estimates | Finite straight-strip positive unique ground state, thermodynamic energy density and locally normal subsequences; genuine Poisson five-state MPO and a posteriori Schatten brackets, width N~m² still unresolved | A three-dimensional, all-coupling/renormalization-trajectory construction or equivalent controlled interaction, with uniform local moment/cluster estimates; physical Gauss-invariant response computed/controlled at joint high spin, width, scale | Finite N, formal Borel, matrix-space bound or polynomial tensor representation presented as a physical continuum state |
| P3 Penrose-specific Wilson current | Face Ward and candidate signed current / completed-cage mechanisms | If Penrose-specific route selected, prove the genuine signed current within the certified 3D interacting vacuum; alternatively exhibit a completely different gap mechanism. P3 is **route-specific**, not a universal axiom of all Yang–Mills proofs | Current estimate on deleted/modified model substituted for full vacuum |
| P4 infrared spectrum | P-78 local positive first moment, conditional quantitative lower spectral weight above a positive threshold, periodic cubic *quadratic tangent* curl spectrum | Common-in-(h,R) positive-time *connected* correlation decay at rate M>0 in physical units for a dense gauge-invariant family; suppress soft low-frequency weight, not just show high-frequency response | First/second spectral moments or fixed finite gaps interpreted as an interval free of spectrum |
| P5 reconstruction | Finite transfer positivity and locally normal strip states | Full 4D OS/axiomatic continuum construction, common limits, Euclidean invariance, nonzero renormalized fields, cyclicity/density, unique vacuum, and above spectral lemma applied to the reconstructed H | Positivity on finite Trotter steps confused with an interacting 4D continuum OS theory |

**Critical dependency distinction:** the P0→P1→P2/P4→P5 chain is **necessary within this proposed route**. P3 is a possible Penrose-specific *mechanism* feeding P4, not inherently required if a different rigorously established infrared mechanism works. P2's one-dimensional strip lemmas are transferable only with explicit 3D operator/model comparison and preservation of every constant and norm used; otherwise they remain supporting examples.

## 4. Progress is not a single percentage

Use **six explicit evidence grades**: `source-located`, `source-reviewed`, `reproduced-finite`, `proved-in-specified-model`, `scale-uniform-proved`, `continuum-certified`. A grade must be attached to a *specific claim/model/quantifier*, not to an entire gate or file count. In particular, historical claim count ≠ certified theorem count; no publication-ready grade until independent review and source-identity acceptance.

Use four nested outcome tiers:
- **T1 — geometry/provenance:** exact incidence, orientation, chain maps, max diameter→0 and source bytes. No interaction or time.
- **T2 — quantum regulator:** a gauge-invariant *interacting* Hamiltonian and same-action temporal measure/transfer at each h, with rigorous domain/coupling conventions. No uniform gap.
- **T3 — uniform interacting estimate:** states, observables and common-rate spectral/cluster bounds under R→∞ and h→0 with physically scaled M, including nontrivial field response. This is the principal unsolved bridge.
- **T4 — OS continuum theorem and gap:** complete nontrivial QFT axioms, matched limits, dense reconstructed field vectors, unique vacuum, and the conditional bridge lemma's hypotheses proved. Only T4 closes the SU(2) theorem.

A tighter trace-norm certificate, a new same-grade norm, a larger Monte Carlo sweep, or another fixed-graph Ritz gap changes the *tools* but does not automatically advance T2→T3 or T3→T4. Any refinement claim must display its quantifiers, model identity, physical units and blockers alongside its data.

## 5. Proposed research sequence (conditional, not a schedule)

**Decision D0:** Choose either (C) cubic as the primary *proof* regulator, while keeping coupled-Z5 Penrose as a distinct historical geometry/conjectured universality research program, or (A) original Z5 if an authentic 3D action/refinement generator can be recovered and verified. Do not condition all proof progress on demonstrating Penrose equivalence; publication can separate a rigorous cubic track from a geometric Penrose track.

**Work package W0 — P0 physical action certificate:** pin a fixed-domain nested cubic family and large-volume sequence, face plaquette words, action in four Euclidean dimensions, spatial and time anisotropic couplings, true reflection-positive transfer/OS measure, Gauss Hilbert space, coherent local block maps and a mathematically specified asymptotically free or otherwise justified g0(h) trajectory. State which propositions are exact vs anticipated. A geometric split alone does not close W0.

**W1 — 3D operator/coupling transport:** compare the corrected original-link strip operators to the P0 3D operator, including shared-edge and Bianchi kernels; either prove a local intertwinement/commutator norm bound under blocking, or discard strip-based estimates as quantitative proof inputs. Run explicit small 3D, multi-plaquette Gauss tests preserving a cube's non-Abelian constraints. A local operator identity at h fixed can count as a T2 step; no continuum claim follows.

**W2 — physical nonlinear response:** reformulate the P-77 operator-MPO/collar response in genuine 3D graph geometry with a degree-dependent tensor network and complete Gauss projector; find a uniform upper trace-norm control or a counterexample as high spin and local graph size grow along physically relevant g0(h). Track constants, rank, boundary, time and physical length dependence. A computable **upper** bound is distinct from the existing Rayleigh/HS lower witnesses; asymptotic N~m² alone does not imply h-uniformity.

**W3 — candidate IR mechanism:** prove an interacting positive-time covariance or transfer estimate that is uniform under both scale and volume. Allow a multiscale renormalization mechanism; do not rely exclusively on weak-magnetic Yarotsky stability because z=4/g0^4 grows as g0→0. Confirm soft transverse modes from periodic cubic curl and topological sectors are not artificially projected away.

**W4 — reconstruct and rule out triviality:** build convergent gauge-invariant Schwinger distributions with OS regularity, covariance and positivity; show a nonzero renormalized local excitation and physical-unit M. Prove the **same** estimate used in W3 applies to a dense continuum family; then invoke the lemma.

**W5 — independent adversarial audit and dissertation integration:** validate original bytes/claims, all field normalizations and countercases, compare every historical model, document negative results, and submit independent theory/constructive QFT review before claiming theorem closure.

## 6. Existing evidence and draft branches

- Original cubic geometry R3-IR-586, finite gauge Hamiltonian R3-IR-587, finite transfer positivity R3-IR-590: `research/theorems/` on main.
- Existing `docs/research/PROOF_DEPENDENCIES.md`, `docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md`, historical acceptance gate.
- P-77/78 source: `research/audits/P2_SOURCE_MPO_RESIDUAL_CYLINDER_DIRICHLET_2026-11-04.md` on main.
- Conditional quantitative local f-sum refinement: draft PR #55, **not merged**.
- Independent source archive, 3D chain and naive quantum non-intertwining witness, plus conditional spectral-weight bound: draft PR #56, **not merged**.
- Clay official problem page: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ ; official formulation includes all compact simple G. The present document targets SU(2) first.

**Scientific status: OPEN.** This document is a falsifiable interface specification plus an elementary spectral lemma. It does not establish a 3D interacting uniform exponential bound, 4D OS existence, or the Yang–Mills mass gap.