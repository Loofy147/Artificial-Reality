import time
from fso_orchestrator import SovereignOrchestrator

class GreatIngestor:
    """
    Project: ELECTRICITY (The Great Ingestion)
    Consumes the most valuable domains of human knowledge:
    Mathematics, Computer Science, Computer Vision, and Advanced System Specs.
    """
    def __init__(self, m=256, k=4):
        self.orchestrator = SovereignOrchestrator(m, k)
        self.registry = {
            "Mathematics": [
                "https://github.com/leanprover/lean4",
                "https://github.com/sympy/sympy"
            ],
            "Computer_Science": [
                "https://github.com/torvalds/linux",
                "https://github.com/llvm/llvm-project"
            ],
            "Computer_Vision": [
                "https://github.com/opencv/opencv",
                "https://github.com/pytorch/pytorch"
            ],
            "Topological_OS_Specs": [
                "https://github.com/Sovereign/ProjectElectricity/Architecture",
                "https://github.com/Sovereign/TGI-Specifications"
            ]
        }

    def execute_global_consumption(self):
        print("\n" + "=" * 60)
        print(" [TGI] INITIATING THE GREAT INGESTION PHASE")
        print("=" * 60)

        start_time = time.time()
        total_domains = 0

        for category, urls in self.registry.items():
            print(f"\n>>> CATEGORY: {category.upper()}")
            for url in urls:
                self.orchestrator.execute_mission(url, mission_name=f"Ingesting {category}: {url.split('/')[-1]}")
                total_domains += 1

        duration = time.time() - start_time
        print("\n" + "=" * 60)
        print(f" [DONE] THE GREAT INGESTION COMPLETE")
        print(f" Total Domains Shattered: {total_domains}")
        print(f" Global Convergence Time: {duration:.2f} seconds")
        print("=" * 60)

if __name__ == "__main__":
    # Mocking the network for the Great Ingestion Demo
    import io, zipfile, urllib.request

    def create_mock_zip(name):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            zf.writestr(f"{name}_logic.py", "def run(): pass")
            zf.writestr(f"{name}_data.txt", f"Valuable {name} knowledge atom.")
        return buf.getvalue()

    orig_urlopen = urllib.request.urlopen
    class MockRes:
        def __init__(self, name): self.c = create_mock_zip(name)
        def read(self): return self.c
        def __enter__(self): return self
        def __exit__(self, *args, **kwargs): pass

    # Simple router for the mock urlopen
    def mock_urlopen(url, *args, **kwargs):
        name = url.split("/")[-1]
        return MockRes(name)

    urllib.request.urlopen = mock_urlopen

    ingestor = GreatIngestor()
    ingestor.execute_global_consumption()

    urllib.request.urlopen = orig_urlopen
