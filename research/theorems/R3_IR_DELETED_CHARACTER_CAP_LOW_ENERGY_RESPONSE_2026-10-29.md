# R3-IR — Physical Wilson cap-response and sharp SU(2) representation resolution

**Date:** 2026-10-29. **Status:** proved exact physical nonlinear SU(2) finite-volume cap-response and UV bound; proved independent heat-kernel rotor obstruction to low-spin-only positivity. **OPEN:** low-energy adverse mixed response in the actual Penrose deleted vacuum, full bulk deletion, fixed-support source covariance, mass gap, continuum reconstruction. Complete expanded proof, executable deterministic verifier and verification log: \`singular_boundary_character_cap_response_2026-10-29.zip\`.

## Setup: exact one-neighbor bridge

Let H=sum_e a_e(-Delta_e)+sum_k b_k(1-p_k) be the positive Wilson Hamiltonian on a finite simply connected four-edge rhombus disk, maximum two magnetic faces per edge, with physical Gauss-invariance. Fix interior target f. Remove its magnetic term throughout. Choose an edge-sharing neighbor g and set H(u)=sum_e a_e(-Delta_e)+sum_{k not in {f,g}} b_k d_k+u b_g d_g (0<=u<=1). At u=0 the edge shared by f,g is private, so the unique normalized positive ground state is independent of that edge and W_f has exactly Haar law even when the rest of the face graph is cycle-rich. Write Omega_u, E_u, K_u=H(u)-E_u, Q_u and G_u=Q_u K_u^{-1}Q_u for the finite physical sector. No regulator-uniform gap is assumed.

Choose smooth real nonnegative central phi_a supported in the SU(2) geodesic ball B_{a/2}, identically 1 on B_{a/4}. Put alpha_a=int phi_a dU, nu_a=int phi_a² dU and k_a=phi_a*phi_a^vee. Then k_a>=0, support k_a subset B_a, 0<=k_a<=nu_a 1_{B_a}, int k_a=alpha_a², and alpha_a,nu_a are each Theta(a³).

## CR-1. Exact nonlinear cap-response formula

The finite-volume physical ground-state derivative for any bounded gauge-invariant multiplier O is

d/du <O>_u = -2 Re <Q_u O Omega_u, G_u Q_u (b_g d_g) Omega_u>.

The Haar bridge gives <k_a(W_f)>_0=alpha_a², hence exactly

<k_a(W_f)>_1=alpha_a²-2 int_0^1 Re <Q_u k_a Omega_u,G_u Q_u (b_g d_g)Omega_u> du.

This identity retains every remaining magnetic face and all electric shared-link interactions.

## CR-2. Uniform high-energy cutoff

Let P_{u,>Lambda} be the physical spectral projector onto excitation energies greater than Lambda. The exact spectral estimate is

2|<Q_u O Omega_u,G_u P_{u,>Lambda}Q_u W Omega_u>| <= 2/Lambda² sqrt(m_1,u(O)m_1,u(W)),

where m_1,u(O)=E_{Omega_u²} Gamma(O). SU(2) gives |grad_e p_k|²=(1-p_k²)/4<=1/4. Thus for W=b_g d_g,

m_1,u(W)<=b_g² A_g/4, A_g=sum_{e in boundary g} a_e.

Convolution plus normalized Haar gives ||grad k_a||_infinity<=||grad phi_a||_L1||phi_a||_infinity<=C_phi a². Every edge differentiation of k_a(W_f) pulls back an isometric SU(2) derivative, so m_1,u(k_a)<=C_phi² A_f a^4. Integrating u:

V_{a,>Lambda} <= C_phi a² b_g sqrt(A_f A_g)/Lambda².

At physical Penrose coupling b_g<=beta_+ h^-2, bounded electric coefficients, and a_h=acos(1-h)=Theta(sqrt(h)), Lambda_h=Lh^-2 gives V_{a_h,>Lambda_h} <= C L^-2 h³. Meanwhile alpha_{a_h}²>=c h³. Choose one sufficiently large fixed L so V<=alpha²/4 for all small h. This estimate is fully nonlinear and uniform in total face count.

## CR-3. Physical cap-versus-low-energy-response alternative

Define the adverse low-energy response

S_{a,<=Lambda}=2int_0^1 [Re <Q_u k_a Omega_u,G_u P_{u,<=Lambda}Q_u (b_g d_g)Omega_u>]_+ du.

Then

Pr_{Omega_{f,h}^-}(W_f in B_a) >= [alpha_a²-S_{a,<=Lambda}-V_{a,>Lambda}]_+/nu_a.

For a=a_h and Lambda=Lh^-2, either S_{a_h,<=Lambda}<=alpha_{a_h}²/4, implying flat-cap probability >=alpha²/(2nu)>=c h^(3/2), or S>alpha²/4>=c h³. The first alternative gives the earlier conditional O(h^-1 log(1/h)) magnetic-deletion estimate. The second certifies an adverse, low-excitation-energy mixed physical resolvent response of order h³. Neither alternative settles the continuum mass gap. The *independent* missing estimate is S<=alpha²/4 for the actual cycle-rich Penrose deleted vacua.

## CR-4. Sharpness of J≈1/a character-sign resolution

Let K_t be the positive normalized SU(2) heat kernel for -Delta with spin-j Casimir j(j+1), and t=J^-2, J positive integer. The center-even normalized density F_t(U)=[K_t(U)+K_t(-U)]/2 is strictly positive with all half-odd characters zero and integer-spin expectations

c_j(F_t)=(2j+1) exp[-j(j+1)/J²] >= e^-2 (2j+1) for 1<=j<=J.

Let eta_a be a smooth center-even nonnegative cutoff vanishing on both center caps B_a(I) and B_a(-I), equal to one outside double-radius caps. By the compact SU(2) heat-kernel bound ||F_t||_infinity<=C t^-3/2, the removed mass delta=int F_t(1-eta_a)<=C(Ja)^3. Choose Ja sufficiently small so delta<e^-2/2. The renormalized smooth density F_t eta_a/(1-delta) has **zero cap probability** at +I, but c_j>0 for every 1<=j<=J, because removing mass changes each character expectation by at most (2j+1)delta. Replacing eta_a by epsilon+(1-epsilon)eta_a produces a smooth *strictly positive* center-even density with the same spin signs and arbitrarily small cap mass. For epsilon=exp(-J²), and a~c/J, this mass is exponentially small in 1/a². The square-root amplitude is the unique strictly positive ground state of a suitable separate smooth center-even SU(2) class rotor potential V=(Delta sqrt(F))/sqrt(F)+constant, selected so V>=0.

Thus center symmetry, strict positive ground-state property and c_j>=0 through J with Ja small **cannot** force a Haar-order a³ cap probability. The previous finite-spin cutoff at J(h)=O(h^-(1+eps)/2), with a_h~sqrt(h), is near the necessary representation resolution (J≳1/a), although the actual nonlinear Wilson Hamiltonian may have stronger structure. This comparator is NOT its ground state.

## Independent deterministic audit and open items

The executable standalone companion verifier checks the SU(2) sharp-cap Fourier integrals, smooth heat-kernel cutoff with J=4,8,12,24 and positive low-spin coefficients, and the exact a² b_g/Lambda²=h³/L² UV exponent. No Monte Carlo and no historical Penrose Stage26 or Q14 files modified.

**PROVED:** CR-1, CR-2, CR-3, CR-4 in their stated domains. **OPEN:** Wilson-specific low-energy response sign/budget; all-bulk deleted-face polynomial cap mass; full fixed-support Wilson-angle equivalence; physical continuum mass gap and reconstruction.
