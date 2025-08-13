PYTHON=python3

.PHONY: dev triage

dev:
	$(PYTHON) -m pip install -r requirements.txt

triage:
	$(PYTHON) -m packages.orchestrator.pipelines
