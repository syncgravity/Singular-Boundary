# The Singular Boundary — Renormalized Wilson-loop frames: construction, spectral obstruction, and continuum gate

**Date:** 26 October 2026. **Status:** Proven finite-volume low-spin/multiloop electric frame, uniform-in-refinement *energy-form upper* bounds for interacting fundamental Wilson sources, volume-counting obstruction, and a precise frame/infrared gap-equivalence theorem. The simultaneous interacting continuum frame with lower observability and infrared suppression is **not proved**.

## 0. Source model and conventions

Take a finite genuine Penrose rhombus patch G=(V,E,F) with simple four-edge faces and at most two faces incident to each edge. Gauge group SU(2), spatial physical Hilbert space \(\mathscr H_G=L^2(SU(2)^E)^{SU(2)^V}\), Casimir normalization \(-\Delta\chi_j=j(j+1)\chi_j\), and Hamiltonian

\[
H_{h,G}=\sum_{e}a_e(-\Delta_e)+\sum_fb_f(1-p_f),\qquad p_f=\tfrac12\operatorname{Tr}_{1/2}W_f, \quad a_e>0,b_f\ge0.
\]

Its unique positive normalized ground state is \(\Omega\). Put \(K=H-E_0\), \(Q=I-|\Omega\rangle\langle\Omega|\), \(P_s=\mathbf1_{(0,s]}(K)\). These operators are always understood on the **physical** gauge-invariant Hilbert space. The interaction strengths may vary by rhombus; all calculations below are finite-volume rigorous. No claim is made that literal Stage 26 couplings are certified without `stage7_checkpointed.setup_geometry`.

For the concrete refined-geometric bounds additionally assume the *specified* dual-area rule:
\[
A_f=h^2\sigma_f,\quad \sigma_f\in\{\sigma_-:=\sin(\pi/5),\sigma_+:=\sin(2\pi/5)\},\quad
w_e=\tfrac{1}{2h^2}\sum_{f\ni e}A_f,
\]
\[
a_e=\frac{g_3^2}{2w_e},\qquad b_f=\frac4{g_3^2 A_f},\qquad
\varphi=\sigma_+/\sigma_-=(1+\sqrt5)/2.
\]
For open boundaries the one-sided weight is retained. Then \(a_e\le g_3^2/\sigma_-\), regardless of patch and h.

## 1. A constructive low-spin *energy-form upper* family at arbitrary magnetic coupling

**Theorem F1 (renormalized fundamental Wilson test-function estimate).** Let \(\phi\) be any real function evaluated at face locations \(x_f\), with finite physical support. Define
\[
\Phi_{h,G}[\phi]=\frac1h\sum_{f\in F} A_f\phi(x_f)\bigl(p_f-\langle p_f\rangle_\Omega\bigr).
\]
Then for every magnetic coupling (no smallness requirement)
\[
\boxed{\langle \Phi[\phi]\Omega,K\Phi[\phi]\Omega\rangle
\le 2\varphi g_3^2\sum_f A_f|\phi(x_f)|^2.}\tag{F1}
\]
Consequently, for any family of sampling functions \(\phi_i\) with a discrete Bessel bound
\[\sum_fA_f|\sum_i c_i\phi_i(x_f)|^2\le B\sum_i|c_i|^2\]
with B independent of h and G, the same source family has the energy-form Bessel bound
\[\boxed{\big\langle\sum_i c_i\Phi_i\Omega,K\sum_j c_j\Phi_j\Omega\big\rangle\le 2\varphi g_3^2B\sum_i|c_i|^2.}\tag{F2}\]
This is **not** a Hilbert-space frame lower bound, and not an infrared estimate.

*Proof.* The ground-state transform and the double-commutator identity yield the exact equality
\[\langle A\Omega,KA\Omega\rangle=\sum_ea_e\int|\nabla_e A|^2|\Omega|^2dU\]
for a real smooth gauge-invariant multiplier A. For a simple face, \(\|\nabla_ep_f\|_\infty\le1/2\) when e belongs to its boundary, zero otherwise. Thus
\[
|\nabla_e\Phi|^2\le\frac1{4h^2}\left(\sum_{f\ni e}A_f|\phi_f|\right)^2
\le\frac1{2h^2}\sum_{f\ni e}A_f^2|\phi_f|^2.
\]
Each face has four edges, hence \(\sum_e|\nabla_e\Phi|^2\le (2/h^2)\sum_fA_f^2|\phi_f|^2\). Use \(A_f^2\le\sigma_+h^2 A_f\) and \(a_e\le g_3^2/\sigma_-\) to obtain F1. Replacing \(\phi\) by a linear combination gives F2. QED.

