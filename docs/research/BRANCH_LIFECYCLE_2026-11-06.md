# Branch lifecycle and source-preserving retirement · November 6, 2026

**Repository:** `syncgravity/singular-boundary` (private). **Snapshot:** 78 remote branch references while this maintenance branch is still awaiting review: 1 default `main`, 3 open-PR branch heads, 1 independent unsubmitted homogeneous-flow branch, 1 active Observatory maintenance branch, and **72 prior integrated-history branch refs**. These 72 are only **retirement candidates**, pending a fresh SHA/ancestry and open-PR verification at execution time. No branch references have been deleted by this record.

## Integration is not ref deletion

Research source records from PRs #63–#73 and #75 were merged with history preserved through [consolidation PR #76](https://github.com/syncgravity/singular-boundary/pull/76), commit `a1689a5fa57c724bf24c2d965fc94faa737ba882`. Closing the redundant stacked PRs did not delete their remote branch heads. GitHub repo configuration has `delete_branch_on_merge=false`. That explains the unusually long branch list after a successful pull.

**All mathematical claims remain source-qualified.** Complete indexing of 754 tracked theorem files never certifies a complete continuum Yang–Mills or gravitational proof.

**Post-integration safety update:** PR #74 has been retargeted to `main` because its former Cartan base is already contained in `main`; it remains a **draft** with unresolved conflicts and is **not merged**. The retirement script now protects both `headRefName` **and** `baseRefName` for every currently open PR, so subsequent review stacks cannot lose a base branch accidentally. An open PR or non-ancestor branch must never be retired merely because an older ancestor PR was integrated.

## Research branches deliberately NOT retired

