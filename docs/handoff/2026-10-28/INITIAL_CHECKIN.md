# Initial remote check-in — research continuity

Date: 2026-10-28. Repository: `syncgravity/singular-boundary`.

## Scope

The existing private GitHub bootstrap (README, governance, status, Git attributes/ignore, and LFS status) was preserved. This check-in adds a source-attributed claim ledger, distinct R3-PRISM and R3-IR problem records, D1 and R2 obligations, binary data policy and source-import state.

This commit **does not** represent a completed archival import or an independent proof. It contains no binary Monte Carlo checkpoints, no rerun simulations and no reconstructed twelve-prism geometry.

## Confirmed local preparation

- A separate local Git tree has 602 tracked text/code entries at `621de19bbf7961072d854f52d2193d1673699aea`.
- `scripts/verify_import.py` reported 582 verified local historical source files and no mismatches.
- Git LFS storage is not available/verified in the working container.
- The exact Stage 7 geometry implementation exists in the original Stage 7 archive; the production D1 certificate is still pending.
- The historical R3 twelve-prism insertion/boundary assignment is not located.
- Source-asserted finite-volume mathematical claims are not certified continuum mass-gap results.

## Next exact operation

Import the prepared text/code tree into a **clone of the existing remote `main`**, preserving original source bytes and independent Git ancestry. Verify `ORIGIN.csv` and hashes after upload. Make raw scientific binaries durable via a deliberately chosen, authenticated immutable-storage mechanism before treating the GitHub repository as complete.

Do **not** force-push the unrelated local root commit.
