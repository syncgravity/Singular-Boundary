# R3-IR — Four distinct edge-adjacent domino geometries: correction of completeness claim

**2026-10-31.** The previously claimed two geometries of face-disjoint, original-link-adjacent domino Wilson-loop pairs are NOT exhaustive. Exhaustive square-lattice enumeration modulo dihedral transformations and loop interchange proves **four** cases:

1. Straight four-face chain: D={(0,0),(0,1)}, E={(0,2),(0,3)}; one common link. **Known** exact unit-weight fourth connected covariance coefficient 30757/1843845120.
2. Bent-end (L-shaped four-face union): D={(0,0),(0,1)}, E={(0,2),(1,2)}; one common link. **UNKNOWN** exact coefficient.
3. Staggered parallel (zigzag): D={(0,0),(0,1)}, E={(1,1),(1,2)}; one common link. **UNKNOWN** exact coefficient.
4. Aligned parallel 2×2 block: D={(0,0),(0,1)}, E={(1,0),(1,1)}; two common links. **Known** exact unit-weight fourth covariance coefficient 19667/420526080.

For N=21, counts are 756 straight, 3040 bent, 1520 staggered, 800 aligned, total 6116; **4560 (74.56%) of the edge-adjacent pairs belong to geometries with unknown exact fourth coefficient**. The per-row degrees by these geometries are bounded by 2,8,4,2; total ≤16. Earlier generic *volume-independent fourth-order norm estimates* remain valid, but treating the two known exact coefficients as the entire edge-adjacent fourth-order matrix is wrong. Corrective exact enumerator, complete table, SHA256 manifest: Library /The Singular Boundary/Proof Audits/R3_IR_FOURTH_ORDER_FOUR_GEOMETRY_CORRECTION_2026-10-31.zip.

Next: compute exact original-link SU(2) four-face fourth connected covariance for the bent-end and staggered cases, correctly assembling primal-tree electric recouplings and verifying boundary trace electric eigenvalues. Physical-coupling clustering, signed-current bound and continuum mass gap remain OPEN.