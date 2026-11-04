# R3-IR — Uniform anchored Casimir-energy splitting for elementary SU(2) magnetic insertion

Research date 2026-11-03. **Restricted theorem for a linear insertion of fundamental plaquettes, not arbitrary quadratic polymer fusion or Yang–Mills mass gap.** Full report + reproducible verifier: conversation archive R3_IR_ANCHORED_CASIMIR_SPLIT_2026-11-03.zip.

Consider finite open simply connected straight square SU(2) strips with Gauss invariance, original-link electric K = -sum_e a_e sum_j X_ej^2, 0<a0<=a_e<=a*, and Gamma_K(f,g)=sum_ej a_e (X_ej f)(X_ej g). Normalize irrep n with dimension d_n=n+1, Casimir c(n)=n(n+2)/4 and generator operator norm <=n/2. The nonconstant gauge-invariant free gap is at least 3a0. Q removes constants, B=K^{-1}Q Gamma_K. The strong projective Fourier norm is ||f||_{P_sigma}=sum_n d_n exp(sigma|n|)||A_n||_1. Each elementary magnetic input v_p is a fundamental plaquette Wilson observable, and b=sup_p||v_p||_{P_sigma}.

## Theorem (uniform summed singleton insertion)
For any finite Gauss-invariant Fourier polynomial f, any sigma>=0 and any number N of faces,
\[
\boxed{\left\|\sum_{p\in D} B(f,v_p)\right\|_{P_\sigma}
\le 36 (a_*/a_0)b\|f\|_{P_\sigma}.}
\]

Proof: Fix an input original-link spin sector n and let q=sum_e c(n_e)>0, q_p=sum_{e in partial p} c(n_e). Every original link is in <=2 faces, hence sum_p q_p<=2q. At most four faces can satisfy q_p>q/2 (exceptional). For each other (good) face, CG fusion leaves all nonface links unchanged, so all output sectors have electric eigenvalue >=a0(q-q_p)>=a0q/2. The projective Fourier multiplication inequality and derivative generators give ||Gamma(f_n,v_p)||<= (3a*/4)(sum_{e in partial p} n_e)||f_n||||v_p||. Sum good faces, use sum_p sum_{e in partial p}n_e<=2sum_e n_e and n<=4c(n)/3 to get <=4(a*/a0)b||f_n|| after inverse.

For an exceptional face and one differentiated shared link e with n_e>=1, all CG output labels on e are n_e+1 or n_e-1. If n_e>=2, output energy >=a0 c(n_e-1) and n_e / energy <=8/(3a0). If n_e=1, projected nonconstant gauge-invariant output has energy >=3a0. The one-edge contribution after inverse is <=2(a*/a0)||f_n||||v_p||. Each plaquette has four original links, and at most four faces are exceptional, costing <=32(a*/a0)b||f_n||. Add 4+32, then sum Fourier sectors. Constant inputs have zero derivatives. Completion extends the bound.

## Corollary (anchored *linearized* polymer map)
For connected history intervals I, let F=sum_I [I] tensor f_I, where each f_I depends only on original links incident on I. Define ||F||_anch,kappa,sigma = sup_x sum_{I containing x} exp(kappa|I|)||f_I||_{P_sigma}. Let G=sum_p[{p}] tensor v_p with ||G||_anch=e^kappa b. Lift the insertion map L_G F by applying B to each f_I,v_p and labelling output with connected history I union {p}, only for actual shared original links. For each output anchor x, the input history I either contains x, or is adjacent to x and the inserted singleton is x. Compare to the three input anchors x-1,x,x+1. Since exp(kappa|I union {p}|)<=exp(kappa|I|)exp(kappa), the bound is
\[
\boxed{\|L_GF\|_{\rm anch,\kappa,\sigma}
\le108(a_*/a_0)\|G\|_{\rm anch,\kappa,\sigma}\|F\|_{\rm anch,\kappa,\sigma}.}
\]
No dependence on ambient strip size or maximum original-link spin.

## Interpretation
The earlier Wilson-rectangle bound used its extensive surviving fundamental perimeter. This generalizes the **linear insertion** estimate to arbitrary spin-network sectors using a good/exceptional Casimir energy dichotomy: no more than four face insertions can concentrate a majority of an input sector's electric energy. This is not a bounded bilinear map for two arbitrary extended histories and does not close the nonlinear connected-score fixed point. Required next: all-history bilinear bound or renormalization into controlled singleton insertions, uniform interacting gap, 3D spatial extension, and physical-unit continuum and OS reconstruction.

## Verification
Reproducible Python checker in accompanying local archive reports 1,382,189 checks: exact rational link-incidence, Casimir, good/exceptional split comparisons across 43 strip sizes with 150 deterministic spin assignments each, plus finite floating overlap-weight diagnostics. This checker is not a formal verification of the general theorem. No historical Stage 26 datasets modified.