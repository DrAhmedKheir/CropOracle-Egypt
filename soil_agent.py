from __future__ import annotations
import json
from pathlib import Path
from app.agents.base import BaseAgent
from app.agents.state import CropOracleState


class SoilAgent(BaseAgent):
    name = "soil_agent"

    def __init__(self, soil_file: str = "apsim_templates/soil_profiles_egypt.json"):
        self.soil_file = Path(soil_file)

    def run(self, state: CropOracleState) -> CropOracleState:
        if state.scenario is None:
            raise ValueError("Scenario must be parsed before soil selection.")
        soil_data = {}
        if self.soil_file.exists():
            soil_data = json.loads(self.soil_file.read_text(encoding="utf-8"))
        gov_key = state.scenario.governorate.lower().replace(" ", "_").replace("-", "_")
        selected = soil_data.get(gov_key) or soil_data.get("default", {})
        state.soil_context = {"governorate_key": gov_key, "soil_profile": selected, "source": str(self.soil_file)}
        state.add_trace(self.name, "Selected Egypt wheat soil profile", note=gov_key)
        return state
