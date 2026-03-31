import math

class SubgroupDecomposer:
    """
    Law X: Recursive Subgroup Decomposition
    Complex manifolds are decomposed into simpler quotients G_{m'}^k.
    Hamiltonian solvability is verified on each level.
    """
    def __init__(self, m=256, k=4):
        self.m = m
        self.k = k
        self.divisors = self._find_divisors(m)

    def _find_divisors(self, n):
        """Find all proper divisors of n (excluding 1 and n)."""
        divs = []
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divs.append(i)
                if i*i != n:
                    divs.append(n // i)
        return sorted(divs, reverse=True)

    def project_to_quotient(self, coord, m_prime):
        """Map a coordinate from Z_m^k to Z_{m'}^k."""
        if self.m % m_prime != 0:
            raise ValueError(f"{m_prime} is not a divisor of {self.m}")
        return tuple(x % m_prime for x in coord)

    def verify_recursive_solvability(self, coord, target_fiber):
        """
        Verify that a coordinate's fiber property is preserved across all quotients.
        If sum(coord) = target mod m, then sum(coord') = target mod m'.
        """
        print(f"\n--- Law X: Recursive Verification for {coord} ---")
        original_sum = sum(coord) % self.m
        is_valid_original = (original_sum == target_fiber)
        print(f"Original (m={self.m}): Sum={original_sum} == {target_fiber}? {is_valid_original}")

        all_valid = is_valid_original
        for m_prime in self.divisors:
            q_coord = self.project_to_quotient(coord, m_prime)
            q_target = target_fiber % m_prime
            q_sum = sum(q_coord) % m_prime
            is_valid_q = (q_sum == q_target)
            print(f"  Quotient (m={m_prime}): {q_coord} Sum={q_sum} == {q_target}? {is_valid_q}")
            all_valid = all_valid and is_valid_q

        return all_valid

if __name__ == "__main__":
    decomposer = SubgroupDecomposer(m=256, k=4)
    # Test a coordinate on Fiber 2: (100, 100, 50, 8) -> sum = 258 = 2 mod 256
    test_coord = (100, 100, 50, 8)
    decomposer.verify_recursive_solvability(test_coord, 2)
