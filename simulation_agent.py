from __future__ import annotations
from app.agents.base import BaseAgent
from app.agents.state import CropOracleState
from app.services.apsim_runner import run_scenario_set


class SimulationAgent(BaseAgent):
    name = "simulation_agent"

    def run(self, state: CropOracleState) -> CropOracleState:
        if state.scenario is None:
            raise ValueError("Scenario must be available before APSIM simulation.")
        df = run_scenario_set(state.scenario)
        state.simulation_results = df.to_dict(orient="records")
        state.add_trace(self.name, f"Ran {len(state.simulation_results)} APSIM scenario(s)")
        return state
