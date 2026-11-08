# PF-I3 — Paper 2 spectral-operator trace and determinant audit

> **PF-I4 SOURCE-PROVENANCE ERRATUM (2026-11-07; original record preserved below).** The archive-native PDFs inside `Sharpe_dissertation_v10.7.tar.gz` have SHA-256 **Paper 1** `2b11426161c32c41a36fd816e3fcd668c7f1b44ee9cf73be1a62638fe6d46be5`, **Paper 2** `2bfc52c29140149d483b8e1b980143b05a43d21fe0e2098516efb1615b7e50e7`, **Paper 4** `871bf58f9d5adf66b2ad7d115f8031dd0c36efc18b147ae91caa48e6865d54ab`. Earlier Paper 1/2 hashes in §1 refer to processed copies verified page-equivalent; the §1 Paper 4 hash `03152...` has **not** been traced to its backing PDF, although a different mounted Paper 4 copy with SHA `741660...` matches all original pages in text and rendered pixels. See [PF-I4 source-byte and mode-count certificate](PF_I4_SOURCE_GRAPH_SELECTION_AND_MODE_CERTIFICATE_2026_11_07.md). Do not describe unlocated historical hashes as archive-native or page-equivalent. No spectral ratio or continuum claim is promoted by this erratum.

**Date:** 2026-11-07 (America/Denver)  
**Research status:** exact finite scalar operator identities, conditional source-compatibility test, and independent illustrative P3/periodic controls. **NOT** independent reproduction of the unpublished Paper 2 numerical generator, its reported `Ngrid=25, Nint=19260` spectrum, a geometric/time reconstruction, a Yang–Mills interacting vacuum or gap, or gravitational UV finiteness. **PF-G0, P0–P5, PF-G0–G5, T0–T5 and gravitational proof gates remain OPEN** (the legacy T5 transfer record remains conditional).

## 1. Primary source and exact stated data

The user's original `Sharpe_dissertation_v10.7.tar.gz` contains:

- `delivery/papers/Paper_1/Sharpe_Paper1_Spectral_Dimension_Flow.pdf`, SHA-256 `42da2082f86858f75771a06ef7767bbea59bf53bd2d27e20357b7a3d62cedf4e`;
- `delivery/papers/Paper_2/Sharpe_Paper2_Z5_Minkowski_Lapidus.pdf`, SHA-256 `5f010279d4cea5ea5db4abac3834759c2cf15e2cb084d56b7beefa0b1d98263f`.
- `delivery/papers/Paper_4/Sharpe_Paper4_Conformal_Boundary_CC.pdf`, SHA-256 `03152f9c17f78b3a6f6f752f230f80eb63d70df440bb96209e1137137185e734`; Paper 4 already reports both `ζ′(0)` and mass-dependent relative determinant ratios, independently investigated in §8 below.

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
5. **Independently reproduce the already reported Paper 4 `ζ′(0)` and mass-relative determinant results** on source-matched matrices, alongside Paper 2 `ζ(-1/2)`; do not mistake the absence of original code for the absence of a published calculation. Require an actual field/geometry fluctuation operator before claiming gravitational UV or continuum physical inference.
6. Once the exact scalar source comparison is reproducible, separately investigate its transfer to gauge-invariant interacting quantum dynamics and spectral exclusion; cubic and square remain controls.

## 7. Evidence protocol and execution

- [Independent executable test](../scripts/verify_pf_i3_spectral_moments.py): finite P3 and periodic operators, eigenvalue spectra, exact trace-moment cross-checks, `m²`, exact s=0, geometric/mean-spectrum normalization variants, and single-ratio calibration. Requires Python, NumPy and SciPy. `verify_pf_i2_pentagrid.py` must be available alongside it (same directory in GitHub). Shapely is not required for this calculation.
- [Regression tests](../tests/test_pf_i3_spectral_moments.py): 12 unit tests, all pass.
- [Compact source/finite evidence summary](../evidence/PF_I3_SPECTRAL_MOMENT_SUMMARY_2026_11_07.json): exact trace restrictions, both patches and representative control ratios; the complete 806-line evidence JSON, logs, code dependency and SHA-256 manifest are persisted in Library. All numbers can be regenerated by running the verifier with `--output ... --summary-output ...`.
- Source originals and full digest-pinned evidence package are preserved in Library `/The Singular Boundary/Proof Audits/PF I3 Spectral Operator 2026-11-07/`. The original PDFs are not re-committed or overwritten.

