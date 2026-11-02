# Covariant third-order SU(2) resolvent conversion — 2026-11-02

On undressed SU(2)^m with radius-two bi-invariant metric, orthonormal left-invariant frames X_i satisfy ∇_{X_i}X_j=Γ_ij^l X_l, Γ_ij^l=epsilon_ijl/2 when indices occupy the same link and zero otherwise. For arbitrary fixed positive original-link weights a_k on the last derivative slot and u=R_0 Q_0 g, the covariant three-tensor T_ijk=(∇_{X_i}Hess u)(X_j,X_k) satisfies

**||∇Hess(R_0g)||_(a,2) <= (7/3+sqrt(6)) ||∇g||_(a,2)**, dimension-independently, coefficient ≈4.7828230761.

Proof: expand T_ijk=X_iX_jX_k u −Γ_jk^l X_iX_l u−Γ_ij^l X_lX_k u−Γ_ik^l X_jX_l u +Γ_ij^lΓ_lk^p X_pu +Γ_ik^lΓ_jl^p X_pu. Since ∑_ij Γ_ij^lΓ_ij^p=δ_lp/2, each single Γ has Hilbert operator norm 1/sqrt2, each double Γ has norm ≤1/2; every replacement of the last derivative index remains on the same original link. Hence ||∇Hess u||_(a,2)≤||D³u||_(a,2)+(3/sqrt2)||D²u||_(a,2)+||Du||_(a,2). The previously established exact identity gives ||D³ R_0g||_(a,2)=||Dg||_(a,2); spectral gap 3/4 yields ||D²R_0g||_(a,2)≤(2/sqrt3)||Dg||_(a,2) and ||DR_0g||_(a,2)≤(4/3)||Dg||_(a,2). Their sum is 7/3+sqrt6. The same link-locality preserves source coordinate support exactly.

This is Haar L², undressed only; the covariant derivative tensor is not claimed fully symmetric. No dressed Poisson derivative theorem, pointwise nonlinear Banach closure, lambda=1 interacting gap or continuum four-dimensional Yang-Mills mass gap follows. Full detailed proof, verifier, log and SHA256 manifest are stored in Proof Audits Library.