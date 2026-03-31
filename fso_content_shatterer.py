import hashlib
import re

class ContentShatterer:
    """
    Law XII Component: The Atomic Shatterer
    Breaks down flat files into multi-dimensional topological atoms.
    """
    def __init__(self, m=256, k=4):
        self.m = m
        self.k = k

    def _get_coord(self, atom_data, target_fiber):
        """Map an atom's data to a Z_m^k coordinate on a specific fiber."""
        h = hashlib.sha256(atom_data.encode('utf-8') if isinstance(atom_data, str) else atom_data).digest()
        coords = []
        for i in range(self.k - 1):
            coords.append(h[i % len(h)] % self.m)

        # Closure Lemma (Law III)
        w = (target_fiber - sum(coords)) % self.m
        coords.append(w)
        return tuple(coords)

    def shatter(self, filename, content):
        """Shatters content based on file type."""
        atoms = []

        if filename.endswith(('.py', '.js', '.c', '.rs', '.go')):
            # Fiber 1: Code / Logic
            fiber = 1
            # Simple logical block splitting (e.g., by double newlines or common keywords)
            blocks = re.split(r'\n\s*\n', content.decode('utf-8', errors='ignore'))
            for b in blocks:
                if b.strip():
                    atoms.append({
                        "data": b.strip(),
                        "fiber": fiber,
                        "coord": self._get_coord(b.strip(), fiber),
                        "type": "logic_block"
                    })

        elif filename.endswith(('.json', '.csv', '.txt', '.pdf', '.md')):
            # Fiber 2: Knowledge / Data
            fiber = 2
            text = content.decode('utf-8', errors='ignore')
            # Split by sentences (simple version)
            sentences = re.split(r'(?<=[.!?])\s+', text)
            for s in sentences:
                if s.strip():
                    atoms.append({
                        "data": s.strip(),
                        "fiber": fiber,
                        "coord": self._get_coord(s.strip(), fiber),
                        "type": "knowledge_atom"
                    })
        else:
            # Fiber 3: Aesthetics / Raw Binary
            fiber = 3
            # Chunking binary into 64-byte atoms
            chunk_size = 64
            for i in range(0, len(content), chunk_size):
                chunk = content[i:i+chunk_size]
                atoms.append({
                    "data": chunk,
                    "fiber": fiber,
                    "coord": self._get_coord(chunk, fiber),
                    "type": "aesthetic_chunk"
                })

        return atoms

if __name__ == "__main__":
    shatterer = ContentShatterer()
    test_text = "TGI is the future of intelligence. It maps raw data into geometric tori. Determinism is the key."
    atoms = shatterer.shatter("test.txt", test_text.encode())
    print(f"Shattered test.txt into {len(atoms)} atoms.")
    for a in atoms:
        print(f"  Atom: '{a['data'][:30]}...' -> Coord: {a['coord']}")
