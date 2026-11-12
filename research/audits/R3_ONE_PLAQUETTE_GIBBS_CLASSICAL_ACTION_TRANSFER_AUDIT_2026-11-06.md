# R3 — One-plaquette SU(2) Gibbs calibration of the classical-action transfer gate
Research audit · 2026-11-06 · **Exact solvable-model theorem; no P0–P5 gate closed**

## Mathematical question
The cubic Wilson-flow results bound classical positive-time behavior under a bounded physical-action assumption, but this does not by itself show that the assumption describes configurations of positive probability uniformly under the interacting quantum vacuum.

## Exact single-plaquette calculation
For a single SU(2) holonomy, write x=(1/2)Tr U=cos(theta) and d=1-x. The normalized Wilson Gibbs measure is dμ_β=Z_β^{-1} exp[-βd]dHaar, where the SU(2) angle Haar density is (2/π)sin²(theta)dtheta. The partition function and expectation are **exact**:

- Z_β=exp(-β)2 I₁(β)/β.
- E_β[d]=1-I₂(β)/I₁(β)=3/(2β)+O(β⁻²) as β→∞.

In the prior cubic report's classical normalization A_h=8d/h, this implies E_β[A_h]~12/(hβ).

For fixed M>0, assume β(h)→∞ and hβ(h)→0. The event A_h≤M is theta≤arccos(1-Mh/8), and the exact probability is the ratio of the integrals of sin²(theta) exp(βcos(theta)) over this cap and over [0,π]. Its small-cap Laplace asymptotic is

**μ_{β(h)}(A_h≤M) ~ [4/(3√π)] [β(h) M h/8]^{3/2} → 0.**

Proof: on the cap, theta²=O(h) and βh→0, so the numerator after removal of exp(β) is theta_h³/3(1+O(βh+h)); the full denominator after removal of exp(β) equals √(π/2) β⁻³ᐟ²(1+O(1/β)). Substitute theta_h²~Mh/4.

## Interpretation and limits
This **disproves the general inference** that a classical bounded-action set must have nonvanishing Gibbs probability merely because β(h) grows. In particular β(h)=c log(1/h) satisfies the countermodel assumptions.

It is **not** a statement about the true interacting 3D Wilson ground state. In particular the actual physical vacuum is not this independent one-plaquette Gibbs measure; its coupling trajectory, gauge correlations, observable renormalization and vacuum density must be analyzed separately. This result does not prove the failure of physical-time smoothing or a mass gap.

**Next proof gate:** derive a flowed, renormalized, gauge-invariant curvature estimate in probability or expectation with respect to the actual interacting finite-regulator vacuum, uniformly under 3D refinement and increasing volume. Do not replace this measure estimate by classical bounded-energy smoothing or a finite-regulator positive-probability statement.

Exact numerical checks were run locally across β=5…200 and h=10⁻³…10⁻⁶ with β=2log(1/h); the asymptotic relative error decreased as expected (finite-β corrections remain). The complete proof note and executable verifier are in the separate reproducibility package shared in the conversation. No certification or Observatory node status is promoted by this audit.
