# Verification Instructions for FSO

## 1. Mathematical Integrity
- Ensure all theorems, lemmas, and definitions from the whitepaper are present in the whitepaper and verified in `verify_fso.py`.
- Verify the $H^2$ parity obstruction (even $m$, odd $k$).
- Verify the canonical $r$-triple: $(1, m-2, 1)$.

## 2. LaTeX Syntax
- The document `fso_whitepaper.tex` must be valid LaTeX.
- All environments (`theorem`, `lemma`, `proof`, `definition`) must be closed.

## 3. Computational Proofs
- Run `python3 verify_fso.py` to confirm the algebraic density and parity obstruction theorems.
- Run `python3 fso_simulator.py` to verify the Hamiltonian Spike routing for $m=3$.

## 4. Routing Dynamics
- Ensure `ROUTING_DYNAMICS.md` correctly explains how the Spike breaks the $m^2$ subgroup constraint.
- The Spike parameters for $m=3$ (x1=0, s!=1, swap_dims(0,2)) are the only verified Hamiltonian configuration for higher-dimensional linkage.
