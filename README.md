# CropOracle Egypt

**CropOracle Egypt** is a WhatsApp-based, multi-agent AI decision-support system that connects Egyptian wheat farmers to real crop simulation workflows using **APSIM Next Generation**.

A farmer sends one message on WhatsApp, for example:

> I am in Kafr El-Sheikh. What if rainfall decreases 20% and temperature increases 2°C? Should I sow wheat on 15 Nov, 1 Dec, or 15 Dec?

The system interprets the question, prepares APSIM scenarios, runs crop simulations, validates the outputs, and sends a farmer-friendly advisory reply through WhatsApp.

![CropOracle Egypt multi-agent workflow](docs/figures/croporacle_egypt_multiagent_workflow.png)

---

## Main objective

To provide smallholder and commercial wheat farmers in Egypt with fast, science-based, location-specific crop advice through WhatsApp, without requiring a mobile app, agronomic training, or direct access to crop modeling software.

---

## Core capabilities

CropOracle Egypt is designed to support:

- Wheat sowing-date comparison
- Climate-change scenarios, including rainfall reduction and warming
- Irrigation strategy comparison
- Nitrogen fertilizer scenario comparison
- Soil-specific simulation using Egyptian soil profiles
- Governorate-specific advisory messages
- Arabic and English farmer replies
- APSIM Next Gen simulation orchestration
- Multi-agent AI workflow using Python and optional LangGraph

---

## Multi-agent architecture

The system is organized as a coordinated group of agents:

| Agent | Role |
|---|---|
| Intake Agent | Understands the farmer message and extracts intent, location, crop, dates, and scenario details |
| Weather Agent | Retrieves or prepares weather data and applies climate-change perturbations |
| Soil Agent | Selects the soil profile for the farmer location |
| APSIM Simulation Agent | Builds and runs APSIM Next Gen scenario files |
| Validation Agent | Checks simulation quality, missing outputs, and outliers |
| Advisory Agent | Converts model outputs into clear farmer recommendations |
| Coordinator | Manages workflow state, memory, and routing between agents |

---

## Expected response time

For a practical farmer-facing service:

| Workflow type | Expected time |
|---|---:|
| Simple query, 3 sowing dates × 5 weather years | 1–3 minutes |
| Moderate query, sowing × irrigation × fertilizer | 3–8 minutes |
| Heavy research query, many locations and 20–30 weather years | 10–30 minutes |
| Precomputed advisory lookup | less than 30 seconds |

Recommended operational design:

- **Fast advisory mode:** use precomputed or small scenario batches for farmers.
- **Research mode:** run larger APSIM scenario ensembles asynchronously for scientists and project teams.

---

## Technology stack

- **Python / Flask**: backend API and webhook service
- **APSIM Next Generation**: crop simulation engine
- **WhatsApp Cloud API or Twilio**: farmer messaging interface
- **LLM planner**: natural-language interpretation and scenario planning
- **LangGraph / CrewAI-compatible structure**: optional agent orchestration
- **NASA POWER / ERA5 / local station data**: weather inputs
- **SoilGrids / Egyptian soil profiles / field observations**: soil inputs
- **SQLite / CSV outputs**: APSIM simulation results

---

## Project structure

```text
CropOracle-Egypt/
├── app/
│   ├── agents/                  # Multi-agent workflow components
│   ├── services/                # APSIM, weather, WhatsApp, advisory services
│   ├── templates/               # Prompt and reply templates
│   ├── config.py
│   └── main.py                  # Flask application and WhatsApp webhook
├── apsim_templates/             # Egypt wheat APSIM templates and soil/cultivar metadata
├── docs/                        # Full technical documentation
│   └── figures/
├── scripts/                     # Local demos and tests
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CropOracle-Egypt.git
cd CropOracle-Egypt
```

### 2. Create Python environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your API keys and APSIM executable path.

### 4. Run local demo

```bash
python scripts/run_multiagent_demo.py
```

### 5. Run Flask service

```bash
flask --app app.main run --host 0.0.0.0 --port 8000
```

---

## WhatsApp deployment concept

1. Farmer sends message to WhatsApp number.
2. WhatsApp webhook forwards the message to Flask.
3. Flask calls the CropOracle multi-agent coordinator.
4. Agents build APSIM scenario files and run simulations.
5. Advisory Agent prepares Arabic/English recommendation.
6. WhatsApp API sends answer back to the farmer.

---

## Example farmer answer

```text
CropOracle Egypt recommendation

Location: Kafr El-Sheikh
Crop: Wheat
Scenario: rainfall -20%, temperature +2°C

Best sowing date: 15 November
Expected yield: 6.4 t/ha
Yield loss under climate stress: 8%

Avoid late sowing on 15 December because simulated heat stress during grain filling reduced yield to 5.1 t/ha.

Recommendation: Plant around mid-November and maintain timely irrigation during tillering and grain filling.
```

---

## Documentation

See:

- [`docs/GITHUB_UPLOAD_GUIDE.md`](docs/GITHUB_UPLOAD_GUIDE.md)
- [`docs/TECHNICAL_DOCUMENTATION.md`](docs/TECHNICAL_DOCUMENTATION.md)
- [`docs/EGYPT_WHEAT_SIMULATION_WORKFLOW.md`](docs/EGYPT_WHEAT_SIMULATION_WORKFLOW.md)
- [`docs/MULTI_AGENT_DESIGN.md`](docs/MULTI_AGENT_DESIGN.md)
- [`docs/WHATSAPP_DEPLOYMENT.md`](docs/WHATSAPP_DEPLOYMENT.md)
- [`docs/RESPONSE_TIME_AND_SCALING.md`](docs/RESPONSE_TIME_AND_SCALING.md)

---

## Development status

This repository is a strong starter framework. Before real farmer deployment, the following must be completed:

- Calibrate APSIM wheat cultivars for Egyptian environments
- Validate soil profiles using field/local datasets
- Connect verified weather sources
- Test WhatsApp webhook with Meta/Twilio
- Validate model outputs against observed wheat yield data
- Add robust safety rules for farmer recommendations
- Add Arabic localization and voice-message support

---

## Suggested repository description

> WhatsApp-based multi-agent AI system for APSIM Next Gen wheat simulations and climate-smart advisory services for Egyptian farmers.

---

## License

MIT License. See `LICENSE`.
