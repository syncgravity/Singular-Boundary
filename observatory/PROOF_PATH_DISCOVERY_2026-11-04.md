# Proof-path discovery — 2026-11-04

**Status:** limited source-derived cross-theorem inference with one new **conditional** formal-coefficient corollary; mathematical review remains required. No continuum mass-gap theorem.

## Sources independently consulted

- `R3_CUBICAL_SU2_GAUSS_HAMILTONIAN_REFERENCE_2026-10-31.md` (original-link Gauss Hamiltonian).
- `R3_CUBICAL_SU2_FULL_PHYSICAL_STRONG_COUPLING_GAP_2026-10-31.md` (full finite graph physical gap, F-dependent).
- `R3_CUBICAL_SU2_FINITE_TRANSFER_POSITIVITY_2026-10-31.md` (finite symmetric transfer).
- `R3_IR_3D_QUANTITATIVE_THRESHOLD_AND_CONTINUUM_SCALING_AUDIT_2026-11-04.md` (Yarotsky regime and physical scaling).
- `R3_IR_HISTORY_AWARE_CONNECTED_HULL_LIFT_AND_OVERLAP_WEIGHTS_2026-11-03.md` (exact history reconstruction).
- `R3_IR_SOURCE_MULTIGRADING_LINKED_HISTORY_2026-11-03.md` (source order and spin selection).
- `R3_IR_LOCAL_FIRST_TAME_2026-11-03.md` (local-first graded tame norm).
- `R3_IR_EXACT_LENGTH_SPIN_MOMENT_TAME_2026-11-03.md` (prior moment result).
- `R3_IR_GAUGE_INVARIANT_WILSON_BILINEAR_COUNTEREXAMPLE_2026-11-02.md` and `R3_IR_ANCHORED_BILINEAR_HIGHEST_WEIGHT_COUNTEREXAMPLE_2026-11-02.md` (norm-specific obstructions).
- `R3_IR_LINKED_CLUSTER_SUBTRACTION_PHYSICAL_OBSTRUCTION_2026-11-03.md` (physical low-energy channel feedback).
- `R3_IR_ROOT_INDEPENDENT_FACE_WARD_2026-10-31.md` (intrinsic marginal identity).
- `R3_IR_THREEFACE_FULL_FOURTH_ORDER_POISSON_2026-11-01.md` and `R3_IR_FOURFACE_CONNECTED_S4_EXACT_2026-11-01.md` (already completed finite low-order cases; **do not duplicate**).
- `R3_IR_FORMAL_CONNECTED_GEVREY8_2026-11-01.md` and `R3_IR_CONNECTED_GEVREY2_OPTIMAL_SCALAR_2026-11-01.md` (different connected-L² scalar majorants; do not conflate with L¹ local-first result).

## New conditional consequence (requires hypothesis-level proof review)

### Proposition — local-first formal Gevrey-1 upper bound

On each finite open original-link square strip, assume the coefficientwise matrix Peter–Weyl hypotheses underlying the local-first tame result, with `κ>0`, `σ≥0`, fixed `0<a0≤a_e≤a*` and constants `C_cross,C_nest` from that record. Let `S(z)=Σ_(n≥1) z^n S_n` be the **formal** homogeneous-source solution for fundamental single-plaquette magnetic leaves, lifted to history channels, where `S_n=Σ_(i+j=n) B_hist(S_i,S_j)` for n≥2. Define `a_n=||S_n||_{L^(1)}`, and `M=||S_1||_{L^(1)}`.

The source multigrading theorem guarantees that `S_n` has at most spin label `n` on any original link. Since the local-first norm sums nonnegative sector nuclear norms *inside each fixed anchor*, coefficientwise it follows that

`||S_n||_{L^(2)} ≤ (n+1) ||S_n||_{L^(1)} = (n+1)a_n.`

Apply the symmetric `L^(1) × L^(2) -> L^(1)` tame estimate to each ordered decomposition `i+j=n`:

`a_n ≤ Σ_(i=1)^(n−1) [C_cross+C_nest((j+1)+(i+1))] a_i a_j`

`     = [C_cross+C_nest(n+2)] Σ_(i=1)^(n−1) a_i a_(n−i).`    (★)

**In particular**, for `D=3 C_cross+12 C_nest`, induction gives

`a_n ≤ M^n D^(n−1) (n−1)!` for all n≥1.    (†)

Proof: with the induction hypothesis,
`Σ_i a_i a_(n−i) ≤ M^n D^(n−2) Σ_i (i−1)!(n−i−1)!`.
For n≥2, the elementary inequality

`Σ_i (i−1)!(n−i−1)! ≤ 3(n−2)!`

holds (equivalently `Σ_(k=0)^(m) 1/C(m,k)≤3`, m=n−2). Since `n+2≤4(n−1)`, (★) gives
`a_n ≤ M^n D^(n−2) [3C_cross+12C_nest](n−1)! = M^n D^(n−1)(n−1)!`.

For homogeneous singleton fundamental source `M` is independent of the number of strip faces because each face anchor belongs to one singleton history only and all local edges have uniformly bounded weights; thus (†) is **volume-independent coefficientwise**. The statement is conditional on the previously recorded analytic tame estimates and has not been separately proven from first principles in this investigation.

### Logical limits

1. This is a **formal Gevrey-1 bound** in a specified *local-first L¹ matrix PW norm*, not an analytic coupling-radius theorem. A factorial upper bound alone does not imply nonzero convergence radius, much less `λ=1`.
2. It does not automatically improve or contradict the previous **Gevrey-2** estimate in a *different* norm and scalar majorant; comparing their exact norms, retained histories and normalizations is necessary.
3. It does not bound the interacting physical spectrum, derive the P3 Wilson current, prove Borel summability, or yield a four-dimensional continuum limit.
4. The source degree cap does **not** make the unrestricted fixed-grade Banach map bounded: the latter's high-spin and linked-channel counterexamples have different quantifier structure.
5. This construction is confined to finite open straight square strips; no transport to the cubic 3D regulator or historic Penrose action is justified.
6. The project-wide original-source-byte provenance and duplicate-claim acceptance gate remain outstanding.

## Decisive incompatible interfaces

- **Coupling:** Cubic periodic weak-interaction stability demands `16z<β_Y` with `z=4/g0⁴`; asymptotically free `g0(a)→0` forces `z→∞`. A fixed-`β_Y` stability theorem cannot cover that trajectory.
- **Lattice/sector:** The original-link straight-strip moment estimate does not automatically apply to a 3D cube; the same-root face-coordinate Wigner lower bounds do not establish a physical Gauss-invariant 3D no-go.
- **Nonlinear quotient:** Discarding disconnected-support physical outputs breaks the exact Poisson recurrence. History reconstruction retains them.
- **Continuum:** A source-certified refining cubic chain geometry and a finite transfer-positive Hamiltonian are complementary ingredients, not the interacting renormalized continuum theory.

## Proposed next controlled experiment

1. Reproduce the local-first tame inequality directly from the original coefficientwise Peter–Weyl matrices and exact original-link spin networks for the smallest genuinely nested cases; verify the inherited inequality before treating (†) as theorem-grade.
2. Compute source multigraded coefficient vectors from the **existing** exact three- and four-face archives; report their L^(1), L^(2) moment ratios and compare against the (n+1) upper cap. Reuse archived results; do not start duplicate fourth-order inversions.
3. Test whether a **factorial-normalized** Borel recursion can be controlled after history-compatible low-energy channel reconstruction. This is the actual missing analytical improvement over (†), not an assertion of convergence.
4. Independently audit the cubic regulator and physical coupling conventions before transporting any strip estimate to 3D.

## Diagram data

Nine typed candidate links with status, explicit source records, model compatibility and missing implications are stored in `observatory/proofpaths.js`. The structural checker confirms IDs, sources, scopes and status vocabulary, but does **not** certify theorem truth.
