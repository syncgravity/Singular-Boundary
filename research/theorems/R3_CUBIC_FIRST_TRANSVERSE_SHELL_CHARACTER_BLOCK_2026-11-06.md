# P0–T2: a complete first 3D transverse shell under SU(2) spatial plaquette blocking

**Research date:** November 6, 2026. **Status:** a source-scoped finite three-dimensional exact strong-coupling/character-contraction result, with independent cubical incidence tests. **Not** a weak-bare-coupling construction, an interacting physical-time correlation bound, a new universal renormalization-group theorem, a continuum Yang–Mills mass gap, a Penrose transfer theorem, or a quantum-gravity ultraviolet result. Independent mathematical review is required before any theorem-ledger acceptance.

## 1. Source context and the specifically completed target

PR #63 established two distinct finite facts about original-link SU(2) on a dyadic cubic regulator: (i) kinematic Haar compression of each individual refined Wilson plaquette vanishes on coarse cylinders, although coarse electric Casimirs survive with modified coefficient; (ii) a complete four-face planar product has conditional expectation `chi_1(U_boundary)/8`, and the isolated planar **exponential** weight has the exact two-dimensional character-convolution formula `sum_n a_n(t)^4 chi_n(U)/(n+1)^3`.

The genuine three-dimensional obstruction to equating that planar formula to an interacting cubical effective action is that every planar edge can belong to transverse plaquettes. This audit completes the **smallest full cubical slab** around the four-face block, with all its 3D transverse plaquettes, and determines the first resulting magnetic boundary channels **for a deliberately specified positive, truncated character weight**. This is an authentic 3D finite magnetic-interaction calculation, but **is not the physical-time Kogut–Susskind heat-kernel transfer or the Wilson exponential weight**. That model distinction is essential.

The exact geometry is the open `2×2×1` cubical slab with x,y∈{0,1,2} and z∈{0,1}, four 3-cells, 18 vertices, 33 oriented edges and 20 square faces: four bottom xy plaquettes, four top xy plaquettes and twelve transverse xz/yz plaquettes. Hold fixed the **eight** bottom perimeter link variables, with ordered total holonomy `U=U_{∂P}`; integrate every other **25** independent original link against normalized SU(2) Haar.

Let `chi_1(V)=tr_fund(V)` be the unnormalized real fundamental character, `chi_0=1`, and `chi_2` the spin-one/adjoint (three-dimensional) character, so `chi_1(V)^2=chi_0(V)+chi_2(V)`. For `|lambda|<1/2`, use the positive *finite spatial plaquette* weight

```
w_lambda(V) = 1 + lambda chi_1(V),
Z_slab(U;lambda) = integral_{25 links} product_{20 faces} w_lambda(U_face) dHaar,
A0(lambda) = integral_SU2 Z_slab(U;lambda) dHaar(U),
Zhat_slab = Z_slab/A0(lambda).
```

Gauge invariance at the retained boundary vertices implies that `Z_slab` is a central function of the loop holonomy `U`, not of a chosen parametrization of its eight links. The **isolated four-face planar kernel with precisely the same truncated face weight** is exactly

```
Z_planar(U;lambda) = 1 + (lambda^4/8) chi_1(U).
```

Do not substitute the earlier planar **exponential** `exp(t chi_1)` kernel into this polynomial-weight comparison. Their higher-order coefficients are different.

## 2. Exact 3D-shell theorem and a finite, explicit remainder bound

**Proposition (complete first 3D transverse shell).** Define

```
P0(lambda) = 1 + lambda^6/4 + lambda^10/64,
P1(lambda) = lambda^4/8 + lambda^8/32 + lambda^10/128,
R12(lambda) = 9 (2|lambda|)^12 + 4 (2|lambda|)^14 + (2|lambda|)^16.
```

For the stated `2×2×1` slab, all `U ∈ SU(2)` and `|lambda|<1/2`, the following **operator-valued/character-valued equality and uniform estimate** hold:

```
Z_slab(U;lambda) = P0(lambda) + P1(lambda) chi_1(U) + E12(U;lambda),
sup_U |E12(U;lambda)| <= R12(lambda).
```

Moreover, **the complete unnormalized spin-one/adjoint character coefficient** is exactly

\[
\boxed{[\chi_2] Z_{\rm slab}(\cdot;\lambda)=\frac{\lambda^{16}}{16384}.}
\]

Since every face factor obeys `w_lambda ≥ 1−2|lambda|`, the normalized vacuum coefficient satisfies

\[
 A_0(\lambda)\ge(1-2|\lambda|)^{20}>0.
\]

The corresponding **quantitative normalized comparison** is

\[
\boxed{
\left\|\widehat Z_{\rm slab}(\cdot;\lambda)
 -\left(1+\frac{P_1(\lambda)}{P_0(\lambda)}\chi_1\right)\right\|_\infty
\le \frac{2R_{12}(\lambda)\left(1+|P_1(\lambda)|/P_0(\lambda)\right)}{(1-2|\lambda|)^{20}}.}
\]

