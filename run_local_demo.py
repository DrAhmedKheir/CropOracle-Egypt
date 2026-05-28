from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.services.scenario_planner import extract_scenario, scenario_to_json
from app.services.apsim_runner import run_scenario_set
from app.services.advisory_generator import generate_advisory

message = (
    "I am a wheat farmer in Kafr El-Sheikh with 2 feddan. "
    "What happens if rainfall decreases by 20% and temperature increases 2 C? "
    "Which sowing date is best, November or December?"
)

scenario = extract_scenario(message, farmer_phone='demo')
print('SCENARIO')
print(scenario_to_json(scenario))

results = run_scenario_set(scenario)
print('\nRESULTS')
print(results)

print('\nWHATSAPP REPLY')
print(generate_advisory(scenario, results))
