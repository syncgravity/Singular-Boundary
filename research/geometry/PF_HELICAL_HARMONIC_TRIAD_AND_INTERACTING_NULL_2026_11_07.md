# PF-H4/H5 — Harmonic-triad chirality criterion, 3D-lift nonuniqueness, interacting quantum null

**2026-11-07 · Independently reviewable finite, conditional research statements only.** All physical PF-G0–G5/PF-H0–H6, P0–P5/T0–T5, gravity and Yang–Mills mass-gap gates OPEN. Full 11,608-check mathematical audit, exact proofs and converged quantum rotor null archived in Library `/The Singular Boundary/Proof Audits/PF_HELICAL_OBSERVER_HARMONIC_TRIAD_AND_QUANTUM_NULL_2026_11_07.zip`, ZIP SHA-256 `081e8768b93abd1daa46752f774053e9b9987f8273ef03705499df2d4863bdb9`.

**Primary source:** Sharpe dissertation v10.7, Paper 3 §§4–5,7, Remark 6, PDF path `delivery/papers/Paper_3/Sharpe_Paper3_J_Operator_Hidden_Domain.pdf`, extracted PDF SHA-256 `de86cf0c5e764ae34f2eaf6d0bcb9041c3986b4754be909b23100abaa4cb7f6d`. The paper specifies a decagonal acceptance window, a source-derived nearest-face/degree-normalized scalar, and a kinematic complementary-plane circle `z₂(t)=A exp(2π i p t)` with p=3/13,5/13,8/13. Its reported m=10 mode and 3:5:8 *continuous-time kinematic frequency* are source claims, not a verified quantum mass spectrum. The actual 3D physical lift, two-strand double-spiral definition and dynamics are OPEN.

## Exact finite harmonic theorem

With N=13 and m=10, set `T_a(F)=1/13 Σ_j F_j F_(j+a) F_(j+3a)`; `Δ=T_5−T_8=T_5−T_{−5}`. For **every** real single-harmonic field `F_j=μ+A cos(2πm j/13+φ)`, **Δ=0 identically** by Fourier orthogonality (13 does not divide m or 3m). The m=10 decagonal mode alone cannot generate the proposed static three-point observer chirality.

For `F_j=μ+A cos(2πm j/13+φ)+B cos(4πm j/13+ψ)`, exact Fourier triad resonance (m,m,−2m) gives
\[
\boxed{\Delta=\tfrac12[\sin(s)+\sin(4s)-\sin(5s)]\,A^2B\sin(\psi-2\phi),\quad s=2\pi m(5)/13.}
\]
For m=10 the prefactor is `−0.5762850408754576...`. The relative phase δ=ψ−2φ is invariant under angular-origin shift (φ,ψ)↦(φ+mχ,ψ+2mχ) and changes sign under reflection (φ,ψ)↦(−φ,−ψ), hence sinδ is a rotation-invariant, reflection-odd angular pseudoscalar. Thus a nonzero static signal requires harmonic phase mixing rather than pitch arithmetic alone. An arbitrary **non-Penrose** bounded positive scalar control with μ=1,A=.4,B=.25,φ=0,ψ=.8 already produces `Δ≈−0.01653606336665`: nonzero Δ is NOT Penrose-specific.

A **regular decagon toy**, with side-normal angles 2πk/10 and `F(θ)=[cos(π/10)−ρ max_k cos(θ−2πk/10)]²` for ρ=.73, has mirror symmetry. Exact aligned sampling gives Δ=0; general angular phase offsets obey `Δ(δ)=−Δ(−δ)`, so uniform mirror-paired phase averaging gives zero. This is a source-inspired **null control only**, *not* the authentic acceptance-window generator or degree-weighted Paper 3 data.

## Genuine 3D-lift underdetermination

The same source's planar circle has infinitely many 3D lifts `X_v(t)=(A cos(ωt),A sin(ωt),v t)`, ω=2πp, with Euclidean curvature `κ=Aω²/(A²ω²+v²)` and torsion `τ=vω/(A²ω²+v²)`. Varying v leaves the complex projection and p fixed but changes physical geometry. Therefore no unique third spatial coordinate, helical pitch or real Lorentzian time follows from the bare Paper 3 circle. The source's `p=du/dv` claim for circle Cartesian coordinates must be reconciled with time-dependent component derivative ratios.

## Explicit interacting SU(2) quantum false-positive null

A conjugation-invariant **one-loop** SU(2) quantum rotor H=α(−Δ)+β(1−½tr U) with α=1,β=3 is solved in the SU(2) class-character basis χ_n, with diagonal kinetic energies n(n+2)/4 and offdiagonal fundamental-character potential −β/2. For arbitrary **nongeometric** based-loop winding labels `r_j=(1,2,3,1,3,2,4,1,2,4,3,2,1)` and true finite quantum rotor ground-state expectations of `W_j=1−cos(r_jθ)`, the *static* chiral difference is `T_5−T_8≈+0.02731236672014`, stable under character cutoffs 16,24,32. Real Euclidean ground-state two-point covariances retain `C_5(t)=C_8(t)` to numerical precision at t=0,.1,1,2. Hence even a genuinely non-free SU(2) quantum ground state **without Penrose geometry** can show Δ≠0 solely through arbitrary geometric loop-label ordering. This is a one-loop gauge class rotor and not a coupled 3D gauge theory.

## Revised exact open test

**PF-H0:** authenticate the actual Conway-worm and two-strand Fibonacci observer source; **PF-H1:** certify its 3D longitudinal coordinate, metric and clock; **PF-H4:** map source paths to distinct gauge-invariant closed Wilson probes in a genuine interacting original-link Hamiltonian; **PF-H5:** estimate harmonic relative phases, directional 3-point and quantum Euclidean correlation against regular-decagon mirror, time-phase, shuffled-label, periodic cubic and non-Penrose interacting-rotor nulls under physically matched units; **PF-G4/G5:** seek a geometrically induced uniform h,R estimate, then prove a continuum quantum gap separately. No operator/model equivalence or gate promotions are claimed.

**Verification:** `verify_pf_harmonic_chirality_2026_11_07.py` passed 11,608 exact/finite-difference deterministic scalar/helix assertions; `verify_interacting_rotor_null.py` passed SU2 character Galerkin/covariance convergence checks. Full report, Python sources, logs and SHA-256 manifest in Library Proof Audits and locally archived ZIP. No simulation of an authenticated 3D coupled-Z5 SU2 vacuum, no Pages deployment.
