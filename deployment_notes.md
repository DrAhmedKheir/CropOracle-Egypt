# Deployment Notes

## Local testing

Run:

```bash
python scripts/run_local_demo.py
python -m app.main
```

Then test direct simulation:

```bash
curl -X POST http://localhost:5000/simulate \
  -H "Content-Type: application/json" \
  -d '{"message":"I am in Nubaria with 3 feddan wheat. Rainfall decreases by 20% and warming 2 C. Best sowing date?"}'
```

## WhatsApp webhook

1. Create Meta developer app.
2. Add WhatsApp product.
3. Set callback URL:
   `https://your-domain.com/webhook/whatsapp`
4. Set verify token equal to `WHATSAPP_VERIFY_TOKEN` in `.env`.
5. Subscribe to messages webhook.
6. Add permanent access token and phone number ID to `.env`.

## APSIM deployment

Install APSIM Next Generation on the server and set:

```env
APSIM_EXE=/path/to/Models
```

On Windows, example:

```env
APSIM_EXE=C:/Program Files/APSIM2025/bin/Models.exe
```

## Production recommendations

- Put APSIM runs in a queue using Celery/RQ if simulations take more than 30 seconds.
- Cache common scenarios by location and sowing date.
- Store farmer questions and results in a database.
- Add bilingual Arabic/English replies.
- Add admin dashboard later for researchers and extension officers.
