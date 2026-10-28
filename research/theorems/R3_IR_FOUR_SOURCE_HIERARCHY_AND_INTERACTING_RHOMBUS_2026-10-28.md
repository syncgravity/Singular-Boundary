# R3-IR — Four-source transfer identity, hierarchy obstruction, and first interacting SU(2) composite-mode mixing

**October 28, 2026. Mathematical evidence classification:** theorems I–IV below are **independently proved under their explicitly finite-model hypotheses**. The existence of a regulator- and volume-uniform Penrose interacting mass gap, and the proposed nonperturbative all-word source-inserted bound, remain **OPEN**. No Monte Carlo simulation or alteration of historical source bytes.

## 0. Source audit and correction of the proposed next step

Historical `SCALAR_WILSON_IR_AND_COMPLETENESS.md` (October 26) already proves the completeness of the full Wilson trace algebra and finite-volume observable frame implications. The repository's `R3_IR_SINGLE_TRACE_COMPLETENESS_AND_COMPOSITE_OBSTRUCTION_2026-10-28.md` strengthens this to density of the *linear span of single traces*, and gives a four-state counterexample to propagating decay from two generating observables to their product. Those are historical inputs, not discoveries here.

**Correction:** The previously proposed `CM-4`, control of a fourth-order connected cumulant, is an optional *diagnostic/intermediate result*, **not a logically necessary gate**. Complete single Wilson traces already supply a sufficient family without fourth-cumulant control. Nor can any fixed-order generator-cumulant control, by itself, yield the full spectral gap. Theorems II and III below give exact reasons. The next *dynamical* proof target must control source insertions over unbounded Wilson-word complexity (or supply a genuinely model-derived alternative to that control), not merely establish fourth-order clustering.

## I. Exact two-time fourth-cumulant decomposition

Let `K=H−E0≥0` be a finite-volume self-adjoint Hamiltonian with simple normalized vacuum `Ω` and stationary Euclidean time `τ_t` represented by `e^(−tK)`. Choose four bounded real gauge-invariant **multiplication** observables `A,B,C,D` (so they commute within each time slice), and center each with its vacuum mean, writing `a=A−ω(A)` etc. Define

`C_{a,c}(t)=<aΩ,e^(−tK)cΩ>`, and
`C_{ab,cd}(t)=<Q(ab)Ω,e^(−tK)Q(cd)Ω>`.

Then the joint fourth cumulant of `a(0),b(0),c(t),d(t)` is exactly

```
κ4(a0,b0,ct,dt) = C_{ab,cd}(t)
                         − C_{a,c}(t) C_{b,d}(t)
                         − C_{a,d}(t) C_{b,c}(t).                  (I.1)
```

**Proof.** For four centered commuting-at-each-slice classical Euclidean variables, the fourth joint cumulant is their four-product moment minus its three pair partitions. The same-time partition subtracts `ω(ab)ω(cd)`, leaving `C_{ab,cd}`. The other pairings give the two displayed cross-time products. All terms have a well-defined transfer representation, with order of time slices fixed. QED.

For identical centered `a` at both times,

```
κ4(a0,a0,at,at) = C_{a²}(t) − 2 C_a(t)².                     (I.2)
```

`C_{a²}(t)=<Q(a²)Ω,e^(−tK)Q(a²)Ω>≥0` is a **positive spectral Laplace transform**, while `κ4` need not be positive. A fourth-cumulant exponential estimate *plus* two-point decay bounds gives a bound on composite covariance, with rate `min(m4,m_ac+m_bd,m_ad+m_bc)`. A fourth-cumulant bound **alone** cannot yield a composite spectral bound. This is a proved algebraic implication, not a new interacting decay estimate.

## II. Exact SU(2) one-rhombus four-source correlator

Take one open spatial rhombus with four SU(2) link variables, equal electric weights `a>0`, Wilson magnetic coefficient `b≥0`, and full gauge projection. Its physical link Hilbert space is unitarily equivalent to the SU(2) class-function space of a single loop holonomy `U`, with orthonormal characters `|j>=χ_j(U)`, `j=0,1/2,1,...`. The Hamiltonian is the exact self-adjoint Jacobi operator

```
H_b |j> = [4a j(j+1)+b]|j> − (b/2)(|j+1/2>+|j−1/2>),      (II.1)
```

where `|−1/2>` is omitted. The source is the normalized real fundamental Wilson trace `p=χ_{1/2}/2`, and the exact Clebsch–Gordan identity is `p²=(χ_0+χ_1)/4`.

### Theorem II.1 — electric-only fourth cumulant

At `b=0`, `Ω=|0>`, `QpΩ=|1/2>/2` and `Qp²Ω=|1>/4`. Consequently

