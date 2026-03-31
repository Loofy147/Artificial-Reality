import time
import zipfile
import io
import urllib.request
import hashlib
from fso_content_shatterer import ContentShatterer

class TGI_Universal_Ingestor:
    """
    Project: ELECTRICITY (Layer 9: The Universal I/O Bridge)
    Allows the Sovereign OS to consume the old internet.
    Fetches HTTPS, decompresses ZIPs, and shatters files into pure Z_m^k topology.
    """
    def __init__(self, m=256, k=4):
        self.m = m
        self.k = k
        self.topological_manifold = {}
        self.shatterer = ContentShatterer(m, k)
        print(f"[{time.strftime('%H:%M:%S')} ALGIERS] Universal Ingestor Online. Ready to consume and shatter external data.")

    def ingest_https_zip(self, url):
        """
        1. Opens an HTTPS socket to the outside world.
        2. Streams the ZIP binary into RAM.
        3. Shatters and distributes the files into the geometric Torus.
        """
        print(f"\n[*] INITIATING HTTPS TOROIDAL SOCKET -> {url}")
        try:
            start_time = time.time()
            with urllib.request.urlopen(url, timeout=10) as response:
                content = response.read()

            if content:
                print(f"  [+] HTTPS payload secured. Size: {len(content) / 1024:.2f} KB")
                print("  [*] Engaging Mathematical Unfolding & Atomic Shattering...")

                with zipfile.ZipFile(io.BytesIO(content)) as z:
                    file_list = z.namelist()
                    total_atoms = 0

                    for filename in file_list:
                        if not filename.endswith('/'):
                            raw_content = z.read(filename)

                            # Shatter the file into atoms (Sentences, Logic Blocks, Binary Chunks)
                            atoms = self.shatterer.shatter(filename, raw_content)

                            for atom in atoms:
                                coord = atom['coord']
                                self.topological_manifold[coord] = {
                                    "filename": filename,
                                    "data": atom['data'],
                                    "fiber": atom['fiber'],
                                    "type": atom['type']
                                }
                                total_atoms += 1
                                # Limit the printing of atoms for the demo log
                                if total_atoms <= 10 or (total_atoms % 50 == 0):
                                    print(f"      [+] ATOM SECURED: '{filename}' -> Fiber {atom['fiber']} @ {coord}")

                latency = (time.time() - start_time) * 1000
                print(f"\n[+] Ingestion & Shattering Complete in {latency:.2f} ms.")
                print(f"[+] Total Topological Atoms Populated: {total_atoms}")
            else:
                print(f"  [-] PARITY HALT: HTTPS Error. Target node unreachable.")
        except Exception as e:
             print(f"  [-] TOPOLOGICAL FRACTURE: Network connection failed. {str(e)}")

if __name__ == "__main__":
    # =============================================================================
    # EXECUTING THE UNIVERSAL INGESTOR (MOCK DEMO)
    # =============================================================================
    print("=========================================================")
    print(" PROJECT ELECTRICITY: OMNIVOROUS DATA CONSUMPTION")
    print("=========================================================\n")

    tgi_io = TGI_Universal_Ingestor(m=256, k=4)

    mock_zip_buffer = io.BytesIO()
    with zipfile.ZipFile(mock_zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("core_logic.py", "def execute():\n\n    print('Running on TGI')")
        zf.writestr("knowledge.txt", "TGI consumes the world. It is a geometric mind. Sovereignty is reached through topology.")
        zf.writestr("readme.md", "# Project ELECTRICITY\nThe Sovereign OS.")

    original_urlopen = urllib.request.urlopen
    class MockResponse:
        def __init__(self, content): self.content = content
        def read(self): return self.content
        def __enter__(self): return self
        def __exit__(self, *args): pass

    urllib.request.urlopen = lambda url, timeout=10: MockResponse(mock_zip_buffer.getvalue())

    tgi_io.ingest_https_zip("https://github.com/Sovereign/ProjectElectricity/archive/main.zip")
    urllib.request.urlopen = original_urlopen