**Normalization and complexity audit.** The factor \(h^{-1}\) gives an h-independent first-energy-moment bound for fixed \(\|\phi\|_{L^2}\) in a fixed physical region. Only fundamental SU(2) characters occur. The physical support can be fixed. The number of underlying plaquette terms necessarily grows as \(O(h^{-2})\) for an area of fixed physical size, and the \(L^\infty\) source norm may grow as \(O(h^{-1})\). Neither the variance \(\|\Phi\Omega\|^2\) nor any lower frame bound is proved. **Uniform energy-form normalization is not the same as uniform Hilbert-space normalization.**

### Fixed-degree multiloop products

For nonempty face sets D of total area \(\mathcal A_D\), let \(W_D=\mathcal A_D^{-1}\sum_{f\in D}A_fp_f\), \(\|W_D\|_\infty\le1\). For a *fixed* integer q and physical regions \(D_1,\ldots,D_q\), define
\[\mathcal O_{h;D_1,\ldots,D_q}=h^{-1}\left(\prod_{k=1}^qW_{D_k}-\left\langle\prod_{k=1}^qW_{D_k}\right\rangle\right).\]
**Theorem F3.** For any such product,
\[\boxed{\langle\mathcal O\Omega,K\mathcal O\Omega\rangle
\le 2\varphi g_3^2 q\sum_{k=1}^q\mathcal A_{D_k}^{-1}.}\tag{F3}\]
*Proof.* Apply the Leibniz rule, \(|W_D|\le1\), Cauchy–Schwarz \(|\sum_{k=1}^qv_k|^2\le q\sum_k|v_k|^2\), and the single-block area-average estimate \(\langle W_D\Omega,KW_D\Omega\rangle\le2\varphi g_3^2h^2/\mathcal A_D\). Centering does not affect gradients. QED.

These fixed-degree products are genuine low-spin multiloop multipliers with uniform energy-form bound for fixed physical block areas. But **products of plaquette traces alone are not algebraically complete**: mixed-holonomy traces such as \(\operatorname{Tr}(UV)\) are independent information from \(\operatorname{Tr}(U),\operatorname{Tr}(V)\). Unsmoothed noncontractible loops have support length increasing as \(h^{-1}\) or L/h, and their energy-form estimates are not uniformly bounded by F1/F3.

## 2. Exact *lower* Wilson frame for the physical electric reference Hamiltonian

**Theorem F4 (uniform-complexity low-energy electric spin-network frame).** Assume \(b_f=0\), \(a_e\ge a_->0\), and fix physical energy \(\eta>0\). Let \(\mathscr E_\eta=\operatorname{Ran}\mathbf1_{(0,\eta]}(H_E)\). There is an orthonormal collection of gauge-invariant finite Wilson-trace polynomials \(\{S_\alpha\}\) which spans \(\mathscr E_\eta\), satisfies
\[\boxed{\sum_\alpha|\langle\psi,S_\alpha\Omega_E\rangle|^2=\|\psi\|^2\quad(\psi\in\mathscr E_\eta),}\tag{F4}\]
and has **uniform** (G-, h-independent, at fixed \(\eta/a_-\)) complexity bounds:
\[
\#\{e:j_e>0\}\le M:=\left\lfloor\frac{4\eta}{3a_-}\right\rfloor,
\qquad j_e\le J:=\frac{\sqrt{1+4\eta/a_-}-1}{2}.
\]
Every polynomial S_α can be expanded into fundamental-representation Wilson-loop traces and their products with at most \(2\sum_ej_e\le2JM\) total fundamental edge traversals per monomial. The number of sources grows with patch volume; a uniform bound on *each source's complexity* is not a uniform bound on *the total number of sources*.

