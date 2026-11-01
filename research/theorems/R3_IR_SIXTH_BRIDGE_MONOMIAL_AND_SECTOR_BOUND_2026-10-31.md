# R3-IR — Straight five-face sixth-order SU(2) bridge coefficient reduction and exact spectral majorant

**October 31, 2026.** Original-link planar SU(2), uniform unit electric coefficients, face chain 0–1–2–3–4, two outer-domino traces r_01 and r_34 at face-graph distance two. Independent magnetic couplings t0,...,t4. Center parity, exact tensor factorization, and degree counting force the **only** potentially nonzero sixth-degree connected-covariance monomial to be **t0*t1*t2^2*t3*t4**. Vanishes identically if the bridge coupling t2=0.

With Haar-mean-one vacuum psi=Σt^αu_α, the only nonzero energy counterterm in the rectangular multidegree range is e_(2e2)=−1/12; the amplitude recurrence is u_α=R[Σ_i p_i u_(α−e_i)−(1/12)1_(α2=2)u_(α−2e2)], with mean-zero projection inherent in R. There are **360** distinct multiset insertion orders. The exact isolated bridge coefficient u_(2e2)=(p2²−1/4)/24 has Haar L² norm 1/96.

In center parity sector F(α)={i:α_i odd}, the original-link electric gap is at least 3|∂F|/4; for empty parity, the nonconstant sector gap is at least 2. An exact-rational induction using these gaps gives the rigorously verified **vacuum-amplitude norm bound**
**||u_(1,1,2,1,1)||₂≤28271/2952450≈0.009575437348642652**,
independent of the total inactive cage.

For the signed **connected** coefficient, let w_α=Σ_(β≤α)u_βu_(α−β), h_D=[t0t1t2²]E(r_01), h_E=[t2²t3t4]E(r_34). The remaining exact identity is
**[t0t1t2²t3t4]Cov(r_01,r_34)=〈r_01r_34 w_(1,1,2,1,1)〉−49/1679616−(7/216)(h_D+h_E)**.
The denominator correction 49/1679616 and both fourth-order mean responses must be retained. The signed coefficient **has not been evaluated**.

Full mathematical derivation, executable exact-rational dynamic-programming verifier, results JSON and SHA-256 checksum manifest: Library /The Singular Boundary/Proof Audits/R3_IR_SIXTH_BRIDGE_MONOMIAL_AND_SECTOR_BOUND_2026-10-31.zip. Sixth-order signed connected covariance, regulator-uniform physical coupling, signed current and the continuum mass gap remain OPEN.