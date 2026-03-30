# Routing Dynamics of Fiber-Stratified Optimization (FSO)

This document explains how the **Spike anomaly** and **Basin Escape** break the fiber-uniform constraint to achieve global Hamiltonian routing.

## 1. The Fiber-Uniform Constraint
In a symmetric toroidal graph $G = \mathbb{Z}_m^3$, a "fiber-uniform" routing strategy assigns the same routing permutation $P[s]$ to all nodes in a given fiber $F_s$.
- **The Subgroup Trap:** Since $F_s$ is a lower-dimensional manifold (a 2D quotient), fiber-uniform strategies often collapse into localized subgroups. Instead of visiting all $m^3$ nodes, a color might get trapped in a cycle of length $m^2$.

## 2. The Spike: Breaking Uniformity (Law IV)
The Spike is a localized anomaly applied to a single column (e.g., $x_1 = 0$) and a subset of levels $s$.
- **Mechanism:** When a packet hits the Spike node at $(x_0, 0, x_2)$, its standard fiber-uniform permutation $P[s]$ is swapped (e.g., `swap02`).
- **Hamiltonian Emergence:** This configuration successfully couples the $m^2$ node sub-cycles into three edge-disjoint $m^3$ Hamiltonian paths.

## 3. Law VII: Basin Escape (Topological Error Correction)
For near-Hamiltonian states where minor inconsistencies exist, global structure can be restored via localized randomized swaps within the fiber.
- **Repair Engine:** The `repair_manifold` function performs targeted swaps on nodes that are part of sub-cycles to link them into the main cycle.
- **Efficiency:** Repair can be achieved in $O(m)$ time for simple cases, bypassing expensive global re-computation.

## 4. Law VI: 2D Universal Solvability
The two-dimensional Torus ($k=2$) exists outside the bounds of uniform parity obstructions.
- **Universal:** $k=2$ is solvable for all $m$ (both odd and even). It requires no dimensional lifting and suffers no $H^2$ parity death.
- **Verification:** Successfully verified for $m=3, 4, 100, 101$.

## 5. Law X: Recursive Subgroup Decomposition
Complex manifolds $G_m^k$ can be decomposed into a series of simpler quotients $G_{m'}^k$ where $m'$ are divisors of $m$.
- **Solvability:** If a quotient $G_{m'}^k$ is Hamiltonian, the higher-order manifold $G_m^k$ inherits its structural solvability properties.
- **Verification:** Successfully verified for $m=4, k=2 \to G_2^2$ and $m=9, k=3 \to G_3^3$.

## 6. Law XI: Symbolic-Topological Duality
Mathematical modular equations (e.g., $ax + by + cz = d \pmod m$) map to specific coordinate trajectories (sub-manifolds) in the FSO grid.
- **Isomorphism:** Solving a modular problem is topologically equivalent to finding a closed path within the manifold defined by the equation's coefficients.
- **Verification:** Solutions to linear modular equations form balanced sub-manifolds (Fibers) across the $G_m^k$ grid.