**The previous PF-I0/I1/I2 source corrections and their original files remain preserved without erasure.** The Observatory should add exact-result nodes and leave PF-G0, P0–P5, PF-G0–G5, T0–T5, OS, and gravity proof goals **OPEN**. No Git branch proliferation or public Observatory deployment is required.

## 8. Cross-paper correction: Paper 4 already evaluates \(\zeta'(0)\) and a relative determinant

**This section supersedes any suggestion above that the author did not calculate a logarithmic determinant channel.** Paper 4 §§2–3 reports \(\zeta'_{QC}(0)/\zeta'_{Per}(0)=0.646\pm0.006\) across eight system sizes; this is explicitly different from Paper 2's \(R(-1/2)=0.8332\pm0.0018\). The original numerical source and eigenvalues underlying the claimed \(0.646\) are not in the supplied dissertation archive, and this review **does not independently certify** those values.

Paper 4 Eq.(1) defines \(\zeta_m(s)=N^{-1}\sum_k(\lambda_k+m^2)^{-s}\), Eq.(2) defines

\[
\Gamma_{\mathrm{Paper4}}(m^2)=-\frac12\zeta_m'(0)-\frac12\zeta_m(0)\log m^2.
\]

### Exact theorem PF-I3.D: Paper 4's expression is a relative log determinant

For finite strictly positive retained eigenvalues \(\lambda_k>0\) (paper: zero modes removed), \(m^2>0\), and \(\zeta_m(0)=1\), the equation simplifies **exactly** to

\[
\boxed{\Gamma_{\mathrm{Paper4}}(m^2)=\frac1{2N}\sum_{k=1}^N\log\left(1+\frac{\lambda_k}{m^2}\right).}
\]

It is a **mass-relative** determinant per retained mode: \(\frac1{2N}\log\det(I+L/m^2)\). This resolves the apparent extra \(-\frac12\log m^2\) term in Paper 4 as a normalization relative to the mass reference; it is not simply the unnormalized absolute \(\frac1{2N}\log\det(L+m^2 I)\). Thus the previous PF-I3.C theorem remains true: the square-root moment \(\zeta(-1/2)\) cannot determine either determinant.

For two finite positive retained spectra \(Q\) and \(P\), with their means computed on each own retained set,

\[
\lim_{m^2\to0}\frac{\Gamma_Q(m^2)}{\Gamma_P(m^2)}=1,
\quad
\lim_{m^2\to\infty}\frac{\Gamma_Q(m^2)}{\Gamma_P(m^2)}=
\frac{N_Q^{-1}\operatorname{Tr}L_Q}{N_P^{-1}\operatorname{Tr}L_P},
\]

provided both have strictly positive means and no unreconciled zero-mode fraction. **Proof:** as \(m^2\to0\), \(\log(1+\lambda/m^2)=-\log m^2+\log\lambda+o(1)\), so the common divergent term dominates both per-mode means. As \(m^2\to\infty\), \(\log(1+\lambda/m^2)=\lambda/m^2+O(m^{-4})\), hence the ratio approaches the first trace moment ratio. **QED.** The endpoint behavior is a generic mathematical property of *any* positive pair of finite graph spectra, not an independent proof of an interacting quantum field, renormalization-group flow or geometrically unique universality mechanism. These limits do **not** assert the ratio is monotone for arbitrary spectra.

