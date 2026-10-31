# R3-IR-540 — Available research data recovery inventory (2026-10-30)

User requested data recovery without chat archive dumps. Inspection of the current mounted /mnt/data runtime yields:

**RECOVERED/ACCESSIBLE NOW**:
- Exact original Penrose geometry source bytes recovered at penrose_restore/src/penrose_causal_study.py, 11,168 bytes, SHA256 0e986d81911b30af42920564813311141de5878b03aed55b2677ff6dff45adce.
- wilson_torus.py, 6,075 bytes, SHA256 762d128e9c76441484d45ccde89e405e5f04dc85d5f27d2cfcc4bcb0770a100a.
- Eight named sweep10000_multihit NPZ measurements present, four Penrose and four square seeds 101,211,307,419, with direct/multihit/lag metadata present.
- Eight Stage26 seed ZIP archives available, plus an extra penrose_seed101_stage26_full.zip.
- User-provided archive Archive 4.zip is mounted and inspectable.
- Explicitly *different* candidate M5 Whitney matrix m5_whitney_candidate_2026-10-30.npz, and its assembly source, remain available. The R3-IR-539 addendum found candidate versus historical reported diagnostics disagree by NONUNIFORM scale: eigen-min factor .729902965970, eigen-max factor .485027987334, edge-13 factor 1.119638182080; therefore rescaling cannot retrieve historical values.

**NOT RECOVERED**: historical exact binary global_whitney_11face.npz (30x30 edge mass). Searches covered mounted files, recursive .npz filenames, and names inside available ZIP archives. No historical matrix or original definite assembly rule could be verified. Existing numerical fingerprints must not be inverted into an invented matrix.

**Persistence limitation**: current physical source files are available in this runtime, but this GitHub note stores only metadata. The original bytes have NOT been uploaded to the repository, and should be treated as EPHEMERAL until committed separately. A committed report does not make its source binary durable.

**Next scientifically sound action**: proceed with recovered original Penrose geometry and archive measurements for analyses that do not need missing Whitney mass entries. For the actual-matrix Penrose two-tree comparison, BLOCK the claim on original matrix recovery; do not silently use the candidate. No archive attachments sent to chat. No continuum Yang-Mills mass gap established.
