# P0–P2: full SU(2) Wilson-exponential transverse-shell coefficient and an exact positive physical-time blocking-memory term

**Dated November 6, 2026 (UTC); local research session November 5, America/Denver.** **Status: finite cubic regulator theorem candidate; independent mathematical review pending.** The continuum four-dimensional Yang–Mills mass gap, physical renormalization trajectory, Penrose 3D regulator and gravitational ultraviolet objectives remain **OPEN**. This is not a theorem about spatial-refinement-uniform physical time.

## 1. Source context, operator identity, and the precise new scope

The previous cubical calculation at [the source-identified 2×2×1 shell](R3_CUBIC_FIRST_TRANSVERSE_SHELL_CHARACTER_BLOCK_2026-11-06.md) treated the **truncated positive polynomial** face weight `1+λ χ₁(U_p)` and determined the first transverse coefficient and the higher-spin external-sphere channel. The preceding planar calculation in PR #63 established the isolated four-face SU(2) character convolution for `exp(t χ₁)`. The present result **uses the full exponential on every spatial face** and adds a genuinely physical temporal heat-kernel transfer on the **same fixed 3D original-link SU(2) model**. Neither component implies continuum-scale infrared control.

The open spatial cubical slab has 18 vertices, 33 edges and 20 faces: four bottom xy, four top xy, and twelve transverse xz/yz faces. Fix the eight bottom perimeter links and integrate all other 25 links with normalized SU(2) Haar. Let `χ₁=tr_fund`, `χ_n` be the SU(2) character of dimension `d_n=n+1` (`χ₂` is the adjoint). Let `B` denote the four bottom faces and `S` the remaining sixteen faces. The bottom and shell couplings are separately denoted `b` and `s` **as an analytical probe**; the physical full spatial Wilson action takes `b=s` at a fixed Euclidean time step.

Normalize the full Wilson exponential face weight by

\[
 a_n(x):=I_n(2x)-I_{n+2}(2x),\qquad
 a_0(x)=\int_{SU(2)}e^{x\chi_1(U)}dU>0,\qquad
 b_n(x)=\frac{a_n(x)}{a_0(x)},\qquad
 w_x(U)=\frac{e^{x\chi_1(U)}}{a_0(x)}=\sum_{n\ge0}b_n(x)\chi_n(U).
\]

The expansion converges absolutely and uniformly for each real finite `x` and `b₀=1`. The central character coefficients satisfy `a'_0=a₁`, `a'_n=a_{n−1}+a_{n+1}` for `n≥1`, and `a_n(x)=d_n I_{n+1}(2x)/x` for `x≠0` (continuous extension at zero). `a₀(x)≥1` by Haar Jensen because `∫χ₁=0`.

Define the **one-time-slice spatial conditional Boltzmann kernel**

\[
 Z_{3D}(U;b,s):=\int_{SU(2)^{25}}
 \prod_{p\in B}w_b(U_p)
 \prod_{q\in S}w_s(U_q)\,dU_{\rm integrated},
\quad U=U_{\partial P}.
\]

Gauge covariance and Haar invariance make it a central function of the fixed coarse loop. This spatial integral is **not** an exact closed coarse quantum time transfer, because the integrated fine links have electric/temporal correlations between neighboring time slices. That distinction is proved quantitatively below.

## 2. Exact Wilson-exponential five-face shell decomposition (nonperturbative in the bottom coupling)

For the bottom planar 2×2 face disk, the exact full-exponential character kernel is

\[
 Z_{2D}(U;b)=\sum_{n=0}^{\infty}\frac{b_n(b)^4}{(n+1)^3}\chi_n(U).
\]

Use the **centered shell face factor**

\[
 \delta_s(U)=w_s(U)-1=\sum_{n\ge1}b_n(s)\chi_n(U),\quad
 D(s):=2\left(e^{2|s|}-1\right),\quad\|\delta_s\|_\infty\le D(s).
\]

For each of the four elementary bottom squares `p`, let `C(p)` be the **five-face complementary cap** of its cube above: one top face and four transverse walls. The exact cap integral is the SU(2) disk convolution

