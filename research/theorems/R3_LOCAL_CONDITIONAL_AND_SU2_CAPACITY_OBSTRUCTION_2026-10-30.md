# R3-IR-548 — Local conditional separation and SU(2) center-capacity obstruction (2026-10-30)

## Result 1: full radial projection is not fiberwise conditioning

The valid R3-IR-547 identity concerns **Haar-fiber averaging** PΩ, using the self-adjoint invariant radial subspace and P L = L_rad P. It does not assert that the original PDE, at a **fixed** spectator-link configuration, is a closed one-dimensional radial Schrödinger equation. The full anisotropic electric operator contains off-diagonal first-order directions and their mixed second-order terms. These survive fixed-spectator differentiation. A concrete elliptic toy example is L=∂x²+2c∂x∂y+∂y² on the two-torus with |c|<1 and Ω=1+ε cos(x+y)>0. Then 2c∂x∂y Ω=-2cε cos(x+y), which is not part of the x-only Laplacian at fixed y. A spectatorwise heat-kernel Harnack argument must control those cross derivatives or derive a genuine conditional generator; it cannot be obtained by copying the globally projected q-equation.

## Result 2: a vanishing-capacity family defeats global Fisher-energy control

On SU(2), let p=Tr U/2=cos u, u∈[0,π], with normalized Haar radial measure (2/π)sin²u du. For any fixed κ>0 and 0<r<1/2 define

  f_r(u)=1-(1-r)exp[-sin²u/r²],  Z_r=∫f_r² dHaar,  Ω_r=f_r/sqrt(Z_r).

These are smooth positive, center symmetric and normalized; Ω_r(0)=Ω_r(π)=r/sqrt(Z_r), while Ω_r tends to 1 outside shrinking neighborhoods of the centers. Their electric Dirichlet energy under the exactly closing fundamental-cycle rotor diffusion L_rad=κ(∂u²+2cot u ∂u) is

  E_r=κ/Z_r ∫ |∂u f_r|² dHaar = O(κ r) -> 0.

Proof: ∂u f_r=(1-r) (2sin u cos u/r²) exp[-sin²u/r²]; for u near 0 or π this is of order u exp[-u²/r²]/r²; the weighted volume is O(u² du), giving ∫u⁴ e^{-2u²/r²}du/r⁴=O(r). Away from these neighborhoods the integral is exponentially small. Also Z_r→1.

For center caps C_δ={|p|≥1-δ}, take δ_r=r⁴. The angular cap radius is O(r²), so f_r(u)=r+O(r²) uniformly inside the cap, and hence

  Pr_{Ω_r² Haar}(C_(r⁴))/Pr_Haar(C_(r⁴)) = r²(1+O(r))/Z_r -> 0.

This is a constructive and *sharp-in-principle* obstruction: even kinetic energy tending to **zero**, along with strictly positive smooth center-symmetric densities, does not imply a uniform relative lower cap probability when cap radii shrink. Individual finite r amplitudes can be realized as unique ground states for a suitable smooth bounded rotor class potential V_r=L_rad Ω_r/Ω_r by the ground-state transform; these potentials are **not uniformly bounded** and are **not the physical Wilson magnetic potential**. Consequently the family does not disprove the desired specific Penrose Hamiltonian bound.

Numerics (κ=2.362228738429273, from original archived M5 Whitney matrix; this is used only as the local diffusion constant): r=.1 gives E≈.11388001 and cap/Haar ratio ≈.01229186 at δ=10^-4; r=.05 E≈.06369556, ratio≈.00279444 at δ=6.25e-6; r=.025 E≈.03358219, ratio≈.00066219 at δ≈3.90625e-7. Executed script: research/scripts/audit_local_conditional_capacity.py.

## Consequences for Penrose research

1. A *global* Dirichlet/Fisher-energy estimate for Ω, even one approaching 0, cannot establish positive uniform relative shrinking-center-cap mass without additional local regularity or current/score control.
2. Exact radial closure of the deleted face (R3-IR-546) still permits the valid full **projected-amplitude** inequality of R3-IR-547. Its global L1 normalization factor is not eliminated by unjustified conditioning at a fixed spectator configuration.
3. The next nontrivial obligation is to prove a **local** estimate specific to the actual Wilson interaction and finite-range (or controlled inverse-Whitney) coefficients, e.g. a uniform log-amplitude oscillation bound for the radial marginal. Neither the sector gap nor bounded total electric energy automatically supplies it.
4. Refinement-uniform center caps and the continuum Yang–Mills mass gap remain OPEN.

Persistence: Git stores theorem and source script; binary Whitney NPZ and other archives remain in ChatGPT Library /The Singular Boundary/Source. No new binary research data required.