```
C_p(t)    = 1/4  exp(−3a t),
C_{p²}(t) = 1/16 exp(−8a t),
κ4(p0,p0,pt,pt) = 1/16 exp(−8a t) − 1/8 exp(−6a t).      (II.2)
```

**Proof.** `H_0χ_j=4a j(j+1)χ_j`, normalized character orthogonality, and the source product decomposition give the positive correlations. Apply (I.2) for the cumulant. QED.

The fourth cumulant is negative for all `t≥0`, with asymptotic decay rate `6a`, while the centered composite source `p²` has a *positive* correlation with rate `8a`. Thus **the fourth-cumulant exponent need not be an actual composite excitation energy**. Reading one as the other would be a spectral error.

### Theorem II.2 — explicit interacting leakage into the lowest channel

For sufficiently small `|b|/a`, the isolated ground and first excited eigenpairs of (II.1) are analytic by bounded Kato perturbation theory. Their exact expansions are

```
E0(b)    = b − b²/(12a) + O(b³/a²),
E1/2(b)  = 3a+b+b²/(30a) + O(b³/a²),
Δ(b)     = E1/2−E0 = 3a+7b²/(60a)+O(b³/a²).              (II.3)
```

Write `Ω_b` and `ψ_b` for normalized analytic ground and first-excited eigenvectors, with phases chosen continuously from `|0>` and `|1/2>`. Then

```
<ψ_b,p²Ω_b> = b/(15a) + O((b/a)²),
|<ψ_b,Q_b p²Ω_b>|² = b²/(225 a²) + O((b/a)³).          (II.4)
```

**Proof.** In the character basis the diagonal perturbation `bI` shifts all eigenvalues equally at first order and off-diagonal `−bp` couples only adjacent half-integer spins. Standard second-order Rayleigh–Schrödinger sums give `E0^(2)=−1/(12a)` and `E1/2^(2)=1/(30a)`. The first-order eigenvector derivatives are

```
Ω'_0 = (1/(6a)) |1/2>,
ψ'_0 = −(1/(6a)) |0> + (1/(10a)) |1>.
```

Since `p²|0>=(|0>+|1>)/4` and `p²|1/2>=(2|1/2>+|3/2>)/4`, differentiation gives

```
d/db <ψ_b,p²Ω_b>|_0
  = [−1/(6a)+1/(10a)]/4 + [1/(6a)]/2
  = 1/(15a).
```

All calculations are exact finite-rank perturbation coefficients of a bounded perturbation of an operator with compact resolvent; they do **not** rely on a truncated numerical spectrum. The two lowest eigenvalues remain isolated and ordered for sufficiently small `|b|/a`. QED.

**Consequence.** At *every sufficiently small nonzero* `b`, the composite positive covariance `C_{p²,b}(t)` contains a strictly positive contribution

`[b²/(225 a²)+O((b/a)³)] exp(−Δ(b)t)`.

Since this is the lowest excited channel and its weight is nonzero, `−lim_{t→∞}t^(−1)log C_{p²,b}(t)=Δ(b)≈3a`, whereas at `b=0` the composite-source rate equals `8a`. Hence taking `b→0` and `t→∞` in the *effective decay rate* does not commute. A finite-order perturbative expansion at fixed t cannot alone determine a uniform long-time composite spectral bound. This is a genuine **interacting finite-rhombus** source-mixing theorem, not the Penrose continuum gap.

## III. Any fixed-order temporal cumulant hierarchy can hide a slow mode

Fix an arbitrary integer `k≥2`, binary variables `x_1,...,x_k∈{±1}`, parity `q=∏_i x_i`, and parameters `0<δ<1`, `0<ρ<1`. On the `2^k` configurations define

```
T_{k,ρ,δ}(x,y) = δ 1_{x=y} + (1−δ) 2^(−k)[1+ρ q(x)q(y)].       (III.1)
```

**Theorem III.1.** The matrix is symmetric, has strictly positive **entries and eigenvalues**, and is stochastic with uniform stationary distribution. On Walsh characters `χ_S(x)=∏_{i∈S}x_i`, its eigenvalues are

```
λ_∅=1,
λ_[k]=δ+(1−δ)ρ,
λ_S=δ for every nonempty proper S ⊊ [k].                       (III.2)
```

Thus its gap in units of the time spacing `a_t` is `−a_t^(−1)log[δ+(1−δ)ρ]→0` as `ρ→1`, while each coordinate `x_i` has fast correlation `δ^n`.