In particular, for small real `lambda`, the **finite magnetic shell** modifies the planar Wilson channel in the normalized kernel as

\[
\boxed{
\widehat Z_{\rm slab}(U;\lambda)-Z_{\rm planar}(U;\lambda)
=\left(\frac{\lambda^8}{32}-\frac{3\lambda^{10}}{128}\right)\chi_1(U)
+O(\lambda^{12}),}
\]

uniformly in `U`. The first transverse correction is **`+lambda^8/32`**, and the genuinely new spin-one channel appears at **order 16** for this *squarefree truncated face weight*. The normalization accounts for closed vacuum cube surfaces and changes the order-ten coefficient. These are **finite-block strong-coupling coefficients**, not a physical running coupling, continuum beta function, or gap estimate.

## 3. Proof by relative cubical incidence and SU(2) representation contraction

### (a) Enumerate precisely the admissible squarefree face sets

Expand the **polynomial** product `∏(1+lambda chi_1(U_f))` over all `2^20` subsets `S` of the 20 faces, each selected face contributing exactly one fundamental character. For every integrated link `e`, the Haar center transformation `U_e→−U_e` annihilates any monomial for which an odd number of selected faces meets `e`. Thus any surviving set must be a mod-two 2-chain whose boundary is supported only on the retained eight-edge bottom loop.

The slab is contractible and consists of four 3-cells. Its four cubical 3-boundaries generate the space of closed mod-two 2-cycles; the **bottom four-face disk** represents the additional relative 2-chain with boundary equal to the retained loop. There are therefore exactly `2^5=32` parity-admissible face subsets: 16 vacuum-boundary sets and 16 loop-boundary sets. Their areas are completely fixed by the four cube-boundary symmetric differences:

| Sector | Numbers of admissible face subsets by area |
|---|---|
| No mod-two bottom boundary | `0:1, 6:4, 10:4, 12:2, 14:4, 16:1` |
| Entire bottom loop boundary | `4:1, 8:4, 10:4, 12:7` |

A second executable audit independently enumerates **every one of the `1,048,576` face subsets**, using the full 25-link incidence matrix and no assumption about the topological generator basis, and finds the identical 32 solutions. Parity is **necessary**, not sufficient, at arbitrary order: four-valent nonabelian intertwiners are not replaced by independent surface factors. We use explicit Schur contractions **only** where the surviving surfaces are embedded disks or spheres.

### (b) Evaluate the low-area embedded surfaces exactly

Each of the area-four, area-eight and area-ten loop-sector representatives is an orientable embedded disk spanning the same eight bottom boundary edges, with each integrated edge on the disk incident to exactly two selected faces. SU(2) defining-representation Schur orthogonality at each such link contributes `1/2`, and interior matrix-index loops contribute `2`. Euler's disk identity yields the exact amplitude

\[
 \int \prod_{f\subset S}\chi_1(U_f)\,dU_{\mathrm{int}}
 =2^{1-|S|}\chi_1(U),\qquad S\text{ an embedded disk}. 
\]

There is **one** four-face bottom disk, **four** eight-face disks obtained by replacing exactly one bottom face with the other five faces of the cube above it (a single transverse bulge), and **four** ten-face disks formed by two adjacent transverse bulges. Their combined loop-channel coefficients are respectively

```
area 4:  1 × 2^(1−4)  = 1/8,
area 8:  4 × 2^(1−8)  = 1/32,
area 10: 4 × 2^(1−10) = 1/128.
```

Similarly, four single-cube closed surfaces of six faces and four adjacent two-cube closed spheres of ten faces give scalar coefficients `4×2^(2−6)=1/4` and `4×2^(2−10)=1/64`. The retained bottom boundary links that appear in a proper closed-cube surface form a forest; their holonomies can be gauged away, so the closed-surface coefficient is scalar. This establishes `P0` and `P1`. **No** face subset of area below 12 remains unaccounted for.

### (c) The first new higher-spin character is exactly identified

Each bottom boundary edge occurs in **at most two** faces of the selected face product: one bottom face and one outer vertical face. An effective spin-one character requires two fundamental factors along **every** boundary edge (since `1/2⊗1/2=0⊕1`); if any boundary edge is absent, gauge invariance forces the contribution to be constant, and if each has only one fundamental factor the nontrivial boundary sector is spin one-half.

The only parity-admissible selected set having **two** factors on every one of the eight retained edges is the entire **sixteen-face outer boundary of the `2×2×1` solid**. It splits into two disks meeting only along the retained bottom loop: a bottom four-face disk and a twelve-face complementary lid. Interior Haar integration factorizes and gives

\[
 2^{1-4}\chi_1(U)\;2^{1-12}\chi_1(U^{-1})
 = 2^{-14}\chi_1(U)^2
 =\frac1{16384}\left(1+\chi_2(U)\right).
\]

