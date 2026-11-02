# Independent source and uploaded-input audit — 2026-11-01

**Historical certification: BLOCKED.** This report records actual inspection and execution and does not certify all 246 flagged claims.

## Missing R3-IR-379 citation

The main ledger refers to `SCALAR_WILSON_IR_AND_COMPLETENESS.md` by bare filename. Fetching that exact path on main failed; GitHub code search for the filename and high-spin scalar Wilson phrase returned no hits. **The missing citation was traced and remains unresolved:** no original theorem blob was found. The ledger is not to be re-pointed to an unrelated theorem or labeled source-certified. The statement remains UNVERIFIED.

## Remaining audit-branch documents for flags 373–380

Complete originals inspected:
- `R3_FOLDED_RADIAL_ENERGY_TV_2026-10-30.md` (audit branch Git blob `f831f2b682777979801e5f130cad22978c272c74`): folded Haar TV inequality and countermodel, explicit delta^6 sufficient-energy limitation. The text uses a Neumann spectral gap 8 and a Cauchy–Schwarz argument; no interacting Penrose regulator-uniform estimate follows.
- `R3_LOCAL_STAPLE_DERIVATIVE_BOUND_2026-10-30.md` (blob `83e97ab51bafa67c65c34569bf15bd5fa5d6ac3a`): pointwise local magnetic derivative bound under **unit round S³ normalization**, not an effective fiber-force estimate. Must not use its coefficients without translating to the physical j(j+1) generator convention.
- `R3_EXACT_INTERACTING_RADIAL_REDUCTION_2026-10-30.md` (blob `f150fb3108b76dd8d755d9f6292bd72103ea3d63`): full-angle radial disintegration under regularity assumptions; folded density must combine two branches; interacting one-sided current remains open.

Together with [batch 01](MATHEMATICAL_SOURCE_AUDIT_BATCH01_2026-11-01.md), these locate the first-group theorem hypotheses and their limits. **They are not a complete independent proof verification for all nineteen instances.**

## Independent execution on user-uploaded bytes in this runtime

Executed Python 3 with NumPy, `zipfile.ZipFile.testzip()`, hashlib SHA-256, safe `np.load(..., allow_pickle=False)`, and independent `np.linalg.eigvalsh` on the supplied files:

- **18 binary inputs inspected:** nine Stage26 ZIP files (four Penrose seeds, four square seeds, plus Penrose seed101 full), eight multihit sweep NPZ files, and the historical `global_whitney_11face.npz`.
- All 9 ZIP CRC tests passed; none showed duplicate ZIP member names.
- For each Stage26 ZIP, `latest.json` matched the expected seed and kind, the referenced latest record existed, and its byte SHA-256 equaled the manifest's `record_sha256`.
- All 9 NPZ inputs loaded without Python pickle. This includes the 30×30 Whitney matrix and eight sweep datasets.
- The Whitney matrix was exactly symmetric in loaded floating-point entries; its recomputed eigenvalues exactly matched the saved `eigenvalues` array. Its smallest eigenvalue was approximately **0.14317414869400802**, and its largest approximately **1.1046593441618966**. **Edge label 13**, located by `edge_ids == 13` (not array index 13), had diagonal **0.7778590280946629**. This confirms the historically reported edge-label diagnostic on the uploaded file.
- The complete per-file hashes, byte counts, array key/shape inventories and check outcomes were produced as a local JSON report; original-byte remote Git LFS readback has **not** been verified.

## What was NOT executed

- The GitHub `research/scripts/verify_research_handoff.py` source was inspected previously but not rerun in this audit. The independently run ZIP/NPZ integrity checks are **not equivalent** to its intended malicious ZIP-path and manifest-relative traversal test suite.
- No exact theorem verification script or physics simulation was rerun, and no magnetic/transfer-spectrum or continuum theorem is certified.
- Local test files are uploads and do not establish that the same historical originals are durably available from canonical main.

## Next required actions

Resolve scalar Wilson source using full historical Git tree, archives or actual original attachment; do not invent the source. Run the handoff verifier and adversarial fixtures, write companion test logs, and verify exact original ZIP/NPZ SHA-256 after durable remote upload and fresh retrieval. Then continue proposition-by-proposition source review and independent script execution for the remaining flags.
