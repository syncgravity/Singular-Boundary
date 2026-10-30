# The Singular Boundary — A rigorous cut-cage stability lemma

Date: 2026-10-30. Status: finite-volume perturbative lemma, NOT a completed-cage strong-coupling or continuum mass-gap proof.

## Setting

Work on the original-link Hilbert space restricted to the full Gauss-invariant subspace. Let H_0 be a deleted-target magnetic Hamiltonian whose retained magnetic graph satisfies the incomplete-cage hypothesis, so its unique positive normalized ground state phi_0 has exactly Haar target-trace marginal and independence from the retained-trace vector P_0. Suppose H_s=H_0+s b c_r(1-p_r) for s in [0,1], where addition of r completes the target cage. All kinetic coefficients are positive, volume finite, and the spectral gap gamma_0=E_1(H_0)-E_0(H_0)>0. Write k_s=2sbc_r, because 0<=sbc_r(1-p_r)<=k_s.

## Theorem (cut-cage stability)

If k_s<gamma_0, then for the normalized positive ground state phi_s of H_s,

    q_s := sqrt(1-|<phi_0,phi_s>|^2) <= k_s/(gamma_0-k_s).

Consequently, with m_H(B) the Haar probability of any target trace event B,

    |Prob_s(p_f in B)-m_H(B)| <= q_s,

and, for any measurable event A depending only on retained traces in P_0,

    |Prob_s(A and p_f in B)-Prob_0(A)*m_H(B)| <= q_s.

If m_H(B)>q_s, then

    |Prob_s(A | p_f in B)-Prob_0(A)| <= 2q_s/(m_H(B)-q_s).

The same bound extends to any retained-trace F with 0<=F<=1 by layer-cake representation.

## Proof

The finite-volume compact-group elliptic H_0 and H_s have simple strictly positive ground states, with the positive states gauge invariant. Min-max gives E_0(H_0)<=E_0(H_s)<=E_0(H_0)+k_s. Let Q=I-|phi_0><phi_0|. Project (H_0+V_s)phi_s=E_0(H_s)phi_s with Q:

    Q(H_0-E_0(H_s))Q phi_s = -Q V_s phi_s.

Because QH_0Q>= (E_0(H_0)+gamma_0)Q and E_0(H_s)<=E_0(H_0)+k_s, its inverse on ran Q has operator norm at most (gamma_0-k_s)^(-1). Thus ||Qphi_s||<=k_s/(gamma_0-k_s). This is q_s.

For any multiplication projection M=1_E, the difference of its expectations in normalized pure states phi_s and phi_0 is at most the trace distance of the rank-one density matrices, which equals sqrt(1-|<phi_0,phi_s>|^2)=q_s. Set E={p_f in B} or E=A intersect {p_f in B}; under phi_0 exact conditional Haar gives P_0(E)=P_0(A)m_H(B). For conditional comparison, writing N_s=P_s(A intersect B), d_s=P_s(B), a=P_0(A), m=m_H(B), we have |N_s-am|<=q_s and |d_s-m|<=q_s, so |N_s/d_s-a| <= (|N_s-am|+a|m-d_s|)/d_s <= 2q_s/(m-q_s). QED.

## Interpretation and explicit limitation

This proves quantitative persistence of the exact cut-cage Haar and conditioning laws as one coupling is turned on provided 2sbc_r<gamma_0. At the physical strong-coupling endpoint s=1 and b large, k_s typically grows like b while gamma_0 need not; therefore the lemma is generally NOT applicable to the full completed cage. For rare target caps, m_H(B)~const*radius^3, so a conditional comparison requires the much stronger inequality q_s=o(m_H(B)). The result is an exact mathematical bridge and a precise diagnostic of why a naive single-face completion argument does not close the nonlinear current gate.

Nothing here bounds the derivative of log psi_s, signed radial current T_f,h, connected covariance, or the continuum mass gap. Those remain open.
