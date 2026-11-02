# R3-IR — Third cut-strength coefficient: exact algebra and conditional spatial locality

For H_t=L0+tV, A=V−〈V〉0, R=L0^−1 Q, u=RA, T=RQ(Au), n=||u||², b=〈A,u〉, the normalized ground-vector recursion yields h1=−u, h2=T−(n/2)1, h3=−RQ(A T−(n/2)A−b u)+〈u,T〉1. For centered multiplication observable O, the **exact** third coefficient of its ground-state expectation is

**a3(O)=−2〈O,RQ(A T−(n/2)A−b u)〉−2〈O,uT〉+n〈O,u²〉**.

An independent two-state reversible example, L=[[1,−1],[−1,1]], V=diag(0,1), O=diag(1,−1), has μ_t(O)=t/sqrt(t²+4) and a3=−1/16, exactly matched by symbolic normalized recursion. This verifies perturbation algebra, not SU(2) geometry.

Conditionally on the archived p=2,4 **weighted Bochner/Poisson estimates for the cut generator**, full SU(2) cut-potential pointwise gradient certificate, and exact right-prefix centering, one obtains for a cut after face j and right residual bond k≥j+2:

**|a3(w_k)|≤0.00019491628946309325 (5/6)^max(0,k−j−2)**.

Constants: κ=23/144; B=120/11; c=269/72000; a=2c; v=1/1152; G=√30·15989/1728000; K=B/√κ. Set U4=2√2 a/κ, g_u=B G, G_T4=B(a g_u+G U4), T4=(4√2/κ)a U4, nmax=a²/κ², bmax=a²/κ; M=a B(a B G+G a/κ)+G a²/κ²+(nmax/2)G+bmax B G. Then C3=2v K M+(2v/√κ)(U4 G_T4+T4 g_u)+(2v/√κ)nmax U4 g_u. Components approximately 4.21612e−5, 1.52060e−4, 6.95536e−7.

Higher cut coefficients n≥4 and summability of spatial constants remain open, as do fourth-order connected energy extensivity, interacting λ=1 and continuum Yang–Mills mass gaps. Full detailed proof, test, log, and SHA256 manifest archived in Library /The Singular Boundary/Proof Audits.