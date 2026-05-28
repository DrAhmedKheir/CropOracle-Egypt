from __future__ import annotations
from abc import ABC, abstractmethod
from app.agents.state import CropOracleState


class BaseAgent(ABC):
    name: str = "base_agent"

    @abstractmethod
    def run(self, state: CropOracleState) -> CropOracleState:
        raise NotImplementedError
