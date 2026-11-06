# Proof Atlas — a mathematical-physics reading guide

**All continuum mass-gap and quantum-gravity claims remain OPEN.** This guide is written to make the questions navigable without relying on the original source documents' chronology.

## Read the graph as a typed mathematical argument

- **Model**: a specified space, lattice, gauge group, degrees of freedom and boundary convention. Penrose (2D) and cubic (3D) are different mathematical objects.
- **Result**: a statement actually established within explicit quantifiers. A proof on every *finite* cubic lattice is not a statement uniform in infinite volume or lattice refinement.
- **Interface**: a theorem that would be necessary to move a conclusion between mathematical settings, such as a normalized observable dictionary or a reflection-positive continuum limit. Its node stays OPEN until independently proved.
- **Obstruction**: a concrete failed inference for a specified argument or parameter range. A blocked *proof technique* is not necessarily a counterexample to a physical theorem.
- **Evidence**: source-pinned code, a finite numerical output, a PDF or a SHA-256-identified dataset. A file's presence or correct hash is not a mathematical proof.
- **Review state**: annotations are proposals, never formal certification.

## The six Yang–Mills gates

**P0 (regulator).** Define a genuinely three-dimensional spatial cell family, a refinement to vanishing mesh size, and the physical action and time conventions. Cubic geometry is known; the intended nonperiodic 3D model remains unconstructed at this standard.

**P1 (physical operator).** Define SU(2) holonomies on links, the Gauss-law physical Hilbert space, positive electric and magnetic terms, self-adjoint operators and the physical time transfer—**on the same model**.

**P2 (interaction).** Show that the interacting dynamics and renormalized observables have uniform control in spatial volume and lattice spacing along the actual bare-coupling trajectory. Exact one-dimensional strip estimates have not been transferred into the 3D theory.

**P3 (candidate quasicrystal mechanism).** Analyze source-specific Wilson-current, curvature and geometry estimates that might give a quasicrystalline infrared mechanism. Not required by every possible cubic YM proof route.

**P4 (infrared).** Exclude positive-energy spectral weight in an interval `(0,M)` with `M>0` measured in physical units. Nonzero spectral moments or positive finite-lattice gaps do not exclude arbitrarily soft continuum excitations.

**P5 (continuum existence).** Construct a nontrivial four-dimensional quantum theory from reflection-positive Euclidean Schwinger functions and recover a physical Hilbert space/vacuum. Only then can a common decay estimate imply the desired continuum mass gap.

## The six cubic-to-quasicrystal checks

**T0:** genuine quasicrystalline 3D spatial refinement. **T1:** same-action Gauss-invariant quantum dynamics. **T2:** normalized renormalized gauge-invariant observables. **T3:** large-physical-time interacting correlation comparison uniform in mesh and volume. **T4:** nontrivial continuum Osterwalder–Schrader reconstruction. **T5:** spectral-support implication using dense physical observables. None is fully proved.

The control geometry can be used to validate estimates while the source geometry is developed. It cannot be silently substituted for that source geometry. Equal area, matching seed labels, and finite numerical agreement do not prove universality or equal continuum physics.

## Why the cubic finite gap is not the continuum gap

For `n^3` cubic cells, the known finite Gauss-invariant sufficient estimate is

`Delta_n >= [3g0^2/2 - 2F_n/g0^2]/h` where `F_n=3n^2(n+1)` and `h=1/n`.

Its positivity certificate requires `g0^4>4F_n/3`, which forces `g0` to grow under refinement. Asymptotic freedom instead requires weak bare coupling `g0->0` along the ultraviolet limit. The certificate therefore does not prove the required physical gap. This does not prove that the true gap vanishes.

## Why small numerical error does not transfer a gap

For a positive spectral measure, `C(t)=int exp(-Et) dmu(E)`. Compare `C_c(t)=exp(-Mt)` to `C_q(t)=(1-eta)exp(-Mt)+eta exp(-mt)` with `0<m<M`. These are arbitrarily close in the ordinary supremum norm when `eta` is small, yet the latter has spectral support at `m`. An infrared gap requires an independent spectral exclusion estimate or adequately strong exponential-time comparison.

## The distinct quantum-gravity problem

A quasicrystal graph Laplacian has a spectral measure, an associated heat-kernel trace (when well-defined), and possibly zeta-regularized quantities. The *physical gravitational fluctuation operator* and the integration measure of an interacting quantum-gravity theory are different objects until explicitly identified. Penrose-versus-square scalar SU(2) Monte Carlo and graph spectral-zeta comparisons are also different experiments. The proposed UV mechanism must be tested on the physically justified operator; a Yang–Mills mass-gap theorem would not prove quantum-gravity finiteness by itself.

## Source and review policy

Each research claim links to source-pinned theorem/audit documents. All 26 archived original files remain in Library with exact SHA-256 identities. The atlas presents mathematical topics as nodes; original source file names and titles remain available under provenance, rather than used as explanatory node headings. No source records were deleted; the v2.29 source merge is complete and no public deployment is authorized by that merge.

## True interacting vacuum versus bare Haar blocking

At each finite 3D cubic SU(2) Wilson regulator, the smooth strictly positive ground state Ω defines the physical vacuum probability measure Ω² dHaar. Conditional expectation to a **fixed physical Wilson loop** gives a canonical isometric local observable map; the normalized centered Wilson observable is mathematically defined, even though Ω and its scale behavior remain unknown. The projected coarse generator depends on its marginal density ρ and the full time dynamics include an eliminated-sector score-variance memory term. A variational Schur form compares the **complete** energy-dependent influence without assuming an unbounded offdiagonal block is bounded. A finite gauge-graph counterexample proves that even exact agreement of static marginal probabilities and the projected generator need not give agreement of time-dependent correlations. **The remaining P2/P4 theorem is a scale/volume-uniform physical-time comparison of the actual interacting vacuum and full influence**, not a comparison of bare Haar coefficients alone.

## What does a true-vacuum marginal bound prove?

At every **finite** original-link cubic SU(2) Wilson regulator, the unique smooth positive ground state Ω makes every selected physical Wilson-loop marginal ρ smooth and positive. The global SU(2) heat-kernel/Harnack certificate gives **exp(−2Λ)≤ρ≤exp(2Λ)**, Λ=64F/g₀⁴+E log(101/99). It is mathematically genuine but extremely weak under refinement: F and E grow with the entire lattice. An actual *local, volume-independent* interacting-vacuum estimate remains unknown.

A physical loop does **not** retain a fixed number of elementary links when the lattice is refined. Its centered normalized first spectral moment is α L times a positive quotient of the marginal's expectation and variance; L doubles across dyadic refinement. Thus if adjacent true-vacuum loop densities were uniformly close, the unsmeared short-time moment would still scale approximately by **four** when the bare coupling runs slowly. A physically meaningful comparison must confront observable renormalization and physical time, not simply match the static marginal.

This is an ultraviolet first-moment effect, not a physical infrared mass-gap obstruction. An explicit positive spectral family has a fixed gap while its first moment diverges. Finally, simple ground-state source-response bounds divide by the interacting finite gap; using those same bounds to establish the gap without independent input would be circular. See the [finite source and proof](../research/theorems/R3_FINITE_WILSON_MARGINAL_HARNACK_AND_TWO_SCALE_SUM_RULE_2026-11-06.md).
