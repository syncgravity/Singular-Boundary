# P0–T2: exact magnetic-information loss under naive Haar holonomy blocking

**Date:** November 5, 2026  
**Scope:** finite open cubical original-link SU(2) Hamiltonians at two dyadic spatial resolutions. This is a new exact *obstruction for one specified coarse-graining map*, not a no-go theorem for renormalization, the interacting Yang–Mills theory, a continuum mass gap, or quasicrystalline gravity. Independent mathematical review is required before theorem-ledger certification.

## 1. Existing source basis and actual new question

The current research records already establish finite oriented cubical refinement (R3-IR-586), a physical Gauss-invariant SU(2) Kogut–Susskind Hamiltonian (R3-IR-587/589), an anisotropic finite heat-kernel time transfer (R3-IR-590 and the November 4 P0 action audit), and the observation that a coarse four-link Wilson loop becomes eight original links on dyadic refinement. The prior P0 audit correctly warned that this elementary holonomy pullback does not intertwine the bare Hamiltonians.

The additional mathematical question settled here is stronger and more diagnostic:

> **If one uses the natural gauge-covariant holonomy-product cylinder injection and its Haar-adjoint conditional expectation, does the compressed *refined magnetic interaction* retain any coarse Wilson-plaquette dependence?**

The answer is **no**. The exact compression is a scalar. The refined magnetic dynamics also creates a nonzero, quantitatively computable component orthogonal to the entire coarse-cylinder subspace. Consequently no scalar vacuum-energy counterterm and no electric-coupling adjustment can turn this simple compression into the original coarse interacting Hamiltonian.

## 2. Mathematical setup

Let `G_n` be the open cubical one-skeleton of `[0,1]^3` with mesh `h=1/n` and standard oriented links. Set `G_{2n}` to be its dyadic refinement, with mesh `h/2` and the full new three-dimensional edge and face sets. Denote their edge sets by `E_n,E_{2n}` and plaquette sets by `F_n,F_{2n}`, where

\[
 |F_n|=3n^2(n+1),\qquad |F_{2n}|=3(2n)^2(2n+1).
\]

For a coarse oriented link `e`, write its two positively oriented fine sublinks as `e_1,e_2`. For each fine-link configuration `U`, define the **coarse holonomy projection**

\[
 p_n:SU(2)^{E_{2n}}\longrightarrow SU(2)^{E_n},\qquad
 (p_nU)_e=U_{e_1}U_{e_2}.
\]

Since the product of independent Haar-distributed group variables is Haar, `p_n` pushes normalized product Haar on fine links to product Haar on coarse links. The pullback

\[
 (J_nf)(U)=f(p_nU)
\]

is consequently an isometric injection from `L²(SU(2)^{E_n})` to `L²(SU(2)^{E_{2n}})`. It maps the **coarse Gauss-invariant subspace** into the **fine Gauss-invariant subspace**: internal midpoint gauge transformations cancel in the link product and transformations at coarse vertices act at the endpoints. Its adjoint `J_n^*` is precisely conditional Haar expectation onto the coarse holonomy products. Write `P_n=J_nJ_n^*` for the orthogonal fine-cylinder projection.

Set `C_e=-Δ_e` for the nonnegative bi-invariant SU(2) Casimir normalized by `C_e χ_{1/2}=3χ_{1/2}/4`. On the respective physical Hilbert spaces define

\[
 \begin{aligned}
 K_h&=\alpha_h\sum_{e\in E_n}C_e, & \alpha_h&=\frac{g_0(h)^2}{2h},\\
 V_h&=\beta_h\sum_{p\in F_n}(1-\tfrac12\chi_1(U_{\partial p})), & \beta_h&=\frac{2}{g_0(h)^2 h},\\
 H_h&=K_h+V_h, && g_0(h)>0.
 \end{aligned}
\]

Here `χ_1(U)=tr_fund(U)` is the real, unnormalized, two-dimensional fundamental character, with `∫χ_1=0` and `∫χ_1²=1` under normalized SU(2) Haar; the usual *Wilson potential* uses `χ_1/2`. The notation `χ_1` follows the highest-weight label-1 convention, equivalent to spin `j=1/2`. All forms below are evaluated first on smooth cylindrical Peter–Weyl vectors, including the Gauss-invariant core; statements involving the compressed unbounded operator are quadratic-form or core identities.

## 3. Theorem: exact compression and a quantitative operator mismatch

**Theorem (naive Haar blocking, finite cubical lattice).** For every `n≥1` and all positive bare couplings at both resolutions,

