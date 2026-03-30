import collections
import random

class FSORouter:
    def __init__(self, m, k=3, r=None):
        self.m = m
        self.k = k
        if r:
            self.r = r
        elif k == 3:
            # Law IV: Canonical r-triple (1, m-2, 1)
            self.r = [1, m - 2, 1]
            if m == 3: self.r = [1, 1, 1]
        elif k == 2:
            # Law I: sum r = m, gcd(r_c, m) = 1
            # For even m, r=(1, m-1) works as both are odd.
            # For odd m, r=(1, m-1) also works as 1 and m-1 are coprime to m.
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

        # Check if there's a node-specific anomaly
        if (tuple(x), s) in self.anomalies:
            return self.anomalies[(tuple(x), s)]

        p = list(self.perms.get(s, list(range(self.k))))

        if self.k == 3 and self.m % 2 != 0:
            # Law IV Spike on column x1=0
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
    # Law VII: Basin Escape Axiom
    print(f"--- Law VII: Repairing Manifold (m={m}, k={k}) ---")
    router = FSORouter(m, k)

    if verify_fso_routing(m, k, router, silent=True):
        print("Manifold already Hamiltonian.")
        return router

    for attempt in range(max_iterations):
        # Pick a color that is stuck in a sub-cycle
        color = random.randint(0, k - 1)
        nodes, edges, final_node = router.trace_cycle(color)

        if len(nodes) < m**k:
            # Basin Escape: Pick a random node on the sub-cycle and swap its dim assignment
            target_node = random.choice(nodes)
            s = sum(target_node) % m
            p = list(router.get_permutation(target_node))
            i, j = random.sample(range(k), 2)
            p[i], p[j] = p[j], p[i]
            router.anomalies[(target_node, s)] = p

        if verify_fso_routing(m, k, router, silent=True):
            print(f"Repair successful at attempt {attempt}!")
            verify_fso_routing(m, k, router)
            return router

    print("Repair failed.")
    return None

if __name__ == "__main__":
    print("Standard Verifications:")
    verify_fso_routing(3, 3)

    print("\nRepairing 2D Manifolds (Law VI):")
    repair_manifold(3, 2)
    repair_manifold(4, 2)

    # print("\nRepairing m=5, k=3 (Law VII):")
    # repair_manifold(5, 3)
