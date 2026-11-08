# PF-I3 — Paper 2 spectral-operator trace and determinant audit

**Date:** 2026-11-07 (America/Denver)  
**Research status:** exact finite scalar operator identities, conditional source-compatibility test, and independent illustrative P3/periodic controls. **NOT** independent reproduction of the unpublished Paper 2 numerical generator, its reported `Ngrid=25, Nint=19260` spectrum, a geometric/time reconstruction, a Yang–Mills interacting vacuum or gap, or gravitational UV finiteness. **PF-G0, P0–P5, PF-G0–G5, T0–T5 and gravitational proof gates remain OPEN** (the legacy T5 transfer record remains conditional).

## 1. Primary source and exact stated data

The user's original `Sharpe_dissertation_v10.7.tar.gz` contains:

- `delivery/papers/Paper_1/Sharpe_Paper1_Spectral_Dimension_Flow.pdf`, SHA-256 `42da2082f86858f75771a06ef7767bbea59bf53bd2d27e20357b7a3d62cedf4e`;
- `delivery/papers/Paper_2/Sharpe_Paper2_Z5_Minkowski_Lapidus.pdf`, SHA-256 `5f010279d4cea5ea5db4abac3834759c2cf15e2cb084d56b7beefa0b1d98263f`.

Paper 1 §§6.1, 7.1 supplies pentagrid offsets, accepted integer labels, original-basis edges and level-dependent Fibonacci hopping, reconstructed as the **P3 source-equation model** in [PF-I2](PF_I2_SOURCE_PENTAGRID_GENERATOR_RECOVERY_2026_11_07.md). Paper 1 §7.4 explicitly describes an infrared regulator `m²=10⁻⁴`. The numerical code and exact patch selection used for the published results are *not* contained in the dissertation tar.

Paper 2 §8.2 Eq. (23) defines the finite evaluated quantity

\[
\zeta_{L,m}(s)=\frac1N\sum_{k=1}^N(\lambda_k+m^2)^{-s},
\quad R(-1/2)=0.8332\pm0.0018,\quad R(-1)=0.7371\pm0.0025,
\]

across `Ngrid∈{7,10,12,15,18,20,23,25}`, with source-reported `Nint∈{1550,3042,4324,6980,9950,12207,16435,19260}`. The table states source-coupled bonds link accepted integer sites differing by one of five original basis vectors and describes cross-direction bonds. As PF-I2 establishes, for **the same accepted Paper 1 P3 vertex set** all such edges already coincide with its rhombus edges; Paper 2 may use these inter-family bonds without adding edges. The original Paper 2 selection is not established.

Paper 2 §7.4 describes a **triangular** periodic benchmark with mean coordination approximately six, compared with Penrose mean degree approximately 3.9, and introduces an intermediate uniform-hopping *same-graph* Penrose operator. Paper 2 Eq. (15) factorizes \(\zeta_{fib}/\zeta_{per}=(\zeta_{fib}/\zeta_{uni})(\zeta_{uni}/\zeta_{per})\). The equality itself is an algebraic identity whenever denominators are nonzero; it cannot on its own certify a physical causal attribution to specific mechanisms. Reproducing each factor requires its own exact operator specifications.

**Unrecovered parameters:** Paper 2's specific accepted `Ngrid` vertex sets/cutoffs and phasons, the diagonal convention for `L=D−W` (weighted edge strength versus ordinary number of edges), exact comparator boundary graph and hopping strength, its mass value (Paper 1 states `10⁻⁴`, Paper 2's Eq. (23) does not restate it), and the original numerical program/environment. The Stage7/26 SU(2) Monte Carlo code is **a different experiment** and is not a substitute.

## 2. Exact theorem PF-I3.A: negative-integer zeta is a graph moment

For a finite undirected graph with symmetric zero-diagonal weighted adjacency matrix \(W\), let \(L=D-W\), \(D=\operatorname{diag}(d_v^D)\), and assume the regulator \(m^2>0\) renders \(L+m^2I>0\). If \(\lambda_k\) are eigenvalues of \(L\), then

