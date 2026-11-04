# Exact nonzero tenth-order deleted-face coefficient on extracted open disk

Date: 2026-10-30. Unit electric weights and ten elementary retained magnetic couplings. This is a finite-regulator theorem, NOT a continuum mass gap.

Let C=(1,3,2,4,154,150,11,10,7,8) surround deleted face 0 in the extracted eleven-face open disk. The squarefree tenth-order ground-state coefficient is F_C=R S_C, where R=T_perp^-1 and S_C is the 901-product exact rational source from the forest recursion. For each partition pi of C into k=2,...,10 nonempty connected interval blocks, W_pi is the product of their normalized Wilson half-traces and c_pi>0 its exact source coefficient. The k cut edges each occur twice; twenty boundary edges occur once. Let E_e Haar-project individual cut edges onto spin zero. On W_pi the electric inverse has eigenvalues [15+2r]^-1 and expansion in E_e.

Every term averaging a STRICT subset of the k cut edges joins only proper cyclic intervals. Its Wilson traces depend solely on retained based-face holonomies; the deleted-face Haar complement Q_f annihilates it. Averaging ALL k cut edges yields, by k-1 successive fundamental SU2 Schur mergers and one final annular Schur split, E_all W_pi = 4^(1-k) p_inner p_outer, independent of pi. The two boundary traces are the four-edge deleted-face inner boundary and 16-edge outer disk boundary. The same identity is directly verified on the oriented two-loop smoothing: averaging edge 3 merges two traces by factor 1/4, then averaging edge 14 splits into the inner and outer trace product.

The coefficient of the all-cut projection in the inverse is alpha_k=sum_(j=0)^k (-1)^j binomial(k,j)/(15+2j) = integral_0^1 t^14(1-t^2)^k dt >0. Thus

Q_f F_C = kappa Q_f(p_inner p_outer),
kappa=sum_pi c_pi * 4^(1-k(pi)) * alpha_(k(pi))
=2376252926673252101321919045001703951557/3082322838199847861301112342611033200018689536000000 >0.

Under independent based-face product Haar, choose U=deleted face holonomy and V=the ordered product of ten retained face holonomies. Both are independent Haar and p_inner=p_U, p_outer=p_UV up to orientations and conjugation. Conditional Haar averaging gives P_f(p_U p_UV)=p_V/4. Consequently ||Q_f(p_inner p_outer)||_2^2=1/16-1/64=3/64 and

||Q_f F_C||_2=kappa sqrt(3)/8 = approximately 1.6691108527084225e-13 >0.

The exact local Fraction solver and oriented-word regression passed; runnable validation in research/scripts/validate_complete_tenth_projection.py. This proves an actual nonzero squarefree perturbative coefficient of the finite open-disk deleted Hamiltonian ground state, not a quantitative lower bound on its response at any specified nonzero couplings, not a uniform center cap, and not the continuum Yang-Mills mass gap.
