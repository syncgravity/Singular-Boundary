# Wilson covariance first-order cancellation, finite SU2 square disks

For K=−Σ_e a_e Δ_e, Hλ=K+λΣ_(k≠f)b_k(1−p_k), normalized positive ground state Ωλ, νλ=Ωλ²μ, and F=∂λ log Ωλ|0=Σ_(k≠f)(b_k/ε_k)p_k, the first Wilson coupling derivative of every covariance of two distinct simple two-plaquette outer-loop traces is **zero**:
Cov_νλ(r_i,r_j)=δ_ij/4+O(λ²).
The exact parity proof uses the central element −I on each SU2 original link and the injective F2 boundary map for planar disk plaquette subsets: symmetric difference of two 2-face dominoes has even cardinality, so cannot be one retained plaquette.

For any Haar-preserving target-holonomy transport T fixing F, Q=∂²λ log Ωλ|0, D=Q∘T−Q, there is also an exact perturbative signed expectation identity:
**E_νλ D=−(λ²/2)||D||²_L²(μ)+O(λ³)**.
This follows from Ωλ²=1+2λF+λ²(Q+2F²)+O(λ³), Eμ[D]=Eμ[DF]=Eμ[D F²]=0, and Eμ[D Q]=−||D||²/2 by Haar invariance. This D is *not* the nonnegative excitation-form transport defect Q_g.

Full proof and 77,936 parity-pair tests for 3,5,7,9,11 square disks, plus 1,000 randomized finite-dimensional signed-response tests, are in Library archive R3_IR_WILSON_COVARIANCE_FIRST_ORDER_CANCELLATION_2026-10-31.zip. No λ=1, regulator-uniform current, connected covariance, or mass-gap claim.