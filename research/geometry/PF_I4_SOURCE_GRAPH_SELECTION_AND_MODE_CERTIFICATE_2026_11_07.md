# PF-I4 — Original graph selection, mode counts and degree-normalization audit

**Research checkpoint:** November 7, 2026 (America/Denver). **Object:** Paper 1 §7.2, Paper 2 §8.2, Paper 4 §§2–3, 6–7, and their implication for the source-authentication gate PF-G0. **Status:** exact conditional incompatibility theorems, finite independent P3 controls and source-byte provenance correction. **Not:** reproduction of the unpublished source graph/zeta computation; authentication of coupled-Z5 physical gauge dynamics; demonstration of gravity ultraviolet finiteness or nontrivial four-dimensional Yang–Mills existence/mass gap. All canonical continuum gates **OPEN**. Preserve previous PF-I0–I3 files as historical records with an explicit correction.

## 1. Source comparison and original-byte correction

The original supplied tar file is `Sharpe_dissertation_v10.7.tar.gz`. Directly extracted **native members** of the tar have the following SHA-256 identifiers:

| Native source PDF | Original tar-member SHA-256 | Historical record(s), scoped accurately |
|---|---|---|
| Paper 1 | `2b11426161c32c41a36fd816e3fcd668c7f1b44ee9cf73be1a62638fe6d46be5` | PF-I2 calls `7c0585fa990bb2a762c869665287835bbdb6e07edeb55e9adfe54fe84f9eddea` the source digest (**its backing PDF is not located**). PF-I3 lists `42da2082f86858f75771a06ef7767bbea59bf53bd2d27e20357b7a3d62cedf4e`, a processed copy present and verified page-equivalent to the native PDF. |
| Paper 2 | `2bfc52c29140149d483b8e1b980143b05a43d21fe0e2098516efb1615b7e50e7` | PF-I2 correctly records the native digest. PF-I3 lists `5f010279d4cea5ea5db4abac3834759c2cf15e2cb084d56b7beefa0b1d98263f`, a processed copy present and verified page-equivalent. |
| Paper 4 | `871bf58f9d5adf66b2ad7d115f8031dd0c36efc18b147ae91caa48e6865d54ab` | PF-I3 lists `03152f9c17f78b3a6f6f752f230f80eb63d70df440bb96209e1137137185e734`, whose backing PDF was **not located** in this audit. Another processed copy with SHA `741660e2654a6891c95b25ef689faa16915c32356f537c14d0402fc32ee1ede5` is present and page-equivalent to native Paper 4. |

The **three present native/processed PDF pairs** have differing bytes but *all pages* have identical PyMuPDF text, pixel-identical 1.2× renders and identical `pdftotext -layout` output. Thus the *mathematical passages rechecked here* are unchanged in the present copies. The older unlocated PDF hashes, notably PF-I2 Paper1 `7c0585…` and PF-I3 Paper4 `03152…`, remain unverified as **bytes and contents**; their source identity must not be assumed. Earlier source hash labels must not be represented as native archive bytes without a direct check.

An inventory of the current canonical repository's Git tree found **3,315 entries, including 2,760 blobs and 697 Python scripts**. No filename identifies the original executable that produced Paper 2/4's eight-size graph-zeta tables. Related preserved scripts include `Phase_III_CutProject_Recomputation/audited_penrose.py` (blob `9e1ed6ec2089125304d8db7eb550865452b073b8`) and Stage7/26 source files. The former is a **later** 2D cut-and-project reconstruction using a different offset convention; the latter is 2+1D SU(2) Monte Carlo. Neither is established as the original Paper 2/Paper 4 graph-zeta generator. A filename scan is not proof that no generically named script exists.

## 2. Exact PF-I4.A — the stated degree distribution cannot have the stated mean

Paper 4 §6.1, verified in the native PDF (printed page 5), gives `(f5,f4,f3)=(5.0%,65.9%,28.6%)` together with mean unweighted degree `⟨d⟩=3.748`. Section 6.2 explicitly states that the remaining **0.5%** have **degree at least six**.

For any common vertex population satisfying these four fractions and with the remainder of degree ≥6,

\[
\begin{aligned}
\langle d\rangle&\ge3 f_3+4 f_4+5 f_5+6(1-f_3-f_4-f_5)\\
&=6-3f_3-2f_4-f_5=3.774.
\end{aligned}
\]