\[
\boxed{\begin{aligned}
 J_n^* K_{h/2} J_n&=2\alpha_{h/2}\sum_{e\in E_n}C_e,\\
 J_n^* V_{h/2} J_n&=\beta_{h/2}|F_{2n}|I,\\
 J_n^*H_{h/2}J_n&=2\alpha_{h/2}\sum_{e\in E_n}C_e+\beta_{h/2}|F_{2n}|I.
\end{aligned}}
\]

Thus the compressed magnetic term has **no surviving coarse plaquette interaction**, even though the natural cylinder injection is isometric and gauge compatible. Moreover, on the normalized constant physical state `1`,

\[
\boxed{\bigl\|(I-P_n)H_{h/2}J_n1\bigr\|_{2}
=\frac{\beta_{h/2}}2\sqrt{|F_{2n}|}>0.}
\]

For **every real scalar shift** `c` and every choice of electric coefficients,

\[
\boxed{\bigl\|\left[J_n^*H_{h/2}J_n-H_h-cI\right]1\bigr\|_2
\ge\frac{\beta_h}{2}\sqrt{|F_n|}>0,}
\]

and equality is attained by the scalar shift

\[
 c=\beta_{h/2}|F_{2n}|-\beta_h|F_n|.
\]

The lower bound refers to the unnormalized bare Hamiltonians on the normalized Haar-constant vector. It is **not** a lower bound on any physical mass gap or on a renormalized Schwinger-function error.

### Proof

1. **Isometry and Gauss compatibility.** Each pair `(U_{e_1},U_{e_2})` has independent Haar law, and its product has normalized Haar law. Different coarse links use disjoint pairs. Thus `p_{n*} Haar_fine=Haar_coarse`; Gauss covariance follows by cancelling intermediate vertex rotations. Therefore `J_n^*J_n=I` on the full and physical coarse spaces.

2. **Electric part.** For any smooth function of a group product `U_{e_1}U_{e_2}`, bi-invariance of the SU(2) Casimir implies

   \[
   C_{e_1}(f\circ p_n)=(C_ef)\circ p_n,
   \qquad C_{e_2}(f\circ p_n)=(C_ef)\circ p_n.
   \]

   All other fine-link Casimirs annihilate that cylinder function. Hence `K_{h/2}J_n=J_n[2α_{h/2}Σ_eC_e]`, giving the first identity upon applying `J_n^*`.

3. **Magnetic part.** Every elementary fine plaquette has at least one fine edge *outside* the subdivided coarse one-skeleton. Indeed, a fine lattice edge lies on a subdivided coarse edge only when its two transverse fine-grid coordinates are even. For any fine plaquette in coordinate directions `i,j`, its two parallel `i`-directed boundary edges have transverse `j` coordinates differing by one; one is odd. Hence at least one is off the coarse one-skeleton, for **every** `n`, independently of finite verification. The checker also enumerates this property on several finite grids. Condition on every coarse holonomy product and all other fine links except one such off-skeleton edge. That edge is still independent Haar and appears exactly once (possibly inverse) in the fine plaquette holonomy word. Since `∫_{SU(2)}χ_1(AUB) dU=0`, its conditional expectation vanishes. Consequently, for **every** fine face `p`,

   \[
    J_n^*\chi_1(U_{\partial p})J_n=0
   \]

   as a multiplication form (equivalently, `E[χ_1(U_{∂p})|p_nU]=0`). Summing the finite face set proves the scalar magnetic compression.

4. **Orthogonality of plaquette characters.** For distinct elementary plaquettes `p≠q`, some edge belongs to one loop but not the other. Integrating over that unique Haar edge gives `⟨χ_p,χ_q⟩=0`. Each `χ_p` has Haar squared norm one: one edge in its holonomy product is Haar, and the fundamental character is orthonormal to itself. Therefore

   \[
    \left\|\sum_{p\in F_{2n}}\chi_p\right\|_2^2=|F_{2n}|,
    \qquad\left\|\sum_{p\in F_n}\chi_p\right\|_2^2=|F_n|.
   \]

   On the fine constant state, `K_{h/2}J1=0`. The magnetic nonconstant part is `-β_{h/2}Σ_pχ_p/2`, entirely orthogonal to the `J_n`-cylinder subspace by Step 3. This yields the leakage equality. Likewise, the coarse-vs-compressed Hamiltonian difference applied to the constant state is a scalar plus `+β_hΣ_{p∈F_n}χ_p/2`. The scalar and all plaquette characters are mutually orthogonal, so minimizing over the scalar shift leaves exactly the announced norm.

No claim about the interacting vacuum is made: the reference vector `1` is the kinematic Haar constant, not the interacting ground state for nonzero magnetic coupling. ∎

## 4. Exact free-electric benchmark for a fixed-physical-size loop

