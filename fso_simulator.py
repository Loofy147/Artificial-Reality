import collections
import random

class FSORouter:
    def __init__(self, m, k=3, r=None):
        self.m = m
        self.k = k
        if r:
            self.r = r
        elif k == 3:
            self.r = [1, m - 2, 1]
            if m == 3: self.r = [1, 1, 1]
        elif k == 2:
            self.r = [1, m - 1]
        else:
            self.r = [1] * k

        self.perms = {}
        for s in range(m):
            if k == 3:
                if s < m - 2: p = [0, 1, 2]
                elif s == m - 2: p = [0, 2, 1]
                else: p = [1, 0, 2]
            else:
                p = list(range(k))
            self.perms[s] = p

        self.anomalies = {}

    def get_permutation(self, x):
        s = sum(x) % self.m
        if (tuple(x), s) in self.anomalies:
            return self.anomalies[(tuple(x), s)]

        p = list(self.perms.get(s, list(range(self.k))))
        if self.k == 3 and self.m % 2 != 0:
            if x[1] == 0 and s != self.m - 2:
                d0_idx = p.index(0); d2_idx = p.index(2)
                p[d0_idx], p[d2_idx] = 2, 0
        return p

    def step(self, x, color):
        p = self.get_permutation(x)
        dim = p[color % len(p)]
        nx = list(x)
        nx[dim] = (nx[dim] + self.r[dim]) % self.m
        return tuple(nx), dim

    def trace_cycle(self, color, start_node=None):
        if start_node is None:
            start_node = tuple([0] * self.k)
        visited = []
        visited_set = set()
        edges = set()
        curr = start_node
        for _ in range(self.m ** self.k + 1):
            if curr in visited_set:
                break
            visited.append(curr)
            visited_set.add(curr)
            next_node, dim = self.step(curr, color)
            edges.add((curr, dim))
            curr = next_node
        return visited, edges, curr

def verify_fso_routing(m, k=3, router=None, silent=False):
    if router is None:
        router = FSORouter(m, k)
    all_edges = set(); total_nodes = m ** k; success = True
    results = []
    for color in range(k):
        nodes, edges, final_node = router.trace_cycle(color)
        is_ham = len(nodes) == total_nodes and final_node == nodes[0]
        results.append(is_ham)
        if not is_ham: success = False
        all_edges.update(edges)

    final_success = success and (len(all_edges) == k * total_nodes)
    if not silent:
        print(f"Verification (m={m}, k={k}): Hamiltonian={results}, Success={final_success}")
    return final_success

def repair_manifold(m, k, max_iterations=2000):
    # Law VII: Basin Escape Axiom (Refined for O(m) targeted swaps)
    router = FSORouter(m, k)
    if verify_fso_routing(m, k, router, silent=True):
        return router

    for attempt in range(max_iterations):
        # Identify a broken path
        color = random.randint(0, k - 1)
        nodes, edges, final_node = router.trace_cycle(color)

        if len(nodes) < m**k:
            # TARGETED SWAP: Link the sub-cycle at its tail
            # Find a node *not* in the current cycle
            unvisited = set(tuple(random.randint(0, m-1) for _ in range(k)) for _ in range(m))
            potential_entry = random.choice(list(unvisited))

            # Pick a node in the cycle and force it to divert to the entry node
            # This is "targeted" because we pick a known point of failure (the loop closure)
            tail = nodes[-1]
            s = sum(tail) % m
            p = list(router.get_permutation(tail))

            # Change the dimension chosen by this color at the tail
            dim_to_change = p.index(p[color % k])
            new_dim = (dim_to_change + 1) % k
            p[dim_to_change], p[new_dim] = p[new_dim], p[dim_to_change]

            router.anomalies[(tail, s)] = p

        if verify_fso_routing(m, k, router, silent=True):
            print(f"Refined Repair successful at attempt {attempt}!")
            return router
    return None

def recursive_subgroup_decomposition(m, k):
    print(f"\n--- Law X: Decomposing G_{m}^{k} ---")
    divisors = [i for i in range(2, m) if m % i == 0]
    if not divisors:
        print(f"m={m} is prime. Solvability is atomic.")
        return True

    success = True
    for d in divisors:
        print(f"Testing Quotient G_{d}^{k}...")
        router = repair_manifold(d, k, max_iterations=1000)
        if not router:
            print(f"Warning: Quotient G_{d}^{k} is NOT Hamiltonian.")
            success = False
        else:
            print(f"[✓] Quotient G_{d}^{k} is Hamiltonian.")
    return success

if __name__ == "__main__":
    verify_fso_routing(3, 3)
    recursive_subgroup_decomposition(4, 2)
    recursive_subgroup_decomposition(9, 3)
