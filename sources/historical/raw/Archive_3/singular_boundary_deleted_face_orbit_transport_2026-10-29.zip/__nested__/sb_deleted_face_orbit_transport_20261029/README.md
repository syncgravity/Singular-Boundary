# Exact nonabelian deleted-face flux transport

This package provides a mathematical report and a deterministic verifier for a gauge-compatible Haar-fiber transport and its exact electric commutator reduction. It **does not** establish a polynomial near-flat probability for the actual nonlinear deleted Penrose vacuum or a Yang–Mills mass gap.

Run `python verify_orbit_transport.py`. It requires NumPy. The five-dimensional Penrose spatial seed is reconstructed explicitly; growing square-grid tests are surrogates. All verification is algebraic/deterministic, without Monte Carlo or modification of archived experiments.

The missing quantitative hypothesis is a volume-uniform collective orbital Fisher bound `J_gamma = o(h^(3/2))` or an equivalent cap-restricted statement for the actual magnetic-deleted ground state.
