# P0–P2: exact SU(2) two-time influence kernel and dyadic cubic refinement

**Research review, November 6, 2026 (UTC).** **Scope: fixed finite original-link cubic SU(2) Hamiltonians with the full spatial Wilson potential and positive heat-kernel time transfer.** This is a model-specific finite theorem candidate, subject to independent review—not the four-dimensional continuum Yang–Mills mass gap or a quasicrystalline/gravitational theorem. All P0–P5 and Penrose/quantum-gravity continuum gates remain **OPEN**.

## 1. What is new relative to the full Wilson/time-memory calculation

The preceding [full Wilson and temporal memory record](R3_FULL_WILSON_3D_SHELL_AND_TEMPORAL_MEMORY_2026-11-06.md) proved that one-step spatial Haar compression cannot be composed as a closed Markovian physical-time evolution; its leading two-step discrepancy was `5 beta_h² epsilon²` on the 20-face cubical slab. The present construction supplies (a) the **complete all-time gauge-invariant P/Q influence equation**, (b) an **exact sharp coupling norm on every coarse state**, not just the vacuum, and (c) the **first genuine two-scale comparison on the same physical 3D region**, retaining the same eight coarse boundary holonomy products.

## 2. Matching geometry, operator and projection

Let `G=SU(2)` with normalized Haar measure. The physical spatial slab `[0,2h]×[0,2h]×[0,h]` is meshed in two ways:

| | coarse mesh h | fine mesh h/2 |
|---|---:|---:|
| cell counts | 2×2×1 | 4×4×2 |
| vertices | 18 | 75 |
| edges | 33 | 170 |
| plaquettes | 20 | 128 |
| cubes | 4 | 32 |
| retained bottom fine links | 8 | 16 |
| unretained Haar-integrated links | 25 | 154 |
| **physical coarse boundary holonomies** | 8 links | 8 ordered products of two links |

The Euler characteristic is 1 on both. Let `J_h:L²(G^8)→L²(G^{E_h})` pull each coarse boundary observable back to the ordered original-link holonomy product; define `P_h=J_h J_h*` and `Q_h=I-P_h`. The normalized product Haar pushforward is again normalized Haar, so `J_h` is an isometry. Projection is gauge-covariant and restricts to the physical Gauss-invariant subspace. Importantly, on the fine lattice `P_{h/2}` retains eight **products**, not sixteen independent boundary edges. This identifies both retained spaces with the same coarse-observable algebra.

Use the full source-defined finite original-link Hamiltonian

```
H_h=K_h+V_h,    K_h=alpha_h sum_(e∈E_h) C_e,
V_h=beta_h sum_(p∈F_h) [1−(1/2)chi_1(U_p)],
alpha_h=g0(h)²/(2h),  beta_h=2/[g0(h)² h].
```

Here `C_e=−Δ_e≥0` has eigenvalues `j(j+1)` and `chi_1=tr_fund`. `H_h` is positive self-adjoint on the finite physical Hilbert space: `K_h` has the Peter–Weyl core and the finite Wilson potential is bounded, nonnegative, and gauge invariant. Since each link Casimir is bi-invariant, the product of the two fine-link electric heat semigroups preserves functions of their ordered holonomy product. Thus **P reduces K**, but not V.

## 3. Sharp cross-sector magnetic coupling on the entire retained space

**Lemma (both actual 3D meshes).** Under conditional Haar projection to the eight physical coarse boundary holonomies, for every face p and every pair of distinct faces p≠q,

```
P chi_1(U_p) P = 0,
P chi_1(U_p) chi_1(U_q) P = 0      if p≠q,
P chi_1(U_p)^2 P = P.
```

*Proof.* First condition on the individual fine bottom perimeter links. Every elementary face has at least one edge outside that perimeter, and for each pair p≠q at least one edge of their symmetric difference is outside it. Integrating such a unique unretained link annihilates a single fundamental character. For p=q, integrate one unretained edge using SU(2) Schur orthogonality: `int_G chi_1(gA)^2 dg=1`, independently of all the remaining fixed links. Then condition further from the 16 refined boundary links to their eight two-link products: the preceding identities are scalars at the finer conditioning and remain unchanged. The reproducibility program enumerates **all 190 coarse** and **8128 fine** unordered face pairs to certify the required geometry. ∎

Write the physical P/Q block decomposition of H as

