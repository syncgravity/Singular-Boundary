# Fixed-source Wigner resolvent does not restore stronger anchored regularity (2026-11-02)

**Conditional theorem in the archived original-link SU(2) open-strip matrix-coefficient model.** The preceding width-graded anchored tame theorem establishes boundedness of the fixed-source operator T_G=K^(-1)Q Gamma_K(·,G) on the weak polymer space X=A^s_(σ,κ), and an operator-norm convergent Neumann resolvent (I−λT_G)^(-1) on X for sufficiently small λ. The present audit proves **there is no automatic gain** of the stronger source regularity Y=A^(s+1)_(σ,κ+η), η>0, even when G is a fixed translation-invariant **degree-one singleton source**. Both the spectral-moment and support-exponent gains individually fail.

Use u(U)=U_11=D^(1)_(++), h_t=∏_(i=1)^t u(U_i) on I_t=[1,t]. Normalize the single-polymer input F^(t)_(I_t)=(t+1)^(-s)e^(−κt−σt)h_t, so ||F^(t)||_X=1. Fix G_{ {j} }=ε 2^(−(s+1))e^(−κ−η−σ)u(U_j) for every site j, so ||G||_Y=ε. It also has every finite degree moment and every finite support-exponent norm.

Highest-weight PW functions diagonalize the archived electric operator: E(n)=Σ_i n_i(n_i+2)−(1/2)Σ_i n_i n_(i+1). For internal singleton insertions j=2,...,t−1, the exact Gamma coefficient is −1/2 and output eigenvalue E=(5t+9)/2; for the two endpoints Gamma=−3/4 and E=(5t+10)/2. The outputs have pairwise distinct PW degree vectors, with total degree t+1 and unchanged support I_t. Their exact total unweighted coefficient magnitude is

**L_t=(t−2)/(5t+9)+3/(5t+10)→1/5**.

Hence, omitting additional nonnegative external insertion contributions, the output strong anchored norm satisfies

**||T_GF^(t)||_Y ≥ ε 2^(−(s+1))e^(−κ−η)e^(ηt) [(t+2)^(s+1)/(t+1)^s] L_t**,

which diverges as ε e^(ηt)t while input and source norms are fixed. At η=0 the linear-in-t divergence still excludes one extra polynomial spectral-degree moment. At unchanged polynomial degree weight, the e^(ηt) factor excludes increased support exponent. Moreover choosing nested I_t coefficients suppressed by (t+1)^(-2) gives a **single F∈X** with T_GF∉Y: the anchored weak sum converges while the anchored strong sum diverges exponentially.

**Resolvent no-smoothing corollary:** T_G also preserves Y, since its singleton source belongs to all stronger source spaces and the width-graded tame theorem may be reapplied at the higher degree and support weights. Whenever the weak-space R_λ=(I−λT_G)^(-1) exists, it cannot map all X into Y. Otherwise every F∈X would equal (I−λT_G)R_λF∈Y, contradicting the strict inclusion Y⊊X. The weak resolvent theorem remains valid; the desired nonlinear regularity upgrade does not follow from it.

**Scope limitation:** The counterexample uses non-gauge-invariant highest-weight matrix coefficients of the archived face-variable model. It is not a no-go theorem for the physical gauge-invariant sector, for an interacting spectral gap at λ=1, or for the continuum Yang–Mills mass gap.

Full-length mathematical proof, exact-rational checker, passing execution log and SHA-256 manifest are in The Singular Boundary / Proof Audits Library.