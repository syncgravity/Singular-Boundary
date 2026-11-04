# The Singular Boundary — All-width fusion estimate with analytic-degree loss
Research audit, 2026-11-03. **Conditional finite-strip theorem; not same-radius closure, interacting gap, or continuum proof.** Complete accompanying reproducible audit is available in the conversation proof archive.

## Assumptions
Let E be original links of a finite simply connected open straight square strip, and work on Gauss-invariant functions on SU(2)^E. Put
[
K=-sum_{ein E}a_esum_{j=1}^3 X_{ej}^2,quad 0<a_0le a_ele a_*,
quad Gamma_K(f,g)=sum_{e,j}a_e(X_{ej}f)(X_{ej}g).
]
Use the generator convention where spin n has Casimir n(n+2)/4 and generator operator norm at most n/2. The nonconstant Gauss-invariant spectrum has free-electric gap at least 3a_0. Q removes the constant mode. Define B(f,g)=K^{-1}QGamma_K(f,g).

For the Peter–Weyl expansion f=sum_{\mathbf n}Tr(A_{\mathbf n}pi_{\mathbf n}), define d_{\mathbf n}=prod_e(n_e+1), |\mathbf n|=sum_e n_e and
[
|f|_{P_sigma}=sum_{\mathbf n}d_{\mathbf n} e^{sigma|\mathbf n|}|A_{\mathbf n}|_{S_1}.
]
For connected face intervals I, let f_I depend only on original links incident to I, and set
[
|F|_{kappa,sigma}=sum_I e^{kappa|I|}|f_I|_{P_sigma},
quad F=sum_I[I]otimes f_I.
]
Define B_hist by B applied to each input-history pair, with output labelled by the union I∪J for original-link overlaps and zero otherwise.

## Proposition
For (kappa>0,;sigma>sigma'ge0,;delta=sigma-sigma'>0),
[
oxed{|mathcal B_{m hist}(F,G)|_{kappa,sigma'}
le rac{a_*}{4a_0 e^2delta^2}
left(1+rac{3}{ekappa}ight)
|F|_{kappa,sigma}|G|_{kappa,sigma}.}
]
The constant is independent of strip length, all spin labels, and all connected-history widths.

### Argument
1. SU(2) Clebsch–Gordan output labels satisfy |l|≤|n|+|m|, with d_l≤d_nd_m. Tensor-product decomposition and trace-norm pinching imply that the dimension-weighted nuclear Fourier norm is submultiplicative with constant one, uniformly across original-link products.
2. On an input sector, |dπ_n(X_{ej})|≤n_e/2; and (n_e e^{-delta|mathbf n|}le (edelta)^{-1}). Thus
[
|Gamma_K(f,g)|_{P_{sigma'}}
le rac{3a_*}{4e^2delta^2}|E(f)cap E(g)|
|f|_{P_sigma}|g|_{P_sigma}.
]
3. The exact original-link free-electric inverse K^{-1}Q is diagonal in Peter–Weyl spin sectors. On nonconstant gauge invariants its eigenvalues obey λ≥3a_0; therefore its norm on P_{σ'} is ≤(3a_0)^{-1}.
4. For two overlapping/touching face intervals I,J, put t=|I∩J| and T=I∪J. The original-link overlap obeys |E(I)∩E(J)|≤3t+1, while
[
e^{kappa|T|-kappa|I|-kappa|J|}=e^{-kappa t}.
]
The elementary bound ((3t+1)e^{-kappa t}le1+3/(ekappa)) finishes the estimate after summing histories.

## Scope limits and next steps
This is a map from a **stronger** analytic-degree space to a weaker one, with an unavoidable loss **in this proof** of δ>0. It does **not** prove the same-radius estimate required for straightforward infinite iteration; it does not prove nonlinear score convergence, full interacting λ=1 gap, thermodynamic control, or four-dimensional Yang–Mills mass gap. Prior work shows repeated radius expenditure is potentially fatal to naive tree majorants. The next task is to construct a tame same-radius estimate, or a reorganized convergent nonlinear history-aware recurrence retaining all physical channels.

Geometric assumptions and spin-network boundary conditions are explicit; the free gap ≥3a_0 must be independently checked outside these finite strips. The full audit and exact-integer/Python finite checks remain separately archived.