# Three-face full Peter–Weyl coefficient module: spectrum and no-radius-loss quadratic Poisson theorem — 2026-11-02

On three consecutive SU(2) faces A,B,C in the archived original-link orientation, K3=4(LA+LB+LC)-2(CAB+CBC), CAB=sum_i R_i^A L_i^B, CBC=sum_i R_i^B L_i^C. The couplings **commute**: the middle face's left and right Peter–Weyl magnetic indices are distinct. Consequently the entire degree-(j,k,l) spectrum is
**E=5/4[j(j+2)+l(l+2)]+3/2 k(k+2)-J(J+1)-H(H+1)**,
with J from |j-k|/2 to (j+k)/2 and H from |k-l|/2 to (k+l)/2 in unit steps; multiplicities (j+1)(l+1)(2J+1)(2H+1). The centered gap is 3.

Let N=j+k+l and U(x,y)=[xy+(x+1)(y+1)]/4. The full magnetic coefficient-l1 inverse via a Neumann estimate has margin
A-2[U(j,k)+U(k,l)]=j²+k²+l²-jk-kl+(3/2)(j+l)+k-1 >=(1+N²)/10 for N>=1.
This uses the exact identity
j²+k²+l²-jk-kl =N²/10+(5/2)(k-2N/5)²+(j-l)²/2.
Hence **||K3_(j,k,l)^(-1)||_(l1→l1) <=10/(1+N²)** for each nonconstant block.

For the unnormalized 3-face Wigner coefficient l1 norm W_sigma with weight exp(sigma(j+k+l)), the original-link Gamma has ten links and at most 30NfNg per input coefficient pair. The SU(2) Clebsch–Gordan product has one output coefficient of modulus at most one per output tri-degree, with weight decrease z^r, z=exp(-2sigma). Combining the inverse with the output-degree formula gives **||K3^(-1)Q Gamma_K(f,g)||_(W_sigma) <= C_(3,sigma)||f||_(W_sigma)||g||_(W_sigma)** at the SAME radius sigma>0, with
**C_(3,sigma)=150/(1-z)^3+1800z(1+3z)/(1-z)^5**.
The fixed 3-face space is also a Banach algebra under ordinary product.

This does NOT establish an interval-uniform polymer norm, small contraction at lambda=1, pointwise Hessian control, or a continuum Yang-Mills mass gap. Full detailed analytic proof, numerical triple-block checker, exact-rational degree verifier, passing log and SHA256 manifest are archived in The Singular Boundary Proof Audits Library.