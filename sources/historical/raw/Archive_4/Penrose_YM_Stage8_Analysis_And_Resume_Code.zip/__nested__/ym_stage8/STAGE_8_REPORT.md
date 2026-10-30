# Stage 8: large independent-chain continuation and admission gate

**Status: incomplete thermalization; no physical mass or string tension extracted.** This is a computational progress and reproducibility report, not a continuum Yang–Mills measurement.

## Executed gauge-field continuation

From the verified Stage 7 20-slice M=55 rational Penrose torus (22,808 spatial vertices) and 151×151 square torus (22,801 vertices), both at beta_ref=3.5, we continued the exact checkpointed interacting Metropolis code using hashed seeds 101, 211, 307, 419. Each spacetime lattice has about 1.37 million SU(2) links. All checkpoint parameters are locked, and each completed segment checks the cached plaquettes against full recomputation.

| Geometry | Independently seeded checkpoints | Completed warm-up sweeps per seed (101, 211, 307, 419) | Post-burn samples |
|---|---:|---|---:|
| square | 4 | 24, 20, 20, 20 | 0 |
| penrose | 4 | 24, 20, 20, 20 | 0 |

The nominal burn-in cut is 1000 sweeps, so every completed step above is **thermalization**, not an equilibrium estimate. In particular, no 0++ correlator or torelon/string-tension measurement from these fields is admitted. Distinct seeds do not by themselves certify statistical independence or stationarity.

## Physical-separation screen

The archived deterministic 100-source measurement plans were compared using actual embedded path displacement. **8 / 11** unique square source lengths have a Penrose length within 5%. This helps select common radial bins for future static potentials, but orientation distribution, renormalized matching and operator-overlap biases are not controlled by this test.

## Acceptance ledger

| Requirement | Current status |
|---|---|
| four independent checkpoint states per geometry | Passed (checkpoint existence only) |
| four converged production chains per geometry | Not established |
| all chains postburn sampling | Not established |
| sampling precision Rhat less 1p01 ESS400 | Not established |
| scalar multi time covariance stable fit | Not established |
| confinement multi distance or winding fit | Not established |
| renormalized coupling and anisotropy match | Not established |
| finite volume and orientation stability | Not established |
| multiple cutoffs approximants and offsets | Not established |
| joint bootstrap ratio | Not established |
| continuum extrapolated contrast | Not established |

These criteria must not be conflated. Establishing multiple restorable chains is engineering progress but **not** convergence-certified Yang–Mills spectroscopy. Prior Stage 5 square data did not resolve a stable scalar mass or string tension. Stage 6 conditional sampling reduced raw winding-product fluctuations in a pilot, but its inner/outer convergence was not certified. Neither historical result can fill in absent Stage 8 production data.


## Longer-distance confinement measurement preparations

Beyond the inherited 1–5-edge Wilson path plan, a **separately versioned** 1–12-edge plan was constructed, containing 288 gauge-covariant spatial paths on *each* torus. Endpoints, directed edge continuity, graph hashes and physical displacement vectors were checked. The planned physical endpoint distances reach 6.57155 in the Penrose reference and 6.84130 on the square reference. The new files are `penrose_extra_paths.npz` and `square_extra_paths.npz`, with `stage8_extra_paths_report.json` for auditing. **These are geometric plans only; they have not been measured on equilibrated configurations.** The existing 100-path/3-level Wilson measurement format in the checkpoint code remains unchanged, preventing old and new observables from being silently mixed.

## Independent validation suite

The Stage 8 audit verified the SHA-256 of every archived checkpoint, the setting and graph lock, zero post-burn-in samples, the lengths and dimensions of all observable arrays, and the preserved RNG states. Six new tests for fail-closed reporting and correctly centered correlator construction passed. Previously inherited geometry assembly, deterministic restart, Haar initialization and gauge-invariance tests also passed again. Test completion confirms **implementation consistency**, not statistical equilibrium or physical predictions.

## Available deliverables and compute limits

The accompanying checkpoints contain actual 20-slice link and plaquette arrays plus RNG states, not fabricated observations. `stage8_campaign.py` resumes them; `stage8_admission.py` refuses a fit when the chain, measurement and statistical gates are absent. `stage8_slurm_array.sh` is a reproducible **example** for eight independent cluster jobs. The earlier runtime audit estimated approximately 33 hours for a four-seed 10k-sweep-per-chain campaign across both geometries, **before** full spectroscopy, convergence-driven extensions, multiple lattice spacings, and approximant/coupling matching. That full computation was not completed in this session.

**Scientific decision:** \(m_{0^{++}}\), \(\sigma\), \(m_{0^{++}}/\sqrt{\sigma}\), and any continuum contrast remain **not determined**. A reliable physical extraction cannot be claimed without actual equilibrated correlator measurements and fits.
