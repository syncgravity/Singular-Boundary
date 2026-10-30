# R3-IR-432 — Ground-state Dirichlet variational form of Wilson cap susceptibility

2026-10-30. Exact finite-volume original-link SU(2) Wilson identity; not a uniform susceptibility or continuum mass-gap bound.

For the final-neighbor coupling path H(t), let Ω_t>0 be the normalized real positive gauge-invariant vacuum, E_t its energy, μ_t(dU)=Ω_t(U)^2 dHaar(U), O=k_a(W_f), and F_t=E_{μ_t}O. Write R_t=Q_t(H(t)-E_t)^(-1)Q_t and A_t=<Q_tOΩ_t,R_t Q_tOΩ_t>.

The unitary ground-state transformation v=Ω_t φ identifies the closed quadratic form of H(t)-E_t with
D_t(φ)=Σ_edges a_e ∫|∇_e φ|² dμ_t
on mean-zero gauge-invariant functions φ (with the Laplacian and metric conventions of the original-link Hamiltonian). This follows by integration by parts and (H-E)Ω=0; the magnetic potential drops out of the transformed Dirichlet form but remains in μ_t.

The dual variational characterization of the positive inverse gives the exact formula

A_t = sup_{φ smooth, gauge invariant, E_μ φ=0}
 [ 2 Cov_{μ_t}(O,φ) - D_t(φ) ]. (DV-1)

There is no presupposed uniform gap in DV-1. A constant mean shift does not affect the expression, so one can equivalently optimize over all smooth gauge-invariant φ.

For any smooth nonconstant gauge-invariant test φ with D_t(φ)>0, optimizing its scalar multiple yields the rigorously testable lower bound
A_t >= Cov_{μ_t}(O,φ)^2 / D_t(φ). (DV-2)
In particular, for smooth O, φ=O-F_t gives
A_t >= Var_{μ_t}(O)^2 / [Σ_e a_e∫|∇_e O|²dμ_t]. (DV-3)
These are LOWER bounds, not upper bounds. For a cap O supported on a shrinking region, the denominator may grow under refinement; this observation does not close the transport estimate.

Critical scope: DV-1 optimizes over global gauge-invariant functions of ALL links. Restricting the supremum to private-link functions gives only a lower bound on A_t, never an upper bound. Therefore a local electric Poincare estimate cannot be substituted into R3-IR-431 to bound its complete susceptibility without separately controlling the environmental / collective sectors of the ground-state Dirichlet form.

A uniform upper bound A_t<=C would require an adequate coercivity or sector decomposition estimate for the full weighted Dirichlet form and the particular cap source; the usual spectral-gap shortcut A_t<=Var(O)/δ_t merely reintroduces the unproved infrared gap. The mixed cap transport criterion MS-3 is still OPEN along physical Penrose refinement. No full-coupling signed cap ordering or continuum Yang-Mills mass gap follows.