```
A=PHP,   D=QHQ,   B=QHP=QVP.
```

Since the kinetic operator reduces P, the only off-diagonal term is the **bounded** Wilson potential. Using the lemma yields an **exact operator identity on all coarse boundary states**, not only on the Haar vacuum:

\[
\boxed{PVP=\beta_hF_hP,\qquad B^*B=PVQVP=\frac{\beta_h^2F_h}{4}P.}
\]

In particular `||B||=beta_h sqrt(F_h)/2`, and `B` is a constant multiple of an isometry on the coarse range. For the 20-face mesh `B*B=5 beta_h² P`; for the refined 128-face mesh `B*B=32 beta_{h/2}² P`. The physical Gauss subspace inherits these equalities.

## 4. Exact continuous-time (Volterra and Feshbach) influence theorem

The diagonal operators A and D are nonnegative self-adjoint in their own reducing K-form domains; B is bounded. Let `U_h(t)=P exp(−tH_h)P` on `ran P`, with `U_h(0)=I_P`. Eliminating the Q component by Duhamel gives **Theorem A**, on the generator core and equivalently in the mild evolution:

\[
\boxed{U_h'(t)=-A_hU_h(t)+\int_0^t\mathcal M_h(t-s)U_h(s)\,ds,
\qquad \mathcal M_h(t)=B_h^*e^{-tD_h}B_h\ge0.}
\]

The sign of the memory term is **positive** because the Q component generated by the negative off-diagonal coupling is itself negative. This is not a Markov approximation or a speculative influence path integral: it is an exact block-semigroup identity.

For any real z>0, the exact **Feshbach–Schur resolvent** is

\[
\boxed{P(H_h+z)^{-1}P=(A_h+z-\Sigma_h(z))^{-1},
\quad\Sigma_h(z)=B_h^*(D_h+z)^{-1}B_h
=\int_0^\infty e^{-zt}\mathcal M_h(t)\,dt.}
\]

This self-energy is energy dependent and operator valued; replacing it by a single scalar Wilson coupling would need an additional renormalization theorem.

### Explicit interacting finite memory bounds

Set `c_h²=beta_h² F_h/4` and `mu_h=3 alpha_h/4`. The constant state is in P; Q is orthogonal to it. Every nonconstant original-link representation has electric energy at least `3alpha_h/4`. Since `V≥0`,

`D=QHQ≥QKQ≥mu_h Q` and `0≤V≤2 beta_h F_h`.

Therefore, in **positive operator order**, for any t≥0 and z≥0,

\[
\boxed{\mathcal M_h(0)=c_h^2 I_P,\quad
0\le\mathcal M_h(t)\le c_h^2e^{-\mu_h t}I_P,\quad
0\le\Sigma_h(z)\le\frac{c_h^2}{z+\mu_h}I_P.}
\]

The interacting eliminated-state influence thus has a finite memory bound at each fixed regulator. It does **not** follow that the complete coarse evolution U(t), its vacuum-centered correlations, or the physical continuum spectrum have a common gap.

The vacuum channel has a sharper **positive resolvent sandwich**. Indeed `B1=−(beta_h/2) sum_p chi_1(U_p)` is an exact free-electric eigenvector with eigenvalue `3alpha_h` (four spin-1/2 links per elementary face). Operator monotonicity of the inverse, *not* an invalid assumption that the exponential is operator monotone, gives

\[
\boxed{\frac{c_h^2}{z+3\alpha_h+2\beta_hF_h}
\le\langle1,\Sigma_h(z)1\rangle
\le\frac{c_h^2}{z+3\alpha_h}.}
\]

The **free-electric** vacuum influence is exactly `c_h² exp(−3alpha_h t)`. Pointwise comparison of the interacting and free exponentials is **not claimed**, since K and V need not commute. The two resolvent bounds are rigorous for the full interacting finite Wilson model.

## 5. Exact discrete two-time and many-step transfer-memory recurrence

Let `T_e=e^(−eV/2)e^(−eK)e^(−eV/2)` with e>0, the positive symmetric fixed-grid SU(2) heat-kernel transfer from PR #65. Since K,V≥0, T_e is a positive contraction. Put

`A_e=PT_eP, B_e=QT_eP, D_e=QT_eQ`, and `U_n=PT_e^nP`.

**Theorem B (no time-factorization approximation):**

