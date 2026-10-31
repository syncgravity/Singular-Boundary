# THE SINGULAR BOUNDARY — BRANCH HANDOFF AND CONTINUUM READINESS PROTOCOL
Date: 2026-10-31. Status: research continuity manifest, NOT a proof claim.

## Where to resume
Repository: syncgravity/singular-boundary
Research branch: audit/2026-10-28-independent-reconstruction
Claim-by-claim index: research/claims/CLAIM_LEDGER.csv
Theorem sequence: research/theorems/R3_*.md; recent R3-IR-556 through R3-IR-584
Persistent binary and executed-code archive: ChatGPT Library /The Singular Boundary/Source/
Source files uploaded directly in conversations may also exist as attachments, but do NOT assume they automatically reappear in a branched chat.

## What was actually achieved
The original 11-face Whitney dataset and its historic definition are DISTINCT from the alternative small 3D Penrose-prism candidate regulator. For the latter, edge mass, incidence and action data were constructed, with candidate M in {5,7,9,11,13,15}, and verified elementary incidence/gauge-invariance checks. These are not a physical continuum refinement with proved uniform constants.
- R3-IR-567: degree-sufficient exact-form four-state two-loop Haar integration.
- R3-IR-570: complete degree-eight 600-cell Haar integration of nine-state two-loop Ritz across six candidate prisms.
- R3-IR-572 **CORRECTED**: the old eight-state numerical spectrum assigned EA and EB to the wrong ordered basis indices. Never cite 58.026458 as correct; R3-IR-573 corrects eight-state M5 gap to 60.43640573.
- R3-IR-573: 18-state independent C-loop projected tensor-sum; gap 58.74415466.
- R3-IR-574: fused trace AB intertwiner has nonzero full-metric projected electric coupling 24.65408202.
- R3-IR-576: 10-state fused AB integration degree-certified; M5 gap 58.51602173.
- R3-IR-577: independent C-loop 20-state tensor-sum; gap 58.51602173.
- R3-IR-579: connected third loop D with pair fused channels, 10-state complete projected Hamiltonian; gap 60.43502656.
- R3-IR-580: 11-state all three pair fused channels; gap 60.19916650.
- R3-IR-581: nested 16-state connected higher-spin + pair fused; gap 58.54612014.
- R3-IR-583: certified-degree 17-state orientation-sensitive triple trace with coupling to ABD 1.02700828; gap 58.54611888.
- R3-IR-584: nested 31-state (27 spin-0,1/2,1 triple character products plus 3 pair fused + 1 oriented triple trace). EXACT Haar Gram and projected all-retained-plaquette magnetic matrix constructed; electric matrix **NOT YET COMPUTED**, no 31-state Ritz gap.

All listed spectral gaps are of small Gauss-invariant **trial subspaces**, not proven spectral gaps of the full gauge-invariant finite graph and certainly not continuum theory. Nested trial-state eigenvalue differences need not be monotone. Numerical floating point is not formal interval certification.

## Next computational obligation
Construct the full 31x31 electric quadratic form using full inverse Whitney K and rooted derivatives. The degree-sufficient direct tensor is 120x24x120x24=8,294,400 nodes, with degree 8 needed on chords 1 and 75. Optimize using exact Haar polynomial moments / center-parity block sparse contractions / representation recoupling. Require independent checks: Gram I31; 17x17 certified block; all retained-plaquette magnetic projection; matrix symmetry and positivity. Do not invent gap before calculation.

## Critical continuum gate (do NOT defer indefinitely)
A successively larger finite Ritz space is NOT an approach to the 3+1D Yang-Mills Clay problem by itself. Before claiming any continuum result, require:
1. Define a genuine directed sequence of 3D spatial graphs approximating the SAME fixed physical manifold and a 3+1D transfer matrix/Hamiltonian, with explicit scale h->0, physical anisotropy, gauge group SU2, boundary conditions and Gauss-law Hilbert space.
2. Prove the Whitney/Nedelec mass, incidence, plaquette area/volume coefficients are consistent, local and uniformly stable across genuine refinement; establish positivity/reflection positivity or the correct constructive theory axioms as applicable.
3. Specify bare coupling g(h), units and energy rescaling. Analyze asymptotic freedom/renormalization and verify a regulator-independent limit rather than treating illustrative g²=1 or the arbitrary formal h=1/M patches as physical.
4. Obtain full finite-volume physical ground/excited spectral estimates UNIFORM in h and volume, not gaps between eigenvalues of a fixed-size Ritz matrix. Show the desired lower bound survives h->0, infinite-volume limit, Gauss constraint, and subtraction of vacuum energy; prove existence of the nontrivial quantum theory with required axioms.
5. Independent analytic review and reproducibility: proof ledger, exact/rational/interval checks where needed, regression tests, source provenance and signed hashes. Counterexamples, unsupported estimates and corrected calculations are first-class records.
There is NO proved continuum mass gap in this project at this time.

## Recovery procedure in any new/branched conversation
1. Connect GitHub and access this exact research branch. Read THIS manifest, the claims ledger and the LAST ~5 theorem reports, then follow their cited dependencies backwards to original sources. Do not reconstruct from memory.
2. List Library folder /The Singular Boundary/Source/. Materialize specific .npz/.json/.py objects before running calculations, and check shapes/dtypes/schema and hashes against reported versions.
3. Check known corrections (R3-IR-573 overrides R3-IR-572) and provisional -> certified transitions (R3-IR-575 -> 576, R3-IR-582 -> 583) before relying on numbers.
4. Re-execute representative small-scale invariance/Haar tests and compare to saved matrices; verify all current assets in this runtime.
5. Read the latest open mathematical obligation and the **continuum gate** above; then proceed without silently promoting trial-space statements into exact physical spectrum claims.
If access to the Library or repository is not connected, state the missing dependency and request the exact artifacts; never claim they were retrieved.

## Recommended operational improvements
Maintain at least (a) this single handoff/entry-point file; (b) a machine-readable artifact manifest mapping theorem IDs to Git commit and Library paths + sha256, dependencies, and corrections; (c) one runnable regression command/container environment; (d) a standalone continuum-obligation ledger separate from the finite Ritz computation ledger. Update handoff and artifact manifest after substantive milestones, not relying on the chat transcript.
