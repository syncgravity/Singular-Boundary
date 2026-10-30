# Periodic Penrose spatial slices in interacting 2+1D SU(2) Wilson theory

**Research report: 11 October 2026.** Status: **computed pilot** (fresh simulations in the accompanying code); **exact/combinatorial** (directly checked algebraic identities and test assertions); **not yet established** (any renormalized continuum or pure-glue excitation-gap difference). All reported errors are nominal Monte Carlo blocked standard errors, conditional on approximately independent blocks. Do not mistake a numerical contrast at fixed cutoff for a universal Penrose effect.

## Executive decision

The geometrically weighted 2+1D SU(2) Wilson discretization *does* exhibit easily resolved finite-cutoff Penrose-versus-square differences in spatial and temporal plaquettes, as well as gauge-invariant temporal Wilson rectangles. However, under the important control that **replaces the Penrose's heterogeneous geometric Wilson couplings by uniform, mean-matched couplings on exactly the same Penrose incidence graph**, those differences become unresolved at the precision of this study. Shuffling geometric weights while retaining their multiset on the Penrose graph preserves a sizable difference.

**Interpretation:** the numerical contrast is substantially mediated by the heterogeneous local **geometric coupling prescription**, not shown to be an intrinsic causal consequence of Penrose incidence alone. This is a finite-discretization result in a real interacting three-dimensional gauge model. It is **not** evidence that a continuum 2+1D Yang–Mills glueball gap changes on a Penrose background: renormalized couplings, physical source separations and continuum limits have not all been matched; the connected scalar correlator is not significant at sufficient nonzero temporal separations for a reliable gap fit.

## I. Geometric/spacetime construction

Imported source: `penrose_causal_study.py` from the preceding, independent direct-Z^5 rational-slope cut-and-project study. The periodic approximants comprise oriented four-edge rhombic faces and directed lattice edges exactly from their integer-lattice incidence. The physical face area is the magnitude of the determinant of two projected Z^5 basis vectors, with the physical plane defined by the rational period spans. The fundamental spatial area is the period-parallelogram determinant and equals the sum of all face areas.

For each spatial graph with V vertices, E edges and F faces, cross with a **common periodic Euclidean time circle** of N_t=10 steps. The 3D lattice has N_t(E+V) links and N_t(F+E) plaquettes. Spatial plaquettes retain the four directed rhombic (or square) edges, and each spatial edge e=(u,v) generates a temporal plaquette with oriented boundary

`U_e(t) T_v(t) U_e(t+1)^(-1) T_u(t)^(-1)`.

Both types enter the interacting SU(2) Wilson action:

`S = sum_(t,f) beta_s(f) [1 - P_f(t)] + sum_(t,e) beta_t(e) [1 - P_e^time(t)]`,

where `P = (1/2) ReTr` of the ordered plaquette holonomy and all links are dynamical SU(2) matrices. There is no gauge fixing. Link Metropolis decisions use **all** incident plaquettes (four for a spatial link, spatial-vertex degree 3–7 for a temporal link). This is genuinely a 3D interacting lattice action, not a stack of independent 2D ensembles.

### Calibrated geometry and the remaining calibration limitation

Let A be the common total physical spatial area; a_* = sqrt(A/F_Penrose), and the common time step is a_t=a_*. For a spatial rhombus f of area A_f and a spatial edge e of length l_e adjoining rhombi f_L and f_R, start from the *diagonal geometric Hodge approximation*

`beta_s(f) = beta_ref (a_* a_t/A_f)`,

`beta_t(e) = beta_ref (a_*/a_t) (A_(f_L)+A_(f_R))/(2 l_e^2)`.

On a square lattice with spacing a_sq, these become spatial `beta_ref a_* a_t / a_sq^2` and temporal `beta_ref a_*/a_t`. To avoid the large, trivial mismatch in mean bare couplings resulting from unequal cell shapes, the **primary study further rescales the Penrose spatial and temporal weight sets independently so each average equals its paired square average**. Spatial variations within each weight family are retained. Thus matching is at the **mean bare Wilson coupling level**, not nonperturbatively matched physical gauge coupling, string tension, renormalized anisotropy or an exact nonorthogonal finite-element Hodge star. The diagonal geometric Hodge rule itself is not unique: it is one explicit, gauge-invariant discretization of the local metric.

The shape-calibrated square controls preserve total area with near-square periodic aspect and nearly equal number of faces, but different physical nearest-neighbor distances:

