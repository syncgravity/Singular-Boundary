# R3 — An exact nonlinear one-shell Peierls estimate and its unresolved boundary term

**27 October 2026.** Genuine direct-Z5 Penrose rhombus disks × three periodic temporal intervals. New theorem holds for arbitrary finite bounded-incidence SU(2) Wilson plaquette complexes. **It does not prove absolute local staple-frustration concentration or the general R3 insertion inequality.**

## Setting

Let `R` be any retained face set. On independent SU(2) links put `d(U)=1-(1/2) Tr U` and `dμ_R=Z_R^{-1} exp(-λ Σ_{p∈R}d(W_p)) ∏_e dU_e`, `λ>=1`. Each face is a quadrilateral, and each link meets at most `ν` retained faces (for the verified Penrose three-time complexes `ν<=7`).

For a finite link block `J`, define `A(J)={p∈R:∂p intersects J}`, `S_J(U_J;U_{J^c})= Σ_{p∈A(J)} d(W_p)`, and `s_J(U_{J^c}) = min_{U_J∈SU(2)^J} S_J(U_J;U_{J^c})`.

For `B⊂H`, the variable `s_B` is a random function of the links outside `B`, including the fluctuating links `H\B`. The larger-block minimum `s_H` is a function only of the exterior links `H^c`.

## Theorem 1 (unconditional, nonlinear, one-shell Peierls bound)

Let `h=|H|`, `c_H=8/(3π³)`, and `C_ν=2ν-log c_H`. For every `t>=0` and `λ>=1`, for every fixed exterior configuration `c=U_{H^c}`,

\[
 \boxed{\mu_R\bigl(\lambda[s_B-s_H(c)]\ge t\mid U_{H^c}=c\bigr)
 \le \min\{1,\exp[h((3/2)\log\lambda+C_\nu)-t]\}.}
\]

In particular, without any assumptions on the Gibbs exterior marginal,

\[
 \boxed{\lambda\mathbb E_{\mu_R}s_B
 \le \lambda\mathbb E_{\mu_R}s_H+h((3/2)\log\lambda+C_\nu)+1.}
\]

For `ν=7`, `C_ν=16.4533604045365`. Every constant is **ambient-volume-independent**. The formula is an *increment* tail (`s_B-s_H`), not an absolute tail for `s_B`.

### Proof

1. For each exterior `c`, compactness supplies an exact minimizer `u*` of `S_H(u;c)` with minimum `s_H(c)`. In the product of geodesic SU(2) balls of radius `λ^{-1/2}` about its `h` link coordinates, the first derivative of `S_H` vanishes at `u*`, and each plaquette has second derivative at most the square of the sum of the link angular speeds. Four link factors per plaquette and at most `ν` faces per link give `λ(S_H-s_H) <= 2νh` throughout the product ball.
2. For `0<r<=1`, normalized SU(2) Haar volume satisfies `Haar(B_r)>=c_H r³`: on `S³`, `(2/π)∫₀^r sin²θ dθ >= (2/π)∫₀^r(2θ/π)² dθ=c_H r³`.
3. The exact local conditional partition thus obeys
   \[Z_H(c)=\int e^{-\lambda S_H(u;c)}du
     \ge e^{-\lambda s_H(c)}[c_H e^{-2\nu}\lambda^{-3/2}]^h.\]
4. For every `U_H`, `S_H(U_H;c)>=S_B(U_B;U_{H\setminus B},c)>=s_B(U_{H\setminus B},c)` because `A(B)⊂A(H)` and every deficit is nonnegative. Thus on the event `λ(s_B-s_H)>=t` the integrand is at most `e^{-λs_H-t}`, and the unweighted Haar measure of the event is at most 1. Divide this numerator by the previous local partition lower bound.
5. Integrating the tail of `Y=λ(s_B-s_H)` above `g=h((3/2)logλ+C_ν)` yields `E[Y_+|c] <=g+1`, and hence the expectation inequality.

No Gaussian regularization, Fourier positivity, concentration hypothesis, or high-coupling perturbation expansion is used.

## Corollary 1: a sharp statement of the unresolved terminal condition

For any `u,t>=0`,
\[
\boxed{\Pr\{\lambda s_B\ge u+g+t\}
\le e^{-t}+\Pr\{\lambda s_H>u\},\qquad g=h((3/2)\log\lambda+C_\nu).}
\]

Thus if a geometrically controlled bounded collar `H` with `h<=a|Q|` also satisfies `λ E s_H <= b|Q|(1+logλ)` under the *actual* exterior Gibbs marginal, the desired local energy bound follows. If `s_H(c)=0` for every exterior `c`, this is an unconditional full exponential absolute tail, but that condition is **not true** for the tested local Penrose collars with generic exterior holonomies.

