# R3-IR-539 — Independent Whitney element integration test and non-scalar historical mismatch

This audit uses the recovered M5 geometry and explicitly declared affine quadrilateral Whitney/Nedelec reference 1-forms, with reference-edge functions [(1-v,0),(0,u),(-v,0),(0,u-1)]. Let J be the physical affine Jacobian and G=J^-1 J^-T. For reference basis i,j, the exact element is abs(det J) G_(axis_i,axis_j) times the polynomial moment of their scalar factors. Same-variable linear products integrate to ac+(ad+bc)/2+bd/3, independent-variable factors to (a+b/2)(c+d/2). This exactly integrates the degree-two element product.

The independent verification script compares this analytic polynomial result against 4-point tensor Gauss quadrature on 300 seeded random 2x2 matrices (excluding nearly singular Jacobians), with agreement within 1e-9 and positive semidefinite local mass. This confirms the QUADRATURE arithmetic of the candidate, not the missing historical assembled mass operator.

Candidate versus historical previously reported summary:
minimum eig 0.196155044395 / 0.143174148694 = 1.37004512466;
maximum eig 2.277516706271 / 1.104659344162 = 2.06173669585;
edge13 diagonal 0.694741426782 / 0.777859028095 = 0.89314567510.

Hence the difference cannot be explained by a single scalar normalization of the entire matrix. Which geometry convention, cochain basis, boundary rule or metric yielded the historical matrix is still UNKNOWN; there is not enough information to identify the cause uniquely.

The repository Whitney builder now reads modules from PYTHONPATH or PENROSE_SOURCE_DIR, not a session-dependent absolute path, with WHITNEY_OUTPUT configurable. The archived geometry modules must still be supplied from their verified provenance; this change by itself does not embed those files in GitHub. The original NPZ was not found in this session; no substitute is claimed identical to it. The next obligation is a source-to-element historical provenance reconstruction or retrieval of the exact historical NPZ, followed by tree-dependent multiloop testing with a known matrix.

No continuum Yang-Mills mass gap, refinement-uniform center cap, or historical matrix equivalence is established.
