# The Singular Boundary — nonlinear collective Wilson Dirichlet audit

**Date:** October 28, 2026. **Research area:** R3-IR; finite connected SU(2) rhombus complexes, exact gauge-invariant observables. **Integrity:** only new derived proofs and deterministic checks, no simulation, no modification of the original archives. **Status:** ND-1–ND-4 independently proved under their stated assumptions; the nonlinear interacting, volume- and cutoff-uniform mass gap is **OPEN**.

## 1. Sources, fixed conventions and audit scope

This work extends the archived project theorem `R3_IR_COLLECTIVE_WILSON_FORM_FACTORS_2026-10-28.md` on the branch `audit/2026-10-28-independent-reconstruction`. It uses the recovered `HISTORICAL_Q14_CANONICAL.json` *only* for its three genuine spatial seed rhombi (not the full fourteen-face temporal insertion). The seed has 8 vertices, 10 spatial edges and 3 faces; the exact signed face–edge matrix was verified in the preceding dual-Laplacian audit. No original history or Stage 7–35 numerical result was generated or reinterpreted.

Let `G=(V,E,F)` be a finite simply connected rhombus disk with free spatial boundary. The full-link Hilbert space is `L²(SU(2)^E,dU)` and its physical subspace is invariant under the vertex gauge group. The Hamiltonian is

\[
H_G=\sum_{e\in E}a_e(-\Delta_e)+\sum_{f\in F}b_f d_f,\qquad
 d_f=1-p_f,\quad p_f=\tfrac12\operatorname{ReTr}U_f,
\]

with `a_e>0,b_f≥0`, `−Δ` normalized to have SU(2) spin-`j` eigenvalue `j(j+1)`. Its unique full-link ground state `Ω_G>0` is gauge invariant. Put `dν_G=Ω_G² dU`.

Choose a rooted spanning tree `T`, a base vertex for each face and the tree parallel transport of its face word to the root, denoted `W_f=s_f I+i u_f·σ`. Under local gauge transformations every `W_f` undergoes the same root conjugation. For real weights `v_f` define `S=Σ_f v_f u_f` and the *exactly* gauge-invariant positive Wilson polynomial

\[
\mathcal Q_v=2\sum_{fg}v_fv_g\big[p(W_fW_g^{-1})-p(W_fW_g)\big]=4|S|^2.
\]

The earlier audit independently established `||Q_v||∞=4(Σ|v_f|)²` for an open disk. No logarithms of SU(2) matrices are introduced. On each link write `X_e^a` for the orthonormal `iσ_a/2` left-invariant generators and `|∇_eQ|²=Σ_{a=1}³|X_e^a Q|²`.

## 2. Theorem ND-1 — exact *pure-connector* torque identity at every coupling

Suppose a tree edge `e` belongs to no plaquette boundary with `v_f≠0`, but lies on the rooted connector path to some of their face base points. Define the selected weighted adjoint sums

\[
S_{e}=\sum_{f:\ e\text{ lies on connector to }f}v_fu_f,\qquad
S_{\bar e}=S-S_e.
\]

Then for **every** link configuration and any admissible nonnegative magnetic couplings,

\[
\boxed{\quad |\nabla_e\mathcal Q_v|^2=64\,|S_e\times S_{\bar e}|^2.\quad}\tag{ND1}
\]

**Proof.** Varying the tree link by `exp(t iσ_a/2)` rotates **all and only** based holonomies downstream of `e` by one common root-frame adjoint rotation. Since `e` does not occur on any selected face boundary, this variation changes no unbased selected face holonomy. In the adjoint three-vector notation, `X_e^a S_e=n_e^a×S_e`, with `{n_e^a}` an orthonormal frame (possibly frame-rotated by the root connector). `X_e^a S_{\bar e}=0`. Differentiating `Q=4|S|²` gives `X_e^a Q=8 S·(n_e^a×S_e)=±8 n_e^a·(S_e×S_{\bar e})`. Squaring and summing over the orthonormal Lie-algebra basis proves ND1, including the coefficient 64. There is no expansion or assumption that any holonomy is close to identity.

**Curvature-sensitive corollary.** Because `|u_f|²=1-p_f²≤2d_f` pointwise,

