# P0–T2: exact planar SU(2) character blocking and generated coarse interactions

**Research continuation, November 5, 2026.** **Scope:** an exact finite **two-dimensional planar face-patch** integration within a cubical spatial lattice, using a specified central plaquette weight and independent Haar integration of the face-interior original links. This is a standard character-convolution mechanism specialized to the source-correct cubic regulator comparison. **It is NOT the full interacting 3D cubic effective action**, a renormalized continuum limit, Yang–Mills gap proof, or a Penrose transfer theorem. Mathematical scope subject to review.

## 1. The exact local blocking operation

Fix an oriented simply connected square-grid disk `B` with `F` fine plaquettes, outer boundary holonomy `U_{∂B}`, and fundamental SU(2) character `χ_1(U)=tr_fund U`. Let the *isolated planar patch* have central, gauge-invariant weight

\[
 w_t(U_p)=\exp[t\chi_1(U_p)],\qquad t>0.
\]

The interior fine links are integrated against product normalized Haar, with boundary links fixed. Expand the central weight into irreducible characters indexed by integer highest weight `n≥0`, with `d_n=n+1`:

\[
 w_t(U)=\sum_{n\ge0}a_n(t)\chi_n(U),\qquad
 a_n(t)=\int_{SU(2)}w_t(U)\chi_n(U)\,dU.
\]

**Proposition (exact face-block kernel).** The blocked weight is

\[
\boxed{ Z_B(U_{\partial B};t)
  =\int\prod_{p\subset B} w_t(U_{\partial p})\prod_{e\in E_{\rm int}}dU_e
  =\sum_{n\ge0}\frac{a_n(t)^F}{(n+1)^{F-1}}\chi_n(U_{\partial B}). }
\]

**Proof.** Expand each positive central weight into its absolutely convergent SU(2) character series. Along any interior edge, two adjacent plaquettes traverse the link with inverse orientation. Schur orthogonality

\[
\int_{SU(2)}\chi_n(AU)\chi_m(U^{-1}B)\,dU
=\frac{\delta_{nm}}{d_n}\chi_n(AB)
\]

forces the two adjacent representation labels to match. Connectedness of the dual face graph therefore forces *all* face labels to equal one `n`. All internal-edge contractions contribute `d_n^{-E_int}`; interior index loops contribute `d_n^{V_int}`; Euler's disk relation gives `V_int−E_int=1−F`. The one remaining boundary index loop produces `χ_n(U_{∂B})`. Summing over `n` proves the formula. ∎

This is the exact central-function convolution law of **two-dimensional lattice gauge theory**, not a proposed novel solution of four-dimensional Yang–Mills.

## 2. Coefficients and a dyadic plaquette block

The SU(2) Weyl class formula yields

\[
 a_n(t)=\frac2\pi\int_0^\pi\!\sin^2\theta\,e^{2t\cos\theta}\,
 \frac{\sin((n+1)\theta)}{\sin\theta}\,d\theta
 =I_n(2t)-I_{n+2}(2t)
 =\frac{n+1}{t}I_{n+1}(2t),
\]

where `I_n` is the modified Bessel function. In particular, `a_0=1+t²/2+O(t⁴)`, `a_1=t+t³/3+O(t⁵)`, and `a_2=t²/2+O(t⁴)`.

For the **four** elementary faces of one dyadically subdivided coarse face (`F=4`),

\[
\boxed{Z_{2\times2}(U;t)
 =\sum_{n\ge0}\frac{a_n(t)^4}{(n+1)^3}\chi_n(U).}
\]

After dividing by the scalar coefficient `a_0(t)^4`, the normalized **fundamental** coarse character coefficient is exactly

\[
\boxed{c_1(t)=\frac{a_1(t)^4}{8a_0(t)^4}
=\frac{t^4}{8}-\frac{t^6}{12}+\frac{t^8}{24}+O(t^{10}).}
\]

The first nontrivial higher-spin coefficient is `c_2(t)=a_2(t)^4/(27a_0(t)^4)=t^8/432+O(t^10)`. Thus a fine **fundamental Wilson plaquette weight** generates a coarse central weight with multiple characters. It is **not** generally an exact one-parameter fundamental Wilson weight `exp[t_eff χ_1]` without extra representation-dependent terms. Indeed, matching its leading fundamental coefficient forces `t_eff=t⁴/8+O(t⁶)`; an exponential fundamental Wilson weight would then have normalized highest-weight-2 coefficient `t_eff²/2=t⁸/128+O(t¹⁰)`, whereas the actual blocked coefficient is `t⁸/432+O(t¹⁰)`. The coefficients disagree already at order eight. At small `t`, fitting only its leading fundamental coefficient would give `t_eff=t⁴/8+O(t⁶)`, a **formal isolated planar strong-coupling matching**, not a physical four-dimensional running bare coupling.

The leading `t^4/8` also follows directly from the preceding squarefree four-plaquette conditional expectation: to couple to the coarse loop's eight fine boundary links, all four fundamental face characters must be inserted. The normalized coefficient `1/8` is the exact Haar overlap, including the internal central-index factor two.

## 3. Why this does not solve cubic P2

In the **actual three-dimensional cubic lattice**, an interior planar link also occurs in plaquettes **transverse to the plane**. Consequently the full fine lattice weight does not factor into the four selected coplanar face weights and independent Haar integrations over their interior links. The exact `2×2` planar character convolution therefore cannot be substituted for the full 3D interacting conditional measure. Higher representation modes, transverse plaquettes, Gauss constraints, time transfer, renormalized observables and growing physical volumes all require independent estimates.

The next genuinely P2-relevant target is to **compare this exactly soluble planar block with a finite 3D block including the first transverse plaquette shell**, identifying the new character channels and bounding the correction to the normalized coarse gauge-invariant observable, initially at fixed bare coupling and finite volume. Only thereafter should a mesh-uniform physical-time transfer estimate or a Penrose-specific action dictionary be considered.

## 4. Reproducible checks and status

`verify_planar_character_block.py` checks the Weyl/Bessel coefficients by exact small-`t` power series, character convolution prefactors for `F=1,2,3,4`, the `2×2` fundamental and higher-spin coefficients through order `t^10`, and positive numerical coefficients for several `t` values. Those are symbolic and finite numerical checks of known SU(2) representation formulas, not a computational proof of the general convolution theorem.

The combined research record now contains an **exact obstruction** (`J*V_fine J` is a scalar under kinematic Haar blocking), an **exact observable recovery identity** (`J*∏_4χ_1 J = χ_1/8`), and an **exact isolated planar effective-character kernel** (`a_n^4/d_n^3`). These are distinct scope-limited facts. No physical interacting two-scale 3D correlation theorem or four-dimensional mass-gap proof has been closed; P0–P5 and T0–T5 statuses are unchanged.
