from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import pandas as pd

@dataclass
class WeatherRequest:
    latitude: float
    longitude: float
    start_year: int
    end_year: int
    rainfall_change_pct: float = 0.0
    temperature_change_c: float = 0.0


def apply_climate_scenario(weather: pd.DataFrame, rainfall_change_pct: float = 0.0, temperature_change_c: float = 0.0) -> pd.DataFrame:
    """Apply simple delta climate scenario to daily weather dataframe."""
    df = weather.copy()
    if 'rain' in df.columns:
        df['rain'] = df['rain'] * (1 + rainfall_change_pct / 100.0)
    for col in ['maxt', 'mint', 'tmax', 'tmin']:
        if col in df.columns:
            df[col] = df[col] + temperature_change_c
    return df


def load_local_weather(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() == '.csv':
        return pd.read_csv(path)
    raise ValueError('Only CSV weather loading is implemented in this starter project.')


def nasa_power_placeholder(latitude: float, longitude: float, start_year: int, end_year: int) -> pd.DataFrame:
    """Placeholder. Replace with NASA POWER API downloader and APSIM .met converter."""
    dates = pd.date_range(f'{start_year}-01-01', f'{end_year}-12-31', freq='D')
    return pd.DataFrame({
        'date': dates,
        'year': dates.year,
        'day': dates.dayofyear,
        'radn': 20.0,
        'maxt': 28.0,
        'mint': 15.0,
        'rain': 0.0,
        'vp': 1.2
    })


def get_weather_context(governorate: str) -> dict:
    """Return coordinates and weather source metadata for Egyptian wheat simulations.
    Replace coordinates or link to station/NASA POWER downloader for production.
    """
    coords = {
        'kafr el-sheikh': (31.11, 30.94),
        'dakahlia': (31.04, 31.38),
        'sharkia': (30.73, 31.72),
        'beheira': (30.85, 30.28),
        'nubaria': (30.66, 30.06),
        'fayoum': (29.31, 30.84),
        'minya': (28.10, 30.75),
        'assiut': (27.18, 31.19),
        'sohag': (26.56, 31.70),
        'qena': (26.16, 32.72),
        'luxor': (25.69, 32.64),
        'aswan': (24.09, 32.90),
    }
    key = governorate.lower()
    lat, lon = coords.get(key, coords['kafr el-sheikh'])
    return {
        'governorate': governorate,
        'latitude': lat,
        'longitude': lon,
        'source': 'NASA POWER or local station placeholder',
        'note': 'Production workflow should generate APSIM .met from local station/NASA POWER/ERA5.'
    }
