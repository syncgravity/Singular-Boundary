# Penrose geometry and the causal Wilson comparison

**Research note — 11 October 2026.** Status terms: **exact** = mathematical derivation under stated assumptions; **computed** = run from independently written code in this bundle; **not verified here** = prior work or analysis not reproducible from the attached sources.

## Question and scope

Does the aperiodic incidence of a corrected Penrose model-set graph itself cause a change in an interacting Wilson gauge observable, rather than a graph-generation artifact, discretization choice, differing finite volume, or Monte Carlo fluctuation?

The previous conversation reportedly established and tested a corrected direct-Z^5 generator and recalculated a gauge ensemble, including a corrected excitation-gap calculation. Those particular scripts, tests and numerical results are **not present** in the uploaded dissertation TAR archive (which contains PDFs). This note does not replace or revalidate the prior exact gauge-theoretic results or assert that the independent SU(2) code exactly reproduces prior simulations.

## Exact no-go theorem for homogeneous *2D pure* Wilson theory

Let `G` be a compact gauge group, choose a connected closed oriented cellular embedding of a finite graph into a genus-`g` surface, assign an independent normalized Haar link variable `U_e` and attach a class-function plaquette weight `w_beta(U_f)=exp(beta * (1/2) Re Tr(U_f))` for SU(2). The standard action is `S=beta sum_f [1-(1/2) Re Tr(U_f)]`.

Expand `w_beta(U)=sum_r d_r c_r(beta) chi_r(U)` with `c_r(beta)=(1/d_r) int_G dU w_beta(U) chi_r(U^-1)`. Orthogonality of representation matrices on each link, followed by the standard face contraction, gives

`Z(beta) = exp(-beta F) sum_r (d_r)^(2-2g) (c_r(beta))^F`.

Thus **at fixed F and g**, the partition function, mean plaquette and derivatives of free energy are exactly independent of the graph's local incidence, rhombic angles, aperiodicity or face layout. For a torus `g=1`, the dimension factor is `d_r^0=1`.

For SU(2), index irreps by `n=2j+1=1,2,...`: `c_n(beta)=2 I_n(beta)/beta`, hence

`Z_torus(beta)=exp(-beta F) sum_(n>=1) [2 I_n(beta)/beta]^F`.

The nontrivial-representation contributions are exponentially suppressed in F. The large-F Wilson mean plaquette is exactly

`< 1/2 Re Tr U_f > = I_2(beta) / I_1(beta)`.

Even for heterogeneous face weights `beta_f`, the exact partition function factorizes in the representation sum:

`Z({beta_f})=exp(-sum_f beta_f) sum_r d_r^(2-2g) prod_f c_r(beta_f)`.

Therefore the ordering of the face couplings is invisible to the pure 2D partition function; only their multiset matters (for matched genus and normalization). Geometry may change how physical lengths/areas are associated with lattice loops, but not create an intrinsic dependence on *which face is adjacent to which* in this model.

This no-go theorem **does not apply** without further work to 2+1/3+1-dimensional gauge dynamics, matter, nonlocal interactions, edge/vertex couplings, boundary conditions, gauge-invariant time-dependent spectra, or geometrically specified Wilson-loop families not matched by enclosed plaquette number.

## Computed: rational-slope Z^5 model-set periodic approximants

Define the irrational physical two-plane `E_parallel` by the 5-star columns `(cos(2 pi j/5), sin(2 pi j/5))`, for `j=0,...,4`. Internal space is the orthogonal complement, of dimension three. The canonical vertex window is the orthogonal projection of `[0,1]^5` to internal space. Fix a generic phason displacement whose five components sum to zero: this ensures integer-sum layers 1, 2, 3, 4 are **four pentagons**, rather than inappropriately slicing the 3D window between those layers.

For each integer scale `M`, approximate the physical plane by the rational span of the rounded integer cosine and sine five-vectors, adjusting the cosine first coordinate to enforce sum zero. Take the orthogonal complement to construct its *own* projected hypercube window (rather than mixing an irrational window with rational periods). Quotient lattice vertices by the two integer periods. Retain edges exactly from `n` to `n+e_j` and rhombic faces exactly when all four corners of a two-coordinate square are accepted. The generator operates directly in Z^5, never inferring tiling edges from plotting proximity.

For `M=13`, the **chosen near-square supercell periods** are `T1=(14,4,-11,-11,4)` and `T2=(0,12,8,-8,-12)`. The corresponding quotient has V=1360, E=2720 and F=1360, with orthogonal physical period lengths approximately 21.68 and 20.40. These periods generate an **index-four sublattice** of the full integer period lattice, so the torus is a fourfold cover of the primitive rational-plane torus. The fully saturated primitive cell can also be generated (`primitive_periods=True`): its periods are `T1=(14,4,-11,-11,4)`, `T2=(0,3,2,-2,-3)`, with V=F=340, E=680. The near-square supercell was deliberately used to avoid extreme spatial aspect ratio in the primary matched comparison; neither choice changes the local infinite periodic tiling. Across checked scales `M=3,5,8,13,21,34,55`: (a) four slice windows each have five polygon vertices, (b) all edges have two opposite-oriented face incidences, (c) Euler characteristic V-E+F=0, (d) every vertex has degree from 3 through 7, and (e) summed face areas equal the period-parallelogram area to numerical precision.

