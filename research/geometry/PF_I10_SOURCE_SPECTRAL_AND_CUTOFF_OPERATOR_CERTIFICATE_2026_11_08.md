# PF-I10 — Source-faithful spectral functionals, cutoff-order theorem and finite factorization

**Research checkpoint:** 8 November 2026, America/Denver.  
**Source status:** author's unpublished research script `paper6_extend_local.py`, SHA-256 `86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da`, preserved **privately** in Library. Draft paper numbers do not define manuscript provenance.  
**Scope:** eight original cut-and-project-selected source weighted scalar graph operators and the **source-implemented finite triangular periodic negative control**. Three sizes are verified through **complete dense eigenvalue diagonalization**; five larger sizes through source-matrix sparse **stochastic Lanczos quadrature (SLQ)**, with independently checked numerical errors. Neither a four-dimensional gauge measure, a continuum existence theorem, a positive Yang–Mills physical mass gap, nor gravity UV finiteness is established. The source's original vertex/edge selection remains unmodified.  
**Next proof gate:** source-qualified interacting SU(2) lattice construction, well-defined observables and scale/continuum transfer on intrinsic accepted graph—not adoption of any cubic physical spacetime model.

## 1. Objective: reproduce the published-source scalar spectral channel, not fit it

PF-I9 recovered the original cut-and-project geometry, source weighted-basis edge dictionary and the exact first moment \(R(-1)\). This next milestone independently evaluates the **nontrivial nonlinear spectral functions** and distinguishes the original truncated tile graph from the complete basis-edge/cut-and-project operator.

The original source selects a retained vertex set \(V_g\) using its capped grid enumeration and **35%-of-maximum tile-center radius** followed by a one-pass incident-tile inclusion condition. It constructs five-basis-neighbor edges on **the same retained labels** with Fibonacci hopping

\[
 t(j,k)=\begin{cases}1, & \lfloor(k+1)/\varphi\rfloor\ne\lfloor k/\varphi\rfloor,\\
 \varphi^{-2}, & \text{otherwise},\end{cases}\qquad \varphi=\frac{1+\sqrt5}{2}.
\]

The exact source operator is \(L_g=D_w-W\), \((D_w)_{vv}=\sum_{u\sim v}w_{vu}\). The **source's periodic negative control** is a finite open triangular zigzag graph with side \(q=\lfloor\sqrt{|V_g|}\rfloor\), \(N_\mathrm{per}=q^2\), and every bond weighted at \(t_{\rm avg}=(1+\varphi^{-2})/2\). Its two graph sizes are generally **not identical**, and no physical dimension is inferred from this comparator.

The source script's dense generator was compared **entrywise** with independently assembled sparse matrices at 1,550 vertices, and its periodic dense generator likewise compared with the source-matched sparse comparator. For all eight sizes, exact bond counts, source SHA, row sums, Laplacian trace, periodic edge count, and component counts were checked. **No source mass/coupling or reference scale was tuned to the published values.**

For positive Laplacian eigenvalues \(\lambda>0\) and \(m^2=10^{-4}\), define the normalized, positive-mode source ratios

\[
 R(-\tfrac12)=\frac{\frac1{N_{QC}^+}\sum_{\lambda^+_{QC}}\sqrt{\lambda+m^2}}{\frac1{N_{per}^+}\sum_{\lambda^+_{per}}\sqrt{\lambda+m^2}},\quad
 \frac{\zeta'_{QC,m}(0)}{\zeta'_{per,m}(0)}=\frac{\frac1{N_{QC}^+}\sum_{\lambda^+_{QC}}\log(\lambda+m^2)}{\frac1{N_{per}^+}\sum_{\lambda^+_{per}}\log(\lambda+m^2)}.
\]

(The minus signs in the derivatives cancel in the ratio.) The published Paper4-style mass-relative determinant statistic is

\[
 \Gamma_{g,rel}(m^2)=\frac1{2N_g^+}\sum_{\lambda^+>0}\log\left(1+\frac\lambda{m^2}\right),\qquad
 R_{\Gamma}(m^2)=\frac{\Gamma_{QC,rel}(m^2)}{\Gamma_{per,rel}(m^2)}.
\]

