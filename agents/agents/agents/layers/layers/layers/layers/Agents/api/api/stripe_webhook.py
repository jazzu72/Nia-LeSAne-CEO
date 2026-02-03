from fastapi import APIRouter, Request, HTTPException
import stripe
import os

router = APIRouter()

STRIPE_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

@router.post("/stripe-webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_SECRET)
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        if session['metadata'].get('password') != os.getenv('NIA_SPECIAL_PASSWORD'):
            return {"status": "ignored"}
        # Record in vault (from vault.crypto)
        from vault.crypto import encrypt
        encrypted = encrypt(str(session))
        # Trigger tax ritual
        from niabrain.enhanced_brain import main as brain_main
        brain_main("New payment received - run tax ritual")

    return {"status": "success"}
