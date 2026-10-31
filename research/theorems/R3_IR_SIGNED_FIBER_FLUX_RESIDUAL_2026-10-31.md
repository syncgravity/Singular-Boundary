# R3-IR — Signed cumulative fiber-flux comparison and residual criterion

Date: 2026-10-31. Exact finite-volume theorem; no uniform Wilson current bound.

For the actual positive deleted-face Wilson ground state let Ψ(u)=ψ_f(cos u), A_f=Σ_(e∈∂f)a_e, ω(u)=2sin²u/π, D(u)=U_f(cos u)−E0. The exact radial equation is (A_f/4)(ωΨ′)′=ωΨD. Define G(u)=∫_0^u ω(v)Ψ(v)D(v)dv. Endpoint smoothness and center symmetry give G(0)=G(π/2)=0.

**SF-1:** Ψ′/Ψ=4G/(A_f ωΨ), and therefore 𝔗_f=(4/A_f)∫_0^(π/2)[G]_+/(ωΨ)du. In particular, G≤0 for every prefix is necessary and sufficient for 𝔗_f=0; unlike the prior single-crossing hypothesis, D itself may change sign repeatedly.

**SF-2:** For any D=D0+R write G0(u)=∫_0^u ωΨD0, GR(u)=∫_0^u ωΨR. If every G0(u)≤0, then 𝔗_f≤(4/A_f)∫_0^(π/2)[GR(u)]_+/(ωΨ)du. Favorable baseline contributions of arbitrary size cancel by sign, while only positive cumulative residual flux is charged. This bound is conditional; its denominator can become small on depleted fibers.

**SF-3:** If GR(u)≤−G0(u) for every prefix then 𝔗_f=0. This is a signed-prefix Wilson sufficient condition, *not proved* for the actual completed-cage vacuum.

Numerical audit: six smooth positive center-symmetric scalar profiles Ψ=exp(λcos2u), λ=±2,±1,±0.3. Maximum reconstructed flux-score error on the nonsingular interior grid 1.74e−7; all residual current bounds held. These are scalar identity checks, not interacting Wilson-vacuum simulations.

Full proof, executable verifier, results and SHA-256 manifest in Library Proof Audits file `R3_IR_SIGNED_FIBER_FLUX_RESIDUAL_2026-10-31.zip`. Signed-current, connected covariance and continuum mass gap OPEN.