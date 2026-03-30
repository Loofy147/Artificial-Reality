# Routing Dynamics of Fiber-Stratified Optimization (FSO)

This document explains how the **Spike anomaly** breaks the fiber-uniform constraint to achieve global Hamiltonian routing.

## 1. The Fiber-Uniform Constraint
In a symmetric toroidal graph $G = \mathbb{Z}_m^3$, a "fiber-uniform" routing strategy assigns the same routing permutation $P[s]$ to all nodes in a given fiber $F_s$.
- **The Subgroup Trap:** Since $F_s$ is a lower-dimensional manifold (a 2D quotient), fiber-uniform strategies often collapse into localized subgroups. Instead of visiting all $m^3$ nodes, a color might get trapped in a cycle of length $m^2$, visiting only $m$ fibers and $m$ coordinates in each.

## 2. The Spike: Breaking Uniformity
The Spike is a localized anomaly applied to a single column (e.g., $x_1 = 0$) and a subset of levels $s$.

### Mechanism of the Linkage
1. **Divergence:** When a packet (or color) hits the Spike node at $(x_0, 0, x_2)$, its standard fiber-uniform permutation $P[s]$ is swapped (e.g., `swap02`).
2. **Path Selection:** This swap diverts the packet onto a coordinate path it would not normally take in a uniform field.
3. **Loop Coupling:** By carefully selecting the s-levels for the Spike, we ensure that the packet exits its current $m^2$ localized cycle and enters a *different* $m^2$ cycle.
4. **Hamiltonian Emergence:** When all $m$ localized cycles are linked via the Spike, a single Hamiltonian path of length $m^3$ emerges.

## 3. Verified Dynamics ($m=3$)
For $m=3$, the Spike is defined by:
- **Condition:** $x_1 = 0$ AND $s \in \{0, 2\}$.
- **Action:** `swap_dims(0, 2)`.
- **Result:** This configuration successfully couples the $3^2=9$ node sub-cycles into three edge-disjoint $3^3=27$ Hamiltonian paths.

## 4. The Complexity of Higher $m$
As $m$ increases, the number of localized cycles to link increases, and the "joint sum" constraints ($\sum b \equiv S \pmod m$) become more sensitive. Lemma 6.1 (Composite $m$ Spike Failure) proves that simple single-level spikes are insufficient for all grid sizes, requiring generalized Simulated Annealing (SA) to find the global "coupling" parameters.
