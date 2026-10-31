# R3-IR-562 — Oriented 3D Penrose-prism cellular chains, gauge invariance and candidate canonical Wilson Hamiltonian

Date: 2026-10-31. Provenance: recovered original Penrose generator and user dissertation v10.7, Chapter 3. The dissertation specifies a *coupled Z5* construction distinct from a separable product; the extruded prism below is an **alternative candidate**, not its claimed derivation.

## Chain complex construction

For a finite edge-connected planar Penrose face patch (V,E,F), make bottom and top copies of every V and E, a vertical edge at each V, bottom and top faces for each F, a vertical rectangular face at each E, and a 3-cell prism for each F. Explicit orientation:
- bottom horizontal edge e directed source->target, top copy identically directed, vertical edge v bottom->top;
- horizontal bottom 2-cells carry original oriented face boundary s_fe, and horizontal top 2-cells carry opposite boundary orientation -s_fe;
- side 2-cell at edge e:u->v has boundary e_bottom + z_v - e_top - z_u;
- 3-cell over planar face f has boundary bottom_f + top_f - Σ_e s_fe side_e.

These yield integer matrices ∂1:C1→C0, ∂2:C2→C1, ∂3:C3→C2. Computed exactly on six independently reconstructed candidate patches: **∂1∂2=0 and ∂2∂3=0** (integer arithmetic), ranks (M5) (47,51,14) on cell counts (48,98,65,14), and (M7,11,13,15) ranks (45,50,14) on counts (46,95,64,14). M9 is again (48,98,65,14) and ranks (47,51,14). Euler characteristic 1 and b1=b2=0 for the tested patches. Every chosen bottom chord remains non-tree in the constructed 3D rooted spanning tree. Its three incident elementary plaquettes consist of deleted bottom f0, one retained bottom neighbor, and one retained vertical side; **two** remain in the deleted Hamiltonian.

## Gauge configuration and constraints

Associate U_e∈SU(2) to each oriented 3D edge e, with U_{ar e}=U_e^-1; vertex gauge h_v acts U_e→h_source U_e h_target^-1. For an oriented face boundary word e1^s1...e4^s4 in cyclic order, p_f(U)=1/2 Tr(Π U_ei^si). These class functions are gauge invariant. Numerical random gauge checks across **all** elementary faces on six patches gave max absolute trace change <7e-16. Infinitesimally, at each vertex v the gauge generator G_v^a sums source left derivatives and target right derivatives with signs selected by the gauge action; physical wavefunctions satisfy G_v^a Ψ=0 (equivalently invariant under the full product vertex-gauge group). Because of the global gauge redundancy, these constraints are not all independent.

## Explicit candidate Hamiltonian and limitations

On the gauge-invariant Hilbert space L²(SU(2)^E,dHaar)^Gauge, an explicitly specified candidate **discrete** Hamiltonian is

  H = (g_E²/2) Σ_{e,e'} (M1^-1)_{ee'} D_e·D_e' + Σ_{f in retained 2-cells} β_f [1-p_f(U)].

Here M1 is the fully assembled SPD 3D candidate Whitney 1-form mass archived under R3-IR-560 and D_e=Ad(V_e)X_e are rooted SU2 derivatives for the fixed rooted spanning tree. For the *specified rooted model*, the quadratic electric form is defined by this expression and the potential by the complete Wilson face set. The prefactors g_E² and β_f are **independent explicit model parameters**, not yet derived together from one continuum action. This proposal is gauge invariant on physical gauge-invariant functions because all D_e transform in the common adjoint frame at the root under vertex gauge action. Positivity of the electric form is inherited from SPD M1; gauge-invariant Wilson potential is bounded on each finite patch. A Friedrichs form defines a self-adjoint finite-regulator operator under standard smooth compact configuration assumptions.

**Not yet established:** This is not a derivation of canonical Yang-Mills kinetic energy from a 3+1D action, nor a proof that inverse Whitney M1 is the correct gauge-field electric metric rather than its dual or another mass/hodge map. Scaling and anisotropic β_f are uncalibrated; there is no continuum running-coupling prescription, detailed canonical symplectic derivation, or proof that this is equivalent to dissertation's nonseparable coupled Z5 operator. The oriented cellular Bianchi identity ∂2∂3=0 is combinatorial and should not be confused with the non-Abelian cube-holonomy identity (which requires parallel transport). No continuum mass gap is proved.

The protected chord is coupled to **two** retained Wilson faces, so in a crude bounded forcing estimate its size is B_e≤|β_neighbor|+|β_vertical|, not one retained face. The R3-IR-556 sector-Sobolev cap argument may apply to the explicitly defined rooted candidate if its assumptions on transport independence and the unperturbed Hamiltonian hold; **no physically derived refinement scaling** is presently established.

## Reproducibility and source recovery

Executable fully verified local script `construct_oriented_prism_gauge.py` is preserved in ChatGPT Library `/The Singular Boundary/Source/` (SHA256 `76606f2e4994dcec19dd7a7025a48e50d848c4ad7721227cd513e6297e79f540`); per-approximant JSON `oriented_prism_gauge_results_2026-10-31.json` SHA256 `a2ddcbc583d6d15621e73de086e4a25227040ba737fa6b358a1453dcbfb8af17`. Existing full 3D mass matrices are Library-only. No NPZ in Git.

## Next genuine geometric question

To honor dissertation §3, develop a **directly coupled Z5-derived three-dimensional cell structure** and a comparison map to the prism complex; don't claim the prism realizes the author's extra compact coordinate. A separate action-level derivation and Gauss-law operator-domain audit must precede any physical continuum claim.
