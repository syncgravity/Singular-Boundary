# Three-slab localized SU(2) transfer-overlap comparison: exact theorem, obstruction, and open uniformity step

Date: 2026-10-27. Fourth branch of *Compare Continuum Mass Gaps*. Scope: arbitrary **nonstationary** three-slab positive compact-SU(2) temporal Wilson transfer operators on a finite spatial Penrose rhombus disk, under the same transfer-factorization assumptions as the previous `R3_nonstationary_extension` note. The result is an **exact localized overlap inequality**; it does **not** prove that its localized penalty is volume-uniformly bounded.

## 1. Setting

Let `H=L²(SU(2)^E)` be the spatial-link Hilbert space (or its gauge-invariant subspace). For each slab t=0,1,2, let `A_t` be the completed positive self-adjoint trace-class transfer operator and `B_t` the cavity operator, differing only by deletion of temporal plaquettes `Q_t`. Spatial potentials may vary with t but are identical between `A_t` and `B_t` within a given slab. Define

`z_t = product_{q in Q_t} z(lambda_q)`, where `z(lambda) = ∫_{SU2} exp(-lambda d(g)) dg >0`.

Peter–Weyl gives the exact convolution order `C_lambda >= z(lambda) P_0`, and hence

`D_t := A_t-z_t B_t >=0`.

For the physical finite-volume Wilson transfer representation, `Z_+ = Tr(A_0 A_1 A_2)>0` and `Z_- = Tr(B_0 B_1 B_2)>0`. Products of three arbitrary positive matrices need not have positive trace, so positivity of the *physical* traces is an additional property of the positive integral kernels.

## 2. Exact three-slab localized negative-bridge inequality

For positive self-adjoint `X,Y`, define `J(X,Y)=(XY+YX)/2`, a self-adjoint operator that need not be positive. Put

`J_0=J(A_1,A_2)`, `J_1=J(A_2,B_0)`, `J_2=J(B_0,B_1)`.

Telescoping the products, using cyclicity of trace and the fact that `D_t` is self-adjoint, yields the **exact identity**

```
Z_+ - (z_0 z_1 z_2) Z_-
 = Tr(D_0 J_0) + z_0 Tr(D_1 J_1) + z_0 z_1 Tr(D_2 J_2).
```

Let `J_t^-` denote the positive operator equal to the negative spectral part of `J_t`. Define

```
E_loc = Tr(D_0 J_0^-)
      + z_0 Tr(D_1 J_1^-)
      + z_0 z_1 Tr(D_2 J_2^-).
```

Since `D_t>=0`, `Tr(D_t J_t)>=-Tr(D_t J_t^-)`, hence

`Z_+ + E_loc >= (z_0 z_1 z_2) Z_-`.

Dividing by the positive physical partition functions gives

\[
\boxed{\frac{Z_+}{Z_-}\ge\frac{\prod_{q\in Q}z(\lambda_q)}{1+E_{\rm loc}/Z_+}.}
\]

This inequality is **exact**, nonperturbative, and holds for every finite ambient volume, any time-dependent spatial and temporal retained-face masks represented by positive transfer factors, and arbitrary overlapping temporal deletions.

### Single-slab deletion, commuting outer transfers

If `Q_0=Q_2=∅`, then `D_0=D_2=0` and

`Z_+-z_1 Z_-=Tr(D_1 J(A_2,A_0))`.

If `[A_0,A_2]=0`, then `J(A_2,A_0)=A_2A_0>=0` and `E_loc=0`. Thus

\[
\boxed{Z_+/Z_-\ge z_1}
\]

for **arbitrary nonstationary middle-slab completed masks**, and arbitrary (possibly different) commuting positive outer transfer operators. This extends the stationary three-slab result but is not a theorem for general noncommuting outer masks.

More generally, the exact lower bound `Z_+/Z_- >= product z_t` holds whenever each *local bridge pairing* `Tr(D_t J_t)>=0`. It suffices (but is not necessary) that each `J_t` is positive on the range of `D_t`.

## 3. Actual q-link localization using Peter–Weyl positivity

Let `H_t^Q=L²(SU(2)^{Q_t})` be the tensor factors of spatial links whose temporal plaquettes were deleted in slab t; `H_t^{\bar Q}` is the remaining link Hilbert space. In temporal gauge, the positive temporal convolution factor is a tensor product of one-link central SU(2) convolutions. Let `C_t^Q=⊗_{e∈Q_t} C_{lambda_e}`, `P_t^Q=⊗_{e∈Q_t}P_0`, and `z_t=∏ z(lambda_e)`. Define the *local spectral difference*

\[
\mathscr D_t=C_t^Q-z_tP_t^Q\succeq0.
\]

It vanishes on the tensor product of all trivial Peter–Weyl representations and is positive on the nontrivial modes. Factor the unaffected positive temporal convolutions, the spatial Wilson potential, and the gauge projection into a bounded/trace-class-compatible operator `L_t` so that

\[
D_t=L_t^*(\mathscr D_t\otimes I_{\bar Q})L_t.
\]

The factorization follows from the tensor-product convolution structure, `C_t^{\bar Q}>=0`, and gauge projection (which commutes with central convolution). For any self-adjoint bridge operator `J_t`, define its **local reduced bridge**

\[
\mathscr B_t=\operatorname{Tr}_{\bar Q}(L_tJ_tL_t^*),
\]