The accepted Z^5 vertex/one-step-neighbor decisions were also independently recomputed against separate *2D pentagon* halfspaces; at `M=13`, all 6,736 such classification cases agree. At M=55 all 112,792 audited cases agree.

The approximant subspaces converge to the irrational plane as M increases (integer rounding introduces O(1/M) directional errors). For a nonsingular phason, each fixed finite set of lattice membership decisions therefore eventually stabilizes, giving local convergence of graph balls. Direct common-seed tests found zero discrepancies through graph-ball radius 2 at M=8, radius 4 at M=21, radius 5 at M=34, and radius 6 at M=55. At M=13 the chosen seed has a radius-1 discrepancy; local agreement across different finite scales is not required to be monotone.

## Computed: matched interacting SU(2) Wilson comparison

Independent Metropolis implementation: quaternion SU(2) link variables; each candidate link rotation receives the exact local change of the two adjacent Wilson plaquettes; beta multiplies the plaquette's scalar trace; proposal distribution symmetric; full Haar-random starting links; periodic 2D cellulations, equal `F=1360`, equal link count `E=2720`, equal homogeneous Wilson beta, equal gauge group and update settings.

Geometry: Penrose M=13 torus versus square 34×40 torus. New code tests verify that a vertex-dependent local SU(2) gauge transformation leaves every Penrose plaquette trace unchanged, that all faces are closed and oriented, and that the cached plaquettes exactly equal recomputed final values.

Initial run: **3 independent seeds**, `250` warm-up sweeps and `750` measurement sweeps per chain. Standard errors are computed from 25-sweep blocks pooled across chains, with interblock independence assumed approximately.

| beta | Penrose plaquette | Square plaquette | Exact large-F | Difference Penrose − square |
|---|---:|---:|---:|---:|
| 2 | 0.433266 ± 0.000452 | 0.433074 ± 0.000423 | 0.433127 | +0.000192 ± 0.000618 |
| 4 | 0.657329 ± 0.000348 | 0.658370 ± 0.000344 | 0.658047 | −0.001041 ± 0.000489 |

The initial beta=4 difference was 2.13 nominal standard errors and therefore called for an independent validation rather than a claimed effect. Fresh-seed **beta=4 recheck** (`3` additional chains, `500` warm-up and `1500` measurement sweeps each) returned:

- Penrose: `0.658338 ± 0.000238`
- Square: `0.658368 ± 0.000269`
- Difference: `−0.0000294 ± 0.0003593` (−0.082 standard errors).

Inverse-variance combination of the two *independent* beta=4 runs gives `−0.0003836 ± 0.0002896` (−1.32 nominal standard errors). Both beta settings are consistent with the exact zero difference.

A further calculation on the **primitive index-one M=13 torus**, matched to a 17×20 square torus of F=340, also found no resolved effect: at beta=2, `+0.000872 ± 0.001295` (0.67 standard errors), and at beta=4, `+0.000768 ± 0.000970` (0.79 standard errors). The primitive comparison uses three fresh seeds and 250 warm-up/750 measurement sweeps per chain. Its physical aspect ratio differs from the square control, which would be a confound for dynamical observables, but not for the exact 2D plaquette equality.

The blocked Monte Carlo uncertainties should not be interpreted as proof of ergodicity or a complete autocorrelation analysis. The exact character argument, not the Monte Carlo p-value, provides the geometry-independence result for the stated model.

## Causal conclusion and the experiment that remains

**Established, conditional**: the corrected Penrose rhombus incidence causes no change in a homogeneous pure 2D SU(2) Wilson partition function or mean plaquette at fixed topology, F and beta. A claimed graph-specific bulk plaquette effect in this exact model would indicate unmatched couplings/observables, a faulty cell complex, faulty update, boundary/topology differences or statistical noise.

**Still open**: whether the Penrose-specific physical incidence, face geometry or spectral content modifies **2+1/3+1D Yang–Mills dynamics** when modeled on a spatial Penrose slice. The next causally informative test is a periodic Penrose spatial approximant crossed with a calibrated periodic Euclidean time direction, comparing to a density/volume/shape-calibrated square-lattice spacetime. Temporal-spatial plaquettes and dynamical spatial plaquettes must both be present. Define the physical discretization precisely (dual-cell/geometric face weights, temporal lattice spacing, couplings, renormalization scale), separately measure temporal and spatial plaquettes, area-normalized contractible Wilson loops, and gauge-invariant temporal correlators used to extract excitation gaps. Use several approximant sizes and phason offsets, matched square controls and controlled sampling/autocorrelations. Only an effect that persists under these controls and continuum/thermodynamic scaling would support a genuine geometry-caused dynamical effect.

**Interpretation safeguard:** the previous correction to numerical excitation gaps is retained as a distinct reported correction. Neither the exact 2D partition-function identity nor its plaquette Monte Carlo test validates or invalidates those gaps without knowing their operator, geometry and time evolution.

## Reproduction and provenance

Run `pytest -q test_penrose_causal.py`: **6 passed** on the code supplied here. JSON outputs contain full geometry audits, period vectors, degree histograms, Monte Carlo seed settings and the two beta=4 runs, and the primitive-period benchmark. No previous ZIP code was used, and the six tests reported in the earlier conversation were not replayed.
