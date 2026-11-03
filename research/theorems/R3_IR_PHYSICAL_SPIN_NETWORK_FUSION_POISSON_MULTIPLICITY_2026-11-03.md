# Physical SU(2) spin-network fusion: exact Poisson multiplier and exponential unweighted multiplicity (2026-11-03)

**THEOREM 1, exact physical energy-shell fusion identity.** On any finite SU(2) original-link graph let {Psi_alpha} be an orthonormal Gauss-invariant original-link spin-network electric eigenbasis, K Psi_alpha=E_alpha Psi_alpha. Write Psi_alpha Psi_beta=sum_nu M_(alpha,beta)^nu Psi_nu. The standard original-link carré-du-champ identity 2 Gamma_K(f,g)=fKg+gKf-K(fg) and the centered inverse imply the EXACT physical formula

**K^-1 Q Gamma_K(Psi_alpha,Psi_beta)=sum_(E_nu>0) [(E_alpha+E_beta−E_nu)/(2E_nu)] M_(alpha,beta)^nu Psi_nu.**

Thus a coefficient-l1 nonlinear estimate requires control of the energy-weighted **fusion structure constants**, not merely the sharp electric inverse bound ||K^-1Q||_(SN,l1)=1/3.

**THEOREM 2, an all-length physical obstruction for the UNWEIGHTED canonical spin-network coefficient algebra.** Select r pairwise original-edge-disjoint square plaquettes at positions 1,3,...,2r−1 of a straight ladder. Let F_r=prod_(i=1)^r chi_1(U_(2i−1)), each chi_n the SU(2) spin-n/2 character. Because the plaquette loops share no original edges, their character tensors are orthonormal physical spin-network electric eigenfunctions. F_r is ONE normalized canonical original-link spin-network vector: ||F_r||_(SN,l1)=||F_r||_L2=1 and K F_r=3r F_r.

Character fusion chi_1^2=chi_0+chi_2 gives F_r^2=sum_(S subset {1,...,r}) Psi_S with **2^r orthogonal spin-network channels**. Each Psi_S carries spin 1 on S, is trivial elsewhere, and K Psi_S=8|S| Psi_S. Therefore

**K^-1 Q Gamma_K(F_r,F_r)=sum_(S nonempty) [(3r−4|S|)/(8|S|)] Psi_S,**

and its canonical spin-network coefficient norm is EXACTLY

**sum_(k=1)^r binom(r,k)|3r−4k|/(8k).**

For all r>=18, Chebyshev's binomial concentration inequality and a uniform |coefficient|>=1/16 on k∈[r/3,2r/3] establish

**||K^-1 Q Gamma_K(F_r,F_r)||_(SN,l1) >= 2^r/32**,

and the orthogonality of the physical eigenfunctions gives the **basis-independent Hilbert lower bound ||K^-1QGamma(F_r,F_r)||_L2 >= 2^(r/2)/sqrt(512)**. The normalized l1 ratio tends to 1/4 as r→∞. This shows diagonalizing the physical electric inverse alone does **not** give uniform nonlinear boundedness of the unweighted coefficient or L2 algebras.

**Original-link locality remains true:** for original-edge supports E_f,E_g, Gamma_K(f,g)=sum_(e∈E_f∩E_g) sum_a (nabla_(e,a)f)(nabla_(e,a)g), so it vanishes for link-disjoint inputs and is supported in E_f∪E_g. The counterexample uses r **disconnected plaquette support components** and therefore does NOT disprove a support-weighted connected-polymer algebra. Any next positive theorem must track this connected-component factorization and control energy-weighted recoupling/fusion coefficients in the **same** anchored physical norm, including support incidence.

The exact rational verifier passed **193,601 checks** for 1<=r<=150 and original-link edge separation. Full mathematical proof, checker, log and SHA256 manifest are preserved in The Singular Boundary / Proof Audits Library.

**Limit:** This is an original-link planar ladder *free-electric nonlinear Poisson* calculation. It is neither a thermodynamic interacting lambda=1 gap theorem nor a continuum four-dimensional Yang–Mills mass gap proof.