from __future__ import annotations
from app.agents.base import BaseAgent
from app.agents.state import CropOracleState
from app.services.scenario_planner import extract_scenario


class IntakeAgent(BaseAgent):
    name = "intake_agent"

    def run(self, state: CropOracleState) -> CropOracleState:
        state.scenario = extract_scenario(state.farmer_message, farmer_phone=state.farmer_phone)
        state.add_trace(self.name, "Parsed farmer message into structured scenario")
        return state
