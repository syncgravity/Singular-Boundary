# Boundary-local Peter–Weyl gradient estimate for disjoint adjacent intervals

**2026-11-01 | Finite open straight original-link SU(2) face chain | Precise local lemma.**

## Model and hypotheses

Use the intrinsic Peter–Weyl Hilbert norms `H_sigma(I)` from `R3_IR_INTRINSIC_PW_ANALYTIC_INVERSE_2026-11-01.md`. Let `I=[a,b]` and `J=[b+1,c]` be disjoint adjacent intervals of face coordinates in an **open straight chain**, with one common original link between the right endpoint of I and the left endpoint of J. Extend `f=f(U_I)`, `g=g(U_J)` to `T=I∪J`. Fix `sigma>sigma'>=0`, `delta=sigma-sigma'>0`.

Assume the physical original-link carré du champ uses orthonormal SU(2) invariant generators normalized by the spin-j Casimir `j(j+1)`, equivalently degree `l=2j` has `l(l+2)/4`. An original-link derivative on each one of these separate factors is a *single* left/right invariant derivative of its boundary face, with orientation-dependent sign. This exact statement applies to the standard straight open face-chain original-link coordinate representation; for other link incidence or additional common links, rederive the constant.

Define `b(delta)=sup_{l>=1} (sqrt(l(l+2))/2) exp(-delta*l)`.

## Lemma

```
||Gamma(f,g)||_{H_sigma'(T)}
    <= 3 b(delta)^2 ||f||_{H_sigma(I)} ||g||_{H_sigma(J)}
    <= [9/(4 e^2 delta^2)] ||f||_{H_sigma(I)} ||g||_{H_sigma(J)}.
```

**The constant is independent of |I|, |J| and |T|**, unlike the full-union general touching/overlap estimate.

For Haar-centered `Gamma(f,g)`, or with the projection `P0` inserted, the established free inverse yields

```
||K_T^{-1} P0 Gamma(f,g)||_{H_sigma'(T)}
    <= b(delta)^2 ||f||_{H_sigma(I)} ||g||_{H_sigma(J)}
    <= [3/(4 e^2 delta^2)] ||f||_{H_sigma(I)} ||g||_{H_sigma(J)}.
```

## Proof

The only original link that differentiates *both* disjoint supported functions is their shared boundary link `e_*`. Its derivative acts as a single normalized left/right generator `X_a` on the endpoint face of I and `Y_a` on the endpoint face of J. In the tensor-product Haar representation, with signs depending on the orientations,

`Gamma(f,g)=sum_{a=1}^3 sign_a (X_a f) tensor (Y_a g)`.

For each Peter–Weyl multi-degree `l` on I, an endpoint invariant derivative preserves the complete multi-degree, vanishes for endpoint degree zero, and has L2 operator norm no greater than `sqrt(l_boundary(l_boundary+2))/2`. Because `N(l)>=l_boundary`, the analytic-radius contraction obeys

`||X_a f||_{H_sigma'(I)} <= b(delta)||f||_{H_sigma(I)}`.

Likewise for `Y_a g`. Crucially, I and J are disjoint coordinate sets: the intrinsic Peter–Weyl norm of a simple tensor exactly factorizes,

`||h_I tensor k_J||_{H_sigma'(T)} = ||h_I||_{H_sigma'(I)}||k_J||_{H_sigma'(J)}`.

The triangle inequality over three generator directions proves the first bound. For `l>=1`, `sqrt(l(l+2))<=sqrt(3)l` and `sup_{x>0} x exp(-delta*x)=1/(e delta)`, yielding `b(delta)<=sqrt(3)/(2e delta)`. The previously established uniform free inverse `||K_T^{-1}P0||_{H_sigma'→H_sigma'}<=1/3` proves the Poisson estimate.

The bound was independently checked numerically for degrees 1–1000 at delta = 0.1, 0.25, 0.5, 1 and 2; the proof is analytic and does not rely on this finite check.

## What this does NOT establish

This lemma covers **disjoint adjacent** intervals. The full connected-score recurrence `R3_IR_FORMAL_CONNECTED_GEVREY8_2026-11-01.md` also permits **overlapping** intervals; for overlaps, `f g` is not a tensor product on disjoint coordinates, and the argument above does not apply. There are also questions about rooted summation of interval contributions, iterative radius budgets, and control of analytic norms of nonlinear score coefficients.

In particular, the balanced-tree radius-loss obstruction for the previous full-union constant is **not automatically removed** for the full recurrence, although this estimate removes its exponential-in-t factor for the disjoint-adjacent subcase. It proves no ordinary perturbative convergence, no lambda=1 interacting gap, no Penrose current theorem, and no continuum Yang–Mills mass gap.

**Next mathematical obligation:** derive an overlap-localized multiplier estimate or a connected-recursion reorganization which treats overlapping supports without an exponentially growing whole-union PW factor; then prove a closed global rooted majorant with a finite radius-loss budget.
