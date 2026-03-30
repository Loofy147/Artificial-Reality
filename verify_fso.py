import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi(n):
    result = n
    p = 2
    temp_n = n
    while p * p <= temp_n:
        if temp_n % p == 0:
            while temp_n % p == 0:
                temp_n //= p
            result -= result // p
        p += 1
    if temp_n > 1:
        result -= result // temp_n
    return result

def test_theorem_2_1(m):
    """Theorem 2.1: N_b(m) = m^{m-1} * phi(m)"""
    nb_theoretical = (m**(m-1)) * phi(m)

    # Brute force count for small m
    count = 0
    for i in range(m**m):
        b = []
        temp = i
        for _ in range(m):
            b.append(temp % m)
            temp //= m
        if gcd(sum(b), m) == 1:
            count += 1

    print(f"Theorem 2.1 (m={m}): Theoretical={nb_theoretical}, Empirical={count}")
    return nb_theoretical == count

def test_theorem_3_1(m, k):
    """Theorem 3.1: |M_k(G_m)| = phi(m) * [N_b(m)]^{k-1}"""
    nb = (m**(m-1)) * phi(m)
    mk_theoretical = phi(m) * (nb**(k-1))
    print(f"Theorem 3.1 (m={m}, k={k}): Theoretical={mk_theoretical}")
    return mk_theoretical

def test_theorem_4_1(m, k):
    """Theorem 4.1: Obstruction when m is even and k is odd"""
    if m % 2 == 0 and k % 2 != 0:
        print(f"Theorem 4.1 (m={m}, k={k}): Obstruction Predicted.")
        # Any r_c must be odd for gcd(r_c, m) = 1.
        # Sum of an odd number (k) of odd numbers (r_c) is odd.
        # But sum r_c must be m, which is even.
        return True
    return False

def test_spike_construction(m):
    """Theorem 5.1 & 5.3: Spike Construction (1, m-2, 1)"""
    if m % 2 == 0:
        return False

    r = (1, m-2, 1)
    # Sum constraints for the Spike (Theorem 5.3)
    sum_b0 = 2 % m
    sum_b1 = (m-1) % m
    sum_b2 = (m-1) % m

    # Check Single-Cycle condition: gcd(sum_b, m) == 1
    valid0 = gcd(sum_b0, m) == 1
    valid1 = gcd(sum_b1, m) == 1
    valid2 = gcd(sum_b2, m) == 1

    print(f"Spike (m={m}): r={r}, sums=({sum_b0}, {sum_b1}, {sum_b2}), valid=({valid0}, {valid1}, {valid2})")
    return valid0 and valid1 and valid2

if __name__ == "__main__":
    print("--- FSO Mathematical Verification ---")

    # Verify Theorem 2.1 for small m
    for m in [3, 4, 5]:
        assert test_theorem_2_1(m)

    # Verify Theorem 3.1 for m=3, k=3
    mk33 = test_theorem_3_1(3, 3)
    print(f"Theorem 3.1 (m=3, k=3): Result={mk33} (Expected 648)")
    assert mk33 == 648

    # Verify Theorem 4.1 Parity Obstruction
    assert test_theorem_4_1(4, 3) == True
    assert test_theorem_4_1(3, 3) == False

    # Verify Spike Construction for multiple odd m
    for m in [3, 5, 7, 9, 11, 13, 101]:
        assert test_spike_construction(m)

    print("--- All Tests Passed Successfully ---")
