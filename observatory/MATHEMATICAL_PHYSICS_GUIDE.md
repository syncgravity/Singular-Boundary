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

## A local vacuum estimate without assuming a mass gap

The actual finite cubic SU(2) Wilson ground state Ω satisfies **α⟨Cₑ⟩≤βdₑ≤4β** for any one elementary link e, because its incident plaquette potential can be removed and Haar-averaged in an exact variational trial state. Conditioning Ω² on the *ordered group holonomy of any simple physical loop* yields the local **SU2 Fisher bound** ∫|∇√ρ|²≤16/g₀⁴, independent of spatial volume and the contour's elementary link count. SU2 Sobolev and its known Haar trace distribution then prohibit the finite-coupling loop trace from becoming a delta-mass, and the marginal has convergent subsequences as the box grows **at fixed mesh and g₀**. The local spectral first moments are bounded in the spatial-volume limit, not in the ultraviolet h→0 limit.

This is **not** a uniform pointwise Harnack and does not bound the full interacting Schur complement or exclude a soft infrared spectrum. The coefficient g₀⁻⁴ grows along asymptotic freedom; establishing physical-time and renormalized-marginal control on that trajectory remains an open mathematical problem. The finite theorem is documented in [the exact link-excision and thermodynamic proof](../research/theorems/R3_LOCAL_INTERACTING_SU2_FISHER_AND_THERMODYNAMIC_SUBSEQUENCE_2026-11-06.md).

## Do not conflate Fisher bounds, holonomy noise and flowed gauge fields

A true interacting cubic SU(2) vacuum may have a local Wilson-loop marginal with bounded Fisher information. **Even if this becomes UV-uniform, it is not a mass-gap estimate.** The smooth positive SU(2) class density ρ_ε=(x²+ε²)/(1/4+ε²), x=tr(U)/2, has uniformly bounded sqrt-density H¹ and nonzero Wilson variance but admits a smooth positive class-rotor Hamiltonian with spectral gap ≤ε→0. This **is not** the actual cubic Wilson magnetic action; it is a controlled counterexample to the *logic* of inferring low energies from static regularity alone.

Group heat smoothing of the single *fundamental* loop trace only rescales its character and cancels under variance normalization. Externally adding independent readout noise may produce an attractive smoothed distribution, but it is not a renormalized quantum field. A more relevant **finite candidate** is the gauge-equivariant spatial Wilson-action flow of all link fields; it has an exact volume-uniform Hessian bound and factorial lattice-distance locality at fixed flow time. The currently available estimate grows exponentially for the lattice flow time needed for fixed physical radius, so its **continuum** status remains OPEN.

For any finite family of gauge-invariant flowed Wilson observables, the first true physical-time spectral moment is the exact interacting covariance–Dirichlet matrix ratio α(aᵀG a)/(aᵀS a). Its scale-uniform control would give high-energy tightness **only**. The full renormalized interacting Schur/long-time correlations, nontrivial four-dimensional OS reconstruction, source-certified Penrose transfer and physical quantum-gravity operator still require separate proofs. See the [finite mathematical audit](../research/theorems/R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md).

## The positive result at fixed physical flow radius—and what it does not establish

The cubic **flat-field linearization** of the finite spatial SU(2) Wilson gradient flow is the positive heat equation for discrete oriented curvature (F_h): at fixed (	au=h²s>0), (F_h(	au)=e^{-	au d_1d_1^*/(4h²)}F_h(0)). Its curvature and physical derivatives have **uniform mesh-independent (L²) bounds**, and fixed transverse periodic Fourier modes have **O(h²)** convergence. This is a real control on the physical-radius scaling and is invariant under **linearized** gauge transformations. It does not control the **nonlinear** gauge field or the interacting quantum vacuum.

There is a decisive nonlinear warning: on an isolated four-link SU(2) plaquette with *Haar/free-electric reference*, exact Wilson gradient flow moves its normalized trace into rarer and sharper configurations. The trace variance falls to zero, the variance-normalized first electric spectral moment diverges, and every fixed-positive-electric-time normalized connected correlation tends to zero. This does **not** show that 4D flowed Yang–Mills fields fail; the reference uses a shrinking elementary plaquette, a free vacuum and a different order of limits. It does show why merely normalizing a heavily flowed observable is not sufficient.

