from __future__ import annotations
from app.agents.base import BaseAgent
from app.agents.state import CropOracleState
from app.services.weather_engine import get_weather_context


class WeatherAgent(BaseAgent):
    name = "weather_agent"

    def run(self, state: CropOracleState) -> CropOracleState:
        if state.scenario is None:
            raise ValueError("Scenario must be parsed before weather preparation.")
        state.weather_context = get_weather_context(state.scenario.governorate)
        state.add_trace(self.name, "Prepared weather context for APSIM scenario", note=str(state.weather_context.get("source", "demo")))
        return state