**These are separate functionals.** \(\zeta(-1/2)\) is not \(-\zeta'(0)\), and neither scalar construction is the spectrum of a completed non-Abelian Yang–Mills interacting vacuum. Their finite numerical reproduction does **not** validate a claimed gravitational one-loop action, which would additionally require the correct gauge-fixed fluctuation operator, renormalization prescription, and continuum limit.

## 2. Exact three-size diagonalization

Using the exact source graph selection and the actual finite source periodic matrix, complete symmetric eigensolvers return:

| N_grid | Source N | Source basis edges | \(R(-1/2)\) | \(\zeta'_{QC}(0)/\zeta'_{per}(0)\) | \(R_\Gamma(10^{-4})\) |
|---:|---:|---:|---:|---:|---:|
| 7 | 1550 | 3017 | **0.8338194851** | 0.6421389316 | 0.9589841329 |
| 10 | 3042 | 5927 | **0.8303487155** | 0.6347803746 | 0.9576836646 |
| 12 | 4324 | 8468 | **0.8354604886** | 0.6489207682 | 0.9591528407 |

The first-three mean \(R(-1/2)=0.8332095631\) is numerically close to the *source-reported eight-size* 0.8332, but **three sizes are not an eight-size verification**. Each exact spectrum excludes the positive weighted Laplacian's known zero eigenspace, using threshold \(\lambda>10^{-10}\).

## 3. Eight original source-size results: three exact, five independent SLQ estimates

For the five larger systems, the source matrices are represented sparsely, with 256 Rademacher probes and 180 Lanczos steps at sizes 15,18,20 and 128 probes/160 steps at 23,25; a first-trace control variate is used to reduce probe noise. The SLQ algorithm computes \(z^T f(L+m^2I)z\) from the Lanczos tridiagonal Gauss quadrature, separately for the quasicrystal and source triangular control. The exact zero-mode count \(c=\#\text{components}\) is removed algebraically:

\[
 \overline f_{>0}=\frac{N\overline f_{\rm all}-c f(m^2)}{N-c}.
\]

For the square root, \(f(m^2)=\sqrt{m^2}\); for the logarithm, \(f(m^2)=\log m^2\); for the mass-relative \(\log(1+\lambda/m^2)\), the zero contribution is 0.

| N_grid | Source N | Method | \(R(-1/2)\) | \(\zeta'_{QC}(0)/\zeta'_{per}(0)\) | \(R_\Gamma(10^{-4})\) |
|---:|---:|---|---:|---:|---:|
| 7 | 1550 | Exact | 0.833819 | 0.642139 | 0.958984 |
| 10 | 3042 | Exact | 0.830349 | 0.634780 | 0.957684 |
| 12 | 4324 | Exact | 0.835460 | 0.648921 | 0.959153 |
| 15 | 6980 | SLQ | 0.834590 | 0.651350 | 0.959214 |
| 18 | 9950 | SLQ | 0.831430 | 0.642730 | 0.958094 |
| 20 | 12207 | SLQ | 0.831184 | 0.644401 | 0.958218 |
| 23 | 16435 | SLQ | 0.835051 | 0.655108 | 0.959423 |
| 25 | 19260 | SLQ | 0.833596 | 0.651433 | 0.958939 |
| **Arithmetic mean** | | **3 exact + 5 SLQ** | **0.8331846870** | **0.6463577401** | **0.9587136627** |
| **Sample SD across 8 sizes** | | | 0.00193960 | 0.00657525 | 0.00062816 |

For the five SLQ rows, the conditional standard error of the *eight-size arithmetic mean* due only to randomized probes is about **0.0000222** for the square-root ratio and **0.000129** for the log-derivative ratio. These do **not** bound deterministic quadrature error, source-model specification error, finite-size extrapolation error or physical uncertainty. The reported manuscript values of **0.8332** and approximately **0.646** are thus **numerically reproduced at their stated precision by this source-defined operator**, with three sizes exact and five controlled stochastic estimates. This is not a computation of all 19,260 exact eigenvalues.

### Numerical validation and reproducibility

1. Each of the first three exact systems was compared with the independent SLQ estimates using the same source operator. The controlled estimates agree within their probe standard errors at the scale tested (square-root discrepancies about \(7.1\times10^{-5}\) to \(1.4\times10^{-4}\)); the log-derivative differences are within the quoted sampling uncertainties.
2. On the largest \(19,260\)-vertex graph, **holding the same 128 random probes and seed fixed**, increasing Lanczos depth from 160 to 240 changes \(R(-1/2)\) by **\(6.16\times10^{-8}\)** and the \(\zeta'(0)\) ratio by **\(3.40\times10^{-5}\)** at \(m^2=10^{-4}\). The \(R_\Gamma\) change at that mass is \(3.65\times10^{-6}\). These are observed convergence differences, not rigorous uniform approximation bounds.
3. The original PF-I9 source \(R(-1)\) trace is retained exactly. The new sparse implementation matches that exact first moment on every source graph; no comparator normalization was adjusted to achieve nonlinear ratios.
4. All computations are repeatable from the source SHA, fixed seeds, sparse matrix caches and deterministic JSON outputs. Wall-clock timing fields are deliberately removed from the canonical evidence, following the PF-I9 nondeterminism correction.

## 4. Mass-relative determinant flow reproduced independently

The same source spectra provide the four previously reported mass-flow points:

| Squared mass \(m^2\) | Recomputed eight-size mean | Provisional source value |
|---:|---:|---:|
| \(10^{-4}\) | **0.95871366** | 0.959 |
| \(10^{-2}\) | **0.92682685** | 0.927 |
| 1 | **0.81579626** | 0.816 |
| 100 | **0.73887697** | 0.739 |

All four were obtained without fitting a mass-flow curve; they are the exact original source operator with the quoted masses and zero-mode rule. However, the general endpoint behavior of this mass-relative determinant is mathematical for **any** two finite positive spectra: the ratio approaches 1 at small \(m^2\) and the ratio of mean retained eigenvalues at large \(m^2\). That by itself is **not** a new RG fixed-point or gravitational UV theorem.

## 5. Exact PF-I10.A: missing rhombi add a positive-semidefinite finite operator

Let \(L_{tile}\) be the author's **line-level-capped** tile-edge graph operator and \(L_{basis}\) the source's coupled five-basis-neighbor operator on **the identical original retained vertex labels**. PF-I9 proves all extra source basis edges are genuine edges of **completed** acceptance-window rhombi; this audit directly verifies the sparse weighted matrices. Let \(E_+=E_{basis}\setminus E_{tile}\). Then

\[
 \boxed{L_{basis}-L_{tile}=\sum_{e=\{u,v\}\in E_+} w_e(\delta_u-\delta_v)(\delta_u-\delta_v)^T\succeq0.}
\]

**Proof:** Each original tile edge is also an original basis edge with the **same positive Fibonacci weight**. Subtract the two symmetric weighted Laplacians; the common edges cancel, leaving exactly the positive edge quadratic forms. **QED.**

The min–max principle yields ordered eigenvalue monotonicity \(\lambda_k(L_{tile})\le\lambda_k(L_{basis})\). For any fixed \(m^2>0\), strictly increasing scalar functions \(\sqrt{x+m^2}\) and \(\log(x+m^2)\) applied to the finite eigenvalue multisets therefore yield nondecreasing **full-mode** normalized traces, and strict change whenever \(E_+\ne\varnothing\). In particular

\[
 \operatorname{Tr}\left[\log(L_{basis}+m^2I)-\log(L_{tile}+m^2I)\right]>0
\]

when added edges are nonempty. This is a **finite cutoff-order** result; it does not establish anything about a continuum Yang–Mills Hamiltonian.

| N_grid | Original tile E | Coupled/complete E | Added E | Original tile components | Coupled components |
|---:|---:|---:|---:|---:|---:|
| 7 | 3017 | 3017 | 0 | 1 | 1 |
| 10 | 5865 | 5927 | 62 | 51 | 1 |
| 12 | 8383 | 8468 | 85 | 46 | 1 |
| 15 | 13489 | 13779 | 290 | 11 | 1 |
| 18 | 19149 | 19593 | 444 | 101 | 3 |
| 20 | 23498 | 24091 | 593 | 74 | 1 |
| 23 | 31693 | 32582 | 889 | 46 | 1 |
| 25 | 37073 | 38139 | 1066 | 111 | 5 |

**Why zero-mode filtering matters:** Positive-only *normalized* spectral means are **not** necessarily monotone when the two graphs have different nullities. At grid 10 the same-source full-mode \(R(-1/2)\) moves from **0.821624** (truncated tile) to **0.830351** (basis/complete), in agreement with the exact PSD theorem. But after excluding all zero eigenvalues the tile statistic is **0.835271**, *larger* than the coupled **0.830349**, because the tile graph has **51** zero modes versus **one**. Thus changing both the operator and the retained-mode denominator can reverse the reported comparison. This explains a finite implementation hazard, not the existence or absence of a physical gap.

At grid 25 the same qualitative structural issue is substantial: **111** tile-graph components versus **five** coupled components, with 1,066 omitted edges. The 19,260-site tile spectral comparison is SLQ approximate, so an exact full-eigenvalue tile ratio is not claimed.

## 6. Exact PF-I10.B: source-specific spectral-moment factorization, with a negative-control conclusion

Let \(L_{uni}\) use **the same original source coupled graph** but every edge at the comparator's \(t_{avg}\). For each spectral moment/functional with nonzero denominators, the identity

\[
 \boxed{\frac{Z_{fib}}{Z_{per}}=\frac{Z_{fib}}{Z_{uni}}\frac{Z_{uni}}{Z_{per}}}
\]

is algebraically exact. For the mass-regularized positive-mode square-root moment at \(m^2=10^{-4}\), this finite source study gives eight-size arithmetic means of the **per-size factors**

\[
 \left\langle\frac{Z_{fib}}{Z_{uni}}\right\rangle\approx\boxed{1.0390},
 \qquad\left\langle\frac{Z_{uni}}{Z_{per}}\right\rangle\approx\boxed{0.8019},
 \qquad\left\langle\frac{Z_{fib}}{Z_{per}}\right\rangle=0.833185.
\]

**These are means of factors, so the product of the two means is not asserted to equal the mean of the products.** At every **individual size**, their product agrees exactly with the total ratio. Under the source's finite scalar normalization, Fibonacci weight redistribution **increases** this moment relative to the *same graph with uniform \(t_{avg}\)*; the relative suppression below 1 appears in the uniform-source-graph versus periodic-reference factor. This is a *specific finite scalar comparison*, not a causal partition of a physical effective action or a refutation of intrinsic geometry.

## 7. Scientific interpretation and next actual theorem gate

**Established here:** an independently reproduced original source scalar spectrum (three exact eigendecompositions; five numerically validated approximations), all four mass-relative determinant ratios, an exact cutoff-added-bond PSD theorem, and an exact separation of source Fibonacci hopping from same-graph coordination/reference normalization. These results substantively **resolve the finite scalar source-reproduction portion** of PF-I9's gate under the identified source variant.

**Not established:** the individual exact eigenvalue lists for the five largest graphs; rigorous stochastic trace-confidence and quadrature envelopes independent of numerical assumptions; phason/thermodynamic uniformity; a full physically justified 4D gauge field variable/action on the intrinsic \(\mathbb Z^5\) \(2+2+1\) complex; OS positivity, invariant time evolution, spectral gap uniformity, or nontrivial continuum Yang–Mills existence; gravitational UV renormalization. The triangular/square/cubic controls remain **negative comparisons**, never required physical regulator geometry.

**Next proof objective PF-I11 (OPEN):** Define a source-faithful **gauge-invariant SU(2) link and rhombus-face Wilson action** on the same accepted cut-and-project complex, specify an intrinsic reflection/transfer or constructive continuum framework *without assuming cubic spacetime*, and identify a falsifiable uniform-gap observable with rigorous volume/scale control. Independently examine source quasicrystalline face-completion/crop choices under the gauge action; a scalar \(R(-1/2)\) or determinant ratio is **not** that gap. Carry forward boundary/phason sensitivities and do not promote a finite signal into a theorem without proved uniform estimates.

## 8. Reproducible files and preservation

- **Public derived scripts:** `verify_pf_i10_source_spectral.py` for SHA-pinned original source matrix construction, sparse periodic control and initial SLQ; `verify_pf_i10_multimass.py` for four-mass stochastic Lanczos and exact-trace control variates; `exact_multimass.py` for small-size dense validation; `verify_pf_i10_tile_cutoff.py` for original tile-graph PSD difference; `verify_pf_i10_tile_spectral.py` for comparison under zero filtering; and `assemble_pf_i10_evidence.py` for deterministic analysis summaries. All require the **original unpublished source as a separately provided private input** for source-generation stages.
- **Tests:** `test_pf_i10_source_spectra.py`, **18 passing** with the original private source file available. Source-dependent tests explicitly skip when the unpublished file is absent rather than pretending to certify it in GitHub CI.
- **Summary JSON:** `PF_I10_EIGHT_SIZE_SPECTRAL_SUMMARY.json`, with per-size exact versus SLQ provenance, probe SE, numerical source-convention choices, full four-mass curves, and same-graph factorization.
- **Private full replay:** source script preserved unmodified under user Library, full original sparse source graph NPZ matrices (all eight sizes), raw and timing-stripped SLQ evidence, exact three-size spectra, seed/step-convergence receipt, original tile-cutoff records, test log and manifest. Runtime timing fields are excluded from canonical evidence checksums.
- **Reproduce from Library** with pinned NumPy/SciPy versions, BLAS threads fixed to one for validation. All eight original source graph N/E counts and original periodic conductance are verified independently before spectral ratios are calculated.

**PF-I10 resolution:** Finite source-spectral reproduction is materially advanced and statistically supported; **PF-G0/P0–P5/PF-G0–G5 and all interacting continuum proof gates remain OPEN** until the independent physical construction and uniformly controlled limit are achieved. No source manuscript is declared published or final, and no unpublished source executable is committed to the public repository.
