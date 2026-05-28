from __future__ import annotations
from pathlib import Path
import sqlite3
import pandas as pd


def parse_apsim_sqlite(db_path: str | Path, table_name: str = 'Report') -> pd.DataFrame:
    db_path = Path(db_path)
    if not db_path.exists():
        raise FileNotFoundError(f'APSIM output database not found: {db_path}')
    with sqlite3.connect(db_path) as con:
        return pd.read_sql_query(f'SELECT * FROM {table_name}', con)


def extract_final_yield(report: pd.DataFrame) -> float:
    """Try to extract final wheat yield in t/ha from common APSIM report columns."""
    possible = ['Yield', 'yield', 'Wheat.Grain.Wt', 'GrainWt']
    for col in possible:
        if col in report.columns:
            value = float(report[col].dropna().iloc[-1])
            # APSIM often reports kg/ha or g/m2 depending on report. Adjust after template validation.
            return value
    raise ValueError('No recognizable yield column found in APSIM report.')
