# API Design

## 1. Health check

```http
GET /health
```

Expected response:

```json
{
  "status": "ok",
  "service": "CropOracle Egypt"
}
```

## 2. WhatsApp webhook verification

```http
GET /webhook
```

Used by Meta WhatsApp Cloud API to verify the webhook.

## 3. Incoming WhatsApp message

```http
POST /webhook
```

Receives WhatsApp message payload.

## 4. Internal simulation endpoint, optional

```http
POST /simulate
```

Example body:

```json
{
  "location": "Kafr El-Sheikh",
  "crop": "wheat",
  "sowing_dates": ["2026-11-15", "2026-12-01", "2026-12-15"],
  "climate_scenario": {
    "rainfall_change_percent": -20,
    "temperature_increase_c": 2
  }
}
```

Expected response:

```json
{
  "best_option": "2026-11-15",
  "expected_yield_t_ha": 6.4,
  "message": "Plant around mid-November for more stable yield."
}
```
