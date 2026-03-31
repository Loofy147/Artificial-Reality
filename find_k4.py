import itertools

def verify(m, k, r, p_list):
    def get_p(x):
        s = sum(x) % m
        return p_list[s]

    all_edges = set()
    for color in range(k):
        visited_set = set()
        curr = tuple([0]*k)
        edges = set()
        for _ in range(m**k):
            if curr in visited_set: return False
            visited_set.add(curr)
            p = get_p(curr)
            dim = p[color]
            edges.add((curr, dim))
            nx = list(curr)
            nx[dim] = (nx[dim] + r[dim]) % m
            curr = tuple(nx)
        if curr != (0,0,0,0): return False
        if all_edges.intersection(edges): return False
        all_edges.update(edges)
    return True

perms = list(itertools.permutations(range(4)))
r = [1, 1, 1, 1]
for p0 in perms:
    for p1 in perms:
        if verify(2, 4, r, [p0, p1]):
            print(f"Solution: p0={p0}, p1={p1}")
            import sys
            sys.exit(0)