Paper 4 §10.1 reports \(\Gamma_{QC}/\Gamma_{Per}\) of **0.959**, **0.927**, **0.816**, and **0.739** at squared mass \(10^{-4}\), \(10^{-2}\), \(1\), and \(100\), respectively. The stated limiting behavior toward 1 (small mass) and roughly the first trace-moment ratio (large mass) is explained by the identity above without requiring Penrose-specific spectral properties. The ratio at finite intermediate mass still depends on the whole spectrum and can contain authentic geometric information; the endpoint statement alone cannot distinguish it.

### A one-calibration control reproduces the reported mass flow without original code

Using **only** the PF-I2 published-equation P3 weighted-strength Laplacian on the earlier 186/616-vertex *illustrative* patches, and the respective equal-N triangular site patches, choose a **single** periodic edge conductance from Paper 2's \(R(-1)=0.7371\) by the exact trace formula, and **exclude one zero mode from each connected graph**, as Paper 4 says its calculation does. No Paper 4 mass-flow datum is fitted. The following independently calculated comparison results:

| Squared mass \(m^2\) | Paper 4 reported ratio | PF-I3 control, 186 vertices | PF-I3 control, 616 vertices |
|---|---:|---:|---:|
| \(10^{-4}\) | 0.959 | 0.959475 | 0.959957 |
| \(10^{-2}\) | 0.927 | 0.927654 | 0.928987 |
| \(1\) | 0.816 | 0.817501 | 0.819697 |
| \(100\) | 0.739 | 0.739106 | 0.739167 |

Maximum absolute difference from the four source-rounded values is ~**0.00151** (186 vertices) and **0.00370** (616 vertices). The 616-site control's independently computed \(\zeta'(0)\) ratio at the borrowed mass \(10^{-4}\) is **0.6540**, near but not equal to Paper 4's reported eight-size mean \(0.646\pm0.006\); the 186-site control gives **0.6262**. **None of these constitute reproduction of the unpublished original Paper 4 experiment.** They demonstrate non-uniqueness: a finite ordinary P3 graph and a one-parameter periodic normalization can mimic the reported relative-determinant flow very closely, without certifying the proposed coupled-Z5 geometric or interacting Yang–Mills mechanism. A confirmed source-specific mechanism must therefore be identified by more discriminating, physically normalized observables.

### Exact source-table mode-count discrepancy: PF-I3.E

Paper 2 Eq.(23) and Paper 4 §7.2 print the same full eight-size \(N_{int}\) array:

`[1550, 3042, 4324, 6980, 9950, 12207, 16435, 19260]`.

But Paper 4 §3's separate \(\zeta'(0)\) extension uses:

`[1550, 3042, 4324, 6979, 9947, 12206, 16434, 19255]`.

The pairwise differences are **[0, 0, 0, 1, 3, 1, 1, 5]**; the largest discrepancy is five retained sites or modes. Paper 4 §2 says zero modes are removed, so mode exclusion is a possible explanation, but the paper does **not** supply an eigenvalue list, connectivity/zero-mode count or filtering rule establishing that these differences are precisely zero modes. This must remain an **OPEN source-provenance issue**, especially because normalized \(\zeta(0)=1\) is applied with N taken to be the retained mode count.

The original Paper 4 numerical result is **present in the source**; what remains absent is the executable generator/weights/mode-selection and an independent reproduction. Nothing in this addendum certifies its reported 35% \(\zeta'(0)\) ratio, its asserted one-loop gravitational finiteness, the paper's spectral-triple continuation or a Yang–Mills mass gap.

**New reproducibility files:** `research/scripts/verify_pf_i3_relative_logdet.py`, `research/tests/test_pf_i3_relative_logdet.py` and `research/evidence/PF_I3_PAPER4_RELATIVE_LOGDET_EVIDENCE_2026_11_07.json`. A 7-test local suite checks Eq.(2), asymptotic endpoints, source-table deltas and the four mass-flow finite calculations; together with the original PF-I3 suite there are **19 passing tests**. Source-original PDFs remain unchanged; the enlarged v2 archive is preserved separately in Library, with both research snapshots retained.