\[
 \mathcal K_s(V):=\int\prod_{q\in C(p)}\delta_s(U_q)\,dU_{\rm cap}\ 
 =\sum_{n\ge1}\frac{b_n(s)^5}{(n+1)^4}\chi_n(V),
 \qquad V=U_{\partial p}.
\]

**Theorem A (fixed finite 3D slab, all real `b,s`).**

\[
\boxed{\displaystyle
 Z_{3D}(U;b,s)=Z_{2D}(U;b)+
 \sum_{p\in B}\int_{\text{four bottom internal links}}
 \left(\prod_{q\in B}w_b(U_q)\right)\mathcal K_s(U_{\partial p})\,dU_B
 + \mathcal R_8(U;b,s).
}\]

The remainder obeys the **explicit uniform finite bound**

\[
\boxed{\displaystyle
 \sup_{U\in SU(2)}|\mathcal R_8(U;b,s)|
 \le e^{8|b|}\sum_{k=8}^{16}{16\choose k}\,[2(e^{2|s|}-1)]^k.
}\]

No smallness assumption on `b` is used. The bound holds for all real `s`; it is informative for small shell coupling. A coarser but simpler bound is `e^{8|b|} C(16,8) D(s)^8 (1+D(s))^8`. The proof does not incorrectly factorize nonmanifold higher-spin contributions: those are entirely contained within the explicit absolute remainder.

**Proof.** Expand the 16 factors as `∏_S(1+δ_s)` and collect subsets by the number of activated **distinct** faces. Any shell subset containing an edge in the top/z region which occurs in exactly one activated face integrates to zero: integrate that edge first, since a normalized character with no trivial component has zero Haar integral. Complete combinatorial enumeration of all shell subsets of sizes 1–8 shows that there are no such edge-free subsets of sizes `1,2,3,4,6,7`, precisely four at size 5 (the complementary five-face cube caps), and four at size 8. This finite incidence certificate is independently reproduced without assuming low-order character contractions. Each five-face cap is a disk with fundamental bottom-square boundary and five plaquettes. The SU(2) character orthogonality and disk identity give `d_n^{1−5}=d_n^{-4}` for its spin-n term; `b_n(s)^5` comes from the five activated factors. Every remaining nonzero subset has at least eight activated shell faces. Bound its Haar integral by `e^{8|b|}D(s)^k` using normalized Haar, `a₀(b)≥1`, and `|χ₁|≤2`. Summing `C(16,k)` possible subsets proves the theorem. ∎

### A complete first transverse Taylor coefficient

Since `b₁(s)=s−s³/6+O(s⁵)` and `b_{n≥2}(s)=O(s^n)`, the cap has

\[
 \mathcal K_s(V)=\frac{1}{16}\left(s^5-\frac56 s^7\right)\chi_1(V)+O(s^9).
\]

Consequently, for each fixed finite `b`, uniformly in the retained loop holonomy,