Even allowing each of the three quoted percentage figures independently to be rounded to the nearest **0.1 percentage point** (absolute fraction uncertainty `0.0005`), the smallest possible mean is

\[
6-3(0.2865)-2(0.6595)-(0.0505)=\boxed{3.771}>3.748.
\]

This is an **exact conditional incompatibility** of the stated fractions and unweighted mean on the *same* graph population, not proof that any original spectral eigenvalue is wrong. It may be resolved by reporting different populations, degree versus weighted-strength conventions, or a correction to one of the reported figures. Paper 4 §6.2's additional identification `D=√(⟨d⟩/6)=0.786` would itself imply `⟨d⟩=6×0.786²=3.706776`, different from its reported 3.748; the displayed degree factor therefore also requires its precise convention.

**Source implication:** The degree partition cannot presently certify the `D` diagonal or the geometric degree-deficit factor used to interpret `R(-1)`.

## 3. Exact PF-I4.B — neighbor-closed finite interiors are all-or-nothing

Paper 1 §7.2 (printed page 11) gives a more precise numerical selection than previously recorded: “restrict to vertices whose tile distance from the tiling center falls within 35% of the maximum, and further require that all neighbors of each interior vertex are also interior.” It does **not** state whether the second condition is a one-pass erosion of the initial radius candidate, a repeated closure, or a check against a different ambient graph.

**Lemma.** Let `G=(V,E)` be connected and finite. If `S⊆V` is nonempty and contains every neighbor of each of its vertices, then `S=V`.

**Proof.** Choose any `v∈S`. Along a path from `v` to any `w∈V`, every next vertex is a neighbor of the previous one and must also be in `S`. Connectivity yields `w∈S` for every `w`. **QED.**

Consequently, the published language cannot describe an *iterated* strict-neighbor-closed proper “interior” of one connected finite graph. A coherent finite algorithm may start with a 35%-distance candidate and **remove once** vertices with neighbors outside it; the resulting retained set typically has boundary neighbors outside the final set. Alternatively the condition may be tested against the uncut infinite graph or a separately constructed complex. The original implementation is **unrecovered**.

### Independently reconstructed finite P3 controls (not the source Ngrid algorithm)

Using the source equations from PF-I2 and an **illustrative** BFS tile distance from the retained vertex nearest the origin, with the floor of 35% of the maximum distance, one-pass filtering gives:

| Independent sample | Full `V/E` | max BFS tile distance | 35% candidate | One-pass core | Core vertices with neighbors outside core | Components of core |
|---|---:|---:|---:|---:|---:|---:|
| Radius 6.5 | 186/345 | 10 | 28 | 14 | 10 | 1 |
| Radius 12 | 616/1185 | 18 | 96 | 68 | 20 | 1 |

These are **method-behavior tests**, not a match to the published `Ngrid=7→1550` or `25→19260`. They demonstrate why the one-pass candidate and the final neighbor-closed set must not be confused. In both finite samples the retained core remains connected.

## 4. Exact PF-I4.C — the reported mode-count differences cannot all be standard zero-mode removals

Paper 2 §8.2 and Paper 4 §7.2 give **full `Nint`** at `Ngrid=(7,10,12,15,18,20,23,25)`:

`[1550,3042,4324,6980,9950,12207,16435,19260]`.

Paper 4 §3's separate zeta-prime table instead gives

`[1550,3042,4324,6979,9947,12206,16434,19255]`.

Subtracting gives `[0,0,0,1,3,1,1,5]`.

For the **standard positive-weight graph Laplacian** `L_w=D_w-W`, where `D_w(v)=Σ_{e∋v}w_e` and all occupied edges have `w_e>0`,

\[
\langle f,L_wf\rangle=\sum_{e=\{u,v\}}w_e|f(u)-f(v)|^2.
\]

Therefore `dim ker L_w = # connected components`. Every nonempty graph has at least **one** zero mode; each **connected** graph has **exactly one**. Under the three simultaneous assumptions (i) the two paper tables refer to exactly the same full graph at each size, (ii) `N` in Paper 4 §3 is obtained *solely by deleting all zero modes*, and (iii) the standard positive-weight Laplacian is used, the first three zero differences are **impossible**, and differences `3` or `5` would require as many disconnected components. If the source graphs were all connected, only difference `1` would be possible at every size.

