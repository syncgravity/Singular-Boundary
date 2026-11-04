# Local switch-off ground-state comparison and conditional center cap

Date: 2026-10-30. Fixed finite open SU2 disk, not a continuum mass-gap result.

Let H0 be the deleted Hamiltonian with one retained plaquette g adjacent to deleted face f switched off, and H=H0-b_g p_g with b_g>=0 and ||p_g||<=1. Assume H0 has a normalized simple ground state Omega0 and spectral gap gamma0>0, and that Q_f Omega0=0. The last assumption is established by the boundary-link decoupling argument for the extracted 11-face disk; it is a necessary hypothesis in more general domains.

For 2 b_g < gamma0, center a Riesz circle of radius gamma0/2 on the lowest eigenvalue of H0. The perturbation norm is at most b_g, the resolvent on this circle at most 2/gamma0, and the perturbed resolvent at most 1/(gamma0/2-b_g). The resolvent identity bounds the rank-one spectral-projector difference by 2 b_g/(gamma0-2 b_g). The perturbed rank-one projector is the physical ground-state projector (by spectral order and min-max). Therefore Q_f Omega = Q_f(P-P0)Omega and ||Q_f Omega|| <= min(1,2b_g/(gamma0-2b_g)). This bound explicitly depends on the single switched-off background gap gamma0 but has no additional explicit plaquette count.

With SU2 independent deleted-face Haar coordinates, c_delta=Haar{|Tr u/2|>=1-delta} and m_f(delta)>= [sqrt(c_delta)*sqrt(1-epsilon^2)-epsilon]_+^2, epsilon=min(1,2b_g/(gamma0-2b_g)).

For the extracted eleven-face disk, take all ten couplings b=3/32000 and switch one of the four deleted-adjacent faces off. By elementary min-max, gamma0 >= 3/4-9b=23973/32000; hence epsilon<=2/7989. Exact SU2 cap integration at delta=1/10 yields m_f(1/10)>0.0372893. The regression research/scripts/validate_local_switch_off_bound.py checks these constants.

The refinement obstruction is precisely the missing uniform bound for gamma0 under physical electric/magnetic scaling. A uniform positive gamma0 at physical parameters cannot be presumed, since establishing the relevant spectral gap may be as difficult as the target mass-gap problem. Nor does this comparison certify any uniform shrinking-cap bound at delta~h unless epsilon is controlled on the scale sqrt(c_delta)~h^(3/4).
