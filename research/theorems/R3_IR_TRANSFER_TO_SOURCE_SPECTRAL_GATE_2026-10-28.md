# R3-IR — stationary Wilson insertion vs source-inserted spectral decay

**Audit 2026-10-28.** This is an exact finite SU(2) Wilson-model countertest and a proof-target reconciliation with October 26 historical R3-IR work. It is **not** a claim of a new mass-gap theorem. No Monte Carlo performed.

### Original source provenance

- Historical stationary transfer insertion: \`R3_SU2_transfer_barrier_2026_10_27_bundle.zip\` SHA-256 \`d3c62eaed9b4c65b5b3dc75ab31abf86c97241795d0df9ff36cc3ea4d81cfc94\`.
- Historical single-rhombus coupling-scale obstruction: \`sources/historical-notes/FORMAL_R3_R2_PROOF_AUDIT.md\`.
- Historical source-inserted crossing criterion: \`sources/historical-notes/R3_THEOREM_OBSTRUCTION_AND_MULTISCALE_GATE.md\` SHA-256 \`3fd2db46a7955e4decb9d2d6e6c48f94a1f5bec49955f254b7fce4d41b0cbd98\`.
- Historical interacting Wilson-frame obstruction: \`sources/historical-notes/FORMAL_NOTE.md\` SHA-256 \`b387490e8d5ff58f29c1e7c81b8754e4018cdda14d25ce29d998e963b52dff37\`.
- Full derivation and scope: local handoff \`r3_ir_transfer_to_spectral_checkpoint_2026_10_28.zip\` SHA-256 \`6524c68ca953b757c4fe0e119a7452c7a23fd2ecf2c3a759540705149120cf1e\`.

### Exact elementary transfer countertest

On one open spatial rhombus with four links, equal temporal Wilson coefficient beta>0, spatial magnetic Wilson coefficient zero, and physical link Hilbert space \`L2(SU(2)^4)^gauge\`, let \`T=P_G(⊗_e C_beta)P_G\` with \`C_beta\` convolution by \`exp[-beta(1-Tr(g)/2)]\`. The top eigenvector is \`Omega=1\`, eigenvalue \`z(beta)^4\`, where \`z(beta)=2 exp(-beta)I_1(beta)/beta\`.

For the contractible center-neutral source \`A=Tr(W)/2=chi_(1/2)(W)/2\`, Haar orthogonality gives \`<Omega,A Omega>=0\` and \`||A Omega||²=1/4\`. Each of its four link factors has normalized convolution eigenvalue \`rho=I_2(beta)/I_1(beta)\`; hence
\[
\widehat T A\Omega=\rho^4 A\Omega,\qquad
\langle A\Omega,\widehat T^n A\Omega\rangle=\tfrac14\rho^{4n},\quad \widehat T=T/z(\beta)^4.
\]
The source excitation energy at time spacing a_t is
\[
E_A=-\frac4{a_t}\log\frac{I_2(\beta)}{I_1(\beta)}
=\frac6{a_t\beta}+O((a_t\beta^2)^{-1}).
\]
At fixed a_t and beta->infinity this energy tends to zero, **while the historical stationary completed temporal-face deletion ratio remains valid for any deleted ribbons**. Therefore that ratio alone cannot imply a uniform physical-energy spectral gap.

**Scaling caveat:** this path sends the electric coefficient to zero. On the prescribed fixed-electric anisotropic Hamiltonian scaling \`beta_t=2/(a_e a_t)\`, \`a_t->0\` and fixed a_e, the same energy tends to \`3a_e\`, not zero. The example does **not** refute the physical Penrose continuum trajectory. The October 26 Hamiltonian audit already had the analogous \`b_f=0\` one-face spectral-rescaling obstruction; this note reconciles it with the later stationary insertion theorem.

### Exact missing bridge

For a positive compact physical transfer T with simple top eigenvalue lambda0, define \`T_hat=T/lambda0\`, \`Q=1-|Omega><Omega|\` and \`b_A=QA Omega\`. The connected *vacuum* source correlation has positive spectral expansion
\[
C_A(n)=\langle b_A,T_{\rm hat}^{\,n}b_A\rangle
=\sum_{k\ge1}|\langle \psi_k,b_A\rangle|^2(\lambda_k/\lambda_0)^n.
\]
If a **model-derived** bound \`C_A(n)<=M_(A,G)exp(-m a_t n)\` holds for all n, a common physical \`m>0\` independent of regulator/volume/boundary, and a Wilson source family whose \`b_A\` span is dense in the physical excited Hilbert space, then every excited physical energy is >=m: any lower eigenvalue with nonzero source overlap would contradict the long-time bound. This is a **gap-strength sufficient condition**, not an estimate established for the interacting continuum trajectory.

To advance R3-IR noncircularly, derive a **source-inserted** crossing/polymer estimate (with operator renormalization, all relevant center and winding sectors, physical time, and boundary control), or independently establish quantitative interacting-frame observability together with an operator-norm infrared bound \`||P_s S P_s|| <= C s^p\`. Neither follows from uninserted Q14 insertion ratios, Euclidean finite-slice cumulant averages, character-only blocking, or first positive spectral moments.

### Disposition

- Explicit stationary Wilson transfer countertest: **proved in b_f=0 finite graph**.
- Earlier October 26 obstruction: **recovered** (not rediscovered).
- Stationary unconditioned original Q14 free-energy ratio: **proved within archived hypotheses**.
- Uniform *interacting* connected source decay and physical spectral gap: **OPEN**.
- Quantum spatial continuum and gap: **OPEN**.
