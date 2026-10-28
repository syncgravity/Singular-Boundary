# R3-IR — exact ℤ5 locality reduction and qualified weak-magnetic gap corollary

**Date:** 2026-10-28. **Status:** Penrose-to-ℤ5 representation independently proved; published fixed-scale spectral corollary **source-proved pending direct primary-theorem audit**. Not a continuum mass-gap theorem. Original historical sources unmodified. No Monte Carlo.

## Research correction: two distinct Yarotsky theorems

The earlier report correctly found that Yarotsky (2006), *Ground states in relatively bounded quantum perturbations of classical lattice systems*, CMP 261, requires a translation-invariant ℤ^ν model in its stated theorem. This does **not** rule out applying Yarotsky (2004), *Perturbations of ground states in weakly interacting quantum spin systems*, J. Math. Phys. 45, 2134–2152, DOI [10.1063/1.1705718](https://doi.org/10.1063/1.1705718).

Henheik, Teufel and Wessel (2022), [*Local stability of ground states in locally gapped and weakly interacting quantum spin systems*](https://link.springer.com/article/10.1007/s11005-021-01494-y), §2 Definition 1, specify arbitrary finite subsets of ℤ^ν, potentially **infinite-dimensional** site Hilbert spaces, **unbounded** positive on-site operators with common gap, and bounded finite-range **site-dependent** perturbations. Their introduction expressly credits Yarotsky (2004) with a unique volume-uniformly gapped ground state for sufficiently weak perturbations; their footnote 1 addresses a difference in boundary conventions. They do NOT reprove the 2004 spectral-gap theorem in this paper. The complete Yarotsky (2004) primary article has not yet been reviewed here: its precise all-volume, nonstationary, free-boundary gap hypotheses must be checked before the corollary is called independently proved.

## Theorem Z5-1 — exact integer-lattice embedding (independently proved)

For a finite standard direct-ℤ5 Penrose rhombus patch, take vertex labels `z∈ℤ5`, all links `{z,z+e_i}` in positive basis directions. Map each undirected link to an auxiliary lattice site

`iota({z,z+e_i})=2z+e_i ∈ ℤ5.`

The map is injective: the unique odd parity coordinate identifies `i`, then `z=(iota-e_i)/2`. A face with vertices `z,z+e_i,z+e_j,z+e_i+e_j` has four edge sites
`2z+e_i, 2z+e_j, 2z+e_i+2e_j, 2z+e_j+2e_i`.
Every pair has ℓ1-distance **exactly two**. Every plaquette therefore lies in a radius-two ball around any one of its edge sites. This ℤ5 is an auxiliary *index lattice*, not an assertion of five physical spatial dimensions.

**Finite fixture check:** the three seed rhombi transcribed from the original `HISTORICAL_Q14_CANONICAL.json` have 10 distinct link sites, maximal incidence two, no collisions, and all six intra-rhombus site distances exactly two. The general proof is algebraic and does not depend on this fixture.

## Theorem Z5-2 — direct on-site SU(2) reduction (independently proved)

On the full link Hilbert space `⊗_{e∈E}L²(SU(2))`, let

`H_G = Σ_e a_e(-Δ_e) + Σ_f b_f(1-p_f)`, `a_e≥a_*>0`, `0≤b_f≤b_*`,
with `p_f=ReTr W_f/2 ∈[-1,1]`; every edge of the spatial Penrose patch belongs to at most two faces.

Define `Λ_G=iota(E(G))⊂ℤ5`, `ℓ_x=a_e(-Δ_e)` for `x=iota(e)`. With SU(2) Laplacian convention `-Δ χ_j=j(j+1)χ_j`, each `ℓ_x` has unique product-constant vacuum and gap `g=3a_*/4`.

Choose one incident edge `x(f)` as an anchor for each face and set `Φ_x=Σ_{f:x(f)=x}b_f(1-p_f)`. Since an edge is incident to at most two faces, each anchor receives at most two terms. Each Φ_x is supported in `B_2(x)`, and `||1-p_f||≤2`. Thus exactly

```
H_G = Σ_{x∈Λ_G} ℓ_x + Σ_{x∈Λ_G}Φ_x,
gap(ℓ_x) ≥ 3a_*/4,    supp(Φ_x)⊆B_2(x),
sup_x ||Φ_x||≤4b_*,       sup_x ||Φ_x/g||≤(16/3)b_*/a_*.
```

These are literal **Definition 1** conditions in the 2022 paper, with lattice dimension ν=5, range R=2 and normalized site gap ≥1. Crucially, the **2004 on-site/finite-range** class does **not** require the separate 2006 same-support local `h_f` decomposition. The earlier face splitting remains valid but is not needed here.

## Corollary Z5-3 — finite-scale interacting gap (source-proved, pending original theorem audit)

**Assumption to authenticate against Yarotsky (2004):** its finite-volume gap theorem applies uniformly to arbitrary inhomogeneous ℤ5 finite subsets (or to boxes with arbitrary inhomogeneous perturbations) with single-site gap ≥1 and range R=2. Let `c_{5,2}>0` and `γ_{5,2}>0` denote the resulting smallness threshold and normalized gap.

For `b_*/a_*<(3/16)c_{5,2}`, Theorem Z5-2 gives, uniformly in Penrose patch size,

`H_G-E_0(G) ≥ (3a_*/4)γ_{5,2}(I-|Ω_G><Ω_G|).`

The ground state on the full link space is unique and strictly positive (finite elliptic compact setting), hence invariant under SU(2) vertex gauge transformations, and the same full-space bound restricts to `ℓ_phys`. This is a genuine **nonzero magnetic**, **fixed spatial-scale**, **volume-uniform** gap implication, **conditional on the exact 2004 theorem scope**.

**Free-boundary reduction:** if the published statement is for a containing box, add independent exterior rotor sites with no crossing interactions. Then `H_box=H_G⊗I+I⊗H_ext` and `gap(H_box)=min(gap(H_G),gap(H_ext))`; a box gap implies the G gap. This trick requires **site-dependent** interactions to be admitted and cannot circumvent a translation-invariance assumption.

**Continuum restriction:** physical Penrose spatial refinement has `b_f/a_e ≍(g_3² a)^{-2}`, generally leaving the smallness regime. The 2+1D fixed-scale result does not establish R2 quantum reconstruction or four-dimensional Yang–Mills.

## Verification and provenance

Original Library fixture: `HISTORICAL_Q14_CANONICAL.json`, `seed_faces_z5`. Exact local checked script `verify_z5_reduction.py` and `Z5_CERTIFICATE.json` in the audit handoff; zero simulations. Local handoff SHA-256: `singular_boundary_z5_locality_gap_reduction_2026-10-28.zip` = `7fc8b0b374610ae677df9d24973f09de8a41e3663fdd51b4cf984fe26f80f8e7`.

**Immediate next primary-source obligation:** retrieve complete Yarotsky 2004 J. Math. Phys. 45, 2134–2152, DOI 10.1063/1.1705718, and verify the precise non-translation-invariant finite-volume gap statement, unbounded local domains and free boundary conventions. Preserve this as an explicit literature dependency until completed.
