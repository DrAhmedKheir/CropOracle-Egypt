from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional
import json
import re

class FarmerScenario(BaseModel):
    farmer_phone: Optional[str] = None
    language: str = 'en'
    crop: str = 'wheat'
    governorate: str = 'Kafr El-Sheikh'
    location_text: Optional[str] = None
    farm_area_ha: float = 1.0
    sowing_dates: List[str] = Field(default_factory=lambda: ['2026-11-15', '2026-12-01', '2026-12-15'])
    rainfall_change_pct: float = 0.0
    temperature_change_c: float = 0.0
    irrigation_levels: List[str] = Field(default_factory=lambda: ['farmer_practice'])
    nitrogen_levels_kg_ha: List[int] = Field(default_factory=lambda: [180])
    question: str = ''


def rule_based_extract(message: str, farmer_phone: Optional[str] = None) -> FarmerScenario:
    """Lightweight fallback parser when no LLM key is available."""
    msg = message.lower()
    scenario = FarmerScenario(question=message, farmer_phone=farmer_phone)

    govs = ['kafr el-sheikh', 'dakahlia', 'sharkia', 'beheira', 'nubaria', 'fayoum', 'minya', 'assiut', 'sohag', 'qena', 'luxor', 'aswan']
    for gov in govs:
        if gov in msg:
            scenario.governorate = gov.title()
            scenario.location_text = gov.title()
            break

    area_match = re.search(r'(\d+(?:\.\d+)?)\s*(ha|hectare|hectares|فدان|feddan)', msg)
    if area_match:
        value = float(area_match.group(1))
        unit = area_match.group(2)
        scenario.farm_area_ha = value * 0.42 if unit in ['فدان', 'feddan'] else value

    rain_match = re.search(r'rainfall\s*(drops|decrease|decreases|reduced|less)?\s*(by)?\s*(\d+)', msg)
    if rain_match:
        scenario.rainfall_change_pct = -abs(float(rain_match.group(3)))

    temp_match = re.search(r'(temperature|warming|heat).*?(\+?\d+(?:\.\d+)?)', msg)
    if temp_match:
        scenario.temperature_change_c = float(temp_match.group(2).replace('+', ''))

    # Default Egyptian wheat sowing windows.
    if 'early' in msg or 'november' in msg:
        scenario.sowing_dates = ['2026-11-10', '2026-11-20', '2026-12-01']
    elif 'late' in msg or 'december' in msg:
        scenario.sowing_dates = ['2026-12-01', '2026-12-15', '2026-12-30']

    return scenario


def extract_scenario(message: str, farmer_phone: Optional[str] = None, use_llm: bool = False) -> FarmerScenario:
    # Start with robust rule-based parsing. You can replace/extend with OpenAI or Claude.
    # Keep this deterministic for initial APSIM testing.
    return rule_based_extract(message, farmer_phone=farmer_phone)


def scenario_to_json(scenario: FarmerScenario) -> str:
    return json.dumps(scenario.model_dump(), indent=2, ensure_ascii=False)
