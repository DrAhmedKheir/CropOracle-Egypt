# WhatsApp Deployment

## 1. Deployment options

CropOracle Egypt can connect to WhatsApp using either:

1. Meta WhatsApp Cloud API
2. Twilio WhatsApp Sandbox/API

For early testing, Twilio Sandbox is easier. For production, Meta WhatsApp Cloud API is recommended.

## 2. Webhook flow

```text
Farmer WhatsApp message
        ↓
WhatsApp Cloud API / Twilio
        ↓
Flask webhook: /webhook
        ↓
CropOracle multi-agent coordinator
        ↓
APSIM simulation
        ↓
WhatsApp reply
```

## 3. Webhook endpoint

The Flask application should expose:

```text
GET /webhook   # verification
POST /webhook  # incoming messages
```

## 4. Message template

Example Arabic response style:

```text
توصية CropOracle Egypt

الموقع: كفر الشيخ
المحصول: القمح
السيناريو: نقص الأمطار 20% وزيادة الحرارة 2 درجة مئوية

أفضل ميعاد زراعة: 15 نوفمبر
الإنتاج المتوقع: 6.4 طن/هكتار
نسبة الانخفاض المتوقعة: 8%

ننصح بتجنب الزراعة المتأخرة في 15 ديسمبر بسبب زيادة الإجهاد الحراري أثناء امتلاء الحبوب.
```

## 5. Security

Use:

- Webhook verification token
- HTTPS deployment
- Secure environment variables
- Rate limiting
- Farmer data anonymization

## 6. Production hosting options

Possible hosting options:

- Render
- Railway
- DigitalOcean
- AWS EC2
- Azure App Service
- Local institutional server with public HTTPS tunnel during testing

For APSIM, a Linux or Windows server with enough CPU resources is recommended.
