# The Singular Boundary — Strong-magnetic one-rhombus conditional gap and failure of normalized influence contraction

**26 October 2026 — theorem investigation.** The asymptotics below concern the exact **isolated, four-link, one-rhombus** Wilson Hamiltonian, not the entire interacting Penrose assembly. They prove that a proposed *universal* `||B||<1` sufficient condition cannot hold on all Wilson rhombus blocks. They **do not** disprove the mass gap or exclude a different block variable or renormalization construction.

## 1. Model and normalization

Let `a>0`, `b>0`, `W=U1 U2 U3^{-1} U4^{-1}` and `p(W)=Tr(W)/2`. The gauge-invariant one-face physical Hamiltonian is `H=4a(-Δ_W)+b(1-p(W))` on SU(2) class functions, where `(-Δ)χ_j=j(j+1)χ_j`. Its unique real positive normalized ground state `ω(W)` is a class function. Conditioning on the other three links when one of the four links is varied gives the probability measure `dν(W)=ω(W)^2 dW`, up to a Haar-preserving isometry. For one eliminated edge, let `γ(a,b)` be the *full SU(2)* Poincaré constant of `ν` (not only its class-function radial restriction). For distinct edges `e,g` in the rhombus let `I_{eg}=∫|∇_g logρ_e|²ρ_e`, the previously proved Fisher influence. The prior exact identity is `I_{eg}=4∫|∇ω|²dW`, independent of e,g.

Define the dimensionless parameter `c=√(b/(2a))`, which tends to infinity at strong magnetic coupling. SU(2)≈S³ near the identity, with tangent coordinates `x∈R³`, `r=|x|=θ`, metric `-Δ=(1/4)(-Δ_{S³})`. Around its unique nondegenerate minimum, `1-p=1-cos θ=θ²/2+O(θ⁴)`. Hence near the well,

`H = -a Δ_{R³}+(b/2)|x|²+ lower-order curvature/quartic terms`.

Set `y=√c x`. The leading normalized ground-state density in y is `π^{-3/2}exp(-|y|²) dy`, i.e. `ω(x)≈const·exp(-c|x|²/2)`.

## 2. Theorem A — sharp local asymptotics

For fixed a and b/a→∞, standard compact-manifold, unique-nondegenerate-well harmonic approximation, including localization of the normalized positive ground state and convergence of the first full weighted Poincaré eigenvalues (via ground-state transform), yields

\[
\boxed{\gamma(a,b)=\frac{c}{2}(1+o(1))=\frac{1}{2\sqrt2}\sqrt{b/a}\,(1+o(1)),}\tag{A1}
\]
\[
\boxed{\mathcal I_{eg}(a,b)=\frac{3c}{2}(1+o(1))=\frac{3}{2\sqrt2}\sqrt{b/a}\,(1+o(1)).}\tag{A2}
\]
In particular,
\[
\boxed{\lim_{b/a\to\infty}\frac{\mathcal I_{eg}}{\gamma}=3.}\tag{A3}
\]

**Detailed reduction / verification of constants.** The ground-state transform in local x coordinates has limiting Dirichlet form `\tfrac14∫|∇_x f|²ω²dx`. Rescale to y=√c x; dividing the form by c gives `\tfrac14∫|∇_y f|²dμ_G`. For `dμ_G=π^{-3/2}e^{-|y|²}dy`, the optimal Poincaré constant relative to `∫|∇_y f|²` is **2**, as can be seen by linear coordinate eigenfunctions of the Ornstein–Uhlenbeck generator. Thus `γ/c→(1/4)·2=1/2`. Full angular-coordinate functions give this lowest eigenvalue; restricting to radial functions alone would instead give an eigenvalue `c` (a factor two error).

For the influence, `logρ=2logω=-c|x|²+constant+o(1)` on the localized scale, while the gradient norm for `-Δ` is `|∇f|²=(1/4)|∇_{R³}f|²(1+o(1))`. Therefore

`I = ∫|∇ logρ|²dν = c² E|x|²(1+o(1)) = c E|y|²(1+o(1)) = (3/2)c(1+o(1)).`

A *rigorous justification* of the limiting relations uses the classical one-well harmonic approximation for Schrödinger operators on compact manifolds, plus localization and convergence of the corresponding low eigenfunctions and quadratic forms; cf. Helffer–Nier, *Semiclassical Analysis for the Schrödinger Operator: Harmonic Approximation*, LNM 1862 (2005), Chapter 12, and single-plaquette SU(2) Mathieu reductions. The elementary displayed computation alone is an asymptotic calculation; if a standalone full proof without invoking the established harmonic approximation is required, the missing technical ingredient is a quantified global IMS/Agmon localization and weighted-form liminf/recovery argument. **Do not misrepresent the local Taylor expansion alone as a self-contained global error bound.**

