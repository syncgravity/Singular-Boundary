# R3-IR-552 — Constructive quadratic center-cap response from a Doeblin bound

2026-10-30. **Finite-regulator theorem with explicit constants in terms of a heat-kernel minorization**. No refinement-uniform minorization is established.

## Setting

On compact X=SU(2)^E with normalized Haar μ, fix a positive smooth ground state Ω0 of H0=H_E+V_other, eigenvalue E0, with unique simple lowest eigenvalue. Assume Ω0 is independent of chord U13, and the involution J: U13→−U13 commutes with H0. Let W=-p10 be the adjacent Wilson multiplier, ||W||∞≤1 and JWJ=−W. Set H_b=H0+bW; assume H0 is uniformly elliptic for the fixed regulator and the positive ground-state transform of H0 has a continuous strictly positive heat kernel.

Let π(dU)=Ω0(U)^2 μ(dU), normalized, and define the positive Markov ground-state diffusion semigroup P_t=e^{-tA0}, A0=Ω0^{-1}(H0−E0)Ω0. Suppose for some t>0 its kernel k_t(x,y) relative to π satisfies the positive lower bound η=inf_{x,y}k_t(x,y)>0. Necessarily η≤1. This is an **explicit finite-regulator datum**; its value has NOT been computed for the 30-link M5 Penrose operator.

## Quantitative lemma

On zero-π-mean bounded functions, R=A0^{-1}=∫_0^∞ P_s ds satisfies ||R g||∞≤A||g||∞ with **A=2t/η**. Proof: P_t(x,dy)≥ηπ(dy), so osc(P_tg)≤(1−η)osc(g), and π(g)=0 ensures ||P_sg||∞≤osc(P_sg)≤2(1−η)^floor(s/t)||g||∞. Integrate over successive length-t intervals.

For complex z with |z|≤r=1/(100A), solve the nonlinear normalized eigenfunction equation for q_z=1+u_z, π(u_z)=0:

u_z = -z R[(W−π(Wq_z))q_z].

For ||u||∞≤1/2 the right side has sup ≤(15/4)A|z| and Lipschitz constant ≤4A|z| (using ||W||∞≤1, |π Wq|≤3/2). Thus it is a uniform contraction at |z|≤r and produces a holomorphic u_z with ||u_z||∞≤0.04. For real b it is positive and the unique normalized ground state ratio: Ω_b=Ω0 q_b /sqrt(πq_b²). The associated eigenvalue shift is δE_b=bπ(Wq_b).

The exact center involution implies q_−z=Jq_z by holomorphic uniqueness. For the deleted-face trace p0, let π(·|p0=p) be the unperturbed conditional law; Ω0 is U13-independent, so p0 has Haar law under π and J maps p to −p. Define the radial relative density

s_z(p)=π(q_z²|p)/π(q_z²),   t_z(p)=[s_z(p)+s_z(−p)]/2.

The denominator π(q_z²)=1+π(u_z²) is nonzero for |z|≤r and >=1−0.04² in modulus. The numerator has modulus ≤(1.04)², so ||t_z||∞≤1.09. By parity, t_−z=t_z; also t_0=1. Cauchy coefficient bounds for even holomorphic t_z yield for real |b|≤r/2

sup_p |t_b(p)−1| ≤ 1.09 (|b|/r)² /(1−|b|/r) ≤ **3×10^4 A² b²**.

Consequently every two-center radial cap simultaneously obeys the explicit finite-regulator inequality

**Pr_b(C_delta) ≥ [1−C_h b²] c_delta,   C_h=3×10^4 (2t/η)^2,   |b|≤η/(400t),   0<delta≤1.**

The bound becomes vacuous near the largest permitted b due to deliberately conservative coefficients; one can tighten constants or use a direct resolvent expansion. Importantly C_h is independent of cap radius but depends on the full unperturbed diffusion and may scale terribly with number of links.

## Verification and limitations

A positive reversible 3-state Markov chain with a parity-odd potential was used only as an independent numerical regression: with t=1, η≈0.4730743724, A≈4.2276650704, r≈0.00236537186, C≈536194.5584; the formula passed for both signs b=±r/2. This toy does NOT replace an interacting Penrose eigensolve. All proof inequalities above are mathematical rather than dependent on this regression.

The original 30×30 M5 Whitney array remains archived in ChatGPT Library, but **η_h(t) has not been computed for that operator**, and no uniform positive lower bound has been proved as the Penrose graph refines. A full-dimensional heat-kernel minorization can degrade exponentially with link count even when a local cap probability is healthy. Thus this theorem makes the prior nonconstructive C_h *explicit in a computable finite-regulator kernel constant*, but does not prove the physically required uniform response. Research should pursue a local-in-face conditional mixing, influence decay, or local score bound, not assume a volume-independent global Doeblin η.

No NPZ/ZIP data are committed to Git. No continuum Yang–Mills mass gap is proved.

Reproducer: research/scripts/validate_wilson_doeblin_quadratic.py.
