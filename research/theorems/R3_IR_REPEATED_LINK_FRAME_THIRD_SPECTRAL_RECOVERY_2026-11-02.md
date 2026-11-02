# Exact weighted recovery of repeated SU(2) link frame third derivatives

On undressed SU(2)^m with Haar measure, L0=-sum_{e,a}X_{e,a}^2, R0=L0^{-1}Q0 and positive configuration-independent weights a_k, for every smooth g,

sum_{k,c,e,a,d,b} a_k ||X_{e,a}X_{d,b}X_{k,c}R0g||_2^2 = sum_{k,c} a_k ||X_{k,c}g||_2^2.

This is **exact, with constant one and no dimension dependence**, including all repeated-link indices. Proof: [L0,X_{k,c}]=0 and the double-frame energy identity sum_{e,a,d,b}||X_{e,a}X_{d,b}h||²=||L0h||². Set h=X_{k,c}R0g. For a source depending on link set S, the undressed resolvent stays on S, and frame derivatives outside S vanish.

Caution: covariant third tensor ∇Hess differs from ordered frame third derivatives by local SU(2) connection lower-order terms; no sharp covariant tensor bound is claimed. For dressed Lg=L0-2Y·grad, exact Haar frame recovery has right side sum a_k||X_{k,c}g+2X_{k,c}(Y·grad u)||² and controlling the new drift term uniformly remains open. Dressed measure is not Haar. No nonlinear lambda=1 interacting gap or continuum Yang–Mills mass gap established. Full mathematical proof, rational checker, passing log and SHA256 manifest archived in The Singular Boundary Proof Audits Library.