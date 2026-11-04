# R3-IR-524 — Strong magnetic background can close global gap without closing a symmetry-protected local sector gap

Date 2026-10-30. A rigorous 2D torus analogue, NOT an SU(2) Penrose local-gap theorem.

On L²(T²), with normalized Haar dx dy, let H_B=(-i∂x)²+2a(-i∂x)(-i∂y)+(-i∂y)²+B(1-cos(2y)), |a|<1 and B>=0. Its principal kinetic matrix [[1,a],[a,1]] is positive definite and has genuine off-diagonal electric coupling. The potential is x-independent, so the Fourier projector P onto k_x=0 REDUCES H_B exactly. In sector k, writing P_y=-i∂y, H_(B,k)=(P_y+ak)²+B(1-cos2y)+(1-a²)k². The diamagnetic inequality on the circle guarantees inf spec[(P_y+ak)²+V(y)] >= inf spec[P_y²+V(y)]=E_(B,0). Hence

(I-P)(H_B-E_(B,0))(I-P) >= (1-a²)(I-P)

for all B>=0. The full ground energy is E_(B,0) because all nonzero k sectors are higher. The bound is independent of B. This is a strong-background protected local excitation sector even when the background k=0 spectral gap decreases to zero due to two deep wells at y=0 and pi.

Numerical Fourier Galerkin check (|m_y|<=35, a=.35) yields for B=0,10,50,100: background first gap 1,0.009965422214,5.618827e-7,2.419931e-10, and local k=1 sector ground-energy differences 1,0.8802112569,0.8775001534,0.8775000001, all >=1-a²=0.8775. Values are floating-point and the tiny background gap has truncation/roundoff sensitivity; only the analytical sector inequality is claimed as rigorous.

Relevance: global-gap estimates (e.g. R3-IR-523) may be much too restrictive for a local excitation. The sufficient structural ingredient is an EXACT reducing local projection or an analogue of diamagnetism on a covariantly twisted background. The ACTUAL inverse-Whitney SU2 Penrose operator contains configuration-dependent adjoint transports; whether a selected-link Haar projection reduces it, or permits a suitable covariant sector comparison, is unproved. A Schur-complement coercivity inequality by itself is insufficient (R3-IR-500/517). This analogy does not prove a Penrose uniform local sector gap, a refinement-uniform shrinking center cap, or a continuum Yang-Mills mass gap.

Reproduction: research/scripts/validate_strong_background_local_gap.py.
