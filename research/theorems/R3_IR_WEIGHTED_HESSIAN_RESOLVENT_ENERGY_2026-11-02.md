# Weighted Hessian resolvent energy — 2026-11-02

Conditional on the archived **pointwise anisotropic Bochner inequality** for the finite dressed SU(2) strip with c=11/120, define weights a_e=(6/5)^(2d(e,S)), Gamma_a(u)=sum_e a_e|grad_e u|², and H_a(u)²=sum_(e,d)a_e|Hess_de u|². The exact integrated weighted Bochner identity is
  int Gamma2_a(u) dnu = sum_e a_e <grad_e u,grad_e L u>_(L²nu),
and pointwise Gamma2_a(u)>=H_a(u)²+c Gamma_a(u).
For centered Poisson u=R g, Lu=Qg, grad Qg=grad g. Writing X=||grad_a u||₂, Y=||grad_a g||₂, Z=||H_a u||₂ gives Z²+cX²<=XY, whence **Z<=Y/(2sqrt(c))=sqrt(30/11) Y** by completing the square, independent of strip length.

For any original-link tail T separated by r=d(T,S), the norm of Hessian components with first index in T is <=(5/6)^r sqrt(30/11)||grad_a g||₂. Symmetry gives second index as well. The weighted gradient heat energy also yields ∫₀∞||H_a(P_t f)||₂²dt≤1/2||grad_a f||₂².

Unlike the previously derived unweighted Hessian resolvent estimate, the result detects spatial localization, but it requires weighted H¹ regularity of the source. It does not produce an L∞ Hessian estimate for the nonlinear interacting log-ground state or prove either an interacting lambda=1 gap or a continuum Yang-Mills mass gap. The continuous SU(2) pointwise Bochner certificate remains an analytic prerequisite. Detailed report, passing verifier, log and hash manifest are archived in the project Proof Audits Library.