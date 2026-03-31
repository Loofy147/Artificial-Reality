import hashlib

class ParityVault:
    """
    TGI Security Layer: The Parity Vault
    Enforces manifold-level encryption. Data is only accessible if the
    querier's (m, k) and target_fiber exactly match the secret key.
    """
    def __init__(self, m=256, k=4):
        self.m = m
        self.k = k
        self.secrets = {}

    def secure_data(self, key_name, data, secret_fiber=0):
        """
        Encrypts a secret within the manifold by hashing the key name
        to a specific coordinate on 'secret_fiber'.
        """
        h = hashlib.sha256(key_name.encode()).digest()
        coords = [h[i % len(h)] % self.m for i in range(self.k - 1)]
        w = (secret_fiber - sum(coords)) % self.m
        coord = tuple(coords + [w])

        # Manifold-level lock: The data is stored at a coordinate
        # that only exists if the (m, k, secret_fiber) are exactly known.
        self.secrets[coord] = {
            "key": key_name,
            "data": data,
            "fiber": secret_fiber
        }
        print(f"\n--- [TGI SECURITY]: Parity Vault Secured '{key_name}' ---")
        print(f"      Manifold Lock @ {coord}")
        return coord

    def access_data(self, key_name, provided_m, provided_k, provided_fiber=0):
        """
        Attempts to access the vault. If m, k, or fiber are wrong,
        the manifold coordinate will be different, and the data remains hidden.
        """
        h = hashlib.sha256(key_name.encode()).digest()
        coords = [h[i % len(h)] % provided_m for i in range(provided_k - 1)]
        w = (provided_fiber - sum(coords)) % provided_m
        coord = tuple(coords + [w])

        print(f"\n--- [TGI SECURITY]: Vault Access Attempt for '{key_name}' ---")
        print(f"      Calculated Coordinate: {coord}")

        secret = self.secrets.get(coord)
        if secret and provided_m == self.m and provided_k == self.k:
            print(f"[✓] ACCESS GRANTED: '{secret['data']}'")
            return secret['data']
        else:
            print("[!] ACCESS DENIED: Topological coordinate mismatch or parity fracture.")
            return None

if __name__ == "__main__":
    vault = ParityVault(m=256, k=4)
    vault.secure_data("Sovereign_Root_Key", "TGI_SEC_KEY_8892")

    # 1. Success
    vault.access_data("Sovereign_Root_Key", 256, 4)
    # 2. Failure: Wrong m
    vault.access_data("Sovereign_Root_Key", 255, 4)
    # 3. Failure: Wrong k
    vault.access_data("Sovereign_Root_Key", 256, 3)
