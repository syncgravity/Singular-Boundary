# Independent proof status and repository reconciliation — 2026-10-29

This review reconciles the current audit branch with its claim ledger and local verification packages. **The continuum Yang–Mills mass gap is not proved.**

## Live inventory

- 75 theorem reports under `research/theorems`.
- 67 scripts under `scripts/audit` after the double self-weighted cap regression was added.
- 334 rows in `research/claims/CLAIM_LEDGER.csv`; highest R3-IR identifier 324, no duplicate IDs, and no missing referenced repository theorem filenames.
- Some claims deliberately cite local ZIP packages which are not part of a clean repository checkout. These artifacts need durable repository preservation before release.
- The complete latest ZIP verifier passed local rerun, ZIP integrity, and SHA256SUMS checks; the repository companion regression is smaller.

## Mathematical classification

**Finite physical SU(2) statements:** Gauss-invariant Wilson carré-du-champ and spectral sum rules; nonlinear magnetic-deletion comparisons for private-edge or dual-bridge faces; exact one-neighbor cap-response identities; positive source self-weighted Dirichlet bounds; the coupling-integrated neighbor f-sum; and the latest UV bound at cutoff `L h^(-11/8)`.

**Conditional under unresolved dynamical hypotheses:** polynomial flat-holonomy probability for a deleted cycle-rich interior face, complete bulk magnetic-deletion bound, fixed-support Wilson-versus-angle centered source comparison.

**Open:** normalized adverse low-energy response below `L h^(-11/8)`, full-volume connected covariance, nonzero fixed-physical-time source survival, regulator-uniform physical mass gap, nonlinear quartic resolvent, and continuum reconstruction.

## Precise current proof gate

For `a_h=arccos(1-h)`, `alpha_a=int phi_a ~ h^(3/2)`, and `F_a(u)=<k_a(W_f)>_u`, define

`B_(a,<=Lambda)=int_0^1 [2 Re <Q_u k_a Omega_u,G_u P_(0,Lambda] Q_u(b_g d_g)Omega_u>]_+/(2 sqrt(F_a(u)))du`.

The proved estimate bounds the ultraviolet contribution by `alpha_a/4` for sufficiently large fixed `L` at `Lambda=L h^(-11/8)`. The missing **independent nonlinear estimate** is `sup_f B_(a_h,<=Lambda)<=alpha_(a_h)/4`. Neither center parity nor Gaussian tangent positivity proves it.

## Reproducibility / release gates

1. Synchronize full local-only proof and verification packages with repository files or immutable release artifacts.
2. Add an explicit hypothesis and dependency index and automated execution of the complete verifiers.
3. Peer-audit coefficient normalizations, physical Hilbert-space projection, the gauge-reduced boundary domains, and every claimed volume-uniform constant.
4. Keep historical Stage26 numerical data and dissertation archive out of this proof-status certification until separately rechecked.

**No merge into main and no physical mass-gap result are claimed.**
