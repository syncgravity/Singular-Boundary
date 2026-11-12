# R3 / P2–T2: Coupled cubic quantum-vacuum link deletion and bare-action cap
**2026-11-06 — finite original-link SU(2) theorem, submitted for independent audit. All continuum gates OPEN.**

Model: open cubic graph with plaquettes of four distinct original links, link incidence d_e≤4; physical gauge-invariant ground state Ω>0 for H=α Σ_e C_e + β Σ_p ℓ(U_p), C_e=−Δ_e, ℓ(U)=1−½Tr₂U∈[0,2], α=g₀(h)²/(2h), β=2/(g₀(h)²h). Haar is product Haar. This is the *genuine coupled gauge-invariant model*, not an independent rotor approximation.

## Theorem A (uniform-in-volume per-link kinetic bound)
For every link e, T_e=∫|∇_eΩ|²dHaar≤2d_e β/α≤8β/α.

Proof. Define Ω̃(U_{≠e})=(∫_{SU(2)_e}Ω(u,U_{≠e})²du)^{1/2}. It is normalized, gauge invariant (Haar is bi-invariant under endpoint transformations), and has no e-gradient. Cauchy–Schwarz for derivatives of the L²-fiber norm shows that no other-link Dirichlet energy increases. Potential expectations for nonincident plaquettes are unchanged because the marginal law on U_{≠e} is identical. For each of d_e incident plaquettes, the potential change is at most 2β because 0≤ℓ≤2. Thus the trial-energy difference is at most −αT_e+2d_eβ. The ground-state variational principle makes the difference nonnegative, proving the claim.

## Theorem B (genuine interacting vacuum bare plaquette cap bound)
For any face p and M>0, define B_{p,h}(M)={ℓ(U_p)≤Mh/8}. There is C_M finite and independent of h, box size and α,β such that for small h,

ν(B_{p,h}(M))≤C_M h(1+8β/α).

Proof. Freeze the other links and choose one e on the face. The face holonomy is A u^{±1}B, so this cap is a translated/inverted SU(2) round-ball in u, with Haar volume v_h=(θ_h−sinθ_h cosθ_h)/π, θ_h=arccos(1−Mh/8), v_h=O_M(h^{3/2}). Conditional Hölder and S³ Sobolev ||f||₆²≤C_S(||∇f||₂²+||f||₂²) give cap probability ≤C_S v_h^{2/3}(1+T_e). Apply Theorem A.

## Corollary (no automatic classical-to-quantum bounded-action transfer)
The classical spatial functional in the exact nonlinear cubic dissipation audit is 𝓔_h(U)=(8/h) Σ_pℓ(U_p). For any nonempty cubic box,
ν_{h,R}(𝓔_h≤M)≤C_M h(1+32/g₀(h)^4).
Hence h/g₀(h)^4→0 implies ν_{h,R}(𝓔_h≤M)→0 uniformly in box size. For illustration, g₀(h)²=1/log(1/h) satisfies this condition.

This is an actual **coupled 3D quantum-ground-state measure** theorem about **bare zero-flow-time** classical action. It does NOT exclude nontrivial positive-physical-flow-time smoothing, renormalized curvature tightness, interacting infrared decay or a continuum mass gap. The required next P2–T2 theorem is a uniform-in-h,R quantum vacuum bound for a precisely specified renormalized, gauge-invariant *flowed* curvature observable at τ>0.

## Reproducibility and provenance
The independent Python checker passed 9,753 incidence/Haar-cap/trial-kinetic assertions for cubic subdivisions n=1…8 and θ_h small-cap limits. These finite checks do not replace the analytic variational/Sobolev argument. The **complete** report, executable verifier, test log and SHA-256 manifest are preserved in the user's Library under /The Singular Boundary/Proof Audits/R3_COUPLED_CUBIC_QUANTUM_VACUUM_LINK_DELETION_2026-11-06.zip. Preserve existing P0–P5 and T0–T5 OPEN statuses; do not modify canonical theorem counts. No public deployment.
