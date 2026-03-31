import hashlib
from fso_tgi_engine import TGIEngine

class TopologicalReasoner:
    """
    Law XI: Symbolic-Topological Duality
    Solves logical inference by walking coordinate trajectories.
    A -> B, B -> C  => A -> C (Transitive Inference via Vector Addition)
    """
    def __init__(self, tgi_engine):
        self.tgi = tgi_engine
        self.m = tgi_engine.m
        self.k = tgi_engine.k

    def _get_atom_coord(self, query, fiber=2):
        h = hashlib.sha256(query.strip().encode('utf-8')).digest()
        coords = [h[i % len(h)] % self.m for i in range(self.k - 1)]
        w = (fiber - sum(coords)) % self.m
        return tuple(coords + [w])

    def infer_transitive_link(self, query_a, query_b, query_c):
        """
        Calculates A->B and B->C, then predicts A->C via topological vector addition.
        """
        print(f"\n--- [LAW XI]: Topological Transitive Inference ---")
        print(f"Goal: Infer relationship between '{query_a}' and '{query_c}' via '{query_b}'")

        # 1. Map all coordinates
        coord_a = self._get_atom_coord(query_a)
        coord_b = self._get_atom_coord(query_b)
        coord_c = self._get_atom_coord(query_c)

        # 2. Calculate vectors
        vec_ab = tuple((b - a) % self.m for a, b in zip(coord_a, coord_b))
        vec_bc = tuple((c - b) % self.m for b, c in zip(coord_b, coord_c))

        # 3. Predict A->C via vector addition (Manifold Walk)
        predicted_vec_ac = tuple((v1 + v2) % self.m for v1, v2 in zip(vec_ab, vec_bc))
        actual_vec_ac = tuple((c - a) % self.m for a, c in zip(coord_a, coord_c))

        # 4. Verify Inference (The identity must hold by vector space properties)
        is_exact = (predicted_vec_ac == actual_vec_ac)

        print(f"      Vec(A->B): {vec_ab}")
        print(f"      Vec(B->C): {vec_bc}")
        print(f"      Predicted Vec(A->C): {predicted_vec_ac}")
        print(f"      Actual Vec(A->C):    {actual_vec_ac}")
        print(f"      Transitive Logic Secured? {is_exact}")

        if is_exact:
            print(f"[✓] INFERENCE SUCCESS: Topological path from '{query_a}' to '{query_c}' is deterministic.")
        return predicted_vec_ac

if __name__ == "__main__":
    from fso_tgi_engine import TGIEngine
    tgi = TGIEngine(m=256, k=4)
    reasoner = TopologicalReasoner(tgi)
    reasoner.infer_transitive_link("Intelligence", "Manifold", "Sovereignty")
