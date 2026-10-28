# Historical verification programs — original source audit (2026-10-28)

**Scope:** Twenty user-supplied Python files `verify.py`, `verify (1).py`, …, `verify (19).py`, read as bytes and parsed as Python syntax. This was a **static, read-only audit**: no historical verification program was executed and no original archive was modified.

## Results

- **20/20** source files parse as Python; every original source SHA-256 and exact byte length is in `SCRIPT_MANIFEST.csv`.
- **18/20** contain explicit write-capable calls (`np.savez*`, `json.dump`, `write_text`, or `open`); running them in their original context could overwrite artifacts or produce fresh certificates. The only 2 without such calls are `verify (2).py` and `verify (4).py`.
- `verify (2).py`, `(3).py`, and `(5).py` load historic NumPy files with `allow_pickle=True`; do not execute on untrusted content. `verify (13).py` contains `assert ... or True`, which cannot test the asserted rank condition.
- Their hard-coded `/mnt/data/R3_*_2026_10_27/` input/output directories (`R3_two_prism_certified`, `R3_looped_four_prism`, `R3_three_four_step_transfer`, `R3_local_conditional`, etc.) are **not present in the active mounted directory**. The exact original runtime environment and generated certificates have not been recovered from these loose files.
- They are **not** the Stage 19–35 reproducibility verifier constructed in this conversation. That separate read-only suite passed 100 checks across 42 pinned historical ZIPs; its PASS result does **not** certify these 20 script executions.

## Historical mathematical sequence encoded in the scripts

| Scripts | Historical focus | Evidence limitation |
|---|---|---|
| `verify.py`–`verify (5).py` | One- and two-quadrilateral prism incidence; two-prism rank, convolution and positive seam-interface calculations | Explicitly *constructed combinatorial models*, not source-derived original Penrose tiling |
| `verify (6).py`–`verify (12).py` | Three-/four-prism multiport geometry, center-parity selection, four-port singlet intertwiners, gauge-fixed interface words, two-step temporal comparison | Mostly small finite toy subcomplexes; not full Penrose nor generic interacting R3-IR spectral contraction |
| `verify (13).py`–`verify (17).py` | Two-/three-/four-step transfer incidence and positive character blocks; nonstationary trace/Loewner counterexamples | Abstract PSD counterexamples and truncated character blocks do not prove or disprove all-scale SU(2) Penrose contraction |
| `verify (18).py`–`verify (19).py` | Canonical four-quadrilateral × three-periodic-slab incidence; conditional relative-rank and regularized Gaussian determinant | Clearly says **not Penrose-extracted**; Gaussian exterior reference is an added assumption; not compact SU(2) nonlinear comparison |

## Specific safeguards and limitations

1. Preserve these original 20 scripts unchanged (including bugs and old hard-coded paths) as **primary historical evidence**. New safer wrappers should live separately.
2. To replay historically, first source-locate original `incidence.npz` and contemporaneous `certificate.json` by original SHA-256; do not regenerate or replace them as a substitute for recovery. Any eventual execution must be sandboxed in a separate copy with network disabled, pinned dependencies, and write-path redirection.
3. Do not treat script `assert` statements alone as independently reviewed mathematical proofs. NumPy floating ranks and Gaussian determinant calculations require their own assumptions/condition checks.
4. The 4-quadrilateral/3-slab input in `verify (18).py` is expressly a **constructed rectangular 2×2 patch**, not the authentic Penrose Q14 or the older provenance-uncertain 12-prism/37-free-link configuration. Do not merge them by matching counts.
5. No mass-gap theorem is established here. The R3-IR interacting low-energy source-decay, physical unit normalization, observability, and R2 continuum obligations remain open.

## Verification acceptance levels

- **Verified**: exact source bytes, script count, parseability, named dependencies, write-capable code paths, and the failure of one written assertion to test anything.
- **Not verified**: historical execution outcomes or equality with the contemporaneous archived originals; those require locating the historical source members and/or original generated certificates.
- **Not attempted**: running the scripts, regenerating incidence matrices, recomputing Gaussian estimates or gauge field simulations.