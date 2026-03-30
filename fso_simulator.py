import collections

class FSORouter:
    def __init__(self, m, r=None):
        self.m = m
        self.r = r if r else [1, m - 2, 1]
        if m == 3: self.r = [1, 1, 1]

    def get_permutation(self, x):
        m = self.m
        s = sum(x) % m
        if s == 0: p = [0, 1, 2]
        elif s == 1: p = [0, 2, 1]
        else: p = [1, 0, 2]

        if m == 3:
            # Verified spike for m=3: x1=0, s!=1, swap_dims(0, 2)
            if x[1] == 0 and s != 1:
                d0_idx = p.index(0); d2_idx = p.index(2)
                p[d0_idx], p[d2_idx] = 2, 0
        return p

    def step(self, x, color):
        p = self.get_permutation(list(x))
        dim = p[color]
        nx = list(x)
        nx[dim] = (nx[dim] + self.r[dim]) % self.m
        return tuple(nx), dim

    def trace_cycle(self, color, start_node=(0, 0, 0)):
        visited = set(); edges = set(); curr = start_node
        for _ in range(self.m ** 3):
            if curr in visited: break
            visited.add(curr)
            next_node, dim = self.step(curr, color)
            edges.add((curr, dim))
            curr = next_node
        return visited, edges, curr

def verify_fso_routing(m):
    print(f"\n--- Verifying FSO Routing for m={m} ---")
    router = FSORouter(m)
    all_edges = set(); total_nodes = m ** 3; success = True
    for color in range(3):
        nodes, edges, final_node = router.trace_cycle(color)
        is_ham = len(nodes) == total_nodes and final_node == (0, 0, 0)
        print(f"Color {color}: Hamiltonian={is_ham}, Length={len(nodes)}")
        if not is_ham: success = False
        if all_edges.intersection(edges): success = False
        all_edges.update(edges)
    final_success = success and (len(all_edges) == 3 * total_nodes)
    print(f"Overall Success: {final_success}")
    return final_success

if __name__ == "__main__":
    verify_fso_routing(3)
