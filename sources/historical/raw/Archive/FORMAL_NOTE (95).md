# R3 on nested *genuine Penrose rhombus-prism* patches — relative repair and conditional exterior cost

Date: October 27, 2026. **Status**: exact nested geometric/cellular audit and constructive local Bianchi word bound for two selected supports; exploratory finite-volume SU(2) MCMC; **no arbitrary-support or ambient-uniform Wilson measure theorem**.

## A. Geometric provenance

`direct_cut_project.py` is the unmodified Z^5 window-first patch generator extracted from the user-uploaded `Phase_III_Cut_and_Project_Recomputed.zip`. It uses normalized offset gamma and accepts whole rhombi by Z^5 neighbor-square incidence. Independent Phase III tests previously verified it against a pentagrid construction on tested windows. `extended_audit.py` constructs spatial disks at physical radii 5, 6.5, 8, 10 and crosses each with the **three-edge periodic Euclidean time circle**. Rhombi per slice: 70, 122, 196, 338. 3D prism cells: 210, 366, 588, 1014. These are genuine *two-dimensional Penrose rhombus spatial slices*, not a three-dimensional icosahedral quasicrystal.

The same fixed local inserted faces are identified in each larger patch by the original five-integer Z^5 vertex labels. The code checks the nested vertex/face inclusion, oriented cellular equations ∂1∂2=∂2∂3=0, bounded degree, and canonical hashes of every local interacting link, face, and boundary link.

## B. Two distinct nonuniform temporal supports

1. `overlapping14`: at time 0 insert temporal plaquettes around the union of boundaries of the central face and one adjacent face; at time 1 insert those around the union of boundaries of the central face and a different adjacent face. Support contains exactly 14 faces. The affected local link set has 36 links. The retained action on those links has 62 adjacent retained faces plus the 14 insertions; the immediate exterior boundary has 89 links.
2. `star8`: at time 0 insert the four temporal faces incident on the temporal link through the four-valent central spatial vertex; at time 1 insert four temporal faces on a neighboring five-valent vertex's star. This is an eight-face time-nonuniform and spatially overlapping local support. The affected local link set has 25 links; 48 retained faces touch that set, and 71 exterior links enter those retained face words.

In both cases these counts and the **exact SHA-256 fingerprints of the canonical interacting neighborhoods** are identical for all four radii. A zero/one/two-shell expansion (through face-to-link incidence) has link counts 36/125/258 and 25/96/208 respectively. Because the fixed supports are well inside the smallest radius-five disk, these are identical local geometries, not a demonstration of a uniform bound over *all possible* growing supports.

## C. Exact curvature-rank conclusions and the limited nonabelian word theorem

The full 3-step prism disk's oriented face-boundary rank is `3E`, following the cellular homology of disk × S1. The modular column-rank calculations are performed over GF(1000003) on signed integer incidence columns; independent cellular Bianchi/row witnesses make the asserted *rank differences* exact over Q, not merely floating SVD guesses.

* For `overlapping14`, the projection of the 3-cell boundary map to the 14 inserted faces has rank 14. A constructive algorithm peels **all fourteen faces** via fourteen neighboring prism boundary identities. The signed abelianized face-chain length is at most fifteen. A separate substitution audit counts **at most seventeen conjugated retained plaquette holonomies** without permitting abelian cancellations (or their inverses), with all conjugating paths inside this fixed local cell neighborhood. The associated signed face-chain expressions are independently checked by direct boundary equality over integers. They involve 54 distinct retained faces. The pointwise Wilson-curvature comparison, for equal face couplings, is

      sum_{q∈Q} d(W_q) <= 35 sum_{p in 54 neighboring retained faces} d(W_p).

  This bound uses d(AB)^1/2 ≤ d(A)^1/2+d(B)^1/2 and the column occurrence bound. The value 44 is a verified nonabelian factor-occurrence bound for this *specific finite Q*, and stays unchanged as the surrounding disk grows. It is NOT a general bound 35 for arbitrary Q.

* For `star8`, the projection of the cell-boundary map to Q has rank 7, and exactly one independent curvature relation is added on inserting all eight faces. Four faces can be peeled sequentially by the local greedy algorithm; the other four form a temporal-plaquette star. The single temporal link through the central four-valent vertex meets **only those four inserted faces and no retained face**. It is therefore an exact independent normalized Haar SU(2) coordinate under the *retained* Wilson measure. It need not remain independent after insertion. The global curvature ranks are `rank D_R = 3E−1`, `rank D_all = 3E`, while the original local link ranks differ by one, giving **zero added exterior curvature rank**, for every tested radius. This is an actual nonabelian compact-Haar coordinate, not Gaussian linearization.

* On both supports, the exterior-rank increase is zero with the original local link set, and stays zero under one/two shells. The original small square prism example from the previous turns had a different, genuinely exterior-obstructed support: no generalization from the present favorable examples to all supports is justified.

