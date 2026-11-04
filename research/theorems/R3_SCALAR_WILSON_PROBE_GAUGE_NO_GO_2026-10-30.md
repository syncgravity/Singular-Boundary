# Gauge-covariance no-go for scalar Wilson probes of dual-path current
Date: 2026-10-30
Status: exact representation-theoretic conditional no-go in canonical based-face coordinates; direct scalar Haar projection remains valid.

After maximal-tree gauge fixing on finite simply connected SU(2) disk, residual root gauge acts by simultaneous conjugation W_g -> k W_g k^-1. Assume the canonical dual-path action is left multiplication on W_f with other based face holonomies held fixed, as in OT-4. Then conjugation intertwines the orbit multiplications: R_k T_g R_k^-1=T_{kgk^-1}, and the three infinitesimal generators transform covariantly as an adjoint triplet R_k D_a R_k^-1=sum_b Ad(k)_{ba} D_b (up to indexing conventions). Let Omega be residual-gauge invariant, the positive deleted ground state, H commute with gauge, and B any bounded gauge-invariant scalar multiplication observable, including every trace Wilson loop product.

Set c_a=<D_a Omega,B Omega>. Gauge invariance and unitary conjugation imply c=Ad(k)c for every k in SU(2). The SU(2) adjoint representation has no nonzero invariant vector, hence c_a=0 for all a. The same holds for spectrally projected overlaps <P_L D_a Omega,P_L B Omega>, as P_L=1_(0,L](H-E) commutes with gauge action. Equivalently the full gauge-invariant projection kills each D_a Omega.

Therefore a lower frame bound on a nonzero span of P_L D_a Omega is IMPOSSIBLE using gauge-invariant scalar Wilson probes: all mixed overlaps vanish and the frame lower constant is zero. This supersedes the proposed practical scalar Wilson-frame route in R3-IR-395 / R3-IR-397 (their abstract conditional inequalities remain algebraically valid but hypotheses cannot hold for this scalar probe class).

IMPORTANT: Individual D_a Omega may not be in the physical gauge-invariant Hilbert space, so prior discussions treating them as individually physical low-energy vectors require full-space spectral formulation. Their summed squared norm J=sum_a||D_a Omega||² is gauge invariant; the orbital Poincare inequality and Q_f Omega physical Haar projection remain valid. Likewise the scalar Wilson cap observable can probe Q_f Omega directly, and covariant/adjoint-index probes could couple to D_a Omega after suitable index contraction; neither offers a proved smallness estimate.

This result assumes the conjugation-equivariant canonical based-face action and gauge-invariant ground state, not an arbitrary gauge-noncovariant lift. It does not prove Penrose cap survival or continuum mass gap.
