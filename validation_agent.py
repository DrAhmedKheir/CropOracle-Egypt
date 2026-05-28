from __future__ import annotations
from app.agents.base import BaseAgent
from app.agents.state import CropOracleState


class ValidationAgent(BaseAgent):
    name = "validation_agent"

    def run(self, state: CropOracleState) -> CropOracleState:
        warnings = []
        if state.scenario is None:
            warnings.append("No scenario was parsed.")
        else:
            if state.scenario.crop.lower() != "wheat":
                warnings.append("Current calibrated workflow is designed for wheat only.")
            if state.scenario.temperature_change_c > 5:
                warnings.append("Temperature increase is high; advisory should be treated as exploratory.")
            if abs(state.scenario.rainfall_change_pct) > 60:
                warnings.append("Rainfall scenario is outside the normal advisory range.")
        if not state.simulation_results:
            warnings.append("No simulation results were generated.")
        state.validation_warnings = warnings
        state.add_trace(self.name, "Checked scenario limits and simulation outputs", note="; ".join(warnings) if warnings else "No major warnings")
        return state