*Proof.* Gauge-invariant Peter–Weyl spin networks form an orthonormal eigenbasis for \(H_E\), each basis vector labeled by edge spins \(j_e\) and vertex invariant intertwiners. Its energy is \(\sum_ea_ej_e(j_e+1)\). Each nonzero edge costs at least \(3a_-/4\), and every individual spin costs at least \(a_-j_e(j_e+1)\). This proves M and J. By SU(2) invariant tensor calculus, each spin-j matrix coefficient is a symmetric tensor of 2j fundamentals, and invariant contractions pair fundamental indices into closed strands; this expresses each spin-network function as a finite linear combination of products of fundamental Wilson traces whose total traversals do not exceed \(2\sum_ej_e\). Each basis member is therefore a finite Wilson polynomial. The constant vacuum \(\Omega_E=1\); the nonconstant spin networks are already orthogonal to it. The Parseval identity follows from orthonormality. QED.

The individual source support can have several distant connected components: uniform **total occupied-edge count** is not uniform spatial diameter, and the source *count* can grow as a polynomial in |E|. This exact frame cannot be carried to \(b_f\asymp h^{-2}\) by assuming perturbative closeness of ground states or low-energy spectral projectors.

### A fully explicit, low-spin face subframe

At \(b_f=0\), set \(A_f=\chi_{1/2}(W_f)=\operatorname{Tr}_{1/2}W_f\). For distinct rhombi with distinct edge sets,
\[\langle A_f\Omega_E,A_g\Omega_E\rangle=\delta_{fg},\quad H_E A_f\Omega_E=\kappa_f A_f\Omega_E,\quad \kappa_f=\frac34\sum_{e\in\partial f}a_e.\tag{F5}\]
The norm is one by SU(2) character orthogonality; off-diagonal inner products vanish by Haar integration on an edge belonging to one face and not the other. In particular, for a_e=a,
\[\kappa_f=3a,\quad \dim\operatorname{span}\{A_f\Omega_E\}_{f\in F}=|F|.\]
The \(A_f\) therefore give an exact Parseval frame of that elementary electric excitation subspace, with **one spin-1/2, four-edge operator per face**, uniformly in G and h.

## 3. An unavoidable volume-counting obstruction

**Theorem F6 (low-energy frame source budget).** Let \(\mathscr E\) be an N-dimensional physical excited-state subspace, and \(b_i=QA_i\Omega\). If the weighted sources observe that subspace with a lower frame bound c>0,
\[\sum_iw_i|\langle\psi,b_i\rangle|^2\ge c\|\psi\|^2\quad(\psi\in\mathscr E),\]
then necessarily
\[\boxed{cN\le\sum_iw_i\|P_{\mathscr E}b_i\|^2\le\sum_iw_i\|A_i\|_\infty^2.}\tag{F6}\]
*Proof.* Sum the lower frame inequality over an orthonormal basis of E and interchange the nonnegative sums. QED.

Apply F6 at zero magnetic coupling to the |F| orthonormal face excitations F5, with all \(\kappa_f\le3a_+\). At any energy threshold \(\eta\ge3a_+\), \(N\ge|F|\). If \(\|A_i\|_\infty\le M_0\), then \(\sum_iw_i\ge c|F|/M_0^2\). In particular, a bounded number/total weight of uniformly bounded local probes cannot observe the complete low-energy band uniformly in growing volume. A **frame density** with O(number of faces) source budget is mathematically natural.

For periodic complexes, contractible loops alone fail even qualitative completeness outside the center-neutral sector because of the exact \(\mathbb Z_2\) one-form center symmetry. Noncontractible winding loops are needed to observe charged sectors; their physical support/edge length necessarily scales with the torus circumference. This is a separate boundary/topology obstruction.

## 4. The exact point where the sought simultaneous frame would prove the gap