\[
\boxed{U_0=I_P,\quad U_{n+1}=A_eU_n+
\sum_{k=0}^{n-1}\mathscr L_{n-1-k}U_k,
\qquad\mathscr L_j=B_e^*D_e^jB_e\ge0.}
\]

At n=1, the exact two-step memory is `U_2−U_1²=B_e*B_e`. Because P reduces K, applying bounded-potential Duhamel to `M_e=e^(−eV/2)` gives `||Q M_e P||≤(e/2)||B||`. Expanding `Q M_e e^(−eK)M_eP` into P/Q paths, all other factors are contractions, hence

\[
\boxed{\|B_e\|\le e\|B\|=e c_h,\qquad
0\le\mathscr L_j\le e^2c_h^2 I_P\quad(j\ge0).}
\]

For each fixed spatial lattice and e>0, the transfer is compact and has norm strictly below 1 (the nonconstant, nonnegative Wilson potential has no nonzero L² support on its zero set); thus the memory-series decay rate is finite-regulator dependent. No rate uniform in volume or h is claimed. On every fixed-grid smooth Peter–Weyl core, `e^(−2) mathscr L_0→c_h² I_P` strongly as e→0, recovering the 20-face and 128-face leading coefficients.

## 6. Genuine two-scale quantitative result and its limitation

The two physical boundary spaces are canonically identified with `L²(SU(2)^8)`. Let `g_c=g0(h)` and `g_f=g0(h/2)`.

\[
\boxed{\frac{c_{h/2}^2}{c_h^2}
=\frac{128}{5}\left(\frac{g_c}{g_f}\right)^4,
\quad\|\mathcal M_{h/2}(0)-\mathcal M_h(0)\|=|c_{h/2}^2-c_h^2|.}
\]

For locally decreasing bare coupling `g_f≤g_c`, the bare zero-time memory grows by at least **25.6** across this one dyadic refinement. This is an exact finite **unrenormalized** comparison, not a physical divergence proof. The exact free-electric vacuum difference at physical time t is

\[
c_{h/2}^2 e^{-3\alpha_{h/2}t}-c_h^2e^{-3\alpha_h t}.
\]

For the actual interacting kernels, the explicit, but **not-small**, two-scale estimate is

\[
\boxed{\|\mathcal M_{h/2}(t)-\mathcal M_h(t)\|
\le c_{h/2}^2e^{-\mu_{h/2}t}+c_h^2e^{-\mu_ht}.}
\]

Because the coefficients can grow rapidly along the weak-bare-coupling refinement trajectory, this bound does **not** establish a summable renormalization comparison or a continuum positive mass gap.

**Why decay of the memory itself is insufficient.** The positive 2×2 toy Hamiltonian `[[1,1−δ],[1−δ,1]]`, for any `0<δ<1`, has an eliminated-state memory `(1−δ)^2e^{−t}` decaying at rate 1, while the total Hamiltonian has an arbitrarily soft eigenvalue δ. The entire energy-dependent Schur complement and physical vacuum sectors must be controlled.

## 7. Executed independent verification and next theorem contract

The companion executable reconstructs oriented cubical geometry and validates **all 190+8128 distinct face pairs**, Euler identities, the retained eight holonomy products and exact dimensional counts. It checks SU(2) fundamental first/second Haar moments using the 8-element quaternion group, which is exact for moments up to degree two only—not a substitute for higher-spin recoupling. The independent 17-character finite Peter–Weyl toy matrix checks Feshbach and the all-step Volterra recurrence to machine precision. Exact formulas, strict operator inequalities and their domain assumptions constitute the analytic proof; numerical tests are independent regressions rather than evidence of an infinite-dimensional continuum theorem.

**Open path**: (1) define a **physically renormalized, gauge-invariant coarse observable map** with fixed physical support; (2) carry the non-Markovian influence and higher-spin channels into an actual interacting two-scale effective action; (3) obtain a summable, physical-time weighted difference for the full Schur complement along `g0(h)→0` and increasing physical volume; (4) independently prove a nontrivial 4D OS continuum and spectral exclusion; (5) separately develop the genuine 3D Penrose-related regulator and a physically justified gravitational fluctuation operator. No current bound completes those steps.

**Final classification:** exact **finite** P/Q influence kernel, discrete time-memory recurrence, sharp bare magnetic coupling and first physically matched cubic refinement comparison. **Mass gap, Penrose transfer, and quantum-gravity ultraviolet finiteness all OPEN.**