### Independent spectral justification that avoids assuming convergence of logarithmic scores

Let `L=-Δ_W` be the Laplacian on the **full SU(2)** link space and put `t=b/(4a)`. The same positive `ω` is the ground state of `L+t(1-p)`. Its ground-state transformed Poincaré generator is unitarily equivalent to `L+t(1-p)-e_0(t)` on **all** SU(2) functions. Consequently, the conditional `γ` is **exactly** the first excitation gap of that auxiliary one-link Schrödinger operator. The relevant excitation is angular, not the radial gauge-invariant excitation of the physical one-face Hamiltonian. The compact-manifold one-well harmonic approximation applies to this auxiliary spectrum and directly yields A1.

Moreover, the Fisher coefficient can be obtained without assuming convergence of derivatives of `logω`: define `E_0(a,b)=inf spec(H_{a,b})`. Feynman–Hellmann gives `∂_b E_0=⟨1-p⟩_{ω²}`. The exact kinetic sum rule gives

`I_{eg}=4∫|∇ω|² = [E_0-b ∂_b E_0]/a`.

The one-well harmonic approximation yields `E_0(a,b)=3√(ab/2)(1+o(1))` for `b/a→∞`. Since `E_0` is a differentiable **concave** function of b (an infimum of affine functions), the standard secant-slope squeeze for a concave function with asymptotic `C√b` shows `∂_b E_0=(3/2)√(a/(2b))(1+o(1))`. Thus

`I_{eg}=[3√(ab/2)-(3/2)√(ab/2)]/a(1+o(1))=3c/2(1+o(1))`,

which proves A2 once the standard one-well energy asymptotic is invoked. This avoids an unjustified passage to a logarithmic-score limit.

## 3. Theorem B — no contraction of the proposed normalized influence matrix

The earlier proposed matrix was
\[
\mathsf B_{eg}=\sqrt{a_g\mathcal I_{eg}/(a_e\gamma_e)},\quad g\ne e,\quad \mathsf B_{ee}=0.
\]
For the four equal electric coefficients on one isolated rhombus, every conditional `γ_e=γ` and every `\mathcal I_{eg}=I`, so the four-by-four matrix is **exactly**
\[
\mathsf B=\sqrt{I/\gamma}\,(\mathbf 1\mathbf 1^T-I_4).
\]
Its eigenvalues are `3√(I/γ)` (once) and `-√(I/γ)` (threefold). Therefore
\[
\boxed{\|\mathsf B\|_{\mathrm{op}}=3\sqrt{I/\gamma}\longrightarrow3\sqrt3>1.}\tag{B1}
\]
Thus `||B||≤1-ε` cannot be a **universal all-coupling**, single-link Penrose-compatible blocking criterion. Its failure already appears on a connected block of one rhombus, before any issue of volume growth. In a larger Penrose complex, the conditional law depends on the other loops and is not literally this isolated one-face law; (B1) is not a theorem about the full many-face matrix. It blocks the *unrestricted* approach, not every possible Penrose-specific or simultaneous multi-link RG map.

## 4. Gauge-invariant sector clarification

On this single, simply connected rhombus the *physical* observables are functions of the conjugacy class of the total holonomy. Conditional integration of any such `f(W)` over one link with respect to `ω(W)²dW` equals its global interacting mean and is independent of the other links. Hence **conditional averaging collapses the whole vacuum-orthogonal physical one-face space** to zero. A lower bound on its eliminated-sector spectral gap is then a rephrasing of the one-face physical gap for that particular graph; it cannot be iterated naively to bound the retained physical spectrum on a many-face Penrose patch.

## 5. Implications for R3 and R2

1. The good news: the *shape-sensitive* conditional Poincaré constant actually grows at strong magnetic coupling, at the same power `√(b/a)` as Fisher influence.
2. The bad news: their normalized ratio tends to 3, and the elementary four-edge influence matrix has norm `3√3`, so the proposed `||B||<1` route **fails** as a general sufficient condition.
3. For a genuine spatial RG one should eliminate **whole gauge-invariant loop/face clusters simultaneously**, retain boundary-holonomy states and their Gram metric, and control their connected multi-source Schur complement. The source map must remain independent of an assumed spectral gap, and a remaining-sector Poincaré estimate must still be derived.
4. On the physical continuum coefficient path `b/a≈(g_3²h)^{-2}`, A1–A3 describe *only the isolated one-face model*. A Penrose many-face quantum continuum limit, vacuum-normalized Wilson-frame observability and physical spectral gap remain **unproved**. Exact C5 tensor isotropy is insufficient.

**Status ledger:** one-face harmonic asymptotics (under standard one-well harmonic approximation) ESTABLISHED; normalized *isolated-rhombus* matrix fails contraction ESTABLISHED; many-face normalized Penrose matrix UNKNOWN; uniform R3 and continuum R2 UNPROVED.