\[
\boxed{\displaystyle
 Z_{3D}(U;b,s)=Z_{2D}(U;b)+
 \left(s^5-\frac56 s^7\right) C_5(U;b)+O_b(s^8),
\quad C_5(U;b)=\frac1{16}\left(\partial_b+4\frac{a'_0(b)}{a_0(b)}\right) Z_{2D}(U;b).
}\]

Equivalently, the **full-exponential coefficient for arbitrary fixed bottom coupling** is

\[
 \boxed{\displaystyle
 C_5(U;b)=\frac14\sum_{n\ge0}
 \frac{a_n(b)^3a_n'(b)}{a_0(b)^4(n+1)^3}\chi_n(U).
 }
\]

The `s⁷` term is essential: absence of distinct six- or seven-face **supports** does **not** eliminate higher-order character coefficients on the five existing faces. This corrects an initially tempting but invalid shortcut. Near `b=0`, the scalar part begins `b/4`, and the coarse fundamental channel begins `b³χ₁/32`, recovering the previous truncated-weight geometric coefficients `b s⁵/4` and `b³s⁵χ₁/32` without confusing the two actions. At the physical equal-coupling slice `b=s=t`, the first transverse scalar contribution begins `t⁶/4` and the first transverse fundamental contribution begins `t⁸ χ₁/32`; other equal-order scalar terms arise from the full exponential and are not asserted to vanish.

## 3. Full Wilson spatial Hamiltonian and positive physical-time heat-kernel transfer

On the **same finite original-link 3D SU(2) Hilbert space**, let

\[
 \mathcal H=L^2(SU(2)^{33}),\quad
 K_h=\alpha_h\sum_{e=1}^{33}C_e,\quad
 V_h=\beta_h\sum_{p=1}^{20}\left(1-\frac12\chi_1(U_p)\right),
\quad \alpha_h=\frac{g_0(h)^2}{2h},\quad \beta_h=\frac{2}{g_0(h)^2h}.
\]

All operators commute with the vertex SU(2) gauge action and restrict to the Gauss-invariant physical subspace. The kinetic form is positive self-adjoint on the usual Peter–Weyl core, the finite-volume magnetic potential is bounded and nonnegative, and the **same-action symmetric transfer** is

\[
 T_\varepsilon=e^{-\varepsilon V_h/2}\,e^{-\varepsilon K_h}\,e^{-\varepsilon V_h/2},
 \qquad T_\varepsilon\ge0,\quad T_\varepsilon^*=T_\varepsilon.
\]

The spatial factor `e^{-εV_h}` is the **full Wilson exponential**, with one face coupling `t=εβ_h/2` and an overall scalar vacuum-energy factor `e^{-εβ_h20}`. Normalizing the one-face exponential by `a₀(t)` changes only an overall scalar for a single time-slice spatial weight. The time kinetic term is a product of positive central SU(2) heat kernels. For each **fixed h and spatial box**, `(T_ε)^{⌊τ/ε⌋}→e^{-τ(K_h+V_h)}` strongly as ε→0. These are familiar finite-transfer properties, not a continuum existence theorem.

### Exact obstruction: spatial Haar compression is not a closed time evolution

Let `P` be the orthogonal conditional expectation that **retains the eight bottom perimeter links** and Haar-averages the other 25. Set `Q=I−P`. This projection is gauge-covariant and commutes with the independent-link kinetic Casimirs; it preserves the physical Gauss-invariant space. Every elementary face contains at least one integrated link, so

\[
 P\chi_1(U_p)P=0,\qquad
 PHP=PK_hP+20\beta_hP,
 \qquad H=K_h+V_h.
\]

Nevertheless **the compressed full time transfer is not** `e^{−εPHP}`. The failure is explicit, positive and present for every ε>0 in the constant Gauss-invariant test vector `1`:

\[
\boxed{\displaystyle
 \langle1,T_\varepsilon1\rangle
 \ge \left(\int e^{-\varepsilon V_h/2}\,dU\right)^2
 > e^{-\varepsilon20\beta_h}
 = \langle1,e^{-\varepsilon PHP}1\rangle.
}\]

**Proof.** `e^{−εK_h}` fixes the constant vector, and as a positive self-adjoint operator it dominates the orthogonal projection onto constants, so for `f=e^{−εV_h/2}` its quadratic form is at least `|⟨1,f⟩|²`. Strict scalar Jensen for `exp(−ε x/2)` proves the second inequality because `V_h` is not constant under product Haar. This uses the **actual full Wilson V** and physical-time heat kernel, not a truncated character surrogate. ∎

The quantitative short-time vacuum discrepancy is also exact at leading order:

\[
\boxed{\displaystyle
 \langle1,T_\varepsilon1\rangle-e^{-20\varepsilon\beta_h}
 =\frac{20\beta_h^2}{8}\varepsilon^2+O_h(\varepsilon^3).
}\]

Indeed, each distinct elementary face character is Haar-orthogonal to the others and has Haar squared norm one, so

\[
 \mathrm{Var}_{Haar}(V_h)=\big\|(V_h-20\beta_h)1\big\|_2^2
 =\frac{20\beta_h^2}{4}=5\beta_h^2.
\]

The analogous exact **two-step coarse-transfer memory identity** is

\[
\boxed{\displaystyle
 PT_\varepsilon^2P-(PT_\varepsilon P)^2
 =PT_\varepsilon QT_\varepsilon P
 =(QT_\varepsilon P)^*(QT_\varepsilon P)\ge0.
}\]

On the constant physical test vector,

\[
\boxed{\displaystyle
 \langle1,PT_\varepsilon QT_\varepsilon P1\rangle
 =\varepsilon^2\frac{20\beta_h^2}{4}+O_h(\varepsilon^3)
 =5\beta_h^2\varepsilon^2+O_h(\varepsilon^3).
}\]

To see the asymptotic, `T_ε1=1−εV_h1+O_h(ε²)` in `L²` because the constant is in the domain of all needed finite-grid operators. Since `QV_h1=−(β_h/2)Σ_pχ₁(U_p)` and the 20 characters are orthogonal, the leading squared norm is `ε²5β_h²`. No non-Markovian representation has been assumed; the identity directly shows that naive Haar compression of **one time step** cannot be composed into exact **two-step** coarse evolution. The positive memory term is the additional object a dynamical blocking theorem must control.

## 4. Independent finite checks and acceptance limits

`research/scripts/verify_wilson_shell_time_2026_11_06.py` implements:

1. Independent 3D incidence enumeration of all shell-face subsets of sizes 1–8, confirming the four minimal five-face caps and absence of sizes 1–4, 6 and 7. Prior shell code supplies the geometry, but its earlier character conclusions are not assumed by this enumeration.
2. Normalized Haar Jacobi quadrature verifying all first 13 SU(2) exponential-character Fourier coefficients at six positive/negative couplings against Bessel and representation-dimensional identities (maximum observed absolute residual `~1.9×10⁻¹⁴`).
3. Independent comparison of the spectral `C₅` series with the derivative expression and central finite-difference at 20 (`b`, loop-angle) combinations.
4. Exact all-spin five-face cap expansion and finite explicit uniform residual bounds, without pretending a small-bound numerical check proves a continuum assertion.
5. A separate one-plaquette gauge-invariant spin-character matrix model verifying both `t²` short-time coefficients for `e^{−tH}` and the symmetric heat-kernel `T_t`, and the positive two-step memory coefficient. The **20-face 3D** variance and time-memory coefficients are established algebraically by exact product-Haar orthogonality and incidence, not extrapolated from the one-plaquette matrix.

A reproducible evidence JSON and SHA-256 manifest accompany this report. These checks test definitions and finite arithmetic, not independent peer review.

## 5. Remaining P0–P5 and cubic-to-quasicrystal gates

**Finite target completed:** the first genuinely transverse shell has been analyzed with the full SU(2) Wilson exponential, a source-independent coupling perturbation, and the first exact **physical-time coarse-transfer memory** identity. It establishes why a *one-slice* effective magnetic interaction is insufficient for a closed coarse Hamiltonian under Haar projection.

**Still open:** (i) construct an interacting, gauge-invariant replacement for `P` retaining or systematically resumming time-memory and generated higher-spin operators; (ii) prove scale-/volume-uniform estimates along the **weak-bare-coupling** four-dimensional asymptotically free trajectory; (iii) establish a nontrivial full four-dimensional OS reconstruction and dense physical probes with a common positive infrared rate; (iv) define a genuine 3D Penrose-related physical regulator and justify any model transfer; (v) separately derive and control a physically justified gravitational fluctuation operator/quantum measure. The bare memory coefficient `5β_h²` is scale dependent; its growth is **not by itself evidence of a physical continuum divergence**, because renormalized observables, time rescaling, and cancellations have not been analyzed.

**Next mathematically discriminating task:** derive a gauge-invariant **two-time-slice influence/transfer kernel** retaining the integrated fine-link boundary data (or an explicit resolvent/Feshbach memory kernel), and bound its connected part on two successive 3D refinements. The exact positive memory above is the first nonzero coefficient any such construction must reproduce. Do **not** replace it by a Markovian scalar potential unless a uniform error theorem is supplied.

**Literature/scope:** standard SU(2) Peter–Weyl, character/Bessel expansions, Schur orthogonality, Wilson/Kogut–Susskind finite-lattice Hamiltonian and Trotter/heat-semigroup facts. The precise fixed cubical slab and new finite-block formulas are a scoped computational proof checkpoint, not a claim to invent character methods or to solve the Clay Yang–Mills problem.
