from __future__ import annotations
from typing import List, Dict, Any, Optional
from app.agents.state import CropOracleState
from app.agents.intake_agent import IntakeAgent
from app.agents.weather_agent import WeatherAgent
from app.agents.soil_agent import SoilAgent
from app.agents.simulation_agent import SimulationAgent
from app.agents.validation_agent import ValidationAgent
from app.agents.advisory_agent import AdvisoryAgent


class CropOracleMultiAgentCoordinator:
    """
    Deterministic multi-agent coordinator.
    It works without paid LLM APIs and can later be replaced by LangGraph nodes.
    """

    def __init__(self):
        self.agents = [
            IntakeAgent(),
            WeatherAgent(),
            SoilAgent(),
            SimulationAgent(),
            ValidationAgent(),
            AdvisoryAgent(),
        ]

    def run(self, farmer_message: str, farmer_phone: Optional[str] = None) -> CropOracleState:
        state = CropOracleState(farmer_message=farmer_message, farmer_phone=farmer_phone)
        for agent in self.agents:
            state = agent.run(state)
        return state


def run_multi_agent_workflow(message: str, farmer_phone: Optional[str] = None) -> Dict[str, Any]:
    state = CropOracleMultiAgentCoordinator().run(message, farmer_phone=farmer_phone)
    return state.model_dump()