\[
\boxed{|\nabla_e\mathcal Q_v|^2\le256
\left(\sum_{f\in A_e}|v_f|\sqrt{d_f}\right)^2
\left(\sum_{g\notin A_e}|v_g|\sqrt{d_g}\right)^2,}\tag{ND1b}
\]

where `A_e` denotes the selected face indices downstream of `e`. This gives an exact **quartic curvature-cost structure** for remote connector derivatives. It is not yet an expectation bound uniform over growing disks: the indicated fourth-order products of curvature deficits require independent interacting moment or clustering estimates, which have not been established.

A useful alternate consequence, when all selected face coefficients are strictly positive, follows by Cauchy–Schwarz:

\[
|\nabla_e\mathcal Q_v|²\le256
\Big(\sum_{f\in A_e}\frac{v_f²}{b_f}\Big)
\Big(\sum_{g\notin A_e}\frac{v_g²}{b_g}\Big)
\Big(\sum_{f\in A_e}b_fd_f\Big)
\Big(\sum_{g\notin A_e}b_gd_g\Big).
\]

Its constant and product of regional energies may still be extensive; it is **not** an infrared bound.

## 3. Theorem ND-2 — general all-coupling nonlinear Dirichlet inequality

For every tree edge `e` let `A_e` be its downstream selected face set. For a non-tree edge let `A_e=∅`. Write `W_e=Σ_{f:e∈∂f}|v_f|`. The exact link variation splits into the connector adjoint rotation of the downstream group plus a direct variation of at most one occurrence of `e` in each selected four-edge face word. In the fundamental SU(2) Casimir metric, the vector-part derivative of one group factor has Lie-gradient Hilbert–Schmidt norm at most `√3/2`. Thus

\[
\boxed{
|\nabla_e\mathcal Q_v|^2\le
128|S_{A_e}\times S_{\bar A_e}|^2
+96|S|^2 W_e^2.
}\tag{ND2}
\]

**Proof.** For each Lie direction, write `X_e S=n_e×S_{A_e}+R_e`, where `R_e` contains only selected face boundaries incident to `e`. Minkowski's inequality over the three Lie directions gives `(Σ_a|R_e^a|²)^{1/2}≤(√3/2)W_e`. The connector contribution to `∇Q` has squared norm exactly `64|S_{A_e}×S_{\bar A_e}|²` when treated on its own, and the direct boundary contribution is bounded by `64|S|²(3W_e²/4)=48|S|²W_e²`. Apply `|x+y|²≤2|x|²+2|y|²`, establishing ND2. For a pure connector, use the sharper equality ND1.

Combining ND2 with the exact ground-state transform produces the **all-coupling nonlinear Dirichlet bound**

\[
\boxed{
D_G(v):=\langle \mathcal Q_v\Omega_G,(H_G-E_0)\mathcal Q_v\Omega_G\rangle
\le128\sum_{e\in T}a_e\,\mathbb E_{\nu_G}|S_{A_e}\times S_{\bar A_e}|²
+24\,\mathbb E_{\nu_G}\mathcal Q_v\sum_e a_eW_e².
}\tag{ND2b}
\]

The first term is an **adjoint connector-torque** cost; the second is an explicit **true face-boundary** cost. The split preserves the large-field nonabelian effects that a bare local-plaquette estimate would omit. It has no assumed gap or ground-state mixing input. It is not a volume-uniform estimate, since the tree sum and the curvature moment can increase with patch size.

For an exactly pure connector, the sharper contribution is `64a_e E|S_{A_e}×S_{\bar A_e}|²`.

## 4. Theorem ND-3 — exact electric-vacuum variance and connector cost

