# Source-order/local-first tame implication audit: uniform formal Borel disk

**Date:** 2026-11-04  
**Status:** New conditional deduction from previously archived finite-strip theorems. Independent mathematical audit of the full coefficientwise matrix Peter–Weyl tame inequality is **not completed**. Not a Yang–Mills continuum or mass-gap proof.

## 1. Sources and exact scope

This note uses three repository statements:

1. [Source multigrading and linked-history reachability](../../research/theorems/R3_IR_SOURCE_MULTIGRADING_LINKED_HISTORY_2026-11-03.md): at homogeneous fundamental plaquette source order `n`, every nonzero original-edge SU(2) label is at most `n`; histories and disconnected physical outputs are retained.
2. [Local-first fixed-radius tame fusion](../../research/theorems/R3_IR_LOCAL_FIRST_TAME_2026-11-03.md): conditional graded estimate for `B_hist` on a **finite open straight square strip** in the corrected original-link model, with coefficientwise PW trace-class assumptions.
3. [Proof-path discovery](../observatory/PROOF_PATH_DISCOVERY_2026-11-04.md): the formal Gevrey-1 majorant obtained by combining (1)–(2).

The archived full supporting proof and executable of (2) have **not** been independently replayed in this investigation. In particular, a function-norm estimate cannot automatically replace its required coefficientwise PW recoupling inequality. The conclusion below inherits that gap.

## 2. Conditional theorem: common positive Borel radius

Assume the original-link finite-strip model, `κ>0`, `σ≥0`, and uniform kinetic coefficients `0<a_0≤a_e≤a_*`. Let `L^(r)` denote the archive's local-first norm

```
||F||_(L^r) = sup_x sum_(I contains x) exp(κ |I|)
               sum_(spin sectors n) d_n exp(σ |n|)
               (1+max_e n_e)^r ||A_(I,n)||_(S1).
```

Let `C_cross,C_nest≥0` be the explicit constants in source (2), assumed independent of strip length. For a homogeneous **formal** score `S_N(z)=sum_(n≥1) z^n S_(n,N)` from fundamental magnetic plaquette sources, let

`a_(n,N) = ||S_(n,N)||_(L^1)`, `M_N=a_(1,N)`.

Assume a finite `M_0` independent of N with `M_N≤M_0`. This holds for identical bounded singleton source strengths under the local-first norm, as the one-face source has bounded local PW coefficients and each spatial anchor belongs to at most one singleton face history. This bound is uniform in N but can depend on `κ,σ,a_0,a_*`.

Set `D=3 C_cross+12 C_nest>0`. Then the already derived source-graded recurrence yields

```
a_(n,N) ≤ M_0^n D^(n−1) (n−1)!,  n≥1.
```

Define the *order-one formal Borel transform* of the vacuum score by

```
B_N(ξ) = sum_(n≥1) S_(n,N) ξ^n/n!.
```

For all `N`, this series converges absolutely in the corresponding finite-strip `L^(1)` Banach completion for

```
                      |ξ| < 1/(M_0 D).
```

Moreover, whenever `0≤r<1/(M_0D)`,

```
sup_N sup_(|ξ|≤r) ||B_N(ξ)||_(L^1)
        ≤ (1/D) [-log(1 − M_0 D r)].
```

For `M_0=0` all formal coefficients vanish under the homogeneous recurrence and the transform is identically zero.

**Proof.** The source-order selection rule implies `||S_(n,N)||_(L^2)≤(n+1)a_(n,N)` because the Fourier-sector sum occurs **inside** each anchor supremum, so every sector has `1+max_e n_e≤n+1`. The local-first tame inequality applied to `S_i,S_j` with `i+j=n` gives

```
a_n ≤ [C_cross + C_nest(n+2)] sum_(i=1)^(n−1) a_i a_(n−i).
```

The induction in source (3) then yields the displayed Gevrey-1 bound (one may use `sum_(k=0)^m 1/binom(m,k)≤3` and `n+2≤4(n−1)` for `n≥2`). Divide by `n!` and sum norms:

```
||B_N(ξ)|| ≤ sum_(n≥1) (M_0D|ξ|)^n/(D n)
           = −log(1−M_0D|ξ|)/D.
```

This proves the common open Borel disk and local uniform convergence. The argument is valid in each finite-strip Banach completion, not a claim of a common infinite-volume limit; the spaces vary with N.

## 3. What this actually contributes

- The formal Gevrey-1 majorant yields a **strictly positive, volume-independent lower bound for the Borel analytic radius** as an immediate deduction; this was not explicitly singled out in the prior proof-path report.
- This is a statement about Borel transforms of **formal perturbative score coefficients**, *not* convergence of `S_N(z)` for any nonzero physical `z`.
- It does **not** prove analytic continuation of `B_N` along a Laplace ray, at-most-exponential growth, equality to a physically positive ground state, a resummation uniqueness theorem, or a 3D/4D continuum limit. These are indispensable independent Borel-summability obligations.
- The bound does not independently validate the inherited coefficientwise Clebsch–Gordan and Casimir estimates, and does not supersede Gevrey-2 results proved for **different connected-L² scalar majorants**.
- The independent positive *scalar equality* recurrence with the same `n`-linear kernel can have factorial growth. No inference from this observation to actual signed SU(2) coefficients is justified.

## 4. Reproducible check and next mathematically decisive gate

The exact arithmetic script [`verify_local_first_borel.py`](../scripts/verify_local_first_borel.py) checks orders 1–80 for the positive scalar recurrence with `M=1,C_cross=2,C_nest=3`, verifying the convolution factorial majorant, reciprocal-binomial bound and Borel coefficient estimate. It does **not** check the infinite-dimensional operator theorem.

**Next objective:** independently reconstruct the original-link coefficientwise Peter–Weyl recoupling bound behind the local-first tame estimate, prioritizing the smallest nested physical spin networks, and verify original-source convention equivalence. Only once the tame map is independently validated should one investigate whether actual source-generated cancellations imply Borel continuation and growth control. Any claim transporting the strip result to a 3D refining regulator must first pass P0.

## 5. Status decision

**Conditionally valid mathematical inference**, with the analytic tame hypothesis and local source norm explicitly identified. **No novel unconditional proof of a Yang–Mills mass gap.**