| Penrose scale | A (physical spatial area) | Penrose F | square F | common a_t | Penrose mean spatial edge | square spatial edge |
|---|---:|---:|---:|---:|---:|---:|
| M=5 | 61.70899 | 188 | 182 (13×14) | 0.572922 | 0.634336 | 0.582289 |
| M=8 | 160.09997 | 492 | 483 (21×23) | 0.570444 | 0.632720 | 0.575734 |

NOTE: The actual square periodic dimensions for M=5 and M=8 should be verified from the generated square period matrices (automatically selected by the script; 13×14 and 21×23 respectively here). Square links are approximately 8–10% shorter than the average Penrose edge. Consequently comparing **one-edge** Wilson rectangles does NOT match physical static-source separation. An additional square control matches that separation approximately, at the cost of differing lattice face density: M=5, 12×13 (156 faces, edge length 0.628944); M=8, 20×20 (400 faces, edge length 0.632653). In this second control the square mean bare couplings are held at the original density-comparison values, and the unchanged Penrose ensemble serves as reference. This control illustrates sensitivity but does not solve simultaneous physical renormalization/cutoff matching.

## II. Monte Carlo design and verification

* Gauge group SU(2), quaternion links, Haar-random starts, symmetric compact left-multiplication proposals, local Metropolis updates; N_t=10 periodic time steps.
* Production *geometric-weight* runs: beta_ref=2.5 and 3.5, M=5 and M=8, two independent random seeds (109, 211) for each graph; 240 thermalization sweeps and 1,000 measurement sweeps per chain; every fourth configuration stored; 10 stored-configuration blocks (40 sweeps) for standard errors.
* Uniform-coupling diagnostic: M=5 beta=2.5 and 3.5, M=8 beta=2.5; 200 thermalization and 650 measurement sweeps per chain, every fifth stored, 10-configuration blocks. The M=5 shuffled diagnostic (beta=2.5) uses the same shorter settings; a deterministic fixed shuffle acts on the face and edge coupling distributions, identically at every time slice.
* Rectangular Wilson loops: for a spatial edge e joining u and v, and any temporal lag k, measure `W_e(k)= (1/2) ReTr[U_e(t) T_v(t,t+k) U_e(t+k)^(-1) T_u(t,t+k)^(-1)]`, averaged over t and edges. k=1 is *exactly* the temporal plaquette. Test verifies that these loops are gauge-invariant under independent vertex-dependent SU(2) transformations.
* Connected gauge-invariant scalar correlator: `O(t) = [sum_f (1-P_f(t))/A_f]/[sum_f 1/A_f]`, and `C(k)=<O(t)O(t+k)>-<O>^2`, evaluated with all t and blocked leave-one-block-out jackknife. The normalization is convenient for comparison; the operator is not smeared or variationally optimized.
* For static-source energy only, examine `V_eff(k)= - log[W(k+1)/W(k)]/a_t`. This is a Wilson rectangle static-source effective energy **not** a 0++ vacuum glueball gap.

Full 3D plaquette paths close, all link-face incidence degrees are correct, gauge transformations preserve the plaquettes and temporal rectangles, and direct full-action updates equal the local Metropolis action change. Including the six tests from the preceding geometry package, **12 tests pass**. Cached plaquettes also agree with independently recalculated final values in the Markov chains. Independent extraction of the package is checked by the packaging run.

## III. Measured differences in the gauge ensemble

### Penrose-minus-square, geometric-weight model

| Penrose scale | beta_ref | Δ spatial plaquette | Δ temporal plaquette | Δ temporal rectangle, k=2 |
|---|---:|---:|---:|---:|
| M=5 | 2.5 | −0.013556 ± 0.000885 | −0.006058 ± 0.000681 | −0.005146 ± 0.001007 |
| M=5 | 3.5 | −0.014086 ± 0.000625 | −0.006348 ± 0.000485 | −0.007471 ± 0.000824 |
| M=8 | 2.5 | −0.010245 ± 0.000477 | −0.004349 ± 0.000431 | −0.003729 ± 0.000591 |
| M=8 | 3.5 | −0.009615 ± 0.000347 | −0.004848 ± 0.000322 | −0.006427 ± 0.000573 |

Each error uses pooled independent-chain blocked errors added in quadrature. These are nominal sampling errors, not continuum/matching/discretization/systematic errors. Both increasing approximant sizes leave a nonzero fixed-cutoff contrast under the chosen geometric weights; M increases **spatial volume at roughly fixed local tile scale**, not a→0 at fixed physical area.

