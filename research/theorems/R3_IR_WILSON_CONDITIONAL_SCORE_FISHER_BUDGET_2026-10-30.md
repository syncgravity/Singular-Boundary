# R3-IR-436 — Conditional score Fisher bound from the full Wilson electric budget

2026-10-30. Exact finite-volume full-coupling estimate on the original-link SU(2) Wilson disk. It controls a weighted integrated conditional score, not a regulator-uniform cap susceptibility.

Let H=sum_e a_e(-Delta_e)+sum_{g retained} b_g(1-p_g), with a_e>0, b_g>=0, target face deleted, and Omega>0 the normalized genuine physical vacuum. Haar-normalized constant wavefunction 1 is gauge invariant, has zero electric energy, and integrates every nontrivial face trace p_g to zero. Thus E0<=sum_g b_g. Since every magnetic term is nonnegative, the ground-state kinetic budget obeys

sum_e a_e int |grad_e Omega|² dHaar <= sum_g b_g. (SF-1)

Choose the selected private x link and environmental coordinates y, and disintegrate Omega²dHaar=rho_y(x)dx nu(dy). Let v(y) be a smooth environmental vector field. Its conditional-density score is h(x,y)=v dot grad_y log rho_y(x). Differentiation of rho_y=Omega(x,y)²/N(y) and N(y)=int Omega²dx shows exactly

h=2[v dot grad_y log Omega-E_(rho_y)(v dot grad_y log Omega)].

Consequently, by conditional variance contraction and weighted Cauchy-Schwarz,
int h² dmu <=4 int |v dot grad_y log Omega|²dmu
<=4 V_infty(v) sum_(e environmental) a_e int |grad_e Omega|² dHaar
<=4 V_infty(v) sum_g b_g, (SF-2)
where V_infty(v)=esssup_y sum_(e environmental) |v_e(y)|²/a_e and the environmental vector norm uses the compatible link metrics.

This is a true Wilson-specific integrated bound on the conditional-density score variance, with all retained magnetic interactions active and without assuming a global spectral gap. It is applicable to the residual score term in R3-IR-434/435. For example, lambda_x(y)>=3r_s²/4 from R3-IR-435 implies

int lambda_x(y)^(-1) Var_(rho_y)(v dot grad_y log rho_y) dnu
<= (16/3)r_s^(-2) V_infty(v) sum_g b_g. (SF-3)

The RHS may be extensive in the full magnetic volume, and requires a sup-norm bound on a legitimate marginal environmental flux v. Neither is established uniformly under Penrose refinement. No local replacement of sum_g b_g by b_g alone is claimed, and this result does NOT imply the half-Haar cap bound or continuum Yang-Mills mass gap.