**Theorem III.2 (fixed-order hierarchy obstruction).** For *any mixed two-time joint cumulant of coordinate variables* with total insertion order `M<2k`, involving at least one coordinate at time 0 and at least one at time n≥1, there is a finite constant `C_M`, depending only on M and **not on ρ**, such that

```
|κ_M| ≤ C_M δ^n.                                               (III.3)
```

Yet the fully composite k-coordinate observable `q` satisfies

```
C_q(n) = [δ+(1−δ)ρ]^n.                                        (III.4)
```

For k=3, the exact six-source cumulant with three distinct coordinates at each time is

```
κ6(x1(0),x2(0),x3(0),x1(n),x2(n),x3(n))
       = λ_[3]^n − 3 δ^(2n) + 2 δ^(3n).                         (III.5)
```

**Proof.** The Walsh characters diagonalize the kernel because the constant, full-parity and proper nonempty characters are orthogonal under the uniform measure; the eigenvalue formula proves strict operator and entrywise positivity. The two-time joint law after n steps is the uniform product law plus the Walsh cross terms `λ_S^n χ_S(x)χ_S(y)`. Any joint moment of fewer than `2k` coordinate insertions contains fewer than k factors on at least one time slice, so it cannot couple to the full-parity `χ_[k]` channel and is independent of `λ_[k]`. Its difference from the `δ=0` reference (where all such mixed moments factorize) is at most `δ^n`. By the moment–cumulant partition formula and telescoping the products over partition blocks, the mixed cumulant is bounded by `C_M δ^n`, for example `C_M=Σ_{π∈Part(M)} |π|!`. The full k-fold product at each time is q and has eigenvalue `λ_[k]`; direct moment-partition counting for k=3 yields (III.5). QED.

**Scope:** Theorem III is an abstract finite-state, strictly operator-positive transfer model, **not** an SU(2) Wilson counterexample. It proves that no fixed finite truncation of generator-cumulant bounds can imply a gap *from positivity and algebra generation alone*. The actual SU(2) interacting system may possess extra dynamical structure; deriving and exploiting it is the open problem.

## IV. Corrected next proof dependency and precise research target

The earliest open source-inserted R3-IR obligation is **not** a standalone four-cumulant inequality. It is a model-derived, physically normalized and scale-controlled estimate for a source family with unbounded Wilson-word complexity, or a genuinely derived reduction from simpler operators that propagates the control to such a family. Theorem III rules out propagation based solely on a fixed finite cumulant hierarchy and positivity. Theorem II exhibits a nontrivial interacting mode that is invisible in the corresponding electric-only composite correlator.

**Candidate next useful lemma, open:** For actual Penrose SU(2) Wilson transfer with the historically verified geometric couplings and reflection-positive temporal seam, derive an exact *word-resolved* transfer recursion for 

`C_{W_γ}(t)=<QW_γΩ,e^(−t(H−E0))QW_γΩ>`

including the source's full character mixing and all induced multi-loop terms. Prove a nontrivial, **model-derived** bound on its generated coefficient remainder over one spatial/temporal blocking step in a norm whose constants depend explicitly on word length and volume. Proving only the recursion is an intermediate algebraic result; a gap would require an independently derived all-scale contraction *with a common physical energy rate* and control across winding/center sectors, without assuming gap-strength mixing. Try low-complexity mixed words and the exact one-rhombus transfer first to test whether the norm closes; reject a nonclosing word-only scheme if it generates unsummable words.

The genuine continuum R3-IR/R2 theorem additionally requires nontrivial renormalized observables, physical time, and uniformity in both volume and spatial refinement. No such theorem is claimed here. The fixed-scale small-magnetic local-state stability result does not cover the physical strong-magnetic trajectory.

## V. Provenance, test, and preservation

The deterministically executed scripts `verify_four_source.py` and `verify_interacting_rhombus.py` use only exact fractions and symbolic expressions. `EXACT_CERTIFICATE.json` and `RHOMBUS_CERTIFICATE.json` record the checked formulas. No historical MCMC reruns, source simulations, mass fitting, or replacement results. Historical file hashes and original source archives remain untouched. Existing research source: historical `SCALAR_WILSON_IR_AND_COMPLETENESS.md` and the preceding audit `R3_IR_SINGLE_TRACE_COMPLETENESS_AND_COMPOSITE_OBSTRUCTION_2026-10-28.md`.

**Ledger:** I — independently proved exact finite-model identity; II — independently proved electric and weakly interacting one-rhombus spectral statements; III — independently proved abstract strictly positive transfer obstruction; IV model-derived interacting Penrose all-word source recursion and uniform infrared bound — OPEN. The earlier claim that CM-4 is a necessary first gate is **corrected/superseded**, not silently deleted.