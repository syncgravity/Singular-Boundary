# Inverse-Whitney two-link block audit and nonperturbative coercivity obligation
Date: 2026-10-30. Source: prior 30-link M5 extracted OPEN disk global_whitney_11face.npz, positive definite 30x30 matrix M with edge_ids.

Define K=M^-1. For the four target-adjacent retained faces choose target-shared/boundary-free pairs L=(0,86),(1,88),(4,372),(13,26). Separate remaining links as B and form the **matrix-only** effective quadratic coefficient K_eff,L=K_LL-K_LB K_BB^-1 K_BL. These are exactly the Schur complements of SPD K and hence strictly SPD. Executed double-precision values:

L=(0,86): ||K_LB||_2=0.6311719708357876; min eig(K_eff)=1.6848697857079034.
L=(1,88): ||K_LB||_2=1.3176740386402281; min eig(K_eff)=1.18741201978661.
L=(4,372): ||K_LB||_2=0.9247357057985095; min eig(K_eff)=1.7110577880440834.
L=(13,26): ||K_LB||_2=1.242265570819589; min eig(K_eff)=1.2855792798087755.

The exact algebraic Schur identity gives a pointwise lower bound on the quadratic derivative metric after minimizing over background derivative vectors; in particular the values show non-negligible electric couplings crossing every candidate local pair. They are NOT certified interval eigenvalue bounds, and NOT lower bounds on the excited-sector spectrum relative to the switched-off *interacting* ground energy.

For a transported-derivative form H_E=(g2²/2) D* K D, the earlier diagonal electric model split as H0=H_rest + a_e(-Delta_e)+a_d(-Delta_d). This splitting fails when K_LB is nonzero. A free-link projection P_L need not reduce H0 unless transport paths avoid those link variables and one verifies the commutators of the resulting variable-coefficient differential operator. Even if P_L reduces H0, the lower form bound H_E >= c T alone is NOT enough to assert R(H0-E0)R >= c*(3/4)R in the presence of an arbitrary interacting magnetic background; an independent comparison of sector ground energies or a ground-state transform is needed.

A valid finite-energy general statement is only H_E >= (g2²/(2 lambda_max(M))) T as a quadratic form. This ensures finite electric-only coercivity, not a magnetic-background gap nor shrinking-cap estimate. The independent-face Haar projector Q_f remains kinematically meaningful on the open disk, but its commutation with this geometric kinetic operator is not assumed.

Reproduction: research/scripts/audit_inverse_whitney_local_blocks.py, which loads the saved NPZ containing 'matrix' and 'edge_ids'. The physical strong-magnetic center-cap problem and continuum Yang-Mills mass gap remain OPEN.