| Branch | Treatment |
| --- | --- |
| `main` | Canonical; never delete |
| `audit/2026-11-04-quantitative-local-fsum` ([PR #55](https://github.com/syncgravity/singular-boundary/pull/55)) | Independent f-sum audit; review separately |
| `audit/2026-11-05-p0-refinement-p4-source-visible` ([PR #56](https://github.com/syncgravity/singular-boundary/pull/56)) | Independent P0/P4 source audit; review separately |
| `audit/2026-11-06-nonabelian-tube-complete-theorem-index` ([PR #74](https://github.com/syncgravity/singular-boundary/pull/74)) | Parallel non-Abelian result with conflicting catalog methodology; reconcile before merging |
| `audit/2026-11-06-nonabelian-homogeneous-and-theorem-index` | Unsubmitted independent noncommuting analysis; reconcile separately |
| `maintenance/2026-11-06-observatory-754-index-sync` | Active maintenance branch; becomes a retirement candidate only **after** merging to main |

## Retirement method: safe, manual and recorded

This repository now provides [the reviewed cleanup script](../../scripts/safe_prune_merged_branches.sh) and [a manual GitHub Actions workflow](../../.github/workflows/retire-merged-branches.yml). It always runs on **main**, fetches live refs and checks every candidate's exact commit is an ancestor of `origin/main`. It excludes the four independent research branches and all open PR heads (via authenticated `gh`); it rechecks ancestry and uses a SHA lease for each remote deletion. A branch that moved after inspection cannot be deleted under that lease. **Git history, merged PR discussions and theorem files remain preserved in main.**

To run directly from GitHub after this maintenance PR merges: **Actions → Retire fully merged branch references (manual approval) → Run workflow**; select `dry-run` first. Inspect the eligible list. To retire them, select `retire` and type `DELETE_MERGED_BRANCHES` exactly. It is *never triggered by a normal push* and makes **no Pages deployment**. If no manual run is authorized, the branches remain visible.

Alternatively in a local authenticated Git checkout:

```bash
git switch main
git pull --ff-only origin main
bash scripts/safe_prune_merged_branches.sh --dry-run
# After reviewing the list, explicitly confirm:
bash scripts/safe_prune_merged_branches.sh --delete
```

## Snapshot of 72 candidate branch refs

These are **not deletion instructions**; all are subject to the live checks above. The commit SHA records allow audit if a name changes or is removed later.

| Candidate ref | Recorded head SHA |
| --- | --- |
| `audit/2026-10-28-independent-reconstruction` | `eafaa6d2fb288d1bd92de2dfe7a63167100f4cd6` |
| `audit/2026-11-04-knowledge-graph` | `d6b338454f26502cb1e5e47a5dd5421149e6bbd8` |
| `audit/2026-11-04-p0-heat-kernel-transfer` | `4baa79166ddff88bbee15a18116086b3561036d4` |
| `audit/2026-11-04-uniform-continuum-bridge` | `f049fd034fe2883690c4942b08c35286eed52a19` |
| `audit/2026-11-05-cubic-haar-blocking` | `5d902e6aae40d56becd7d7befafa5b09f34ac419` |
| `audit/2026-11-05-mathematical-physics-bridge` | `29e5258cfcba3c4cc4b87b006293a6d79032cb41` |
| `audit/2026-11-05-penrose-primary-control` | `9527bae74c6df3e0aeb67f7f49764fce5ec99c30` |
| `audit/2026-11-05-physical-radius-linearized-cubic-flow` | `204c8f6235e2224219d387c64191595da42e420b` |
| `audit/2026-11-06-cartan-positive-time-cubic-smoothing` | `e64a6f57a742043cdcea4fb708e9ee80f715527a` |
| `audit/2026-11-06-cubic-transverse-shell` | `c782e0c3d52525b1cb8e1a80196a12d6fceb7b39` |
| `audit/2026-11-06-full-nonabelian-locality-and-index` | `b7e160af1d32a521b8b4a2464268aa402a4932c5` |
| `audit/2026-11-06-full-wilson-time-memory` | `f2a50dc7040b936afb4bc23748f34a32d4505632` |
| `audit/2026-11-06-local-wilson-fisher-thermodynamic` | `5aafdda968570c0f2c1e83abde81b04fb3c1e635` |
| `audit/2026-11-06-marginal-harnack-loop-sumrule` | `ffd90e884e50dba646157e1ee35819e5c229fc00` |
| `audit/2026-11-06-nonlinear-cubic-physical-energy` | `515beb37cd11696725f64d2042c96ea3a474ab9d` |
| `audit/2026-11-06-two-scale-influence-kernel` | `cba3beb0c4ac5645f39fb811c46fdbc0e957157f` |
| `audit/2026-11-06-vacuum-weighted-schur-form` | `8ea33a1dab81e64cec4f0dc7e911d65796a98129` |
| `audit/2026-11-06-wilson-spatial-flow-fisher-gap` | `e39c406e862d5201975cc63a50644e31cd8e68fc` |
| `audit/handoff-verifier-security-tests-2026-11-01` | `01d87b30441a63358864cd10ad96e6508858355e` |
| `audit/source-and-original-inputs-2026-11-01` | `0de099867b1f70a1c6a62595df69b13a8aed0897` |
| `audit/source-trace-381-392-2026-11-01` | `40d06c7144ef4e8efd66da85e0190ed1f1670117` |
| `audit/theorem-source-certification-batch01-2026-11-01` | `5e06b556c0ac3b9525437120cdec10592ad8ff36` |
| `docs/research-navigation-provenance-2026-11-01` | `add0f2f1d40d8370b5a82d83ddd898fb0214ba62` |
| `feature/research-observatory-2026-11-04` | `fa679010eb51773ff3f1cc5df6b37e2ffedb0488` |
| `fix/reproducible-research-handoff-2026-10-30` | `630ee91f13c0b857b5b5a496a45c623453f0361c` |
| `reconcile/claim-identity-crosswalk-2026-11-01` | `b55943eb5bafe47d39415baba12df01506e6b716` |
| `reconcile/historical-branches-2026-11-01` | `5060286eb7def96f22e404ddb6e5b3364a100412` |
| `reconcile/immutable-ledger-snapshots-2026-11-01` | `dd7505dd05172a0dbda925b8944768a0524fc41a` |
| `release/2026-11-05-observatory-v2-29` | `21462c8abcf59c55e3a2d4b9dafe9fd3f621e1db` |
| `research/arbitrary-four-degree-pw-threeface-2026-11-04` | `3e172480b5ea1183f321ad9e47878f568750b976` |
| `research/direct-face-nested-casimir-tame-2026-11-04` | `3f972f6dd1d2e1b494d2fc00de26e82cfc8fcece` |
| `research/exact-haar-cubature-frechet-entire-borel-2026-11-04` | `3af303a21bdb9794b14e8aea27758b0fd32f1e33` |
| `research/gauge-balanced-twirl-borel-optimum-2026-11-04` | `e7424eae7ee1a5f3c2507db6ebcf5a93a9358194` |
| `research/gauss-twirl-spectrum-historywise-borel-2026-11-04` | `dfae329d12d2632f0588eb8337ddd7a1e49338fe` |
| `research/highspin-recoupled-matrix-sectors-2026-11-04` | `cc29b17abeb44d072730829d076afc5fd8d3ca6d` |
| `research/local-first-borel-audit-2026-11-04` | `dd2b20cae4c6392f1bfab48f0659f78fffe85cd6` |
| `research/local-pw-poisson-two-certified-gates-2026-11-04` | `72892ccacadc1ad3c276d9677d6f7a204b2d2107` |
| `research/nested-physical-pw-regression-2026-11-04` | `c48121fcc0b92ff55084cd3567047dc8b9614c25` |
| `research/noncharacter-overlapping-traces-2026-11-04` | `652be8c857de9c1675dc2886a5925607423aff0c` |
| `research/p2-bernstein-thermodynamic-local-measures-2026-11-04` | `b224784ca9cffbd16bd2cb90d30d9e257f99cc3c` |
| `research/p2-central-binomial-quantum-local-states-2026-11-04` | `80e9c60e2544973e648db08e5a8493f8bac7ed74` |
| `research/p2-certified-brackets-borel-tails-observatory-version-2026-11-04` | `885c01a535743cf0ddae6134a56fc26df6a20896` |
| `research/p2-chebyshev-first-frequency-2026-11-04` | `db7f87826577734dd9ea11ae0c1b067c36a0def6` |
| `research/p2-collar-s1-hopf-graph-2026-11-04` | `cba6716457005243ecd96cd7cdb9f3d4a790e943` |
| `research/p2-electric-depth-positive-frequency-2026-11-04` | `ea1600d3b7c341515266ea8d3567671ca68ffce8` |
| `research/p2-exact-physical-inverse-fourth-frequency-2026-11-04` | `34ef8f022d2625b36548c3e65f2b9d83383bddba` |
| `research/p2-extremal-counterexample-borel-germ-2026-11-04` | `d7fb1052cc71458ea1359df80a52a90fb069c98c` |
| `research/p2-fixed-collar-jacobi-scalar-borel-2026-11-04` | `033acf5d34c5dcd6d18806bad4f89287969e240a` |
| `research/p2-fourface-physical-inverse-casimir-c2-obstruction-2026-11-04` | `475ae3a382297333ab75edd6585429186199d436` |
| `research/p2-full-inverse-dual-factorial-borel-2026-11-04` | `9d56dc1327fcb846e504e93d7a2c63166949a267` |
| `research/p2-fusion-dimension-weighted-domain-2026-11-04` | `0af649c5cee3262115c104f62ef09b0ec4a85b4e` |
| `research/p2-gram-dual-history-weight-obstruction-2026-11-04` | `a8ecd6657d16806c4ab58406d017f18095f53847` |
| `research/p2-highrank-thermodynamic-energy-2026-11-04` | `f41646071f2f5f32cfcfe5b1343b92ca759f9a79` |
| `research/p2-local-fusion-source-half-casimir-2026-11-04` | `bf189b3fb821608726ca8fcb40cf5dbcdb92d351` |
| `research/p2-onehaar-dual-sourceorder-algebra-2026-11-04` | `5196849870f1da833bfa66d6230ba7d18929067f` |
| `research/p2-rayleigh-witness-cap-finite-real-score-2026-11-04` | `1d293e06a7494a989cf3de077c3291cfe3659047` |
| `research/p2-schur-gram-norm-dynamics-2026-11-04` | `0a9b906ff25f1a76c2496d3da18403b542a1cf7f` |
| `research/p2-schur-rank-local-ground-form-2026-11-04` | `b8222894a898b2f3f2bdcd081e0e46f0243ae2d5` |
| `research/p2-source-mpo-cylinder-dirichlet-2026-11-04` | `3949a3d2462a3118efeedbed83d8ce12605a7140` |
| `research/p2-trace-ideal-log-depth-second-time-2026-11-04` | `ca3e272f3b40f7e03a7f3398c3e3ffd99c19e73f` |
| `research/p2-wigner-gram-casimir-dynamics-2026-11-04` | `ad8a239812381ce8bfa4728e3ea0aaac12aa11bb` |
| `research/physical-twirl-response-borel-volterra-2026-11-04` | `e3e5de7b2c41208f16a11a50eb8c630aaa393d9c` |
| `research/pw-norm-transport-operator-audit-2026-11-04` | `8aed16fe6d1123fc4487ac0b338bb8662608c1aa` |
| `research/summed-gauss-sectors-infinite-borel-germ-2026-11-04` | `a1fa3ea7e6539106f466cc96e2b8e4e2922c8239` |
| `research/tensor-gram-supergaussian-borel-2026-11-04` | `a7d45150e18d9249d3c43767804dc0e824429efa` |
| `research/three-independent-spins-2026-11-04` | `864bbc4f975b1e2c3670619d1e78dee19c8f6a3e` |
| `research/threeface-nested-pw-2026-11-04` | `eec2b5899451fe24d012307f2f9dab1db598c516` |
| `research/two-extended-histories-2026-11-04` | `efddee8d971ce7a97353b251b405ff46023b4a97` |
| `research/two-highspin-threeface-2026-11-04` | `b27bfa986b0122c62b0bc8506ee8a9ebbb0aeaf3` |
| `research/twoface-singleton-width2-one-step-2026-11-04` | `d535f800412e52cb4400b6003c701a9373e61a6c` |
| `research/weighted-unbounded-nested-casimir-2026-11-04` | `652a2dd2a1feebf9fb6eb5ec67d299811842e93b` |
| `research/width34-feedback-crossing-pw-2026-11-04` | `cf98deb740a3bcfc67e4c324706226fdec34fc17` |

**After manual retirement:** assuming the active maintenance branch has been merged and no new branches have been created, the expected remaining refs are `main` plus the four independent branches. GitHub may retain tags and PR histories but those do not appear as branches. Do not prune any unmerged branch merely because its PR is old.

## Observatory and theorem source visibility

The [current complete theorem navigator](THEOREM_INDEX_CURRENT.md) covers 754/754 source paths; the [historical navigator](THEOREM_INDEX.md) maintains the prior 740-record snapshot and later appendices. The [source-hashed registry](THEOREM_INDEX_LIVE.json) governs both the searchable [Observatory](../../observatory/index.html) and [Proof Atlas](../../observatory/graph.html). [Automatic consistency checks](../../observatory/tools/sync_theorem_catalog.py) guard against future stale counts. All P0–P5 and transfer/UV gates remain OPEN.
