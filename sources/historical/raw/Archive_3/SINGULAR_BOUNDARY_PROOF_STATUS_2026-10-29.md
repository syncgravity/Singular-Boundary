# The Singular Boundary — Proof Status and Repository Reconciliation

**Review date:** 2026-10-29. **Branch:** `audit/2026-10-28-independent-reconstruction` in `syncgravity/singular-boundary`.

## Executive finding

The sequence has established many **finite-regulator, physical Gauss-invariant SU(2) Hamiltonian identities and inequalities** and a number of **conditional Penrose-refinement implications**. It has **not proved a regulator-uniform positive physical mass gap**, nonzero finite-time Wilson-source survival, the fixed-support nonlinear connected remainder estimate, or full continuum reconstruction. In particular, the most recent result, `R3_IR_DOUBLE_SELF_WEIGHTED_CAP_RESPONSE_2026-10-29.md`, is a conditional cap-probability alternative, not the missing low-energy response estimate.

## Verified repository inventory (live GitHub directory and ledger read)

- `research/theorems/`: **75** Markdown entries.
- `scripts/audit/`: **67** entries after adding the latest cap-response regression, including both earlier symbolic companions and fuller downloadable-package verifiers.
- `research/claims/CLAIM_LEDGER.csv`: **334** rows, 7 columns, highest indexed R3-IR claim **R3-IR-324**; no duplicate claim IDs. The consecutive R3-IR-264 through R3-IR-324 entries are present.
- All repository theorem paths referenced by ledger entries resolve by exact filename to the live theorem directory. Entries whose primary source is a `local package ...zip` are **not independently archived in the GitHub repository**.
- The latest full local verifier `sb_cap_double_selfweighted_20261029/verify_double_selfweighted_cap.py` completed successfully in this review; its package ZIP passed integrity inspection and internal `SHA256SUMS.txt` verification. The repository regression `scripts/audit/verify_double_selfweighted_cap_response.py` is a **smaller companion check**, not an exact byte copy of the complete packaged verifier.
- Recent GitHub writes are on the audit branch, not the default branch. No merge, release, or CI green status is claimed.

## Substantive proof map

| Area | Evidence class | Status / logical limitation |
| --- | --- | --- |
| SU(2) Gauss invariant Hamiltonian identities, source carré-du-champ and first/third spectral moment commutators | Analytic finite regulator | Claimed proved in theorem reports; numerical checks sample limited finite examples |
| Regional curvature energy comparison, exponential tilts, local tails | Analytic finite regulator under explicit geometry/coefficient assumptions | Proved under stated hypotheses; not a connected covariance bound |
| Boundary and dual-bridge interior magnetic-face deletion | Analytic finite regulator | Private-edge/bridge cases have square-root deletion bounds; **general cycle-rich interior case open** |
| One-neighbor interpolating response and double self-weighted cap-source inequality | Analytic finite regulator | Exact response decomposition and high-energy cutoff at `L h^(-11/8)` proved; low-energy adverse response **not bounded** |
| Full nonlinear Penrose flat-holonomy probability at magnetic-deleted interior face | Conditional refinement | Polynomial `h^(3/2)` lower bound requires an independent sign, current, Fisher, or low-energy response estimate |
| Fixed-support nonlinear Wilson-versus-angle centered covariance | Open | Sparse-defect and mesoscopic results do not supply the fixed-support connected cumulant |
| Finite physical-time source survival and uniform physical mass gap | Open | Neither finite-volume moment bounds nor the Gaussian tangent imply these continuum statements |
| Quartic resolvent and Osterwalder-Schrader continuum construction | Open | Must not be represented as proved |

## Exact immediate missing inequality

For a smooth positive SU(2) convolution bump at `a_h=arccos(1-h)`, define `F_a(u)=<k_a(W_f)>_{Omega_u}` along the interpolation restoring only a neighboring magnetic face. The source-normalized adverse low-excitation response is

`B_{a,<=Lambda} = integral_0^1 [2 Re <Q k_a Omega_u, G_u P_(0,Lambda] Q(b_g d_g) Omega_u>]_+ / (2 sqrt(F_a(u))) du`.

The latest theorem proves that for `Lambda_h=L h^(-11/8)` and sufficiently large fixed `L` the UV correction is <=`alpha_a/4`, with `alpha_a=int phi_a ~ h^(3/2)`. To complete the cap lower bound it remains necessary to prove a genuinely **model-specific** inequality such as

`sup_{f in D_R} B_{a_h,<=L h^(-11/8)} <= alpha_(a_h)/4`.

This missing estimate may require cancellation/sign control of the physical reduced resolvent; it cannot be inferred from positivity, character parity, a mass gap assumption, local energy budgets, or a Gaussian reference without new proof.

## Reproducibility / documentation risks to address next

1. Local-only proof bundles and verifiers referenced by the claim ledger are not fully available to a clean GitHub checkout. Upload the **complete** scripts/reports or link immutable, accessible archive artifacts if source-size limits permit.
2. The independent-review branch has many small reports but needs a top-level dependency map with precise hypotheses and proof status, plus a CI workflow to run the complete audit scripts.
3. Audit claims that use `proved` should be subjected to standalone peer-style checking of normalizations, boundary assumptions, low-energy projections, resolvent domains, and uniformity of constants before any publication or merge.
4. The supplied Stage26 Penrose/square archives and dissertation tarball remain intact and were **not** reprocessed in this repository-focused reconciliation; this review does not certify their data provenance or Stage26 numerical conclusions.

## Recommended next theorem

Resolve the one-neighbor, low-energy **normalized adverse cap-response** inequality in the *actual* cycle-rich magnetic-deleted SU(2) vacuum. If unavailable, seek an exactly quantified counterexample inside a **finite physical Wilson patch** or a weaker positive source inequality, and update the ledger explicitly; do not silently upgrade a conditional cap certificate into a gap proof.
