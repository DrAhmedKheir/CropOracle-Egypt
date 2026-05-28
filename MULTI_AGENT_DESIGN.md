# Multi-Agent Design

## 1. Why multi-agent AI?

A farmer question may require several specialized tasks: understanding local language, identifying location, retrieving weather, choosing soil data, creating APSIM files, running simulations, checking results, and writing a useful answer. A multi-agent architecture separates these tasks into clear, testable components.

## 2. Agent roles

### Intake Agent

Extracts structured information:

- Location
- Crop
- Question type
- Sowing dates
- Fertilizer levels
- Irrigation levels
- Climate scenario
- Preferred language

### Weather Agent

Prepares weather data:

- Retrieves historical weather
- Applies climate perturbations
- Generates APSIM `.met` files
- Checks missing values

### Soil Agent

Prepares soil inputs:

- Selects soil profile based on location
- Checks compatibility with APSIM
- Estimates missing soil parameters where required

### APSIM Simulation Agent

Runs model workflow:

- Creates scenario files
- Runs APSIM Next Gen
- Saves outputs
- Tracks simulation status

### Validation Agent

Checks quality:

- Detects failed APSIM runs
- Checks unrealistic yield values
- Flags missing outputs
- Compares scenarios consistently

### Advisory Agent

Generates farmer-facing message:

- Recommends best option
- Explains reason simply
- Includes expected yield and risk
- Avoids overconfident claims

### Coordinator Agent

Controls the entire workflow:

- Maintains state
- Routes between agents
- Handles errors
- Stores context

## 3. Suggested state object

```python
state = {
    "farmer_message": "...",
    "language": "en/ar",
    "location": "Kafr El-Sheikh",
    "crop": "wheat",
    "scenarios": [],
    "weather_files": [],
    "soil_profile": {},
    "apsim_runs": [],
    "results": [],
    "validation_flags": [],
    "advisory_message": "..."
}
```

## 4. LangGraph extension

The workflow can be represented as a graph:

```text
Intake → Weather → Soil → Simulation → Validation → Advisory
                    ↑                         ↓
                    └──── Error handling ─────┘
```

## 5. Error handling

If APSIM fails:

- Send a graceful message to the farmer.
- Store the failed job for debugging.
- Notify administrator.
- Optionally return a cached advisory if available.

## 6. Human-in-the-loop option

For early deployment, suspicious recommendations should be flagged for agronomist review before being sent to farmers.