## D. Exact conditional exterior-locality theorem (not the desired cost bound)

Fix either Q and its local links L. Let A denote the retained faces touching at least one link in L, B the exterior links participating in those face words, and f a function on SU(2)^B defined by the local conditional insertion ratio

      f(b) = [∫_{SU(2)^L} exp{-S_R^loc(u,b)-V_Q(u,b)} du]
             /[∫_{SU(2)^L} exp{-S_R^loc(u,b)} du].

All other retained faces depend exclusively on the exterior links and cancel inside the conditional ratio. The full partition-function identity is

      Z_1^{(R)}/Z_0^{(R)} = E_{ν_R}[ f(B) ],

where ν_R is the retained-cavity **exterior boundary marginal**. The canonical local face/link fingerprints are identical across the four radii, so f itself is **exactly identical** as a function of canonically matched boundary SU(2) variables. Only ν_R can change with ambient radius. This is a rigorous, exact ambient-locality statement and explains precisely why checking just collar size/word complexity does NOT bound the full insertion free energy.

For `overlapping14`, the nonabelian Bianchi identity also gives the exact deterministic inequality `V_Q ≤ 44 λ ∑_{p∈local R} d(W_p)` at equal couplings. Hence

      Z_1/Z_0 ≥ E_{μ0}[exp{-35 λ ∑_{p∈local R} d(W_p)}].

To deduce an ambient-uniform support bound it suffices, for example, to bound λ times the expected local retained curvature uniformly in radius (via Jensen), or to prove that the boundary marginal ν_R gives at least exp[-C|Q|] probability to a polynomially favorable repair event. **Neither input is currently proved** in the physical SU(2) ensemble. In particular there is no general *pointwise* polynomial conditional lower bound for arbitrary boundary assignments.

## E. Exploratory retained-cavity SU(2) sampling

`conditional_probe.py` samples the *correct retained-cavity action separately for each insertion Q*, using normalized unit-quaternion variables, link-local Metropolis sweeps and independent two-chain seed handling. For each radius and each λ=8,30, 2 chains use 180 burn-in sweeps and 8 samples 25 sweeps apart: 16 records per support/radius/coupling, 256 records total. The conditional minima for retained and inserted actions are approximated with a quaternion-normalized analytic-gradient L-BFGS-B method, with multiple restarts. No iteration-limit hits were recorded. These are **not certified global minima**, and two short chains do not provide a reliable finite-volume Gibbs equilibrium error analysis.

Diagnostic `Hopt = -log(mean(exp(-[estimated E1−estimated E0])))`:

| Radius | Q14 λ=8 | Q14 λ=30 | Q8 λ=8 | Q8 λ=30 |
|---|---:|---:|---:|---:|
| 5.0 | 6.012 | 5.376 | 2.662 | 2.463 |
| 6.5 | 5.787 | 5.086 | 2.193 | 2.416 |
| 8.0 | 4.811 | 4.453 | 2.129 | 2.372 |
| 10.0 | 5.936 | 5.274 | 2.749 | 2.557 |

The sampled values are order-one and show no monotone growth over these sizes, but some separate chain estimates differ substantially (especially for Q14 at λ=30). They do NOT establish uniform bounded exterior frustration, equilibration, a high-coupling asymptotic, or a limit as volume→∞. The primary scientific conclusion remains the **exact local conditional factorization**, not the small pilot MCMC.

## F. Decision

For these two *fixed* supports on genuine nested Penrose spatial disks, a bounded collar and bounded nonabelian word complexity persist through all four tested volumes, and the conditional function is exactly local after the neighborhood stabilizes. This verifies geometric feasibility in two concrete Penrose cases. It does **not** decide the all-support alternative. The remaining theorem requirements are either:

(i) establish a uniform local retained-curvature bound `sup_{V,p} λ E_{μ0}d(W_p) <= C` under comparable Wilson couplings (sufficient for the Bianchi-fillable class); or

(ii) construct a good-event / correlated-Haar transport argument controlling the boundary marginal on rank-changing and overlapping supports that do not admit a bounded filling.

Any proposed proof must be tested on long connected supports as well as these fixed local supports. Bounded vertex degree and finite local complexity alone do not ensure bounded-radius repair for all supports. The continuum Yang–Mills mass gap remains unproved.

## Reproduction

```
python extended_audit.py
python conditional_probe.py --radii 5 6.5 8 10 --lambdas 8 30 --samples 8 --burn 180 --stride 25 --chains 2 --maxiter 140
python summarize_probe.py
```

`certificate.json` contains per-radius incidence and rank results plus canonical locality hashes. `conditional_samples.json` contains the 256 pilot optimization records; `probe_summary.csv` contains aggregate diagnostics. `nested_audit.py` supplies the signed incidence and GF(p) rank primitives, and `direct_cut_project.py` is the unchanged audited geometric generator.