At `b_f=0` for all faces, `Ω_0=1` and the full-link measure is product Haar. On a simply connected planar disk the tree-gauge face holonomies can be chosen as independent Haar variables (bounded-face loops generate the graph's free cycle group; the corresponding free Nielsen changes preserve product Haar). In particular,

\[
\mathbb E_0[u_f]=0,\quad
\mathbb E_0[u_f^a u_g^b]=\frac14\delta_{fg}\delta_{ab},\quad
\operatorname{Var}_0(|u_f|²)=\frac1{16}.
\]

For arbitrary real face weights `v_f`, exact integration of the fourth moments yields

\[
\boxed{\mathbb E_0\mathcal Q_v=3\sum_f v_f²,\qquad
\operatorname{Var}_0(\mathcal Q_v)=\sum_f v_f^4+12\sum_{f<g}v_f²v_g².}\tag{ND3a}
\]

For `Σv_f²=1` the variance is `6−5Σv_f^4`, between 1 and 6. For a pure connector edge separating sets `A_e` and its complement, independence and rotational invariance give

\[
\mathbb E_0|S_{A_e}\times S_{\bar A_e}|²
=\frac38\Big(\sum_{f\in A_e}v_f²\Big)
\Big(\sum_{g\notin A_e}v_g²\Big).
\]

Therefore its **exact** electric-vacuum Dirichlet contribution is

\[
\boxed{D_{0,e}(v)=24a_e
\Big(\sum_{f\in A_e}v_f²\Big)
\Big(\sum_{g\notin A_e}v_g²\Big).}\tag{ND3b}
\]

This nonzero remote-connector energy is present even when the edge belongs to no selected face boundary. It is not a proof that a physical excitation gap is small: the Rayleigh quotient of this particular nonlocal source is an **upper** bound on the physical gap, and its Dirichlet numerator may be very large.

**Authentic recovered three-rhombus seed.** The canonical seed contains 8 vertices, 10 edges and three rhombi. With tree root `(0,-1,-1,0,-1)`, select source faces 1 and 2, and choose their face base vertices `(-1,-1,-1,-1,-1)` and `(0,-1,-1,-1,-1)`. The edge from `(-1,-1,-1,0,-1)` to `(0,-1,-1,0,-1)` belongs to face 0, but to **neither selected face**; it lies only on the connector to selected face 1. For `v=(0,1/√2,1/√2)` the exact electric benchmark is

\[
\boxed{\mathbb E_0 \mathcal Q_v=3,\quad
\operatorname{Var}_0(\mathcal Q_v)=\tfrac72,\quad
D_{0,e}(v)=6a_e.}\tag{ND3c}
\]

This is a true canonical spatial Penrose fixture, **not** the full temporal Q14 construction. The exact incidence, rooted paths, rational quaternion identities, and Haar moment coefficients were verified without Monte Carlo.

## 5. Theorem ND-4 — exact first-moment/variance diagnostic and remaining gate

For any finite `G`, smooth real gauge-invariant `Q_v` and the genuine interacting vacuum,

\[
V_G(v)=\operatorname{Var}_{\nu_G}(\mathcal Q_v)>0,\quad
D_G(v)=\sum_e a_e\mathbb E_{\nu_G}|\nabla_e\mathcal Q_v|²,
\]

and its connected semigroup correlation obeys

\[
C_v(0)=V_G(v),\quad -C'_v(0+)=D_G(v),\quad
0\le V_G(v)-C_v(t)\le tD_G(v).
\]

The nonlinear Rayleigh quotient gives

\[
\boxed{\operatorname{gap}(H_G)\le D_G(v)/V_G(v).}\tag{ND4}
\]

Since `Ω_G>0` everywhere and `Q_v` is nonconstant when `v≠0` on a simply connected disk, `V_G(v)>0` at **every finite** magnetic coupling. But **no volume- and cutoff-uniform positive lower bound** on `V_G(v)` has been established, and ND2 does not give a uniform upper bound on `D_G(v)` for delocalized modes. Therefore ND4 is an exact diagnostic and possible no-go tool, not a proof of a positive gap or of gap closure.

### Research decision / next noncircular theorem

The earliest remaining quantitative obligation is a **transport-torque moment estimate**, for example an independently derived bound on

\[
\mathbb E_{\nu_G}|S_{A_e}\times S_{\bar A_e}|²
\]

in terms of local/region curvature energies with constants controlled by the support cut and physical scale, *and* a compatible nontrivial variance lower bound if using the Rayleigh upper-gap route. A proof must handle interacting gauge-invariant ground-state correlations, arbitrary nonflat SU(2) words, tree-choice dependence and large regions. An energy upper bound or an assumed ground-state Poincaré/tensorization inequality cannot be treated as this missing estimate. It is possible that global tree-based sources are too expensive for the intended continuum bound; negative outcomes must be retained and a more local/covariant transport prescription considered.

**Evidence classifications:** ND1–ND4 **independently proved for the specified finite model**. Exact three-seed test **computationally certified**. Nonlinear, all-scale positive interacting gap and continuum reconstruction **OPEN**.
