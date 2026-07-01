import json
from orchestrator.fsm_controller import IncidentFSM

with open("data/cpu_spike.log") as f:
    logs = f.read()
# Load logs
with open("data/cpu_spike.log") as f:
    logs = f.read()

# Load metrics
with open("data/cpu_usage.json") as f:
    metrics = json.load(f)


fsm = IncidentFSM()
fsm.handle_incident(logs, metrics={})