No other squarefree face set can contribute `chi_2`, so the adjoint coefficient is **exactly** `lambda^16/16384` in the unnormalized kernel (and `lambda^16/[16384 A0(lambda)]` in the normalized one). This is an actual generated **higher-representation interaction** from the finite 3D spatial shell. It should not be confused with the much earlier adjoint coefficient generated by the *different exponential planar face action* of PR #63.

### (d) Bound all remaining nonabelian higher-order configurations without evaluating them

The nine remaining area-twelve, four area-fourteen and one area-sixteen face subsets exhaust every allowed contribution not included in `P0+P1 chi_1`. Each selected fundamental trace has absolute value at most two; normalized Haar is probability measure. Consequently

\[
 \|E_{12}(\cdot;\lambda)\|_\infty
 \le9(2|\lambda|)^{12}+4(2|\lambda|)^{14}+(2|\lambda|)^{16}
 =R_{12}(\lambda).
\]

Haar integration of the fixed boundary holonomy gives `A0=P0+overline E12` with `|overline E12|≤R12`. With `P0≥1`, `|chi_1|≤2`, and `A0≥(1−2|lambda|)^20`, straightforward algebra yields the displayed normalized error inequality. The order-ten coefficient in `P1/P0` is `1/128−(1/8)(1/4)=−3/128`, proving the stated asymptotic comparison. ∎

## 4. Reproducibility and code limits

`verify_cubic_transverse_shell.py` builds the exact oriented cubical incidence structure, calculates the relative mod-two nullspace (rank 15, nullity five), and **independently** evaluates all 1,048,576 face masks. It reports the allowed surface area census, derives the low-order disk/sphere factors by Euler counts and Schur orthogonality, verifies that only the outer 16-face sphere has two fundamental factors on every boundary edge, and checks the fundamental SU(2) Schur matrix-element identity against the exactly matching `Q8` second moments. The `Q8` check is used **only** at the pairwise matrix-element level: it is **not** incorrectly substituted for SU(2) Haar fourth moments at branching links.

The checker also evaluates the explicit normalized sup-norm remainder bounds at six sample coupling values. These are analytical finite-combinatorial checks, not a numerical construction of the interacting gauge-theory vacuum. Results: `slab_verification.json`, `verification.log` and a SHA-256 manifest. Prior isolated planar/verifier records from PR #63 remain unaltered.

## 5. What this settles, what it does not, and the next rigorous test

**Settled (finite 3D spatial truncated-weight model):** the first full transverse shell creates vacuum closed-cube fluctuations at order six, a **nonzero** transverse correction to the coarse fundamental Wilson character at order eight, and an exact adjoint character at order sixteen. The normalized finite-block difference from the planar truncation is bounded explicitly in sup norm for `|lambda|<1/2`.

**Not settled:** the full exponential Wilson plaquette weight, the **same-action physical Euclidean-time heat-kernel transfer**, the actual `g0(h)→0` ultraviolet trajectory, nonperturbative vacuum correlations, a volume/refinement-uniform mass gap, the source-correct quasicrystalline 3D action or a gravitational fluctuation operator. In particular the finite positive polynomial weight has no independently established reflection-positive **time** transfer; **no** four-dimensional dynamical claim is licensed by this report. High-temperature small `lambda` does not substitute for weak-bare-coupling asymptotic freedom.

**Next testable bridge:** repeat this small 3D shell calculation with the **actual Wilson exponential** and temporal heat-kernel transfer, keeping the full SU(2) recoupling/intertwiner channels. Compare physically time-separated, renormalized Wilson-derived probes across an `h→h/2` pair. A useful finite block estimate must then be extended with constants controlled uniformly in 3D spatial box size, refinement and the genuine bare-coupling trajectory. The Penrose model separately requires a valid oriented **three-dimensional** regulator and action before any transfer statement.

## Source and literature anchors

- `research/theorems/R3_CUBIC_HAAR_BLOCK_MAGNETIC_LEAKAGE_2026-11-05.md` — original-link Haar cylinder obstruction.
- `research/theorems/R3_CUBIC_FACE_BLOCK_HAAR_RECOVERY_2026-11-05.md` — four-face exact fundamental-character contraction.
- `research/theorems/R3_SU2_PLANAR_BLOCK_CHARACTER_TRANSFER_2026-11-05.md` — isolated planar **exponential** SU(2) character convolution.
- `research/audits/P0_CUBIC_HEAT_KERNEL_TRANSFER_CERTIFICATE_2026-11-04.md` — finite same-action heat-kernel time transfer.
- `docs/research/YM_CUBIC_PENROSE_TRANSFER_AND_INFRARED_GATES_2026-11-05.md` — model-specific P0–P5 and T0–T5 open obligations.
- K. G. Wilson (1974), *Confinement of Quarks*; J. B. Kogut (1979), *An introduction to lattice gauge theory and spin systems*. The SU(2) character/Schur strong-coupling machinery is standard; the finite `2×2×1` slab coefficients here are a scoped check within the project's chosen geometric interface, **not** a claim to discover the method.
