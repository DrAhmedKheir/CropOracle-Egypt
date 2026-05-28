# CropOracle Egypt — Google Cloud End-to-End Deployment

## Overview

This guide deploys CropOracle Egypt on Google Cloud Run using:

- Flask API
- APSIM Next Gen orchestration
- LangChain / LangGraph multi-agent AI
- WhatsApp Cloud API
- Docker containers
- Google Secret Manager
- Google Artifact Registry
- Google Cloud Build

---

# Architecture

Farmer WhatsApp
↓
Meta WhatsApp Cloud API
↓
Flask Webhook
↓
Multi-Agent AI Coordinator
↓
Weather + Soil + APSIM Agents
↓
APSIM Next Gen Simulation
↓
Advisory Agent
↓
WhatsApp Response

---

# 1. Install Google Cloud SDK

Download:

https://cloud.google.com/sdk/docs/install

Verify installation:

```bash
gcloud --version
```

---

# 2. Create Google Cloud Project

```bash
gcloud projects create croporacle-egypt-001
```

Set active project:

```bash
gcloud config set project croporacle-egypt-001
```

---

# 3. Enable APIs

```bash
gcloud services enable \
run.googleapis.com \
cloudbuild.googleapis.com \
artifactregistry.googleapis.com \
secretmanager.googleapis.com
```

---

# 4. Create Artifact Registry

```bash
gcloud artifacts repositories create croporacle-egypt-repo \
--repository-format=docker \
--location=europe-west1
```

---

# 5. Configure Docker Authentication

```bash
gcloud auth configure-docker europe-west1-docker.pkg.dev
```

---

# 6. Create Secrets

## LLM API Key

```bash
echo -n "YOUR_API_KEY" | \
gcloud secrets create LLM_API_KEY --data-file=-
```

## WhatsApp Access Token

```bash
echo -n "YOUR_WHATSAPP_TOKEN" | \
gcloud secrets create WHATSAPP_ACCESS_TOKEN --data-file=-
```

---

# 7. Dockerfile

Create Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080

CMD exec gunicorn --bind :$PORT app.main:app
```

---

# 8. Build Container

```bash
gcloud builds submit \
--tag europe-west1-docker.pkg.dev/croporacle-egypt-001/croporacle-egypt-repo/croporacle-api
```

---

# 9. Deploy to Cloud Run

```bash
gcloud run deploy croporacle-egypt \
--image europe-west1-docker.pkg.dev/croporacle-egypt-001/croporacle-egypt-repo/croporacle-api \
--platform managed \
--region europe-west1 \
--allow-unauthenticated \
--memory 4Gi \
--cpu 2 \
--timeout 900
```

---

# 10. Configure WhatsApp Webhook

Webhook URL:

```text
https://YOUR_CLOUD_RUN_URL/webhook
```

Configure inside:

Meta Developers Console → WhatsApp → Webhooks

---

# 11. APSIM Next Gen Integration

## Option 1 — Mock Mode

Use simulated APSIM outputs during testing.

## Option 2 — Full APSIM Worker

Deploy APSIM on:

- Compute Engine VM
- Kubernetes worker
- HPC cluster

Cloud Run sends jobs to APSIM worker queue.

---

# 12. Scaling

Expected response time:

| Workflow | Time |
|---|---|
| Simple advisory | 1–3 min |
| Multi-scenario APSIM | 5–15 min |
| Large climate ensemble | 30+ min |

---

# 13. Future Improvements

- Arabic NLP
- Voice WhatsApp support
- Farmer memory profiles
- Climate forecasting integration
- Satellite data ingestion
- DSS dashboard
- National-scale APSIM grids

---

# 14. Recommended Production Stack

| Component | Technology |
|---|---|
| Messaging | WhatsApp Cloud API |
| Backend | Flask |
| AI Agents | LangGraph |
| Crop Model | APSIM Next Gen |
| Database | PostgreSQL |
| Queue | Redis + Celery |
| Hosting | Google Cloud Run |
| Storage | Google Cloud Storage |
| Secrets | Secret Manager |

---

# 15. Authors

Prof. Dr. Ahmed Kheir  
Crop Modeling • AI • Climate-Smart Agriculture