an operator on the q_t affected spatial-link coordinates only. Then

\[
\boxed{\operatorname{Tr}(D_tJ_t)=\operatorname{Tr}_{Q_t}(\mathscr D_t\mathscr B_t).}
\]

In particular, since `\mathscr D_t>=0`,

\[
\operatorname{Tr}(D_tJ_t)\ge
-\operatorname{Tr}_{Q_t}(\mathscr D_t\mathscr B_t^-).
\]

Thus one may replace the global `E_loc` above by the **q-link-reduced** quantity

\[
\mathfrak E_Q=
\operatorname{Tr}_{Q_0}(\mathscr D_0\mathscr B_0^-)
+z_0\operatorname{Tr}_{Q_1}(\mathscr D_1\mathscr B_1^-)
+z_0z_1\operatorname{Tr}_{Q_2}(\mathscr D_2\mathscr B_2^-).
\]

The exact bound `Z_+/Z_- >= (∏z)/(1+\mathfrak E_Q/Z_+)` follows. This is a genuine *localized overlap inequality*: the nontrivial spectral test lives on at most `q` SU(2) link coordinates. **Its reduced bridge states still depend on the entire ambient system through partial trace; locality of the operator's domain does not imply uniform boundedness of its negative part.**

The trace-class manipulations can be justified first in finite Peter–Weyl cutoffs and then by trace-norm convergence of the smooth compact SU(2) convolution kernels. The partial trace exists for the trace-class products involved.

## 4. Explicit positive-kernel obstruction

Even strictly positive integral kernels and a positive convolution spectrum do **not** imply that `Tr(D_t J_t)>=0` in a nonstationary three-factor trace. The independent exact rational two-state example in `bridge_counterexample.py` uses the finite group Z2 (not SU2):

```
C=[[1,7/10],[7/10,1]], P0=(1/2)[[1,1],[1,1]], z=17/10
D=C-zP0=(3/20)[[1,-1],[-1,1]] >=0
A0=diag(1,2) C diag(1,2)
A2=diag(2,1) C diag(2,1)
```

All three completed transfer kernels have strictly positive entries and are positive definite. Nevertheless,

\[
\operatorname{Tr}(A_0 C A_2)-z\operatorname{Tr}(A_0P_0A_2)=-39/125<0.
\]

The *single-slab* three-factor monotonicity fails in this positive-kernel, positive-definite-convolution toy model. It is not a Wilson SU(2) counterexample, but proves that **these two generic positivity properties alone are insufficient**. Any full SU(2) result must exploit further SU(2)-specific gauge identities or quantitative control of the local reduced bridge's negative spectral mass.

## 5. Consequence for the actual exterior Gibbs barrier

The prior two-sided conditional Haar-ball theorem gives, for insertion-link count `k`, incidence bound `nu`, and actual cavity exterior marginal `nu_0`, the rigorous comparison

\[
\mathbb E_{\nu_0}e^{-\lambda\Delta(v)}\ge b_{k,\nu}(\lambda)\,Z_+/Z_-,
\]

where `b_{k,nu}(lambda)>=c_{k,nu}(1+lambda)^(-3k/2)` is independent of ambient volume. The local three-slab inequality therefore yields

\[
\boxed{
-\log\mathbb E_{\nu_0}e^{-\lambda\Delta}
\le\frac32(k+q)\log(1+\lambda)+C_{k,\nu,q}
+\log\bigl(1+\mathfrak E_Q/Z_+\bigr).}
\]

For the verified 14-face Penrose insertion, `k=36`, `q=14`, `nu<=7`, so the explicit logarithmic coefficient before the overlap term is **75**. The last term is *not* yet shown to be O(log lambda) uniformly in ambient volume.

A sufficient, precisely localized remaining estimate is

\[
\boxed{
\sup_\Lambda\mathfrak E_Q/Z_+\le C(1+\lambda)^a,
}
\]

with `C,a` depending only on the fixed insertion support. If established, it would prove the desired uniform barrier bound with logarithmic coefficient `75+a`. The stronger condition `\mathscr B_t\succeq0` on the nontrivial Peter–Weyl modes would make `\mathfrak E_Q=0` and recover the direct `z^q` comparison, but that positivity is **not** a consequence of positive integral kernels alone.

## 6. Research status

**Proved:** exact three-slab telescoping; localized Jordan negative-bridge inequality; q-link Peter–Weyl partial-trace reduction; exact extension for one-slab insertions with commuting outer transfers; explicit positive-kernel Z2 obstruction to an unqualified Loewner replacement proof.

**Not proved:** a polynomial bound on `\mathfrak E_Q/Z_+` uniform in ambient Penrose volume for arbitrary nonstationary masks; arbitrary three-slab compact SU(2) R3; continuum mass gap.

The next viable proof target is a quantitative nontrivial-representation bound on the *negative part of the local reduced bridge*, potentially using SU(2) gauge constraints, Bianchi-fillability and finite-collar transport. Simply invoking convolution positivity or an abstract Schatten inequality is insufficient.

## Reproduction

`python bridge_counterexample.py` verifies the exact rational obstruction. `python verify_local_bridge.py` performs 200 finite-matrix sanity tests of the telescoping identity and negative-bridge inequality. These are checks, not substitutes for the exact operator proof.
