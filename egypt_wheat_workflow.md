# Egypt Wheat Simulation Workflow

## 1. Define priority regions

Start with 3 contrasting Egyptian wheat regions:

- Nile Delta: Kafr El-Sheikh / Dakahlia / Sharkia
- Reclaimed sandy soils: Nubaria / West Delta
- Upper Egypt: Minya / Assiut / Sohag

## 2. Prepare APSIM template

Create one validated APSIM Next Gen wheat template with:

- Egyptian wheat cultivar parameters
- Soil profile
- Irrigation manager
- Nitrogen manager
- Sowing manager
- Weather file node
- Report node with grain yield, biomass, flowering, maturity, water stress, nitrogen stress

## 3. Scenario dimensions

Minimum useful farmer scenarios:

- Sowing date: 10 Nov, 20 Nov, 1 Dec, 15 Dec, 30 Dec
- Irrigation: low, farmer practice, high
- Nitrogen: 120, 180, 240 kg N/ha
- Climate: rainfall -20%, temperature +1/+2/+3 °C

## 4. Weather data

Use one of these options:

- Local station data from Egypt
- NASA POWER daily weather
- ERA5-Land converted to APSIM met format
- Existing DSSAT/APSIM weather files

## 5. Soil data

Use measured soil profiles where available. For scaling, prepare governorate-level representative profiles using SoilGrids/ISRIC and local calibration.

## 6. Validation

Validate simulated yield against field experiments or official governorate yield statistics before using advisory messages with real farmers.

## 7. Output message

The advisory should include:

- Best option
- Expected yield
- Comparison with worst/late option
- Yield advantage in kg/ha and total farm area
- Short explanation: heat stress, water stress, or nitrogen limitation
- Uncertainty warning
