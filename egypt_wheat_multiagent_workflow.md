# Egypt Wheat Workflow with Multi-Agent AI

## Step 1. Farmer message

A farmer sends a WhatsApp message, for example:

> I am in Nubaria. My farm is 10 feddan. What happens if temperature increases by 2 degrees? Should I sow wheat on 15 Nov, 1 Dec, or 15 Dec?

## Step 2. Intake Agent

The message is converted into a structured `FarmerScenario` object.

## Step 3. Weather Agent

The system selects coordinates and prepares weather data. For Egypt, start with governorate centroids, then improve to village-level coordinates.

## Step 4. Soil Agent

The system selects soil data. For early deployment, use calibrated representative soil profiles for:

- Nile Delta clay soils
- New lands sandy soils
- Middle Egypt alluvial soils
- Upper Egypt alluvial soils

## Step 5. Simulation Agent

APSIM Next Gen runs combinations of:

- sowing dates
- nitrogen levels
- irrigation levels
- climate perturbations

## Step 6. Validation Agent

The system checks the reliability domain and attaches warnings when needed.

## Step 7. Advisory Agent

The answer is returned through WhatsApp as a short recommendation, not a scientific report.

## Strong first pilot

Recommended pilot domain:

- Crop: wheat
- Locations: Kafr El-Sheikh, Dakahlia, Nubaria, Minya
- Scenarios: sowing date, irrigation amount, nitrogen rate, heat stress
- Language: Arabic + English
