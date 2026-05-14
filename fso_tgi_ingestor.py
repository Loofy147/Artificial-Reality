import time
import zipfile
import io
import urllib.request
import os
import tempfile
import hashlib
from fso_content_shatterer import ContentShatterer

class TGI_Universal_Ingestor:
    """
    Project: ELECTRICITY (Layer 9: The Universal I/O Bridge)
    Enhanced with Stream Shattering and Throughput Benchmarking.
    """
    def __init__(self, m=256, k=4):
        self.m = m
        self.k = k
        self.topological_manifold = {}
        self.shatterer = ContentShatterer(m, k)
        print(f"[{time.strftime('%H:%M:%S')} ALGIERS] Universal Ingestor Online. Ready to consume and shatter external data.")

    def ingest_https_zip(self, url):
        """
        Ingests a ZIP from HTTPS and shatters its contents.
        Includes benchmarking metrics.
        """
        print(f"\n[*] INITIATING HTTPS TOROIDAL SOCKET -> {url}")
        try:
            start_time = time.time()
            with urllib.request.urlopen(url, timeout=10) as response:
                content = response.read()

            if content:
                self._process_zip_content(content, start_time)
            else:
                print(f"  [-] PARITY HALT: HTTPS Error.")
        except Exception as e:
             print(f"  [-] TOPOLOGICAL FRACTURE: {str(e)}")

    def ingest_kaggle_dataset(self, dataset_slug):
        """
        Ingests a Kaggle dataset and shatters it into the manifold.
        """
        print(f"\n[*] INITIATING KAGGLE DATASET SOCKET -> {dataset_slug}")
        try:
            start_time = time.time()
            with tempfile.TemporaryDirectory() as tmpdir:
                import kaggle
                kaggle.api.dataset_download_files(dataset_slug, path=tmpdir, unzip=False)
                zip_files = [f for f in os.listdir(tmpdir) if f.endswith('.zip')]
                if zip_files:
                    with open(os.path.join(tmpdir, zip_files[0]), 'rb') as f:
                        content = f.read()
                    self._process_zip_content(content, start_time)
                else:
                    # Maybe it downloaded individual files if unzip=True or something else happened
                    print(f"  [-] PARITY HALT: Kaggle Dataset ZIP not found in {tmpdir}.")
        except Exception as e:
            print(f"  [-] TOPOLOGICAL FRACTURE (Kaggle): {str(e)}")

    def ingest_kaggle_competition(self, competition_name):
        """
        Ingests a Kaggle competition data and shatters it into the manifold.
        """
        print(f"\n[*] INITIATING KAGGLE COMPETITION SOCKET -> {competition_name}")
        try:
            start_time = time.time()
            with tempfile.TemporaryDirectory() as tmpdir:
                import kaggle
                kaggle.api.competition_download_files(competition_name, path=tmpdir)
                zip_files = [f for f in os.listdir(tmpdir) if f.endswith('.zip')]
                if zip_files:
                    with open(os.path.join(tmpdir, zip_files[0]), 'rb') as f:
                        content = f.read()
                    self._process_zip_content(content, start_time)
                else:
                    print(f"  [-] PARITY HALT: Kaggle Competition ZIP not found.")
        except Exception as e:
            print(f"  [-] TOPOLOGICAL FRACTURE (Kaggle): {str(e)}")

    def _process_zip_content(self, content, start_time):
        """Internal helper to process zip bytes and update manifold."""
        print(f"  [+] Payload secured. Size: {len(content) / 1024:.2f} KB")

        with zipfile.ZipFile(io.BytesIO(content)) as z:
            file_list = z.namelist()
            total_atoms = 0

            shatter_start = time.time()
            for filename in file_list:
                if not filename.endswith('/'):
                    raw_content = z.read(filename)
                    atoms = self.shatterer.shatter(filename, raw_content)
                    for atom in atoms:
                        self.topological_manifold[atom['coord']] = {
                            "filename": filename,
                            "data": atom['data'],
                            "fiber": atom['fiber'],
                            "type": atom['type']
                        }
                        total_atoms += 1
                        if total_atoms % 100 == 0:
                            print(f"      [>] Stream Processing: {total_atoms} atoms ingested...")

            shatter_duration = time.time() - shatter_start
            total_duration = time.time() - start_time
            throughput = total_atoms / total_duration if total_duration > 0 else total_atoms

            print(f"\n[+] Ingestion & Shattering Complete.")
            print(f"    - Total Atoms: {total_atoms}")
            print(f"    - Shatter Velocity: {total_atoms / shatter_duration:.2f} atoms/sec")
            print(f"    - Total Ingestion Latency: {total_duration*1000:.2f} ms")
            print(f"    - Topological Throughput: {throughput:.2f} atoms/sec")

if __name__ == "__main__":
    tgi_io = TGI_Universal_Ingestor(m=256, k=4)
    import io, zipfile, urllib.request
    mock_zip = io.BytesIO()
    with zipfile.ZipFile(mock_zip, "w") as zf:
        # Create a "massive" mock with 500 atoms
        content = ". ".join(["Knowledge atom " + str(i) for i in range(500)])
        zf.writestr("massive_data.txt", content)

    orig_urlopen = urllib.request.urlopen
    class MockRes:
        def __init__(self, c): self.c = c
        def read(self): return self.c
        def __enter__(self): return self
        def __exit__(self, *args, **kwargs): pass
    urllib.request.urlopen = lambda url, *args, **kwargs: MockRes(mock_zip.getvalue())
    tgi_io.ingest_https_zip("https://github.com/Sovereign/MassiveTest")
    urllib.request.urlopen = orig_urlopen