\[
\boxed{\zeta_{L,m}(-1)=m^2+\frac1N\sum_v d_v^D}
\]

holds exactly by the trace identity, without a spectral calculation. Likewise,

\[
\boxed{\zeta_{L,m}(-2)=m^4+2m^2\overline{d^D}
 +\frac1N\left[\sum_v(d_v^D)^2+2\sum_{e=\{u,v\}}w_e^2\right].}
\]

The second equation follows by expanding \(\operatorname{Tr}(L+m^2I)^2\), since the cross term \(\operatorname{Tr}(DW)\) vanishes for \(W_{vv}=0\). In particular:

- **Weighted-strength diagonal:** \(d_v^D=\sum_{u\sim v}w_{uv}\), so \(\zeta(-1)=m^2+\frac2N\sum_e w_e\). This is the standard diffusion graph Laplacian and annihilates the constant vector.
- **Count-degree diagonal:** \(d_v^D=\#\{u:W_{vu}>0\}\), so \(\zeta(-1)=m^2+2|E|/N\), *independent of Fibonacci hopping weights*. For \(0<w_e\le1\), its lowest eigenvalue is strictly positive on a connected graph containing weak edges, and its row sum need not vanish.

**Consequences:** At `s=-1`, a numerical eigenvalue computation cannot reveal anything about the off-diagonal Fibonacci distribution beyond how that distribution enters the chosen diagonal. At `s=-2`, exact weighted second moments offer an additional source-operator fingerprint. For every full N-mode regulated finite spectrum, \(\zeta(0)=1\) exactly. Paper 2's approximate `R(0)=1.01` in the §7.2 summary therefore requires clarification (e.g. graph mode exclusions, rounding, interpolation or other conventions); it is not an exact result of the printed full-spectrum finite zeta definition.

## 3. Conditional source-normalization exclusion PF-I3.B

Use the **reported approximate** mean degrees \(d_{QC}\simeq3.9\) and \(d_{tri}\simeq6\). In the *candidate* interpretation in which `D` is ordinary degree on each graph, the comparator has unit-strength triangular edges, and the regulator is the `m²=10⁻⁴` explicitly stated by Paper 1,

\[
\boxed{R(-1)=\frac{3.9+10^{-4}}{6+10^{-4}}=0.650005833\ldots\ne0.7371.}
\]

For the **weighted-strength** Penrose diagonal with the printed hopping convention \(t_A=1,\;t_B=\varphi^{-2}<1\), the same conditional unit-strength triangle comparator gives \(\overline d_{QC}^{(w)}\le\overline d_{QC}^{(c)}\simeq3.9\), hence **also** \(R(-1)\lesssim0.65001\). Thus that entire unit-strength-triangle normalization family fails to match the reported `R(-1)` under the stated approximate coordination and mass assumptions. This is a statement about the **specified model assumptions**, not a disproof of the original data: the actual periodic edge weights, graph and mass are not authenticated.

If the *count-degree Penrose* hypothesis and six-valent weighted triangular reference were assumed but a single global periodic conductance \(t_{per}\) were left free, matching the reported \(R(-1)=0.7371\) would instead require
\[
\boxed{t_{per} = \frac{(3.9+10^{-4})/0.7371-10^{-4}}6\simeq0.88184016.}
\]
If \(t_{per}=1\) were fixed instead, the required squared mass would be \(\simeq1.98783\), vastly different from Paper 1's `10⁻⁴` (but Paper 2 has not authenticated the mass used). These explicit values identify **what source normalization must be recovered**.

## 4. Exact theorem PF-I3.C: \(\zeta(-1/2)\) is not a one-loop determinant

Paper 2 Eq. (21) displays \(\Gamma^{(1)}=\frac12\log\det(-\Delta+m^2)\) and Eq. (22) invokes \(\zeta'(0)\). For any finite positive \(L+m^2I\),

\[
\boxed{\frac1N\log\det(L+m^2I)=-\zeta_{L,m}'(0)}
\]

is the corresponding exact determinant identity (up to overall factors and a separately specified renormalization scale). By contrast,
\(\zeta(-1/2)=N^{-1}\sum_k\sqrt{\lambda_k+m^2}\) is a **square-root spectral moment**, not the determinant.

Counterexample: two positive **shifted** spectra `(1,9)` and `(4,4)` both give normalized \(\zeta(-1/2)=2\); their normalized log determinants are \(\log3\ne\log4\). The original unshifted operators can be taken as positive matrices by choosing any fixed \(0<m^2<1\). **Therefore** the quoted 16.7% difference at \(\zeta(-1/2)\) does not mathematically imply a 16.7% difference in \(\Gamma^{(1)}\). No statement is made here about whether a separate physical quantity intentionally uses the square-root energy sum; that would require its own specified action, spectrum and interpretation.

The continuum issue remains independent: finite graph spectral moments do not establish four-dimensional Yang–Mills existence/mass gap, a correct interacting gravitational fluctuation operator, or a UV-finite continuum determinant.

## 5. Reproducible finite source-equation controls (not Paper 2 replication)

`research/scripts/verify_pf_i3_spectral_moments.py` imports the separately authenticated Paper 1 **source-equation reconstruction** (`verify_pf_i2_pentagrid.py`), and on its explicit two circular-rhombus-centroid cutoff patches compares three P3 diagonal/weight interpretations against deterministic **equal-vertex-count** triangular and square disk-like site selections. The controls have equal **N**, but not inherently matched physical area, boundary, Hodge weights, or Paper 2 original configuration. The script explicitly also reports two *optional* normalizations: equal convex-hull vertex area with a `1/h²` lattice scaling, and an **illustrative spectral mean-matching scale** (not a claim of physical equivalence).

All numerics below use the *borrowed Paper 1* mass `m²=10⁻⁴`, not a recovered Paper 2 parameter.

| P3 patch | P3 graph | Triangular control | P3 weighted-strength / triangular unit-edge \(R(-1/2),R(-1)\) | P3 count-degree-minus-weighted / triangular unit-edge \(R(-1/2),R(-1)\) |
|---|---|---|---|---|
| radius 6.5 | 186 V / 345 E | 186 V / 507 E | 0.69504, 0.50982 | 0.83110, 0.68048 |
| radius 12 | 616 V / 1185 E | 616 V / 1755 E | 0.70705, 0.52767 | 0.82182, 0.67522 |

**One matching moment does not validate a model.** The smaller count-degree sample gives \(R(-1/2)=0.8311\), close to the source's `0.8332`, but simultaneously gives \(R(-1)=0.6805\) rather than `0.7371` against the declared unit-strength triangular control. The source's full two-point numerical definition is therefore a more discriminating test than simply obtaining `0.8332` under one choice.

**One-parameter calibration test (not original reproduction).** Instead use the weighted-strength P3 and choose exactly **one** global triangular-control bond strength to force the *reported* \(R(-1)=0.7371\) using the trace theorem. The required strengths are `0.69165` (186 V) and `0.71587` (616 V); these then predict **without a second fit** \(R(-1/2)=0.83573\) and `0.83566`, respectively, and \(R(-2)\simeq0.6482,0.6508\). Their closeness to the reported `0.8332` at \(-1/2\) shows that *the ratio pair alone does not uniquely identify a specific extra coupled-Z5 mechanism*: a reconstructed source P3 model with one comparator scale can produce similar moments. This is a **sensitivity/falsification control**, not source-code recovery or confirmation of the reported results. The source value `0.8332±0.0018` is not exactly reproduced.

**Spectral-trace-matching test (also not physical).** If each unit triangular comparator is rescaled to match the *P3 spectral first moment*, then \(R(-1)=1\) by construction and the weighted P3 \(R(-1/2)\) becomes `0.973415` (186) and `0.973345` (616), rather than the raw `0.695045` and `0.707049`. This illustrates **normalization sensitivity**, and cannot be used as a physical renormalization prescription without an independent action/metric theorem.

**Fibonacci hopping control on identical P3 graph:** replacing all P3 hopping with the finite sample's own mean edge strength holds \(\zeta(-1)\) exactly fixed for the weighted-strength diagonal; the weighted-to-uniform \(R(-1/2)\) is approximately `0.98717` (186) and `0.98947` (616). The graph coordination, absolute scale and hopping redistribution are separable questions at the exact moment level; these small finite samples do not establish the large-source Lapidus explanation.

The exact source-reported eight sizes and `Ngrid=25` results **are not reproduced**. Neither finite-scalar comparison is an interacting SU(2) or continuum calculation. The physical control would require matched domain, graph parameterization, area, edge-energy/metric, and regulator/coupling scales.

## 6. Concrete next proof gate and falsification criteria

The source-authentication obligation PF-G0 is now sharpened to a **finite parameter-identification record**:

1. Recover Paper 2's exact `Ngrid` accepted vertex/cutoff rule and phason parameters; verify `Nint=19260` from these rules independently, rather than matching it by a tuned cutoff.
2. Establish whether Paper 2 uses the already interlinked Paper 1 P3 rhombus-edge graph or a distinct accepted graph; publish precise original-index vertex and edge sets and all hopping levels.
3. Establish `D` by determining whether \(L\mathbf1=0\) and whether \(\operatorname{Tr}L=2\sum_e w_e\) or `2|E|` on the published numerical matrix. Require a **mass-parameter citation** for Paper 2, not an unlabelled import from Paper 1.
4. Identify the actual periodic comparator (triangular/square, finite domain/boundary and conductance) and **first reproduce the exact \(s=-1\) trace identity** before checking \(s=-1/2,-2\) or complex dimensions.
5. Evaluate both the normalized square-root moment and the correctly specified \(\zeta'(0)\)/logdet on the same matrices before claiming a one-loop effective-action percentage. Require an actual field/geometry fluctuation operator before claiming gravitational UV or continuum physical inference.
6. Once the exact scalar source comparison is reproducible, separately investigate its transfer to gauge-invariant interacting quantum dynamics and spectral exclusion; cubic and square remain controls.

## 7. Evidence protocol and execution

- [Independent executable test](../scripts/verify_pf_i3_spectral_moments.py): finite P3 and periodic operators, eigenvalue spectra, exact trace-moment cross-checks, `m²`, exact s=0, geometric/mean-spectrum normalization variants, and single-ratio calibration. Requires Python, NumPy and SciPy. `verify_pf_i2_pentagrid.py` must be available alongside it (same directory in GitHub). Shapely is not required for this calculation.
- [Regression tests](../tests/test_pf_i3_spectral_moments.py): 12 unit tests, all pass.
- [Compact source/finite evidence summary](../evidence/PF_I3_SPECTRAL_MOMENT_SUMMARY_2026_11_07.json): exact trace restrictions, both patches and representative control ratios; the complete 806-line evidence JSON, logs, code dependency and SHA-256 manifest are persisted in Library. All numbers can be regenerated by running the verifier with `--output ... --summary-output ...`.
- Source originals and full digest-pinned evidence package are preserved in Library `/The Singular Boundary/Proof Audits/PF I3 Spectral Operator 2026-11-07/`. The original PDFs are not re-committed or overwritten.

**The previous PF-I0/I1/I2 source corrections and their original files remain preserved without erasure.** The Observatory should add exact-result nodes and leave PF-G0, P0–P5, PF-G0–G5, T0–T5, OS, and gravity proof goals **OPEN**. No Git branch proliferation or public Observatory deployment is required.
