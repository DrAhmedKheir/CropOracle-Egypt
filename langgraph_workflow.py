from __future__ import annotations
"""
Optional LangGraph workflow for CropOracle Egypt.
Install langgraph and langchain only when you want graph-based orchestration:
    pip install langgraph langchain langchain-openai

This file mirrors the deterministic coordinator but exposes each expert as a node.
"""
from typing import Dict, Any, Optional
from app.agents.state import CropOracleState
from app.agents.intake_agent import IntakeAgent
from app.agents.weather_agent import WeatherAgent
from app.agents.soil_agent import SoilAgent
from app.agents.simulation_agent import SimulationAgent
from app.agents.validation_agent import ValidationAgent
from app.agents.advisory_agent import AdvisoryAgent


def build_langgraph_app():
    try:
        from langgraph.graph import StateGraph, END
    except Exception as exc:
        raise ImportError("LangGraph is not installed. Run: pip install langgraph") from exc

    def wrap(agent):
        def _node(data: Dict[str, Any]) -> Dict[str, Any]:
            state = CropOracleState(**data)
            state = agent.run(state)
            return state.model_dump()
        return _node

    graph = StateGraph(dict)
    graph.add_node("intake", wrap(IntakeAgent()))
    graph.add_node("weather", wrap(WeatherAgent()))
    graph.add_node("soil", wrap(SoilAgent()))
    graph.add_node("simulation", wrap(SimulationAgent()))
    graph.add_node("validation", wrap(ValidationAgent()))
    graph.add_node("advisory", wrap(AdvisoryAgent()))

    graph.set_entry_point("intake")
    graph.add_edge("intake", "weather")
    graph.add_edge("weather", "soil")
    graph.add_edge("soil", "simulation")
    graph.add_edge("simulation", "validation")
    graph.add_edge("validation", "advisory")
    graph.add_edge("advisory", END)
    return graph.compile()


def run_langgraph_workflow(message: str, farmer_phone: Optional[str] = None) -> Dict[str, Any]:
    app = build_langgraph_app()
    initial_state = CropOracleState(farmer_message=message, farmer_phone=farmer_phone)
    return app.invoke(initial_state.model_dump())
