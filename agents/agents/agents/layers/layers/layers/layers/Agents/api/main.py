from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
import os
from api.stripe_webhook import stripe_router
from api.telegram_webhook import telegram_router
from niabrain.enhanced_brain import main as brain_main

load_dotenv()

app = FastAPI(title="Nia LeSane CEO API")

app.include_router(stripe_router)
app.include_router(telegram_router)

@app.post("/invoke")
async def invoke(request: Request):
    data = await request.json()
    if data.get('password') != os.getenv('NIA_SPECIAL_PASSWORD'):
        raise HTTPException(status_code=401, detail="Unauthorized")
    invocation = data.get('invocation', 'Default invocation')
    brain_main(invocation)
    return {"status": "success", "message": "Ritual launched"}

@app.get("/")
def root():
    return {"message": "Nia LeSane CEO - House of Jazzu"}
