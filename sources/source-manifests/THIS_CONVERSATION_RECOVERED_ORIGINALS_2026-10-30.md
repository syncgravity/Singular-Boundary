# Original byte-source handoff — Paper 3 / R3-R2 current conversation, 2026-10-30

**Archival status: LOCAL VERIFIED; NOT REMOTELY ARCHIVED.** This record refers to actual readable mounted bytes in the research execution session. It is not a claim that the files were pushed to GitHub, imported through Git LFS, or clean-clone verified. The earlier 20-source intake register remains intact and must not be marked complete as a side effect of this text commit.

## Mount inventory

- **90** files: **45 Git-text/code** and **45 LFS-target original binary** files; aggregate original bytes **95,363,495**.
- All 90 actual streams were individually SHA-256 checked and packaged with unchanged internal bytes.
- Complete per-file provenance, original relative path, byte size, SHA-256, file type, proposed Git destination and Git/LFS classification: `MOUNTED_SOURCE_INVENTORY_SHA256.csv` distributed in the local handoff, SHA-256 `95915c05a301e88a990cca2eaead7407762e4c6e4060a0203603ba6ef4162e98`.
- `SINGULAR_BOUNDARY_LFS_ORIGINALS_2026-10-30.zip`: **94,960,667** bytes, SHA-256 `a22d3d0685836050a5402668b2351becdf73675da65f2c19aee43ae669f8611c`.
- `SINGULAR_BOUNDARY_GIT_TEXT_ORIGINALS_2026-10-30.zip`: **422,838** bytes, SHA-256 `715cd4fd1226dddc05ee5882588551e34324bd073098183870c15bd99ac19a4a`.
- Local package also contains `KNOWN_UNAVAILABLE_SOURCES.csv`, `README_IMPORT.md`, `VERIFY_SOURCE_HASHES.py`, and `PACKAGE_CHECKSUMS.json`.
- Each archive member was read back from the ZIP to recheck original SHA-256 and byte size. Neither package itself nor its contents are yet remotely archived.

## Major file families (use complete CSV, not this summary)

1. Dissertation `Sharpe_dissertation_v10.7.tar.gz`, actual SHA-256 `c405acd6daa5a0a923429ab659b122b22231787d7a30e97db7f2974f278354d1`.
2. Eight original `penrose/square_seed{101,211,307,419}_stage26.zip`, eight sweep10000 NPZ, and 52,884,778-byte `penrose_seed101_stage26_full.zip` (SHA-256 `6cfa12935428533cfeaff40a467705d632b19ede07b7f30e0bb9fb7a0cc68657`). These largely overlap the canonical 20-item intake register; deduplicate by hash.
3. `Stage27_Helical_Observer_Falsifiable_Spectroscopy.zip` through `Stage35_C5_Production_Helical_Ensemble.zip`, including Stage34 12,882,569-byte exact per-anchor archive; Stage33 original data, Stage29 covariance archive, production scripts, deterministic tests.
4. Phase III source `Phase_III_Cut_and_Project_Recomputed.zip`, theorem manuscripts for Level I, D1/J, R3/R2 transfer, scalar loops, Wilson frame, numerical scripts, JSON, PNG, PDF extracted copy.
5. `Branch · Read Conversation Content.txt`, exact **6,253** bytes, SHA-256 `982ee1b4667e4b1099852408d00211881cc03c9ddc06618efc260485f220b601`. Despite its filename, inspection identifies a *rendered signed radial-current theorem report*, not a native full transcript.

The original `completed_cage_cut_comparison_2026-10-30.md` is **not** mounted although a historical intake register lists size 3,217 and a claimed SHA; its original bytes were NOT rehashed in this operation. Other gaps: complete native current/predecessor conversation exports and identifiers, 602-file prepared tree, NOTES.zip, earlier historic ZIP chains not available in this session.

## Import requirements

From a fresh clean clone with `git lfs install`, extract the LFS handoff under its embedded `data/raw/session-2026-10-30/` paths and the text handoff under `sources/originals/session-2026-10-30/`. Compare each original against the included manifest with `python3 VERIFY_SOURCE_HASHES.py <clone-root> <manifest-path>`, stage/add/commit/push without force, then a **second fresh clone** + `git lfs pull` and SHA recheck. Never replace an already archived original with a matching-looking source: compare byte hashes and preservation history. Git LFS pointer files alone are insufficient.

This manifest document contains retrospective context; the byte-hashed original text and binary streams are deliberately separate and still await actual GitHub remote intake.
