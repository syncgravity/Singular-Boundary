# Center-flux parity forces pointwise vanishing of the private-link environmental bridge

2026-10-30. R3-IR-397. Exact finite-volume Wilson boundary result; does not establish full-coupling cap survival.

## Assumptions
Use the magnetic-deleted target face f and one switched-off neighboring coupling t_g=0 in a finite simply connected edge-to-edge SU(2) disk. The archived four-neighbor theorem FN-2 asserts an **independent center-flux involution** S_g (a measure-preserving product of sign changes of original links) which at t_g=0 preserves the Hamiltonian H_0 and target class observable O=k_a(W_f), but reverses the neighboring character p_g. Explicitly:
S_g H_0 S_g^{-1}=H_0, S_g O S_g^{-1}=O, S_g p_g S_g^{-1}=-p_g.
This hypothesis is essential; verify the center-flux path construction on each actual finite graph before using it.

## Theorem: all Euclidean-time mixed responses vanish
Let Omega_0>0 be the unique normalized physical ground state of H_0 and K_0=H_0-E_0. Its uniqueness and positivity give S_g Omega_0=Omega_0. For every s>=0,
C(s)=<Omega_0, O exp(-s K_0) p_g Omega_0>.
Conjugating by S_g gives C(s)=-C(s), hence

C(s)=0, for every s>=0. (CF-1)

The reverse correlator <Omega_0,p_g exp(-sK_0) O Omega_0> is also exactly zero by the same parity argument.

The identity holds for the original full-link and physical Gauss-invariant semigroups (all insertions are gauge invariant), any other retained magnetic couplings, and requires no spectral gap estimate. Therefore the first neighbor-coupling derivative of the cap expectation vanishes at t_g=0, as in FN-2, now strengthened to every Euclidean time lag.

## Environmental bridge implication
The previously recorded exact private-link bridge WB-3 for s>=0 says
C(s)=exp(-3a_e s/4) m_a E_y[p_bridge(y(0),y(s))].
If the cap has m_a nonzero (in particular, a positive identity-centered cap with radius under pi/2), the exponential is positive and CF-1 yields

E_y[p_bridge(y(0),y(s))]=0 for every s>=0. (CF-2)

This is an **unconditional pointwise mean-zero statement under the archived FN-2 involution**. It strengthens the caution in R3_IR_SHARED_EDGE_EUCLIDEAN_WILSON_BRIDGE_2026-10-30.md, which noted that pointwise vanishing had not yet been established. The *conditional bridge p_bridge(y0,ys)* may have either sign; only its expectation vanishes. No sign claim at t_g>0 is implied.

## Proof audit and boundaries
The result uses exact discrete center-flux parity of the genuine Wilson Hamiltonian at a deleted-neighbor hyperplane, not reflection positivity or an assumed mass gap. It is a structural selection rule on all-time correlators, not an actual bound across 0<t_g<=1. A purported global sign argument from C(s)=0 at t_g=0 would be invalid. Further work must control the effect of activating the neighboring plaquette on the coupled environmental paths.

Dependency: FN-2 in R3_IR_FOUR_NEIGHBOR_SPIN_SELECTION_AND_MIXED_RESPONSE_2026-10-29.md and WB-3 in R3_IR_SHARED_EDGE_EUCLIDEAN_WILSON_BRIDGE_2026-10-30.md.
