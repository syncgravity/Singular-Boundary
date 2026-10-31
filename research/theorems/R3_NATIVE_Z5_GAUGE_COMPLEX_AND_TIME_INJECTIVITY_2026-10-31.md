# R3-IR-565 — Native coupled-Z5 SU(2) gauge cell complex and spatial-time arithmetic

Date 2026-10-31. Based on Paper 2's C5 projection and the source-defined native integer lattice, not a separable prism.

Construct all cubical cells of the **native unit five-cube** {0,1}^5. Cells in dimensions 0 through 5: **32,80,80,40,10,1**; exact integral boundary identities d[k-1]d[k]=0 for every k from 2 to 5; boundary ranks **31,49,31,9,1**. SU(2) matrices are assigned to the 80 native edges; 80 native elementary Wilson squares have gauge-invariant normalized traces. An independent random SU(2) check gave maximum Wilson-trace error 7.77e-16. Every native origin edge lies in four elementary plaquettes.

**Exact projection theorem.** Let omega=exp(2 pi i/5), z1=sum_j m_j omega^j, z2=sum_j m_j omega^(2j). For integer m,n, if z1(m)=z1(n), the difference polynomial sum(m_j-n_j)t^j is divisible by the minimal polynomial Phi5=1+t+t^2+t^3+t^4, so all coefficient differences are equal. It follows that z2(m)=z2(n). Therefore even the (x,y)=z1 projection is injective on Z5 modulo the diagonal redundancy, and determines both complementary coordinates (u,v). This is an arithmetic **discrete-label** fact, while the real-linear spatial projection (x,y,u) has rank 3 and the real-linear (x,y,u,v) projection has rank 4. It does not refute the paper's complex geometry or imply the coordinates are linearly dependent over R.

Define a native finite gauge Wilson action S=sum_f beta_f(1-p_f) for beta_f>=0 and p_f=Tr(U_f)/2. It is gauge invariant and has a finite positive Haar partition function. An *auxiliary* electric rotor Hamiltonian on L2(SU(2)^80)^Gauge may also be defined using the sum of Casimirs and the bounded Wilson potential, but this is **not** yet a Hamiltonian obtained by time-reconstructing the coupled-Z5 geometric coordinate v.

**Major unresolved step:** a physical time-reversal map and a positive transfer kernel must be constructed. Wilson Boltzmann positivity does NOT by itself imply Osterwalder–Schrader reflection positivity. Native edges change v in four of five directions and no exact independent time layer over fixed (x,y,u) is supplied by the integer point set. The five-cube is ambient and is NOT an acceptance-window-selected three-dimensional manifold. The finite complex does not establish a 3+1D continuum limit or Yang–Mills mass gap.

Full proof, reproducer and JSON archived in ChatGPT Library /The Singular Boundary/Source/:
R3_IR_565_native_Z5_gauge_and_projection_2026-10-31.md;
build_native_z5_gauge_complex.py;
native_z5_gauge_complex_2026-10-31.json.
No binary arrays in Git.