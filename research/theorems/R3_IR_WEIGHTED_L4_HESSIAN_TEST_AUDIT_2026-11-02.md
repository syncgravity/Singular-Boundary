# Weighted L4 Hessian test audit — 2026-11-02

Assuming the archived weighted pointwise Bochner inequality Gamma2,a(u)>=H_a(u)^2+c G_a(u), with c=11/120, and u=R g, multiply the exact Gamma2 identity by G_a(u)=sum_e a_e |grad_e u|^2. Invariance and integration by parts yield

integral G_a H_a^2+c integral G_a^2+(1/2)integral |grad G_a|^2 <= integral G_a sum_e a_e <grad_e u,grad_e g>.

The estimate bounds Hessian energy weighted by squared gradient, not the fourth power of the Hessian. For scalar circle u=sin(kx), the exact unweighted equality has three coefficients k^6/8, k^6/4 and 3k^6/8, checked independently for k=1..9. At critical points, grad u=0 but Hess u nonzero, so no positive direct inequality of the form G H^2 >= C H^4 holds pointwise. This demonstrates an obstruction to the particular testing method, not impossibility of a stronger SU(2)-specific W2,4 theorem. Weighted Hessian-resolvent L4, interacting lambda=1 gap and continuum Yang–Mills gap remain open. Full mathematical audit, script, log and SHA256 in Proof Audits Library.