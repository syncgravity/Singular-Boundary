# R3 P2/T2: Genuine coupled SU(2) vacuum cap bound and center-saddle attraction-basin audit
**2026-11-06 · finite original-link cubic regulator · independent review pending · all P0–P5/T0–T5 gates OPEN**

## Setting
Finite open 3D cubic lattice; original links E, plaquettes P, four distinct links per face and link incidence d_e≤4. Normalize group generators iσ_j/2. Physical quantum Hamiltonian H=αΣ_e(−Δ_e)+βΣ_p(1−½tr U_p), α=g₀²/(2h), β=2/(g₀²h). Its unique smooth strictly positive gauge-invariant ground state Ω induces ν=Ω²dHaar. The exact classical *spatial* Wilson gradient flow Φ_s is distinct from quantum time evolution. Prior true-coupled-vacuum link-deletion result (draft PR #81): ∫|∇_eΩ|²≤8β/α=32/g₀⁴.

## Theorem A — genuine vacuum negative-center cap
For any plaquette p and 0<δ<1 put C⁻_{p,δ}={½tr U_p≤−1+δ} and θ=arccos(1−δ). The Haar volume of its single-holonomy cap is v_δ=(θ−sin θ cos θ)/π~(4√2/3π)δ^(3/2). Then
\[
ν(C^-_{p,δ}) ≤ C_S v_δ^{2/3}(1+32/g₀(h)^4).
\]
The constant C_S is the single-SU(2) H¹→L⁶ Sobolev constant, independent of p and the spatial volume. In particular, sup_{p,R}ν(C⁻_{p,δ_h})→0 if δ_h=o(g₀(h)^4) as g₀(h)→0.

**Proof:** Hold all links except any one e∈∂p fixed; the face holonomy is Au^{±1}B and thus the negative-center event is a translated/inverted Haar cap of fixed volume. Conditional Hölder followed by the SU(2) Sobolev inequality gives probability ≤C_S v_δ^(2/3)(1+T_e). Integrate over remaining links and use prior link kinetic bound. No factorization of the interacting vacuum.

## Theorem B — null attraction basin for individually specified unstable center equilibrium
For any center background U_e*=z_eI, z_e=±1, write z_p=∏_{e∈∂p}z_e. It is a stationary point of S=Σ_p(1−½tr U_p). Its Hessian in each Lie algebra direction is H*=(1/4)Bᵀdiag(z_p)B, with B the oriented face-edge incidence. If some link e has Σ_{p∋e}z_p<0, then the Rayleigh quotient on coordinate e is negative and the negative gradient vector field has a nonempty unstable eigenspace. The *fixed-point* basin {U:lim_{s→∞}Φ_s(U)=U*} has Haar and ν measure zero: a local center-stable manifold of positive codimension contains the eventually trapped trajectories; countable backwards flow images remain null. For an isolated negative center link with four incident plaquettes, Σz_p=−4 and the Hessian Rayleigh quotient is −1.

**Scope:** The theorem concerns convergence to each specified equilibrium, not the union of its continuous gauge orbit. No finite-time exponential estimate uniform in h or R is claimed. Initial cap control cannot be applied directly to the pushed-forward ν_s, whose density and entropy change were calculated in draft PR #84. These results do not establish fixed-physical-flow-radius curvature tightness, interacting spectral decay, Penrose equivalence, gravity finiteness, or a 4D mass gap.

## Verification and persistence
Deterministic incidence / signed-Hessian / exact Haar cap tests passed **30,448 assertions** for cubic n=2,3,4,5 and reproducible seeded center assignments. Tests corroborate algebra and cap asymptotics; they do not independently prove the center-stable manifold theorem or sample the quantum vacuum. The complete proof note, executable verifier, log, SHA-256 manifest and CRC-tested ZIP are preserved in the user's Library at /The Singular Boundary/Proof Audits/R3_CENTER_SADDLE_VACUUM_CAP_2026-11-06.zip.

Next gate: an explicitly h- and R-controlled finite-time **residence tube** bound for coupled non-Abelian flow at s=τ/h², combined with a physically renormalized fixed-support curvature observable and its interacting-vacuum probability law.
