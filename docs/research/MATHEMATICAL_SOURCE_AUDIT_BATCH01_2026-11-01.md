# Mathematical source certification — batch 01 (2026-11-01)

**Scope:** Historical IDs R3-IR-373 through R3-IR-380 (eight flagged IDs, nineteen historical ledger occurrences). This is not a completed certification of all 246 flags.

## Primary source retrieval

13 of 14 distinct (Git ref, cited theorem path) pairs were retrieved through GitHub. The exception is the main-ledger source `SCALAR_WILSON_IR_AND_COMPLETENESS.md` cited for one `R3-IR-379` occurrence: the exact path could not be retrieved from the cited ref. This is **missing citation evidence**, not a mathematical refutation.

These are **19 occurrences representing 8 legacy IDs** and multiple unrelated propositions. A legacy ID cannot be used as an unambiguous mathematical citation.

## Theorem-content audits (four full source files read)

### Audit branch R3-IR-379 / R3-IR-380: historical factor-four correction

- `research/theorems/R3_GROUND_STATE_SCORE_NORMALIZATION_AUDIT_2026-10-30.md`, blob `6b38545fe6443b36e7287f38e2268ca6dcbdb8a0`, explicitly derives the current without factor four **under unit-round-S³ Laplacian** and calls the original October 29 factor a discrepancy.
- `research/theorems/R3_SU2_GENERATOR_CONVENTION_CORRECTION_2026-10-30.md`, blob `d688589d7908c483a94b77539fce50c7e7d26fcf`, explicitly supersedes that allegation for the **physical generator with -Δχ_j=j(j+1)χ_j**, where `Γ(p,p)=A_f(1-p²)/4`.
- Under the physical convention and `p=cos u`, the corrected source equation is `d_u log ψ=-4C(cos u)/(A_f sin u)`. A separate elementary chain-rule check reproduces this coefficient from `Γ(p,p)=A_f(1-p²)/4` and `Γ(p,logΩ)=κ∂_p logψ`.
- **Disposition:** documented correction/supersession, algebraically consistent at the normalization level. Not independent certification of every downstream deletion constant.

### Main R3-IR-373: incomplete-cage conditional Haar theorem

- `research/theorems/CONDITIONAL_HAAR_INCOMPLETE_CAGE_CI1_CI2_2026-10-30.md`, blob `b973513e8b9435f0e11f5cf101b8f1cdfd9c0907`.
- The source invokes the explicit **IC hypothesis**: every retained link-connected magnetic component intersects a proper subset of the target boundary. The conditional Haar result is confined to this setting. The theorem text explicitly excludes a completed magnetic cage.
- The document describes verification scripts but explicitly states their companion bytes had **not** been verified in Git at the time of writing.
- **Disposition:** theorem statement and hypothesis located and checked; mathematical proof and original verification scripts not independently reproduced. Do not upgrade beyond finite incomplete-cage conditional claim.

### Main R3-IR-378 (second occurrence): exact physical score/Fisher contraction

- `research/theorems/R3_IR_TARGET_SCORE_FISHER_CONTRACTION_2026-10-30.md`, blob `60711c16c8c4b5bfb54d8411d5eda438d34f1743`.
- The source's `κ=A_f(1-p²)/4`, `κ∂_p logψ=J`, and `d_u logψ=-4J/(A_f sin u)` are mutually consistent; the stated Fisher contraction follows from conditional Cauchy–Schwarz and does **not** imply a uniform unweighted signed-current estimate.
- **Disposition:** key scalar algebra checked against the text; complete original-link, domain and physical-model audit and executable verification remain uncompleted.

## Collision decision

IDs 373–380 encode different propositions across original branches. Treat every original occurrence as a separate historical item, preserve source-qualified aliases, and do not select a winner based solely on a label or timestamp. Earlier factor-four claims are convention-specific and one historical allegation is expressly superseded.

## Verification boundary

- All 19 occurrences have an attributed ledger row and cited path; **13 of 14 unique source paths were retrieved**, but only four complete documents received initial mathematical-content inspection.
- The other retrieved files were inspected through opening text, not fully audited.
- No theorem scripts, external binary evidence, full dependency graph, or complete derivation formalization was executed.
- **Eight flagged IDs processed at source-location level; zero of eight globally certified as independently reproducible mathematical packages.**

## Required next step

Resolve the missing scalar-Wilson citation; complete the exact statement/proof checks for all remaining paths within these IDs and then proceed by dated batches through the other 238 flags. The overall historical acceptance gate remains **BLOCKED**.