A purported proof using `s_H=0` solely from bounded degree or local Bianchi identities is invalid. A local Tietze/Haar chart likewise does not show such a zero conditional minimum.

## Corollary 2: explicit support-local but still conditional R3 reduction

For the previously verified 14-temporal-face Penrose insertion, exact nonabelian prism Bianchi word substitution implies the pointwise inequality
\[\sum_{q\in Q}d(W_q)\le44\sum_{p\in A}d(W_p),\qquad |A|=54.\]
The construction counts transported noncommuting face factors; the longest factor sequence is 17. Let `B` consist of all links in faces `A`: the code gives `|B|=101`. Take `H` to be its one-face collar in the retained complex: `|H|=232`. The counts are identical at Penrose radii 5, 6.5, 8 and 10.

Combining Jensen's inequality, the previously proved conditional-block Haar-ball estimate and Theorem 1 yields
\[
\boxed{-\log\frac{Z_{R\cup Q}}{Z_R}
\le44\left[333\left(\frac32\log\lambda+C_7\right)+1+
\lambda\mathbb E_{\mu_R}s_H\right].}
\]

The first term is logarithmic and independent of ambient volume; **the final `λ E s_H` is NOT controlled**. This is a rigorous boundary-to-interior reduction of the nonlinear insertion problem, not its conclusion.

## Penrose collars and the obstruction to zero-cost pointwise termination

The anchor is the time-0 spatial link with Z5 labels `((-1,-1,-1,-1,-1),(-1,-1,-1,0,-1))`; the cavity is the *identical* 14-face overlapping temporal support in all four direct-Z5 patches.

Define `B_0` as the one-link anchor and recursively `B_{j+1}` as all links in retained faces touching `B_j`.

| Block | Links `|B_j|` | Retained faces touching block | Exterior links entering those faces | Relative exterior linearized rank |
|---|---:|---:|---:|---:|
| `B_0` | 1 | 3 | 9 | 2 |
| `B_1` | 10 | 20 | 31 | 8 |
| `B_2` | 41 | 74 | 89 | 24 |

These counts, and the exact Z5 labels of the local link and face sets, coincide across all four ambient volumes. The rank column equals `rank(D_{A(B_j)}) - rank(D_{A(B_j)} restricted to B_j)` over GF(1,000,003). The restricted matrices have full column rank (`1`, `10`, `41`), so the displayed positive gap is a rigorous lower bound on the real exterior compatibility rank. Consequently the local linearized flatness equations have nontrivial constraints on the fixed exterior variables at **all three tested collar levels**. A pointwise zero-minimum terminal condition cannot be justified by these collar checks. This does not exclude a *probabilistic* bound on their exterior Gibbs distributions.

## Why direct Chernoff/Peierls closure would be circular

For `A=A(H)`, the deterministic bound `s_H<=Σ_{p∈A}d(W_p)` gives, for `0<θ<1`,
\[
 \Pr\{\lambda s_H\ge u\}
 \le e^{-\theta u}
 \frac{Z_R(\lambda\text{ on }R\setminus A,\, (1-\theta)\lambda\text{ on }A)}{Z_R(\lambda\text{ on }R)}.
\]

The unknown factor is itself a *local coupling-comparison partition function ratio*, essentially the problem R3 seeks to control. Replacing it by 1, or assuming it is a fixed constant, is invalid. The same difficulty occurs in the exterior boundary-minimum law.

## What is genuinely new and what remains open

**Proved:** a model-independent nonlinear Peierls collar-increment distribution/tail with an explicit local Haar entropy prefactor; an ambient-independent 14-face Penrose insertion inequality with only one explicit exterior-minimum expectation remaining; exact canonical Penrose link/face and rank audits.

**Not proved:** a uniform unconditional tail for `λs_H`, an absolute local staple-frustration law for 3D retained Penrose Wilson measures, a volume-uniform bound of the exterior Gibbs marginal for arbitrary Q, the arbitrary-support R3 theorem, or a continuum Yang–Mills mass gap.

Next proof candidate: construct a *measure-preserving/controlled-Jacobian surgery* changing the shell exterior variables, with (i) energy decrement at least a fixed fraction of `s_H`, (ii) bounded-overlap local support, (iii) conditional Gibbs probability cost `exp[C|Q|(1+logλ)]`. The existence of that surgery for all Penrose Q is not shown by the present incidence ranks or exact relative Haar coordinates.
