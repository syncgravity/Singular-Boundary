# R3-IR-443 — Static Wilson covariance bound across a magnetic cut

2026-10-30. Finite original-link SU(2) Wilson disk. Rigorous small-cross-cut comparison; NOT a uniform spatial clustering theorem.

Partition the original links into two nonempty sets A and B. Let H0=H_A tensor I+I tensor H_B contain all electric link terms and all retained magnetic faces whose boundary links lie entirely in one block. Let V_cut=sum_(g crossing A,B) b_g(1-p_g). Every term is nonnegative and bounded by 2b_g, so 0<=V_cut<=2B_cut I where B_cut=sum_crossing b_g. The actual full-coupling H=H0+V_cut.

Each finite compact-link block Hamiltonian has a unique strictly positive normalized lowest state omega_A and omega_B; H0 has product ground omega0 and a strictly positive first excitation gap delta0=min(delta_A,delta_B)>0. This is a finite-volume cut-system gap, NOT an established regulator-uniform gap for the physical coupled model.

Let Omega be the positive normalized ground state of H. The product-state variational upper bound gives E(H)<=E(H0)+2B_cut. Since V_cut>=0, the minmax bound for H0 gives

delta0 [1-|<omega0,Omega>|²]
<=<Omega,H0 Omega>-E(H0)
<=E(H)-E(H0)
<=2B_cut.

Thus eta:=1-|<omega0,Omega>|²<=min(1,2B_cut/delta0). (SC-1)

For any bounded real multiplication observables O_A depending only on A and P_B depending only on B, their covariance in the decoupled product vacuum is zero. The pure-state expectation difference between Omega and omega0 for any bounded observable X is at most 2||X|| sqrt(eta), by the rank-one density trace-distance formula. Therefore

|Cov_Omega(O_A,P_B)|
<= |<O_AP_B>Omega-<O_AP_B>omega0|
 + |<O_A>Omega <P_B>Omega-<O_A>omega0 <P_B>omega0|
<= 6 ||O_A|| ||P_B|| sqrt(eta)
<= 6 ||O_A|| ||P_B|| min(1,sqrt(2B_cut/delta0)). (SC-2)

The bound is legitimate for the full interacting original-link physical vacuum, including any gauge-invariant cap multiplier supported in A and a retained plaquette supported in B. The unrestricted positive ground states are gauge invariant in the relevant full-link systems. Gauge projections need not be factorized.

If the magnetic cut is removed, B_cut=0 and the disconnected product vacuum has exactly zero cross-block covariance. But at genuine full physical coupling B_cut need not be small even for distant observables: separating them into A and B generally requires crossing a boundary with nonzero Wilson terms, and delta0 may be small. Hence SC-2 is a true weak-cut clustering comparison, not exponential decay in spatial distance. It does not control the long-time resolvent response or establish regulator-uniform half-Haar cap survival or the continuum Yang-Mills mass gap.
