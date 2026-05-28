from __future__ import annotations
import requests
from app.config import settings


def send_whatsapp_text(to_phone: str, message: str) -> dict:
    """Send message using WhatsApp Cloud API."""
    if not settings.WHATSAPP_PHONE_NUMBER_ID or not settings.WHATSAPP_ACCESS_TOKEN:
        print('WHATSAPP MOCK SEND:', to_phone, message)
        return {'status': 'mock', 'to': to_phone, 'message': message}

    url = f"https://graph.facebook.com/v20.0/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        'Authorization': f'Bearer {settings.WHATSAPP_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    payload = {
        'messaging_product': 'whatsapp',
        'to': to_phone,
        'type': 'text',
        'text': {'body': message}
    }
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()