### Causal interventions at fixed lattice scale

| Model/intervention | M | beta_ref | Δ spatial plaquette | Δ temporal plaquette | Δ k=2 temporal rectangle |
|---|---:|---:|---:|---:|---:|
| Geometric weights | 5 | 2.5 | −0.013556 ± 0.000885 | −0.006058 ± 0.000681 | −0.005146 ± 0.001007 |
| **Uniform matched mean weights** | 5 | 2.5 | +0.000268 ± 0.001097 | −0.000117 ± 0.000931 | −0.000371 ± 0.001203 |
| **Same weights, shuffled across Penrose sites** | 5 | 2.5 | −0.015715 ± 0.001066 | −0.005673 ± 0.000849 | −0.005169 ± 0.001070 |
| Geometric weights | 8 | 2.5 | −0.010245 ± 0.000477 | −0.004349 ± 0.000431 | −0.003729 ± 0.000591 |
| **Uniform matched mean weights** | 8 | 2.5 | +0.000767 ± 0.000633 | +0.000783 ± 0.000504 | +0.000709 ± 0.000698 |
| Uniform matched mean weights | 5 | 3.5 | −0.000344 ± 0.000728 | −0.000723 ± 0.000661 | −0.001273 ± 0.001222 |

The operational result is unusually informative: the *same Penrose incidence* produces a large Penrose-square contrast with heterogeneous shape-derived couplings, but little resolved difference with uniform, mean-matched couplings. Shuffling the heterogeneity while retaining its marginal distribution and keeping the Penrose topology does not eliminate the effect at current precision. This favors coupling **heterogeneity** over the detailed Penrose incidence/weight placement as its proximate cause in the measured observables. It is not a theorem that 2+1D incidence never matters; the matched homogeneous difference is bounded only at this experiment's precision and parameters.

## IV. Temporal observables and the gap question

The gauge-invariant Wilson rectangles have excellent signal over k=1..5 and decay approximately exponentially in the observed range. Representative *point estimates* of the nearest-neighbor static-source effective energy from the ratio W(2)/W(1):

| M | beta_ref | Penrose V_eff(1) | Density-matched square V_eff(1) | Length-matched square V_eff(1) |
|---|---:|---:|---:|---:|
| 5 | 2.5 | 1.0423 | 1.0318 | 1.0299 |
| 5 | 3.5 | 0.6361 | 0.6249 | 0.6270 |
| 8 | 2.5 | 1.0438 | 1.0361 | 1.0319 |
| 8 | 3.5 | 0.6336 | 0.6224 | not run |

These ratios are **not asymptotic static-source energies**, let alone glueball gaps: k=1 can have excited-state and contact effects; the first geometric-weight production runs did not archive the covariance-aware jackknife errors of the *ratio itself* (only Wilson loop means and their errors), and the physical nearest-neighbor distances of the density-matched square and Penrose graphs differ. The shorter uniform and length-matched controls do archive jackknife ratio errors in JSON, but they do not cure the physical/renormalization or long-k plateau problem.

The connected scalar correlator provides the relevant gauge-invariant 0++-channel candidate. Its second nonzero temporal lag C(2) is **not resolved at >=3 blocked standard errors in any principal matched run**: for example, at M=8 beta=2.5, Penrose C(2)=(0.62±3.20)×10^-6 and square C(2)=(0.26±3.74)×10^-6. At M=8 beta=3.5, Penrose C(2)=(0.48±1.68)×10^-6 and square C(2)=(−2.68±2.48)×10^-6. Thus **no reliable scalar mass/gap and no reliable Penrose-minus-square gap difference can be extracted**. Fitting a two-point exponential or a cosh in this regime would be numerology. An unsmeared spatial plaquette average is a weak interpolating field for higher excitation channels; temporal multilevel sampling and variational smearing are needed.

## V. Causal verdict and next decisive work

**Established by computation (finite lattice):** the interacting 3D Wilson action on periodic Penrose spatial slices has different plaquette and temporal-rectangle means from a near-density- and area-matched square control when one imposes a nonuniform diagonal geometric Hodge rule; those differences are resolved far beyond the nominal blocked Monte Carlo fluctuations. This occurs at two couplings and two spatial approximant sizes.

