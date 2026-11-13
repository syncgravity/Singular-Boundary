# PF 34:55 parastichy count and explicit 3D lift — correction

**2026-11-12 · finite construction audit and correction to the recent exploratory graph experiment**

## Disposition

The finite **34:55 count is already established by the radial golden-angle/Delaunay construction** recorded in `research/scripts/verify_pf_conceptual_parastichy_2026_11_07.py`. The earlier script established dominant neighbour-index offsets. This correction strengthens the verifier: it now checks that every possible lag-(k) edge occurs in the selected annulus and that the lag graph has exactly (k) connected residue-class chains.

This is a finite synthetic construction, not yet a source-authenticated derivation from the coupled-ℤ^5 Conway-worm generator. Keep those two claims separate.

## 1. Exact mechanism

Let
[
\varphi=\frac{1+\sqrt5}{2},\qquad \alpha=\varphi^{-2},\qquad
x_n=\sqrt n\,e^{2\pi i n\alpha}.
]
For Fibonacci numbers (F_k),
[
F_k\alpha-F_{k-2}=(-1)^k\varphi^{-k},\qquad k\ge3.
]
In particular,
[
34\alpha-F_7=-\varphi^{-9},\qquad
55\alpha-F_8=+\varphi^{-10}.
]
Thus the 34- and 55-step angular increments have opposite small signed residuals after removal of their integer turns. These are the two counter-winding parastichy directions.

## 2. Exact finite chain-count result

The verifier constructs the Delaunay graph of (N=1600) points and restricts edges to both endpoints in each annulus. The central interval is the zero-based array-index interval ([400,800)), corresponding to sequence labels (n=401,ldots,800).

| Lag (k) | Delaunay edges | All possible lag-(k) pairs (800-400-k) | Connected residue chains |
|---:|---:|---:|---:|
| 34 | 366 | 366 | **34** |
| 55 | 345 | 345 | **55** |
| 89 | 311 | 311 | 89 |

The equality of the observed edge count and the number of all possible pairs proves that every pair ((i,i+k)) in the annulus is a Delaunay edge for these three lags. The lag-(k) graph is therefore exactly
[
G_k=\bigl(\{400,\ldots,799\},\{(i,i+k):400\le i<800-k\}\bigr).
]
Its connected components are the (k) residue classes modulo (k), each a path. Hence the count is not inferred from a frequency peak alone: it is an exact finite graph decomposition.

At the next radial scale, ([800,1300)), the leading lags are 55, 89 and 144, with respectively 445, 411 and 356 edges—again exactly (500-k) possible edges. The parastichy counts advance with scale; 34:55 is not a universal all-radius pair.

The earlier annulus ([200,400)) similarly gives 34 and 55 chains, with 166 and 145 edges, respectively.

## 3. Controls

| Construction | Dominant lags in ([400,800)) | Interpretation |
|---|---|---|
| Golden angle (\alpha=\varphi^{-2}) | 34, 55, 89 | Opposite-signed Fibonacci parastichies |
| Opposite irrational orientation (1/\varphi) | 34, 55, 89 | Same chain counts, reversed winding |
| Rational (8/13) | 5, 8, 13 | Finite rational pitch does not reproduce 34:55 |
| Deterministically phase-shuffled | 10, 37, 39 (small counts) | No comparable coherent hierarchy |

The rational control is important: the finite Paper 3 (8/13) pitch is not interchangeable with the irrational golden-angle construction.

## 4. Explicit three-dimensional lift

The radial construction has a direct, non-folding 3D lift once an independent longitudinal scale and clock are declared:
[
\Gamma_n=\left(
\sqrt n\cos(2\pi n\alpha),\,
\sqrt n\sin(2\pi n\alpha),\,
hn
\right),\qquad t_n=nT,
]
with (h,T>0) chosen independently and product Euclidean metric
[
d\ell^2=dx^2+dy^2+ds^2.
]

For each residue (r\pmod k), the corresponding lag-(k) parastichy strand is
[
\Gamma_{k,r}(q)=\Gamma_{r+qk}
]
over the (q)'s lying in the annulus. Its increments are:
- radial coordinate: (\sqrt{r+(q+1)k}-\sqrt{r+qk}), so the strand widens;
- angular coordinate modulo full turns: (2\pi(-1)^k\varphi^{-k});
- longitudinal coordinate: (hk);
- clock time: (kT).

Thus the 34 and 55 residue chains lift to two families of **discrete radially expanding 3D helices with opposite winding**. This is not a constant-radius circular helix. It is a legitimate explicit geometric lift of the synthetic parastichy construction, but its longitudinal scale, clock and metric are declared model data—not derived from Papers 2–4.

## 5. Correction to the recent fivefold directed-walk experiment

The previous exploratory answer applied an exact-return test to paths composed of the five original ℤ^5 basis steps. That test is about exact transverse closure in that separate cyclotomic graph. It does **not** constrain Delaunay parastichy offsets in the golden-angle point set and therefore does not refute the 34:55 chain count.

The claimed 100-seed/300,000-step walk statistics in that answer were not produced by a reproducible script in that turn and are withdrawn. The associated asserted degree histogram, 75/25 basin split, and Paper 4 failure-band compatibility should not be used as evidence. The quadratic equivariant map and the ad hoc direction-selection rule are separate candidates, not the construction that produced 34:55.

The Paper 2/Paper 4 window/shift normalization issue also remains a separate source-reconciliation obligation; it is not an input to the golden-angle Delaunay calculation.

## 6. Updated evidence boundary and next objective

**Established:** exact Fibonacci angular identity; finite Delaunay lag counts; exactly (k) residue-class chains for the checked annuli; opposite 34/55 winding; explicit discrete 3D lift with independent (h,T).

**Still open:** identify a source-derived map from the authentic five Conway-worm families / coupled-ℤ^5 acceptance generator to the golden-angle radial sequence or prove a different source-native construction yields the same two parastichy counts. The source-specific observer clock and physical metric remain open. The original 34:55 finite construction is not itself a Yang–Mills spectral or mass-gap result.

**Verifier:** `research/scripts/verify_pf_conceptual_parastichy_2026_11_07.py`, now 74 deterministic checks. It checks the Fibonacci identity, all lag-edge counts, exact residue-chain component counts across three annuli, the explicit longitudinal lift, rational (8/13) aliasing and shuffled controls. Run with NumPy and SciPy installed.

**Source context:** `research/geometry/PF_CONCEPTUAL_3D_CONWAY_HELICAL_RECONSTRUCTION_2026_11_07.md`, `research/geometry/PF_G0_QUOTIENT_DOUBLE_SPIRAL_SOURCE_AUDIT_2026_11_07.md`, and the Observatory helical-observer concept index. All source-to-Conway-worm and physical continuum proof gates remain OPEN.
