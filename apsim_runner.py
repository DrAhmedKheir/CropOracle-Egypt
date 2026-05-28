from __future__ import annotations
from pathlib import Path
import json
import shutil
import subprocess
import uuid
from typing import Dict, Any, List
import pandas as pd
from app.config import settings
from app.services.scenario_planner import FarmerScenario


def _safe_name(text: str) -> str:
    return ''.join(c if c.isalnum() else '_' for c in text)[:60]


def prepare_apsim_file(scenario: FarmerScenario, sowing_date: str, nitrogen_kg_ha: int, irrigation_level: str) -> Path:
    run_id = f"{_safe_name(scenario.governorate)}_{sowing_date}_{nitrogen_kg_ha}_{irrigation_level}_{uuid.uuid4().hex[:8]}"
    run_dir = settings.OUTPUT_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    target = run_dir / 'simulation.apsimx'

    if settings.APSIM_TEMPLATE.exists():
        shutil.copy(settings.APSIM_TEMPLATE, target)
    else:
        # Minimal placeholder file; replace with real calibrated APSIM wheat template.
        target.write_text(json.dumps({
            'Name': 'Egypt_Wheat_Template_Placeholder',
            'Note': 'Replace with a real APSIM Next Gen .apsimx file.',
            'Scenario': scenario.model_dump(),
            'SowingDate': sowing_date,
            'NitrogenKgHa': nitrogen_kg_ha,
            'IrrigationLevel': irrigation_level
        }, indent=2), encoding='utf-8')

    metadata = run_dir / 'scenario_metadata.json'
    metadata.write_text(json.dumps({
        'scenario': scenario.model_dump(),
        'sowing_date': sowing_date,
        'nitrogen_kg_ha': nitrogen_kg_ha,
        'irrigation_level': irrigation_level
    }, indent=2, ensure_ascii=False), encoding='utf-8')
    return target


def run_apsim(apsim_file: Path) -> Dict[str, Any]:
    """Run APSIM Next Gen. If APSIM_EXE is unavailable, returns deterministic demo output."""
    if not settings.APSIM_EXE or not Path(settings.APSIM_EXE).exists():
        return {'status': 'demo', 'message': 'APSIM executable not found; demo output generated.', 'apsim_file': str(apsim_file)}

    cmd = [settings.APSIM_EXE, str(apsim_file)]
    result = subprocess.run(cmd, cwd=apsim_file.parent, capture_output=True, text=True, check=False)
    return {
        'status': 'success' if result.returncode == 0 else 'error',
        'returncode': result.returncode,
        'stdout': result.stdout[-4000:],
        'stderr': result.stderr[-4000:],
        'apsim_file': str(apsim_file)
    }


def run_scenario_set(scenario: FarmerScenario) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    for sowing_date in scenario.sowing_dates:
        for n in scenario.nitrogen_levels_kg_ha:
            for irrigation in scenario.irrigation_levels:
                apsim_file = prepare_apsim_file(scenario, sowing_date, n, irrigation)
                status = run_apsim(apsim_file)

                # In production: parse APSIM SQLite result. For demo, use simple agronomic logic.
                base_yield = 6.5
                day_offset = {'2026-11-10': 0.2, '2026-11-15': 0.1, '2026-11-20': 0.0, '2026-12-01': -0.3, '2026-12-15': -0.8, '2026-12-30': -1.3}.get(sowing_date, -0.2)
                climate_penalty = abs(scenario.rainfall_change_pct) * 0.015 + scenario.temperature_change_c * 0.25
                n_effect = min(max((n - 120) / 300, -0.4), 0.5)
                irrigation_effect = 0.0 if irrigation == 'farmer_practice' else (0.4 if irrigation == 'high' else -0.4)
                yield_t_ha = max(1.0, base_yield + day_offset + n_effect + irrigation_effect - climate_penalty)

                rows.append({
                    'sowing_date': sowing_date,
                    'nitrogen_kg_ha': n,
                    'irrigation_level': irrigation,
                    'yield_t_ha': round(yield_t_ha, 2),
                    'yield_kg_ha': round(yield_t_ha * 1000),
                    'run_status': status['status'],
                    'apsim_file': str(apsim_file)
                })
    df = pd.DataFrame(rows).sort_values('yield_t_ha', ascending=False)
    out_csv = settings.OUTPUT_DIR / f"results_{uuid.uuid4().hex[:8]}.csv"
    df.to_csv(out_csv, index=False)
    return df
