# Technical Documentation

## 1. System overview

CropOracle Egypt is a backend service that receives farmer questions through WhatsApp, converts them into structured crop simulation scenarios, runs APSIM Next Gen, validates outputs, and returns an advisory message.

The system has four main layers:

1. Messaging layer: WhatsApp Cloud API or Twilio.
2. Application layer: Flask webhook and API routes.
3. Intelligence layer: multi-agent AI workflow.
4. Simulation layer: APSIM Next Generation and input/output processing.

## 2. Request lifecycle

A typical request follows this sequence:

1. Farmer sends WhatsApp message.
2. WhatsApp webhook sends payload to Flask endpoint.
3. Flask extracts sender ID and message text.
4. Intake Agent parses intent and required scenario details.
5. Weather Agent retrieves weather data and applies climate scenario.
6. Soil Agent selects or builds soil profile.
7. Simulation Agent prepares APSIM scenario files.
8. APSIM Next Gen runs simulations.
9. Results Parser extracts yield and stress indicators.
10. Validation Agent checks output consistency.
11. Advisory Agent prepares farmer-friendly response.
12. WhatsApp Client sends final message.

## 3. Core Python components

### `app/main.py`

Main Flask app. Handles webhook verification and incoming WhatsApp messages.

### `app/agents/coordinator.py`

Controls the workflow and passes shared state between agents.

### `app/services/apsim_runner.py`

Responsible for APSIM file preparation, command-line execution, and output collection.

### `app/services/weather_engine.py`

Handles weather retrieval and climate perturbation, such as rainfall reduction or temperature increase.

### `app/services/advisory_generator.py`

Converts simulation output into a clear advisory message.

## 4. Configuration

Configuration is controlled through `.env` variables. See `.env.example`.

Important variables:

```text
APSIM_EXE_PATH=/path/to/Models.exe
WHATSAPP_TOKEN=your_token
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
VERIFY_TOKEN=your_webhook_verify_token
LLM_PROVIDER=openai_or_anthropic
LLM_API_KEY=your_key
```

## 5. APSIM execution

APSIM Next Gen can be run from command line. The Simulation Agent should:

1. Copy the base wheat `.apsimx` template.
2. Modify sowing date, cultivar, soil, weather file, irrigation, nitrogen, and climate scenario.
3. Run APSIM executable.
4. Read the generated SQLite or CSV output.
5. Return summary statistics.

Recommended output indicators:

- Grain yield, kg/ha or t/ha
- Biomass
- Flowering date
- Maturity date
- Water stress index
- Nitrogen stress index
- Soil water at sowing
- Seasonal evapotranspiration
- Water productivity

## 6. Production considerations

For real deployment, add:

- Queue system: Celery or RQ
- Redis cache
- PostgreSQL database
- User/session storage
- APSIM job status tracking
- Input validation
- Logging and monitoring
- Farmer privacy protection
- Arabic language support
- Voice-to-text support for WhatsApp audio messages

## 7. Testing strategy

Start with three levels of testing:

1. Unit tests for scenario parsing.
2. Integration tests for APSIM execution.
3. End-to-end test using WhatsApp sandbox.

## 8. Minimum viable product

A strong MVP can be limited to:

- One crop: wheat
- Three regions: Nile Delta, Middle Egypt, Upper Egypt
- Three sowing dates
- Three climate scenarios
- One calibrated APSIM wheat template
- WhatsApp text messages only
