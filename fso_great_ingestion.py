import time
from fso_orchestrator import SovereignOrchestrator

class GreatIngestor:
    """
    Project: ELECTRICITY (The Great Ingestion)
    Consumes the most valuable domains of human knowledge:
    Mathematics, Computer Science, Computer Vision, and Advanced System Specs.
    Enhanced with Kaggle Machine Intelligence.
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
            ],
            "Machine_Intelligence": [
                {"type": "kaggle_dataset", "slug": "abdullah1133/arc-prize-2024"},
                {"type": "kaggle_competition", "slug": "arc-prize-2024"}
            ]
        }

    def execute_global_consumption(self):
        print("\n" + "=" * 60)
        print(" [TGI] INITIATING THE GREAT INGESTION PHASE")
        print("=" * 60)

        start_time = time.time()
        total_domains = 0

        for category, sources in self.registry.items():
            print(f"\n>>> CATEGORY: {category.upper()}")
            for source in sources:
                if isinstance(source, str):
                    self.orchestrator.execute_mission(source, mission_name=f"Ingesting {category}: {source.split('/')[-1]}")
                elif isinstance(source, dict):
                    m_type = source['type'].split('_')[1] # 'dataset' or 'competition'
                    self.orchestrator.execute_kaggle_mission(source['slug'], mission_type=m_type, mission_name=f"Ingesting Kaggle {category}: {source['slug']}")
                total_domains += 1

        duration = time.time() - start_time
        print("\n" + "=" * 60)
        print(f" [DONE] THE GREAT INGESTION COMPLETE")
        print(f" Total Domains Shattered: {total_domains}")
        print(f" Global Convergence Time: {duration:.2f} seconds")
        print("=" * 60)

if __name__ == "__main__":
    # Mocking the network for the Great Ingestion Demo
    import io, zipfile, urllib.request, os, tempfile, kaggle

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

    class MockKaggleApiGreat:
        def dataset_download_files(self, slug, path, unzip=False):
            print(f"      [MOCK] Downloading dataset {slug} to {path}")
            with open(os.path.join(path, "mock_data.zip"), "wb") as f:
                f.write(create_mock_zip(slug.replace("/", "_")))
        def competition_download_files(self, name, path):
            print(f"      [MOCK] Downloading competition {name} to {path}")
            with open(os.path.join(path, "mock_comp.zip"), "wb") as f:
                f.write(create_mock_zip(name))

    kaggle.api = MockKaggleApiGreat()

    ingestor = GreatIngestor()
    ingestor.execute_global_consumption()

    urllib.request.urlopen = orig_urlopen
