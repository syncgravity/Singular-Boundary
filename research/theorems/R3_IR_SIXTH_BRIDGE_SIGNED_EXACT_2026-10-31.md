# Exact signed sixth-order straight five-face SU(2) domino covariance

**Date:** 2026-10-31. **Hamiltonian:** finite original-link planar SU(2) Wilson system, five consecutive plaquettes A–B–X–C–D, unit electric link coefficients and independent magnetic couplings. r_AB and r_CD are the normalized outer Wilson domino traces.

**Theorem (Taylor coefficient):**
[t_A t_B t_X² t_C t_D]Cov(r_AB,r_CD) = **34818566119/628757676254822400 > 0** (≈5.53767650621712×10⁻⁸).

**Exact intermediate calculations:** The sixth-order raw Haar contraction is **20523667746919/628757676254822400**. The fourth-order bridge-induced domino mean raw numerator is **9247/9704448**, with normalized mean **h_D=h_E=511/9704448**. The complete sixth-order normalization and disconnected mean subtraction is **34153/1048080384**. Independent order-two mean check is **7/216**.

**Important archival corrections:** (1) The previously reported h_D=12367/9704448 and sixth-order subtraction 117145/1048080384 are wrong. The vacuum-energy counterterm e_X²=−1/12 must insert the constant quaternion identity **Σ_{μ=0}³x_{X,μ}²=1**, not just x_{X,0}². A separate corrected three-face original-link solver now reproduces the corrected fraction h_D=511/9704448. (2) The archived 41 lower-order electric matrices and newer magnetic maps used different invariant-tensor coordinate bases. Their exact rational change-of-basis was performed before composing the full recursion.

**Reproduction:** All 47 projected electric sector matrices, 128 exact magnetic insertion maps, delta/epsilon invariant generator, exact mean-one vacuum recursion, Haar contraction (448 nonzero canonical density monomials), independent corrected three-face solver, theorem and checksums are archived at `/The Singular Boundary/Proof Audits/R3_IR_SIXTH_BRIDGE_SIGNED_EXACT_2026-10-31.zip`. Run `python solve.py && python contract.py` in the unpacked directory.

**Caution:** The previous shared-face repeated-insertion audits and derivative fourth-order full matrix may require re-verification because they potentially share the counterterm mistake. This result establishes only a specific sixth-order **finite-lattice Taylor coefficient**; it proves neither physical-coupling covariance clustering, a regulator-uniform signed-current estimate, nor the continuum Yang–Mills mass gap.