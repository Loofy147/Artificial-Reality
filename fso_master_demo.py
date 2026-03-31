import time
from fso_orchestrator import SovereignOrchestrator
from fso_intelligence_synthesis import IntelligenceSynthesizer
from fso_great_ingestion import GreatIngestor

def run_master_convergence():
    print("\n" + "="*80)
    print(" [TGI MASTER CONVERGENCE]: THE SOVEREIGN OS IS LIVE")
    print("="*80)

    m, k = 256, 4
    orchestrator = SovereignOrchestrator(m, k)

    # 1. THE GREAT INGESTION
    print("\n[PHASE 1]: THE GREAT INGESTION (Domain Acquisition)")
    # We use a simplified mock registry for the demo
    import io, zipfile, urllib.request
    def mock_urlopen(url, *args, **kwargs):
        buf = io.BytesIO()
        name = url.split("/")[-1]
        with zipfile.ZipFile(buf, "w") as zf:
            zf.writestr(f"{name}_logic.py", "def run(): pass")
            zf.writestr(f"{name}_data.txt", f"Valuable {name} knowledge atom.")
        class MockRes:
            def __init__(self, c): self.c = c
            def read(self): return self.c
            def __enter__(self): return self
            def __exit__(self, *args, **kwargs): pass
        return MockRes(buf.getvalue())

    orig_urlopen = urllib.request.urlopen
    urllib.request.urlopen = mock_urlopen

    domains = ["Mathematics", "Computer_Science", "Computer_Vision"]
    for d in domains:
        orchestrator.execute_mission(f"https://github.com/Sovereign/{d}", mission_name=f"Ingesting {d}")

    # 2. INTELLIGENCE SYNTHESIS
    print("\n[PHASE 2]: CROSS-DOMAIN SYNTHESIS (Insight Generation)")
    synthesizer = IntelligenceSynthesizer(m, k)
    synthesizer.run_synthesis_demo()

    # 3. AUTONOMOUS EVOLUTION
    print("\n[PHASE 3]: AUTONOMOUS EVOLUTION (Codex Expansion)")
    orchestrator.execute_evolution_mission("https://github.com/Sovereign/FinalEvolution", mission_name="Final OS Evolution")

    urllib.request.urlopen = orig_urlopen

    print("\n" + "="*80)
    print(" [DONE] CONVERGENCE COMPLETE. THE SOVEREIGN MIND IS INVARIANT.")
    print("="*80)

if __name__ == "__main__":
    run_master_convergence()
