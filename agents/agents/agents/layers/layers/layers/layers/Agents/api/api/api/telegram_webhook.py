from fastapi import APIRouter, Request
import os
import requests

router = APIRouter()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

@router.post("/telegram-webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    message = data.get('message', {})
    text = message.get('text', '')

    if message.get('chat', {}).get('id') != int(CHAT_ID):
        return {"status": "ignored"}

    if text.startswith('invoke '):
        invocation = text[7:].strip()
        # Trigger brain
        from niabrain.enhanced_brain import main as brain_main
        brain_main(invocation)
        send_telegram("Ritual launched: " + invocation)

    return {"status": "success"}

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, json=payload)
