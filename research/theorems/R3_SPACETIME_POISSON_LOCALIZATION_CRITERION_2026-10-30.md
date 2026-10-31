# R3-IR-555 — Conditional spacetime-to-Poisson localization criterion and gapless-chain obstruction

Date 2026-10-30. This result is a **conditional localization theorem** plus an independently verified countercheck, not a proof of dynamic localization for the Penrose Wilson vacuum.

Let P_t=exp(-tA_0) denote the unperturbed reversible ground-state Markov semigroup (A_0≥0), and W a mean-zero localized forcing. Let ℓ_x be a linear local observation/sensitivity functional at graph distance d=d(x,supp W) with ℓ_x(1)=0. Suppose, with C, μ, v, λ strictly positive **independent of graph size**, that for every t≥0,

|ℓ_x(P_t W)| ≤ C min{exp(-λt), exp[-μ(d-vt)]}.

For the Poisson solution u=A_0^-1 W=∫_0^∞P_tW dt, both terms can be integrated by splitting at t*=μd/(λ+μv). In the early interval use the finite propagation estimate and in the late interval use temporal mixing. This proves the quantitative spatial localization bound

**|ℓ_x(u)| ≤ C [1/(μv)+1/λ] exp[-βd],  β=μλ/(λ+μv)>0.**

This is a theorem about the stated semigroup hypotheses; it is not a claim that such C,μ,v,λ have been demonstrated for the original Penrose SU2 ground-state diffusion. In particular the static Whitney inverse decay proved in R3-IR-554 is a possible ingredient in a finite-propagation estimate, but does not provide either estimate above by itself. For v=0, the simpler bound |ℓ_x(u)|≤C exp(-μd)/λ follows.

The second Poisson response u2=A_0^-1[W A_0^-1W−mean] requires a corresponding influence estimate for the *composite, nonlocal forcing* W u1 and cannot simply be inferred from u1's local estimate without an algebra/product norm and centeredness control. Uniform bounds on the conditional symmetrized coefficient D_h(p), its higher responses, and physical coupling normalization remain independent obligations.

## Explicit chain obstruction

On an n-vertex path consider the graph Laplacian Δ_n with reflecting endpoints, and mean-zero forcing f=e_1−1/n. Its mean-zero Poisson solution u=Δ_n^† f satisfies u_1=(n−1)(2n−1)/(6n), hence grows ~n/3 as n grows. A strictly local, uniformly bounded-degree generator therefore need not yield a volume-independent resolvent response. With added restoring mass m>0, (Δ_n+mI)^−1e_1 has bounded peak (~2.701562 at m=.1) and an exponentially small far-end response. This is a transparent *linear elliptic chain analogy*, not a model of the full SU2 interacting ground-state generator. The gapless chain is not claimed to satisfy the time-mixing hypothesis λ>0 uniformly.

## Verification

Executed `research/scripts/audit_poisson_spacetime_localization.py`. For C=1, μ=.7, v=1.4, λ=.35, direct quadrature at distances 0,2,5,10,20 agrees with the derived upper bound. Reflecting chains n=16,32,64,128 give gapless response peak 4.84375, 10.171875, 20.8359375, 42.16796875, whereas with m=.1 peaks stay close to 2.70156. Original Whitney M5 static metric results remain under R3-IR-554; no assertion of actual Penrose dynamic mixing was numerically tested.

## Next physical test

For an actual sequence of archived or newly assembled Whitney M_h with explicit coupling prescription, derive an influence differential inequality for the Wilson unperturbed ground-state generator, including nonlocal K=M_h^-1, rooted transport commutators, and the interacting drift 2Γ(log Ω_0,·). Show temporal mixing and propagation constants remain useful across h. Until then **no refinement-uniform center-cap coefficient and no continuum Yang–Mills mass gap are established**.

Git stores only text and executable source; source binary matrices stay in ChatGPT Library /The Singular Boundary/Source.
