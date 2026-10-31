# Stage 26 geometry provenance gate

**Status:** finite checkpoint provenance check, **not** all-refinement geometric certification.

The eight user-supplied Stage 26 run archives (Penrose/square seeds 101,211,307,419) each contain 100 NPZ checkpoints, sweeps 10020–12000. In each run the `latest.json` final `record_sha256` matches the actual final NPZ file; all 100 records' `catalogue_sha256` and `source_sha256` fields agree with that run's manifest. The checkpoint NPZ arrays do **not** contain complete original-link face-edge incidence, oriented face boundaries, or spanning-tree definitions. Consequently this data alone does not reconstruct a completed-cage Penrose dual path. Matching hashes in checkpoint metadata do not establish that the actual catalogue/source bytes have been recovered. The previously certified native 3-face seed is distinct from the Stage 26 production catalogue.

**Next gate:** recover the deterministic generator source and catalogue bytes matching the recorded source/catalogue hashes, construct signed face boundaries and dual adjacency across several nested original Penrose patches, prove distinct-edge dual walks to exterior and evaluate the actual link Jacobian. The uniform deleted-vacuum score-current estimate and continuum gap remain OPEN.

Supporting full audit report, executable, checkpoint JSON result and SHA-256 manifest preserved in Library `/The Singular Boundary/Proof Audits/STAGE26_GEOMETRY_GATE_2026-10-31.zip`. All historical data were read-only.
