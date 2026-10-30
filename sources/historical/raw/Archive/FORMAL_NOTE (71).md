# R3: coherent transport and the non-additivity trap

## Verified source
The independently assembled two-prism complex from `R3_two_prism_certified_2026_10_27/incidence.npz` has coboundary D=d2.T of shape (11,20), rank 9, two cell relations. Exact SymPy rational/integer rank calculation verifies that after deleting **any one** of its 11 faces, the retained 10-row curvature matrix still has rank 9. Hence ker D_retained is contained in ker D_deleted. Any differentiable path of link coordinates whose retained linearized curvature is invariant has zero linearized variation of that deleted face. At nonlinear level, for each deleted face at least one of the two prism nonabelian Bianchi identities represents its holonomy, up to conjugation and based parallel transports, via five retained faces. Invariance of retained *based* holonomies (including needed transport paths) rules out independent repair. This patch is a combinatorial two-quadrilateral extrusion, not verified actual Penrose tile data.

## Exact pathwise transport identity
Let G^E be compact product group, µ0=e^-S0 Haar/Z0. For an absolutely continuous family of diffeomorphisms T_t, µ_t=(T_t)_*µ0, and vector velocity field v_t=\dot T_t\circ T_t^-1, the relative entropy satisfies

 D(µ_1||µ0)= E_µ0[S0(T_1 U)-S0(U)-log J_{T_1}(U)]

provided the transforms and Jacobians are regular. The infinitesimal derivative of the RHS under µ_t is

 d/dt D(µ_t||µ0)=E_µt[ (v_t·∇S0) - div_Haar v_t],

not the quadratic small-translation cost computed afresh from the initial µ0 at each step. Hence any pathwise small steps must be evaluated under the transported laws and may accumulate order-λ cost.

## Exact SU(2) obstruction to naïve microstepping
Let µλ(du)=exp(λ n·u)/z(λ) du, where u is unit quaternion, n identity quaternion, z(λ)=2 I1(λ)/λ. Its first moment Eµλ[u]=aλ n with aλ=I2(λ)/I1(λ). For fixed SU(2) left rotations R_θ through angle θ,

 D((R_θ)_*µλ ||µλ)=Eµλ[S(R_θ u)-S(u)]=λ aλ(1-cos θ).

Split θ into N small increments δ=θ/N. If µ_j is law after j rotations, the exact incremental expectation is λ aλ (cos(jδ)-cos((j+1)δ)). Summing gives λ aλ(1-cos θ), independently of N. Therefore a finite-angle displacement cannot be made entropy-cheap simply by concatenating N translations of angular size λ^-1/2 and using the initial-measure Taylor estimate at each step. The cost is O(λ) for fixed θ ≠0 at large λ.

## What construction would be required
The correct variational quantity for an invertible configuration-dependent link transport T is Eµ0[V_Q(TU)+S0(TU)-S0(U)-log J_T]. A method that achieves O(|Q| log λ) must exploit an actual low-action fiber or a correlated exterior rearrangement, with an independently bounded Jacobian; the small-fixed-rotation lemma does not establish this. The example shows no uniform exact invariant fiber for a single deleted face on the two-prism complex. Control may still arise by making small *net plaquette* deformations with large link rotations or by comparing the fully coupled Gibbs distribution to an explicit trial measure, but neither is proved here for arbitrary Penrose supports.

## Status
Proved: one-face-deleted rank check on abstract assembled patch; exact KL flow identity and non-additivity of microstep costs; explicit O(λ) single-link obstruction. Open: arbitrary Penrose support-local finite-curvature repair, logarithmic insertion free energy, continuum-stable R3/R2 and mass gap.
