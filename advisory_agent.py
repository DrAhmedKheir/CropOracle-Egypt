from __future__ import annotations
import pandas as pd
from app.agents.base import BaseAgent
from app.agents.state import CropOracleState
from app.services.advisory_generator import generate_advisory


class AdvisoryAgent(BaseAgent):
    name = "advisory_agent"

    def run(self, state: CropOracleState) -> CropOracleState:
        if state.scenario is None:
            raise ValueError("Scenario must be available before advisory generation.")
        df = pd.DataFrame(state.simulation_results)
        advisory = generate_advisory(state.scenario, df)
        if state.validation_warnings:
            advisory += "\n\nNote: " + " ".join(state.validation_warnings)
        state.advisory_text = advisory
        state.add_trace(self.name, "Generated farmer-ready WhatsApp advisory")
        return state
