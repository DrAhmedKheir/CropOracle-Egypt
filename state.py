from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from app.services.scenario_planner import FarmerScenario


class AgentTrace(BaseModel):
    agent: str
    action: str
    status: str = "ok"
    note: Optional[str] = None


class CropOracleState(BaseModel):
    farmer_message: str
    farmer_phone: Optional[str] = None
    scenario: Optional[FarmerScenario] = None
    weather_context: Dict[str, Any] = Field(default_factory=dict)
    soil_context: Dict[str, Any] = Field(default_factory=dict)
    simulation_results: List[Dict[str, Any]] = Field(default_factory=list)
    validation_warnings: List[str] = Field(default_factory=list)
    advisory_text: Optional[str] = None
    trace: List[AgentTrace] = Field(default_factory=list)

    def add_trace(self, agent: str, action: str, status: str = "ok", note: Optional[str] = None) -> None:
        self.trace.append(AgentTrace(agent=agent, action=action, status=status, note=note))