For a simple axis-aligned nonselfintersecting coarse Wilson loop with `L_h=P/h` occupied links and fixed physical perimeter `P>0`, its unnormalized fundamental character is a physical, normalized Haar state. Every occupied link carries fundamental Casimir `3/4`, so

\[
\boxed{K_h\chi_{C_h}=E_h^{(E)}\chi_{C_h},\quad
E_h^{(E)}=\frac{3g_0(h)^2 P}{8h^2}.}
\]

The natural refined loop `C_{h/2}` contains `2L_h` fine links, and its free-electric energy satisfies

\[
 \frac{E_{h/2}^{(E)}}{E_h^{(E)}}=4\frac{g_0(h/2)^2}{g_0(h)^2}.
\]

The **exact** free-electric intertwinement condition for this holonomy-product injection is `α_h=2α_{h/2}`, equivalently

\[
\boxed{g_0(h/2)^2=\frac14 g_0(h)^2.}
\]

This scaling is not the expected 4D logarithmic asymptotically free bare-coupling trajectory. Along any `g_0(h)^2\sim c/\log(1/h)`, the bare free-electric loop energy grows like `P/[h²\log(1/h)]`, so its **free-electric** connected normalized Haar two-point function `exp[-t E_h^(E)]` vanishes for any fixed physical `t>0`. This is a free-electric calculation, **not** an interacting YM mass-gap or continuum-Wilson-loop theorem. In particular it does **not** imply that a properly renormalized and smeared interacting observable cannot have a nontrivial continuum limit.

## 5. What mathematical work this changes

The P0 audit already identified a failure of naive dynamical intertwining for bare subdivided links. The theorem above identifies the **exact missing magnetic information**: product-Haar conditional coarse-graining integrates every refined magnetic character to zero. It cannot be repaired by tuning one scalar gauge coupling, modifying only the free-electric coefficient, or subtracting a vacuum energy. The finer magnetic interaction also leaks outside the coarse cylinder with known positive norm.

The **next testable P0/T2 requirement** is therefore a nontrivial **face-aware gauge-covariant blocking** or an explicitly **renormalized observable/action dictionary**, not another attempt to equate the bare generators under their kinematic Haar measures. A candidate construction must declare:

- the fine interacting Euclidean measure (or positive time transfer) and the conditions under which coarse variables are distributed;
- a gauge-covariant map retaining physical plaquette information, or a controlled effective action generated by conditional integration under the interacting rather than product-Haar measure;
- renormalized, physically supported gauge-invariant observables and their normalization/centering;
- a one-step quantitative interacting correlation comparison uniform enough to iterate over h→h/2 and spatial volume, with physical time fixed;
- nontrivial OS continuum reconstruction and physical spectral exclusion before any mass-gap claim.

Averaging under a genuinely interacting measure need not yield the Haar projection used above; therefore the theorem leaves the renormalization program logically open. The Penrose model still needs a **separate genuine 3D geometry and operator identity** before any transfer can be tested. The gravitational fluctuation operator and ultraviolet theory remain independent of this gauge-blocking result.

## 6. Verification and preservation

The accompanying executable checks the 3D coarse/fine cubical incidence for `n=1,2,3,4,8`, counts skeleton and off-skeleton edges, confirms every fine plaquette has an unused edge, and verifies pairwise-distinct plaquette supports. It independently integrates exact SU(2) Haar character moments symbolically via the Weyl class formula and performs a fixed-coarse-boundary Monte Carlo sanity check for the 2×2 refined face. These finite machine checks verify the enumerated hypotheses; the theorem follows from the general incidence and SU(2) Haar arguments above, not from finite sampling.

**Status:** Exact finite-model coarse-cylinder compression/orthogonality theorem and its bare operator mismatch are established subject to mathematical review. P0 physical continuum regulator, P2 uniform interacting multiscale control, P4 physical gap, P5 nontrivial 4D OS reconstruction, quasicrystalline transfer T0–T5, and quantum-gravity ultraviolet claims all remain **OPEN**.

**Source anchor files (before this continuation):**

- `research/theorems/R3_FIXED_DOMAIN_CUBICAL_CHAIN_REFINEMENT_2026-10-31.md` (R3-IR-586)
- `research/theorems/R3_CUBICAL_SU2_FULL_PHYSICAL_STRONG_COUPLING_GAP_2026-10-31.md` (R3-IR-589)
- `research/theorems/R3_CUBICAL_SU2_FINITE_TRANSFER_POSITIVITY_2026-10-31.md` (R3-IR-590)
- `research/audits/P0_CUBIC_HEAT_KERNEL_TRANSFER_CERTIFICATE_2026-11-04.md`
- `docs/research/YM_CUBIC_PENROSE_TRANSFER_AND_INFRARED_GATES_2026-11-05.md`