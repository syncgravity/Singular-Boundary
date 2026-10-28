# R3-IR — verified published LPPL application and Penrose boundary theorem (2026-10-28)

**Status:** an independently checked **deduction from a primary, published local-stability theorem**; not an independent re-proof of that paper, not a volume-uniform spectral-gap theorem, not a continuum claim. No original source modified or Monte Carlo performed.

## Primary literature audit and unresolved spectral dependency

**Primary theorem directly consulted:** J. Henheik, S. Teufel, T. Wessel, *Local stability of ground states in locally gapped and weakly interacting quantum spin systems*, Lett. Math. Phys. 112, 9 (2022), DOI [10.1007/s11005-021-01494-y](https://link.springer.com/article/10.1007/s11005-021-01494-y). Its Definition 1 and Theorem 3 allow **arbitrary finite subsets** of Z^ν, **possibly infinite-dimensional** local Hilbert spaces, **possibly unbounded** positive on-site operators with unique ground and common gap, and bounded site-dependent finite-range interactions. Theorem 3 is exponential local perturbation stability (LPPL) for arbitrary relatively bounded perturbations with relative bound <1, including all **bounded** local perturbations. It does *not* itself state a spectral gap for the perturbed system.

**Separate spectral theorem not independently audited:** D. A. Yarotsky, *Perturbations of ground states in weakly interacting quantum spin systems*, J. Math. Phys. 45, 2134–2152 (2004), DOI 10.1063/1.1705718. The 2022 authors attribute a volume-uniform weak-interaction gap to this article, but explicitly flag differences in treatment of boundary interactions (their Footnote 1). The 2004 full primary article could not be accessed in this audit. In particular, the 2022 bulk-uniqueness theorem (their Theorem 7 quoting a **different** 2005 Yarotsky paper) must *not* be mistaken for the 2004 finite-volume gap theorem. Therefore the **uniform weak-magnetic Penrose spectral gap remains source-supported pending complete primary review**.

## Exact canonical five-dimensional embedding

For a finite canonical Penrose rhombus complex G, vertices have integer labels z∈Z⁵ and each edge joins z to z+e_i. The map
`iota({z,z+e_i})=2z+e_i`
is injective by parity. Every four-edge rhombus has all four link sites pairwise ℓ¹-distance **exactly 2**. Thus `Λ_G=iota(E(G))` is an arbitrary finite subset of Z⁵ and every Wilson face is range-two.

On the **full** link Hilbert space `⊗_{e∈E(G)}L²(SU(2))`, let
`H_G=Σ_e a_e(-Δ_e)+Σ_f b_f(1−p_f)` with `a_e≥a_*>0`, `0≤b_f≤b_*`, `p_f=ReTr W_f/2`.
Every electric site has unique constant vacuum and gap at least `g=3a_*/4` (first nontrivial SU(2) Casimir 3/4). Assign each face f to one of its four link sites x(f). Since an edge belongs to at most two rhombi, the anchored interaction `Φ_x=Σ_{f:x(f)=x} b_f(1−p_f)` is self-adjoint, supported in `B₂(x)`, and `||Φ_x||≤4b_*`. The normalized interaction has `sup_x||Φ_x/g|| ≤ η := (16/3)b_*/a_*`.

## Theorem LPPL-P (deduction from 2022 Theorem 3; fixed weak coupling)

Choose published constants `c_{5,2},c₁,c₂>0` for ν=5, R=2 and normalized on-site gap ≥1. Assume `η≤c_{5,2}`. For any nonempty index-site set X, any bounded self-adjoint P supported on X, any ground state `ρ_P` of `H_G+P`, and bounded local A supported on Y,
```
|Tr(ρ_P A) − <Ω_G,AΩ_G>| ≤ exp(c₁|Y|) ||A|| exp[−c₂ d₁(Y,X)] .   (LPPL-P)
```
**Proof:** normalizing H and P by g preserves ground states and verifies every condition of the published Definition 1 and Theorem 3, including boundedness of P (relative bound zero). The unperturbed finite full-link ground Ω_G is unique and gauge-invariant by elliptic positivity and symmetry on the compact connected SU(2) configuration space. Apply the published theorem. No interacting gap is assumed as an extra model-specific input.

## Theorem B1 (boundary deletion and interior observable comparison)

Let F⊂G be nested **edge-induced, face-complete** finite subcomplexes with identical coefficients on their shared links and faces. Define crossing plaquettes C as faces of G with some edge in F and some edge outside F, and let X be the union of their index-link support. The finite-rank *in spatial support*, bounded perturbation `P=−Σ_{f∈C}b_f(1−p_f)` removes exactly the crossing magnetic terms and obeys the published theorem regardless of its potentially extensive total norm.

The resulting **full-link** Hamiltonian factorizes exactly:
`H_G+P=H_F⊗I+I⊗H_out`
where H_out contains the exterior electric and wholly exterior magnetic terms. Both factor ground states are unique, so for any observable A supported on Y⊂iota(E(F)),
```
|<Ω_G,AΩ_G>−<Ω_F,AΩ_F>| ≤ exp(c₁|Y|)||A|| exp[−c₂ d₁(Y,X)].   (B1)
```
If no crossing faces, the difference vanishes exactly. The physical gauge-invariant comparison uses the **gauge-invariant full-link ground vectors** and local Wilson observables; it does *not* assume that the gauge-projected Hilbert space factorizes.

**Physical spatial bound:** for the standard cut/project edge length a and unit edge directions u_i, the physical midpoint is `r(x)=(a/2)Σ_i x_i u_i`. Thus `|r(x)−r(y)|≤(a/2)d₁(x,y)`. If the physical midpoint separation between Y and X is r, the B1 upper bound is at most `exp(c₁|Y|)||A|| exp(−2c₂r/a)`. This is **spatial** ground-state boundary insensitivity; its exponent is not an excitation mass or temporal connected decay.

## Theorem B3 (local thermodynamic expectations, same fixed scale)

For a nested exhaustion `G_n` of one infinite canonical Penrose link complex with induced faces and compatible fixed coefficients satisfying the same smallness bound, each bounded fixed-local A has a Cauchy sequence `ω_{G_n}(A)=<Ω_{G_n},AΩ_{G_n}>`.

**Proof:** apply B1 to n<m. The crossing index support is at most distance 2 from an outside link; hence
`d₁(Y,X_{n,m})≥ d₁(Y,Λ_∞\Λ_n)−2`.
The RHS diverges under an exhaustive increasing sequence of finite site sets for fixed Y. The B1 estimate is uniform in m>n. The consistent positive normalized local limits define a state on the quasi-local link observable algebra, independent of compatible finite exhaustions by a common-refinement argument. Gauge invariance of fixed-local observables persists. **This does not alone establish the unbounded infinite-volume dynamical generator, quantum spatial continuum or a positive mass gap.**

## Exact deterministic fixture

Historical canonical seed: `HISTORICAL_Q14_CANONICAL.json/seed_faces_z5` (three rhombi, ten distinct edge sites). The new read-only verifier exhaustively checks `d₁(Y,X_cross)≥d₁(Y,outside)−2` over **5,120** subset/site cases (5,110 with crossing), with no failures and maximal loss exactly 2. These are finite combinatorial tests, not numerical spectral evidence or re-execution of the original generator.

The complete source-grounded note, original-free executable fixture, output and SHA-256 derived manifest are in the local artifact `singular_boundary_penrose_boundary_locality_2026-10-28.zip`, SHA-256 `6995d67ec99f60d0699f2e056a289ac1a109659b3101878a6eae47dc28260c6b`.

## Evidence status and critical path

- Z⁵ midpoint embedding / local perturbation hypotheses: **independently proved**.
- LPPL-P, B1 and B3: **mathematical deductions verified against the full accessible primary 2022 theorem statement**, whose published proof has not been independently reproduced. They are not gap estimates.
- 2004 weak-interaction spectral-gap transfer: **source-proved, pending direct primary theorem review**; do not promote from a citation/footnote.
- Fixed-scale weakly interacting, volume-uniform Penrose spectral gap: **conditional pending primary theorem audit**.
- Regulator-uniform source-inserted temporal decay and physical quantum continuum: **open**.