**Established as a finite-lattice control:** homogenizing the Penrose local couplings while retaining all the Penrose graph incidence reduces each measured Penrose-square difference to a statistically unresolved level; shuffling the original geometric couplings does not. This implicates the marginal distribution of local coupling weights and finite-cutoff metric discretization as the leading mechanism, not a demonstrated universal aperiodic-incidence effect.

**Not established:** any change in the continuum Yang–Mills mass gap, string tension or other renormalized long-distance dynamics due specifically to Penrose geometry. The numerical Euclidean time correlator is too short/noisy for the scalar gap; bare mean coupling is not equivalent to a matched renormalized coupling; a density-matched square and Penrose nearest-neighbor loop probe different physical lengths; and the two spatial scales are volume changes rather than a controlled a→0 trajectory.

To make the next experiment decisive, pre-register the observable `m_(0++)/sqrt(sigma)` and possibly a static-source potential V(r)/sqrt(sigma) at **equal physical r**, and:

1. Define and test a genuinely isotropic, gauge-invariant nonorthogonal geometric discretization or explicitly contrast multiple positive geometric prescriptions; avoid interpreting one arbitrary diagonal Hodge star as geometry-independent physical truth.
2. Determine a matched renormalized scale (e.g., long Wilson-loop string tension), tune spatial and temporal bare couplings *separately* so that the physical anisotropy and reference coupling agree, and use the same physical spacetime volume and shape.
3. Compute physical-area-binned Wilson loops, variational/smeared 0++ operators, temporal correlators with multilevel variance reduction; show a >=3-point fit window and stable effective-mass plateau with covariance-aware fits and block-length/thermalization checks.
4. Vary phason offset, rational approximant scale, spatial physical volume and time extent; perform an actual continuum trajectory by scaling tiles down while increasing beta_ref and N_t to keep physical volume/time fixed. Distinguish finite-volume, finite-cutoff and aperiodic-order effects.
5. Require the final continuum-extrapolated geometry contrast to persist with a confidence interval excluding zero **after** reference-scale and operator matching; otherwise the defensible conclusion is no established universal geometry effect.

The pre-existing exact two-dimensional character-expansion result is unaffected. It does not furnish a no-go theorem for 2+1D Yang–Mills. The current computational study tests that open territory without mistaking a short-distance response or source-distance mismatch for a corrected excitation gap.

## Reproduction

Dependencies: Python 3, numpy, scipy, numba, pytest, matplotlib (only for plots). Source: `penrose_causal_study.py`, `wilson_torus.py`, `penrose_2p1_study.py`, `test_penrose_causal.py`, `test_penrose_2p1.py`, `analyze_2p1.py`, `plot_2p1.py`, `length_matched_control.py`. JSON files contain parameters, all independent-chain summary statistics, coupling ranges and cache residuals; `study_2p1_aggregate.json` contains every displayed contrast. Four original geometric-model runs are `study_2p1_M5.json` and `study_2p1_M8.json`; additional controls are named `uniform`, `shuffled`, and `lengthsquare`.

Commands (from extracted package root):

```bash
pytest -q test_penrose_causal.py test_penrose_2p1.py
python penrose_2p1_study.py --M 5 --betas 2.5 3.5 --nt 10 --seeds 109 211 --burn 240 --steps 1000 --thin 4 --block 10 --out study_2p1_M5.json
python penrose_2p1_study.py --M 8 --betas 2.5 3.5 --nt 10 --seeds 109 211 --burn 240 --steps 1000 --thin 4 --block 10 --out study_2p1_M8.json
python penrose_2p1_study.py --M 5 --betas 2.5 3.5 --nt 10 --seeds 109 211 --burn 200 --steps 650 --thin 5 --block 10 --weight-mode uniform --out study_2p1_M5_uniform.json
python penrose_2p1_study.py --M 8 --betas 2.5 --nt 10 --seeds 109 211 --burn 200 --steps 650 --thin 5 --block 10 --weight-mode uniform --out study_2p1_M8_uniform.json
python penrose_2p1_study.py --M 5 --betas 2.5 --nt 10 --seeds 109 211 --burn 200 --steps 650 --thin 5 --block 10 --weight-mode shuffled --out study_2p1_M5_shuffled.json
python length_matched_control.py
python analyze_2p1.py
python plot_2p1.py
```

This is a fresh extension of the preceding independent geometry/Wilson code. Prior dissertation-specific excitation gaps and scripts from older conversations were not available here and were not silently equated with these new 2+1D correlators.