For the other candidate `L_c=D_count-W` with every `0<w_e≤1`, a connected graph with **at least one edge of weight less than one** has **zero** zero modes, because

\[
\langle f,L_cf\rangle=\sum_e w_e|f(u)-f(v)|^2
+\sum_{e=\{u,v\}}(1-w_e)(|f(u)|^2+|f(v)|^2),
\]

which is strictly positive unless `f=0`. The reconstructed connected 186/616-site P3 controls have `dim ker L_w=1` but `dim ker L_c=0`; this depends on the operator definition, not the word “Laplacian.”

The published N differences **cannot presently be attributed solely to zero modes** without the actual source matrix and selection data. They could reflect different graph selection, eigenvalue thresholds, distinct operator diagonals or misreported counts. The present calculation does not choose among these alternatives.

## 5. Exact status of the two claimed graph constructions

Paper 1 §6.1 specifies P3 rhombus-edge adjacency through integer-label differences `±e_j`; Paper 2 §8.2 describes the coupled-Z5 graph using such steps. PF-I2 proved that **if the accepted vertex set is exactly the same**, every permitted nearest-basis pair is already an edge in the reconstructed P3 graph.

However, Paper 4 §7.1 explicitly names **two Laplacians**—a tile-edge 2D P3 graph and a coupled-Z5 graph using all five basis directions with up to ten neighbors—and reports close but not identical `s=-1/2` results across three sizes. The original accepted vertex sets, edge-selection and diagonal definitions for the two matrices are not provided. Thus mathematical equivalence of the finite graphs and their spectra **is neither established nor excluded**: a difference requires a different vertex selection, edge rule, diagonal, weight assignment, or finite boundary convention. The source claim of two operators remains a source claim, not an independently authenticated pair of matrices.

## 6. Target for the next source-authentication certificate

The following per-size machine-readable items would settle the current ambiguity with no further interpretive choice:

- **Vertex provenance:** all five integer labels and any 2D/4D projections; `Ngrid`; source pentagrid offsets and phason; original acceptance/window or 35% interior selection and the order of neighbor filtering.
- **Edge provenance:** each oriented original-basis endpoint pair and `j,k` Fibonacci-family level; edge conductance; whether the 2D and coupled operators share the selected labels and all basis pairs.
- **Operator identity:** a verified diagonal `D`, `L1` row sums, normalized trace `Tr L/N`, `Tr L²/N`, positivity and exact zero-mode count for each graph; explicit mass `m²`.
- **Reference identity:** periodic triangular/square control vertices and edges, weights, physical matching and zero-mode rule; eigenmode counts and normalization denominators.
- **Spectral fingerprint:** reproduce the source `R(-1)` directly from `Tr L`, then `R(-1/2)`, `R(-2)`, and the source-reported `ζ'(0)` and mass-dependent relative determinant **on those same matrices**; retain code hash and input snapshot.

**Acceptance condition:** the actual eight-size source operator must be deterministically reproducible from archived source or authenticated matrices; source-interpretation ambiguities must be resolved by those bytes, not by fitting one plotted ratio. **Current state: OPEN.** The published finite data and prior PF-I0–I3 controls remain evidence, not certification of an interacting coupled-Z5 Yang–Mills vacuum or continuum gap.

## 7. Reproducibility / preservation

- `verify_pf_i4_source_selection.py`: exact rational degree-partition bounds, full Paper2/Paper4 `N` table comparison, source-PDF tar-member hashes, finite PF-I2 graph BFS/one-pass source-selection tests and Wilson-independent connectivity zero-mode arguments.
- `test_pf_i4_source_selection.py`: nine passing independent regression tests; small and large P3 finite sample assertions.
- `PF_I4_SOURCE_CORE_EVIDENCE.json`: full strict machine-readable outcomes (original tar bytes verified where supplied).
- Source original archive user-provided, **not re-uploaded to Git**. Historical code blobs and older PF-I2/I3 report versions remain preserved; provenance errata should be attached rather than silently rewriting old source digests.

**No original Paper2/Paper4 full graph matrix recovered. No proof gate closed.**
