# CropOracle Egypt Multi-Agent Architecture

This version upgrades CropOracle Egypt from one linear pipeline to a modular multi-agent advisory system.

## Agent roles

1. **Intake Agent**
   Parses the farmer WhatsApp message and extracts crop, location, farm area, sowing dates, climate scenario, irrigation and nitrogen options.

2. **Weather Agent**
   Selects the weather source and coordinates. In production it should generate APSIM `.met` files from NASA POWER, ERA5 or local Egyptian station data.

3. **Soil Agent**
   Selects an Egyptian soil profile by governorate or agroecological zone. It currently reads `apsim_templates/soil_profiles_egypt.json`.

4. **Simulation Agent**
   Builds scenario files and runs APSIM Next Gen. If APSIM is not installed, it returns deterministic demo outputs so the software can be tested.

5. **Validation Agent**
   Checks whether the request is inside the advisory domain, e.g. wheat-only, realistic climate perturbation, and available simulation outputs.

6. **Advisory Agent**
   Converts the simulation results into a farmer-ready WhatsApp answer in simple language.

## Recommended endpoint

Use:

```bash
POST /simulate-agent
```

Example JSON:

```json
{
  "phone": "demo",
  "message": "I am in Kafr El-Sheikh. Rainfall drops 20% and warming is 2 C. Should I sow wheat in November or December?"
}
```

## Optional LangGraph workflow

The file `app/agents/langgraph_workflow.py` provides the same workflow as LangGraph nodes. It is optional. The deterministic coordinator is recommended for the first production version because it is easier to debug with farmers.

## Production improvements

- Replace demo APSIM template with calibrated Egyptian wheat `.apsimx` files.
- Add NASA POWER/ERA5 downloader and APSIM `.met` writer.
- Add governorate-level soil calibration from SoilGrids and Egyptian soil surveys.
- Add Arabic dialect support for farmer questions.
- Add Redis/Celery queue for long APSIM jobs.
- Store every query, scenario, output, and recommendation in PostgreSQL.
- Add an agronomist review mode before deployment.