**Theorem F7 (uniform frame + collective infrared bound implies a positive gap).** Fix \(\eta>0\), \(p>0\). Suppose, for *each* admitted h,G and boundary type, there are gauge-invariant Wilson sources \(b_i=QA_i\Omega\) and weights \(w_i>0\) satisfying
\[
\sum_iw_i|\langle\psi,b_i\rangle|^2\ge c\|\psi\|^2\quad (\psi\in\operatorname{Ran}P_\eta),\tag{O}
\]
\[
\sum_iw_i\|P_sb_i\|^2\le Cs^p\quad (0<s\le\eta),\tag{IR}
\]
with \(c,C>0\) independent of h,G and boundary. Then
\[\boxed{\operatorname{gap}(H_{h,G})\ge\min\{\eta,(c/C)^{1/p}\}.}\tag{F7}\]
*Proof.* If \(\operatorname{Ran}P_s\) is nonzero for \(0<s\le\eta\), sum (O) over an orthonormal basis in that space. Its dimension N_s satisfies
\[cN_s\le\sum_iw_i\|P_sb_i\|^2\le Cs^p.\]
Since N_s≥1, \(s\ge(c/C)^{1/p}\). There are no excitations below the claimed threshold. QED.

For an infrared response bound based on inverse energy moments, typically p>1 is needed. However, **any p>0** together with uniform O and IR already proves a spectral gap. Consequently, establishing both is essentially a mass-gap theorem; they cannot be obtained from Wilson algebraic density, positivity, or geometric C5 covariance alone.

F6 moreover shows that if the source budget is extensive, the collective constant C in (IR) will generally be extensive unless an additional *model-specific* local spectral suppression or spatial localization mechanism is proved. Bounding each source individually does not prevent the sum from growing like |F|.

## 5. Why the two proven constructions cannot presently be spliced

* F1/F3 give spatial-refinement-uniform **positive first energy moments** for low-spin, physically supported Wilson averages, but they give no variance lower bound, no Hilbert frame lower bound, and no *low*-energy spectral upper bound. At fixed variance, their first-moment bound even allows (or forces) the spectrum toward low energies.
* F4/F5 give exact quantitative *Hilbert* observability for the physical electric reference dynamics, but b=0 is not the continuum magnetic trajectory b_f\asymp h^-2. Under that trajectory the interacting ground state and the spectral projections are not known to be uniformly close to their electric limits.
* The complete finite Wilson trace algebra is qualitatively dense in the physical Hilbert space (Thierry Lévy, *Wilson loops in the light of spin networks*, J. Geom. Phys. 52 (2004), 382–397, DOI 10.1016/j.geomphys.2004.04.003), but density supplies no h,L-independent lower frame constant or source complexity.
* Spatially flowed Wilson loops are a plausible physically regularized source class; 3D Euclidean Yang–Mills state-space work of Cao–Chatterjee provides motivation for positive-flow-time Wilson observables. Such work does not prove Penrose Hamiltonian spectral convergence or the desired frame conditions, and finite-time flow introduces its own locality/support issues.
* C5 transport preserves these inequalities on exactly isomorphic weighted gauge complexes; the geometric complex structure J supplies no proven improvement of c or C.

## 6. Rigorous acceptance conditions for a genuine interacting renormalized Wilson frame

A future all-coupling R3/R2 proof must construct from actual Wilson dynamics a family A_{i,h,L} (including mixed and winding holonomies where required), and establish:

1. **Physical normalization:** a specified renormalization prescription, finite nonzero vacuum variances/overlap normalization or an equivalent frame-normalization control, and a physical continuum interpretation of the sources.
2. **Localized complexity:** uniform degree/representation bounds or a proven scale-dependent tail estimate for degrees and Wilson path lengths; support controlled in physical units, and total *source density* rather than total source number controlled when volume grows.
3. **Interacting low-energy observability:** a positive c in (O) independent of h,L and admitted boundaries, with a clear treatment of the zero-form/one-form superselection sectors and global winding operators.
4. **Independent infrared suppression:** a dynamically derived low-energy estimate with the proper source-count normalization. A *collective* bound (IR) with uniform C already implies a gap by F7; a local-per-block alternative needs an additional spatial localization/tensorization theorem rather than pretending an extensive sum is uniformly bounded.
5. **Continuum gate R2:** a uniform physical-time transfer normalization, convergence of the relevant continuum observables/correlators and physical Hamiltonian, and proof that the spectral inequalities survive the limiting state and boundary construction.

**Not proved:** Items 1–5 simultaneously for fully interacting center-neutral Penrose SU(2) along the continuum trajectory. No 2+1-dimensional physical continuum mass-gap theorem is claimed. No Stage 26 or Stage 35 computation is required for these analytic findings.