**Open P2–P5 bridge:** prove a **nonlinear** positive-physical-flow-radius estimate in a physically appropriate full 4D regulator, show the **actual interacting** renormalized gauge-invariant Wilson field has nontrivial covariance, and control its **complete** energy-dependent Schur form and long-time connected correlations through weak-bare-coupling refinement. The quasicrystalline gauge geometry and gravitational UV operator are separate open interfaces. [Technical source](../research/theorems/R3_FIXED_PHYSICAL_RADIUS_LINEARIZED_CUBIC_FLOW_2026-11-05.md).

## The first nonlinear physical-radius estimate: exactly what it controls

For the full finite 3D original-link SU(2) **classical spatial** Wilson gradient flow, with `E_h=8S_h/h` and physical flow time `tau=h²s`, the exact nonlinear energy identity bounds `E_h(tau)` and the **time integral** of the physically normalized squared gradient by the initial `E_h(0)`. If that total *classical* initial action is uniform in lattice spacing, every plaquette holonomy is close to the identity at least at rate `sqrt h`, and the curvature-energy measures have weak subsequences on a fixed physical box. This goes beyond the earlier linearized heat theorem but is **weaker than a pointwise derivative-smoothing or quantum continuum theorem**.

A simple genuine SU(2) cubical configuration with a single link angle `sqrt h` has bounded physical energy tending to 4 but an initial **atomic curvature-energy limit** and physical plaquette curvature blowing up as `h^-3/2`. This explicitly prevents importing diffuse regularity from an energy bound alone. It does **not** refute positive-flow-time smoothing, because the concentration counterexample is at initial flow time.

Finite interacting ground-state positivity and invertibility of the finite spatial flow guarantee that nonconstant flowed Wilson traces have positive variance at each fixed regulator, but no **uniformly nonzero physical field** or complete interacting time/Schur estimate follows. A classical energy expectation bound under the quantum vacuum is another **unproved input**, and raw gauge-action energy may need UV renormalization. All P0–P5, 3D quasicrystalline transfer, and gravitational ultraviolet gates remain OPEN. [Full mathematical proof](../research/theorems/R3_NONLINEAR_CUBIC_PHYSICAL_ENERGY_DISSIPATION_2026-11-06.md).

## Why one nonlinear positive-physical-time estimate is possible—and why it is not yet Yang–Mills

The full finite 3D original-link SU(2) **classical** Wilson spatial flow contains a rigidly constrained, *exactly invariant* subset: all x/y links lie in one commuting Cartan U(1), are identical across z, and every vertical link is identity. Its 2D lifted plaquette flux obeys the **nonlinear sine-diffusion equation**, not a linearization. Under the explicit non-winding admissibility and uniformly bounded **three-dimensional classical initial action**, it becomes a uniformly elliptic time-dependent scalar graph heat equation. A discrete Nash proof gives a **mesh-independent positive-physical-time L∞ curvature bound**. The nonlinear solution also differs from the corresponding flat Maxwell heat curvature by **O(h²) in physical L², uniformly for all flow times**, including initially concentrated but bounded-action original-link configurations.

That is real positive-time **nonlinear classical curvature regularity**, but *only for this strict Abelian planar subspace*. This fixed subgroup has **Haar measure zero** in the full SU(2) link manifold. Therefore, the full **interacting quantum Wilson vacuum** gives it zero probability: one cannot average the estimate over that vacuum and infer non-Abelian or four-dimensional QFT regularity. The missing theorem needs noncommutative covariant curvature estimates valid on positive-probability interacting configurations and genuine gauge-invariant renormalized covariance/complete physical-time Schur bounds. The UV quantum-gravity fluctuation operator and Penrose spatial model remain distinct open questions. See [the exact source proof](../research/theorems/R3_EMBEDDED_CARTAN_NONLINEAR_POSITIVE_RADIUS_SMOOTHING_2026-11-06.md).
