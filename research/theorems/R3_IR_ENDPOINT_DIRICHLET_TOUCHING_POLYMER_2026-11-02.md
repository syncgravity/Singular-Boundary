# Endpoint Dirichlet localization for touching connected polymers — 2026-11-02

Conditional on the archived original-link shared-face Wigner action and magnetic coefficient-l1 Neumann inverse estimate, this audit improves the **adjacent disjoint-support** Poisson estimate from cubic to linear dependence on the union interval length.

For I=[1,b], J=[b+1,t], put x=n_b, y=n_(b+1), and Q(n)=1/2Σ_(i=0)^t(n_(i+1)−n_i)^2 with n_0=n_(t+1)=0. The cross-gradient has a single shared physical original link, so ||Γ_K(f_n,g_m)||_1 ≤3xy||f_n||_1||g_m||_1, with no facewise Clebsch–Gordan degree reduction.

**Exact sharp Dirichlet endpoint inequality:** Q(n)≥[x²/b+(x−y)²+y²/(t−b)]/2, whence xy/Q(n)≤R_(t,b):=1/[sqrt((1+1/b)(1+1/(t−b)))−1]<3t/4. This follows by Cauchy–Schwarz on increments and elementary optimization; piecewise-linear tent profiles attain equality in the real-degree relaxation.

Using the archived inverse bound ||K_t(n)^−1||_1 ≤1/[Q(n)+(N+1)/2], for every σ≥0 and touching face-disjoint supports, **||K_t^−1P_0Γ_K(f,g)||_(Wσ(T)) ≤3R_(t,b)||f||_(Wσ(I))||g||_(Wσ(J)) < (9t/4)||f||||g||**. This improves the prior 3A_t/4~t³/8 to O(t), without analytic-radius loss.

For midpoint cuts of even t, the sharp ratio xy/Q=t/2 is attained by symmetric integer tent degrees, and the extra linear margin can be made negligible by scaling degree. Thus the **specific Q-based coefficientwise proof method cannot eliminate linear t growth**. This is NOT a lower bound for the actual nonlinear Poisson operator, whose spin-coupling cancellations might give stronger endpoint localization. A strip-uniform connected-polymer convolution and physical lambda=1 interacting or continuum Yang–Mills mass gaps remain open.

The full mathematical report, exact-rational verification script (32,412 checks), passing log and SHA-256 manifest are preserved in Proof Audits Library.