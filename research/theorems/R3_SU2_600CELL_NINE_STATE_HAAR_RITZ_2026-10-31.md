# R3-IR-570 — Degree-eight 600-cell SU(2) tensor Haar contraction: all six nine-state Ritz matrices (2026-10-31)

## Result

The quaternion unit-sphere 600-cell has **120 vertices**: 8 coordinate axes, 16 sign corners (±1/2)^4, and 96 even permutations of (0, ±1/2, ±φ/2, ±1/(2φ)), φ=(1+√5)/2, taking independent signs on the three nonzero entries. The equal-weight design was validated against **all 495 monomials of total degree ≤8**, using exact rational S³ Haar moments as targets; largest numerical discrepancy 5.55e−17. This is consistent with the classical spherical-design property of the 600-cell. The executable tests numerical moment identities, not a computer-assisted exact-algebra proof of the 600-cell design theorem.

The resulting three-independent-chord tensor consists of 120³=1,728,000 nodes, rather than the 300³=27,000,000 nodes of R3-IR-569. A batchwise contraction evaluates all 9×9 electric Ritz entries using full inverse-Whitney K and rooted gauge fixing, with local two-loop gradient metric tensors. This retains the two distinct adjacent Wilson loops, the correct Haar-orthonormal character basis χ_{a/2}(U_A)χ_{b/2}(U_B) for a,b=0,1,2, and the exact magnetic character recursion. All six runs completed.

| M | nine-state gap | max electric off-diagonal residual |
|---:|---:|---:|
|5|58.744154660340655|3.08e−14|
|7|83.61514681458567|1.90e−13|
|9|111.12533645239117|2.75e−13|
|11|132.1789229145107|1.32e−13|
|13|158.31188907264578|5.18e−14|
|15|183.97339665383237|5.42e−13|

All Haar Gram matrices agree with I_9 to within ~3e−15. The eigenvalue gaps reproduce the previously approximate rotated-24-cell values of R3-IR-568. This removes that rule's degree-eight exactness objection for the nine-state polynomial integrands, **provided** the documented per-chord polynomial-degree bound is applied correctly. Numerical entries are floating-point approximations of exact-form Haar contractions, not certified floating-point intervals. The full electric 9×9 matrices and all nine Ritz eigenvalues are preserved in the JSON output.

## Reproducibility and caveats

Source files `compute_nine_state_600cell.py` and `test_600cell.py`, equal-weight 600-cell points `su2_600cell_design_120.npy`, and `nine_state_600cell_exact_haar_ritz_2026-10-31.json` are persisted in ChatGPT Library `/The Singular Boundary/Source/`. All source original 3D mass and incidence NPZ files remain in Library, not Git.

**Critical bounds:** This is a finite-dimensional Ritz projection on two selected gauge-invariant plaquette characters in each 95–98 link *candidate* prism, not the low-energy spectrum of the complete Gauss-law-constrained graph. Ritz gaps can vary nonmonotonically with basis enlargement and do not provide a uniform full-spectrum lower bound. The six arbitrary h=1/M patches are not a physically calibrated continuum refinement. No continuum Yang–Mills mass gap is proved.

**Next obligation:** expand the gauge-invariant trial space beyond these two plaquettes and retain extra intertwiner channels; quantify truncation and truncation error for physical low energies. Note that all 9-state electric offdiagonals vanish for this tested basis in the evaluated exact-form integral, which may admit an independent representation-theoretic selection proof.
