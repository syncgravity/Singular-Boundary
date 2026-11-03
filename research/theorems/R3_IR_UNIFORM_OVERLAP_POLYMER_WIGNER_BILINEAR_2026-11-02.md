# Uniform overlapping-polymer Wigner Poisson bilinear theorem — 2026-11-02

**Conditional on archived SU(2) open-strip original-link face-coordinate conventions.** The sharper uncoupled-Wigner resolvent ||K_T(c)^(-1)||_(1→1)<=2/D(c), D(c)=Σ_i c_i(c_i+2), combines with original-link local magnetic derivative estimates to eliminate the union-length factor from the earlier overlap Poisson theorem.

For input degree vectors a,b on intervals I,J, and output Wigner degrees c_i=a_i+b_i−2r_i, the Clebsch–Gordan reductions r_i occur only in o=|I∩J| overlapping faces. On each of the at most 3o+1 original links active in both inputs, with local input degrees A_e,B_e, local output degree sum s_e, and local reduction r_e, the inverse-weighted derivative coefficient satisfies **6A_eB_e/D(c)<=3(1+2R)^2** for nonconstant output, R=Σ_{overlap}r_i. Proof: A_eB_e≤(s_e+2r_e)^2/4; if s_e≥1 use D(c)≥s_e²/2, while s_e=0 uses D(c)≥3.

Writing z=e^(−2σ), σ>0, the full same-radius Wigner coefficient-l1 bilinear Poisson estimate for overlapping input intervals is
**||K_(I∪J)^(-1) Q Γ_K(f_I,g_J)||_(Wσ)<= B_o(z)||f_I||_(Wσ)||g_J||_(Wσ)**,
**B_o(z)=3(3o+1)(1−z)^(-o)[1+8oz/(1−z)+4o(o+1)z²/(1−z)²]**.
For touching but face-disjoint intervals o=0, the archived sharp endpoint theorem supplies **B_0=1/4**. For separated intervals Γ=0. Importantly, B_o depends on OVERLAP LENGTH o, not union length t.

Define the connected-interval **global-sum** polymer family norm ||F||_(σ,κ)=Σ_I e^(κ|I|)||F_I||_(Wσ). The bilinear polymer operation (B(F,G))_T=Σ_(I∪J=T)K_T^(-1)QΓ_K(F_I,G_J) is bounded **uniformly in finite strip volume** if κ>−log(1−e^(−2σ)). With q=e^(−κ)/(1−z)<1 it obeys
**||B(F,G)||_(σ,κ)≤C_(σ,κ)||F||||G||**,
C=1/4+3Σ_(o≥1)(3o+1)q^o[1+8oz/(1−z)+4o(o+1)z²/(1−z)²]<∞.
Example σ=log 2, κ=log(16/3): **C=12197/324**.

This **is** a same-radius bounded nonlinear quadratic operation on localized absolutely summable interval-polymer families, with constants independent of ambient volume and interval lengths. This **is not** a theorem for an extensive translation-invariant potential: the global-sum norm diverges for a nonzero one-face term at every site. An anchored/per-site polymer norm, interaction-strength control, continuation to λ=1, dressed Hessian coercivity, an interacting gap, and the continuum four-dimensional Yang–Mills mass gap remain open. Independent verification script: 5,049 generator-column checks; 58,751 exact-rational local ratios; 52,088 interval-pair link-count checks; overlap generating sums; exact rational C. Complete full-length proof, script, log and SHA256 manifest archived in The Singular Boundary / Proof Audits Library.