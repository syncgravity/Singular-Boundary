# PF-I16 — Connected-support counting with source-uniform incidence constants

**Date:** 2026-11-10  
**Scope:** correction and strengthening of the combinatorial counting gate for the authentic five-direction coupled-\(\mathbb Z^5\) Penrose–Fibonacci accepted-rhombus complex.  
**Status:** exact combinatorial upper bound established from the elementary five-direction inventory; sharper degree-four bound supported on the eight recorded finite source crops, but not yet proved for every source region/refinement. No all-orders quantum activity bound or interacting gap is claimed.

## 1. Why the incidence constant needs qualification

Two source records contain different levels of incidence information:

* The PF-I16 four-face counting argument used the statement that each original link belongs to at most two accepted rhombi. If this is valid uniformly, the face-overlap graph has maximum degree at most four.
* The PF-I11/PF-I16 source geometry record gives a universal elementary-inventory bound of at most \(2(5-1)=8\) candidate coordinate rhombi incident to an original link. The PF-I11 evidence table records zero edges with more than two accepted-face incidences for each of the eight tested original crops \(N_{grid}=7,10,12,15,18,20,23,25\). That finite census is stronger on those crops, but by itself is not a proof for every accepted source region or every refinement.

Accordingly, a source-volume-uniform theorem should use the conservative universal bound eight unless the strict triangular acceptance rule is separately proved to reduce the maximum to two for all source points.

## 2. Universal face-overlap degree bound

Let \(\mathcal G_F\) be the simple graph whose vertices are accepted rhombi, with two faces adjacent when they share an original link. Every rhombus has four boundary links. Each original link is incident to at most eight elementary coordinate rhombi. Therefore a fixed face has at most seven other faces incident through each of its four links, so

\[
\boxed{\Delta(\mathcal G_F)\le 4(8-1)=28.}
\]

This is a safe bound; it may overcount a neighboring face that shares more than one link.

For the eight explicitly recorded source crops, the evidence reports greater_than_two_incidence_edges = 0, hence the observed maximum face-edge incidence is at most two and the crop-specific overlap degree is at most four. This sharper constant is retained as a finite-crop observation, not silently promoted to a theorem for all source volumes.

## 3. Corrected connected-support count

Fix a root face \(f\). For a connected set \(S\subseteq F\) with \(|S|=k\) and \(f\in S\), choose a deterministic spanning tree of the induced connected subgraph and its depth-first closed traversal. The traversal has length \(2(k-1)\), starts at \(f\), and at each step has at most \(D\) choices if the face-overlap graph has maximum degree \(D\). The visited-vertex set recovers \(S\), so the chosen walk encoding is injective. Thus

\[
\#\{S\ni f: |S|=k,\ S\text{ connected}\}\le D^{2(k-1)}.
\]

Using the universal \(D=28\),

\[
\boxed{N_f(k)\le 784^{k-1}.}
\]

The previous \(16^{k-1}\) estimate is valid on any source family for which the degree-four incidence statement is proved; it is also valid for the eight finite crops whose evidence records no edge with more than two accepted-face incidences. It is not yet the safe all-source-volume constant.

## 4. Conditional cluster-summability implication

Let \(\zeta_G(S;\mathbf b)\) be the exact-support Möbius activity, with disconnected supports vanishing by tensor factorization. If a separate quantum theorem proves

\[
|\zeta_G(S;\mathbf b)|\le A q^{|S|}
\]

with \(A,q\) independent of source volume, then

\[
\sum_{\substack{S\ni f,\ S\text{ connected}}}|\zeta_G(S;\mathbf b)|
\le A\sum_{k\ge1}784^{k-1}q^k
=\boxed{\frac{Aq}{1-784q}},\qquad 784q<1.
\]

Therefore the safe combinatorial threshold is \(q<1/784\). Under a separately proved degree-four source-uniform theorem it improves to \(q<1/16\).

This is only a counting implication. It does not prove the required activity estimate.

## 5. Why the existing finite-support Cauchy estimate still fails

The fixed-support Riesz/Cauchy argument gives, for a connected support of \(k\) faces and first allowed multi-index of total degree \(2k\),

\[
|C_{(2,\ldots,2)}(S)|\le \frac{3a_0}{4}\left(\frac{4k}{3a_0}\right)^{2k}.
\]

This is a valid fixed-support analytic envelope, but its \(k^{2k}\) growth is not absorbed by either \(16^{k-1}\) or \(784^{k-1}\) at any fixed nonzero coupling. The correct conclusion is that the finite-support Cauchy estimate plus connected-support counting is insufficient; it does not imply divergence of the true Wilson-vacuum expansion.

The next quantum step must improve the coefficient estimate before taking absolute values—most plausibly by a local dressed reference state or a linked-cluster/Kirkwood–Thomas construction that treats repeated insertions on one plaquette nonperturbatively and bounds only genuinely connected shared-link fusion. Any such theorem must retain the original-link SU(2) recoupling and the infinite Peter–Weyl tower.

## 6. Proof ledger

**Established here:** the universal incidence-based degree bound \(28\); the depth-first connected-support count \(784^{k-1}\); the conditional geometric-series implication; the finite-crop degree-four observation as recorded in PF-I11 evidence.

**Not established:** a uniform degree-four incidence theorem for all accepted source regions; a volume-independent bound \(|\zeta_G(S)|\le Aq^{|S|}\); convergent all-orders cluster expansion; conditional tensorization/Poincaré; the interacting physical gap; source-derived physical time; continuum reconstruction or Yang–Mills mass gap.

**Source discipline:** this note does not alter the accepted source geometry, the original crop populations, Stage 26 archives, or the canonical theorem ledger. The unit-electric four-face coefficients remain finite-support auxiliary results only.
