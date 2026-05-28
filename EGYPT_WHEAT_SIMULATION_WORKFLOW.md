# Egypt Wheat Simulation Workflow

## 1. Purpose

The Egypt wheat workflow converts farmer questions into APSIM Next Gen simulations for wheat production under local climate, soil, and management conditions.

## 2. Target regions

Initial recommended regions:

| Region | Example governorates | Main purpose |
|---|---|---|
| Nile Delta | Kafr El-Sheikh, Dakahlia, Beheira, Sharkia | High-productivity irrigated wheat |
| Middle Egypt | Beni Suef, Minya, Fayoum | Heat-risk and irrigation scheduling |
| Upper Egypt | Assiut, Sohag, Qena, Aswan | Late-season heat stress and water management |
| New Lands | Nubaria, Toshka, East Oweinat | Sandy soils and irrigation/fertilizer optimization |

## 3. Required input data

### Weather

Daily data should include:

- Maximum temperature
- Minimum temperature
- Solar radiation
- Rainfall
- Vapor pressure or relative humidity
- Wind speed, optional depending on APSIM configuration

Potential sources:

- Local meteorological stations
- NASA POWER
- ERA5 / ERA5-Land
- Existing APSIM/DSSAT weather archives

### Soil

Soil profile should include:

- Soil texture by layer
- Bulk density
- LL15
- DUL
- SAT
- Organic carbon
- pH
- Initial water
- Initial nitrogen

Potential sources:

- Field measurements
- SoilGrids
- Egyptian soil maps
- Published soil profiles

### Management

Minimum management inputs:

- Sowing date
- Wheat cultivar
- Plant population
- Row spacing
- Irrigation schedule
- Nitrogen fertilizer amount and timing
- Initial soil water

## 4. Example scenario matrix

For a farmer asking about sowing date under climate stress:

| Scenario | Sowing date | Climate setting |
|---|---|---|
| S1 | 15 November | Baseline |
| S2 | 1 December | Baseline |
| S3 | 15 December | Baseline |
| S4 | 15 November | Rainfall -20%, temperature +2°C |
| S5 | 1 December | Rainfall -20%, temperature +2°C |
| S6 | 15 December | Rainfall -20%, temperature +2°C |

## 5. Output interpretation

The system ranks options based on:

1. Highest simulated grain yield.
2. Lowest yield loss under climate stress.
3. Lower heat/water stress during flowering and grain filling.
4. Practical farmer feasibility.

## 6. Advisory rule example

If two sowing dates have similar yield, the system should prefer the date with:

- Lower heat stress risk
- More stable yield across years
- Better water productivity
- Lower fertilizer loss risk

## 7. Validation requirement

Before real deployment, APSIM outputs should be validated against Egyptian wheat field data from ARC, published experiments, or regional yield statistics.
