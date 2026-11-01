# Exact SU(2) bent-bridge coefficient and interior overlapping-domino fourth Taylor coefficients

**Date: October 31, 2026.** Finite original-link planar SU(2), unit electric weights and independently coupled retained magnetic plaquettes.

For two overlapping domino loops AB and BC in a 2×2 block with A=(0,0), B=(1,0), X=(0,1), C=(1,1), the exact rational original-link calculation gives

**[t_A t_X² t_C] Cov(r_AB,r_BC)=1360751/5046312960 >0.**

At t_B=0, integrate the independent B Haar holonomy to obtain **∫p(AB)p(BC)dB=p(A C⁻¹)/4** (the inverse is essential). The normalized squared-vacuum raw coefficient is **2334191/5046312960**, minus density normalization **1/5184**. The independent exact second-order check is **[t_A t_C]Cov=1/144**. The vacuum recursion includes the correct e_(X²)=−1/12 counterterm; the exact active quaternion-invariant repeated-X sector is eight-dimensional.

Combining previously proved repeated-nonshared, repeated-shared, one-sided, and B-only spectator cancellations gives complete **interior, unit-weight, distinct overlapping-domino off-diagonal fourth Taylor coefficients**, if all faces of the local support are retained:

- Straight three-face overlap: **−73090501/100926259200**.
- Bent three-face overlap: **−3991219/8410521600**.

For these fully retained interior cases, the overlap block has at most two straight and four bent neighbors per row, giving a volume-independent absolute row-sum bound **2·73090501/100926259200+4·3991219/8410521600**. Near the deleted face or boundary, omit missing spectator contributions.

**Critical limitation:** The earlier isolated-domino diagonal fourth coefficient need not equal the full-cage diagonal because additional local magnetic spectators may contribute. Therefore this result does **not** complete the entire fourth-order covariance matrix. No physical-coupling convergence, regulator-uniform signed-current estimate or continuum Yang–Mills mass gap is asserted.

Full proof, exact executable rational original-link solver, independent lower-order checks, JSON and checksum manifest: Library /The Singular Boundary/Proof Audits/R3_IR_BENT_BRIDGE_AND_OVERLAP_FOURTH_EXACT_2026-10-31.zip.