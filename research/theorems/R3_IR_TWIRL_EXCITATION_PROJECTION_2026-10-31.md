# R3-IR — Gap-free SU(2) transport-twirl excitation-form projection

2026-10-31. Exact finite-volume theorem, for the established planar-disk potential-preserving SU(2) transport action. No regulator-uniform current bound.

Let Ω>0 be the normalized ground state of deleted-face H, A=H−E0≥0, and let U_g be the Haar-unitary action of the holonomy transports on the full original-link L² space, with U_g preserving the quadratic-form domain. Define P=∫_SU2 U_g dg, h=PΩ, r=(I−P)Ω, and Q_g=⟨U_gΩ,A U_gΩ⟩.

**TP-1.** P is an orthogonal projection onto transport-invariant amplitudes. Since AΩ=0, **⟨h,Ah⟩=⟨r,Ar⟩**.

**TP-2.** Quadratic-form Jensen gives the gap-free estimate **0≤⟨r,Ar⟩≤∫_SU2 Q_g dg**. The ground-state transform identifies the left side exactly with **∫Ω² Σ_e a_e|∇_e(r/Ω)|² dμ**. This controls the relative ground-state Dirichlet energy, not the ordinary electric Sobolev energy of r.

**TP-3.** The invariant positive amplitude h has Haar-uniform target holonomy. Let α=||r||₂<1. The normalized reference state h/||h|| yields **TV(Law_Ω(W_f),Haar_SU2)≤α** by the Hellinger overlap ⟨Ω,h/||h||⟩=sqrt(1−α²). A bound on the excitation form ⟨r,Ar⟩ alone does not bound α without an independent coercivity estimate on this noninvariant sector. Local vertex gauge-charged Casimir coercivity cannot automatically supply it.

Independent verifier: 5000 finite-dimensional positive spectral / orthogonal-projection tests, maximum excitation-split error 2.0e−15; SU2 class radial eigenvalue 3 verified. Complete report, source code and checksums in Library at /The Singular Boundary/Proof Audits/R3_IR_TWIRL_EXCITATION_PROJECTION_2026-10-31.zip. Neither the required vacuum-averaged metric defect nor regulator-uniform signed current, connected covariance, or continuum Yang–Mills mass gap is proved.